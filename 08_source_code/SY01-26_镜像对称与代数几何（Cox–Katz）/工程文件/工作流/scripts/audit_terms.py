#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Term-consistency audit over chapters/*.tex.

usage: python audit_terms.py [--ctx] [--term 单值化]
Prints per-term occurrence counts by file and flags variant pairs that co-occur.
"""
import glob, os, re, sys, collections

os.chdir(os.path.dirname(os.path.abspath(__file__)))
# 本脚本原在 scripts/ 下 os.chdir，导致 chapters/ 相对路径落空、审计恒为空（2026-11-20 修正）。
# 从脚本目录向上找到含 chapters/*.tex 的工程根再 chdir。
_d = os.getcwd()
while _d != os.path.dirname(_d):
    for _sub in ("", "源码"):
        if glob.glob(os.path.join(_d, _sub, "chapters", "*.tex")):
            os.chdir(os.path.join(_d, _sub) if _sub else _d)
            _d = None
            break
    if _d is None:
        break
    _d = os.path.dirname(_d)
FILES = sorted(glob.glob("chapters/*.tex"))
SKIP_INDEX = {"chapters/index.tex"}

PAIRS = [
    ("单值化", "单值性"),
    ("线性束", "线性系"),
    ("通用族", "万有族"),
    ("轨形", "轨道流形"),
    ("翻越", "翻转"),
    ("束", "层"),
    ("除子", "因子"),
    ("多胞形", "多面体"),
    ("扇", "扇形"),
    ("丰沛", "充足"),
    ("幂零", "幂零元"),
    ("自反多胞形", "反身多胞形"),
    ("镜像对称", "镜对称"),
    ("三维簇", "三维流形"),
    ("量子上同调", "量子同调"),
    ("未定", "未定"),
]

def counts(term, files=FILES):
    c = collections.Counter()
    for f in files:
        t = open(f, encoding="utf-8").read()
        n = t.count(term)
        if n:
            c[f] = n
    return c

def show_ctx(term, pat):
    for f in FILES:
        for i, line in enumerate(open(f, encoding="utf-8"), 1):
            if term in line:
                m = re.search(r".{0,25}" + re.escape(term) + r".{0,25}", line)
                print(f"{f}:{i}: {m.group(0) if m else term}")

if __name__ == "__main__":
    if "--ctx" in sys.argv:
        t = sys.argv[sys.argv.index("--ctx") + 1]
        show_ctx(t, None)
        sys.exit()
    print("=== pair audit (excluding index.tex) ===")
    for a, b in PAIRS:
        ca = counts(a, [f for f in FILES if f not in SKIP_INDEX])
        cb = counts(b, [f for f in FILES if f not in SKIP_INDEX])
        na, nb = sum(ca.values()), sum(cb.values())
        flag = "  <== mixed" if na and nb else ""
        if na or nb:
            print(f"{a}:{na}  {b}:{nb}{flag}")
