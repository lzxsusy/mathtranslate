# -*- coding: utf-8 -*-
"""把 make_bib.py 生成的 “姓, 名” 改为 “名 姓”。在生成阶段处理，避免二次改写。"""
import io
import os
import re

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p = os.path.join(root, "scripts", "make_bib.py")
s = io.open(p, encoding="utf-8").read()

old_render_auth = '''    if len(auth) == 1:
        a = auth[0]
    elif len(auth) > 1:
        a = ", ".join(auth[:-1]) + ", and " + auth[-1]
    else:
        a = ""'''
new_render_auth = '''    def flip(n):
        if "," not in n:
            return n.strip()
        last, first = n.split(",", 1)
        return ("%s %s" % (first.strip(), last.strip())).strip()

    names = [flip(x) for x in auth]
    if len(names) == 1:
        a = names[0]
    elif len(names) > 1:
        a = ", ".join(names[:-1]) + " and " + names[-1]
    else:
        a = ""'''
assert old_render_auth in s
s = s.replace(old_render_auth, new_render_auth)
io.open(p, "w", encoding="utf-8", newline="\n").write(s)
print("patched make_bib.py")
