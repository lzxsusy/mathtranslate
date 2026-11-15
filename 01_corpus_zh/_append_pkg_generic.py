# -*- coding: utf-8 -*-
r"""把「有译文但没进语料」的工程补进 01_corpus_zh（通用版，2026-11-15）。

背景：`_append_pkg.py` 只服务 SY01-23 一个包（按 `\SourceParagraph` 锚点切段）；
v2 抽取器没有随仓库发布，所以另外 10 部有完整译文的工程一直没进 `zh_paragraphs.jsonl`
（合计 470,060 汉字 = 原语料的 12.8%）。本脚本用同一套清洗函数（`_tex_clean` +
`_build_corpus_v3` 的残渣清洗/公式修复）做**通用抽取**，只追加、不改已有行。

抽取口径（写进每行的 `seg` 字段，便于复核）：
- `seg="anchor"`：源文件含 `\SourceParagraph{id}{页号}` 锚点，按锚点切段并带 page_orig；
- `seg="blank"`：没有锚点，按空行切段（与 v2 抽取器同口径），page_orig 留空。

文件选择：优先 `chunks/`、`sections/`、`chapters/`、`sec/`、`body/`（递归），
外加顶层 `sec*/chapter*/part*/appendix*/abstract*/lecture*` 的 .tex；
一律跳过 `main/preamble/refs/translator_note` 与 `_` 开头的临时文件（模板与目录残渣的来源）。

用法：
    python _append_pkg_generic.py                    # 只统计 + 抽样，不写盘
    python _append_pkg_generic.py --write            # 追加并刷新 stats
    python _append_pkg_generic.py --pkgs SY08-01,SY07-08 --write
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import io
import json
import os
import re
import shutil
import sys
import time

sys.stdout.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from _tex_clean import expand as _expand, strip_unbalanced_braces as _strip  # noqa: E402
from _append_pkg import paragraphs_of_segment, is_content  # noqa: E402
from _build_corpus_v3 import clean_junk, repair_math  # noqa: E402

CORPUS = os.path.join(HERE, "zh_paragraphs.jsonl")
STATS = os.path.join(HERE, "zh_paragraphs_stats.json")
SRC_ROOT = os.path.join(REPO, "08_source_code")
ZH = re.compile(r"[\u4e00-\u9fff]")
ANCHOR = re.compile(r"\\SourceParagraph\{([^}]*)\}\{(\d+)\}")

CONTENT_DIRS = ("chunks", "sections", "chapters", "sec", "body", "text")
SKIP_NAMES = {"main", "preamble", "refs", "translator_note", "macros", "commands"}
LOOSE = re.compile(r"^(?:sec|chapter|part|appendix|abstract|lecture)\w*\.tex$", re.I)

# 术语表/索引/符号表整章：是术语资源，不是正文散文，不进语料
SKIP_FILE_RX = re.compile(r"(术语|glossary|index|索引|符号表)", re.I)
GLOSS_BODY = re.compile(
    r"英中术语对照|术语对照表|术语表|本表收录|英中术语|汉英术语|符号表|"
    r"按英文条目的字母序|按中文条目的拼音序")

# 通用抽取要多做三步清理（v2 抽取器本来就会做，这里补上）：
#   1. 去掉所有 \begin{env}/\end{env}（不止白名单里的那几种）；
#   2. 连组删掉章节命令（\section{…} 之类，与既有语料「标题行不入库」的口径一致）；
#   3. 去掉字号/居中声明，如 {\small …}、\centering、\noindent。
ENV_ANY = re.compile(r"\\(?:begin|end)\{[^{}]*\}(?:\[[^\]]*\])?")
HEADING = re.compile(
    r"\\(?:chapter|section|subsection|subsubsection|paragraph|part|subparagraph)\*?"
    r"\s*(?:\[[^\]]*\])?\s*\{")
DECL = re.compile(
    r"\\(?:small|footnotesize|scriptsize|tiny|normalsize|large|Large|LARGE|huge|Huge|"
    r"bfseries|itshape|slshape|scshape|rmfamily|sffamily|ttfamily|centering|noindent|indent|"
    r"flushright|flushleft|raggedright|par)\b")
LATIN = re.compile(r"[A-Za-z]")

EN_MIN_RATIO = 0.35     # 汉字占比低于此且汉字 <20 的段判为「英文原文没译」
EN_MIN_ZH = 20


def strip_headings(t: str) -> str:
    """连组删掉 `\\section{…}` 这类命令（保留命令之后的正文）。"""
    while True:
        m = HEADING.search(t)
        if not m:
            return t
        i = m.end() - 1
        depth, j = 0, i
        while j < len(t):
            c = t[j]
            if c == "\\":
                j += 2
                continue
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    j += 1
                    break
            j += 1
        t = (t[:m.start()] + " " + t[j:]).strip()


def post_clean(t: str) -> str:
    t = strip_headings(t)
    t = ENV_ANY.sub("", t)
    t = DECL.sub("", t)
    t = t.replace("\\item", " ")
    t = re.sub(r"\\cite[a-z]*\{([^}]*)\}", r"[\1]", t)
    # 只剩纯文字的裸花括号组，如 {同调镜像对称（HMS）}。
    # 必须排除「紧跟命令名」的花括号：`\mathcal{F}` 的 `{F}` 不是裸组，剥掉会变成 `\mathcalF`（坏命令）。
    t = re.sub(r"(?<![A-Za-z])\{([^{}$\\]*)\}", r"\1", t)
    t = re.sub(r"\{\s*\}", "", t)
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


TIKZ = re.compile(r"\\(?:node|draw|path|fill|coordinate|matrix)\b")
BYLINE = re.compile(r"^\S{1,12}\\\\\s*\S{2,30}$|^\S{1,12}\\\\")


def is_garbage(t: str) -> bool:
    """tikz 图元漏出来、纯作者署名行——都不是正文散文。"""
    if TIKZ.search(t):
        return True
    s = t.strip()
    if len(ZH.findall(s)) < 15 and "。" not in s and ("\\\\" in s or s.count("\n") == 0 and len(s) < 22):
        return True
    return False


def is_translated(t: str) -> bool:
    zh = len(ZH.findall(t))
    lat = len(LATIN.findall(t))
    if zh == 0:
        return False
    if zh < EN_MIN_ZH and lat > 3 * max(1, zh):
        return False
    return zh / (zh + lat) >= EN_MIN_RATIO or zh >= 60


def pick_files(pkg_dir: str) -> list[str]:
    src = os.path.join(pkg_dir, "源码")
    out: list[str] = []
    for sub in CONTENT_DIRS:
        d = os.path.join(src, sub)
        if os.path.isdir(d):
            out += sorted(glob.glob(os.path.join(d, "**", "*.tex"), recursive=True))
    out += sorted(p for p in glob.glob(os.path.join(src, "*.tex"))
                  if LOOSE.match(os.path.basename(p)))
    keep = []
    for p in out:
        b = os.path.splitext(os.path.basename(p))[0]
        if b in SKIP_NAMES or b.startswith("_"):
            continue
        if SKIP_FILE_RX.search(b):
            continue
        if p not in keep:
            keep.append(p)
    if not keep:      # 兜底：结构不合惯例的工程，取 源码/ 下全部 .tex（去掉模板）
        for p in sorted(glob.glob(os.path.join(src, "**", "*.tex"), recursive=True)):
            b = os.path.splitext(os.path.basename(p))[0]
            if b in SKIP_NAMES or b.startswith("_") or SKIP_FILE_RX.search(b):
                continue
            keep.append(p)
    return keep


def rows_of_file(pkg: str, fp: str) -> tuple[list[dict], str]:
    rel = pkg + "/" + os.path.relpath(fp, os.path.dirname(os.path.dirname(fp))).replace("\\", "/")
    src = io.open(fp, encoding="utf-8", errors="replace").read()
    seg_method = "blank"
    items = []          # [(page, text)]
    if ANCHOR.search(src):
        seg_method = "anchor"
        parts = ANCHOR.split(src)
        if parts[0].strip():
            items.append((None, parts[0]))
        for i in range(1, len(parts), 3):
            items.append((int(parts[i + 1]), parts[i + 2]))
    else:
        items.append((None, src))

    rows = []
    idx = 0
    for page, seg in items:
        for t, env in paragraphs_of_segment(seg):
            t = post_clean(t)
            t, cleaned = clean_junk(t)
            t, mflags = repair_math(t)
            if cleaned:
                mflags = sorted(set(mflags) | {"junk_trimmed"})
            if not is_content(t) or not is_translated(t) or GLOSS_BODY.search(t) or is_garbage(t):
                continue
            idx += 1
            t = t.replace("<本地路径>", "\\\\")     # 与 _repair_2026-11-15.py 同口径
            rec = {
                "pkg": pkg,
                "file": rel,
                "para": idx,
                "para_id": hashlib.sha1(t.encode("utf-8")).hexdigest()[:16],
                "page_orig": page,
                "env": env,
                "tier": "B",
                "text": t,
                "zh_chars": len(ZH.findall(t)),
                "seg": seg_method,
            }
            if mflags:
                rec["flags"] = mflags
            rows.append(rec)
    return rows, seg_method


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--pkgs", default="", help="逗号分隔；空=自动取全部缺口工程")
    args = ap.parse_args()

    rows = [json.loads(l) for l in io.open(CORPUS, encoding="utf-8") if l.strip()]
    have = {d["pkg"] for d in rows}
    seen_text = {d["text"].strip() for d in rows}

    dirs = {}
    for d in sorted(os.listdir(SRC_ROOT)):
        p = os.path.join(SRC_ROOT, d)
        if not os.path.isdir(p) or not os.path.isdir(os.path.join(p, "源码")):
            continue
        dirs[d.split("_")[0]] = p

    if args.pkgs:
        targets = [x.strip() for x in args.pkgs.split(",") if x.strip()]
    else:
        targets = sorted(k for k in dirs if k not in have)

    print("corpus pkg: %d | 有源码工程: %d | 本次补: %d -> %s"
          % (len(have), len(dirs), len(targets), ",".join(targets)))

    new_rows = []
    for pkg in targets:
        p = dirs.get(pkg)
        if not p:
            print("  !! %s 找不到源码目录，跳过" % pkg)
            continue
        files = pick_files(p)
        got, dup, methods = 0, 0, set()
        for fp in files:
            rs, m = rows_of_file(pkg, fp)
            methods.add(m)
            for r in rs:
                if r["text"].strip() in seen_text:
                    dup += 1
                    continue
                seen_text.add(r["text"].strip())
                new_rows.append(r)
                got += 1
        hz = sum(r["zh_chars"] for r in new_rows if r["pkg"] == pkg)
        print("  %-8s files=%-3d rows=%-5d 汉字=%-7d dup_skipped=%-4d seg=%s"
              % (pkg, len(files), got, hz, dup, "/".join(sorted(methods))))

    tot_hz = sum(r["zh_chars"] for r in new_rows)
    print("\n新增 %d 段 / %d 汉字（占原语料 %.1f%%）"
          % (len(new_rows), tot_hz, 100.0 * tot_hz / max(1, sum(d["zh_chars"] or 0 for d in rows))))

    print("\n--- 抽样（每包 2 段）---")
    shown = {}
    for r in new_rows:
        if shown.get(r["pkg"], 0) >= 2:
            continue
        shown[r["pkg"]] = shown.get(r["pkg"], 0) + 1
        print("[%s] %s" % (r["pkg"], r["text"][:150].replace("\n", " ")))

    if not args.write:
        print("\n[dry-run] 未写盘")
        return

    stamp = time.strftime("%Y%m%d-%H%M%S")
    bak = os.path.join(os.path.dirname(REPO), "_corpus_backups", "append_%s" % stamp)
    os.makedirs(bak, exist_ok=True)
    shutil.copy2(CORPUS, os.path.join(bak, os.path.basename(CORPUS)))
    print("backup ->", os.path.relpath(bak, REPO))

    with io.open(CORPUS, "a", encoding="utf-8", newline="\n") as f:
        for r in new_rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    rows += new_rows
    st = json.load(io.open(STATS, encoding="utf-8"))
    fc: dict[str, int] = {}
    for r in rows:
        for x in (r.get("flags") or []):
            fc[x] = fc.get(x, 0) + 1
    st.update({
        "total": len(rows),
        "with_math": sum(1 for d in rows if "$" in d["text"] or "\\begin{" in d["text"]),
        "exact_dup_flagged": sum(1 for d in rows if d.get("dup_of")),
        "near_dup_flagged": sum(1 for d in rows if d.get("near_dup_of")),
        "unique_para_id": len({d["para_id"] for d in rows}),
        "packages": len({d["pkg"] for d in rows}),
        "with_page_orig": sum(1 for d in rows if d.get("page_orig") is not None),
        "zh_chars_total": sum(int(d.get("zh_chars") or 0) for d in rows),
    })
    st["with_math_pct"] = round(100.0 * st["with_math"] / max(1, st["total"]), 2)
    st["flag_counts"] = dict(sorted(fc.items()))
    io.open(STATS, "w", encoding="utf-8", newline="\n").write(
        json.dumps(st, ensure_ascii=False, indent=1))
    print(json.dumps(st, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
