#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""把式数从源码计数（340，含注释行虚高）改为 PDF 行末实测（333）。"""
import io
import os
import re

ROOT = r"C:\Users\admin\Desktop\GMN系列"
PROJ = os.path.join(ROOT, "01_翻译", "GMN3_1006.0146")
BRIEF = os.path.join(PROJ, "工程文件", "BRIEF.md")

NEW = [5, 15, 31, 32, 26, 28, 29, 19, 10, 19, 11, 23, 25, 15, 27, 18]

txt = io.open(BRIEF, encoding="utf-8").read()

# 1) 分块表：逐行替换式数列
lines = txt.split("\n")
k = 0
for i, line in enumerate(lines):
    if re.match(r"^\| ch\d\d \|", line):
        f = line.split("|")
        f[6] = " %d " % NEW[k]
        lines[i] = "|".join(f)
        k += 1
assert k == 16, k
txt = "\n".join(lines)

# 2) 元信息规模行
txt = txt.replace(
    "**编号公式 340 条**（§1 5、§2 15、§3 63、§4 55、§5 35、§6 15、§7 14、§8 19、§9 11、§10 48、§11 3、§12 12、§13 0、A 7、B 2、C 3、D 8、E 7、F 10、G 8）",
    "**编号公式 333 条**（§1 5、§2 15、§3 63、§4 54、§5 29、§6 15、§7 14、§8 19、§9 11、§10 48、§11 3、§12 12、§13 0、A 7、B 2、C 3、D 8、E 7、F 10、G 8）")

# 3) 计数口径说明
txt = txt.replace(
    "行号：`Lamination-Paper.tex`。式数与图数由 `work/chunk_stats.py` 按 `\\begin{equation}` / `align` 行与 `\\insfig` 计数，**译文落笔前须回原文复核**。",
    "行号：`Lamination-Paper.tex`（空行/注释行照原样计）。**式数取原文 PDF 行末编号实测**（`work/eqcount_pdf.py`，按右栏 x≈489–512 判据），并与源码逐节交叉核对；源码按 `\\begin{equation}`/`align` 行粗计为 340，因注释行与 align 共享编号虚高 7 条（§4 +1、§5 +6），**一律以 333 为准**。图数由 `\\insfig` 计数。")

# 4) 合计行
txt = txt.replace("式数合计 340，图数合计 52，与原文总账一致。",
                  "式数合计 333，图数合计 52，与原文总账一致（PDF 实测逐节与源码式号最大值完全吻合）。")

io.open(BRIEF, "w", encoding="utf-8", newline="").write(txt)
print("BRIEF ok")

# 5) 其他文件里的 340 表述
def sub(path, pairs):
    p = os.path.join(ROOT, path) if not os.path.isabs(path) else path
    s = io.open(p, encoding="utf-8").read()
    for a, b in pairs:
        assert a in s, (p, a[:40])
        s = s.replace(a, b)
    io.open(p, "w", encoding="utf-8", newline="").write(s)
    print("ok", path)

sub(os.path.join(PROJ, "工程文件", "STYLE_GUIDE.md"),
    [("编号公式 340 条", "编号公式 333 条（PDF 行末实测）")])

sub(os.path.join(PROJ, "工程文件", "work", "01_通读笔记.md"),
    [("340 条编号公式", "333 条编号公式")])

sub(os.path.join(PROJ, "工程文件", "work", "02_疑点清单.md"),
    [("| B8 | 全文 | 340 条编号公式的分布 | 已核（`work/eqnum.py`）：§1 5、§2 15、§3 63、§4 55、§5 35、§6 15、§7 14、§8 19、§9 11、§10 48、§11 3、§12 12、§13 0、A 7、B 2、C 3、D 8、E 7、F 10、G 8 |",
      "| B8 | 全文 | 编号公式总数 | 已定：**333 条**（PDF 行末实测，逐节 §1 5、§2 15、§3 63、§4 54、§5 29、§6 15、§7 14、§8 19、§9 11、§10 48、§11 3、§12 12、§13 0、A 7、B 2、C 3、D 8、E 7、F 10、G 8）。早先按源码粗计 340，因 `%` 注释掉的 equation 行（§4 1 条、§5 3 条）与 align 共享编号虚高 7 条；**已弃用 340** |")])

sub(os.path.join(ROOT, "排期.md"),
    [("340 条编号公式", "333 条编号公式")])

sub(os.path.join(ROOT, "进度.md"),
    [("340 条编号公式", "333 条编号公式")])
