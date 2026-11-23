#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""统一 \label 命名：每个标签加章号前缀，消除跨章重复与未定义引用。

各单元译者按「节.序号」给标签（如 \label{lem:1.2}），不同章会撞号；
本脚本把章 C 内文件里的 \label{X:a.b} 改成 \label{X:C.a.b}，
并把 \ref{X:a.b} 解析到唯一存在的标签上；解析不到就退化为纯数字文本。

用法（在 源码/ 下）：
    python ../工程文件/tools/fix_labels.py [--dry-run]
"""
import os
import re
import sys
import collections

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(os.path.dirname(os.path.dirname(HERE)), "源码")

MAIN = os.path.join(SRC, "main.tex")
CHAP_RE = re.compile(r"\\inputif\{(ch(\d+)[a-z]?)\}")
LABEL_RE = re.compile(r"\\label\{([a-zA-Z]+):([0-9][0-9.]*)\}")
REF_RE = re.compile(r"\\(ref|eqref)\{([a-zA-Z]+):([0-9][0-9.]*)\}")


def chapters():
    """返回 [(文件名, 章号)]，按 main.tex 顺序。"""
    text = open(MAIN, encoding="utf-8").read()
    out = []
    for name, ch in CHAP_RE.findall(text):
        p = os.path.join(SRC, "chapters", name + ".tex")
        if os.path.exists(p):
            out.append((p, ch))
    return out


def main():
    dry = "--dry-run" in sys.argv
    files = chapters()
    texts = {p: open(p, encoding="utf-8").read() for p, _ in files}

    # 收集所有标签（原样）与改后名
    labels = {}           # 新名 -> 文件
    for p, ch in files:
        for kind, num in LABEL_RE.findall(texts[p]):
            parts = num.split(".")
            new = num if parts[0] == ch else "%s.%s" % (ch, num)
            labels.setdefault("%s:%s" % (kind, new), p)

    changed_labels = changed_refs = literalized = 0
    for p, ch in files:
        t = texts[p]

        def lab(m):
            nonlocal changed_labels
            kind, num = m.group(1), m.group(2)
            parts = num.split(".")
            new = num if parts[0] == ch else "%s.%s" % (ch, num)
            if new != num:
                changed_labels += 1
            return "\\label{%s:%s}" % (kind, new)

        t = LABEL_RE.sub(lab, t)

        def ref(m):
            nonlocal changed_refs, literalized
            cmd, kind, num = m.group(1), m.group(2), m.group(3)
            parts = num.split(".")
            # 候选：本章的 C.num，或原样的 num
            cands = []
            if parts[0] != ch:
                cands.append("%s:%s.%s" % (kind, ch, num))
            cands.append("%s:%s" % (kind, num))
            for c in cands:
                if c in labels:
                    if c != "%s:%s" % (kind, num):
                        changed_refs += 1
                    return "\\%s{%s}" % (cmd, c)
            literalized += 1
            return num          # 解析不到：写成纯数字（原文编号）

        t = REF_RE.sub(ref, t)
        texts[p] = t

    for p, _ in files:
        orig = open(p, encoding="utf-8").read()
        if texts[p] != orig and not dry:
            open(p, "w", encoding="utf-8").write(texts[p])

    print("文件 %d 个；改标签 %d 处，改引用 %d 处，退化为数字 %d 处%s" %
          (len(files), changed_labels, changed_refs, literalized, "（dry-run）" if dry else ""))
    seen = {}
    for p, _ in files:
        for m in LABEL_RE.finditer(texts[p]):
            name = "%s:%s" % (m.group(1), m.group(2))
            seen.setdefault(name, []).append(os.path.basename(p))
    dup = {k: v for k, v in seen.items() if len(v) > 1}
    if dup:
        print("仍有重复标签 %d 个：" % len(dup), list(dup.items())[:5])
    else:
        print("标签全部唯一（%d 个）" % len(seen))
    return 0


if __name__ == "__main__":
    sys.exit(main())
