# -*- coding: utf-8 -*-
"""修 notes.tex 附录对照表：删重复/重定向行，替换不可用词条。"""
p = r'C:\Users\admin\Downloads\GL_work\源码\chunks\notes.tex'
lines = open(p, encoding='utf-8').read().split('\n')

ZW = '\u200b'
AB = '\\allowbreak '

row_stack = ('$G$-主丛／向量丛模栈 & moduli+' + ZW + AB + 'stack & '
             '§2.2、§2.2.1--2.2.2；$\\Bun_{G}$ 与 $\\mathrm{Pic}$ 的框架 \\\\')
row_char = ('奇异支撑 & characteristic+' + ZW + AB + 'variety & '
            '§4.2、§5.1；$\\Nilp$ 下标（nLab 的 \\emph{singular support} 页实为重定向到“分布的支集”，义项不同） \\\\')

out = []
for i, l in enumerate(lines, 1):
    if i in (60, 66, 73):
        continue
    if i == 65:
        out.append(row_stack)
        continue
    if i == 91:
        out.append(row_char)
        continue
    out.append(l)

open(p, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
print('data rows:', sum(1 for l in out if l.rstrip().endswith('\\\\')))
