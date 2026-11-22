# -*- coding: utf-8 -*-
"""把 RELEASE_REGISTER.csv 恢复成「HEAD 原序 + 在尾部追加的新行」，并追加 SY02-21 行。

背景：insert_register_row.py 曾把整表按 id 重排，破坏了原有（按建库先后）的行序。
本脚本以 HEAD 的行序为准重建，保留工作区里别人新加的行（如 SY02-20），再补上 SY02-21。
用法： python fix_register_order.py
"""
import io
import subprocess

ROOT = r"C:\Users\admin\Desktop\数译发布\gitee_shuyi"
CSV = ROOT + r"\RELEASE_REGISTER.csv"

head = subprocess.run(["git", "-C", ROOT, "show", "HEAD:RELEASE_REGISTER.csv"],
                      capture_output=True).stdout.decode("utf-8")
head_lines = [l for l in head.split("\n") if l.strip()]
head_ids = set(l.split(",")[0] for l in head_lines[1:])

cur = io.open(CSV, encoding="utf-8").read().split("\n")
cur_lines = [l for l in cur if l.strip()]

extra = [l for l in cur_lines[1:] if l.split(",")[0] not in head_ids]
extra = [l for l in extra if l.split(",")[0] != "SY02-21"]

row21 = [l for l in cur_lines[1:] if l.split(",")[0] == "SY02-21"]

out = head_lines + extra + row21
io.open(CSV, "w", encoding="utf-8", newline="").write("\n".join(out) + "\n")
print("head rows:", len(head_lines) - 1, "extra:", [e.split(",")[0] for e in extra],
      "row21:", len(row21), "total:", len(out) - 1)
