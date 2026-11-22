# -*- coding: utf-8 -*-
import os, sys
import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(os.path.dirname(HERE), 'work', 'pdf', 'src.pdf')
OUT = os.path.join(os.path.dirname(HERE), 'work', 'pdftext.txt')

pages = [int(x) for x in sys.argv[1:]] or [1, 2, 3, 9, 10]
d = pymupdf.open(PDF)
with open(OUT, 'w', encoding='utf-8') as f:
    for p in pages:
        f.write('\n===== page %d =====\n' % p)
        f.write(d[p - 1].get_text())
print('ok', OUT, os.path.getsize(OUT))
