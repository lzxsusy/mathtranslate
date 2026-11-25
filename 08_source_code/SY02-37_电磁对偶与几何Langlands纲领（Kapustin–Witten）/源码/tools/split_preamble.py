# -*- coding: utf-8 -*-
"""把 main.tex 的导言区抽成 preamble.tex，并让 main.tex 变薄。
   （只跑一次；之后修改导言请改 preamble.tex）"""
import io, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
main = io.open(os.path.join(ROOT, 'main.tex'), encoding='utf-8').read()
i = main.index(r'\begin{document}')
pre, body = main[:i], main[i:]
# 导言部分：\documentclass 保留在 main，其余进 preamble
j = pre.index(r'\usepackage')
docclass = pre[:j]
io.open(os.path.join(ROOT, 'preamble.tex'), 'w', encoding='utf-8').write(
    '%% 导言区（由 tools/split_preamble.py 从 main.tex 抽出，请直接改这里）\n' + pre[j:])
new = docclass + '\\input{preamble}\n\n' + body
io.open(os.path.join(ROOT, 'main.tex'), 'w', encoding='utf-8').write(new)
print('preamble.tex', len(pre) - j, 'chars; main.tex', len(new), 'chars')
