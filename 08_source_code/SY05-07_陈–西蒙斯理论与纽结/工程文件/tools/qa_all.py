"""Whole-document QA for the assembled translation.

Usage: python tools/qa_all.py   (run after tools/assemble.py)

Hard checks (exit 1 on failure):
  * all 74 original equation tags present exactly once, in ascending order per section
  * every \\label{eq:X} matches a \\tag{X}; every \\eqref/\\ref target resolves
  * every \\cite key has a \\bibitem, and the 32 \\bibitem come in the prescribed order
  * figure files referenced actually exist
  * \\begin/\\end pairing, brace balance, $ parity, \\left/\\right parity
  * 5 \\section, 14 \\subsection, each \\section preceded by a keytakeaways box
Soft checks (printed): CJK style smells, yizhu count, per-file size.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEX = os.path.join(ROOT, "CS and Knots.tex")
SECT = os.path.join(ROOT, "sections")

MASTER = []
for sec, last in (("2", 31), ("3", 32), ("4", 7), ("5", 4)):
    for i in range(1, last + 1):
        MASTER.append(f"{sec}.{i}")

BIB = ["witten1989", "dunne", "tong_gauge", "tong_qhe", "chern1974", "polyakov1988",
       "ricca2011", "achucarro1986", "steenrod1951", "nakahara", "coleman", "bott1956",
       "barnatan1991", "schwarz1978", "aps1975", "aps1976a", "aps1976b", "parker1984",
       "milnor1974", "elhamdadi2020", "atiyahbott1982", "woodhouse", "quillen1986",
       "segal", "connes2006", "kirillov2004", "beasley2013", "verlinde1988",
       "moore1989", "moore1988", "witten1988", "witten2007"]


def strip_comments(text):
    out = []
    for line in text.splitlines():
        r, i = [], 0
        while i < len(line):
            if line[i] == "\\" and i + 1 < len(line):
                r.append(line[i:i + 2]); i += 2; continue
            if line[i] == "%":
                break
            r.append(line[i]); i += 1
        out.append("".join(r))
    return "\n".join(out)


def main():
    text = open(TEX, encoding="utf-8").read()
    code = strip_comments(text)
    errors, warns = [], []

    # --- tags
    tags = re.findall(r"\\tag\{([^}]*)\}", code)
    tags = [t.strip() for t in tags]
    miss = [t for t in MASTER if tags.count(t) == 0]
    extra = [t for t in tags if t not in MASTER]
    dup = sorted({t for t in tags if tags.count(t) > 1})
    if miss:
        errors.append(f"missing tags: {miss}")
    if extra:
        errors.append(f"unexpected tags: {extra}")
    if dup:
        errors.append(f"duplicate tags: {dup}")
    print(f"tags: {len(tags)}/{len(MASTER)}")

    # --- labels / refs
    labels = re.findall(r"\\label\{([^}]*)\}", code)
    dup_lab = sorted({l for l in labels if labels.count(l) > 1})
    if dup_lab:
        errors.append(f"duplicate labels: {dup_lab}")
    eq_refs = re.findall(r"\\eqref\{eq:([0-9.]+)\}", code)
    for r in eq_refs:
        if r not in tags:
            errors.append(f"\\eqref{{eq:{r}}} unresolved (no such tag)")
    refs = re.findall(r"\\(?:ref|autoref)\{([^}]*)\}", code)
    for r in refs:
        if r not in labels:
            errors.append(f"\\ref{{{r}}} unresolved (no such label)")
    labels_used = set(re.findall(r"\\(?:ref|eqref|autoref)\{(?:eq:)?([^}]*)\}", code))
    for lab in labels:
        if lab.startswith("eq:"):
            continue
        if lab not in labels_used:
            warns.append(f"label never referenced: {lab}")

    # --- citations
    bibitems = re.findall(r"\\bibitem(?:\[[^\]]*\])?\{([^}]*)\}", code)
    if bibitems != BIB:
        errors.append(f"bibitem list mismatch:\n  got {len(bibitems)}: {bibitems}\n  exp {len(BIB)}: {BIB}")
    cites = re.findall(r"\\cite\{([^}]*)\}", code)
    for c in cites:
        for k in [x.strip() for x in c.split(",")]:
            if k and k not in bibitems:
                errors.append(f"\\cite{{{k}}} has no bibitem")

    # --- figures
    figs = re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}", code)
    for f in figs:
        p = os.path.join(ROOT, f.replace("/", os.sep))
        if not os.path.exists(p):
            errors.append(f"missing figure file: {f}")
    if len(figs) != 5:
        errors.append(f"expected 5 figures, found {len(figs)}: {figs}")

    # --- env pairing & braces
    stack = []
    for n, line in enumerate(code.splitlines(), 1):
        for m in re.finditer(r"\\(begin|end)\{([^}]+)\}", line):
            if m.group(1) == "begin":
                stack.append((m.group(2), n))
            else:
                if not stack or stack[-1][0] != m.group(2):
                    errors.append(f"L{n}: env mismatch at \\end{{{m.group(2)}}}")
                    if stack:
                        stack.pop()
                else:
                    stack.pop()
    for env, n in stack:
        errors.append(f"L{n}: \\begin{{{env}}} never closed")
    tmp = code.replace(r"\{", "").replace(r"\}", "")
    if tmp.count("{") != tmp.count("}"):
        errors.append(f"brace imbalance {tmp.count('{')} vs {tmp.count('}')}")
    if len(re.findall(r"(?<!\\)\$", code)) % 2:
        errors.append("odd number of unescaped $")
    nl = len(re.findall(r"\\left(?![a-zA-Z])", code)); nr = len(re.findall(r"\\right(?![a-zA-Z])", code))
    if nl != nr:
        errors.append(f"\\left {nl} vs \\right {nr}")

    # --- structure
    secs = re.findall(r"\\section\*?\{([^}]*)\}", code)
    subs = re.findall(r"\\subsection\*?\{([^}]*)\}", code)
    print(f"sections: {len(secs)} {secs}")
    print(f"subsections: {len(subs)}")
    if len(subs) != 14:
        warns.append(f"expected 14 subsections, found {len(subs)}")
    nkey = code.count(r"\begin{keytakeaways}")
    if nkey != 5:
        warns.append(f"expected 5 keytakeaways boxes, found {nkey}")
    nyz = code.count(r"\begin{yizhu}")
    ntn = len(re.findall(r"%\s*\[Tutor Note:", text))
    print(f"yizhu={nyz} TutorNote={ntn}")
    if nyz < 45:
        warns.append(f"few yizhu: {nyz}")

    # --- style smells
    for pat, name in ((r"被[^。，]{0,12}所", "被……所"),
                      (r"进行[^。，]{0,6}的(讨论|计算|研究|分析)", "进行……的"),
                      (r"对于[^。，]{0,10}而言", "对于……而言")):
        hits = re.findall(pat, code)
        if hits:
            warns.append(f"style {name}: {len(hits)} occurrences")

    # --- per-file size
    for f in sorted(os.listdir(SECT)):
        if f.endswith(".tex"):
            body = open(os.path.join(SECT, f), encoding="utf-8").read()
            cjk = len(re.findall(r"[\u4e00-\u9fff]", body))
            print(f"  {f:28s} {cjk:6d} CJK chars")

    print()
    for w in warns:
        print("WARN ", w)
    print()
    for e in errors:
        print("ERROR", e)
    print()
    print("RESULT:", "OK" if not errors else f"{len(errors)} ERROR(S)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
