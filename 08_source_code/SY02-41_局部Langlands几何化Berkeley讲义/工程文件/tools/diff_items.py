# -*- coding: utf-8 -*-
"""对某一讲：按顺序列出源文本编号条目类型 与 译文的条目环境类型，找出第一处错位。"""
import re, sys, pathlib

PROJ = pathlib.Path(r"C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-41_局部Langlands几何化Berkeley讲义")
SRC = pathlib.Path(r"C:\Users\admin\Downloads\fs_scholze_work\pages")
RANGE = {1:(2,6),2:(7,11),3:(12,16),4:(17,21),5:(22,26),6:(27,31),7:(32,36),8:(37,41),9:(42,48),
         10:(49,54),11:(55,59),12:(60,65),13:(66,71),14:(72,78),15:(79,83),16:(84,89),17:(90,94),
         18:(95,101),19:(102,107),20:(108,112),21:(113,117),22:(118,123),23:(124,127),24:(128,132),
         25:(133,137),26:(138,142),27:(143,147)}
MAP = {"Def":"definition","Theorem":"theorem","Proposition":"proposition","Lemma":"lemma",
       "Corollary":"corollary","Remark":"remark","Example":"example","Warning":"warning",
       "Question":"question","Conjecture":"conjecture","Notation":"notation"}
ITEM = re.compile(r"^(Deﬁnition|Definition|Theorem|Proposition|Lemma|Corollary|Remark|Example|Warning|Question|Conjecture|Notation)\s+(\d+)\.(\d+)\s*[\.:]?\s*(.*)")

n = int(sys.argv[1])
lo, hi = RANGE[n]
src = []
for p in range(lo, hi+1):
    for line in (SRC/f"p{p:03d}.txt").read_text(encoding="utf-8").splitlines():
        m = ITEM.match(line.strip())
        if m and int(m.group(2)) == n:
            t = "Def" if m.group(1) in ("Deﬁnition","Definition") else m.group(1)
            src.append((p, m.group(2)+"."+m.group(3), MAP[t], line.strip()[:60]))

f = next(PROJ.glob("源码/sections/s%02d-*.tex" % n))
t = f.read_text(encoding="utf-8")
envs = [(m.start(), m.group(1)) for m in re.finditer(r"\\begin\{(definition|theorem|proposition|lemma|corollary|remark|example|warning|question|conjecture|notation)\}", t)]

print("源 %d 条 / 译 %d 条" % (len(src), len(envs)))
for i in range(max(len(src), len(envs))):
    s = src[i] if i < len(src) else None
    e = envs[i] if i < len(envs) else None
    mark = "  " if (s and e and s[2] == e[1]) else "**"
    print("%s %2d 源 %-12s %-12s" % (mark, i+1, (s[1]+" "+s[2]) if s else "--", e[1] if e else "--"),
          "|", (s[3] if s else ""))
if len(sys.argv) > 2:
    pos = int(sys.argv[2])
    print("\n译文上下文：")
    print(t[max(0,pos-300):pos+300])
