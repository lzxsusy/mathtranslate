# -*- coding: utf-8 -*-
"""Crop figures 1-8 from the PDF at 500 dpi (PDF point coordinates)."""
import sys, os
sys.stdout.reconfigure(encoding='utf-8')
import pymupdf as fitz

PDF = r"<本地路径>).pdf"
OUT = r"<本地路径>"
os.makedirs(OUT, exist_ok=True)

# (figure no, pdf page, x0, y0, x1, y1)  page = 612 x 792 pt
CROPS = [
    (1, 16, 208, 310, 389, 458),
    (2, 17, 208, 62, 389, 212),
    (3, 30, 143, 343, 441, 600),
    (4, 32,  92, 62, 506, 210),
    (5, 33,  92, 62, 506, 210),
    (6, 35, 128, 286, 468, 414),
    (7, 36, 128, 62, 468, 174),
    (8, 36,  84, 198, 515, 314),
]

doc = fitz.open(PDF)
for fig, pno, x0, y0, x1, y1 in CROPS:
    p = doc[pno-1]
    clip = fitz.Rect(x0, y0, x1, y1)
    pix = p.get_pixmap(dpi=500, clip=clip)
    out = os.path.join(OUT, f"fig{fig}.png")
    pix.save(out)
    print(f"fig{fig}: p{pno} {clip} -> {pix.width}x{pix.height} {os.path.getsize(out)//1024}KB")
