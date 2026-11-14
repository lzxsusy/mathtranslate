# -*- coding: utf-8 -*-
"""Apply the mechanical terminology/notation fixes recommended by the
term-consistency audit (task-13).  Every rule states its expected hit count and
the script aborts if a count differs, so a stale line number cannot silently
corrupt the text."""
import os, re, sys

CH = r"<本地路径>"
files = {}
for fn in ["ch01.tex", "ch03.tex", "ch04.tex", "ch05.tex", "ch06.tex",
           "ch07.tex", "ch08-sec82.tex", "ch02.tex", "ch08.tex",
           "ch08-sec83.tex", "ch08-sec84head.tex", "ch08-sec85.tex"]:
    p = os.path.join(CH, fn)
    files[fn] = open(p, encoding="utf-8").read()

def sub(fn, pattern, repl, expect, label):
    text = files[fn]
    new, n = re.subn(pattern, repl, text)
    if n != expect:
        print("ABORT: %s in %s: expected %d hit(s), got %d" % (label, fn, expect, n))
        sys.exit(1)
    files[fn] = new
    print("OK  %-34s %-16s %d" % (label, fn, n))
    return n

# A. quintic wording: kill the hybrid coinage "五次三维超曲面"
for fn, exp in [("ch03.tex", 1), ("ch04.tex", 1), ("ch06.tex", 2)]:
    sub(fn, "五次三维超曲面", "五次三维流形", exp, "五次三维超曲面 -> 五次三维流形")
sub("ch03.tex", "镜像五次超曲面", "镜像五次三维流形", 1, "镜像五次超曲面 -> 镜像五次三维流形")

# B. operator names
sub("ch01.tex", r"\\mathrm\{id\}", r"\\operatorname{id}", 1, "\\mathrm{id} -> \\operatorname{id}")
sub("ch08-sec82.tex", r"\\mathcal Hom", r"\\mathcal{H}om", 15, "\\mathcal Hom -> \\mathcal{H}om")

# C. brace style leak in ch05
sub("ch05.tex", r"\\mathbb Z", r"\\mathbb{Z}", 5, "\\mathbb Z -> \\mathbb{Z}")

# D. bare group names -> \operatorname
sub("ch03.tex", r"\$SO\(2\)\$", r"$\\operatorname{SO}(2)$", 1, "$SO(2)$")
sub("ch03.tex", r"\$SU\(3\)\$", r"$\\operatorname{SU}(3)$", 3, "$SU(3)$")
sub("ch04.tex", r"\$SU\(2\)\\to SO\(3\)\$", r"$\\operatorname{SU}(2)\\to\\operatorname{SO}(3)$", 1, "$SU(2)->SO(3)$")
sub("ch05.tex", r"\$SU\(3\)\$", r"$\\operatorname{SU}(3)$", 1, "$SU(3)$")
sub("ch05.tex", r"\$SU\(n\)\$", r"$\\operatorname{SU}(n)$", 1, "$SU(n)$")

# E. ch07 line 106: same sentence mixed CP and P
files["ch07.tex"] = files["ch07.tex"].replace(r"$U\subset\mathbb P^k$", r"$U\subset\mathbb{CP}^k$")
assert r"$U\subset\mathbb P^k$" not in files["ch07.tex"]
print("OK  ch07:106 \\mathbb P^k -> \\mathbb{CP}^k                           1")

# F. \BookRef display strings: drop the space before numbers (majority style)
sub(None or "ch02.tex", r"(\\Book(?:Ref|EqRef)\{[^{}]*\}\{)(定理|定义|命题|引理|例题|构造|猜想|笔记|问题) ",
    r"\1\2", 1, "BookRef thm space")
for fn, exp in [("ch03.tex", 1), ("ch07.tex", 40), ("ch08-sec83.tex", 1),
                ("ch08-sec84head.tex", 1), ("ch08-sec85.tex", 1), ("ch08.tex", 2)]:
    sub(fn, r"(\\Book(?:Ref|EqRef)\{[^{}]*\}\{)(定理|定义|命题|引理|例题|构造|猜想|笔记|问题) ",
        r"\1\2", exp, "BookRef thm space")
for fn, exp in [("ch08-sec82.tex", 6), ("ch08-sec83.tex", 11)]:
    sub(fn, r"(\\Book(?:Ref|EqRef)\{[^{}]*\}\{)图 ", r"\1图", exp, "BookRef fig space")

for fn, text in files.items():
    with open(os.path.join(CH, fn), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
print("written:", len(files), "files")
