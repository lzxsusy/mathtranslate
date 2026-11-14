#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从原始扫描 PDF 中渲染页面，或按像素框裁剪/放大图片。

用法（工作目录 = 工作区根目录）：
  python qsg/tools/pageimg.py page 30 work/tmp/p030.png --dpi 150
  python qsg/tools/pageimg.py fig  30 120 600 1100 1500 qsg/figures/fig_p030_1.png --dpi 300

坐标 (x0,y0,x1,y1) 一律采用 **150 dpi 页面图**（1240 x 1753 像素）中的像素坐标；
脚本内部自动换算为 PDF 点坐标并以更高 dpi 重新渲染，保证图表清晰。
若只是放大查看某一区域的公式，也用 fig 子命令，输出到 work/tmp/ 下即可。
"""
import argparse
import os
import sys

import pymupdf as fitz

PDF = r"<本地路径>"
BASE_DPI = 150.0


def render(page_no: int, rect_px=None, dpi=300) -> fitz.Pixmap:
    doc = fitz.open(PDF)
    page = doc[page_no - 1]
    clip = None
    if rect_px is not None:
        x0, y0, x1, y1 = rect_px
        s = 72.0 / BASE_DPI
        clip = fitz.Rect(x0 * s, y0 * s, x1 * s, y1 * s) & page.rect
    return page.get_pixmap(dpi=dpi, clip=clip)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    p1 = sub.add_parser("page")
    p1.add_argument("page", type=int)
    p1.add_argument("out")
    p1.add_argument("--dpi", type=int, default=150)

    p3 = sub.add_parser("fig")
    p3.add_argument("page", type=int)
    p3.add_argument("x0", type=float)
    p3.add_argument("y0", type=float)
    p3.add_argument("x1", type=float)
    p3.add_argument("y1", type=float)
    p3.add_argument("out")
    p3.add_argument("--dpi", type=int, default=300)

    a = ap.parse_args()
    if a.cmd == "page":
        pix = render(a.page, None, a.dpi)
    else:
        pix = render(a.page, (a.x0, a.y0, a.x1, a.y1), a.dpi)
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    pix.save(a.out)
    print(f"saved {a.out} ({pix.width}x{pix.height})")


if __name__ == "__main__":
    main()
