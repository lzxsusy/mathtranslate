# -*- coding: utf-8 -*-
"""把 harvmac 老式 {\bf \bar 4} 改成 \bar{\bf 4}（LaTeX2e 数学模式下 \bf→\mathbf 只吃一个记号，多记号会炸）。"""
import io, re, glob, sys
pat = re.compile(r'\{\\bf\s*\\bar\s*(\{[^{}]*\}|[^{}\s\\])\}')
n = 0
for f in sorted(glob.glob('skel/*.tex')):
    s = io.open(f, encoding='utf-8').read()
    s2, k = pat.subn(lambda m: r'\bar{\bf ' + m.group(1) + '}', s)
    if k:
        io.open(f, 'w', encoding='utf-8').write(s2)
        print(f, k)
        n += k
print('total', n)
