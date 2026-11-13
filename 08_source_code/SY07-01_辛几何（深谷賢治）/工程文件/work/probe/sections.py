# -*- coding: utf-8 -*-
"""定位各章/节在 PDF 中的起始页"""
import pymupdf, re
SRC = r"<本地路径> (深谷賢治 Kenji Fukaya) (z-library.sk  1lib.sk  z-lib.sk).pdf"
doc = pymupdf.open(SRC)
sec_re = re.compile(r'^\s*[ｧ§]\s*([0-9])\s*[\.．]\s*([0-9]{1,2})\s')
ch_re = re.compile(r'第\s*([0-9])\s*章\s')
found = []
for i in range(doc.page_count):
    lines = doc[i].get_text("text").splitlines()
    for j, line in enumerate(lines[:4]):
        m = sec_re.match(line)
        if m:
            found.append(("sec", int(m.group(1)), int(m.group(2)), i+1, i+1-10, line.strip()[:50]))
        m = ch_re.search(line)
        if m and j <= 2 and i+1 >= 11:
            # 章起始页通常页眉就是章名
            found.append(("chap", int(m.group(1)), 0, i+1, i+1-10, line.strip()[:50]))
for f in found:
    print(f)
doc.close()
