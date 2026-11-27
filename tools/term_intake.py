#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""教材术语表投稿 → 冻结术语表 + 差异报告。

读 `01_corpus_zh/数语规范/intake/*.tsv`（表头：英文 / 中文 / 来源书 / 版次 / 页码 / 备注），
按「来源书」分组成 `01_corpus_zh/terms_frozen_教材_<书简称>.tsv`（等级固定 B），
并与现有 `TERMS.tsv` 比对，输出「新增 / 一致 / 与本库不同」三条清单。

用法：
    python tools/term_intake.py                # 正常处理
    python tools/term_intake.py --dry-run      # 只报差异，不写冻结表
    python tools/term_intake.py --dir <目录>    # 指定投稿目录（测试用）

注意：本脚本不直接改 `TERMS.tsv`；并入统一表请跑 `tools/build_norm.py`。
书里给的译名照抄，不许在录入时「顺手改正」——差异本身就是结论。
"""
from __future__ import annotations

import argparse
import csv
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INTAKE = ROOT / "01_corpus_zh" / "数语规范" / "intake"
TERMS = ROOT / "01_corpus_zh" / "数语规范" / "TERMS.tsv"
OUT_FROZEN = ROOT / "01_corpus_zh"

HEADER = ["英文", "中文", "来源书", "版次", "页码", "备注"]
FROZEN_HEADER = ["英文", "中文", "等级", "依据", "首次出现", "备注"]


def slugify(name: str) -> str:
    s = re.sub(r"[（）()《》\s]+", "", name)
    s = re.sub(r"[^0-9A-Za-z\u4e00-\u9fff_-]+", "", s)
    return s or "未命名"


def show(path: Path) -> str:
    """相对仓库根的友好路径；投稿目录在仓外时原样打印。"""
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def read_rows(path: Path) -> list[dict]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    out = []
    for i, r in enumerate(rows, start=2):
        clean = {k: (r.get(k) or "").strip() for k in HEADER}
        if not clean["英文"] or not clean["中文"]:
            print(f"  ! {path.name}:{i} 英文或中文为空，已跳过")
            continue
        if not clean["页码"]:
            print(f"  ! {path.name}:{i} 缺页码（{clean['英文']}），该条不能进 B 级")
            continue
        out.append(clean)
    return out


def load_terms() -> dict[str, dict]:
    """外文 → {中文, 等级, 状态}（取 TERMS.tsv 里等级最高/冻结优先的一条）。"""
    rank = {"A": 0, "B": 1, "I": 2, "D": 3}
    best: dict[str, dict] = {}
    if not TERMS.exists():
        return best
    with TERMS.open(encoding="utf-8-sig", newline="") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            key = (r.get("外文") or "").strip()
            if not key:
                continue
            cur = {
                "中文": (r.get("中文") or "").strip(),
                "等级": (r.get("等级") or "D").strip() or "D",
                "状态": (r.get("状态") or "candidate").strip(),
                "来源": (r.get("来源") or "").strip(),
                "ID": (r.get("术语ID") or "").strip(),
            }
            key_rank = (rank.get(cur["等级"], 3), 0 if cur["状态"] == "frozen" else 1)
            if key not in best:
                best[key] = cur
                best[key]["_rank"] = key_rank
            elif key_rank < best[key]["_rank"]:
                cur["_rank"] = key_rank
                best[key] = cur
    return best


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=str(INTAKE))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    intake_dir = Path(args.dir)
    if not intake_dir.exists():
        print(f"投稿目录不存在：{intake_dir}")
        return 1

    files = sorted(
        p for p in intake_dir.glob("*.tsv")
        if not p.name.startswith("_") and "模板" not in p.name
    )
    if not files:
        print(f"没有待处理投稿（{intake_dir}）。把书里的术语表按 README 的格式存成 .tsv 放进来。")
        return 0

    per_book: dict[str, list[dict]] = defaultdict(list)
    for path in files:
        rows = read_rows(path)
        print(f"读到 {path.name}：{len(rows)} 条")
        for r in rows:
            book = r["来源书"] or path.stem
            edition = r["版次"]
            per_book[f"{book}__{edition}"].append(r)

    terms = load_terms()
    total_new = total_same = total_diff = 0

    for book_key, rows in sorted(per_book.items()):
        book, _, edition = book_key.partition("__")
        slug = slugify(book)
        new, same, diff = [], [], []
        seen: set[tuple[str, str]] = set()
        for r in rows:
            k = (r["英文"], r["中文"])
            if k in seen:
                continue
            seen.add(k)
            cur = terms.get(r["英文"])
            if cur is None:
                new.append(r)
            elif cur["中文"] == r["中文"]:
                same.append((r, cur))
            else:
                diff.append((r, cur))

        total_new += len(new)
        total_same += len(same)
        total_diff += len(diff)

        print(f"\n== {book}（{edition}）：共 {len(seen)} 条 → 新增 {len(new)} / 一致 {len(same)} / 不同 {len(diff)}")

        rep = intake_dir / f"_报告_{slug}.md"
        lines = [
            f"# 教材术语投稿报告：{book}（{edition}）",
            "",
            f"来源文件：{', '.join(p.name for p in files)}",
            f"合计 {len(seen)} 条：**新增 {len(new)}**、与库一致 {len(same)}、**与库不同 {len(diff)}**。",
            "",
            "## 一、本库没有（新增，等级 B）",
            "",
        ]
        lines += [f"- `{r['英文']}` → **{r['中文']}**（p.{r['页码']}）" for r in new] or ["（无）"]
        lines += ["", "## 二、与本库译名不同（需裁定，优先保留本库冻结值）", "",
                  "| 英文 | 书中 | 本库 | 本库等级/状态 | 页 |", "|---|---|---|---|---|"]
        lines += [f"| `{r['英文']}` | {r['中文']} | {c['中文']} | {c['等级']}/{c['状态']} | {r['页码']} |"
                  for r, c in diff] or ["| （无） | | | | |"]
        lines += ["", "## 三、与库一致（可作为该译名的 B 级依据补强）", ""]
        lines += [f"- `{r['英文']}` → {r['中文']}（p.{r['页码']}）" for r, _ in same] or ["（无）"]
        lines += ["", "## 四、下一步", "",
                  "1. 逐条看第二节：能定的并入冻结表（`tools/build_norm.py` 后刷新 CONFLICTS），不能定的登记 `_meta/冲突台账.tsv`；",
                  "2. 第一节的新增条目随 `terms_frozen_教材_*.tsv` 一起被 `build_norm.py` 吸收为 B 级候选；",
                  "3. 已译工程若用了旧译名，按冲突台账逐条回扫（高频术语优先）。", ""]
        if not args.dry_run:
            rep.write_text("\n".join(lines), encoding="utf-8")
            frozen = OUT_FROZEN / f"terms_frozen_教材_{slug}.tsv"
            with frozen.open("w", encoding="utf-8", newline="") as fh:
                w = csv.writer(fh, delimiter="\t", lineterminator="\n")
                w.writerow(FROZEN_HEADER)
                for r in rows:
                    w.writerow([r["英文"], r["中文"], "B",
                                f"{book}（{edition}）p.{r['页码']}",
                                "—", r["备注"] or "教材术语表投稿"])
            print(f"   写出 {show(frozen)}")
            print(f"   写出 {show(rep)}")

    print(f"\n合计：新增 {total_new} / 一致 {total_same} / 不同 {total_diff}")
    if args.dry_run:
        print("（dry-run：未写任何文件）")
    else:
        print("下一步：python tools/build_norm.py  # 然后 python tools/build_norm.py --check")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
