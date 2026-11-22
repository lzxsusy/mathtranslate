# -*- coding: utf-8 -*-
r"""编号对账（第二条腿）：用 main.aux 的 \newlabel 编号 vs 原文 PDF 上印出的编号。
用法：python number_check_sy022.py
"""
import os, re, io, sys
import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PROJ = os.path.dirname(ROOT)
AUX = os.path.join(PROJ, "源码", "main.aux")
PDF = os.path.join(ROOT, "work", "pdf", "src.pdf")

aux = io.open(AUX, encoding="utf-8", errors="replace").read()
# \newlabel{key}{{num}{page}...}
pairs = re.findall(r"\\newlabel\{([^}]*)\}\{\{([^}]*)\}\{([^}]*)\}", aux)
mine = {}
for key, num, page in pairs:
    mine[key] = num
print("译文 \\newlabel 条数:", len(pairs))

def norm(s):
    s = s.strip()
    s = s.replace("(", "").replace(")", "")
    return s

mynums = set(norm(v) for v in mine.values())

# 原文 PDF 抽全部 N.M.K 编号
doc = pymupdf.open(PDF)
text = []
for p in doc:
    text.append(p.get_text())
alltext = "\n".join(text)
orig_tokens = re.findall(r"\b\d+\.\d+\.\d+\b", alltext)
origset = set(orig_tokens)
print("原文 PDF 中 N.M.K 编号：出现 %d 次，去重 %d 个" % (len(orig_tokens), len(origset)))

print("译文编号去重 %d 个" % len(mynums))
miss = sorted(origset - mynums, key=lambda s: [int(x) for x in s.split(".")])
extra = sorted(mynums - origset, key=lambda s: [int(x) if x.isdigit() else 0 for x in s.split(".")])
print("原文有、译文无：", miss[:40], "（共 %d）" % len(miss))
print("译文有、原文无：", extra[:40], "（共 %d）" % len(extra))

# 分节统计
def per_section(nums):
    from collections import Counter
    c = Counter()
    for n in nums:
        parts = n.split(".")
        if len(parts) == 3:
            c[(parts[0], parts[1])] += 1
    return c

co, cm = per_section(origset), per_section(mynums)
print("\n分节计数（原文 / 译文）:")
for k in sorted(set(co) | set(cm), key=lambda t: (int(t[0]), int(t[1]))):
    a, b = co.get(k, 0), cm.get(k, 0)
    flag = "" if a == b else "   <== 不一致"
    print("  §%s.%s : %d / %d%s" % (k[0], k[1], a, b, flag))
