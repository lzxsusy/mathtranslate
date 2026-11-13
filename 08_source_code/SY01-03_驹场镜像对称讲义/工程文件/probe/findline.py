# -*- coding: utf-8 -*-
"""鎸夊叧閿瓧瀹氫綅琛屽苟瑁佸浘锛堥珮 dpi锛夛紝鐢ㄤ簬澶嶆牳鏄撻敊绗﹀彿銆?""
import sys, os
sys.stdout.reconfigure(encoding='utf-8')
import pymupdf as fitz

PDF = r"<本地路径>).pdf"
TMP = r"<本地路径>"
doc = fitz.open(PDF)

def find(page_no, keywords, out, pad=4, dpi=500):
    p = doc[page_no - 1]
    d = p.get_text("dict")
    hit = None
    for b in d["blocks"]:
        for l in b.get("lines", []):
            txt = "".join(s["text"] for s in l["spans"])
            if all(k in txt for k in keywords):
                hit = l["bbox"]
                print(f"p{page_no}: {txt[:90]!r} bbox={[round(x,1) for x in hit]}")
                break
        if hit:
            break
    if not hit:
        print(f"p{page_no}: NOT FOUND {keywords}")
        return
    clip = fitz.Rect(60, hit[1] - pad, 560, hit[3] + pad)
    pix = p.get_pixmap(dpi=dpi, clip=clip)
    pix.save(out)
    print("  ->", out, pix.width, "x", pix.height)

find(5, ["O_B", "B-chiral"], os.path.join(TMP, "chk_Bchiral.png"), pad=8)
find(20, ["(4.7)"], os.path.join(TMP, "chk_eq47.png"), pad=14)
find(20, ["A-chiral"], os.path.join(TMP, "chk_Achiral.png"), pad=8)
