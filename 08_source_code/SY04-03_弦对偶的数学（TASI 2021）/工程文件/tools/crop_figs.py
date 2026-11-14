#!/usr/bin/env python
"""Crop the 14 figures from the source PDF into figures/figNN.png (300 dpi).

Rects are in PDF points (page 595.276 x 841.89), determined by inspecting the
vector-drawing bounding boxes plus the figure labels, and excluding caption
text and body text.  Verified visually against the page images.
"""
import os
import sys

import pymupdf

PDF = (r"<本地路径>"
       r"\2026-10\2204.01914v2(1).pdf")
OUT = r"<本地路径>"

# name, page, x0, y0, x1, y1
CROPS = [
    ("fig01", 7,  248,  88, 361, 190),
    ("fig02", 24, 236, 276, 381, 402),
    ("fig03", 25, 155,  88, 442, 214),
    ("fig04", 25, 241, 264, 353, 389),
    ("fig05", 26, 260,  89, 333, 189),
    ("fig06", 31, 131,  88, 484, 216),
    ("fig07", 33, 146,  88, 447, 222),
    ("fig08", 38, 197,  88, 401, 242),
    ("fig09", 43, 117, 356, 479, 563),
    ("fig10", 47, 232, 454, 363, 572),
    ("fig11", 50, 140,  96, 455, 217),
    ("fig12", 50, 183, 452, 412, 618),
    ("fig13", 51, 112,  93, 481, 215),
    ("fig14", 54, 206,  87, 389, 270),
]


def main() -> int:
    doc = pymupdf.open(PDF)
    os.makedirs(OUT, exist_ok=True)
    for name, pno, x0, y0, x1, y1 in CROPS:
        page = doc[pno - 1]
        r = pymupdf.Rect(x0, y0, x1, y1) & page.rect
        pix = page.get_pixmap(clip=r, dpi=300)
        pix.save(os.path.join(OUT, name + ".png"))
        print(f"{name}: p{pno} {pix.width}x{pix.height}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
