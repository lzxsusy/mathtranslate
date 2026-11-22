# -*- coding: utf-8 -*-
r"""漏译粗查：按小节比较 \ref/\eqref/\cite 的键的多重集。

一段文字里引用的标签/文献键几乎不会重复，因此若整段漏译，该小节的键多重集就会变。
按小节（"2.1" 这种）配对比较，只报不一致的小节。
"""
import glob
import os
import re
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PROJ = os.path.dirname(ROOT)
ORIG = os.path.join(ROOT, "work", "原文", "main.tex")
CHUNKS = os.path.join(PROJ, "源码", "chunks")

KEY = re.compile(r"\\(?:ref|eqref)\{([^}]*)\}|\\(?:cite)\{([^}]*)\}")


def strip_quash(text):
    out, i = [], 0
    while True:
        j = text.find("\\quash{", i)
        if j < 0:
            out.append(text[i:])
            break
        out.append(text[i:j])
        k, depth = j + len("\\quash{"), 1
        while k < len(text) and depth:
            if text[k] == "{":
                depth += 1
            elif text[k] == "}":
                depth -= 1
            k += 1
        i = k
    return "".join(out)


def per_section(text):
    sec = sub = 0
    d = {}
    for line in text.split("\n"):
        code = line if not line.lstrip().startswith("%") else ""
        if re.search(r"\\section(?!\*)\s*\{", code):
            sec += 1
            sub = 0
            d.setdefault("%d" % sec, Counter())
        elif re.search(r"\\subsection(?!\*)\s*\{", code):
            sub += 1
            d.setdefault("%d.%d" % (sec, sub), Counter())
        key = "%d.%d" % (sec, sub) if sub else "%d" % sec
        for m in KEY.finditer(code):
            ref, cite = m.group(1), m.group(2)
            if cite:
                for c in cite.split(","):
                    d.setdefault(key, Counter())[c.strip()] += 1
            else:
                d.setdefault(key, Counter())[ref.strip()] += 1
    return d


def main():
    otext = strip_quash(open(ORIG, encoding="utf-8").read()
                        .split(r"\begin{thebibliography}")[0])
    mtext = ""
    for f in sorted(glob.glob(os.path.join(CHUNKS, "ch*.tex"))):
        mtext += open(f, encoding="utf-8").read().split(r"\begin{thebibliography}")[0] + "\n"
    o, m = per_section(otext), per_section(mtext)
    bad = 0
    for k in sorted(o, key=lambda s: [int(x) for x in s.split(".")]):
        a, b = o[k], m.get(k, Counter())
        if a != b:
            bad += 1
            only_o = sorted((a - b).elements())
            only_m = sorted((b - a).elements())
            print("节 %-5s 仅原文有: %s" % (k, only_o[:12]))
            if only_m:
                print("            仅译文有: %s" % only_m[:12])
    print("键多重集不一致的小节数：", bad)


if __name__ == "__main__":
    main()
