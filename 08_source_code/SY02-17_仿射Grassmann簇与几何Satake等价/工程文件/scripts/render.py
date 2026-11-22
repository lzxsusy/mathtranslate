# -*- coding: utf-8 -*-
"""把译本 PDF 逐页渲染成 PNG，供目视核对。用法： python render.py [dpi] [起始页] [结束页]"""
import os
import sys

import pymupdf

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # 工程文件
proj = os.path.dirname(root)
pdf = os.path.join(proj, "源码", "main.pdf")
outdir = os.path.join(root, "work", "proof")
os.makedirs(outdir, exist_ok=True)

dpi = int(sys.argv[1]) if len(sys.argv) > 1 else 115
a = int(sys.argv[2]) if len(sys.argv) > 2 else 1
b = int(sys.argv[3]) if len(sys.argv) > 3 else 10 ** 6

doc = pymupdf.open(pdf)
b = min(b, doc.page_count)
for i in range(a, b + 1):
    pix = doc[i - 1].get_pixmap(dpi=dpi)
    pix.save(os.path.join(outdir, "my_p%02d.png" % i))
print("pages", doc.page_count, "rendered", a, "-", b)
