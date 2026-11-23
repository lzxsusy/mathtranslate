# -*- coding: utf-8 -*-
"""校验 sy0530 卡片：字段完整性 + anchor 是否落在译稿行号范围内。

退出码 0 = 全过；1 = 有问题（打印清单）。
"""
import json, os, io, glob, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(os.path.dirname(ROOT))
SRC = os.path.join(REPO, "08_source_code",
                   "SY05-30_模空间的几何与量子化（Álvarez-Cónsul、Andersen、Mundet 编）",
                   "源码")

REQUIRED = ["id", "type", "track", "title", "aliases", "summary", "question",
            "definition", "key_points", "formulas", "theorems", "pitfalls",
            "related", "sources", "rights", "status", "verification"]

problems = []

def line_count(path):
    with io.open(path, encoding="utf-8") as f:
        return sum(1 for _ in f)

cards = []
for p in sorted(glob.glob(os.path.join(ROOT, "cards", "**", "*.json"), recursive=True)):
    with io.open(p, encoding="utf-8") as f:
        try:
            cards.append((p, json.load(f)))
        except Exception as e:
            problems.append("%s: JSON 解析失败 %s" % (p, e))

ids = {c["id"] for _, c in cards}

for path, c in cards:
    rel = os.path.relpath(path, ROOT)
    for k in REQUIRED:
        if k not in c:
            problems.append("%s: 缺字段 %s" % (rel, k))
    if c.get("type") == "concept" and not c.get("theorems"):
        problems.append("%s: 概念卡无 theorems（允许，但请确认是有意为之）" % rel)
    if c.get("type") == "concept" and not c.get("pitfalls"):
        problems.append("%s: 缺 pitfalls" % rel)
    d = c.get("definition") or {}
    if not d.get("text"):
        problems.append("%s: definition.text 为空" % rel)
    for r in c.get("related", []):
        if r not in ids:
            problems.append("%s: related 指向不存在的卡 %s" % (rel, r))
    if len(c.get("summary", "")) > 200:
        problems.append("%s: summary 超过 200 字（当前 %d）" % (rel, len(c["summary"])))
    for s in c.get("sources", []):
        a = s.get("anchor") or ""
        m = re.match(r"^.*[(（][^()（）]*[)）]/源码/(.+?)(?::(\d+)(?:-(\d+))?)?$", a)
        if not m:
            problems.append("%s: anchor 格式不认识：%s" % (rel, a))
            continue
        fname, l1, l2 = m.group(1), m.group(2), m.group(3)
        fpath = os.path.join(SRC, fname)
        if not os.path.exists(fpath):
            problems.append("%s: anchor 文件不存在：%s" % (rel, fpath))
            continue
        n = line_count(fpath)
        if l1:
            a1 = int(l1); a2 = int(l2) if l2 else a1
            if a1 < 1 or a2 > n or a1 > a2:
                problems.append("%s: anchor 行号越界 %s:%d-%d（文件 %d 行）" % (rel, fname, a1, a2, n))
    for t in c.get("theorems", []):
        pr = t.get("proof") or {}
        st = pr.get("status")
        if st not in ("full", "sketched", "cited", "absent"):
            problems.append("%s: 定理「%s」proof.status=%r 不在枚举内" % (rel, t.get("name"), st))
        if st in ("full", "sketched") and not pr.get("steps"):
            problems.append("%s: 定理「%s」status=%s 但无 steps" % (rel, t.get("name"), st))
        for s in pr.get("steps", []):
            if not s.get("why"):
                problems.append("%s: 定理「%s」第 %s 步缺 why" % (rel, t.get("name"), s.get("no")))

print("cards:", len(cards), " problems:", len(problems))
for p in problems:
    print(" -", p)
sys.exit(1 if problems else 0)
