# -*- coding: utf-8 -*-
"""扫描原文 tex，给出：每节编号公式数、\\label{eq:..} -> 公式号。
编号与原文一致：numberwithin{equation}{section}，\\section 重置计数器。
实现：单次扫描字符串，遇到环境起点就整段吃掉，不再回退。"""
import re, io, json

SRC = r"C:/Users/admin/Desktop/GMN系列/00_原文/GMN3_1006.0146/1006.0146v2_src/Lamination-Paper.tex"
txt = io.open(SRC, encoding="utf-8", errors="replace").read()
line_of = lambda pos: txt.count("\n", 0, pos) + 1

# 1) 顶层 \section 起点（不含 \section*）
secs = []   # (line, name)
for m in re.finditer(r"(?m)^\s*\\section\{([^}]*)\}", txt):
    nxt = txt[m.end():m.end()+1]
    if nxt == "*":
        continue
    secs.append((line_of(m.start() + m.group(0).index("\\section")), m.group(1).strip()))
secs.sort()

# 2) 收集编号公式：环境 -> 每个编号行生成一个 (pos, label列表)
units = []   # (pos, [labels])
BODY0 = txt.find("\\begin{document}")
pat = re.compile(r"\\begin\{(equation|align|eqnarray|gather|multline|flalign)\}")
i = 0
while True:
    m = pat.search(txt, max(i, BODY0))
    if not m:
        break
    env = m.group(1)
    end = txt.find("\\end{%s}" % env, m.end())
    if end < 0:
        break
    body = txt[m.end():end]
    if env == "equation":
        if "\\nonumber" not in body and "\\notag" not in body:
            units.append((m.start(), re.findall(r"\\label\{([^}]*)\}", body)))
    else:
        # 顶层切行
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
            units.append((m.start(), re.findall(r"\\label\{([^}]*)\}", r)))
    i = end + 5

# 3) 分配节号与式号
sect_lines = [s[0] for s in secs]
def sec_index(line):
    idx = 0
    for j, L in enumerate(sect_lines):
        if L <= line:
            idx = j
    return idx

counts = {}
label_no = {}
for pos, labels in units:
    ln = line_of(pos)
    si = sec_index(ln)
    counts[si] = counts.get(si, 0) + 1
    num = "%d.%d" % (si + 1, counts[si])
    for lab in labels:
        label_no[lab] = num

print("sections: %d" % len(secs))
for j, (ln, nm) in enumerate(secs):
    print("  §%-2d line %5d  eqs %3d  %s" % (j + 1, ln, counts.get(j, 0), nm))

want = ["eq:intro-eq", "eq:trh-large-r", "eq:Def-Framed-PSC", "eq:PSC-one", "eq:form-gen",
        "eq:L-5d-Holon", "eq:wilson-vev-nf0", "eq:Nf4-Wilson", "eq:Def-BPS-Walls",
        "eq:Spin-KS-tmn-S", "eq:Spin-KS-ii"]
print("\nlabels:")
for w in want:
    print("  %-22s -> %s" % (w, label_no.get(w, "MISSING")))
json.dump(label_no, io.open(r"C:/Users/admin/Downloads/_gmn3_labels.json", "w"), indent=0)
print("\nnumbered units total: %d, labels total: %d" % (len(units), len(label_no)))
