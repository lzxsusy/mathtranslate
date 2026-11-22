# -*- coding: utf-8 -*-
r"""把 chunk 里的 `\medskip\noindent\textbf{标题}\label{..}\par` 统一改写为 `\ssszh{标题}\label{..}`。

\ssszh 会 step subsubsection 计数器（原文 \sss 即 \subsubsection，即使不显示编号也步进），
从而让定理类编号与原文逐条对应。
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CH = os.path.join(os.path.dirname(ROOT), "源码", "chunks")

pat = re.compile(r"\\medskip\\noindent\\textbf\{((?:[^{}]|\{[^{}]*\})*)\}(\\label\{[^}]*\})?\\par")

total = 0
for path in sorted(glob.glob(os.path.join(CH, "ch0*.tex"))):
    s = open(path, encoding="utf-8").read()
    new, n = pat.subn(lambda m: "\\ssszh{%s}%s" % (m.group(1), m.group(2) or ""), s)
    if n:
        open(path, "w", encoding="utf-8").write(new)
    total += n
    print(os.path.basename(path), n)
print("total", total)
