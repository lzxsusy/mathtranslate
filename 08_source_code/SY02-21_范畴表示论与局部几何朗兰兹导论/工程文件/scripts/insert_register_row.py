# -*- coding: utf-8 -*-
"""把 SY02-21 一行按编号序插入 RELEASE_REGISTER.csv（用 csv 模块，不手工编辑）。

用法： python insert_register_row.py
重复运行会先删掉已有的 SY02-21 行再插入，便于最后更新备注。
"""
import csv
import io
import os

ROOT = r"C:\Users\admin\Desktop\数译发布\gitee_shuyi"
CSV = os.path.join(ROOT, "RELEASE_REGISTER.csv")

ROW = {
    "id": "SY02-21",
    "中文题名": "范畴表示论与局部几何朗兰兹导论",
    "工程目录": "08_source_code/SY02-21_范畴表示论与局部几何朗兰兹导论",
    "底本类型": "arXiv 预印本",
    "底本标识": "arXiv:2205.14578（Dhillon；83 页；2022）",
    "权利状态": "演绎作品；底本为 arXiv 预印本，权利归原作者",
    "风险": "低",
    "源码级别": "L2 公开·受限（可撤下）",
    "成品级别": "Release 外链",
    "成品在仓": "否",
    "成品直链": "",
    "原文级别": "L4 禁入",
    "判定方式": "manual",
    "状态": "合规",
    "复核日期": "2026-11-22",
    "备注": ("底本 83 页；中译注本 __ 页；0 error/0 Overfull/0 Missing character/0 未定义引用；"
             "编号对象 __ 个与原文逐条对齐；图 5 处 xy-pic 交换图；作者脚注 __ 条保号；"
             "译注 __ 条；术语 __ 条；疑点 __ 行（未解 0）；勘误 E1–E3；成品待上传 Release"),
}

with io.open(CSV, encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
    fields = list(rows[0].keys())

rows = [r for r in rows if r["id"] != "SY02-21"]
rows.append(ROW)
rows.sort(key=lambda r: (r["id"][:2], r["id"]))

with io.open(CSV, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    for r in rows:
        w.writerow({k: r.get(k, "") for k in fields})

print("rows:", len(rows), "fields:", len(fields))
print("last ids:", [r["id"] for r in rows[-4:]])
print("SY02-21 in file:", any(r["id"] == "SY02-21" for r in rows))
