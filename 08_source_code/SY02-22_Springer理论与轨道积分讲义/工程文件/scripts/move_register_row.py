import csv

path = r"C:\Users\admin\Desktop\数译发布\gitee_shuyi\RELEASE_REGISTER.csv"

with open(path, "r", encoding="utf-8", newline="") as f:
    rows = list(csv.reader(f))

# 先移除已插入的 SY02-22 行，再按「最后一个 SY02-2x 之后」重插
target = [r for r in rows[1:] if r[0] == "SY02-22"]
assert len(target) == 1
new = target[0]
rows = [r for r in rows if r[0] != "SY02-22"]

pos = 1
for i, r in enumerate(rows[1:], start=1):
    if r[0].startswith("SY02-2"):
        pos = i + 1
rows.insert(pos, new)

with open(path, "w", encoding="utf-8", newline="") as f:
    csv.writer(f).writerows(rows)

print("moved to line", pos + 1)
for r in rows[max(0, pos - 2):pos + 2]:
    print(r[0], "|", r[1][:20])
