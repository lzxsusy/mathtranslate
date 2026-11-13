# -*- coding: utf-8 -*-
"""打印指定页所有文本 span 的字体名（用于判定 斜体/正体/粗体/哥特体/黑板体）。"""
import sys, re
sys.stdout.reconfigure(encoding='utf-8')
import pymupdf as fitz

PDF = r"<本地路径>).pdf"
doc = fitz.open(PDF)

def dump(page_no, pattern):
    p = doc[page_no - 1]
    d = p.get_text("dict")
    for b in d["blocks"]:
        for l in b.get("lines", []):
            txt = "".join(s["text"] for s in l["spans"])
            if re.search(pattern, txt):
                print(f"--- p{page_no}: {txt[:120]!r}")
                for s in l["spans"]:
                    print(f"   font={s['font']:14s} size={s['size']:5.1f} text={s['text']!r}")

dump(18, r"weight lattice")
dump(18, r"Weyl group")
dump(18, r"maximal torus")
