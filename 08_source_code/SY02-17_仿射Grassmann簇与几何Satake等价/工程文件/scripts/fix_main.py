# -*- coding: utf-8 -*-
"""重建 main.tex 的正文区：ch00 ... ch21。"""
import io
import os
import re

here = os.path.dirname(os.path.abspath(__file__))
p = os.path.normpath(os.path.join(here, "..", "..", "源码", "main.tex"))
s = io.open(p, encoding="utf-8").read()

inputs = "\n".join(r"\input{chunks/ch%02d}" % i for i in range(0, 22))
marker = r"\input{chunks/ch00}"
head, sep, _tail = s.partition(marker)
tail = s[s.rindex(r"\end{document}"):]
new = head + inputs + "\n\n" + tail
io.open(p, "w", encoding="utf-8").write(new)
print(new[-800:])
