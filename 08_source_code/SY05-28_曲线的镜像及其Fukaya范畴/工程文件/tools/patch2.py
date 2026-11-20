# -*- coding: utf-8 -*-
import io, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '源码'))

# 1) 目录只到 subsection 层
s = io.open('preamble.tex', encoding='utf-8').read()
if 'tocdepth' not in s:
    s = s.replace('\\begin{document}', '\\begin{document}')  # noop guard
    s += '\n\\setcounter{tocdepth}{2}\n'
    io.open('preamble.tex', 'w', encoding='utf-8').write(s)

# 2) 裤子 ≅ P^1
s = io.open('ch3_talk3.tex', encoding='utf-8').read()
old = r'\text{裤子}=\PP^1\setminus\{-1,0,\infty\}'
new = r'\text{裤子}\cong\PP^1\setminus\{-1,0,\infty\}'
assert old in s
s = s.replace(old, new, 1)
io.open('ch3_talk3.tex', 'w', encoding='utf-8').write(s)
print('ok')
