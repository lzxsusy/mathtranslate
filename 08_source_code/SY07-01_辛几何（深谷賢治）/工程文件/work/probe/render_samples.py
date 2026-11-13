# -*- coding: utf-8 -*-
"""渲染样页，检查扫描质量与页面结构"""
import pymupdf, os
SRC = r"<本地路径> (深谷賢治 Kenji Fukaya) (z-library.sk  1lib.sk  z-lib.sk).pdf"
OUT = r"<本地路径>"
doc = pymupdf.open(SRC)
for pdfpage in [1, 9, 11, 20, 21, 45, 100, 200, 300, 400, 420]:
    p = doc[pdfpage-1]
    pix = p.get_pixmap(dpi=150)
    fn = os.path.join(OUT, f"sample_{pdfpage:03d}.png")
    pix.save(fn)
    print(fn, pix.width, pix.height, os.path.getsize(fn))
doc.close()
