import csv, io, os

path = r"C:\Users\admin\Desktop\数译发布\gitee_shuyi\RELEASE_REGISTER.csv"

with open(path, "r", encoding="utf-8", newline="") as f:
    rows = list(csv.reader(f))

header = rows[0]
assert len(header) == 16, header

new = [
    "SY02-22",
    "Springer 理论与轨道积分讲义",
    "08_source_code/SY02-22_Springer理论与轨道积分讲义",
    "arXiv 预印本",
    "arXiv:1602.01451（Yun；62 页；2016）",
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
    "底本 62 页；中译注本 __ 页；0 error/0 Overfull/0 Missing character；编号对象 __ 个与原文逐条对齐；"
    "56 处 xy-pic 交换图；作者脚注 __ 条保号；译注 __ 条；术语 __ 条；疑点 __ 行（未解 0）；"
    "勘误 E1–E3；成品待上传 Release",
]

ids = [r[0] for r in rows[1:]]
assert "SY02-22" not in ids, "already registered"

pos = len(rows)
for i, r in enumerate(rows[1:], start=1):
    if r[0] > "SY02-22":
        pos = i
        break

rows.insert(pos, new)

with open(path, "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerows(rows)

print("inserted at line", pos + 1, "total rows", len(rows) - 1)
