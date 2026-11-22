# -*- coding: utf-8 -*-
"""把 make_bib.py 生成的 “姓, 名” 改为 “名 姓”，并合并连续条目。"""
import io
import os
import re

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out = os.path.join(os.path.dirname(root), "源码", "chunks", "ch08.tex")
s = io.open(out, encoding="utf-8").read()


def flip(name):
    if "," not in name:
        return name
    last, first = name.split(",", 1)
    first = first.strip()
    last = last.strip()
    if not first:
        return last
    return "%s %s" % (first, last)


def fix_line(line):
    m = re.match(r"(\\bibitem\{[^}]*\} )(.*)$", line)
    if not m:
        return line
    head, rest = m.group(1), m.group(2)
    # 作者段 = 到第一个 ", \emph{" 之前
    idx = rest.find("\\emph{")
    if idx <= 0:
        return line
    auth = rest[:idx].rstrip().rstrip(",")
    tail = rest[idx:]
    names = [x.strip() for x in re.split(r",\s*and\s+|,\s*(?=[A-Z])|,\s*and\s*", auth) if x.strip()]
    out_names = [flip(n) for n in names]
    if len(out_names) > 1:
        auth2 = ", ".join(out_names[:-1]) + " and " + out_names[-1]
    else:
        auth2 = out_names[0] if out_names else auth
    return head + auth2 + ", " + tail


lines = [fix_line(l) for l in s.split("\n")]
io.open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines))
print("done")
