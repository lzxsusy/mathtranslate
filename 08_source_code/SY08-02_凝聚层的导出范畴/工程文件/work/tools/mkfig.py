# -*- coding: utf-8 -*-
"""按分数坐标从原书页裁切图版，输出 src/figures/dg_<书页>_<字母>.pdf 与同名 .png。

坐标一律用页面的**分数**（0–1，左上为原点），这样与分辨率无关。

用法一（单张）：
  python tools/mkfig.py 545 a 0.24 0.72 0.60 0.83
用法二（批量，从 TSV 读，列：书页 字母 fx0 fy0 fx1 fy1）：
  python tools/mkfig.py --tsv work/figure_rects.tsv

选项：--dpi 400（默认），--pad 2（pt 内边距），--png-only
"""
import os, sys, glob
import pymupdf as fitz

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF_DIR = r"C:\Users\admin\xwechat_files\wxid_x0ix6rgox7aq22_4797\msg\file\2026-11"
PDF = [q for q in glob.glob(os.path.join(PDF_DIR, '*.pdf')) if 'rlov' in q][0]
OUT = os.path.join(ROOT, 'src', 'figures')


def cut(doc, book, letter, fx0, fy0, fx1, fy1, dpi=400, pad=2):
    page = doc[book - 510 - 1]
    R = page.rect
    clip = fitz.Rect(R.x0 + fx0 * R.width, R.y0 + fy0 * R.height,
                     R.x0 + fx1 * R.width, R.y0 + fy1 * R.height)
    clip = fitz.Rect(clip.x0 - pad, clip.y0 - pad, clip.x1 + pad, clip.y1 + pad)
    pix = page.get_pixmap(dpi=dpi, clip=clip)
    base = 'dg_%d_%s' % (book, letter)
    png = os.path.join(OUT, base + '.png')
    pix.save(png)
    # 用同一张位图生成 PDF：按 72dpi 的物理尺寸放置，宽度记为该裁切的真实点数
    pdf = os.path.join(OUT, base + '.pdf')
    d = fitz.open()
    w_pt = clip.width
    h_pt = clip.height
    pg = d.new_page(width=w_pt, height=h_pt)
    pg.insert_image(fitz.Rect(0, 0, w_pt, h_pt), filename=png)
    d.save(pdf, deflate=True)
    d.close()
    print('  %-14s %5.0fx%-5.0f pt  ->  %s' % (base, w_pt, h_pt, os.path.basename(pdf)))


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    dpi = 400
    pad = 2
    for i, a in enumerate(sys.argv):
        if a == '--dpi':
            dpi = int(sys.argv[i + 1])
        if a == '--pad':
            pad = float(sys.argv[i + 1])
    doc = fitz.open(PDF)
    os.makedirs(OUT, exist_ok=True)
    if '--tsv' in sys.argv:
        path = sys.argv[sys.argv.index('--tsv') + 1]
        import io
        for line in io.open(path, encoding='utf-8'):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            f = line.split('\t')
            book, letter = int(f[0]), f[1]
            fx0, fy0, fx1, fy1 = [float(x) for x in f[2:6]]
            cut(doc, book, letter, fx0, fy0, fx1, fy1, dpi, pad)
    else:
        book, letter = int(args[0]), args[1]
        fx0, fy0, fx1, fy1 = [float(x) for x in args[2:6]]
        cut(doc, book, letter, fx0, fy0, fx1, fy1, dpi, pad)


main()
