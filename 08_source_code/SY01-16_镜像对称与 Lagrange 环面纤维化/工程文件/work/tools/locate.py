# -*- coding: utf-8 -*-
"""locate.py <page> <keyword> ：打印该页内含 keyword 的文本行，及其 300dpi 像素 bbox。"""
import sys, os, io
import pymupdf
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PDF = os.path.join(ROOT, 'src',
    'JP03_植田一石_ミラー対称性とLagrangeトーラスファイブレーション_10p.pdf')
doc = pymupdf.open(PDF)
page = int(sys.argv[1])
kw = sys.argv[2] if len(sys.argv) > 2 else ''
z = 300/72.0
p = doc[page-1]
d = p.get_text('dict')
for b in d['blocks']:
    for l in b.get('lines', []):
        txt = ''.join(s['text'] for s in l['spans'])
        if kw in txt:
            x0, y0, x1, y1 = l['bbox']
            print('%.0f %.0f %.0f %.0f | %s' % (x0*z, y0*z, x1*z, y1*z, txt))
