# -*- coding: utf-8 -*-
"""在 RELEASE_REGISTER.csv 中插入/更新 SY02-20 一行（16 列，utf-8）。"""
import csv, io, os, sys

R = r"C:\Users\admin\Desktop\数译发布\gitee_shuyi"
path = os.path.join(R, "RELEASE_REGISTER.csv")

note = sys.argv[1] if len(sys.argv) > 1 else (
    "底本 50 页；中译注本 %s 页；0 error/0 Overfull/0 Missing character/0 未定义引用；"
    "140 个编号对象（75 定理类 + 65 公式）；48 条文献；译注 %s 条；术语 %s 条；"
    "疑点 %s 条（未解 0）；勘误 %s 条；图 0 张（全为 xy-pic/tikz 交换图）；成品待上传 Release"
)
pages = sys.argv[2] if len(sys.argv) > 2 else "__"
zy = sys.argv[3] if len(sys.argv) > 3 else "__"
terms = sys.argv[4] if len(sys.argv) > 4 else "__"
q = sys.argv[5] if len(sys.argv) > 5 else "__"
err = sys.argv[6] if len(sys.argv) > 6 else "__"
note = note % (pages, zy, terms, q, err)

row = [
    "SY02-20",
    "几何Satake、范畴迹与志村簇的算术",
    "08_source_code/SY02-20_几何Satake范畴迹与志村簇算术",
    "arXiv 预印本",
    "arXiv:1810.07375（Zhu；50 页；2018）",
    "演绎作品；底本为 arXiv 预印本，权利归原作者",
    "低",
    "L2 公开·受限（可撤下）",
    "Release 外链",
    "否",
    "",
    "L4 禁入",
    "manual",
    "合规",
    "2026-11-22",
    note,
]

rows = list(csv.reader(io.open(path, encoding="utf-8", newline="")))
hdr = rows[0]
assert len(hdr) == 16, (len(hdr), hdr)
out = [hdr]
found = False
for r in rows[1:]:
    if r and r[0] == "SY02-20":
        out.append(row)
        found = True
    else:
        out.append(r)
if not found:
    out.append(row)

with io.open(path, "w", encoding="utf-8", newline="") as f:
    csv.writer(f, lineterminator="\n").writerows(out)

print("rows", len(out), "updated" if found else "appended")
