# -*- coding: utf-8 -*-
import io, os, re
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p = os.path.join(root, "work", "原文", "main.tex")
s = io.open(p, encoding="utf-8", errors="replace").read()
print("len", len(s))
print("bibdiv", s.count("\\begin{bibdiv}"), s.count("\\end{bibdiv}"))
print("bib{", s.count("\\bib{"))
i = s.rfind("\\begin{bibdiv}")
print("i", i, repr(s[i:i + 60]))
j = s.find("\\bib{", i)
print("first bib at", j, repr(s[j:j + 40]))
