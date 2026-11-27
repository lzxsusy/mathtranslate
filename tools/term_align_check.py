# -*- coding: utf-8 -*-
"""校验 01_corpus_zh/数语规范/术语对照_香蕉空间.tsv。

检查项：
1. 表头与列数；
2. 「关系」取值合法；
3. 每个「本库译名」都能在 TERMS.tsv 的中文列里找到（或标为“不译”/“无专条”）；
4. 英文列不重复；
5. 「香蕉空间依据」非空。

用法：python tools/term_align_check.py [--quiet]
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZH = ROOT / "01_corpus_zh" / "数语规范"
TABLE = ZH / "术语对照_香蕉空间.tsv"
TERMS = ZH / "TERMS.tsv"

HEADER = ["英文", "本库译名", "香蕉空间译名", "关系", "香蕉空间依据", "说明"]
RELATIONS = {
    "一致", "异名", "异名（大小写）",
    "分歧（本库冻结）", "分歧（保留原文）",
    "无专条", "无",
}


def load_terms() -> set[str]:
    """TERMS.tsv 的中文列 + 各工程 glossary.tsv 的中文列（后者作次级依据）。"""
    out: set[str] = set()
    if TERMS.exists():
        with TERMS.open(encoding="utf-8") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                zh = (row.get("中文") or "").strip()
                if zh:
                    out.add(zh)
    for p in (ROOT / "08_source_code").rglob("glossary.tsv"):
        try:
            with p.open(encoding="utf-8-sig") as fh:
                reader = csv.reader(fh, delimiter="\t")
                for cells in reader:
                    if len(cells) >= 2:
                        zh = cells[1].strip()
                        if zh and not zh.startswith("中文"):
                            out.add(zh)
        except OSError:
            continue
    return out


def main() -> int:
    quiet = "--quiet" in sys.argv
    if not TABLE.exists():
        print(f"[错误] 缺少 {TABLE}")
        return 2

    with TABLE.open(encoding="utf-8") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        if reader.fieldnames != HEADER:
            print(f"[错误] 表头不符：{reader.fieldnames}")
            return 2
        rows = list(reader)

    known = load_terms()
    problems: list[str] = []
    seen: dict[str, int] = {}

    for i, r in enumerate(rows, start=2):
        en = (r["英文"] or "").strip()
        zh = (r["本库译名"] or "").strip()
        rel = (r["关系"] or "").strip()
        ev = (r["香蕉空间依据"] or "").strip()

        if not en:
            problems.append(f"第 {i} 行：英文为空")
        if en in seen:
            problems.append(f"第 {i} 行：英文重复（首次在第 {seen[en]} 行）")
        else:
            seen[en] = i
        if rel not in RELATIONS:
            problems.append(f"第 {i} 行：关系取值非法「{rel}」")
        if not ev:
            problems.append(f"第 {i} 行：香蕉空间依据为空")
        if not zh:
            problems.append(f"第 {i} 行：本库译名为空")
            continue
        if "不译" in zh or rel in {"无专条", "无"}:
            continue
        base = zh.split("（")[0].strip()
        if known and base not in known and zh not in known:
            problems.append(f"第 {i} 行：本库译名「{zh}」不在 TERMS.tsv 中")

    if problems:
        print(f"[失败] {len(problems)} 个问题：")
        for p in problems:
            print("  -", p)
        return 1

    if not quiet:
        from collections import Counter
        print(f"[OK] {len(rows)} 行，关系分布：{dict(Counter(r['关系'] for r in rows))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
