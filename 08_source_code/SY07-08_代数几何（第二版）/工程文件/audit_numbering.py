# -*- coding: utf-8 -*-
"""编号审计：从成品 PDF 抽出条目编号，检查每节内序号连续、节间衔接、类型顺序。"""
import re, sys, collections
import pymupdf

pdf = r"C:\Users\admin\Desktop\数译发布\shuyi\translations\SY07-08\源码\main.pdf"
doc = pymupdf.open(pdf)
kind = r"(定义|命题|定理|引理|推论|例|注|构造|习题)"
pat = re.compile(rf"^{kind}\s*(\d+)\.(\d+)\.(\d+)\s*[\.．]?\s*(.*)$")

items = []   # (page, kind, sec, sub, num)
for pno in range(doc.page_count):
    txt = doc[pno].get_text()
    for line in txt.split("\n"):
        line = line.strip()
        m = pat.match(line)
        if m:
            items.append((pno + 1, m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4))))

print(f"抽出条目 {len(items)} 条")
# 按 (sec, sub) 分组的连续性
by = collections.OrderedDict()
for pno, k, s, sub, n in items:
    by.setdefault((s, sub), []).append((n, k, pno))

bad = 0
for (s, sub), lst in by.items():
    nums = [x[0] for x in lst]
    if nums != list(range(1, len(nums) + 1)):
        bad += 1
        print(f"!! 节 {s}.{sub} 编号异常: {nums}")
print(f"节内连续性: {len(by)} 节，异常 {bad} 节")

# 全局计数
c = collections.Counter(k for _, k, _, _, _ in items)
print("类型计数:", dict(c))
secs = collections.Counter((s, sub) for _, _, s, sub, _ in items)
print("每节条目数:", {f"{s}.{sub}": n for (s, sub), n in secs.items()})

# 相邻小节衔接（同一大节内 sub 递增时，前一节最后一条 → 下一节第一条应为 .1）
keys = list(by.keys())
for i in range(len(keys) - 1):
    s1, sub1 = keys[i]
    s2, sub2 = keys[i + 1]
    last = by[keys[i]][-1][0]
    print(f"  {s1}.{sub1} 末号={last}  →  {s2}.{sub2} 首号={by[keys[i+1]][0][0]}")
