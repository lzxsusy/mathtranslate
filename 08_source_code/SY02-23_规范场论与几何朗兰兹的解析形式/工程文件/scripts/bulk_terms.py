# -*- coding: utf-8 -*-
import pathlib, re
root = pathlib.Path(r"C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-23_规范场论与几何朗兰兹的解析形式\源码\chunks")
repls = [
    ("起来来", "起来"),
    ("表示表示", "表示"),
    ("Poisson 括号", "泊松括号"),
    ("Poisson 交换", "泊松交换"),
    ("自旋结构", "旋量结构"),
    ("局部算子", "局部算符"),
    ("谱流算子", "谱流算符"),
    ("微分算符", "微分算子"),
    ("单值性", "单值"),
    ("opers", "oper"),
    ("Calabi-Yau", "Calabi–Yau"),
    ("规范理论", "规范场论"),
    (r"\caption{\small  (", r"\caption{\small ("),
]
for p in sorted(root.glob("ch*.tex")):
    if p.name == "ch17.tex":
        continue
    s = p.read_text(encoding="utf-8")
    orig = s
    for a, b in repls:
        s = s.replace(a, b)
    if s != orig:
        p.write_text(s, encoding="utf-8")
        print(p.name, "updated")
