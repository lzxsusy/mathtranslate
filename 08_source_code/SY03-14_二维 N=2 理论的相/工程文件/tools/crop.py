#!/usr/bin/env python
"""Crop a region of a page image for close inspection of formulas.

Usage:
  python crop.py --page 22 --rect 120,300,520,430 [--dpi 500] [--out z1.png]

--rect is in PDF points (page is 612x792 pt). Coordinates: x0,y0 (top-left) to
x1,y1 (bottom-right), origin at top-left of the page.
"""
import argparse
import os
import sys

import pymupdf

PDF = (r"<本地路径>"
       r"\2026-10\Witten 1993 二维N=2理论的相.pdf")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--page", type=int, required=True, help="1-based PDF page number")
    ap.add_argument("--rect", required=True, help="x0,y0,x1,y1 in PDF points")
    ap.add_argument("--dpi", type=int, default=500)
    ap.add_argument("--out", required=True)
    ap.add_argument("--pdf", default=PDF)
    a = ap.parse_args()

    x0, y0, x1, y1 = (float(v) for v in a.rect.split(","))
    doc = pymupdf.open(a.pdf)
    page = doc[a.page - 1]
    r = pymupdf.Rect(x0, y0, x1, y1) & page.rect
    if r.is_empty:
        print("empty rect after clipping", file=sys.stderr)
        return 2
    pix = page.get_pixmap(clip=r, dpi=a.dpi, colorspace=pymupdf.csGRAY)
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    pix.save(a.out)
    print(f"wrote {a.out} {pix.width}x{pix.height}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
