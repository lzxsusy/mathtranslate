# -*- coding: utf-8 -*-
"""按 backup→current 的行号映射，重锚 sy0117 卡片源码里的 chNN.tex:A-B。

用法：
    python reanchor.py --backup <旧章节目录> --chapters <新章节目录> [--write]

旧章节目录里应有 ch01.tex … ch12.tex（第三轮校订前的快照）。
脚本把 cards_concepts.py / cards_concepts2.py / cards_corrections.py 中
形如 "ch04.tex:938-998" 的锚点映射到新行号；加 --write 才会真正写文件。
"""
import argparse
import difflib
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
TARGETS = ["cards_concepts.py", "cards_concepts2.py", "cards_corrections.py"]
ANCHOR = re.compile(r"(ch\d{2}\.tex:)(\d+)-(\d+)")


def read_lines(path):
    with open(path, encoding="utf-8", newline="") as f:
        return [ln.rstrip("\r") for ln in f.read().split("\n")]


def build_maps(backup_dir, chapters_dir):
    maps = {}
    for i in range(1, 13):
        name = "ch%02d.tex" % i
        old = read_lines(os.path.join(backup_dir, name))
        new = read_lines(os.path.join(chapters_dir, name))
        sm = difflib.SequenceMatcher(None, old, new, autojunk=False)
        # old 行号 (1-based) -> new 行号；未匹配的行映射到最近的下一段
        m = {}
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == "equal":
                for k in range(i2 - i1):
                    m[i1 + k + 1] = j1 + k + 1
            else:
                for k in range(i1, i2):
                    m[k + 1] = min(j1 + 1, len(new))
        maps[name[:-4]] = m
    return maps


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--backup", required=True)
    ap.add_argument("--chapters", required=True)
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    maps = build_maps(args.backup, args.chapters)
    changed = 0
    for fn in TARGETS:
        path = os.path.join(HERE, fn)
        with open(path, encoding="utf-8", newline="") as f:
            src = f.read()

        def repl(mo):
            nonlocal changed
            name, a, b = mo.group(1)[:4], int(mo.group(2)), int(mo.group(3))
            m = maps[name]
            na, nb = m.get(a), m.get(b)
            if not na or not nb:
                return mo.group(0)
            if (na, nb) != (a, b):
                changed += 1
            return "%s.tex:%d-%d" % (name, na, nb)

        out = ANCHOR.sub(repl, src)
        if args.write and out != src:
            with open(path, "w", encoding="utf-8", newline="\n") as f:
                f.write(out)
        print("%s: %d anchors" % (fn, len(ANCHOR.findall(src))))
    print("total changed:", changed)


if __name__ == "__main__":
    main()
