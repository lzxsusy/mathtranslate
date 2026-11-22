import csv, io

p = r"C:\Users\admin\Desktop\数译发布\gitee_shuyi\RELEASE_REGISTER.csv"
with io.open(p, encoding="utf-8", newline="") as f:
    rows = list(csv.reader(f))

hdr = rows[0]
n = 0
for r in rows:
    if r and r[0] == "SY02-22":
        note = ("底本 62 页；中译注本 71 页；0 error/0 Overfull/0 Missing character/0 未定义引用；"
                "250 个编号对象（161 小节 + 37 公式 + 30 子节 + 10 定理 + 3 命题 + 2 引理 + 2 注 + 5 讲）"
                "与原文逐条对齐；图 5 处 xy-pic 交换图；作者脚注按原序保留；译注 8 条；术语 112 条；"
                "疑点 14 条（未解 0）；勘误 E1、E2；成品 PDF 71 页已生成")
        assert len(r) == 16, len(r)
        r[15] = note
        n += 1
assert n == 1, n

with io.open(p, "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerows(rows)

with io.open(p, encoding="utf-8") as f:
    for line in f:
        if line.startswith("SY02-22"):
            print(len(line.split(",")), "fields-ish")
            print(line[:120])
            print("...")
            print(line[-160:])
