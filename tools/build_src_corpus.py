#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把仓库里【已公开】的原文文本抽成可检索的段落语料：01_corpus_src/src_paragraphs.jsonl

只读本仓 git 跟踪的文本文件，不引入任何新的原文摘录：
  - 08_source_code/*/工程文件/work/full.txt（按 ===== PAGE n ===== 分页）
  - 08_source_code/*/工程文件/work/split/pNNN.txt（每文件一页）
  - 05_seminar_witten/seminars/*/source/text/pNNN.txt
  - 08_source_code/*/工程文件/work/原文/*（逐文件一段）

输出每行：
  {"pkg","file","page","seg","lang","text","chars"}
    pkg   工程号（SY01-13 / SEM-9407087 / SY02-10 …）
    page  原文页码（无分页信息时为 null）
    seg   同一页内的段序号
    lang  ja / en / zh / other（按字符集启发式判定）
    text  段落正文（已去页眉页脚重复行、去空白与页码行）

用法：
  python tools/build_src_corpus.py            # 写出 jsonl 并打印统计
  python tools/build_src_corpus.py --dry-run  # 只统计，不写文件
"""
import io
import gzip
import hashlib
import json
import os
import re
import subprocess
import sys
import collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "01_corpus_src")
OUT = os.path.join(OUT_DIR, "src_paragraphs.jsonl")

PAGE_RE = re.compile(
    r"^\s*%?\s*=+\s*(?:(?:PDF|BOOK)\s+)?(?:PAGE|p\.)\s*([A-Za-z]{0,6}-?\d+)\b[^=]*=+\s*$", re.I
)
MARKER_LEFT = re.compile(r"=+\s*(?:(?:PDF|BOOK)\s+)?(?:PAGE|p\.)\s*\d+", re.I)
# 行内页标记：`% PDF p.3 (printed 2) 正文…` —— 标记与正文在同一行
INLINE_MARK = re.compile(
    r"^\s*%?\s*(?:=+\s*)?(?:(?:PDF|BOOK)\s+)?(?:PAGE|p\.)\s*([A-Za-z]{0,6}-?\d+)(?:\s*\([^)]{0,20}\))?\s*(?:=+\s*)?", re.I
)
CJK = re.compile(r"[\u4e00-\u9fff]")
KANA = re.compile(r"[\u3040-\u30ff]")
LATIN = re.compile(r"[A-Za-z]")
PAGENUM_LINE = re.compile(r"^\s*[-–—]?\s*\d{1,4}\s*[-–—]?\s*$")


def tracked(pattern=None):
    cmd = ["git", "ls-files"] + ([pattern] if pattern else [])
    out = subprocess.run(cmd, capture_output=True, cwd=ROOT).stdout
    return out.decode("utf-8", "replace").splitlines()


def pkg_of(path):
    parts = path.split("/")
    if parts[0] == "08_source_code" and len(parts) > 1:
        m = re.match(r"(SY\d{2}-\d{2}|SEM-[\w-]+)", parts[1])
        return m.group(1) if m else parts[1].split("_")[0]
    if parts[0] == "03_translations_meta" and len(parts) > 1:
        return parts[1]
    if parts[0] == "05_seminar_witten":
        for p in parts:
            if p.startswith("SEM-") or p.startswith("SEM_"):
                return p
    return parts[1] if len(parts) > 1 else parts[0]


def lang_of(text):
    kana = len(KANA.findall(text))
    cjk = len(CJK.findall(text))
    latin = len(LATIN.findall(text))
    if kana > max(8, 0.02 * len(text)):
        return "ja"
    if cjk > max(8, 0.18 * len(text)):
        return "zh"
    if latin > 0.25 * len(text):
        return "en"
    return "other"


def clean_paras(text):
    """去页码行、去重复页眉页脚、按空行切段。"""
    lines = [ln.rstrip() for ln in text.replace("\r\n", "\n").split("\n")]
    counts = collections.Counter(ln.strip() for ln in lines if ln.strip())
    out_lines = []
    for ln in lines:
        s = ln.strip()
        if not s:
            out_lines.append("")
            continue
        if PAGENUM_LINE.match(s):
            continue
        if MARKER_LEFT.search(s) or re.match(r"^\s*%?\s*=+\s*$", s):
            continue                            # 页标记行（含格式变体）不进正文
        if counts[s] > 3 and len(s) < 80:      # 跨页重复的页眉/页脚
            continue
        out_lines.append(s)
    paras = []
    for chunk in "\n".join(out_lines).split("\n\n"):
        p = " ".join(x.strip() for x in chunk.split("\n") if x.strip()).strip()
        if not p:
            continue
        if len(p) < 20 and not re.search(r"[=<>$]", p):
            continue
        paras.extend(split_long(re.sub(r"[ \t]{2,}", " ", p)))
    return paras


SENT_END = re.compile(r"(?<=[。．！？!?;；])\s*|(?<=[.])\s+(?=[A-Z(\\$])")


def split_long(p, limit=1100, target=850):
    """超长段落（常见于无空行分段的讲义）按句子切成 ~850 字的块。"""
    if len(p) <= limit:
        return [p]
    parts = [s for s in SENT_END.split(p) if s]
    out, buf = [], ""
    for s in parts:
        if len(buf) + len(s) <= target:
            buf += s
            continue
        if buf.strip():
            out.append(buf.strip())
        buf = s
    if buf.strip():
        out.append(buf.strip())
    return out


def _page_of(num):
    """页码归一：负数（书前罗马页/封面页）记 None，不进检索的页过滤。"""
    try:
        n = int(num)
    except (TypeError, ValueError):
        return None
    return n if n >= 0 else None


def parse_file(path):
    """返回 [(page|None, [para, ...]), ...]"""
    raw = io.open(os.path.join(ROOT, path), encoding="utf-8", errors="replace").read()
    lines = raw.replace("\r\n", "\n").split("\n")
    blocks, cur_page, cur = [], None, []
    for ln in lines:
        m = PAGE_RE.match(ln)
        if m:
            blocks.append((cur_page, cur))
            cur_page, cur = _page_of(m.group(1)), []
            continue
        mi = INLINE_MARK.match(ln)
        if mi:
            # 页标记（可能与正文同行）：换页，剩下的当正文
            rest = ln[mi.end():].strip()
            blocks.append((cur_page, cur))
            cur_page, cur = _page_of(mi.group(1)), ([rest] if rest else [])
            continue
        cur.append(ln)
    blocks.append((cur_page, cur))
    # 单文件多页的信息（split/pNNN.txt）从文件名取；此时把残留页标记行去掉
    if all(p is None for p, _ in blocks):
        m = re.search(r"p(\d{3})\.txt$", path)
        body = []
        for ln in lines:
            mi = INLINE_MARK.match(ln)
            if PAGE_RE.match(ln):
                continue
            if mi:
                rest = ln[mi.end():].strip()
                if rest:
                    body.append(rest)
                continue
            body.append(ln)
        blocks = [(int(m.group(1)) if m else None, body)]
    return [(p, clean_paras("\n".join(body))) for p, body in blocks]


def collect():
    files = []
    files += [f for f in tracked() if f.endswith("/work/full.txt") or f.endswith("/工程文件/full.txt")]
    files += [f for f in tracked() if re.search(r"/(work/split|source/text)/p\d{3}\.txt$", f)]
    files += [f for f in tracked() if "/work/原文/" in f and f.endswith((".txt", ".md"))]
    files = sorted(set(files))
    # 同一工程若已有 full.txt，就不要再扫它的 split/pNNN.txt（内容是同一份，只是切法不同）
    full_pkgs = {pkg_of(f) for f in files if f.endswith("full.txt")}
    files = [
        f for f in files
        if f.endswith("full.txt") or pkg_of(f) not in full_pkgs
    ]

    rows, seen = [], set()
    for f in files:
        pkg = pkg_of(f)
        for page, paras in parse_file(f):
            for i, p in enumerate(paras):
                h = hashlib.sha1(p.encode("utf-8")).hexdigest()[:16]
                key = (pkg, h)
                if key in seen:
                    continue
                seen.add(key)
                rows.append({
                    "pkg": pkg,
                    "file": f,
                    "page": page,
                    "seg": i,
                    "lang": lang_of(p),
                    "text": p,
                    "chars": len(p),
                })
    return files, rows


def main():
    files, rows = collect()
    pkgs = sorted({r["pkg"] for r in rows})
    langs = collections.Counter(r["lang"] for r in rows)
    chars = sum(r["chars"] for r in rows)
    paginated = sum(1 for r in rows if r["page"] is not None)
    print("files=%d projects=%d paragraphs=%d chars=%d paginated=%d(%.0f%%)"
          % (len(files), len(pkgs), len(rows), chars, paginated, 100.0 * paginated / max(1, len(rows))))
    print("langs:", dict(langs))
    print("projects:", ", ".join(pkgs))
    if "--dry-run" in sys.argv:
        return
    os.makedirs(OUT_DIR, exist_ok=True)
    with io.open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print("->", os.path.relpath(OUT, ROOT), "%.1f MB" % (os.path.getsize(OUT) / 1048576.0))
    write_plugin_gz(rows)


def write_plugin_gz(rows):
    """插件随包数据：plugins/dsh-kb/data/src/src_paragraphs.jsonl.gz（离线检索用）"""
    dst_dir = os.path.join(ROOT, "plugins", "dsh-kb", "data", "src")
    os.makedirs(dst_dir, exist_ok=True)
    dst = os.path.join(dst_dir, "src_paragraphs.jsonl.gz")
    with io.open(dst, "wb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw, compresslevel=9, mtime=0) as gz:
            for r in rows:
                gz.write((json.dumps(r, ensure_ascii=False) + "\n").encode("utf-8"))
    print("->", os.path.relpath(dst, ROOT), "%.2f MB gz" % (os.path.getsize(dst) / 1048576.0))


if __name__ == "__main__":
    main()
