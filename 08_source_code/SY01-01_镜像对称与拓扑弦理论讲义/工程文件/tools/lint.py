"""Light-weight linter for one translated .tex fragment.

Usage:
  python lint.py sections/s03a-tft.tex --tags 3.1,3.2,...,3.20
  python lint.py sections/s03a-tft.tex --tags-file tags.txt

Checks:
  * \begin/\end pairing per environment
  * brace balance
  * forbidden preamble commands
  * every expected \tag present exactly once, no unexpected duplicate tags
  * counts of keytakeaways / yizhu / [Tutor Note] / [待确认]
Prints a report and exits 1 if hard errors are found.
"""
import argparse
import os
import re
import sys


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--tags", default="")
    ap.add_argument("--tags-file", default="")
    a = ap.parse_args()
    text = open(a.file, encoding="utf-8").read()
    lines = text.splitlines()
    errors, warns = [], []

    # environment pairing
    stack = []
    env_re = re.compile(r"\\(begin|end)\{([^}]+)\}")
    for n, line in enumerate(lines, 1):
        code = re.sub(r"(?<!\\)%.*$", "", line)
        for m in env_re.finditer(code):
            kind, env = m.group(1), m.group(2).strip()
            if kind == "begin":
                stack.append((env, n))
            else:
                if not stack:
                    errors.append(f"line {n}: \\end{{{env}}} without \\begin")
                elif stack[-1][0] != env:
                    errors.append(f"line {n}: \\end{{{env}}} but open is {stack[-1][0]} (line {stack[-1][1]})")
                    stack.pop()
                else:
                    stack.pop()
    for env, n in stack:
        errors.append(f"unclosed \\begin{{{env}}} at line {n}")

    # brace balance (ignore escaped braces and comments)
    depth = 0
    for n, line in enumerate(lines, 1):
        code = re.sub(r"(?<!\\)%.*$", "", line)
        i = 0
        while i < len(code):
            ch = code[i]
            if ch == "\\":
                i += 2
                continue
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth < 0:
                    errors.append(f"line {n}: unmatched closing brace")
                    depth = 0
            i += 1
    if depth != 0:
        errors.append(f"unbalanced braces, final depth {depth}")

    for bad in ["\\usepackage", "\\documentclass", "\\begin{document}", "\\tableofcontents",
                "\\newcommand", "\\def\\", "\\input{"]:
        if bad in text:
            errors.append(f"forbidden command present: {bad}")

    # tags
    tags = [t.strip() for t in a.tags.split(",") if t.strip()]
    if a.tags_file:
        tags = [t.strip() for t in re.split(r"[,\s]+", open(a.tags_file).read()) if t.strip()]
    found = re.findall(r"\\tag\{([^}]*)\}", text)
    found_clean = [f.strip() for f in found]
    if tags:
        missing = [t for t in tags if t not in found_clean]
        if missing:
            errors.append("missing \\tag: " + ", ".join(missing))
    dup = sorted({t for t in found_clean if found_clean.count(t) > 1})
    if dup:
        errors.append("duplicated \\tag: " + ", ".join(dup))
    extra = [t for t in found_clean if tags and t not in tags]
    if extra:
        warns.append("tags outside expected list: " + ", ".join(sorted(set(extra))))

    # counts
    n_section = len(re.findall(r"\\section\{", text))
    n_kt = len(re.findall(r"\\begin\{keytakeaways\}", text))
    n_yz = len(re.findall(r"\\begin\{yizhu\}", text))
    n_tn = len(re.findall(r"%\s*\[Tutor Note", text))
    n_tbc = len(re.findall(r"\[待确认", text))
    n_yiwu = len(re.findall(r"\[原文疑误", text))
    if n_kt < n_section:
        errors.append(f"keytakeaways ({n_kt}) < sections ({n_section})")
    if n_yz and n_tn < n_yz:
        warns.append(f"[Tutor Note] comments ({n_tn}) < yizhu boxes ({n_yz})")
    if n_yz == 0:
        warns.append("no yizhu notes found")
    if n_tbc:
        warns.append(f"{n_tbc} [待确认] markers remain")
    # unicode math check
    uni = set(re.findall(r"[αβγδεζηθικλμνξπρστυφχψωΓΔΘΛΞΠΣΦΨΩ∑∫√≤≥→←↔×·⋯]", text))
    if uni:
        warns.append("unicode math symbols present: " + "".join(sorted(uni)))

    print(f"file: {a.file}")
    print(f"lines: {len(lines)}  chars: {len(text)}")
    print(f"sections: {n_section}  keytakeaways: {n_kt}  yizhu: {n_yz}  TutorNote: {n_tn}")
    print(f"tags: {len(found_clean)} (expected {len(tags)})")
    for e in errors:
        print("ERROR:", e)
    for w in warns:
        print("WARN :", w)
    if not errors:
        print("OK: no hard errors")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
