# -*- coding: utf-8 -*-
import io
import difflib
import pymupdf

a = pymupdf.open(r"<本地路径>")
b = pymupdf.open(r"<本地路径>")
ta = [" ".join(p.get_text().split())[:60] for p in a]
tb = [" ".join(p.get_text().split())[:60] for p in b]
out = []
sm = difflib.SequenceMatcher(a=ta, b=tb, autojunk=False)
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag != "equal":
        out.append("%s A[%d:%d] B[%d:%d]" % (tag, i1, i2, j1, j2))
        out += ["  A: " + x for x in ta[i1:i2]]
        out += ["  B: " + x for x in tb[j1:j2]]
io.open(r"<本地路径>", "w", encoding="utf-8").write("\n".join(out))
print("done", len(out))
