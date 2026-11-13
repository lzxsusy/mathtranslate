# -*- coding: utf-8 -*-
import pymupdf, os, sys, json, re
sys.stdout.reconfigure(encoding='utf-8')
SRC = r"<本地路径> (M.F.アティヤ Michael Francis Atiyah) (z-library.sk  1lib.sk  z-lib.sk).pdf"
doc = pymupdf.open(SRC)
toc = doc.get_toc()
print("=== TOC (1-based pdf page) ===")
for lvl, t, p in toc:
    print(f"  L{lvl} p{p:3d}  {t}")
print()
print("=== per page: textlen, first 2 lines, last 2 lines ===")
for i in range(doc.page_count):
    t = doc[i].get_text("text")
    lines = [x.strip() for x in t.split("\n") if x.strip()]
    head = " | ".join(lines[:2])[:60]
    tail = " | ".join(lines[-2:])[:60]
    print(f"p{i+1:3d} len={len(t):5d} HEAD[{head}] TAIL[{tail}]")
