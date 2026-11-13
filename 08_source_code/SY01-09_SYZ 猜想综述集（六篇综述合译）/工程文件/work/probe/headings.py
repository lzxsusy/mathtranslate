# -*- coding: utf-8 -*-
"""用字号/字重识别章节标题 → work/probe/headings.txt"""
import os, io
from collections import Counter
import pymupdf

BASE = r"<本地路径>"
SRC = os.path.join(BASE, "01_surveys")
W = os.path.join(BASE, "work")
PAPERS = [
    ("p1", "Chan-2014_SYZ-conjecture-and-its-impact_arXiv1408.6062.pdf", 14),
    ("p2", "Glimpse-of-the-SYZ-conjecture-and-related-developments_ICCM2016.pdf", 14),
    ("p3", "Gross-2008_SYZ-conjecture_torus-fibrations-to-degenerations_arXiv0802.3407.pdf", 41),
    ("p4", "Gross-2013_Mirror-symmetry-and-SYZ-conjecture_arXiv1212.4220.pdf", 64),
    ("p5", "YangLi-2022_Survey-metric-SYZ-conjecture-non-archimedean-geometry_arXiv2204.11363.pdf", 42),
    ("p6", "Collins-Lin-2022_Recent-progress-SYZ-noncompact-CY-surfaces_arXiv2208.14485.pdf", 25),
]
out = io.open(os.path.join(W, "probe", "headings.txt"), "w", encoding="utf-8", newline="\n")
def P(*a): print(*a, file=out)

for key, fn, body_end in PAPERS:
    doc = pymupdf.open(os.path.join(SRC, fn))
    P("=" * 90); P(key, fn)
    sizes = Counter()
    pages = []
    for i in range(body_end):
        d = doc[i].get_text("dict")
        pages.append(d)
        for b in d["blocks"]:
            for l in b.get("lines", []):
                for s in l["spans"]:
                    sizes[round(s["size"], 1)] += len(s["text"])
    body = sizes.most_common(1)[0][0]
    P("body size:", body, "sizes:", sizes.most_common(5))
    for i, d in enumerate(pages):
        for b in d["blocks"]:
            for l in b.get("lines", []):
                txt = "".join(s["text"] for s in l["spans"]).strip()
                if not txt or len(txt) > 110:
                    continue
                mx = max(s["size"] for s in l["spans"])
                bold = any(("Bold" in s["font"] or "Medi" in s["font"] or "Black" in s["font"]) for s in l["spans"])
                if mx > body + 0.8 or (bold and mx >= body and len(txt) > 4):
                    P(f"p{i+1:03d} sz={mx:.1f} bold={bold}: {txt[:100]}")
    doc.close()
out.close()
print("ok")
