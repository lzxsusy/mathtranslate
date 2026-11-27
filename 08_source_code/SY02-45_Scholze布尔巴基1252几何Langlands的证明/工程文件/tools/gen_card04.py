# -*- coding: utf-8 -*-
"""从 glossary.tsv 生成 资料卡/04 的 ① 术语冻结表。"""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

BASE = Path(__file__).resolve().parent.parent.parent
rows = [
    l.split("\t")
    for l in (BASE / "工程文件" / "work" / "glossary.tsv").read_text(encoding="utf-8").splitlines()[1:]
    if l.strip()
]

out = [
    "# 04 · 术语文献勘误",
    "",
    "> 本文件办五件事：① 术语冻结表（全 123 条）；② 与香蕉空间（bananaspace.org）通行译名的增量与分歧；",
    "> ③ 参考文献逐条外核；④ 原文笔误与内部不一致；⑤ 方法与局限。",
    "",
    "## ① 术语冻结表（123 条，开工前冻结）",
    "",
    "依据代号：**L** = 本库已冻结（`01_corpus_zh/数语规范/TERMS.tsv` 或 SY02-41/SY02-26 的 glossary）；"
    "**A** = 权威通行（本库无专条，按社区通行中文，已对照香蕉空间）；**I** = 待 Lead 裁定（本文保留英文）。"
    "首现页 = 原文印刷页。",
    "",
    "| # | 英文 | 中文 | 依据 | 首现页 | 备注 |",
    "| --- | --- | --- | --- | --- | --- |",
]
for i, r in enumerate(rows, 1):
    r = (r + ["", "", "", "", ""])[:5]
    en, zh, basis, page, note = (x.strip() for x in r)
    out.append(f"| {i} | {en} | {zh} | {basis} | {page or '—'} | {note} |")

out += [
    "",
    "> 另有 6 条本库冻结值在**本文中完全不出现**（affinoid、perfectoid、diamond、prism、solid、isocrystal），"
    "已移入 `工程文件/work/glossary-本文未用.tsv`，不作覆盖率要求。这不是漏译：本文的三种 setting 是 de Rham / Betti / étale，"
    "不涉及完满空间、菱形与棱镜上同调。",
    "",
]
dst = BASE / "资料卡" / "04-术语文献勘误.md"
dst.write_text("\n".join(out), encoding="utf-8")
print(f"写入 {dst}（{len(rows)} 条）")
