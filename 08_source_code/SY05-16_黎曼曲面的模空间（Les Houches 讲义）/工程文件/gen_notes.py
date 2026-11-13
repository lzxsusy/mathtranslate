# -*- coding: utf-8 -*-
"""gen_notes.py — 从 src/*.tex 抽取全部 Tutor Note，生成 译注汇总.md（按原文页序）

用法： python gen_notes.py
"""
import glob, os, re

ROOT = r"<本地路径>"
ORDER = ["sec1.tex", "sec21.tex", "sec22.tex", "sec23a.tex", "sec23b.tex",
         "sec31.tex", "sec32.tex", "sec33.tex", "sec4.tex", "refs.tex"]
TITLE = {
    "sec1.tex": "§1 引言",
    "sec21.tex": "§2.1 模空间的定义",
    "sec22.tex": "§2.2 分层结构与重言映射",
    "sec23a.tex": "§2.3 相交理论与 Witten 猜想（前半）",
    "sec23b.tex": "§2.3 相交理论与 Witten 猜想（后半）",
    "sec31.tex": "§3.1 公理",
    "sec32.tex": "§3.2 Givental 作用",
    "sec33.tex": "§3.3 与拓扑递归的联系",
    "sec4.tex": "§4 进一步的方向",
    "refs.tex": "参考文献",
}

out = []
out.append("# 译注汇总（Tutor Notes）\n")
out.append("> 本文件由 `gen_notes.py` 从 `src/*.tex` 的 `% [Tutor Note: ...]` 注释自动抽取生成。\n")
out.append("> 这些批注在排版中不出现，仅供读者对照源码阅读；每条前面的页码为原文页码。\n")

total = 0
for name in ORDER:
    p = os.path.join(ROOT, "src", name)
    if not os.path.exists(p):
        continue
    lines = open(p, encoding="utf-8").read().splitlines()
    notes = []
    page = None
    for ln in lines:
        s = ln.strip()
        m = re.match(r"^%\s*\[原文 p\.(\d+)\]", s)
        if m:
            page = m.group(1)
        m = re.search(r"%\s*\[Tutor Note:\s*(.*)$", ln)
        if m:
            txt = m.group(1)
            txt = re.sub(r"\]\s*$", "", txt).strip()
            notes.append((page, txt))
    if not notes:
        continue
    out.append("\n## %s\n" % TITLE.get(name, name))
    for i, (pg, txt) in enumerate(notes, 1):
        total += 1
        out.append("%d. %s%s" % (i, ("（原文 p.%s）" % pg) if pg else "", txt))
    out.append("\n")

out.insert(2, "\n**共 %d 条批注。**\n" % total)

with open(os.path.join(ROOT, "译注汇总.md"), "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(out))
print("译注汇总.md：%d 条批注" % total)
