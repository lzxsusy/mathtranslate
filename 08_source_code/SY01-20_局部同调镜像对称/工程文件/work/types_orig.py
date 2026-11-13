# -*- coding: utf-8 -*-
import io
import re
from collections import Counter

T = "thm|defn|dfn|prp|prop|crl|cor|conj|nota|ques|exmp|example|lmm|lemma|rmk|cv|exer"
lines = io.open(r"<本地路径>", encoding="utf-8").read().splitlines()
live = [l for l in lines if not l.lstrip().startswith("%")]
text = "\n".join(live)
c = Counter(re.findall(r"<本地路径>" + T + r")\}", text))
print(dict(sorted(c.items())), "total", sum(c.values()))
