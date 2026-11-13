# -*- coding: utf-8 -*-
"""check_toc.py — 比对目录页码与正文实际（印刷）页码"""
import re
import pymupdf

PDF = r"<本地路径>"
HEADS = [
    "引言（Introduction）",
    "黎曼曲面的模空间（Moduli spaces of Riemann surfaces）",
    "模空间的定义（Definition of the moduli spaces）",
    "分层结构与重言映射（Stratification and tautological maps）",
    "相交理论与 Witten 猜想（Intersection theory and Witten",
    "上同调场论（Cohomological field theories）",
    "公理（Axioms）",
    "Givental 作用（Givental",
    "与拓扑递归的联系（Connection to topological recursion）",
    "进一步的方向（Further directions）",
    "双曲曲面的模空间（Moduli of hyperbolic surfaces）",
    "弦论与映射的模空间（String theory and moduli of maps）",
    "参考文献",
]

doc = pymupdf.open(PDF)
toc_txt = doc[1].get_text()

# 从目录页解析：标题 + 页码（页码是行末的孤立数字）
toc_map = {}
for line in toc_txt.splitlines():
    m = re.match(r"^\s*(\d+(?:\.\d+)?)\s*(.+?)\s*\.{2,}\s*(\d{1,3})\s*$", line)
    if m:
        toc_map[m.group(2).strip()] = int(m.group(3))
    else:
        m2 = re.match(r"^\s*(\d+(?:\.\d+)?)\s*(\D.*)$", line)
        if m2:
            toc_map.setdefault("__pending__", None)
            toc_map[m2.group(2).strip()] = None

# 正文实际页：查找标题出现的第一个非目录页，并取该页页眉印刷页码
actual = {}
for h in HEADS:
    for i in range(2, len(doc)):
        t = doc[i].get_text()
        if h in t:
            # 印刷页码：页眉右上角数字（取页面文本第一行的数字？）改用页脚/页眉搜索
            head = t.splitlines()
            pnum = None
            for ln in head[:5]:
                ln = ln.strip()
                if re.fullmatch(r"\d{1,3}", ln):
                    pnum = int(ln)
                    break
            actual[h] = (i + 1, pnum)
            break

print("%-58s %8s %8s" % ("标题", "目录页", "实际页"))
ok = True
for h in HEADS:
    a = actual.get(h)
    # 目录里匹配（标题可能被折行，做前缀匹配）
    tp = None
    for k, v in toc_map.items():
        if k and v is not None and (k.startswith(h[:12]) or h[:12] in k):
            tp = v
            break
    print("%-58s %8s %8s" % (h[:56], tp if tp is not None else "?", a[1] if a else "?"))
    if tp is not None and a and a[1] is not None and tp != a[1]:
        ok = False
print("TOC 一致：" , ok)
