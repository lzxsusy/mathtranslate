#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""把 源码/chapters/chNN.tex 里的 \\input{units/...} 就地展开成全文。

用法：python inline.py 7 8 9 10
      python inline.py all
只处理仍是 \\input 形态的章；已内联的章会被跳过（避免重复内联）。
展开后每段前后保留 %% begin/end units/xxx.tex 注释便于回溯。
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.normpath(os.path.join(HERE, '..', '..', '源码'))
CHAP = os.path.join(SRC, 'chapters')
UNITS = os.path.join(SRC, 'units')
INPUT = re.compile(r'^[ \t]*\\input\{(units/[^}]+)\}[ \t]*$', re.M)


def inline_one(num):
    path = os.path.join(CHAP, 'ch%02d.tex' % num)
    if not os.path.exists(path):
        print('  skip (no file):', path)
        return False
    s = io.open(path, encoding='utf-8').read()
    hits = INPUT.findall(s)
    if not hits:
        print('  skip (already inlined): ch%02d' % num)
        return False

    def repl(m):
        rel = m.group(1)
        p = os.path.join(SRC, rel + '.tex')
        body = io.open(p, encoding='utf-8').read().rstrip('\n')
        return '%%%% begin units/%s.tex\n%s\n%%%% end units/%s.tex' % (
            os.path.basename(rel), body, os.path.basename(rel))

    s2 = INPUT.sub(repl, s)
    io.open(path, 'w', encoding='utf-8', newline='\n').write(s2)
    print('  ch%02d: %d units inlined, %d lines' % (num, len(hits), s2.count('\n') + 1))
    return True


def main():
    args = sys.argv[1:]
    if not args:
        print('usage: python inline.py 7 8 9 10 | all')
        return
    nums = range(0, 11) if args == ['all'] else [int(a) for a in args]
    for n in nums:
        inline_one(n)


if __name__ == '__main__':
    main()
