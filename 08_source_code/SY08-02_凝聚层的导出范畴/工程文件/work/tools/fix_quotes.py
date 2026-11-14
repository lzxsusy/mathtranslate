# -*- coding: utf-8 -*-
"""把 chunk 里的直角引号「」换成简体出版规范的弯引号“”。"""
import io, sys

for p in sys.argv[1:]:
    s = io.open(p, encoding='utf-8').read()
    n1, n2 = s.count('\u300c'), s.count('\u300d')
    if n1 or n2:
        s = s.replace('\u300c', '\u201c').replace('\u300d', '\u201d')
        io.open(p, 'w', encoding='utf-8').write(s)
    print(p, 'replaced', n1, n2)
