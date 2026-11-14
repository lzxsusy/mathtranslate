import re

# ---------------- README ----------------
p = "README.md"
lines = open(p, encoding="utf-8").read().splitlines()
out = []
info = {"83 条学术译注": "84 条学术译注",
        "83 条译注的汇总索引": "84 条译注的汇总索引",
        "译注 1–83": "译注 1–84",
        "| **合计** | **83** |": "| **合计** | **84** |",
        "| 原文疑误 | 13 |": "| 原文疑误 | 14 |"}
new_row = ("| 14 | p.4 | 式 (2.5) 的 $E_i=-\\partial_iA_0-\\partial_0A_i$ 与 (2.6) 的 "
           "$J^i=\\frac{k}{2\\pi}\\varepsilon^{ij}E_j$ 仅在 $A_0=0$（原文随后一直采用的规范）时自洽；"
           "由 (2.4) 直接算得 $J^i=\\frac{k}{2\\pi}\\varepsilon^{ij}(E_j+2\\partial_jA_0)$ | "
           "定义/规范不自洽（在所用规范下无碍） |")
for ln in lines:
    for a, b in info.items():
        ln = ln.replace(a, b)
    if ln.startswith("| 13 | p.30 |"):
        out.append(ln)
        out.append(new_row)
    else:
        out.append(ln)
open(p, "w", encoding="utf-8").write("\n".join(out) + "\n")
print("README done; rows:", sum(1 for l in out if re.match(r"\| \d+ \| p\.", l)))

# ---------------- 审校报告 ----------------
p = "审校报告.md"
t = open(p, encoding="utf-8").read()
t = t.replace("**有 5 处实质性数学/表述错误、8 处排印或符号笔误**",
              "**有 6 处实质性数学/表述问题、8 处排印或符号笔误**")
t = t.replace("## 二、可确证的原文笔误（13 处，正文照录 + 批注）",
              "## 二、可确证的原文笔误（14 处，正文照录 + 批注）")
t = t.replace("**对这 13 处的处理原则**", "**对这 14 处的处理原则**")
lines = t.splitlines()
idx = [i for i, l in enumerate(lines) if re.match(r"\| \d+ \| p\.", l)]
assert len(idx) == 13, len(idx)
newrow = ("| 3 | p.4 | 式 (2.5) $E_i\\equiv-\\partial_iA_0-\\partial_0A_i$ 与式 (2.6) "
          "$J^i=\\frac{k}{2\\pi}\\varepsilon^{ij}E_j$ | 由 (2.4) 的 $\\mu=i$ 分量直接算得 "
          "$J^i=\\frac{k}{2\\pi}\\varepsilon^{ij}(E_j+2\\partial_jA_0)$，与 (2.6) 差一项 "
          "$\\frac{k}{\\pi}\\varepsilon^{ij}\\partial_jA_0$；仅当 $\\partial_jA_0=0$（如原文此后一直采用的 "
          "$A_0=0$ 库仑规范）时两式一致。属定义与规范使用的不自洽，不影响后续结论 | 照录 + 原文疑误批注（译注 11），并指出在 $A_0=0$ 下无碍 |")
# renumber rows 3..13 -> 4..14 (descending)
for i in reversed(idx[2:]):
    m = re.match(r"\| (\d+) \|", lines[i])
    n = int(m.group(1))
    lines[i] = lines[i].replace(f"| {n} |", f"| {n+1} |", 1)
lines[idx[2]] = newrow + lines[idx[2]].split("|", 2)[2].split(" | ", 0)[0] if False else lines[idx[2]]
# insert new row before (now renumbered) old row 3, i.e. before index idx[2]
lines.insert(idx[2], newrow)
open(p, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("report rows:", sum(1 for l in lines if re.match(r"\| \d+ \| p\.", l)))
