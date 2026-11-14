#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build bilingual page-aligned review files from the translation tex + original PDF text.

For each chapter, for each source page:
  <original English page text (pdftotext -layout)>
  --- 中文段落 (tex line numbers) ---
  [L123] \SourceParagraph{...}{page} 译文...
"""
import re, os, sys, pathlib, json

ROOT = pathlib.Path(r"C:\Users\admin\Downloads\DBMS_work\Dirichlet-Mirror-Symmetry-zh")
ORIG = pathlib.Path(r"C:\Users\admin\Downloads\DBMS_work\original")
OUT = pathlib.Path(r"C:\Users\admin\Downloads\DBMS_work\review")
OUT.mkdir(exist_ok=True)

full = (ORIG / "full.txt").read_text(encoding="utf-8", errors="replace")
pages = full.split("\f")
print("pdf pages:", len(pages))

def clean(s):
    s = s.replace("\r", "")
    # collapse page headers/footers of running heads? keep as is
    return s.strip("\n")

def parse_chapter(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    blocks = []
    cur = None
    for i, line in enumerate(lines, 1):
        m = re.match(r"\\SourceParagraph\{([^}]+)\}\{(\d+)\}", line)
        if m:
            if cur: cur["end"] = i - 1
            cur = {"id": m.group(1), "page": int(m.group(2)), "start": i, "lines": []}
            blocks.append(cur)
            rest = line[m.end():].strip()
            if rest: cur["lines"].append(rest)
        elif cur is not None:
            cur["lines"].append(line)
    if cur: cur["end"] = len(lines)
    return blocks

chapters = ["preface", "ch01", "ch02", "ch03", "ch04", "ch05", "ch06", "ch07",
            "ch08", "ch08-sec82", "ch08-sec83", "ch08-sec84head", "ch08-sec84tail", "ch08-sec85"]

summary = {}
for ch in chapters:
    p = ROOT / "chapters" / f"{ch}.tex"
    if not p.exists():
        print("missing", p); continue
    blocks = parse_chapter(p)
    bypage = {}
    for b in blocks:
        bypage.setdefault(b["page"], []).append(b)
    out = []
    for pg in sorted(bypage):
        out.append(f"============================================================")
        out.append(f"### 原文 PDF 第 {pg} 页  (English, pdftotext -layout)")
        out.append(f"============================================================")
        if 1 <= pg <= len(pages):
            out.append(clean(pages[pg-1]))
        else:
            out.append("!! page out of range")
        out.append("")
        out.append(f"---------------- 译文 tex 第 {pg} 页对应段落 ----------------")
        for b in bypage[pg]:
            body = "\n".join(b["lines"]).strip()
            out.append(f"[L{b['start']}-L{b['end']}] <<{b['id']}>> page={b['page']}")
            out.append(body)
            out.append("")
        out.append("")
    dest = OUT / f"{ch}_align.txt"
    dest.write_text("\n".join(out), encoding="utf-8")
    summary[ch] = {"paras": len(blocks), "pages": [min(bypage), max(bypage)], "file": str(dest), "tex": str(p)}
    print(ch, len(blocks), "paras", len(bypage), "pages", min(bypage), max(bypage))

(OUT / "_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
print("done ->", OUT)
