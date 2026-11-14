# -*- coding: utf-8 -*-
"""Crop a figure region from a scanned PDF page.

Usage:
    python crop_fig.py --page 31 --box 0.10,0.55,0.90,0.86 --out figs/fig_p031_1.png
Box is x0,y0,x1,y1 as fractions of page width/height (origin top-left).
Optional --pad (fraction of page size, default 0.008) enlarges the box slightly.
"""
import argparse
import os

import pymupdf

PDF = r"<本地路径>"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", default=PDF)
    ap.add_argument("--page", type=int, required=True, help="1-based page number")
    ap.add_argument("--box", required=True, help="x0,y0,x1,y1 fractions 0..1")
    ap.add_argument("--out", required=True)
    ap.add_argument("--dpi", type=int, default=300)
    ap.add_argument("--pad", type=float, default=0.006)
    args = ap.parse_args()

    x0, y0, x1, y1 = [float(v) for v in args.box.split(",")]
    x0 = max(0.0, x0 - args.pad)
    y0 = max(0.0, y0 - args.pad)
    x1 = min(1.0, x1 + args.pad)
    y1 = min(1.0, y1 + args.pad)
    if x1 <= x0 or y1 <= y0:
        raise SystemExit("empty box")

    doc = pymupdf.open(args.pdf)
    page = doc[args.page - 1]
    r = page.rect
    clip = pymupdf.Rect(
        r.x0 + x0 * r.width,
        r.y0 + y0 * r.height,
        r.x0 + x1 * r.width,
        r.y0 + y1 * r.height,
    )
    pix = page.get_pixmap(dpi=args.dpi, clip=clip, colorspace=pymupdf.csGRAY)
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    pix.save(args.out)
    print("saved", args.out, pix.width, "x", pix.height)


if __name__ == "__main__":
    main()
