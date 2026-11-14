# -*- coding: utf-8 -*-
import sys, pymupdf
src, out = sys.argv[1], sys.argv[2]
page = int(sys.argv[3]) if len(sys.argv) > 3 else 1
doc = pymupdf.open(src)
pix = doc[page - 1].get_pixmap(dpi=140)
pix.save(out)
print("pages:", doc.page_count, "->", out)
