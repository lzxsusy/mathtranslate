# -*- coding: utf-8 -*-
"""原文分节提取（稳健版：纯字符串扫描，不用正则匹配反斜杠）。"""
import sys, os, glob
sys.stdout.reconfigure(encoding="utf-8")
B = chr(92)
ROOT = r"<本地路径>"
SRC = r"<本地路径>"
REF = os.path.join(ROOT, "work", "ref")
os.makedirs(REF, exist_ok=True)
t = open(SRC, encoding="utf-8", errors="replace").read()

def find_sections(text):
    res = []
    i = 0
    while True:
        k = text.find(B + "section", i)
        if k < 0:
            break
        j = k + len(B) + len("section")
        star = False
        if j < len(text) and text[j] == "*":
            star = True; j += 1
        if j < len(text) and text[j] == "{":
            # 取标题（处理嵌套花括号）
            d = 0; p = j
            while p < len(text):
                ch = text[p]
                if ch == B:
                    p += 2; continue
                if ch == "{": d += 1
                elif ch == "}":
                    d -= 1
                    if d == 0: break
                p += 1
            title = text[j+1:p]
            res.append({"start": k, "title_end": p+1, "title": title, "star": star})
        i = j + 1
    return res

secs = find_sections(t)
print("original \\section 数量:", len(secs))
for k, s in enumerate(secs):
    print(f"  [{k:02d}] star={s['star']!s:5s} {s['title'][:70]!r}")

# 切分
bodies = []
for k, s in enumerate(secs):
    start = s["start"]
    end = secs[k+1]["start"] if k+1 < len(secs) else len(t)
    bodies.append((s["title"], t[start:end]))

mapping = [
    ("00-introduction",        [0, 1]),
    ("01-electromagnetic",     [2]),
    ("02-multiplets",          [3]),
    ("03-renormalization",     [4]),
    ("04-pure-su2",            [5]),
    ("05-one-flavor",          [6]),
    ("06-six-dimensions",      [7]),
    ("07-higgs",               [8]),
    ("08-two-three-flavors",   [9]),
    ("09-gaiotto",             [10]),
    ("10-argyres-douglas",     [11]),
    ("11-other-groups",        [12]),
    ("12-su-n-duality",        [13]),
    ("13-conclusions",         [14]),
    ("A-instantons",           [15]),
    ("B-theory-zoo",            [16]),
]
print("\n写出 work/ref/*-en.tex:")
for name, idxs in mapping:
    parts = []
    for i in idxs:
        if i >= len(bodies):
            print("  !! index out of range", name, i); continue
        parts.append(bodies[i][1])
    body = ("\n\n" + "% " + "="*60 + "\n").join(parts)
    head = "% 原文（arXiv:1312.2684v2, dummies.tex）对应小节：\n" + \
           "\n".join("%   - " + bodies[i][0] for i in idxs if i < len(bodies)) + "\n\n"
    with open(os.path.join(REF, name + "-en.tex"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(head + body)
    print(f"  {name}-en.tex  {len(body):7d} chars  ({', '.join(bodies[i][0][:40] for i in idxs if i<len(bodies))})")

