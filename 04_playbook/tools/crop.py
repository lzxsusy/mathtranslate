#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""crop.py — 从 PDF 页面裁一小块区域成 PNG（核对公式用，别整页读图）

用法：
  python crop.py <pdf> <pdf 页号，1 起> <x0> <y0> <x1> <y1> <out.png> [--dpi 200]

坐标是页面宽高的比例（0–1），例如 0.1 0.2 0.9 0.45。
输出单边超过 1200 px 会提示：公式核对用 200 dpi、裁到所需区域即可，整页图更贵。
"""
import argparse
import sys

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("page", type=int, help="PDF 页号（1 起，不是原书页）")
    ap.add_argument("box", nargs=4, type=float, metavar=("X0", "Y0", "X1", "Y1"))
    ap.add_argument("out")
    ap.add_argument("--dpi", type=int, default=200)
    a = ap.parse_args()

    import pymupdf
    doc = pymupdf.open(a.pdf)
    page = doc[a.page - 1]
    w, h = page.rect.width, page.rect.height
    x0, y0, x1, y1 = a.box
    clip = pymupdf.Rect(x0 * w, y0 * h, x1 * w, y1 * h)
    pix = page.get_pixmap(clip=clip, matrix=pymupdf.Matrix(a.dpi / 72, a.dpi / 72))
    pix.save(a.out)
    print(f"{a.out}  {pix.width}x{pix.height} px  ({a.dpi} dpi, p{a.page} crop {x0},{y0}–{x1},{y1})")
    if max(pix.width, pix.height) > 1200:
        print("提示：单边 >1200 px。公式核对可再裁小一点——整页大图既慢又贵。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
