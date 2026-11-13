# -*- coding: utf-8 -*-
import io
import re

SRC = r"<本地路径>"


def balanced(s, i):
    d = 0
    j = i
    while j < len(s):
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == "{":
            d += 1
        elif c == "}":
            d -= 1
            if d == 0:
                return j
        j += 1
    return -1


out = []
for name in ("ch04", "ch05", "ch08", "ch11"):
    s = io.open(SRC + "\\" + name + ".tex", encoding="utf-8").read()
    for m in re.finditer(r"<本地路径>", s):
        k = s.find("{", m.end())
        e = balanced(s, k)
        title = s[k + 1:e]
        if "轨道" not in title:
            continue
        body_end = s.find("\\end{conceptbox}", e)
        body = s[e + 1:body_end].strip()
        out.append("==== %s [%s] len=%d ====\n%s" % (name, title, len(body), body[:400]))
io.open(r"<本地路径>", "w", encoding="utf-8").write("\n\n".join(out))
print("ok")
