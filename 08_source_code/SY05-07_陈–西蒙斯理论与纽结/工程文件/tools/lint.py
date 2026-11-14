"""Light-weight linter for one translated .tex fragment of the CS/Knots project.

Usage:
  python tools/lint.py sections/s02a-abelian.tex --tags 2.1,2.2,...,2.19

Checks:
  * \begin/\end pairing (per environment)
  * brace balance (ignoring \{ \})
  * $ parity (unescaped)
  * \left / \right pairing
  * every expected \tag present exactly once, no unexpected tags
  * \label{eq:X} matches \tag{X}; duplicate labels; \eqref targets exist
    (in this fragment or in the global expected-tag list)
  * forbidden preamble commands
  * counts: keytakeaways, yizhu, [Tutor Note], [待确认]
  * basic CJK style smells: "被……所", "进行……的", "对于……而言"
Exit code 1 on hard errors.
"""
import argparse
import re
import sys

FORBIDDEN = [
    r"\\documentclass", r"\\usepackage", r"\\begin\{document\}", r"\\end\{document\}",
    r"\\newcommand", r"\\renewcommand", r"\\input", r"\\include\{",
    r"\\bibliography\{", r"\\pagestyle", r"\\setcounter", r"\\setlength",
    r"\\title\{", r"\\author\{", r"\\date\{", r"\\tableofcontents", r"\\part\{",
    r"\\bibliographystyle", r"\\maketitle",
]

TAGS_ALL = []
for sec, last in (("1", 0), ("2", 31), ("3", 32), ("4", 7), ("5", 4)):
    for i in range(1, last + 1):
        TAGS_ALL.append(f"{sec}.{i}")


def strip_comments(line):
    out, i = [], 0
    while i < len(line):
        c = line[i]
        if c == "\\" and i + 1 < len(line):
            out.append(line[i:i + 2]); i += 2; continue
        if c == "%":
            break
        out.append(c); i += 1
    return "".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--tags", default="", help="comma separated expected original numbers, e.g. 2.1,2.2")
    ap.add_argument("--tags-file", default="")
    a = ap.parse_args()
    text = open(a.file, encoding="utf-8").read()
    raw = text.splitlines()
    code_lines = [strip_comments(l) for l in raw]
    code = "\n".join(code_lines)

    errors, warns = [], []

    # environment pairing
    stack = []
    for n, line in enumerate(code_lines, 1):
        for m in re.finditer(r"\\(begin|end)\{([^}]+)\}", line):
            kind, env = m.group(1), m.group(2).strip()
            if kind == "begin":
                stack.append((env, n))
            else:
                if not stack:
                    errors.append(f"L{n}: \\end{{{env}}} without matching begin")
                elif stack[-1][0] != env:
                    errors.append(f"L{n}: \\end{{{env}}} but open env is {stack[-1][0]} (L{stack[-1][1]})")
                    stack.pop()
                else:
                    stack.pop()
    for env, n in stack:
        errors.append(f"L{n}: \\begin{{{env}}} never closed")

    # brace balance on code (strip escaped braces)
    tmp = code.replace(r"\{", "").replace(r"\}", "")
    if tmp.count("{") != tmp.count("}"):
        errors.append(f"brace imbalance: {{ = {tmp.count('{')}, }} = {tmp.count('}')}")

    # $ parity
    dollars = 0
    for n, line in enumerate(code_lines, 1):
        cnt = len(re.findall(r"(?<!\\)\$", line))
        dollars += cnt
        if cnt % 2 and "$$" not in line:
            # odd $ on a line is legal if math spans lines; only warn
            warns.append(f"L{n}: odd number of $ on this line (check math spanning)")
    if dollars % 2:
        errors.append(f"total unescaped $ count odd: {dollars}")

    nl = len(re.findall(r"\\left(?![a-zA-Z])", code)); nr = len(re.findall(r"\\right(?![a-zA-Z])", code))
    if nl != nr:
        errors.append(f"\\left ({nl}) != \\right ({nr})")

    # forbidden commands
    for pat in FORBIDDEN:
        for m in re.finditer(pat, code):
            errors.append(f"forbidden command {m.group(0)!r} at line {code[:m.start()].count(chr(10))+1}")

    # tags
    exp = [t.strip() for t in a.tags.split(",") if t.strip()]
    if a.tags_file:
        exp = [t.strip() for t in open(a.tags_file, encoding="utf-8").read().replace("\n", ",").split(",") if t.strip()]
    got = re.findall(r"\\tag\{([^}]*)\}", code)
    got = [g.strip() for g in got]
    for t in exp:
        c = got.count(t)
        if c != 1:
            errors.append(f"expected \\tag{{{t}}} exactly once, found {c}")
    for t in got:
        if t not in exp:
            errors.append(f"unexpected \\tag{{{t}}}")

    # labels
    labels = re.findall(r"\\label\{([^}]*)\}", code)
    dup = {l for l in labels if labels.count(l) > 1}
    for d in sorted(dup):
        errors.append(f"duplicate label {d}")
    for lab in labels:
        m = re.fullmatch(r"eq:([0-9]+\.[0-9]+)", lab)
        if m and m.group(1) not in got:
            errors.append(f"\\label{{{lab}}} has no matching \\tag{{{m.group(1)}}}")

    # eqref targets
    refs = re.findall(r"\\eqref\{eq:([0-9.]+)\}", code)
    for r in refs:
        if r not in got and r not in exp and r not in TAGS_ALL:
            errors.append(f"\\eqref{{eq:{r}}} target not found")
        elif r not in got and r not in TAGS_ALL:
            warns.append(f"\\eqref{{eq:{r}}} refers to another fragment (ok if that fragment has it)")

    # stats
    keys = code.count(r"\begin{keytakeaways}")
    yz = code.count(r"\begin{yizhu}")
    tn = len(re.findall(r"%\s*\[Tutor Note:", text))
    todo = len(re.findall(r"\[待确认", code))
    chars = len(re.findall(r"[\u4e00-\u9fff]", code))
    print(f"file: {a.file}")
    print(f"lines={len(raw)}  cjk_chars={chars}  tags={len(got)}/{len(exp)}  keytakeaways={keys}  yizhu={yz}  TutorNote={tn}  todo={todo}")
    if exp and got != exp:
        print(f"tag order: got={got}")
        print(f"           exp={exp}")
    # CJK style smells
    for pat, name in ((r"被[^。，]{0,12}所", "被……所"), (r"进行[^。，]{0,6}的(讨论|计算|研究|分析)", "进行……的"),
                      (r"对于[^。，]{0,10}而言", "对于……而言")):
        for m in re.finditer(pat, code):
            warns.append(f"style {name}: …{code[max(0,m.start()-15):m.end()+10]}…")

    print()
    for w in warns[:40]:
        print("WARN ", w)
    if len(warns) > 40:
        print(f"  ... {len(warns)-40} more warnings")
    print()
    for e in errors:
        print("ERROR", e)
    print()
    print("RESULT:", "OK" if not errors else f"{len(errors)} ERROR(S)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
