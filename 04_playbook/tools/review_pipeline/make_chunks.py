#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Split each *_align.txt by source-page blocks into readable chunks."""
import re, pathlib

REV = pathlib.Path(r"C:\Users\admin\Downloads\DBMS_work\review")
OUT = REV / "chunks"
OUT.mkdir(exist_ok=True)

PAGES_PER_CHUNK = 10

def split_pages(text):
    # blocks start with the '====' separator line then '### 原文 PDF 第 N 页'
    parts = re.split(r"(?=^={60}\n### 原文 PDF 第 \d+ 页)", text, flags=re.M)
    return [p for p in parts if p.strip()]

index = []
for f in sorted(REV.glob("*_align.txt")):
    name = f.stem.replace("_align", "")
    text = f.read_text(encoding="utf-8")
    pages = split_pages(text)
    d = OUT / name
    d.mkdir(exist_ok=True)
    for i in range(0, len(pages), PAGES_PER_CHUNK):
        group = pages[i:i+PAGES_PER_CHUNK]
        m1 = re.search(r"第 (\d+) 页", group[0])
        m2 = re.search(r"第 (\d+) 页", group[-1])
        a, b = (int(m1.group(1)), int(m2.group(1))) if m1 and m2 else (i, i+1)
        dest = d / f"p{a:03d}-{b:03d}.txt"
        dest.write_text("\n".join(group), encoding="utf-8")
        index.append((name, dest.name, dest.stat().st_size))
    print(name, len(pages), "pages ->", len((list(d.glob('*.txt')))), "chunks")

print("\ntotal chunks:", len(index))
(REV / "_chunks.txt").write_text("\n".join(f"{a}\t{b}\t{c}" for a,b,c in index), encoding="utf-8")
