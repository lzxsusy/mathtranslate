# -*- coding: utf-8 -*-
import os, re
ENG = r"<本地路径>"
ENV = re.compile(r"^(Definition|Theorem|Proposition|Lemma|Corollary|Conjecture|Hypothesis|Remark|Example|Question|Problem)\s+(\d+\.\d+)\b")
out = []
for i in range(1, 35):
    p = os.path.join(ENG, "split", "p%02d.txt" % i)
    txt = open(p, encoding="utf-8").read()
    hits = []
    for ln in txt.splitlines():
        m = ENV.match(ln.strip())
        if m:
            hits.append(m.group(1)[:4] + " " + m.group(2))
    eqs = [m.group(1) for m in re.finditer(r"^\((\d+)\)\s*$", txt, re.M)]
    out.append("p%02d | eq=%s | env=%s" % (i, ",".join(eqs) or "-", "; ".join(hits) or "-"))
open(os.path.join(ENG, "env_map.txt"), "w", encoding="utf-8", newline="\n").write("\n".join(out))
print("ok")
