# -*- coding: utf-8 -*-
"""分块统计：每块的行号区间、节标题、编号公式数、插图数。"""
import re, io

SRC = r"C:/Users/admin/Desktop/GMN系列/00_原文/GMN3_1006.0146/1006.0146v2_src/Lamination-Paper.tex"
txt = io.open(SRC, encoding="utf-8", errors="replace").read()
lines = txt.split("\n")
line_of = lambda pos: txt.count("\n", 0, pos) + 1

BODY0 = txt.find("\\begin{document}")
units = []      # (line, kind)
pat = re.compile(r"\\begin\{(equation|align|eqnarray|gather|multline|flalign)\}")
i = max(0, BODY0)
while True:
    m = pat.search(txt, i)
    if not m:
        break
    env = m.group(1)
    end = txt.find("\\end{%s}" % env, m.end())
    if end < 0:
        break
    body = txt[m.end():end]
    ln = line_of(m.start())
    if env == "equation":
        if "\\nonumber" not in body and "\\notag" not in body:
            units.append((ln, "eq"))
    else:
        rows, depth, cur, k = [], 0, [], 0
        while k < len(body):
            if body.startswith("\\begin{", k):
                depth += 1; cur.append("\\begin{"); k += 7; continue
            if body.startswith("\\end{", k):
                depth -= 1; cur.append("\\end{"); k += 5; continue
            if depth == 0 and body.startswith("\\\\", k):
                rows.append("".join(cur)); cur = []; k += 2; continue
            cur.append(body[k]); k += 1
        rows.append("".join(cur))
        for r in rows:
            if not r.strip() or "\\nonumber" in r or "\\notag" in r or "\\intertext" in r:
                continue
            units.append((ln, "eq"))
    i = end + 5

figs = []
for mm in re.finditer(r"\\insfig\{", txt):
    figs.append(line_of(mm.start()))
for mm in re.finditer(r"\\instwofigs", txt):
    figs.append(line_of(mm.start())); figs.extend([line_of(mm.start())] * 1)
for mm in re.finditer(r"\\insthreefigs", txt):
    figs.append(line_of(mm.start()))

chunks = [(360, 560), (561, 1028), (1029, 1506), (1507, 2020), (2021, 2606),
          (2607, 3114), (3115, 3694), (3695, 4378), (4379, 4685), (4686, 5050),
          (5051, 5359), (5360, 5654), (5655, 5863), (5864, 6289), (6290, 6895),
          (6896, 7129)]
pages = [(4, 6), (7, 13), (14, 21), (22, 27), (28, 38), (39, 47), (48, 56),
         (57, 66), (67, 72), (73, 78), (79, 85), (86, 92), (93, 98), (99, 106),
         (107, 114), (115, 124)]

print("| 块 | 行号区间 | 编号式 | 图 | 节起始 |")
print("|---|---|---|---|---|")
tot_eq = tot_fig = 0
for k, ((a, b), (p1, p2)) in enumerate(zip(chunks, pages), 1):
    neq = sum(1 for (ln, _) in units if a <= ln <= b)
    nfig = sum(1 for ln in figs if a <= ln <= b)
    secs = [l.strip() for l in lines[a - 1:b] if re.match(r"\s*\\section\{", l)]
    secs = [re.sub(r"\\section\{(.*)\}", r"\1", s)[:40] for s in secs]
    tot_eq += neq; tot_fig += nfig
    print("| ch%02d | %d–%d | %d | %d | %s |" % (k, a, b, neq, nfig, " / ".join(secs)))
print("TOTAL eq=%d fig=%d" % (tot_eq, tot_fig))
