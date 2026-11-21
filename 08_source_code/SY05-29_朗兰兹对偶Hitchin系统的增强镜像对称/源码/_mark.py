# -*- coding: utf-8 -*-
import io

items = [
    ("ch1_intro.tex", "1987 年", 2229),
    ("ch2_background.tex", "对我们来说", 2230),
    ("ch2_background.tex", "为表述 \\cite{hausel-thaddeus}", 2233),
    ("ch2_background.tex", "2007 年", 2234),
    ("ch3_enhanced.tex", "下面这些考察", 2235),
    ("ch3_enhanced.tex", "设复数乘法群", 2236),
    ("ch3_enhanced.tex", "主要想法是", 2238),
    ("ch3_enhanced.tex", "这里我们说明", 2241),
    ("ch3_enhanced.tex", "最后，我们来表述", 2244),
]

files = {}
for fn, anchor, num in items:
    if fn not in files:
        files[fn] = io.open(fn, encoding="utf-8").read()
    s = files[fn]
    if anchor not in s:
        print("MISS", fn, num)
        continue
    s = s.replace(anchor, "\\origpage{%d}%s" % (num, anchor), 1)
    files[fn] = s
    print("marked", num)

for fn, s in files.items():
    io.open(fn, "w", encoding="utf-8", newline="\n").write(s)
print("ok")
