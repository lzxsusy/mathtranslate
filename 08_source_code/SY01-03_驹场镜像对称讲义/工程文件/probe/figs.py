# -*- coding: utf-8 -*-
"""Locate figure captions and drawing bboxes."""
import sys, re
sys.stdout.reconfigure(encoding='utf-8')
import pymupdf as fitz

PDF = r"<本地路径>).pdf"
doc = fitz.open(PDF)
for i, p in enumerate(doc):
    t = p.get_text()
    for m in re.finditer(r"Figure\s+(\d+):", t):
        print(f"p{i+1:02d} caption Figure {m.group(1)}: ...")
    if "Figure" in t:
        # print caption line bbox
        d = p.get_text("dict")
        for b in d["blocks"]:
            for l in b.get("lines", []):
                txt = "".join(s["text"] for s in l["spans"])
                if txt.strip().startswith("Figure"):
                    print(f"   p{i+1} bbox={[round(x,1) for x in l['bbox']]} text={txt[:80]!r}")
        print(f"   p{i+1}: drawings={len(p.get_drawings())}")
