# -*- coding: utf-8 -*-
import io
import re
import difflib

T = "thm|defn|dfn|prp|prop|crl|cor|conj|nota|ques|exmp|example|lmm|lemma|rmk|cv|exer"
lines = io.open(r"<本地路径>", encoding="utf-8").read().splitlines()
live = [l for l in lines if not l.lstrip().startswith("%")]
orig = re.findall(r"<本地路径>" + T + r")\}", "\n".join(live))
ours = []
for i in range(15):
    ours += re.findall(r"<本地路径>" + T + r")\}",
                       io.open(r"<本地路径>" % i, encoding="utf-8").read())


def norm(t):
    return "DEF" if t in ("defn", "dfn") else t


A = [norm(t) for t in orig]
B = [norm(t) for t in ours]
print("orig", len(A), "ours", len(B))
sm = difflib.SequenceMatcher(a=A, b=B, autojunk=False)
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag != "equal":
        print(tag, "orig[%d:%d]=%s" % (i1, i2, A[i1:i2]), "ours[%d:%d]=%s" % (j1, j2, B[j1:j2]))
