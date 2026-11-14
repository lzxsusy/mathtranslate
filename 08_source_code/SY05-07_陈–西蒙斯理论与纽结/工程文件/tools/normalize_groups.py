"""Normalise physics group names to upright roman: U(1), SU(N), SO(3), Spin(3), ISO(2,1)...

Math-mode occurrences become \\mathrm{X}(...); text-mode occurrences become $\\mathrm{X}(...)$.
Comment tails are skipped. Idempotent (already-\\mathrm tokens are left alone).
"""
import re
import sys

GROUPS = ["U(1)", "SU(2)", "SU(N)", "SU(5)", "SO(3)", "SO(3,1)", "SO(2,2)",
          "ISO(2,1)", "Spin(3)"]
TOK = re.compile(r"(?<![\\A-Za-z{}])(" + "|".join(re.escape(g) for g in GROUPS) + r")")


def process(path):
    lines = open(path, encoding="utf-8").read().splitlines(keepends=True)
    in_math = False
    out = []
    changed = 0
    for line in lines:
        res = []
        i = 0
        while i < len(line):
            c = line[i]
            if c == "%":
                res.append(line[i:])
                i = len(line)
                break
            if c == "\\":
                # copy control sequence / escaped char verbatim
                m = re.match(r"\\[A-Za-z]+\*?|\\.", line[i:])
                tok = m.group(0) if m else line[i]
                res.append(tok)
                i += len(tok)
                continue
            if c == "$":
                in_math = not in_math
                res.append(c)
                i += 1
                continue
            m = TOK.match(line, i)
            if m:
                g = m.group(1)
                head, inner = g.split("(")
                rep = "\\mathrm{%s}(%s)" % (head, inner)
                if not in_math:
                    rep = "$" + rep + "$"
                res.append(rep)
                i = m.end()
                changed += 1
                continue
            res.append(c)
            i += 1
        out.append("".join(res))
    if changed:
        open(path, "w", encoding="utf-8").write("".join(out))
    if in_math:
        print("WARNING: unbalanced $ at EOF in", path)
    print(f"{path}: {changed} replacements")
    return changed


if __name__ == "__main__":
    for p in sys.argv[1:]:
        process(p)
