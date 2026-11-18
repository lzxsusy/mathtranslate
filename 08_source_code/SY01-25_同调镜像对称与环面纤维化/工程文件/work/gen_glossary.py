# -*- coding: utf-8 -*-
"""由 工程文件/work/glossary.tsv 生成 源码/back/glossary.tex（附录 A 英汉术语对照表）。
用法：python gen_glossary.py
tsv 三列：English<TAB>中文<TAB>备注
"""
import os

root = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
src = os.path.join(root, '工程文件', 'work', 'glossary.tsv')
out = os.path.join(root, '源码', 'back', 'glossary.tex')

ESC = {'\\': r'\textbackslash{}', '&': r'\&', '%': r'\%', '#': r'\#', '_': r'\_',
       '$': r'\$', '{': r'\{', '}': r'\}', '~': r'\textasciitilde{}', '^': r'\textasciicircum{}'}


def esc(s):
    return ''.join(ESC.get(c, c) for c in s)


rows = []
for line in open(src, encoding='utf-8'):
    if not line.strip():
        continue
    parts = line.rstrip('\n').split('\t')
    while len(parts) < 3:
        parts.append('')
    rows.append(parts)

body = '\n'.join('%s & %s & %s \\\\' % (esc(a), esc(b), esc(c)) for a, b, c in rows)

tex = r"""% 附录 A 术语表（由 工程文件/work/glossary.tsv 经 work/gen_glossary.py 生成）
\section{英汉术语对照表}

本表收录正文出现的专名术语。原语一律照原文拼写（含重音符号）；中文为本书统一译名。
正文中术语首次出现时以「中文（English）」形式给出，其后只用中文；专名（人名、空间名、
猜想名，如 Calabi--Yau、Fukaya、Berkovich）按通行习惯保留原文，不作音译。

\begingroup
\small
\begin{longtable}{@{}p{0.36\textwidth}p{0.30\textwidth}p{0.26\textwidth}@{}}
\toprule
\textbf{English} & \textbf{中文} & \textbf{备注} \\
\midrule
\endhead
\bottomrule
\endfoot
""" + body + r"""
\end{longtable}
\endgroup
"""
open(out, 'w', encoding='utf-8').write(tex)
print('已生成 glossary.tex，术语 %d 条' % len(rows))
