# -*- coding: utf-8 -*-
"""把 glossary.tsv 导出为交付用术语对照表（Markdown + TSV）。"""
import csv, io

src = r"C:\Users\admin\Desktop\数译发布\shuyi\translations\SY07-08\工程文件\glossary.tsv"
rows = []
with open(src, encoding="utf-8") as f:
    for line in f:
        line = line.rstrip("\n")
        if not line.strip():
            continue
        parts = line.split("\t")
        while len(parts) < 6:
            parts.append("")
        rows.append(parts[:6])

rows.sort(key=lambda r: r[0].lower())

mode_name = {"cn": "译中文", "keep": "保留英文"}
md = io.StringIO()
md.write("# 术语对照表 — SY07-08 扶磊《代数几何》（第二版）中文译注本\n\n")
md.write("列：英文 | 中文 | 处理 | 首现原书页 | 备注。`处理` 为「译中文」或「保留英文」；"
         "「保留英文」用于通行译名不唯一或人名、缩写。\n\n")
md.write(f"共 {len(rows)} 条。\n\n")
md.write("| 英文 | 中文 | 处理 | 首现页 | 备注 |\n|---|---|---|---|---|\n")
for en, zh, mode, grade, page, note in rows:
    md.write(f"| {en} | {zh} | {mode_name.get(mode, mode)} | {page} | {note} |\n")

out = r"C:\Users\admin\Desktop\数译发布\shuyi\translations\SY07-08\成品\SY07-08_术语对照表.md"
open(out, "w", encoding="utf-8", newline="\n").write(md.getvalue())
print("写出", out, len(rows), "条")
