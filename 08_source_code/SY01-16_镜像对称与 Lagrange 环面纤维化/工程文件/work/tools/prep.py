# -*- coding: utf-8 -*-
"""JP03 预处理：逐页文字层 + 150/200dpi 渲染图 + 整本全文。"""
import pymupdf, os, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PDF = os.path.join(ROOT, 'src',
    'JP03_植田一石_ミラー対称性とLagrangeトーラスファイブレーション_10p.pdf')
WORK = os.path.join(ROOT, 'work')
PAGES = os.path.join(WORK, 'pages')
SPLIT = os.path.join(WORK, 'split')
os.makedirs(PAGES, exist_ok=True)
os.makedirs(SPLIT, exist_ok=True)

doc = pymupdf.open(PDF)
print('pages:', doc.page_count)
full = []
for i in range(doc.page_count):
    p = doc[i]
    txt = p.get_text('text')
    open(os.path.join(SPLIT, 'p%03d.txt' % (i+1)), 'w', encoding='utf-8').write(txt)
    full.append('===== PDF PAGE %d =====\n' % (i+1) + txt)
    pix = p.get_pixmap(dpi=150)
    pix.save(os.path.join(PAGES, 'p%03d.png' % (i+1)))
    pix300 = p.get_pixmap(dpi=300)
    pix300.save(os.path.join(PAGES, 'p%03d_300.png' % (i+1)))
    print('p%d  chars=%d  size=%s' % (i+1, len(txt), p.rect))
open(os.path.join(WORK, 'full.txt'), 'w', encoding='utf-8').write('\n'.join(full))
print('done')
