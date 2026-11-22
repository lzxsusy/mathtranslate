# -*- coding: utf-8 -*-
r"""编号对账（第二条腿）：源码推演编号。
按 pcmi.cls 机制（\numberwithin{equation}{subsection}，\subsubsection 也消耗 equation 计数器）
分别在「原文正文」与「译文 chunks」上推演，逐条比对 (类型, 编号) 序列。
用法：python sim_numbering_sy022.py
"""
import os, re, io

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PROJ = os.path.dirname(ROOT)
SRC = os.path.join(ROOT, "work", "src", "ZhiweiYunPCMI.tex")
CH = os.path.join(PROJ, "源码", "chunks")

THEOREM_ENVS = ["theorem", "lemma", "prop", "cor", "conj", "fact", "ansatz",
                "dfn", "cons", "remark", "exam", "ques"]

pat_sec = re.compile(r"^\s*\\section\{")
pat_sub = re.compile(r"^\s*\\subsection\{")
pat_substar = re.compile(r"^\s*\\subsection\*\{")
pat_sss = re.compile(r"\\subsubsection\{")
pat_sss_star = re.compile(r"\\subsubsection\*\{")
pat_env = re.compile(r"\\begin\{(" + "|".join(THEOREM_ENVS) + r")\}")
pat_eq = re.compile(r"\\begin\{equation\}")


def simulate(lines, sec0=-1):
    sec, sub, eq = sec0, 0, 0
    out = []
    for line in lines:
        if pat_substar.match(line):
            continue
        if pat_sec.match(line):
            sec += 1
            sub, eq = 0, 0
            out.append(("section", str(sec)))
            continue
        if pat_sub.match(line):
            sub += 1
            eq = 0
            out.append(("subsection", "%d.%d" % (sec, sub)))
            continue
        # 一行里可能先后出现 \subsubsection 与 \begin{...}，按出现顺序处理
        events = []
        for m in pat_sss_star.finditer(line):
            events.append((m.start(), "sss*", None))
        for m in pat_sss.finditer(line):
            events.append((m.start(), "sss", None))
        for m in pat_eq.finditer(line):
            events.append((m.start(), "equation", None))
        for m in pat_env.finditer(line):
            events.append((m.start(), m.group(1), None))
        events.sort()
        for _, kind, _ in events:
            if kind == "sss*":
                continue
            eq += 1
            out.append((kind, "%d.%d.%d" % (sec, sub, eq)))
    return out


text = io.open(SRC, encoding="utf-8").read()
i0 = text.find("\\begin{document}")
i1 = text.find("\\begin{bibdiv}")
orig_lines = text[i0:i1].split("\n")

mine_lines = []
for f in sorted(os.listdir(CH)):
    if f.endswith(".tex") and f != "ch18.tex":
        mine_lines += io.open(os.path.join(CH, f), encoding="utf-8").read().split("\n")

o = simulate(orig_lines)
m = simulate(mine_lines)
print("原文编号对象：%d   译文编号对象：%d" % (len(o), len(m)))

ok = True
for i in range(max(len(o), len(m))):
    a = o[i] if i < len(o) else None
    b = m[i] if i < len(m) else None
    if a != b:
        ok = False
        print("首个不一致 @%d：原文 %s  译文 %s" % (i, a, b))
        print("  上文：", o[max(0, i - 3):i], m[max(0, i - 3):i])
        break
if ok:
    print("全部 %d 条一一对应，编号完全一致。" % len(o))

from collections import Counter
co, cm = Counter(k for k, _ in o), Counter(k for k, _ in m)
print("\n分类计数（原文 / 译文）：")
for k in sorted(set(co) | set(cm)):
    print("  %-11s %d / %d" % (k, co.get(k, 0), cm.get(k, 0)))
