# -*- coding: utf-8 -*-
"""Extract \\index entries from the Chinese TeX parts into a TSV term list."""
import re
import collections
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(ROOT, "源码")
OUT = os.path.join(ROOT, "校对记录", "索引术语.tsv")

terms = collections.Counter()
firstloc = {}
for fn in ["part1_zh.tex", "part2_zh.tex", "part3_zh.tex", "part4_zh.tex"]:
    txt = open(os.path.join(SRC, fn), encoding="utf-8").read()
    for m in re.finditer(r"\\index\{([^}]*)\}", txt):
        key = m.group(1)
        terms[key] += 1
        if key not in firstloc:
            line = txt[: m.start()].count("\n") + 1
            firstloc[key] = (fn, line)

with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write("term\tcount\tfile\tline\n")
    for k, c in terms.most_common():
        fn, ln = firstloc[k]
        f.write("%s\t%d\t%s\t%d\n" % (k, c, fn, ln))

print("entries=%d unique=%d -> %s" % (sum(terms.values()), len(terms), OUT))
