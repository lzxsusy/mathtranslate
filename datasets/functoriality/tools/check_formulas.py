#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_formulas.py —— 公式子串回查。

资料卡的 formulas 必须逐字取自中译本对应章的 .tex 源码；本工具把每条公式
去掉空白后，在给定的语料（中译本 chapter*.tex 拼接）里做子串查找，找不到即报错。

用法：
    python tools/check_formulas.py cards --corpus /path/to/book/chapter*.tex
    python tools/check_formulas.py cards --corpus /path/to/book          # 自动取目录下 chapter*.tex

说明：语料不在仓库内（中译本源码单独保管），因此本工具需要显式给 --corpus；
仓库里的卡片本身不依赖语料也能通过 lint_cards.py。
"""
import argparse
import glob
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def norm(s: str) -> str:
    """去掉全部空白，并去掉公式定界符，便于子串比对。"""
    s = s.strip()
    if s.startswith("$$") and s.endswith("$$"):
        s = s[2:-2]
    elif s.startswith("$") and s.endswith("$"):
        s = s[1:-1]
    return "".join(s.split())


def load_corpus(patterns):
    files = []
    for pat in patterns:
        if Path(pat).is_dir():
            files.extend(sorted(glob.glob(str(Path(pat) / "chapter*.tex"))))
        else:
            files.extend(sorted(glob.glob(pat)))
    if not files:
        raise SystemExit(f"语料为空：{patterns}")
    text = "\n".join(Path(f).read_text(encoding="utf-8") for f in files)
    return norm(text), files


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cards", nargs="?", default="cards")
    ap.add_argument("--corpus", nargs="+", required=True)
    args = ap.parse_args()

    corpus, files = load_corpus(args.corpus)
    card_files = sorted((ROOT / args.cards).glob("**/*.json"))
    if not card_files:
        print("没有找到卡片")
        return 1

    print(f"语料：{len(files)} 个文件，归一化后 {len(corpus)} 字符")
    total = ok = 0
    problems = []
    for p in card_files:
        card = json.loads(p.read_text(encoding="utf-8"))
        rel = p.relative_to(ROOT)
        for i, f in enumerate(card.get("formulas", []) or [], 1):
            total += 1
            if norm(f) and norm(f) in corpus:
                ok += 1
            else:
                problems.append(f"{rel}: formulas[{i}] 未在语料中找到：{f[:80]}")
        for t in card.get("theorems", []) or []:
            st = t.get("statement", "")
            for m in __import__("re").findall(r"\$\$?(.+?)\$\$?", st):
                if len(norm(m)) < 6:
                    continue
                total += 1
                if norm(m) in corpus:
                    ok += 1
                else:
                    problems.append(f"{rel}: theorem「{t.get('name')}」陈述里的公式未在语料中找到：{m[:60]}")

    for msg in problems:
        print("ERROR", msg)
    print(f"{'OK' if not problems else 'FAIL'}：{ok}/{total} 条公式在语料中找到（{len(problems)} 条未命中）")
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
