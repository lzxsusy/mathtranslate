# -*- coding: utf-8 -*-
import sys, re
sys.stdout.reconfigure(encoding='utf-8')
import pymupdf as fitz
doc = fitz.open(r"<本地路径>).pdf")
p = doc[21]  # p22
W = p.rect.width
print("W", W)
d = p.get_text("dict")
for b in d["blocks"]:
    for l in b.get("lines", []):
        txt = "".join(s["text"] for s in l["spans"])
        x1 = max(s["bbox"][2] for s in l["spans"])
        if "(" in txt and ")" in txt:
            print(f"x1={x1:6.1f} spans={len(l['spans'])} {txt!r}")
print("\n--- lines x1>500 ---")
for b in d["blocks"]:
    for l in b.get("lines", []):
        txt = "".join(s["text"] for s in l["spans"])
        x1 = max(s["bbox"][2] for s in l["spans"])
        if x1 > 500:
            print(f"x1={x1:6.1f} {txt!r}")
