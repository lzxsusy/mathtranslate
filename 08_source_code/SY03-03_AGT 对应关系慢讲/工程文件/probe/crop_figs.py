# -*- coding: utf-8 -*-
"""Crop the 5 figures from the source PDF as PNG at 400 dpi."""
import sys, re, os
sys.stdout.reconfigure(encoding='utf-8')
import pymupdf as fitz

SRC = r"<本地路径>).pdf"
FIG = r"<本地路径>"
os.makedirs(FIG, exist_ok=True)
doc = fitz.open(SRC)

# candidate pages per figure (where the drawing is)
targets = {
    1: [7],
    2: [19],
    3: [54, 56],
    4: [79],
    5: [80],
}

for fig, pages in targets.items():
    for pg in pages:
        p = doc[pg - 1]
        cap = p.search_for(f"Figure {fig}:")
        txt = p.get_text()
        if not cap:
            print(f"fig{fig} p{pg}: no caption bbox")
            continue
        capr = cap[0]
        # collect drawing rects above the caption (allow caption below figure)
        rects = [d["rect"] for d in p.get_drawings()]
        above = [r for r in rects if r.y1 <= capr.y0 + 2 and r.width > 2 and r.height > 2]
        if not above:
            print(f"fig{fig} p{pg}: no drawings above caption")
            continue
        x0 = min(r.x0 for r in above); x1 = max(r.x1 for r in above)
        y0 = min(r.y0 for r in above); y1 = max(r.y1 for r in above)
        # restrict to drawings within a plausible vertical band just above caption
        band = [r for r in above if r.y0 > y1 - 380]
        x0 = min(r.x0 for r in band); x1 = max(r.x1 for r in band)
        y0 = min(r.y0 for r in band); y1 = max(r.y1 for r in band)
        # caption may be to the right of the drawing? check overlap
        m = 12
        clip = fitz.Rect(max(0, x0 - m), max(0, y0 - m), min(p.rect.x1, x1 + m), capr.y0 - 5)
        pix = p.get_pixmap(dpi=400, clip=clip)
        out = os.path.join(FIG, f"fig{fig}_p{pg}.png")
        pix.save(out)
        print(f"fig{fig} p{pg}: clip={clip} size={pix.width}x{pix.height} -> {out}")
        print("   caption:", re.sub(r"\s+", " ", " ".join(p.get_textbox(fitz.Rect(capr.x0, capr.y0, p.rect.x1, capr.y0 + 90)).split()))[:400])
