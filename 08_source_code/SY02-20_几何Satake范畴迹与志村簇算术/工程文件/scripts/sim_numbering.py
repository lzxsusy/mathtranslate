# -*- coding: utf-8 -*-
r"""模拟 LaTeX 计数器，算出每个带编号对象的印刷编号。

用法：
  python sim_numbering.py orig        只解析原文 main.tex
  python sim_numbering.py mine        只解析 源码/chunks/*.tex
  python sim_numbering.py diff        两边逐项比对

原文与译文的差别在这里抹平：原文用 \section/\subsection/\sss(\subsubsection)/定理环境
（amsart，定理类挂 [subsubsection]），译文用 \section/\subsection/\ssszh/同款定理环境。
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)          # 工程文件
PROJ = os.path.dirname(ROOT)

ORIG = os.path.join(ROOT, "work", "原文", "main.tex")
CHUNKS = os.path.join(PROJ, "源码", "chunks")

# 原文/译文的定理类环境名 → 统一类别
KIND = {
    "theorem": "thm", "thm": "thm",
    "lemma": "lem", "lem": "lem",
    "proposition": "prop", "prop": "prop",
    "corollary": "cor", "cor": "cor",
    "conjecture": "conj", "conj": "conj",
    "definition": "dfn", "dfn": "dfn", "defn": "dfn",
    "remark": "rmk", "rmk": "rmk",
    "example": "ex", "exam": "ex", "ex": "ex", "exs": "ex",
    "question": "ques", "ques": "ques",
    "fact": "fact", "ansatz": "ansatz",
    "construction": "cons", "cons": "cons",
}
THM_ENVS = "|".join(sorted(KIND, key=len, reverse=True))
EQ_ENVS = ("equation", "align", "multline", "gather", "eqnarray")


def strip_quash(text):
    """删除 \\quash{...} 的内容（作者用它在 PDF 中隐藏整段，故不参与编号）。"""
    out = []
    i = 0
    while True:
        j = text.find("\\quash{", i)
        if j < 0:
            out.append(text[i:])
            break
        out.append(text[i:j])
        k = j + len("\\quash{")
        depth = 1
        while k < len(text) and depth:
            if text[k] == "{":
                depth += 1
            elif text[k] == "}":
                depth -= 1
            k += 1
        i = k
    return "".join(out)


def simulate(text, need_doc=True):
    """返回 [(编号, 类别)]，按正文出现次序。"""
    sec = sub = sss = 0
    eqs = 0
    out = []
    lines = text.split("\n")
    in_doc = not need_doc
    for raw in lines:
        line = raw.split("%")[0] if not raw.lstrip().startswith("%") else ""
        if "\\begin{document}" in line:
            in_doc = True
            continue
        if not in_doc:
            continue
        if "\\appendix" in line:
            sec = 0
            sub = sss = eqs = 0
        # 计数器步进
        for m in re.finditer(r"\\section(?!\*)\s*\{", line):
            sec += 1
            sub = sss = eqs = 0
        for m in re.finditer(r"\\subsection(?!\*)\s*\{", line):
            sub += 1
            sss = 0
            eqs = 0
        n_sss = len(re.findall(r"\\subsubsection(?!\*)\s*\{", line))
        n_sss += len(re.findall(r"\\sss\s*\{", line))
        n_sss += len(re.findall(r"\\ssszh\s*\{", line))
        sss += n_sss
        # 定理类
        for m in re.finditer(r"\\begin\{(%s)\}" % THM_ENVS, line):
            sss += 1
            out.append(("%d.%d.%d" % (sec, sub, sss), KIND[m.group(1)]))
        # 编号公式
        for m in re.finditer(r"\\begin\{(%s)\}(?!\*)" % "|".join(EQ_ENVS), line):
            if m.group(0).endswith("*"):
                continue
            eqs += 1
            out.append(("%d.%d.%d" % (sec, sub, eqs), "eq"))
    return out


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "diff"
    orig = simulate(strip_quash(open(ORIG, encoding="utf-8").read()))
    joined = "\n".join(open(p, encoding="utf-8").read()
                         for p in sorted(glob.glob(os.path.join(CHUNKS, "ch*.tex"))))
    mine = simulate(strip_quash(joined), need_doc=False)

    if mode == "orig":
        for n, k in orig:
            print(n, k)
        print("total", len(orig))
        return
    if mode == "mine":
        for n, k in mine:
            print(n, k)
        print("total", len(mine))
        return

    print("orig", len(orig), "mine", len(mine))
    bad = 0
    for i in range(max(len(orig), len(mine))):
        a = orig[i] if i < len(orig) else ("-", "-")
        b = mine[i] if i < len(mine) else ("-", "-")
        if a != b:
            bad += 1
            if bad <= 40:
                print("  #%d  orig=%s %s   mine=%s %s" % (i + 1, a[0], a[1], b[0], b[1]))
    print("mismatch", bad)


if __name__ == "__main__":
    main()
