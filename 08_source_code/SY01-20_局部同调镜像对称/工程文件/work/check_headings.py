# -*- coding: utf-8 -*-
import io
import re
import pymupdf

ZH = "定理|定义|引理|命题|推论|问题|注记|例|记号|猜想|约定|练习|断言"
NUM = r"((?:\d+|[A])\.\d+)"
pdf = pymupdf.open(r"<本地路径>")
text = "\n".join(p.get_text() for p in pdf)
seq = [(m.group(2), m.group(1)) for m in re.finditer("(" + ZH + r")\s*" + NUM, text)]
# 去掉正文里的「见定理 3.4」类引用：只保留连续出现且前面是行首/段首的
print("total headings:", len(seq))
seen = {}
dups = []
for n, t in seq:
    seen.setdefault(n, []).append(t)
print("dup nums:", {k: v for k, v in seen.items() if len(v) > 1})
order = [n for n, t in seq]
# 检查是否有相邻重复（可能重复排印）
adj = [(order[i], order[i + 1]) for i in range(len(order) - 1) if order[i] == order[i + 1]]
print("adjacent dup:", adj)
io.open(r"<本地路径>", "w", encoding="utf-8").write("\n".join("%s %s" % x for x in seq))
