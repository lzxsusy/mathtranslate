# -*- coding: utf-8 -*-
import io, os, collections, sys
CARD = u"C:\\Users\\admin\\Desktop\\数译发布\\gitee_shuyi\\08_source_code\\SY02-45_Scholze布尔巴基1252几何Langlands的证明\\资料卡"
print("exists:", os.path.isdir(CARD))
print([x for x in os.listdir(CARD)])
p = [x for x in os.listdir(CARD) if x.endswith(".tsv")][0]
p = os.path.join(CARD, p)
rows = [l.rstrip("\n").split("\t") for l in io.open(p, encoding="utf-8") if l.strip()]
hdr, body = rows[0], rows[1:]
print("rows:", len(body), "cols:", collections.Counter(len(r) for r in body))
print("cards:", collections.Counter(r[0] for r in body))
print("status:", collections.Counter(r[7] for r in body))
for i, name in enumerate(hdr):
    empties = [r for r in body if not r[i].strip()]
    print(i, name, "empty:", len(empties), "ids:", [r[1] for r in empties][:4])
print("02 rows:")
for r in body:
    if r[0] == "02":
        print("  ", r[1], r[2], r[3])
print("DIFF rows:")
for r in body:
    if r[7] == "DIFF":
        print("  ", r[1])
print("status names:", sorted(set(r[7] for r in body)))
