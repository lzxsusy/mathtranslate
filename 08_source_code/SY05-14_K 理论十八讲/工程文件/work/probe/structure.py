# -*- coding: utf-8 -*-
"""结构分析：编号定理/公式/章节边界/正文语料统计。"""
import re, json, collections, io, sys
import pymupdf

PDF = r"<本地路径>).pdf"
ROOT = r"<本地路径>"
doc = pymupdf.open(PDF)

out = io.StringIO()
def p(*a):
    print(*a)
    out.write(" ".join(str(x) for x in a) + "\n")

# ---------- 1. 编号公式扫描（多种位置判据） ----------
eq_pat = re.compile(r"^\((\d{1,2}\.\d{1,2})\)$")
left_pat = re.compile(r"^\(\d{1,2}\.\d{1,2}\)")
found = collections.defaultdict(list)
for i, page in enumerate(doc):
    W = page.rect.width
    d = page.get_text("dict")
    for b in d["blocks"]:
        if b.get("type") != 0:
            continue
        for ln in b["lines"]:
            txt = "".join(s["text"] for s in ln["spans"]).strip()
            if eq_pat.match(txt):
                x0 = min(s["bbox"][0] for s in ln["spans"])
                x1 = max(s["bbox"][2] for s in ln["spans"])
                found[i + 1].append((txt, round(x0), round(x1), round(W)))
p("== 形如 (x.y) 的独立行：", sum(len(v) for v in found.values()), "条，分布前 20 页 ==")
for pg in sorted(found)[:20]:
    p(pg, found[pg][:6])

# ---------- 2. 定理类编号 ----------
kinds = ["Definition", "Proposition", "Theorem", "Lemma", "Corollary", "Example", "Remark", "Note", "Exercise"]
p("== 定理类出现次数（全文正则）==")
alltext = []
for i, page in enumerate(doc):
    alltext.append((i + 1, page.get_text("text")))
cnt = collections.Counter()
first = {}
for name in kinds:
    pat = re.compile(r"\b" + name + r"\s+\d+\.\d+")
    for pg, t in alltext:
        for m in pat.finditer(t):
            cnt[name] += 1
            first.setdefault(name, (pg, m.group(0)))
for name in kinds:
    p(name, cnt[name], first.get(name))

# ---------- 3. 章节起始页定位（按标题串） ----------
heads = [
    ("1", "Topological K-Theory"), ("2", "Lecture 1 (Topological Preliminaries on Vector Bundles)"),
    ("3", "Lecture 2 (Homotopy, Bott Periodicity and Cohomological"),
    ("4", "Lecture 3 (Products and Bott Periodicity Revised)"),
    ("5", "Lecture 4 (Chern Character and Chern Classes)"),
    ("6", "Lecture 5 (Operations in K-Theory, Symmetric Products and"),
    ("7", "Lecture 6 (Applications of Adams operations"),
    ("8", "Analytic K-Theory (K-Homology)"),
    ("9", "Lecture 1 (Some preliminaries from Functional Analysis"),
    ("10", "Lecture 2 (Index of Toeplitz Operators"),
    ("11", "Lecture 3 (The slant product and the pairing"),
    ("12", "Lecture 4 (Bott Periodicity)"),
    ("13", "Lecture 5 (K-Theory of Banach and C"),
    ("14", "Lecture 6 (C"),
    ("15", "Higher Algebraic K-Theory"),
    ("16", "Lecture 1 (Algebraic Preliminaries"),
    ("17", "Lecture 2 (The Whitehead and the Steinberg Groups)"),
    ("18", "Lecture 3 (Central Extensions of Groups)"),
    ("19", "Lecture 4 (Classifying Spaces and Group"),
    ("20", "Lecture 5 (The Plus Construction"),
    ("21", "Lecture 6 (Some Theorems and Examples)"),
    ("22", "Appendix"),
    ("R", "References"),
]
p("== 标题出现页 ==")
for code, h in heads:
    pages = [pg for pg, t in alltext if h in t]
    p("chap", code, "|", h, "->", pages[:8])

# ---------- 4. 每页统计 ----------
p("== 每页字符数（正文）==")
per = []
for pg, t in alltext:
    n = len(re.sub(r"\s", "", t))
    per.append(n)
p("mean=%.0f min=%d max=%d" % (sum(per) / len(per), min(per), max(per)))
p("first 12:", per[:12])
p("last 12:", per[-12:])

# ---------- 5. 目录原文 ----------
p("== Contents page 2-3 原文 ==")
p(doc[1].get_text("text"))
p(doc[2].get_text("text"))

# ---------- 6. 字体大小分布（判断标题层级） ----------
p("== 字号分布 ==")
sizes = collections.Counter()
for page in doc:
    for b in page.get_text("dict")["blocks"]:
        if b.get("type") != 0:
            continue
        for ln in b["lines"]:
            for s in ln["spans"]:
                sizes[round(s["size"], 1)] += len(s["text"])
for k, v in sorted(sizes.items(), key=lambda x: -x[1])[:12]:
    p(k, v)

open(ROOT + r"\probe\structure.txt", "w", encoding="utf-8").write(out.getvalue())
p("== done ==")
