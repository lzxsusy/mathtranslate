# -*- coding: utf-8 -*-
"""lines.py <page> [dpi] ：按行列出该页文本及其 bbox（像素），供确定裁图带。"""
import sys, os, io
import pymupdf
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PDF = os.path.join(ROOT, 'src',
    'JP03_植田一石_ミラー対称性とLagrangeトーラスファイブレーション_10p.pdf')
doc = pymupdf.open(PDF)
page = int(sys.argv[1])
dpi = int(sys.argv[2]) if len(sys.argv) > 2 else 300
z = dpi/72.0
p = doc[page-1]
d = p.get_text('dict')
rows = []
for b in d['blocks']:
    for l in b.get('lines', []):
        txt = ''.join(s['text'] for s in l['spans'])
        x0, y0, x1, y1 = l['bbox']
        rows.append((y0, y1, x0, x1, txt))
rows.sort()
for y0, y1, x0, x1, txt in rows:
    print('%4.0f %4.0f  x%4.0f-%4.0f | %s' % (y0*z, y1*z, x0*z, x1*z, txt))
