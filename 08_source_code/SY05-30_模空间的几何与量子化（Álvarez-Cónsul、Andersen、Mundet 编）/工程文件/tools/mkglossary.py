# -*- coding: utf-8 -*-
"""工程文件/work/术语表.tsv → 成品/术语对照表.md（Markdown 表格，转义竖线）。"""
import csv, io, os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(ROOT, "工程文件", "work", "术语表.tsv")
OUT = os.path.join(ROOT, "成品", "术语对照表.md")

rows = list(csv.reader(io.open(SRC, encoding="utf-8"), delimiter="\t"))
hdr, body = rows[0], [r for r in rows[1:] if r and r[0].strip()]

def esc(x):
    return str(x).replace("|", "\\|").strip()

out = [
    "# SY05-30 术语对照表",
    "",
    "底本：*Geometry and Quantization of Moduli Spaces* 第 2 章（Schaffhauser，印刷页 67–108）。",
    "",
    "口径：术语先冻结再落笔（《纪律》§2.5）。`依据` 列分三级：**A** = 外部权威译法可查；**B** = 本库既有译法；**I** = 译者自定（译注里给理由）。",
    "",
    "| # | English | 中文 | 依据 | 首现 | 备注 |",
    "| --- | --- | --- | --- | --- | --- |",
]
for i, r in enumerate(body, 1):
    r = (r + [""] * 5)[:5]
    out.append("| %d | %s | %s | %s | %s | %s |" % (i, esc(r[0]), esc(r[1]), esc(r[2]), esc(r[3]), esc(r[4])))
out += ["", "共 %d 条。机读版：`工程文件/work/术语表.tsv`。" % len(body), ""]

io.open(OUT, "w", encoding="utf-8", newline="\n").write("\n".join(out))
print("rows", len(body), "->", OUT)
