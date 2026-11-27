#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""术语基（termbase.jsonl）自身的清洁工具。

三个动作，默认只报告：
  --report            体检：一外多中 / 垃圾行 / 精确重复 / 命名问题
  --apply <映射.tsv>   按「变体 → 应作」把旧译名并到规范译名（改 zh，不删行）
  --write             真的落盘（配合 --apply；--report 永远只读）

设计原则
--------
- **不删证据**：旧译名行不删除，只把 `zh` 改成规范译名——行里的 `pkg`/`note`/`source`
  是它出处的证据，删了就查不到「哪个工程这样译过」。
- **冲突才算错**：同一外文出现两种中文才进 CONFLICTS。并名之后冲突自动消失，
  而统计口径（多少条源自哪个工程）不变。
- **垃圾行单独处理**：含句读、以虚词开头、纯符号的行才是真垃圾，`--drop-junk` 才删。

用法：
    python tools/term_clean.py --report
    python tools/term_clean.py --apply 01_corpus_zh/数语规范/_清洁/变体映射.tsv --write
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TB = ROOT / "01_corpus_zh" / "termbase.jsonl"


def norm(s: str) -> str:
    """去掉空格与连字符差异，用于判断「是不是同一个译名」。"""
    if not s:
        return ""
    return re.sub(r"[\s\-‐‑‒–—·]+", "", s)


def load() -> list[dict]:
    rows = []
    for line in TB.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            print(f"! 坏行，跳过：{line[:60]}")
    return rows


def field(r: dict, *names: str) -> str:
    for n in names:
        v = r.get(n)
        if v:
            return str(v).strip()
    return ""


def junk_reason(zh: str) -> str | None:
    if not zh:
        return "中文为空"
    if re.search(r"[，。、；：？！]", zh):
        return "含句读（抽句残片）"
    if re.match(r"^(的|其|此|该|这|那|所|若|故|则|即|且|而)", zh):
        return "以虚词开头（抽句残片）"
    if len(zh) > 40:
        return f"过长（{len(zh)} 字，疑为句子）"
    return None


def report(rows: list[dict]) -> None:
    by_foreign: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        f = field(r, "foreign", "source_term", "en")
        z = field(r, "zh", "zh_term", "cn")
        if f and z:
            by_foreign[f].append(r)

    multi = {f: rs for f, rs in by_foreign.items() if len({norm(field(r, "zh", "zh_term", "cn")) for r in rs}) > 1}
    print(f"条目 {len(rows)}；有一外多中的外文 {len(multi)} 个")

    print("\n== 一外多中（前 40 组，按候选数/条数排序）==")
    for f, rs in sorted(multi.items(), key=lambda kv: -len({norm(field(r, 'zh', 'zh_term', 'cn')) for r in kv[1]}))[:40]:
        variants: dict[str, list[dict]] = defaultdict(list)
        for r in rs:
            variants[field(r, "zh", "zh_term", "cn")].append(r)
        desc = "；".join(
            f"{z}（{field(rs[0], 'status') or '-'}，{len(v)} 条，{','.join(sorted({field(r, 'pkg') or '?' for r in v}))[:40]}）"
            for z, v in sorted(variants.items(), key=lambda kv: -len(kv[1]))
        )
        print(f"  {f}\n      {desc}")

    print("\n== 垃圾行 ==")
    junk = [(r, junk_reason(field(r, "zh", "zh_term", "cn"))) for r in rows]
    junk = [(r, why) for r, why in junk if why]
    for r, why in junk[:20]:
        print(f"  [{why}] {field(r, 'foreign', 'source_term')} → {field(r, 'zh', 'zh_term', 'cn')[:40]}（{field(r, 'pkg')}）")
    print(f"  合计 {len(junk)} 行")

    print("\n== 精确重复（同外文+同中文+同工程）==")
    seen: dict[tuple, int] = defaultdict(int)
    for r in rows:
        seen[(field(r, "foreign", "source_term"), norm(field(r, "zh", "zh_term", "cn")), field(r, "pkg"))] += 1
    dup = {k: v for k, v in seen.items() if v > 1}
    print(f"  重复组 {len(dup)}，多出 {sum(v - 1 for v in dup.values())} 行")
    for k, v in list(dup.items())[:10]:
        print(f"  {k[0]} / {k[1]} / {k[2]}：{v} 行")


def apply_map(rows: list[dict], mapping: dict[str, str], drop_junk: bool) -> tuple[list[dict], dict[str, int]]:
    stats: dict[str, int] = defaultdict(int)
    out = []
    for r in rows:
        zh_key = "zh" if "zh" in r else ("zh_term" if "zh_term" in r else "cn")
        zh = str(r.get(zh_key) or "").strip()
        if drop_junk and junk_reason(zh):
            stats["删除垃圾行"] += 1
            continue
        if zh in mapping and mapping[zh] != zh:
            r = dict(r)
            r[zh_key] = mapping[zh]
            stats[f"{zh} → {mapping[zh]}"] += 1
        out.append(r)

    # 并名后再去重：同外文+同中文+同工程 + 同 note，只留第一条
    seen: set[tuple] = set()
    dedup = []
    for r in out:
        k = (field(r, "foreign", "source_term"), norm(field(r, "zh", "zh_term", "cn")), field(r, "pkg"), field(r, "note"))
        if k in seen:
            stats["删除并名后重复"] += 1
            continue
        seen.add(k)
        dedup.append(r)
    return dedup, stats


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--apply", metavar="MAP_TSV")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--drop-junk", action="store_true")
    args = ap.parse_args()

    rows = load()
    if args.report or not args.apply:
        report(rows)
        return 0

    mapping: dict[str, str] = {}
    for line in Path(args.apply).read_text(encoding="utf-8-sig").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) >= 2 and parts[0].strip() and parts[1].strip():
            mapping[parts[0].strip()] = parts[1].strip()
    print(f"映射 {len(mapping)} 条")

    new_rows, stats = apply_map(rows, mapping, args.drop_junk)
    print(f"行数 {len(rows)} → {len(new_rows)}")
    for k, v in sorted(stats.items(), key=lambda kv: -kv[1]):
        print(f"  {k}：{v}")

    if not args.write:
        print("（未写盘；加 --write 才落盘）")
        return 0

    shutil.copy2(TB, TB.with_suffix(".jsonl.bak"))
    with TB.open("w", encoding="utf-8", newline="\n") as fh:
        for r in new_rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"已写 {TB.relative_to(ROOT)}（备份 termbase.jsonl.bak）")
    print("下一步：python tools/build_norm.py && python tools/build_norm.py --check")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
