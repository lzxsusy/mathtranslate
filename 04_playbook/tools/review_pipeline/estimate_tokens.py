# -*- coding: utf-8 -*-
import os, re, glob
root = r"<本地路径>"
tot = {}
for d in sorted(os.listdir(os.path.join(root, "chunks"))):
    p = os.path.join(root, "chunks", d)
    if not os.path.isdir(p):
        continue
    n = 0
    est = 0
    for f in glob.glob(os.path.join(p, "*.txt")):
        s = open(f, encoding="utf-8").read()
        cjk = len(re.findall(r"[\u4e00-\u9fff]", s))
        other = len(s) - cjk
        est += cjk * 0.75 + other / 3.8
        n += 1
    tot[d] = (n, est)
    print("%-14s chunks=%2d est_tokens=%6d" % (d, n, est))
print("TOTAL est tokens = %.0f" % sum(v[1] for v in tot.values()))
