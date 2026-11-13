# -*- coding: utf-8 -*-
"""生成附录 B 术语表、附录 C 页码对照表、附录 D 译注索引。"""
import io
import json
import os
import re

ROOT = r"<本地路径>"
SRC = os.path.join(ROOT, "src")

# ---------------- B. 术语表 ----------------
rows = []
for line in io.open(os.path.join(ROOT, "work", "terms_zh.tsv"), encoding="utf-8").read().splitlines()[1:]:
    if not line.strip():
        continue
    parts = line.split("\t")
    while len(parts) < 3:
        parts.append("")
    en, zh, note = parts[0].strip(), parts[1].strip(), parts[2].strip()
    if not en:
        continue
    en = en.replace("&", r"\&").replace("_", r"\_").replace("%", r"\%").replace("#", r"\#")
    rows.append((en, zh, note))

terms = [r"% 附录 B 术语英中对照表（由 work/terms_zh.tsv 生成）",
         r"\section{术语英中对照表（译者所加）}",
         r"\addcontentsline{toc}{section}{附录 B\quad 术语英中对照表}",
         r"\markboth{附录 B\quad 术语英中对照表}{附录 B\quad 术语英中对照表}",
         r"下表列出本书正文中出现的专门术语及其统一译名。凡「备注」栏注明「保留英文」的，",
         r"正文中一律使用英文原词；注明「首现括注」的，第一次出现时写作「中文（English）」。",
         r"同一术语在全书中只允许一种译法；若发现不一致，以本表为准。",
         r"",
         r"{\small",
         r"\begin{longtable}{p{5.0cm}p{5.6cm}p{3.6cm}}",
         r"\toprule",
         r"英文术语 & 中文译名 & 说明 \\",
         r"\midrule",
         r"\endfirsthead",
         r"\toprule",
         r"英文术语 & 中文译名 & 说明 \\",
         r"\midrule",
         r"\endhead",
         r"\bottomrule",
         r"\endfoot"]
for en, zh, note in rows:
    terms.append("%s & %s & %s \\\\" % (en, zh, note))
terms += [r"\end{longtable}", r"}", r""]
io.open(os.path.join(SRC, "back", "terms.tex"), "w", encoding="utf-8").write("\n".join(terms))

# ---------------- C. 页码对照表 ----------------
pages = json.load(io.open(os.path.join(ROOT, "work", "page_start.json"), encoding="utf-8"))
pages = {int(k): v for k, v in pages.items()}
labels = [
    (171, "§1\\quad 引言"),
    (196, "§1a\\quad 主要结果"),
    (215, "§1b\\quad 多重单值性"),
    (331, "§1c\\quad Hirzebruch 面"),
    (354, "§1d\\quad 全文结构"),
    (365, "§2\\quad 定理的证明"),
    (367, "§2a\\quad 预备与证明蓝图"),
    (415, "§2b\\quad 扇形下降与真下降"),
    (492, "§2c\\quad 环面丛"),
    (508, "§2d\\quad Hirzebruch 面（证明）"),
    (516, "§3\\quad 代数预备"),
    (518, "§3a\\quad $A_\\infty$ 范畴与 dg 范畴"),
    (811, "§3c\\quad 群作用与轨道范畴"),
    (857, "§3d\\quad dg 范畴的张量积"),
    (1055, "§4\\quad 离散商的 Fukaya 范畴"),
    (1065, "§4a\\quad 带群作用的 Weinstein 扇形"),
    (1413, "§4b\\quad 商的包裹 Fukaya 范畴"),
    (1433, "§4c\\quad Künneth 定理与形变不变性"),
    (1466, "§4d\\quad Kartal 修改"),
    (1805, "§5\\quad $G$-等变层"),
    (1808, "§5a\\quad $G$-等变 $\\mathcal{O}_X$-模范畴"),
    (2170, "§5b\\quad 特征群 $\\widehat{G}$ 的作用"),
    (2416, "§5c\\quad 权空间分解"),
    (2671, "§5d\\quad 限制到子群概形"),
    (3013, "§5e\\quad 群概形作用的乘积"),
    (3291, "§6\\quad 扭 Künneth 公式"),
    (3293, "§6a\\quad 导出 dg 范畴"),
    (3618, "§6b\\quad $G$-等变导出 dg 范畴"),
    (4216, "§6c\\quad 扭 Künneth 公式（主定理）"),
    (4656, "附录 A\\quad Čech 复形的 Eilenberg--Zilber 收缩"),
    (4663, "附录 Aa\\quad 链复形的 Eilenberg--Zilber 收缩"),
    (4873, "附录 Ab\\quad Čech 复形的 Eilenberg--Zilber 收缩"),
]
pm = [r"% 附录 C 原文页码对照表（由 work/page_start.json 生成）",
      r"\section{原文页码对照表（译者所加）}",
      r"\label{sec:pagemap}",
      r"\addcontentsline{toc}{section}{附录 C\quad 原文页码对照表}",
      r"\markboth{附录 C\quad 原文页码对照表}{附录 C\quad 原文页码对照表}",
      r"下表给出原文（arXiv:2611.07202v1，56 页）每一页起始处所在的（小）节。",
      r"译文中每一页起点处用 \verb|% [原文 p.N]| 注释标出，便于逐页对照；",
      r"因中英文排版不同，译文的节与原文的节并不同页，故对照以节为准。",
      r"",
      r"{\small",
      r"\begin{longtable}{p{2.4cm}p{10.0cm}}",
      r"\toprule",
      r"原文页码 & 该页起始处所在的小节 \\",
      r"\midrule",
      r"\endfirsthead",
      r"\toprule",
      r"原文页码 & 该页起始处所在的小节 \\",
      r"\midrule",
      r"\endhead",
      r"\bottomrule",
      r"\endfoot"]
for p in sorted(pages):
    L = pages[p]
    lab = ""
    if p >= 52:
        lab = "参考文献"
    else:
        for line_no, name in labels:
            if line_no <= L:
                lab = name
    pm.append(r"p.%d & %s \\" % (p, lab))
pm += [r"\end{longtable}", r"}", r""]
io.open(os.path.join(SRC, "back", "pagemap.tex"), "w", encoding="utf-8").write("\n".join(pm))

# ---------------- D. 译注索引 ----------------
def find_balanced(text, start):
    depth = 0
    i = start
    while i < len(text):
        c = text[i]
        if c == "\\":
            i += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return text[start + 1:i], i + 1
        i += 1
    return text[start + 1:], len(text)


def scan_events(text):
    events = []
    for m in re.finditer(r"\\(sub)?section\s*(\[[^\]]*\])?\s*\{", text):
        arg, _ = find_balanced(text, m.end() - 1)
        events.append((m.start(), "sec", arg))
    for m in re.finditer(r"<本地路径>*\[", text):
        j = text.index("[", m.end() - 1)
        depth = 0
        k = j + 1
        while k < len(text):
            c = text[k]
            if c == "\\":
                k += 2
                continue
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
            elif c == "]" and depth == 0:
                break
            k += 1
        arg = text[j + 1:k].strip()
        if arg.startswith("{") and arg.endswith("}") and find_balanced(arg, 0)[1] == len(arg):
            arg = arg[1:-1].strip()
        events.append((m.start(), "yz", arg))
    for m in re.finditer(r"<本地路径>*\{", text):
        arg, _ = find_balanced(text, m.end() - 1)
        events.append((m.start(), "cb", arg))
    events.sort()
    return events


entries = []
concepts = []
sec = ""
for i in range(15):
    path = os.path.join(SRC, "chunks", "ch%02d.tex" % i)
    if not os.path.isfile(path):
        continue
    text = io.open(path, encoding="utf-8").read()
    for _, kind, arg in scan_events(text):
        if kind == "sec":
            sec = re.sub(r"<本地路径>]*\}", "", arg).strip()
        elif kind == "yz":
            entries.append((arg.strip(), sec))
        else:
            concepts.append((arg.strip(), sec))

ni = [r"% 附录 D 译注与概念框索引（自动生成）",
      r"\section{译注与概念框索引（译者所加）}",
      r"\addcontentsline{toc}{section}{附录 D\quad 译注与概念框索引}",
      r"\markboth{附录 D\quad 译注与概念框索引}{附录 D\quad 译注与概念框索引}",
      r"\subsection*{译注}",
      r"\begin{enumerate}[label={译注 \arabic*：},leftmargin=2.8cm,itemsep=1pt]"]
for title, s in entries:
    ni.append(r"\item %s \quad（%s）" % (title, s))
ni += [r"\end{enumerate}", r"", r"\subsection*{概念回顾}",
       r"\begin{itemize}[leftmargin=1.2em,itemsep=1pt]"]
for name, s in concepts:
    ni.append(r"\item \textbf{%s}\quad（%s）" % (name, s))
ni += [r"\end{itemize}", r""]
io.open(os.path.join(SRC, "back", "notes-index.tex"), "w", encoding="utf-8").write("\n".join(ni))

print("terms rows:", len(rows), "pages:", len(pages), "yizhu:", len(entries), "concept:", len(concepts))
