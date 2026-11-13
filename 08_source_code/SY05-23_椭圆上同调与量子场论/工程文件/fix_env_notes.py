import io, os, sys, re
sys.stdout.reconfigure(encoding="utf-8")
base = r"<本地路径>"

fixes = {
    "sec1.tex": [
        (r"\begin{definition}[1.5（[ST11, Definition 5.2] 之略述）]",
         r"\begin{definition}[{1.5（[ST11, Definition 5.2] 之略述）}]"),
    ],
    "sec2.tex": [
        (r"\begin{proposition}[2.7（[HST10, §6] [ST04, §3.1]）]",
         r"\begin{proposition}[{2.7（[HST10, §6] [ST04, §3.1]）}]"),
        (r"\begin{hypothesis}[2.14（比较 [ST04, Definition 3.2.10] 与 [HST10, Corollary 6.28]）]",
         r"\begin{hypothesis}[{2.14（比较 [ST04, Definition 3.2.10] 与 [HST10, Corollary 6.28]）}]"),
    ],
    "sec3.tex": [
        (r"\begin{theorem}[3.10（[HST10]，[Che08]）]",
         r"\begin{theorem}[{3.10（[HST10]，[Che08]）}]"),
        (r"\begin{hypothesis}[3.20（比较 [ST04, Proposition 3.2.6] 与 [HST10, Corollary 6.38]）]",
         r"\begin{hypothesis}[{3.20（比较 [ST04, Proposition 3.2.6] 与 [HST10, Corollary 6.38]）}]"),
    ],
}

for fn, pairs in fixes.items():
    path = os.path.join(base, fn)
    s = open(path, encoding="utf-8").read()
    for old, new in pairs:
        n = s.count(old)
        if n != 1:
            print("WARN", fn, "count", n, "for", old[:40])
            continue
        s = s.replace(old, new)
    open(path, "w", encoding="utf-8", newline="\n").write(s)
    print("patched", fn)

# 复核：任何环境可选参数里仍含未加花括号的 '[' 都列出来
pat = re.compile(r"<本地路径>|proposition|corollary|definition|remark|example|conjecture|hypothesis|lemma|proof)\}\[([^\n]*)\]")
for fn in ["sec1.tex", "sec2.tex", "sec3.tex", "sec4a.tex", "sec4b.tex", "refs.tex"]:
    path = os.path.join(base, fn)
    for i, line in enumerate(open(path, encoding="utf-8"), 1):
        m = pat.search(line)
        if m and "[" in m.group(2) and not m.group(2).startswith("{"):
            print("STILL", fn, i, line.strip()[:80])
print("done")
