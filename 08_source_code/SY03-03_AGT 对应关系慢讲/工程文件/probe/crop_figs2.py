# -*- coding: utf-8 -*-
"""Final figure crops with hand-verified clip rects (PDF points)."""
import sys, os
sys.stdout.reconfigure(encoding='utf-8')
import pymupdf as fitz
SRC = r"<本地路径>).pdf"
FIG = r"<本地路径>"
doc = fitz.open(SRC)
CLIPS = {
    1: (7,  fitz.Rect(120, 82, 475, 172)),
    2: (19, fitz.Rect(228, 80, 368, 226)),
    3: (56, fitz.Rect(160, 92, 440, 256)),
    4: (79, fitz.Rect(90, 82, 508, 212)),
    5: (80, fitz.Rect(193, 88, 392, 165)),
}
for fig, (pg, clip) in CLIPS.items():
    p = doc[pg - 1]
    pix = p.get_pixmap(dpi=400, clip=clip)
    out = os.path.join(FIG, f"fig{fig}.png")
    pix.save(out)
    print(f"fig{fig} p{pg} {pix.width}x{pix.height} -> {out}")
