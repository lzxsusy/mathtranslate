# -*- coding: utf-8 -*-
"""Compare the highest numbered equation per chapter with the original book.

In the layout text, a numbered display equation starts a line with "(N.M)".
Take the max M per chapter from the original, then compare with the max
equation number used in our labels eq:N.M.
"""
import re, os, collections

ROOT = r"C:\Users\admin\Downloads\DBMS_work"
pages = open(os.path.join(ROOT, "original", "full.txt"), encoding="utf-8").read().split("\f")

CH_PAGES = {"1": (11, 36), "2": (37, 118), "3": (119, 225), "4": (227, 302),
            "5": (303, 429), "6": (431, 518), "7": (519, 583), "8": (585, 663)}

orig = {}
for ch, (a, b) in CH_PAGES.items():
    nums = set()
    for p in range(a, b + 1):
        for line in pages[p - 1].splitlines():
            m = re.match(r"\s*\((\d+)\.(\d+)\)(?:\s|$)", line)
            if m and m.group(1) == ch:
                nums.add(int(m.group(2)))
    orig[ch] = nums

texdir = os.path.join(ROOT, "Dirichlet-Mirror-Symmetry-zh", "chapters")
ours = collections.defaultdict(set)
for f in os.listdir(texdir):
    if not f.endswith(".tex"):
        continue
    txt = open(os.path.join(texdir, f), encoding="utf-8").read()
    for m in re.finditer(r"\\label\{eq:(\d+)\.(\d+)\}", txt):
        ours[m.group(1)].add(int(m.group(2)))

print("ch | orig max | orig count | our max | our count | missing in ours | extra in ours")
for ch in sorted(CH_PAGES):
    o, u = orig[ch], ours.get(ch, set())
    miss = sorted(o - u)
    extra = sorted(u - o)
    print("%s | %d | %d | %d | %d | %s | %s" % (
        ch, max(o) if o else 0, len(o), max(u) if u else 0, len(u),
        (str(miss[:12]) + ("..." if len(miss) > 12 else "")) if miss else "-",
        str(extra[:12]) if extra else "-"))

