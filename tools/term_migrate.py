#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""把已裁定的术语变体在译文里统一成冻结译名（术语迁移/清洁）。

设计要点
--------
1. **保护译注**：`\\yizhu{...}` 与 `\\footnote{...}` 里的内容默认不动——那里出现
   「学界亦作完美胚空间」是解释，不是错。要动加 `--inside-notes`。
2. **长词优先**：按变体长度降序替换，避免 `完美胚` 先吃掉 `完美胚空间`。
3. **并发保护**：默认跳过最近 N 小时被改过的文件（别的会话可能正在写），
   `--max-age-hours 0` 关闭。
4. **先看再改**：`--dry-run` 只统计不落盘；`--write` 才写，且每文件留 `.bak`。

用法
----
    # 看影响面
    python tools/term_migrate.py --map 01_corpus_zh/数语规范/_清洁/变体映射.tsv \
        08_source_code/SY02-26_局部Langlands对应的几何化 --dry-run

    # 真改（先确认该工程没人在写）
    python tools/term_migrate.py --map ... --write 08_source_code/SY02-26_...

映射表 TSV（无表头或用 # 注释）：
    变体	应作	备注
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import sys
import time
from pathlib import Path

NOTE_CMDS = ("\\yizhu", "\\footnote")


def read_map(path: Path) -> list[tuple[str, str]]:
    pairs: list[tuple[str, str]] = []
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        a, b = parts[0].strip(), parts[1].strip()
        if a and b and a != b:
            pairs.append((a, b))
    pairs.sort(key=lambda p: len(p[0]), reverse=True)
    return pairs


def protected_spans(text: str) -> list[tuple[int, int]]:
    """返回 \\yizhu{...} / \\footnote{...} 的 (start, end) 区间（含命令名）。"""
    spans: list[tuple[int, int]] = []
    for cmd in NOTE_CMDS:
        idx = 0
        while True:
            i = text.find(cmd, idx)
            if i < 0:
                break
            j = i + len(cmd)
            while j < len(text) and text[j] in " \t":
                j += 1
            if j >= len(text) or text[j] != "{":
                idx = i + len(cmd)
                continue
            depth = 0
            k = j
            while k < len(text):
                c = text[k]
                if c == "\\":
                    k += 2
                    continue
                if c == "{":
                    depth += 1
                elif c == "}":
                    depth -= 1
                    if depth == 0:
                        k += 1
                        break
                k += 1
            spans.append((i, k))
            idx = k
    return spans


def apply_map(text: str, pairs: list[tuple[str, str]], inside_notes: bool) -> tuple[str, list[tuple[str, str, int]]]:
    spans = [] if inside_notes else protected_spans(text)
    counts: dict[tuple[str, str], int] = {}

    def is_protected(pos: int) -> bool:
        return any(s <= pos < e for s, e in spans)

    for old, new in pairs:
        if old.startswith("re:"):
            rx = re.compile(old[3:])
            n = 0
            out = []
            last = 0
            for m in rx.finditer(text):
                if is_protected(m.start()):
                    continue
                out.append(text[last:m.start()])
                out.append(m.expand(new))
                last = m.end()
                n += 1
            if not n:
                continue
            out.append(text[last:])
            text = "".join(out)
            counts[(old, new)] = counts.get((old, new), 0) + n
            continue
        if old not in text:
            continue
        out = []
        i = 0
        n = 0
        while True:
            j = text.find(old, i)
            if j < 0:
                out.append(text[i:])
                break
            if is_protected(j):
                out.append(text[i:j + len(old)])
                i = j + len(old)
                continue
            out.append(text[i:j])
            out.append(new)
            n += 1
            i = j + len(old)
        text = "".join(out)
        if n:
            counts[(old, new)] = counts.get((old, new), 0) + n
    return text, [(o, nw, c) for (o, nw), c in counts.items()]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("projects", nargs="+", help="工程目录（相对仓库根）")
    ap.add_argument("--map", required=True, help="变体映射 TSV")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--inside-notes", action="store_true", help="连译注/脚注一起改（不建议）")
    ap.add_argument("--max-age-hours", type=float, default=6.0,
                    help="跳过最近 N 小时改过的文件；0 = 不检查")
    ap.add_argument("--root", default=".")
    args = ap.parse_args()

    if not args.write and not args.dry_run:
        print("要么 --dry-run 要么 --write（先看再改）。")
        return 2

    root = Path(args.root).resolve()
    pairs = read_map(Path(args.map))
    print(f"映射 {len(pairs)} 条：")
    for a, b in pairs:
        print(f"  {a} → {b}")

    total_files = total_hits = 0
    per_word: dict[tuple[str, str], int] = {}
    skipped: list[str] = []

    for proj in args.projects:
        pdir = (root / proj).resolve()
        if not pdir.exists():
            print(f"! 工程不存在：{proj}")
            continue
        texs = sorted(p for p in pdir.rglob("*.tex"))
        print(f"\n== {proj}：{len(texs)} 个 .tex")
        for tex in texs:
            age_h = (time.time() - tex.stat().st_mtime) / 3600.0
            if args.max_age_hours > 0 and age_h < args.max_age_hours:
                skipped.append(f"{tex.relative_to(root)}（{age_h:.1f}h 前改过）")
                continue
            try:
                text = tex.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                print(f"  ! 非 UTF-8，跳过 {tex.relative_to(root)}")
                continue
            new_text, hits = apply_map(text, pairs, args.inside_notes)
            if not hits:
                continue
            n = sum(c for _, _, c in hits)
            total_files += 1
            total_hits += n
            for o, nw, c in hits:
                per_word[(o, nw)] = per_word.get((o, nw), 0) + c
            detail = "；".join(f"{o}×{c}" for o, _, c in hits)
            print(f"  {tex.relative_to(root)}：{n} 处（{detail}）")
            if args.write:
                shutil.copy2(tex, tex.with_suffix(tex.suffix + ".bak"))
                tex.write_text(new_text, encoding="utf-8")

    print("\n" + "=" * 60)
    for (o, nw), c in sorted(per_word.items(), key=lambda kv: -kv[1]):
        print(f"  {o} → {nw}：{c} 处")
    print(f"合计：{total_files} 个文件，{total_hits} 处")
    if skipped:
        print(f"跳过 {len(skipped)} 个最近改动文件（防并发），例如：")
        for s in skipped[:10]:
            print(f"  {s}")
    if not args.write:
        print("（dry-run：未写任何文件）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
