# -*- coding: utf-8 -*-
"""Append a verifiable source marker to every existing explanatory note.

Rules (04_playbook/01 §2.5.6):
- note depends on the original text -> [来源：原书 p.N 上下文（A）]
- 原文疑误 -> compare with original wording
- 存疑 -> original wording + unresolved flag
- 背景补充 -> no external source claimed -> [译者按（背景补充，无外部依据）]

Dry run by default; pass --write to modify sections in place.
"""
import os, re, sys

HERE = os.path.dirname(__file__)
SEC = os.path.join(HERE, "..", "..", "..", "源码", "sections")
ANCHOR = re.compile(r"^%\s*====\s*原文 PDF 第\s*(\d+)\s*页")
NOTE = re.compile(r"^%\s*\[(Tutor Note|原文疑误|存疑|背景补充)\s*[:：]")
MARKERS = ("来源：", "依据：", "译者按")

def page_for(lines, idx):
    p = None
    for i in range(idx, -1, -1):
        m = ANCHOR.match(lines[i])
        if m:
            p = int(m.group(1)); break
    if p is None:
        for i in range(idx + 1, len(lines)):
            m = ANCHOR.match(lines[i])
            if m:
                p = int(m.group(1)); break
    return p

def marker(kind, page):
    if kind == "Tutor Note":
        return f"来源：原书 p.{page} 上下文（A）。"
    if kind == "原文疑误":
        return f"来源：原书 p.{page} 英文原文与译本对照（A）。"
    if kind == "存疑":
        return f"来源：原书 p.{page} 英文原文；存疑待核（A）。"
    return "译者按（背景补充，无外部依据）。"

def main(write=False):
    files = sorted(f for f in os.listdir(SEC) if f.endswith(".tex") and f.startswith(("s0", "s1")))
    total = changed = skipped = 0
    samples = []
    for fn in files:
        path = os.path.join(SEC, fn)
        with open(path, encoding="utf-8") as f:
            lines = f.read().splitlines()
        for i, line in enumerate(lines):
            m = NOTE.match(line)
            if not m:
                continue
            total += 1
            if any(k in line for k in MARKERS):
                skipped += 1
                continue
            page = page_for(lines, i)
            if page is None or not line.rstrip().endswith("]"):
                skipped += 1
                continue
            body = line.rstrip()[:-1].rstrip()
            sep = " " if body.endswith("。") else "；"
            new = body + sep + marker(m.group(1), page) + "]"
            lines[i] = new
            changed += 1
            if len(samples) < 8:
                samples.append((fn, i + 1, page, m.group(1), new[-120:]))
        if write:
            with open(path, "w", encoding="utf-8") as f:
                f.write("\n".join(lines) + "\n")
    print(f"total={total} changed={changed} skipped={skipped} write={write}")
    for s in samples:
        print(s)

if __name__ == "__main__":
    main("--write" in sys.argv)
