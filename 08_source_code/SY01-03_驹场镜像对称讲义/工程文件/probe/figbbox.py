# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import pymupdf as fitz

PDF = r"<本地路径>).pdf"
doc = fitz.open(PDF)
for pno in [16, 17, 30, 32, 33, 35, 36]:
    p = doc[pno-1]
    print(f"=== page {pno} (w={p.rect.width}, h={p.rect.height}) ===")
    ds = p.get_drawings()
    bbs = [d["rect"] for d in ds]
    for bb in bbs:
        print(f"   {round(bb.x0,1)},{round(bb.y0,1)} - {round(bb.x1,1)},{round(bb.y1,1)}")
