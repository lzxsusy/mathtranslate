"""Convert ASCII bracket citations in translated fragments to \\cite{ref...}.

Scans s01..s04 fragments (not s00/s05), finds [n], [n, m], [n--m] patterns and
rewrites them as \\cite{refn,...}. Writes .bib-cites.txt report.
"""
import os
import re
import sys

ZH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SECT = os.path.join(ZH, "sections")
FILES = ["s01-intro.tex", "s02-sca.tex", "s03a-tft.tex", "s03b-bmodel.tex",
         "s03c-example.tex", "s04a-ttstar.tex", "s04b-highergenus.tex"]

# [12], [3, 4], [1--3], [7,8,9,10], [64--138]
CIT = re.compile(r"\[(\d{1,2}(?:\s*(?:,|--)\s*\d{1,2})*)\]")


def expand(group):
    out = []
    for part in re.split(r"\s*,\s*", group.strip()):
        if "--" in part:
            a, b = [int(x) for x in part.split("--")]
            out.extend(f"ref{n}" for n in range(a, b + 1))
        else:
            out.append(f"ref{int(part)}")
    return out


def main():
    total = 0
    report = []
    for fn in FILES:
        path = os.path.join(SECT, fn)
        if not os.path.exists(path):
            print("skip missing", fn)
            continue
        text = open(path, encoding="utf-8").read()
        n = [0]

        def repl(m):
            refs = expand(m.group(1))
            n[0] += 1
            return "\\cite{" + ",".join(refs) + "}"

        new = CIT.sub(repl, text)
        if new != text:
            open(path, "w", encoding="utf-8", newline="\n").write(new)
        total += n[0]
        report.append(f"{fn}: {n[0]} citations")
        print(report[-1])
    print("total", total)


if __name__ == "__main__":
    main()
