# -*- coding: utf-8 -*-
import io
import re

TYPES = "thm|defn|dfn|prp|prop|crl|cor|conj|nota|ques|exmp|example|lmm|lemma|rmk|cv|exer"
orig = io.open(r"<本地路径>", encoding="utf-8").read()
ours = "".join(io.open(r"<本地路径>" % i, encoding="utf-8").read()
               for i in range(15))
po = re.findall(r"<本地路径>" + TYPES + r")\}", orig)
pm = re.findall(r"<本地路径>" + TYPES + r")\}", ours)
from collections import Counter
co, cm = Counter(po), Counter(pm)
print("orig total", len(po), "ours total", len(pm))
for t in sorted(set(co) | set(cm)):
    if co[t] != cm[t]:
        print("DIFF", t, "orig", co[t], "ours", cm[t])
