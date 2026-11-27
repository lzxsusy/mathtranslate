# -*- coding: utf-8 -*-
"""v1/v2 逐词对齐，列正文改动；输出 external/v1v2_diff.txt。"""
import difflib
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
V1TXT = HERE / "v1txt"
ROOT = HERE.parent.parent.parent
V2TXT = ROOT / "txt" / "04"

sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def page_texts(d):
    n = len(list(d.glob("p*.txt")))
    return [(d / f"p{i:03d}.txt").read_text(encoding="utf-8") for i in range(1, n + 1)]


def toks(s):
    return re.findall(r"[A-Za-z0-9]+|\S", s)


def main():
    p1 = page_texts(V1TXT)
    p2 = page_texts(V2TXT)
    w1 = toks("\n".join(p1))
    w2 = toks("\n".join(p2))
    sm = difflib.SequenceMatcher(None, w1, w2, autojunk=False)
    out = []
    nchg = 0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        nchg += 1
        a = " ".join(w1[i1:i2])
        b = " ".join(w2[j1:j2])
        out.append(f"--[{tag}] v1 words {i1}-{i2} / v2 words {j1}-{j2}")
        out.append(f"   v1: {a[:300]}")
        out.append(f"   v2: {b[:300]}")
        if len(a) > 300 or len(b) > 300:
            out.append(f"   (长度 v1={len(a)} v2={len(b)})")
    (HERE / "v1v2_diff.txt").write_text("\n".join(out), encoding="utf-8")
    print(f"改动块 {nchg} 处，已写 v1v2_diff.txt")
    print(f"v1 words {len(w1)}, v2 words {len(w2)}")
    for line in out[:80]:
        print(line)


if __name__ == "__main__":
    main()
