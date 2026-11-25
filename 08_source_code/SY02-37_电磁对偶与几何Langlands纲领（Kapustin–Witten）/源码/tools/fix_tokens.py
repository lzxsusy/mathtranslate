# -*- coding: utf-8 -*-
"""LaTeX2e 老式字体开关的两处致命写法修正（必须放在流水线最后、check_shards 之前）：
1) {\bf \bar 4}：数学模式下 \bf 是 \mathbf（只吃一个记号），多记号会报 Extra }。
   改为 \bar{\bf 4}。
2) {\it $...}：\it 后紧跟数学会炸（本机 preamble 下），改为 {\itshape $...}。
"""
import io, re, glob
n1 = n2 = 0
pat1 = re.compile(r'\{\\bf\s*\\bar\s*(\{[^{}]*\}|[^{}\s\\])\}')
for f in sorted(glob.glob('skel/*.tex')):
    s = io.open(f, encoding='utf-8').read()
    s, k1 = pat1.subn(lambda m: r'\bar{\bf ' + m.group(1) + '}', s)
    s, k2 = re.subn(r'\{\\it \$', r'{\\itshape $', s)
    if k1 or k2:
        io.open(f, 'w', encoding='utf-8').write(s)
        print(f, 'bfbar=%d it=%d' % (k1, k2))
        n1 += k1; n2 += k2
print('total bfbar=%d it=%d' % (n1, n2))
