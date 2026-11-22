#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compare math/cite/ref/label content of each translated chunk with the
corresponding slice of the original GLDraft_D.tex. Read-only.

Whitespace is ignored inside math. Translator notes may add math; only
missing/modified original segments and key differences are flagged.
"""
import re, sys, pathlib
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC = ROOT / "工程文件" / "work" / "原文" / "GLDraft_D.tex"
CH = ROOT / "源码" / "chunks"

ENVS = ["equation", "equation*", "align", "align*", "gather", "gather*",
        "multline", "multline*", "eqnarray", "eqnarray*"]


def strip_comments(s):
    return "\n".join(re.sub(r"(?<!\\)%.*$", "", ln) for ln in s.splitlines())


def norm(x):
    return re.sub(r"\s+", "", x)


def math_segments(s):
    s = strip_comments(s)
    out = []
    for env in ENVS:
        pat = re.compile(r"\\begin\{" + re.escape(env) + r"\}(.*?)\\end\{" + re.escape(env) + r"\}", re.S)
        for m in pat.finditer(s):
            out.append(("env:" + env, norm(m.group(0))))
    for m in re.finditer(r"\\\[(.*?)\\\]", s, re.S):
        out.append(("display", norm(m.group(0))))
    for m in re.finditer(r"\$\$(.+?)\$\$", s, re.S):
        out.append(("dd", norm(m.group(0))))
    tmp = re.sub(r"\\begin\{(equation|align|gather|multline|eqnarray)\*?\}.*?\\end\{\1\*?\}", "", s, flags=re.S)
    tmp = re.sub(r"\\\[.*?\\\]", "", tmp, flags=re.S)
    tmp = re.sub(r"\$\$.*?\$\$", "", tmp, flags=re.S)
    for m in re.finditer(r"(?<!\\)\$(?!\$)(.+?)(?<!\\)\$", tmp, re.S):
        out.append(("inline", norm(m.group(0))))
    return out


def keys(s, cmd):
    return Counter(re.findall(r"\\" + cmd + r"\{([^{}]*)\}", strip_comments(s)))


def parse_range(path):
    head = path.read_text(encoding="utf-8", errors="replace").splitlines()[:2]
    m = re.search(r"行\s*(\d+)[–-](\d+)", head[0])
    if not m:
        m = re.search(r"lines?\s*(\d+)[–-](\d+)", head[0])
    return (int(m.group(1)), int(m.group(2))) if m else None


def main():
    orig_lines = SRC.read_text(encoding="utf-8", errors="replace").splitlines()
    bad = 0
    for path in sorted(CH.glob("ch*.tex")):
        rng = parse_range(path)
        if not rng:
            print(f"{path.name}: no line range in header, skip")
            continue
        a, b = rng
        orig = "\n".join(orig_lines[a - 1:b])
        cur = path.read_text(encoding="utf-8", errors="replace")
        mo = Counter(x[1] for x in math_segments(orig))
        mc = Counter(x[1] for x in math_segments(cur))
        missing = mo - mc
        added = mc - mo
        ck_o, ck_c = keys(orig, "cite"), keys(cur, "cite")
        rk_o = keys(orig, "ref") + keys(orig, "eqref")
        rk_c = keys(cur, "ref") + keys(cur, "eqref")
        lb_o, lb_c = keys(orig, "label"), keys(cur, "label")
        flags = []
        if missing:
            flags.append(f"missing math segments: {sum(missing.values())}")
        if ck_o != ck_c:
            flags.append(f"cite keys differ: -{sum((ck_o - ck_c).values())} +{sum((ck_c - ck_o).values())}")
        if rk_o != rk_c:
            flags.append(f"ref keys differ: -{sum((rk_o - rk_c).values())} +{sum((rk_c - rk_o).values())}")
        if lb_o != lb_c:
            flags.append(f"label keys differ: -{sum((lb_o - lb_c).values())} +{sum((lb_c - lb_o).values())}")
        print(f"{path.name}: " + ("OK" if not flags else "; ".join(flags)))
        if missing:
            for seg, n in list(missing.items())[:5]:
                print(f"   MISSING x{n}: {seg[:140]}")
        if added:
            print(f"   note: {sum(added.values())} added math segment(s) (translator notes)")
        bad += len(flags)
    print(f"\nTOTAL issues: {bad}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
