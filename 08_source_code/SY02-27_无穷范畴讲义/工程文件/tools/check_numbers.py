# -*- coding: utf-8 -*-
"""结构审计：核对译文 chunk 的编号对象与原书抽取源文是否一一对应。

用法：
    python 工程文件/tools/check_numbers.py 02
    python 工程文件/tools/check_numbers.py all

规则：源文中每一处 "N.M." 开头的裸编号段落，以及 "Definition N.M." 等具名对象，
都必须在 chunk 中以 \\label{LNN-N.M} 出现；反之 chunk 中不得出现源文没有的编号。
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(ROOT, "工程文件", "work", "src")
CH = os.path.join(ROOT, "源码", "chunks")

NAMES = ("Definition|Theorem|Proposition|Lemma|Corollary|Example|Exercise|"
         "Construction|Variant|Remark|Notation|Warning|Convention|Question|"
         "Challenge|Claim|Slogan|Conjecture|"
         "(?:Proposition|Theorem|Definition|Corollary|Lemma)-(?:Definition|Construction)")

pat_bare = re.compile(r"^(\d{1,2})\.(\d{1,3})\.(?:\s|$)")
pat_named = re.compile(r"^(%s)\s+(\d{1,2})\.(\d{1,3})(?:\.|\s+\()" % NAMES)


def src_objects(path):
    out = []
    lig = {"\ufb01": "fi", "\ufb02": "fl", "\ufb00": "ff", "\ufb03": "ffi", "\ufb04": "ffl"}
    for line in open(path, encoding="utf-8", errors="replace"):
        for k, v in lig.items():
            line = line.replace(k, v)
        s = line.strip()
        m = pat_bare.match(s) or pat_named.match(s)
        if m:
            nums = m.groups()[-2:]
            out.append(f"{int(nums[0])}.{int(nums[1])}")
    return out


def tex_labels(path):
    txt = open(path, encoding="utf-8", errors="replace").read()
    return re.findall(r"\\label\{L(\d+)-(\d+\.\d+)\}", txt)


def check(nn):
    sfile = os.path.join(SRC, f"lec{nn}.txt")
    tfile = os.path.join(CH, f"lec{nn}.tex")
    if not (os.path.exists(sfile) and os.path.exists(tfile)):
        print(f"[SKIP] lec{nn}: 缺源文或译文")
        return None
    want = sorted(set(src_objects(sfile)), key=lambda x: tuple(map(int, x.split("."))))
    got = [b for n, b in tex_labels(tfile)]
    bad = [g for (n, g) in tex_labels(tfile) if int(n) != int(nn)]
    if bad:
        print(f"[FAIL] lec{nn}: 标签讲号不符 {sorted(set(bad))[:6]}")
    # 多重集比较（同一编号不应重复）
    from collections import Counter
    cw, cg = Counter(want), Counter(got)
    miss = sorted((cw - cg).elements(), key=lambda x: tuple(map(int, x.split("."))))
    extra = sorted((cg - cw).elements(), key=lambda x: tuple(map(int, x.split("."))))
    dup = sorted([k for k, v in cg.items() if v > 1])
    ok = not miss and not extra and not dup
    print(f"[{'OK' if ok else 'FAIL'}] lec{nn}: 源文 {len(want)} 个对象，译文 {len(got)} 个标签")
    if miss:
        print("   缺:", " ".join(miss[:30]))
    if extra:
        print("   多:", " ".join(extra[:30]))
    if dup:
        print("   重复:", " ".join(dup[:30]))
    return ok


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else "all"
    if arg == "all":
        nums = list(range(1, 28))
        rcs = [check(f"{i:02d}") for i in nums]
        pending = [r for r in rcs if r is None]
        bad = [r for r in rcs if r is False]
        print(f"== 通过 {len(rcs)-len(pending)-len(bad)}，失败 {len(bad)}，跳过 {len(pending)}")
        if pending:
            print("   跳过：" + ", ".join("lec%02d" % n for n, r in zip(nums, rcs) if r is None))
        sys.exit(0 if not bad else 1)
    else:
        sys.exit(0 if check(f"{int(arg):02d}") else 1)
