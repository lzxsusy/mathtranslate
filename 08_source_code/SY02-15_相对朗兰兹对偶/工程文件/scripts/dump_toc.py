# -*- coding: utf-8 -*-
import pymupdf, io, os
os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
d = pymupdf.open('源码/main.pdf')
out = io.open('工程文件/work/toc.txt', 'w', encoding='utf-8')
out.write(d[3].get_text('text'))
out.write('\n=====\n')
out.write(d[2].get_text('text'))
out.close()
print('ok', d.page_count)
