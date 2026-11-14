# -*- coding: utf-8 -*-
"""交付报告用的统计：条目分类、习题数、译注分类、索引项、图、公式。"""
import glob, os, re, collections

CH = r"C:\Users\admin\Desktop\数译发布\shuyi\translations\SY07-08\源码\chunks"
files = sorted(glob.glob(os.path.join(CH, "c*.tex")))
kinds = collections.Counter()
ex_items = 0
ex_blocks = 0
tn = 0
idx = 0
tikz = 0
disp = 0
labels = 0
refs = 0
chars = 0
lines = 0
for f in files:
    t = open(f, encoding="utf-8").read()
    chars += len(t); lines += t.count("\n") + 1
    for m in re.finditer(r"\\begin\{(definition|proposition|theorem|lemma|corollary|example|remark|construction)\}", t):
        kinds[m.group(1)] += 1
    for m in re.finditer(r"\\begin\{exercises\}(.*?)\\end\{exercises\}", t, re.S):
        ex_blocks += 1
        # 顶层 item（行首 \item）
        ex_items += len(re.findall(r"(?m)^\\item\b", m.group(1)))
    tn += len(re.findall(r"\\begin\{tnote\}", t))
    idx += len(re.findall(r"\\idx\{", t))
    tikz += len(re.findall(r"\\begin\{tikzcd\}", t))
    disp += len(re.findall(r"\\begin\{equation", t)) + len(re.findall(r"(?m)^\\\[", t))
    labels += len(re.findall(r"\\label\{", t))
    refs += len(re.findall(r"\\ref\{", t))

zh = {"definition": "定义", "proposition": "命题", "theorem": "定理", "lemma": "引理",
      "corollary": "推论", "example": "例", "remark": "注", "construction": "构造"}
print(f"文件 {len(files)} 个，源码 {lines} 行，{chars} 字符")
print("条目:", {zh[k]: v for k, v in kinds.items()}, "合计", sum(kinds.values()))
print(f"习题块 {ex_blocks}，习题 {ex_items} 题")
print(f"译注 {tn}，索引项 {idx}，tikzcd 图 {tikz}，编号公式 {disp}")
print(f"label {labels}，ref {refs}")
