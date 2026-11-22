# -*- coding: utf-8 -*-
r"""由 条款索引合并.tsv 生成 资料卡/03-条款索引.md。"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PROJ = os.path.dirname(ROOT)
SRC = os.path.join(ROOT, "work", "条款索引合并.tsv")
OUT = os.path.join(PROJ, "资料卡", "03-条款索引.md")

SEC_TITLE = {
    "2": "§2 $p$ 进群的几何 Satake",
    "3": "§3 范畴迹构造",
    "4": "§4 几何 Satake 的范畴迹",
    "5": "§5 对 Shimura 簇的应用",
    "6": "§6 附录：由对应构造的范畴",
}

rows = [l.rstrip("\n").split("\t") for l in open(SRC, encoding="utf-8") if l.strip()]

lines = []
lines.append("# 条款索引 · SY02-20\n")
lines.append("「译本页」为 PDF 页序（封面 = 1，不编号；印刷页 = PDF 页 − 1）；"
             "「原文页」为底本 arXiv:1810.07375 的 PDF 页序。")
lines.append("带 \\* 的页码表示该对象原文没有给 `\\label`，页面取自相邻对象，仅供定位。\n")
lines.append("共 **140 个编号对象**：75 个定理类（定理、命题、引理、推论、猜想、定义、"
             "构造、例、注）+ 65 个编号公式。\n")

cur_sec = None
cur_sub = None
for num, kind, tpage, opage, key in rows:
    sec, sub = num.split(".")[0], num.split(".")[1]
    if sec != cur_sec:
        if cur_sec is not None:
            lines.append("")
        cur_sec = sec
        cur_sub = None
        lines.append("## %s\n" % SEC_TITLE.get(sec, "§" + sec))
        lines.append("| 编号 | 类别 | 译本页 | 原文页 | 原文 label |")
        lines.append("| --- | --- | --- | --- | --- |")
    label = "—" if key == "-" else "`%s`" % key
    shown = ("(%s)" % num) if kind == "公式" else ("%s %s" % (kind, num))
    lines.append("| %s | %s | %s | %s | %s |"
                 % (shown, kind, tpage, opage if opage != "-" else "—", label))

open(OUT, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("wrote", OUT, len(rows))
