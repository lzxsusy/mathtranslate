"""Zoom helper for reading formulas/diagrams from the source PDF.

Usage:
  python crop.py --page 31 --rect 120,450,600,600 --zoom 3 --out z31.png
  python crop.py --page 18 --rect 100,200,520,420            (zoom defaults to 3)

`--rect` is in PDF points (page is 612 x 792 pt). `--zoom` multiplies 150 dpi.
"""
import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))          # paper1207/
WORKSPACE = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(WORKSPACE, ".pylibs"))
import pymupdf  # noqa: E402

PDF = os.path.join(ROOT, "1207.0496.pdf")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--page", type=int, required=True)
    ap.add_argument("--rect", required=True, help="x0,y0,x1,y1 in PDF points")
    ap.add_argument("--zoom", type=float, default=3.0)
    ap.add_argument("--out", default="crop.png")
    a = ap.parse_args()
    rect = pymupdf.Rect(*[float(v) for v in a.rect.split(",")])
    doc = pymupdf.open(PDF)
    pix = doc[a.page - 1].get_pixmap(clip=rect, dpi=int(150 * a.zoom))
    pix.save(a.out)
    print(f"{a.out}: {pix.width}x{pix.height} px, page {a.page}, rect {rect}")


if __name__ == "__main__":
    main()
