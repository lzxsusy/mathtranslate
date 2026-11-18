# -*- coding: utf-8 -*-
"""按 main.toc 重新生成 源码/back/pagecorr.tex（原文页码对照表）。
用法（在 main.tex 至少编译两遍之后）：python make_pagecorr.py
"""
import os
import re

root = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
toc_path = os.path.join(root, '源码', 'main.toc')
out_path = os.path.join(root, '源码', 'back', 'pagecorr.tex')

sec, sub = {}, {}
refs_page = None
pat = re.compile(r'\\contentsline \{(section|subsection)\}\{(.*)\}\{(\d+)\}')
for line in open(toc_path, encoding='utf-8'):
    for m in pat.finditer(line):
        kind, body, page = m.group(1), m.group(2), m.group(3)
        nm = re.search(r'\\numberline \{([\d.]+)\}', body)
        if kind == 'section':
            if nm:
                sec[nm.group(1)] = page
            elif '参考文献' in body:
                refs_page = page
        else:
            if nm:
                sub[nm.group(1)] = page

rows = [
    ('1--3',   'Introduction', '\\S1', sec.get('1', '—')),
    ('4--12',  'Degenerations of unitary Conformal Field Theories', '\\S2', sec.get('2', '—')),
    ('13--21', 'Calabi--Yau manifolds in the large complex structure limit', '\\S3', sec.get('3', '—')),
    ('22--27', '$A_\\infty$-algebras and $A_\\infty$-categories', '\\S4', sec.get('4', '—')),
    ('28--35', 'Fukaya category and its degeneration', '\\S5', sec.get('5', '—')),
    ('36--41', 'Morse--Smale complex and the category of Morse functions（6.1--6.3）', '\\S6', sec.get('6', '—')),
    ('41--48', '同上（6.4--6.6）', '\\S6', sub.get('6.4', '—')),
    ('48--51', '$A_\\infty$-structure for the derived category of coherent sheaves', '\\S7', sec.get('7', '—')),
    ('52--59', 'Homological mirror conjecture', '\\S8', sec.get('8', '—')),
    ('59--63', 'Appendix: constructions in the case of complex numbers', '\\S9', sec.get('9', '—')),
    ('63--66', 'References', '---', refs_page or '—'),
]

lines = []
for r in rows:
    lines.append('%s   & %s & %s & %s \\\\' % r)

body = '\n'.join(lines)
tex = r"""% 附录 B 原文页码对照（由 工程文件/work/make_pagecorr.py 按 main.toc 生成）
\section{原文页码对照}
\addcontentsline{toc}{section}{附录 B\quad 原文页码对照}

本表给出原文章节与本书页码的对应关系。原文为 arXiv:math/0011041v2（66 页），本书页码见右列。
原文与本书的分页并不一致（原文为 letter 单栏、11pt），逐页对勘时请按「原文章节 → 本书节」再定位。

\begin{center}
\begin{longtable}{@{}p{0.10\textwidth}p{0.50\textwidth}p{0.08\textwidth}p{0.10\textwidth}@{}}
\toprule
\textbf{原文页} & \textbf{原文章节} & \textbf{本书节} & \textbf{本书页} \\
\midrule
\endhead
\bottomrule
\endfoot
""" + body + r"""
\end{longtable}
\end{center}

此外，书中所有定理、命题、引理、定义、注、猜想都沿用原文的编号（各类独立连续编号，
原文跳号处亦保持原样），因此按编号即可直接回查原文。
"""
open(out_path, 'w', encoding='utf-8').write(tex)
print('已生成 pagecorr.tex')
for r in rows:
    print('  %-7s -> p.%s' % (r[0], r[3]))
