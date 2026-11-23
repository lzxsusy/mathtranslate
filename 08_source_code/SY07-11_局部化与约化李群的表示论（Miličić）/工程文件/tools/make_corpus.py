#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 SY07-11 译稿切段，追加进 01_corpus_zh/zh_paragraphs.jsonl，术语表追加进 termbase.jsonl。

用法（在仓库根目录下）：
    python "08_source_code/SY07-11_.../工程文件/tools/make_corpus.py" --dry-run
    python "08_source_code/SY07-11_.../工程文件/tools/make_corpus.py" --write

字段与既有语料一致：pkg / file / para / para_id / page_orig / env / tier / text / zh_chars / flags / seg
para_id = 段落文本 sha1 前 16 位（跨工程同文同号）。
"""
import argparse
import hashlib
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(os.path.dirname(HERE))          # 08_source_code/SY07-11_...
ROOT = os.path.dirname(os.path.dirname(PROJ))          # 仓库根
PKG = "SY07-11"
SRC = os.path.join("源码", "chapters")
CORPUS = os.path.join(ROOT, "01_corpus_zh", "zh_paragraphs.jsonl")
TERMBASE = os.path.join(ROOT, "01_corpus_zh", "termbase.jsonl")
TERMS = os.path.join(PROJ, "工程文件", "work", "术语表.tsv")

CJK = re.compile(r"[\u3400-\u9fff]")
ENV_RE = re.compile(r"^\s*\\(begin|end)\{([a-zA-Z*]+)\}")


def zh_count(s):
    return len(CJK.findall(s))


def strip_comments(line):
    out, i = [], 0
    while i < len(line):
        ch = line[i]
        if ch == "\\" and i + 1 < len(line):
            out.append(line[i:i + 2])
            i += 2
            continue
        if ch == "%":
            break
        out.append(ch)
        i += 1
    return "".join(out)


def clean_para(text):
    t = text.strip()
    t = re.sub(r"\\label\{[^}]*\}", "", t)
    t = re.sub(r"\\index\{[^}]*\}", "", t)
    t = re.sub(r"\\ref\{[^}]*\}", "（见前）", t)
    t = re.sub(r"\n\s*\n", "\n", t)
    t = re.sub(r"[ \t]+", " ", t)
    return t.strip()


def chapter_order():
    main = open(os.path.join(PROJ, "源码", "main.tex"), encoding="utf-8").read()
    return re.findall(r"\\inputif\{([^}]+)\}", main)


def paragraphs(path):
    lines = [strip_comments(l) for l in io.open(path, encoding="utf-8").read().splitlines()]
    buf, env, out = [], "text", []
    for line in lines:
        m = ENV_RE.match(line)
        if m:
            kind, name = m.groups()
            if kind == "begin" and name in ("lemma", "theorem", "proposition", "corollary",
                                            "definition", "example", "remark", "proof", "annote"):
                if buf:
                    out.append((env, "\n".join(buf))); buf = []
                env = name
            elif kind == "end" and env == name:
                if buf:
                    out.append((env, "\n".join(buf))); buf = []
                env = "text"
            continue
        if not line.strip():
            if buf:
                out.append((env, "\n".join(buf))); buf = []
            continue
        if re.match(r"^\s*\\(chapter|section|subsection|subsubsection|part|tableofcontents|printindex)\b", line):
            if buf:
                out.append((env, "\n".join(buf))); buf = []
            continue
        buf.append(line)
    if buf:
        out.append((env, "\n".join(buf)))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    recs = []
    for name in chapter_order():
        path = os.path.join(PROJ, SRC, name + ".tex")
        if not os.path.exists(path):
            continue
        for i, (env, raw) in enumerate(paragraphs(path), 1):
            text = clean_para(raw)
            n = zh_count(text)
            if n < 12:
                continue
            recs.append({
                "pkg": PKG,
                "file": "%s/%s/%s.tex" % (PKG, SRC.replace("\\", "/"), name),
                "para": i,
                "para_id": hashlib.sha1(text.encode("utf-8")).hexdigest()[:16],
                "page_orig": None,
                "env": env,
                "tier": "B",
                "text": text,
                "zh_chars": n,
                "flags": [],
                "seg": "",
            })

    terms = []
    for line in io.open(TERMS, encoding="utf-8").read().splitlines():
        parts = line.split("\t")
        if len(parts) < 2 or parts[0].strip() in ("en", ""):
            continue
        en, zh = parts[0].strip(), parts[1].strip()
        if not en or not zh or zh.startswith("zh"):
            continue
        terms.append({"foreign": en, "lang": "en", "zh": zh, "status": "candidate",
                      "pkg": PKG, "src_format": "tsv"})

    print("段落 %d 条，汉字 %d 个；术语 %d 条" % (len(recs), sum(r["zh_chars"] for r in recs), len(terms)))
    if args.dry_run or not args.write:
        for r in recs[:3]:
            print("  ", r["env"], r["zh_chars"], r["text"][:60].replace("\n", " "))
        return 0

    existing = set()
    for line in io.open(CORPUS, encoding="utf-8"):
        try:
            r = json.loads(line)
        except Exception:
            continue
        if r.get("pkg") == PKG:
            existing.add(r.get("para_id"))
    new = [r for r in recs if r["para_id"] not in existing]
    with io.open(CORPUS, "a", encoding="utf-8") as f:
        for r in new:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    have = set()
    for line in io.open(TERMBASE, encoding="utf-8"):
        try:
            have.add(json.loads(line).get("foreign"))
        except Exception:
            pass
    tnew = [t for t in terms if t["foreign"] not in have]
    with io.open(TERMBASE, "a", encoding="utf-8") as f:
        for t in tnew:
            f.write(json.dumps(t, ensure_ascii=False) + "\n")
    print("写入：新段落 %d（跳过重复 %d），新术语 %d" % (len(new), len(recs) - len(new), len(tnew)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
