# -*- coding: utf-8 -*-
"""Merge the temporary split chapter files back into single chapters and
restore main.tex to the single-file form.  Run once, after all reviewers are
done.  The split files are archived under review/split_final/.
"""
import os, shutil

PROJ = r"<本地路径>"
CH = os.path.join(PROJ, "chapters")
ARC = r"<本地路径>"
os.makedirs(ARC, exist_ok=True)

pairs = [("ch03a.tex", "ch03b.tex", "ch03.tex"),
         ("ch05a.tex", "ch05b.tex", "ch05.tex")]

for a, b, out in pairs:
    pa, pb = os.path.join(CH, a), os.path.join(CH, b)
    ta = open(pa, encoding="utf-8").read()
    tb = open(pb, encoding="utf-8").read()
    if not ta.endswith("\n"):
        ta += "\n"
    merged = ta + tb
    with open(os.path.join(CH, out), "w", encoding="utf-8", newline="\n") as f:
        f.write(merged)
    shutil.copy2(pa, os.path.join(ARC, a))
    shutil.copy2(pb, os.path.join(ARC, b))
    print("merged %s + %s -> %s (%d lines)" % (a, b, out, merged.count("\n")))

main = os.path.join(PROJ, "main.tex")
txt = open(main, encoding="utf-8").read()
old = """\\InputIfFileExists{chapters/ch03a.tex}{}{}
\\InputIfFileExists{chapters/ch03b.tex}{}{}
\\input{chapters/ch04}
\\input{chapters/ch05a}
\\input{chapters/ch05b}"""
new = """\\InputIfFileExists{chapters/ch03.tex}{}{}
\\input{chapters/ch04}
\\input{chapters/ch05}"""
assert old in txt, "main.tex does not contain the split input block"
txt = txt.replace(old, new)
with open(main, "w", encoding="utf-8", newline="\n") as f:
    f.write(txt)
print("main.tex restored to single-file form")
print(txt)
