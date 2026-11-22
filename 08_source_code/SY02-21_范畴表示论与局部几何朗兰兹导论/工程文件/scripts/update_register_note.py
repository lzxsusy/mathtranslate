import io, csv, os, subprocess
root = r"C:\Users\admin\Desktop\数译发布\gitee_shuyi"
p = os.path.join(root, "RELEASE_REGISTER.csv")

# 以 git HEAD 的版本为骨架，避免把工作区里别人的改动写丢
raw = subprocess.run(["git", "-C", root, "show", "HEAD:RELEASE_REGISTER.csv"],
                     capture_output=True, check=True).stdout.decode("utf-8")
rows = list(csv.reader(io.StringIO(raw)))
assert rows[0][0] == "id" and len(rows[0]) == 16

note = ("原文 83 页→译本 105 页；编号对象 288（定理 4／定义 1／注 66／例 54／编号段 163）；"
        "编号公式 72；表 3；参考文献 151；译注 4；术语 77；疑点 10（未解 0）；勘误 9（E1–E8、N1）；"
        "0 error/0 Overfull/0 Missing character/0 未定义引用；标签 132=132；成品待上传 Release")

n = 0
for r in rows[1:]:
    if r and r[0] == "SY02-21":
        assert len(r) == 16, len(r)
        r[12] = "manual"          # 判定方式
        r[13] = "合规"            # 状态
        r[14] = "2026-11-22"      # 复核日期
        r[15] = note              # 备注
        n += 1
assert n == 1, n

buf = io.StringIO()
csv.writer(buf, lineterminator="\n", quoting=csv.QUOTE_MINIMAL).writerows(rows)
out = buf.getvalue()
if not out.endswith("\n"):
    out += "\n"
io.open(p, "w", encoding="utf-8", newline="").write(out)
print("rows", len(rows), "updated", n)
for r in rows:
    if r and r[0] == "SY02-21":
        print("check:", r[12], r[13], r[14], r[15][:30])
