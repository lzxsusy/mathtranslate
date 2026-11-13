# -*- coding: utf-8 -*-
"""Print text spans in figure regions to build exact crop boxes."""
import sys
sys.stdout.reconfigure(encoding='utf-8')
import pymupdf as fitz

PDF = r"<本地路径>).pdf"
doc = fitz.open(PDF)
REGIONS = {16: (300, 470), 17: (55, 230), 30: (330, 615), 32: (55, 215),
           33: (55, 215), 35: (280, 420), 36: (55, 330)}
for pno, (ya, yb) in REGIONS.items():
    p = doc[pno-1]
    print(f"=== p{pno} band y {ya}..{yb} ===")
    d = p.get_text("dict")
    for b in d["blocks"]:
        for l in b.get("lines", []):
            txt = "".join(s["text"] for s in l["spans"]).strip()
            if not txt:
                continue
            bb = l["bbox"]
            if ya <= bb[1] <= yb or ya <= bb[3] <= yb:
                print(f"   [{bb[0]:6.1f},{bb[1]:6.1f},{bb[2]:6.1f},{bb[3]:6.1f}] {txt[:70]!r}")
