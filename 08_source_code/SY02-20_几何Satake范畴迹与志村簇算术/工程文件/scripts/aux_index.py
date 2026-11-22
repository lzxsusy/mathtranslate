# -*- coding: utf-8 -*-
r"""从 main.aux 抽出每个 \label 的印刷编号与页码，按文档次序输出。

用法：python aux_index.py > ../work/条款索引数据.tsv
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PROJ = os.path.dirname(ROOT)
AUX = os.path.join(PROJ, "源码", "main.aux")

text = open(AUX, encoding="utf-8", errors="replace").read()
# \newlabel{key}{{编号}{页}{标题}{锚点}{}}
pat = re.compile(r"\\newlabel\{([^}]*)\}\{\{([^}]*)\}\{([^}]*)\}")
rows = []
for m in pat.finditer(text):
    key, num, page = m.group(1), m.group(2), m.group(3)
    if not page.isdigit():
        continue
    rows.append((int(page), key, num))

rows.sort()
for page, key, num in rows:
    print("%s\t%s\t%s" % (num, key, page))
