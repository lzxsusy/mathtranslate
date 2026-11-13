# -*- coding: utf-8 -*-
"""修正 ch03b 的页标记：tr03 误用了 PDF 页号（132-136），应为原书印刷页 112-116。"""
import re

p = r"<本地路径>"
t = open(p, encoding="utf-8").read()
for pdfpg, prt in [(132, 112), (133, 113), (134, 114), (135, 115), (136, 116)]:
    old = f"% [原文 p.{pdfpg}]"
    new = f"% [原文 p.{prt}]"
    n = t.count(old)
    t = t.replace(old, new)
    print(old, "->", new, "x", n)
open(p, "w", encoding="utf-8").write(t)
print("markers now:", re.findall(r"% \[原文 p\.\d+\]", t))
