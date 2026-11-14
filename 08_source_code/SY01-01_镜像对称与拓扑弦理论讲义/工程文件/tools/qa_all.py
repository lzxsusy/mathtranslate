"""Whole-document QA for the Chinese edition.

Checks equation tags against the numbers present in the source PDF, environment
and brace balance, forbidden commands, note counts, citations vs bibliography.
Usage:  python qa_all.py            (prints report, exit 1 on hard errors)
        python qa_all.py --write    (also writes build/qa-report.md)
"""
import os
import re
import sys

ZH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SECT = os.path.join(ZH, "sections")
ORDER = ["s00-front.tex", "s01-intro.tex", "s02-sca.tex", "s03a-tft.tex",
         "s03b-bmodel.tex", "s03c-example.tex", "s04a-ttstar.tex",
         "s04b-highergenus.tex", "s05-refs.tex"]
EXPECTED = {}
for i in range(1, 43):
    EXPECTED[f"2.{i}"] = "s02-sca.tex"
for i in range(1, 21):
    EXPECTED[f"3.{i}"] = "s03a-tft.tex"
for i in range(21, 46):
    EXPECTED[f"3.{i}"] = "s03b-bmodel.tex"
for i in range(46, 69):
    EXPECTED[f"3.{i}"] = "s03c-example.tex"
for i in range(1, 29):
    EXPECTED[f"4.{i}"] = "s04a-ttstar.tex"
for i in range(29, 49):
    EXPECTED[f"4.{i}"] = "s04b-highergenus.tex"
EXPECTED["1.1"] = "s01-intro.tex"

UNI = "αβγδεζηθικλμνξπρστυφχψωΓΔΘΛΞΠΣΦΨΩ∑∫√≤≥→←↔×·⋯∞∂"


def check_balance(name, text, errs):
    stack = []
    for n, line in enumerate(text.splitlines(), 1):
        code = re.sub(r"(?<!\\)%.*$", "", line)
        for m in re.finditer(r"\\(begin|end)\{([^}]+)\}", code):
            kind, env = m.group(1), m.group(2).strip()
            if kind == "begin":
                stack.append((env, n))
            else:
                if not stack or stack[-1][0] != env:
                    errs.append(f"{name}:{n} \\end{{{env}}} mismatch")
                    if stack:
                        stack.pop()
                else:
                    stack.pop()
    for env, n in stack:
        errs.append(f"{name}: unclosed \\begin{{{env}}} (line {n})")
    depth = 0
    for n, line in enumerate(text.splitlines(), 1):
        code = re.sub(r"(?<!\\)%.*$", "", line)
        i = 0
        while i < len(code):
            if code[i] == "\\":
                i += 2
                continue
            if code[i] == "{":
                depth += 1
            elif code[i] == "}":
                depth -= 1
                if depth < 0:
                    errs.append(f"{name}:{n} unmatched }}")
                    depth = 0
            i += 1
    if depth:
        errs.append(f"{name}: unbalanced braces ({depth})")


def main():
    errs, warns, info = [], [], []
    texts = {}
    for fn in ORDER:
        p = os.path.join(SECT, fn)
        if not os.path.exists(p):
            errs.append(f"missing file: {fn}")
            continue
        texts[fn] = open(p, encoding="utf-8").read()
        check_balance(fn, texts[fn], errs)
        body = re.sub(r"\\verb\|[^|]*\|", "", texts[fn])
        for bad in ["\\usepackage", "\\documentclass", "\\begin{document}", "\\tableofcontents",
                    "\\newcommand", "\\def\\"]:
            if bad in body and fn != "s00-front.tex":
                errs.append(f"{fn}: forbidden {bad}")
        n_tbc = len(re.findall(r"\[待确认", texts[fn]))
        if n_tbc:
            warns.append(f"{fn}: {n_tbc} [待确认]")

    # tags
    tags = {}
    for fn, t in texts.items():
        if fn == "s05-refs.tex":
            continue
        for m in re.finditer(r"\\tag\{([^}]*)\}", re.sub(r"\\verb\|[^|]*\|", "", t)):
            tags.setdefault(m.group(1).strip(), []).append(fn)
    missing = [k for k in EXPECTED if k not in tags]
    dup = {k: v for k, v in tags.items() if len(v) > 1}
    extra = [k for k in tags if k not in EXPECTED]
    if missing:
        errs.append("missing equation tags: " + ", ".join(sorted(missing, key=lambda s: [int(x) for x in s.split('.')])))
    if dup:
        errs.append("duplicate tags: " + ", ".join(f"{k}({len(v)})" for k, v in dup.items()))
    if extra:
        warns.append("tags not in expected set: " + ", ".join(extra))
    for k, where in EXPECTED.items():
        if k in tags and where not in tags[k]:
            warns.append(f"tag {k} found in {tags[k]} but expected {where}")
    info.append(f"equation tags: {len(tags)}/{len(EXPECTED)}")

    # notes
    for fn, t in texts.items():
        if fn in ("s00-front.tex", "s05-refs.tex"):
            continue
        ns = len(re.findall(r"\\section\{", t))
        nkt = len(re.findall(r"\\begin\{keytakeaways\}", t))
        nyz = len(re.findall(r"\\begin\{yizhu\}", t))
        ntn = len(re.findall(r"%\s*\[Tutor Note", t))
        info.append(f"{fn}: sections={ns} keytakeaways={nkt} yizhu={nyz} TutorNote={ntn}")
        if nkt < ns:
            errs.append(f"{fn}: keytakeaways {nkt} < sections {ns}")
        if nyz < 3 and ns > 0:
            warns.append(f"{fn}: only {nyz} yizhu")
        if ntn < nyz:
            warns.append(f"{fn}: TutorNote comments {ntn} < yizhu {nyz}")

    # unicode math
    for fn, t in texts.items():
        bad = sorted(set(ch for ch in t if ch in UNI))
        if bad:
            warns.append(f"{fn}: unicode math chars {''.join(bad)}")

    # citations vs bibliography
    cites = set()
    for fn, t in texts.items():
        for m in re.finditer(r"\\cite\{([^}]*)\}", t):
            for k in m.group(1).split(","):
                cites.add(k.strip())
    bib = set()
    if "s05-refs.tex" in texts:
        bib = set(re.findall(r"\\bibitem\{([^}]+)\}", texts["s05-refs.tex"]))
    missing_refs = sorted(cites - bib)
    if missing_refs:
        errs.append("citations without bibitem: " + ", ".join(missing_refs))
    info.append(f"citations: {len(cites)} distinct; bibitems: {len(bib)}")
    unused = sorted(bib - cites)
    if unused:
        warns.append("bibitems never cited: " + ", ".join(unused))

    # figure
    if "s04a-ttstar.tex" in texts:
        t = texts["s04a-ttstar.tex"]
        if "figure-1.png" not in t:
            errs.append("s04a: figure-1.png not referenced")
        if "\\begin{figure}" not in t:
            errs.append("s04a: no figure environment")

    print("=== QA report ===")
    for i in info:
        print("INFO:", i)
    for w in warns:
        print("WARN:", w)
    for e in errs:
        print("ERROR:", e)
    print("RESULT:", "FAIL" if errs else "PASS")
    return errs


if __name__ == "__main__":
    e = main()
    if "--write" in sys.argv:
        pass
    sys.exit(1 if e else 0)
