#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""按术语表在每章首次出现处插入 \\index，保证正文 / 索引 / 术语表三处同步。

用法（在 源码/ 下）：  python ../工程文件/tools/insert_index.py
幂等：先删掉已有的 \\index{...}，再重新插入。
"""
import re
import sys
from pathlib import Path

try:
    from pypinyin import lazy_pinyin
except ImportError:  # 没有 pypinyin 时退化为按汉字排序
    lazy_pinyin = None

ROOT = Path(__file__).resolve().parents[2]      # 工程根目录
SRC = ROOT / "源码"
TERMS = ROOT / "工程文件" / "work" / "术语表.tsv"

INDEX_RE = re.compile(r"\\index\{[^{}]*\}")


def read_order():
    """按 main.tex 里 \\inputif{...} 的顺序取章节文件。"""
    text = (SRC / "main.tex").read_text(encoding="utf-8")
    names = re.findall(r"\\inputif\{([^}]+)\}", text)
    files = [SRC / f"chapters/{n}.tex" for n in names]
    return [f for f in files if f.exists()]


def load_terms():
    rows = []
    for line in TERMS.read_text(encoding="utf-8").splitlines():
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        zh = parts[1].strip()
        if not zh or zh.startswith("zh"):
            continue
        # 只收纯中文词条；含 LaTeX、英文、标点的跳过
        if re.search(r"[A-Za-z0-9$\\{}%/]", zh):
            continue
        if len(zh) < 2:
            continue
        rows.append(zh)
    # 长词优先，避免「微分算子层」抢在「扭微分算子层」之前
    return sorted(set(rows), key=len, reverse=True)


def pinyin_key(zh):
    if lazy_pinyin is None:
        return zh
    return "".join(lazy_pinyin(zh))


def math_spans(text):
    """返回 $...$ 与 \\(...\\) 的区间列表，用于避开数学模式。"""
    spans = []
    for m in re.finditer(r"\$[^$]*\$", text, re.S):
        spans.append((m.start(), m.end()))
    return spans


def first_plain_occurrence(text, term, spans):
    start = 0
    while True:
        i = text.find(term, start)
        if i < 0:
            return -1
        if not any(a <= i < b for a, b in spans):
            return i
        start = i + 1


def main():
    files = read_order()
    terms = load_terms()
    texts = {}
    for f in files:
        t = INDEX_RE.sub("", f.read_text(encoding="utf-8"))
        texts[f] = t

    inserted = {}
    for term in terms:
        for f in files:
            t = texts[f]
            spans = math_spans(t)
            i = first_plain_occurrence(t, term, spans)
            if i < 0:
                continue
            entry = f"{pinyin_key(term)}@{term}|hyperpage"
            texts[f] = t[: i + len(term)] + f"\\index{{{entry}}}" + t[i + len(term):]
            inserted[term] = f.name
            break

    for f, t in texts.items():
        orig = f.read_text(encoding="utf-8")
        if INDEX_RE.sub("", orig) != t:
            f.write_text(t, encoding="utf-8")

    missing = [x for x in terms if x not in inserted]
    print(f"术语 {len(terms)} 条，插入 {len(inserted)} 条，未出现 {len(missing)} 条")
    if missing:
        print("未出现：", "、".join(missing[:40]))


if __name__ == "__main__":
    sys.exit(main())
