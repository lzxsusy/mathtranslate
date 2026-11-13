#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""把原书某一页的指定区域放大渲染，用于逐符号核对公式 / 插图 / 交换图。

用法（任意目录，python 用当前环境的 python 即可）：
  python src/tools/zoom.py 23 300 100 400 600 700
  参数：PDF 页号（1 起） dpi  x0 y0 x1 y1（PDF 点，1pt = 1/72 inch，页面 A4 宽 595 高 842）
  不给坐标则整页渲染。
输出：work/zoom/p023_x100_y400_w300_h600_300dpi.png，并打印路径。

技巧：先用 work/pages/pNNN.png（130dpi 整页图）看版式确定坐标，
坐标换算：PDF点 = 像素 × 72 / 130。
"""
import os, sys
import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
PDF = os.path.join(ROOT, "work", "source", "EN49_原文_Jeffs2023_156p.pdf")
OUT = os.path.join(ROOT, "work", "zoom")


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 1
    page = int(argv[1])
    dpi = int(argv[2]) if len(argv) > 2 else 300
    doc = pymupdf.open(PDF)
    pg = doc[page - 1]
    clip = None
    if len(argv) >= 7:
        x0, y0, x1, y1 = (float(v) for v in argv[3:7])
        clip = pymupdf.Rect(x0, y0, x1, y1)
    os.makedirs(OUT, exist_ok=True)
    if clip is None:
        fn = os.path.join(OUT, "p%03d_full_%ddpi.png" % (page, dpi))
    else:
        fn = os.path.join(OUT, "p%03d_x%04d_y%04d_w%04d_h%04d_%ddpi.png"
                          % (page, clip.x0, clip.y0, clip.width, clip.height, dpi))
    pix = pg.get_pixmap(dpi=dpi, clip=clip)
    pix.save(fn)
    print(fn)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
