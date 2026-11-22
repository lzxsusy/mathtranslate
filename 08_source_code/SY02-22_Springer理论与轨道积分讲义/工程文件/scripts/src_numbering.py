# -*- coding: utf-8 -*-
"""从译文的 .tex 源推算编号对象序列（不依赖 PDF 抽取）。
规则：section 计数器（\\appendix 后改为字母），subsection 重置子计数器；
equation 计数器由 \\begin{equation}/align/thm 等环境递增（与 preamble 一致）。
输出：工程文件/work/numbering_src.txt，每行「编号 \t 类型 \t 所属节」。
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(os.path.dirname(ROOT), "源码", "chunks")

THM = {
    "thm": "定理", "prop": "命题", "lem": "引理", "sublem": "子引理",
    "cor": "推论", "conj": "猜想", "dfn": "定义", "construction": "构造",
    "hypothesis": "假设", "ques": "问题", "rmk": "注", "ex": "例",
    "exs": "例", "lem-def": "引理-定义",
}

sec = 0
sub = 0
eq = 0
appendix = False
out = []
LETTERS = "ABCDEFGH"


def sec_label():
    return LETTERS[sec - 1] if appendix else str(sec)


for name in sorted(os.listdir(CH)):
    if not name.endswith(".tex"):
        continue
    for raw in open(os.path.join(CH, name), encoding="utf-8"):
        line = re.split(r"(?<!\\)%", raw)[0]
        if re.match(r"\s*\\appendix\b", line):
            appendix = True
            sec = 0
            continue
        if re.match(r"\s*\\section\*?\{", line) and not re.match(r"\s*\\subsection", line):
            if re.match(r"\s*\\section\*", line):
                continue  # 不编号
            sec += 1
            sub = 0
            eq = 0
            continue
        if re.match(r"\s*\\subsection\*?\{", line):
            if re.match(r"\s*\\subsection\*", line):
                continue
            sub += 1
            eq = 0
            continue
        m = re.search(r"\\begin\{(thm|prop|lem|sublem|cor|conj|dfn|construction|hypothesis|ques|rmk|exs|ex|lem-def)\}", line)
        if m:
            eq += 1
            out.append((sec_label(), sub, eq, THM[m.group(1)]))
            continue
        if re.search(r"\\begin\{(equation|align|multline)\}", line):
            eq += 1
            out.append((sec_label(), sub, eq, "公式"))

path = os.path.join(ROOT, "work", "numbering_src.txt")
with open(path, "w", encoding="utf-8") as fh:
    for s, sb, k, kind in out:
        fh.write("%s.%d.%d\t%s\n" % (s, sb, k, kind))
print("wrote", path, len(out), "items")
