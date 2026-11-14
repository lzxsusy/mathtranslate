# -*- coding: utf-8 -*-
"""Check every original PDF page in each chapter range has >=1 \\SourceParagraph
and count paragraphs per page (to spot skipped pages)."""
import re, io, glob, os, collections

root = r"C:\Users\admin\Downloads\DBMS_work\Dirichlet-Mirror-Symmetry-zh\chapters"
ranges = {
    "preface": (7, 9, ["preface.tex"]),
    "ch01": (11, 36, ["ch01.tex"]),
    "ch02": (37, 118, ["ch02.tex"]),
    "ch03": (119, 225, ["ch03a.tex", "ch03b.tex"]),
    "ch04": (227, 302, ["ch04.tex"]),
    "ch05": (303, 429, ["ch05a.tex", "ch05b.tex"]),
    "ch06": (431, 518, ["ch06.tex"]),
    "ch07": (519, 583, ["ch07.tex"]),
    "ch08": (585, 663, ["ch08.tex", "ch08-sec82.tex", "ch08-sec83.tex",
                        "ch08-sec84head.tex", "ch08-sec84tail.tex", "ch08-sec85.tex"]),
}

for ch, (a, b, files) in ranges.items():
    pages = collections.Counter()
    for f in files:
        p = os.path.join(root, f)
        if not os.path.exists(p):
            print("MISSING FILE", p)
            continue
        s = io.open(p, encoding="utf-8").read()
        for m in re.finditer(r"\\SourceParagraph\{[^}]*\}\{(\d+)\}", s):
            pages[int(m.group(1))] += 1
    missing = [p for p in range(a, b + 1) if p not in pages]
    print("%-8s pages %3d-%3d  covered %3d/%3d  total paras %4d  missing pages: %s"
          % (ch, a, b, len([p for p in pages if a <= p <= b]), b - a + 1,
             sum(v for k, v in pages.items() if a <= k <= b),
             missing[:12] if missing else "-"))
