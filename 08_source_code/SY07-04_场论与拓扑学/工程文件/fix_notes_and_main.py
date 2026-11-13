# -*- coding: utf-8 -*-
"""1) main.tex：把 chunks/index_notes 注入 backmatter（在参考文献之前）
   2) gen_notes.py：用显式的 chunk→章 映射代替跨文件继承（继承在长文件链上失效）"""
import os, re

ROOT = r"<本地路径>"

# ---------- 1) main.tex ----------
mp = os.path.join(ROOT, "src", "main.tex")
t = open(mp, encoding="utf-8").read()
old = "<本地路径>"
new = "<本地路径>"
if old in t:
    t = t.replace(old, new)
    open(mp, "w", encoding="utf-8").write(t)
    print("main.tex: appended index_notes OK")
else:
    print("main.tex: pattern not found")

# ---------- 2) gen_notes.py：加章映射 ----------
gp = os.path.join(ROOT, "gen_notes.py")
g = open(gp, encoding="utf-8").read()
if "CH_MAP = {" not in g:
    anchor = "NOTE_RE = re.compile"
    chmap = '''CH_MAP = {
    "fm": "序与理论的概要与展望",
    "ch01a": "共形场理论的几何", "ch01b": "共形场理论的几何",
    "ch01c": "共形场理论的几何", "ch01d": "共形场理论的几何",
    "ch02a": "Jones--Witten 理论", "ch02b": "Jones--Witten 理论",
    "ch02c": "Jones--Witten 理论", "ch02d": "Jones--Witten 理论",
    "ch02e": "Jones--Witten 理论",
    "ch03a": "Chern--Simons 微扰理论", "ch03b": "Chern--Simons 微扰理论",
    "ch03c": "Chern--Simons 微扰理论",
    "future": "今后的方向与课题", "references": "参考文献",
}

'''
    g = g.replace(anchor, chmap + anchor, 1)
    # 在第一遍里用映射覆盖 chapter
    g = g.replace(
        "        chapter, section, page = \"\", \"\", \"\"\n        for line in open(f, encoding=\"utf-8\"):",
        "        chapter, section, page = CH_MAP.get(name, \"\"), \"\", \"\"\n        chapter = CH_MAP.get(name, chapter)\n        for line in open(f, encoding=\"utf-8\"):")
    open(gp, "w", encoding="utf-8").write(g)
    print("gen_notes.py: CH_MAP inserted")
else:
    print("gen_notes.py: already patched")
