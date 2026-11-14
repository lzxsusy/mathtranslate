# -*- coding: utf-8 -*-
"""把原书 198 页渲染为 PNG（150dpi）到 work/orig_png/pNNN.png，供逐页核对公式与图表。"""
import pymupdf, os, sys

WORK = os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(os.path.dirname(WORK), '..', '【合并】  Lecture 1~23.pdf')
PDF = os.path.abspath(os.path.join(r'<本地路径>', '【合并】  Lecture 1~23.pdf'))
OUT = os.path.join(WORK, 'orig_png')
os.makedirs(OUT, exist_ok=True)
d = pymupdf.open(PDF)
print('pages', d.page_count)
for i in range(d.page_count):
    p = os.path.join(OUT, 'p%03d.png' % (i + 1))
    if os.path.exists(p):
        continue
    pix = d[i].get_pixmap(dpi=150)
    pix.save(p)
    if (i + 1) % 20 == 0:
        print('done', i + 1, flush=True)
print('all rendered to', OUT)
