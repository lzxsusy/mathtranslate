#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""normalize_blocks.py — 把词条区块宏统一成带花括号形式

有些作者写成
    \\mathdef
    设 ...
而 SCHEMA 要求
    \\mathdef{设 ...}
本脚本把「裸写」的区块补上花括号（内容到下一个区块宏 / \\end{word} / \\par\\medskip 为止）。
用法（在 rosetta 目录）：python tools/normalize_blocks.py [file ...]   缺省处理 entries/*.tex
"""
import glob
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MACROS = ['mathdef', 'physdef', 'mathex', 'physex', 'bridge', 'intuit', 'pitfall']
BOUNDARY = re.compile(r'^\s*\\(?:' + '|'.join(MACROS) + r')\b|^\s*\\end\{word\}|^\s*\\par\\medskip')


def normalize(text):
    lines = text.split('\n')
    out = []
    i = 0
    changed = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r'^(\s*)\\(%s)\s*(\{.*)?$' % '|'.join(MACROS), line)
        if not m:
            out.append(line)
            i += 1
            continue
        indent, macro, tail = m.group(1), m.group(2), m.group(3)
        if tail:  # 已有花括号，原样
            out.append(line)
            i += 1
            continue
        # 裸写：收集后续行直到边界
        j = i + 1
        body = []
        while j < len(lines) and not BOUNDARY.match(lines[j]):
            body.append(lines[j])
            j += 1
        # 去掉尾部空行
        while body and not body[-1].strip():
            body.pop()
        if not body:
            out.append(line)
            i += 1
            continue
        out.append('%s\\%s{' % (indent, macro))
        out.extend(body)
        out.append('}')
        changed += 1
        i = j
    return '\n'.join(out), changed


def main():
    files = sys.argv[1:] or sorted(glob.glob(os.path.join(ROOT, 'entries', 't*.tex')))
    total = 0
    for f in files:
        p = f if os.path.isabs(f) else os.path.join(ROOT, f)
        text = io.open(p, encoding='utf-8').read()
        new, changed = normalize(text)
        if changed:
            io.open(p, 'w', encoding='utf-8', newline='\n').write(new)
        total += changed
        print('%s  fixed=%d' % (os.path.basename(p), changed))
    print('total fixed=%d' % total)


if __name__ == '__main__':
    main()
