# -*- coding: utf-8 -*-
"""Render a vertical band of a PDF page to PNG (for reading math off the page).

Usage:
  python page_band_png.py PAGE YTOP YBOT NAME [DPI]
Out: 工程文件/work/bands/NAME.png
"""
import os
import sys

import pymupdf

PDF = r"C:\Users\admin\xwechat_files\wxid_x0ix6rgox7aq22_4797\msg\file\2026-11\20-BenZvi_LAWRG2024_lectures.pdf"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, "..", "work", "bands"))


def main() -> None:
    page_no = int(sys.argv[1])
    ytop, ybot = float(sys.argv[2]), float(sys.argv[3])
    name = sys.argv[4]
    dpi = int(sys.argv[5]) if len(sys.argv) > 5 else 170
    os.makedirs(OUT, exist_ok=True)
    doc = pymupdf.open(PDF)
    page = doc[page_no - 1]
    H = page.rect.height
    clip = pymupdf.Rect(0, ytop * H, page.rect.width, ybot * H)
    pix = page.get_pixmap(dpi=dpi, clip=clip)
    path = os.path.join(OUT, name + ".png")
    pix.save(path)
    print(path, pix.width, "x", pix.height)


if __name__ == "__main__":
    main()
