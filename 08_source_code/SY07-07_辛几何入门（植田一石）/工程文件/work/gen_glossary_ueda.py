# -*- coding: utf-8 -*-
"""由 work/TERMS.md 生成 src/chunks/appendix_glossary.tex（术语对照表）。
用法: python gen_glossary_ueda.py
"""
import io
import os
import re

ROOT = r"<本地路径>"
SRC = os.path.join(ROOT, "work", "TERMS.md")
OUT = os.path.join(ROOT, "src", "chunks", "appendix_glossary.tex")

def read(p):
    with io.open(p, encoding="utf-8") as f:
        return f.read().replace("\r\n", "\n")

def esc(s):
    s = s.replace("\u30fb", "\u00b7").replace("\u03c9", "$\\omega$")
    s = s.strip()
    s = s.replace("&", r"\&").replace("%", r"\%").replace("#", r"\#").replace("_", r"\_")
    return s

def table(title, rows):
    out = []
    out.append("\\section*{%s}" % title)
    out.append("\\addcontentsline{toc}{section}{%s}" % title)
    out.append("{\\small")
    out.append("\\begin{longtable}{p{0.31\\linewidth} p{0.26\\linewidth} p{0.25\\linewidth}}")
    out.append("\\toprule")
    out.append("日文原文 & 中文译名 & 备注 \\\\")
    out.append("\\midrule")
    out.append("\\endhead")
    for ja, zh, note in rows:
        note = esc(note)
        out.append("%s & %s & %s \\\\" % (esc(ja), esc(zh), note))
    out.append("\\bottomrule")
    out.append("\\end{longtable}")
    out.append("}")
    out.append("")
    return out

text = read(SRC)
lines = text.split("\n")

# ---- 1. 从「1. 基础表」的 ｜ 分隔段落提取基础术语 ----
base_rows = []
in_base = False
for ln in lines:
    if ln.startswith("## 1."):
        in_base = True
        continue
    if in_base:
        if ln.startswith("## "):
            break
        if "｜" in ln:
            for item in ln.split("｜"):
                item = item.strip().rstrip("。")
                if "=" in item:
                    ja, zh = item.split("=", 1)
                    base_rows.append((ja.strip(), zh.strip(), ""))

# ---- 2. 解析 ### 小节里的 markdown 表格 ----
sections = []
cur = None
for ln in lines:
    if ln.startswith("### "):
        cur = {"title": ln[4:].strip(), "rows": []}
        sections.append(cur)
        continue
    if ln.startswith("## "):
        cur = None
        continue
    if cur is not None and ln.startswith("|"):
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if not cells or cells[0] in ("日文", "") or set(cells[0]) <= set("-: "):
            continue
        while len(cells) < 3:
            cells.append("")
        cur["rows"].append((cells[0], cells[1], cells[2]))

out = []
out.append("% 自动生成：work/gen_glossary_ueda.py（源自 work/TERMS.md）——勿手工编辑")
out.append("\\chapter*{附录 B\\quad 术语对照表}")
out.append("\\addcontentsline{toc}{chapter}{附录 B\\quad 术语对照表}")
out.append("\\markboth{附录 B\\quad 术语对照表}{附录 B\\quad 术语对照表}")
out.append("")
out.append("本表列出书中反复出现的主要术语的日文原文、中文译名与必要的备注。"
           "中译本的处理原则是：中文学界有稳定通行译名者用中文译名，"
           "无稳定译名、或硬译反而妨碍与文献对照者保留原文（表中注明「保留」）。"
           "人名、机构名与定理名称不列入，书中一律保留原文。<本地路径>")
out.append("")
out.append("术语的日文原文按原书五十音顺序编排的索引，中译本不照录；"
           "读者需要按日文检索时，可用本表对照。表中括号内的西文为英文或法文原词，"
           "供查阅外文文献之用。<本地路径>")
out.append("")

if base_rows:
    out += table("B.1 辛几何基础术语", base_rows)

for i, sec in enumerate(sections, start=2):
    if not sec["rows"]:
        continue
    title = "B.%d %s" % (i, re.sub(r"^\d+\.\d+\s*", "", sec["title"]))
    title = re.sub(r"（第 ([\d、]+) 章）", r"（第 \1 章）", title)
    out += table(title, sec["rows"])

out.append("\\section*{B.%d 记号约定}" % (len(sections) + 2))
out.append("\\addcontentsline{toc}{section}{B.%d 记号约定}" % (len(sections) + 2))
out.append("")
out.append("\\begin{itemize}[leftmargin=1.6em,itemsep=3pt]")
out.append("\\item 辛形式 $\\omega$；近复结构 $J$；黎曼度量 $g$；复结构 $I$。")
out.append("\\item 流形 $M$；切丛 $TM$；余切丛 $T^*M$；外微分 $\\rd$。")
out.append("\\item 场论：$\\nabla$ 为联络，$F_\\nabla$ 为曲率，$\\cA$ 为联络空间，"
           "$\\cG$ 为规范群，$\\cM$ 为模空间。")
out.append("\\item 原书用 $\\mathbb{P}^2$ 等记法表示复射影空间，中译本统一写作 $\\CP^2$。")
out.append("\\end{itemize}")
out.append("")

body = "\n".join(out).replace("\n\n\n", "\n\n")
with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write(body)

print("sections:", len(sections), "base:", len(base_rows),
      "table rows:", sum(len(s["rows"]) for s in sections))
print("written:", OUT)

