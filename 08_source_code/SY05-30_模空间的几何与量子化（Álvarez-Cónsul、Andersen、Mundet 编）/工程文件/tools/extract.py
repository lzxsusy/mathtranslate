# -*- coding: utf-8 -*-
"""Extract text + page images from the GQMS volume."""
import os, sys
import pymupdf

SRC = r"C:\Users\admin\xwechat_files\wxid_x0ix6rgox7aq22_4797\msg\file\2026-11\GeometryandQuantizationofModuliSpaces(AlvarezConsul,LuisAndersenetc.)(Z-Library)-1(2).pdf"
OUT = r"C:\Users\admin\Downloads\gqms_work"
IMGDIR = r"C:\Users\admin\Downloads\gqms_pages"
os.makedirs(OUT, exist_ok=True)
os.makedirs(IMGDIR, exist_ok=True)

doc = pymupdf.open(SRC)
n = doc.page_count
print("pages:", n)

# full text with page markers
lines = []
for i in range(n):
    lines.append(f"\n\n=== PDF page {i+1} | printed p.{i+1-11} ===\n")
    lines.append(doc[i].get_text("text"))
open(os.path.join(OUT, "full.txt"), "w", encoding="utf-8").write("".join(lines))

# chapter cuts (printed page ranges -> pdf)
ranges = {
    "front": (1, 11),
    "ch01": (12, 78),
    "ch02": (79, 116),
    "ch03": (117, 181),
    "ch04": (182, 230),
}
for name, (a, b) in ranges.items():
    parts = []
    for p in range(a - 1, b):
        parts.append(f"\n\n=== PDF page {p+1} | printed p.{p+1-11} ===\n")
        parts.append(doc[p].get_text("text"))
    open(os.path.join(OUT, name + ".txt"), "w", encoding="utf-8").write("".join(parts))
    print(name, b - a + 1, "pages", len("".join(parts)), "chars")

# page images at 150 dpi
for i in range(n):
    fn = os.path.join(IMGDIR, f"p{i+1:03d}.png")
    if os.path.exists(fn):
        continue
    pix = doc[i].get_pixmap(dpi=150)
    pix.save(fn)
print("images done")
