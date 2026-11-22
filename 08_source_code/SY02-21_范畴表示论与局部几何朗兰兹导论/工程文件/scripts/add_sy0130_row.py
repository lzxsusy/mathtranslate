# -*- coding: utf-8 -*-
"""在 RELEASE_REGISTER.csv 中按编号序插入 SY01-30 行（并发会话在建工程，据其 BRIEF 登记）。"""
import csv
import os

R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
path = os.path.join(R, "RELEASE_REGISTER.csv")

with open(path, encoding="utf-8", newline="") as f:
    rows = list(csv.reader(f))

head = rows[0]
body = [r for r in rows[1:] if r and r[0].strip()]
if any(r[0] == "SY01-30" for r in body):
    print("already present")
    raise SystemExit(0)

new = [
    "SY01-30",
    "三维镜像对称",
    "08_source_code/SY01-30_三维镜像对称（Webster–Yoo）",
    "arXiv 预印本",
    "arXiv:2308.06191v1 [math.RT]（Webster–Yoo, 3-dimensional mirror symmetry；23 页；2023；另有 Notices AMS 版）",
    "演绎作品；底本为 arXiv 预印本，权利归原作者",
    "低",
    "L2 公开·受限（可撤下）",
    "申请获取（暂无外链）",
    "否",
    "",
    "L4 禁入",
    "manual",
    "合规",
    "2026-11-22",
    "并发会话在建工程，据其 BRIEF 登记；原文 23 页→译本 29 页；bbl 反推 main.bib 30 条；成品 PDF 未入库",
]

idx = None
for i, r in enumerate(body):
    if r[0] == "SY01-29":
        idx = i + 1
        break
if idx is None:
    idx = len(body)
body.insert(idx, new)

with open(path, "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(head)
    w.writerows(body)
print("inserted at", idx, "total", len(body))
