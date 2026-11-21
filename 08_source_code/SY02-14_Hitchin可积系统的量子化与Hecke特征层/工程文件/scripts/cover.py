#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""页覆盖核查：扫 源码/chapters/*.tex 的 \\SourcePage{N}，报告缺失页码。

用法：python cover.py            # 只看 chapters/
      python cover.py --units    # 同时把 units/ 里未装配的页算进来
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.normpath(os.path.join(HERE, '..', '..', '源码'))
SP = re.compile(r'\\SourcePage\{(\d+)\}')


def pages_of(path):
    s = io.open(path, encoding='utf-8').read()
    return [int(x) for x in SP.findall(s)]


def main():
    use_units = '--units' in sys.argv
    chap_dir = os.path.join(SRC, 'chapters')
    have = {}
    for fn in sorted(os.listdir(chap_dir)):
        if not fn.endswith('.tex'):
            continue
        for p in pages_of(os.path.join(chap_dir, fn)):
            have.setdefault(p, []).append(fn)
    if use_units:
        ud = os.path.join(SRC, 'units')
        for fn in sorted(os.listdir(ud)):
            if fn.endswith('.tex'):
                for p in pages_of(os.path.join(ud, fn)):
                    have.setdefault(p, []).append('units/' + fn)
    # 正文范围：原书 p.1 是标题页，p.2 空白，p.3-380 正文，p.381-386 文献
    missing = [p for p in range(1, 387) if p not in have]
    dup = {p: v for p, v in have.items() if len(v) > 1}
    print('页数（有锚点）:', len(have))
    print('缺页:', missing if missing else '无')
    if dup:
        print('重复锚点:')
        for p in sorted(dup):
            print('  p%d -> %s' % (p, ', '.join(dup[p])))


if __name__ == '__main__':
    main()
