#!/usr/bin/env python
"""Generate the page-concordance appendix (original page -> translated page).

1. Insert \\label{op:N} right after each first occurrence of a page anchor
   (idempotent: existing labels are stripped first).
2. Write sections/appendix-pagemap.tex with a compact 8-column table.

Run, then compile twice so \\pageref resolves.
"""
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECT = os.path.join(ROOT, "sections")
ANCHOR = re.compile(r"%\s*====\s*原文 PDF 第\s*(\d+)\s*页")
LABEL = re.compile(r"^\s*\\label\{op:\d+\}\s*$")

files = sorted(glob.glob(os.path.join(SECT, "s*.tex")))

# pass 1: strip any pre-existing concordance labels (idempotent)
for path in files:
    src = open(path, encoding="utf-8").read()
    lines = [ln for ln in src.splitlines() if not LABEL.match(ln)]
    open(path, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")

# pass 2: insert labels after the first anchor of each page
seen = set()
for path in files:
    lines = open(path, encoding="utf-8").read().splitlines()
    out = []
    for ln in lines:
        out.append(ln)
        m = ANCHOR.search(ln)
        if m:
            n = int(m.group(1))
            if n not in seen:
                seen.add(n)
                out.append(r"\label{op:%d}" % n)
    open(path, "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
print("labelled pages:", len(seen))

# pass 3: build the table
pages = list(range(2, 93))
per_row = 4
rows = []
for i in range(0, len(pages), per_row):
    cells = []
    for n in pages[i:i + per_row]:
        cells.append(str(n))
        cells.append(r"\pageref{op:%d}" % n)
    while len(cells) < per_row * 2:
        cells.extend(["", ""])
    rows.append(" & ".join(cells) + r"\\")
header = " & ".join([r"原文页 & 译文页"] * per_row) + r"\\"
body = "\n".join([header, r"\midrule"] + rows)

TPL = r"""% ============================================================
% 附录：原文页码—译文页码对照表（由 tools/gen_pagemap.py 自动生成）
% 原文页 = arXiv PDF 页码 = 印刷页码；译文页由 \pageref 解析
% ============================================================
\clearpage
\section*{附录：原文页码—译文页码对照}
\addcontentsline{toc}{section}{附录：原文页码—译文页码对照}

本译本在源码中为原文每一页保留了锚点注释（\texttt{\% ==== 原文 PDF 第 N 页 ====}）。
下表给出原文第 2--92 页与译文页的对应，便于与原 PDF 逐页对读；原文第 1 页为标题页，
对应本译本封面。

\begin{center}
\small
\setlength{\tabcolsep}{4pt}
\renewcommand{\arraystretch}{1.12}
\begin{tabular}{*{8}{c}}
\toprule
__BODY__
\bottomrule
\end{tabular}
\end{center}
"""

tex = TPL.replace("__BODY__", body)
open(os.path.join(SECT, "appendix-pagemap.tex"), "w", encoding="utf-8",
     newline="\n").write(tex)
print("wrote sections/appendix-pagemap.tex")
