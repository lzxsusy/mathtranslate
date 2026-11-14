# -*- coding: utf-8 -*-
"""列出 PDF 中各章的起始页码（1 基）。用法：python tools/toc_pages.py main.pdf"""
import sys, fitz

doc = fitz.open(sys.argv[1])
for i, page in enumerate(doc, 1):
    t = page.get_text('text')
    lines = [l.strip() for l in t.split('\n') if l.strip()]
    for j, l in enumerate(lines[:4]):
        if l.startswith('第') and '章' in l[:4]:
            print(i, l, '|', lines[j+1] if j+1 < len(lines) else '')
print('total pages', doc.page_count)
