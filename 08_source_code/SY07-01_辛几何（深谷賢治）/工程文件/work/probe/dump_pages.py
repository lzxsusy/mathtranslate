# -*- coding: utf-8 -*-
import pymupdf, sys
SRC = r"<本地路径> (深谷賢治 Kenji Fukaya) (z-library.sk  1lib.sk  z-lib.sk).pdf"
doc = pymupdf.open(SRC)
lo, hi = int(sys.argv[1]), int(sys.argv[2])
for i in range(lo-1, min(hi, doc.page_count)):
    t = doc[i].get_text("text")
    print(f"\n===== PDF p{i+1} len={len(t.strip())} =====")
    print(t)
doc.close()
