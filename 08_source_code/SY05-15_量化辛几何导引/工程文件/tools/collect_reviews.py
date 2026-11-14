#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""汇总审校记录：复制各章 review 文件，并生成合并版。"""
import re
from pathlib import Path

QSG = Path(__file__).resolve().parent.parent
NOTES = QSG / "notes"
DST = QSG / "审校记录"

ORDER = ["ch01", "ch02", "ch03", "ch04", "ch05a", "ch05b", "ch06", "ch07",
         "ch08", "ch09a", "ch09b", "ch10a", "ch10b"]
TITLES = {
    "ch01": "第 1 章 辛流形", "ch02": "第 2 章 辛拓扑中的物理", "ch03": "第 3 章 切触几何",
    "ch04": "第 4 章 Moser 论证", "ch05a": "第 5 章（上）Floer 理论 5.1–5.2",
    "ch05b": "第 5 章（下）Floer 理论 5.3–5.5", "ch06": "第 6 章 定量刻画",
    "ch07": "第 7 章 杂论", "ch08": "第 8 章 量子上同调", "ch09a": "第 9 章（上）9.1–9.3",
    "ch09b": "第 9 章（下）9.4–9.7", "ch10a": "第 10 章（上）10.1–10.4",
    "ch10b": "第 10 章（下）10.5–10.8",
}


def main():
    DST.mkdir(exist_ok=True)
    parts = ["# 原文疑误与审校记录汇总\n",
             "本文件由各章译者提交的 `review_*.md` 自动汇总，逐条给出原书疑误、"
             "记号不一致与处理方式。正文中对应位置均有 `% [Tutor Note: 原文疑误——…]` 批注；"
             "译文原则上**保留原文写法**，仅加注说明，不擅改原书内容。\n"]
    total = 0
    for key in ORDER:
        src = NOTES / f"review_{key}.md"
        if not src.exists():
            continue
        text = src.read_text(encoding="utf-8")
        (DST / f"review_{key}.md").write_text(text, encoding="utf-8")
        n = len(re.findall(r"(?m)^\s*(?:\d+[\.、)]|[-*]\s)", text))
        total += n
        parts.append(f"\n\n---\n\n## {TITLES.get(key, key)}\n\n" + text.strip() + "\n")
    (DST / "review_原文疑误_汇总.md").write_text("".join(parts), encoding="utf-8")

    # 其他记录
    for name in ("QA_report.md", "backup_before_fix/SUMMARY.md"):
        p = NOTES / name
        if p.exists():
            (DST / Path(name).name).write_text(p.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"汇总完成：{DST}  （列表条目约 {total} 条）")


if __name__ == "__main__":
    main()
