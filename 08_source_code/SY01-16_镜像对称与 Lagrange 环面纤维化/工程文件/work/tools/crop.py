# -*- coding: utf-8 -*-
"""裁图核对：python crop.py <page> x0 y0 x1 y1 <out> [dpi]
坐标一律以 300dpi 渲染图的像素给出（与 lines.py / locate.py 一致）。"""
import sys, os
import pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PDF = os.path.join(ROOT, 'src',
    'JP03_植田一石_ミラー対称性とLagrangeトーラスファイブレーション_10p.pdf')
doc = pymupdf.open(PDF)
page = int(sys.argv[1])
x0, y0, x1, y1 = map(float, sys.argv[2:6])
out = sys.argv[6]
dpi = int(sys.argv[7]) if len(sys.argv) > 7 else 300
BASE = 300 / 72.0
p = doc[page - 1]
clip = pymupdf.Rect(x0 / BASE, y0 / BASE, x1 / BASE, y1 / BASE)
pix = p.get_pixmap(dpi=dpi, clip=clip)
pix.save(out)
print(out, pix.width, 'x', pix.height)
