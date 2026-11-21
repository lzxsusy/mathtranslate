# -*- coding: utf-8 -*-
"""Raster-crop a figure out of a page and save it as PNG at high dpi.

Coordinates are fractions of the page width/height (0,0 = top-left), which is what
you read off a rendered band image.

Usage:
  python crop_png.py PAGE X0 X1 Y0 Y1 NAME [DPI]
Out: 源码/figures/NAME.png
"""
import os
import sys

import pymupdf

PDF = r"C:\Users\admin\xwechat_files\wxid_x0ix6rgox7aq22_4797\msg\file\2026-11\20-BenZvi_LAWRG2024_lectures.pdf"
HERE = os.path.dirname(os.path.abspath(__file__))
FIGS = os.path.normpath(os.path.join(HERE, "..", "..", "源码", "figures"))


def main() -> None:
    page_no = int(sys.argv[1])
    x0, x1 = float(sys.argv[2]), float(sys.argv[3])
    y0, y1 = float(sys.argv[4]), float(sys.argv[5])
    name = sys.argv[6]
    dpi = int(sys.argv[7]) if len(sys.argv) > 7 else 300
    doc = pymupdf.open(PDF)
    page = doc[page_no - 1]
    W, H = page.rect.width, page.rect.height
    clip = pymupdf.Rect(x0 * W, y0 * H, x1 * W, y1 * H)
    os.makedirs(FIGS, exist_ok=True)
    pix = page.get_pixmap(dpi=dpi, clip=clip)
    out = os.path.join(FIGS, name + ".png")
    pix.save(out)
    print("%s  %dx%d px  clip=(%.0f,%.0f,%.0f,%.0f)"
          % (name, pix.width, pix.height, clip.x0, clip.y0, clip.x1, clip.y1))


if __name__ == "__main__":
    main()
