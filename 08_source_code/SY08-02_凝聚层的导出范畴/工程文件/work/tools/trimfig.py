# -*- coding: utf-8 -*-
"""按「墨迹减去正文块」的方式精确定位图版并裁切。

原书页面是整页位图 + 文字层。图版（交换图）由线条与少量数学标签组成，
而正文行在文字层里有精确的块坐标。于是：

  1. 取窗口内的位图墨迹（灰度 < 160）；
  2. 把窗口内所有**宽文字块**（宽 > WIDE）覆盖的像素视为正文，擦掉；
  3. 剩下的墨迹就是图版本身（含其数学标签），取其包围盒；
  4. 四周留 PAD，输出 src/figures/dg_<书页>_<字母>.pdf/.png。

窗口来自 work/figure_rects.tsv（分数坐标），只需大致把图框住；
精修由本脚本完成。用法：python tools/trimfig.py [--tsv ...] [--dpi 400]
"""
import os, sys, glob, io, re
import numpy as np
import pymupdf as fitz
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF_DIR = r"C:\Users\admin\xwechat_files\wxid_x0ix6rgox7aq22_4797\msg\file\2026-11"
PDF = [q for q in glob.glob(os.path.join(PDF_DIR, '*.pdf')) if 'rlov' in q][0]
OUT = os.path.join(ROOT, 'src', 'figures')

PAD = 3.0
GROW = 34.0
WIDE = 250.0
DPI = 300


def main():
    args = sys.argv[1:]
    tsv = os.path.join(ROOT, 'work', 'figure_rects.tsv')
    dpi = DPI
    if '--tsv' in args:
        tsv = args[args.index('--tsv') + 1]
    if '--dpi' in args:
        dpi = int(args[args.index('--dpi') + 1])
    doc = fitz.open(PDF)
    os.makedirs(OUT, exist_ok=True)
    scale = dpi / 72.0

    for line in io.open(tsv, encoding='utf-8'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        f = line.split('\t')
        book, letter = int(f[0]), f[1]
        fx0, fy0, fx1, fy1 = [float(x) for x in f[2:6]]
        page = doc[book - 510 - 1]
        R = page.rect
        win = fitz.Rect(R.x0 + fx0 * R.width, R.y0 + fy0 * R.height - GROW,
                        R.x0 + fx1 * R.width, R.y0 + fy1 * R.height + GROW)
        win = win & R

        # 图版的范围 = 窗口内所有「非正文」块（即数学标签与线符号）的并集
        u = None
        for b in page.get_text('blocks'):
            br = fitz.Rect(b[0], b[1], b[2], b[3])
            if not br.intersects(win) or not b[4].strip():
                continue
            if re.search(r'[A-Za-z]{4,}', b[4]):
                continue                      # 含英文单词 → 正文行
            u = br if u is None else (u | br)
        if u is None:
            print('  !! %d%s 窗口内无图版块' % (book, letter))
            continue
        M = 7.0
        clip = fitz.Rect(u.x0 - M, u.y0 - M, u.x1 + M, u.y1 + M) & win
        pix2 = page.get_pixmap(dpi=dpi, clip=clip)
        base = 'dg_%d_%s' % (book, letter)
        png = os.path.join(OUT, base + '.png')
        pix2.save(png)
        d = fitz.open()
        pg = d.new_page(width=clip.width, height=clip.height)
        pg.insert_image(fitz.Rect(0, 0, clip.width, clip.height), filename=png)
        d.save(os.path.join(OUT, base + '.pdf'), deflate=True)
        d.close()
        print('  %-12s %5.0fx%-5.0f pt' % (base, clip.width, clip.height))


main()
