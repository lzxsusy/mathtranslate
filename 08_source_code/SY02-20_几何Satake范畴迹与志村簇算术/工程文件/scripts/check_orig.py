# -*- coding: utf-8 -*-
"""检查原文自身的 label/ref 一致性，并统计编号对象。"""
import re, collections, io, sys

p = sys.argv[1] if len(sys.argv) > 1 else "main.tex"
src = io.open(p, encoding="utf-8").read()

labels = re.findall(r"\\label\{([^}]*)\}", src)
refs = re.findall(r"\\(?:eq|auto|c|C)?ref\{([^}]*)\}", src)
cit = re.findall(r"\\cite(?:\[[^\]]*\])?\{([^}]*)\}", src)
bibkeys = re.findall(r"\\bibitem(?:\[[^\]]*\])?\{([^}]*)\}", src)

lab = collections.Counter(labels)
dup = [k for k, v in lab.items() if v > 1]
missing = sorted(set(refs) - set(labels))
unused = sorted(set(labels) - set(refs))
cites = set()
for c in cit:
    for k in c.split(","):
        cites.add(k.strip())
bibm = sorted(cites - set(bibkeys))
bibunused = sorted(set(bibkeys) - cites)

print("labels", len(labels), "uniq", len(lab), "refs", len(refs), "uniqrefs", len(set(refs)))
print("dup labels:", dup)
print("missing labels:", missing)
print("unused labels:", unused)
print("bibitems", len(bibkeys), "cites", len(cites))
print("missing bib:", bibm)
print("unused bib:", bibunused)

envs = collections.Counter(re.findall(r"\\begin\{([a-zA-Z*]+)\}", src))
thmenvs = ["thm","prop","lem","sublem","lem-def","cor","theorem","proposition","lemma","sublemma",
           "conjecture","corollary","example","ex","exs","remark","rmk","hypothesis","definition",
           "dfn","question","notation","construction","caution","convention"]
tot = 0
for e in thmenvs:
    if envs.get(e):
        print("env", e, envs[e]); tot += envs[e]
print("theorem-like total", tot)
eq = sum(envs.get(e, 0) for e in ["equation","equation*","align","align*","eqnarray","gather","multline","alignat"])
print("display eq envs", eq)
