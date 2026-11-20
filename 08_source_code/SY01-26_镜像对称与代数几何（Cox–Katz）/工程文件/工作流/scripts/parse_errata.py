#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 AMS 官方勘误（2020-01-29 版，typos.pdf 的 pdftotext 输出）解析成对照表骨架。

输入：userpdf/typos.txt（pdftotext -layout）
输出：官方勘误2020对照表.md（表格：序号 | 官方页 | 条目（原文摘录） | 译本状态 | 备注）
状态默认「待核」，已人工核过的在 STATUS 字典里覆盖。
"""
import io
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "userpdf", "typos_raw.txt")

# 已人工核对的条目（键=官方页, 值=(状态, 备注)）；同页多条时用 (页, 序号) 精确指定
STATUS = {
    ("16", 1): ("已吸收", "译本 (2.1) 的 A 模型关联函数求和已是 d=0"),
    ("98", None): ("已吸收", "译本 (5.43) 把 (−1)^{Σc₁·β_j} 提为前置因子，与勘误的 (−λ_{r+i}) 写法等价"),
}


def parse(path):
    txt = io.open(path, encoding="utf-8", errors="replace").read()
    txt = re.sub(r"\s+", " ", txt)
    parts = re.split(r"(?=Pages?\s+(?:\d+|xviii|xx)\b)", txt)
    items = []
    for part in parts:
        part = part.strip()
        m = re.match(r"^Pages?\s+([0-9xvi]+(?:[–-][0-9xvi]+)?)\s*[,:]\s*(.*)$", part)
        if not m:
            continue
        page, body = m.group(1), m.group(2).strip()
        if not body or body.startswith("Errata"):
            continue
        items.append({"page": "Page " + page, "text": body})
    return items


def page_key(p):
    m = re.search(r"(\d+)", p)
    return m.group(1) if m else p


def main():
    items = parse(SRC)
    out = ["# 官方勘误（2020-01-29 版）对照表", "",
           "来源：Cox–Katz 官方勘误 `surv-68-errata.pdf`，2020-01-29 版（用户 2026-11-20 提供 `typos.pdf`）。",
           "译本位置换算：**PDF 页 = 印刷页 + 23**（`\\SourcePage{N}` 的 N 即 PDF 页）。",
           "状态说明：已吸收＝译本已按勘误处理；待核＝尚未逐条比对；已修＝本轮按勘误改过；不适用＝中文改写后不涉及。", "",
           "| # | 官方页 | 条目（原文摘录） | 译本状态 | 备注 |", "|---|---|---|---|---|"]
    for i, it in enumerate(items, 1):
        pk = page_key(it["page"])
        st, note = STATUS.get((pk, None), ("待核", ""))
        text = it["text"].replace("|", "\\|")
        if len(text) > 220:
            text = text[:217] + "…"
        out.append(f"| {i} | {it['page']} | {text} | {st} | {note} |")
    out.append("")
    out.append(f"共 {len(items)} 条。")
    dst = os.path.join(BASE, "官方勘误2020对照表.md")
    io.open(dst, "w", encoding="utf-8", newline="\n").write("\n".join(out))
    print(f"parsed {len(items)} items -> {dst}")


if __name__ == "__main__":
    main()
