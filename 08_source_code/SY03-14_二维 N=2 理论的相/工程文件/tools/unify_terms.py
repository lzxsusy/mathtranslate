#!/usr/bin/env python
"""Unify terminology variants across fragments (from notes/consistency-audit.md).

Idempotent. Comments are normalised too (keeps notes coherent).
"""
import glob
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECT = os.path.join(ROOT, "sections")

RULES = [
    ("异常", "反常"),        # anomaly (GLOSSARY: 反常)
    ("目标空间", "靶空间"),  # target space (GLOSSARY: 靶空间)
    ("扭曲手征", "扭手征"),  # twisted chiral (GLOSSARY: 扭手征)
    ("拉氏量", "拉格朗日量"),  # Lagrangian
    ("相消", "抵消"),
    (r"\mathbf{C}", r"\mathbb{C}"),
    (r"\mathbf{R}", r"\mathbb{R}"),
    (r"\mathbf{Z}", r"\mathbb{Z}"),
]


def main():
    total = {}
    for path in sorted(glob.glob(os.path.join(SECT, "s*.tex"))):
        text = open(path, encoding="utf-8").read()
        new = text
        for a, b in RULES:
            new = new.replace(a, b)
        if new != text:
            total[os.path.basename(path)] = sum(new.count(b) for _, b in RULES) - \
                sum(text.count(b) for _, b in RULES)
            open(path, "w", encoding="utf-8", newline="\n").write(new)
    print("unified:", total if total else "none")


if __name__ == "__main__":
    main()
