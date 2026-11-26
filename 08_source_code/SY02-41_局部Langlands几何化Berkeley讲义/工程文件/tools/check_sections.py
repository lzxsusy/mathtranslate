# -*- coding: utf-8 -*-
"""SY02-41 分讲自检：页锚数 / 编号条目数 / 环境配对 / 禁用命令 / 交叉引用编号是否对得上。

用法：
  python 工程文件/tools/check_sections.py            # 全部讲
  python 工程文件/tools/check_sections.py 07 08      # 指定讲
"""
import re, sys, pathlib

PROJ = pathlib.Path(__file__).resolve().parents[2]
SRC = pathlib.Path(r"C:\Users\admin\Downloads\fs_scholze_work\pages")

RANGE = {
    1: (2, 6), 2: (7, 11), 3: (12, 16), 4: (17, 21), 5: (22, 26), 6: (27, 31),
    7: (32, 36), 8: (37, 41), 9: (42, 48), 10: (49, 54), 11: (55, 59), 12: (60, 65),
    13: (66, 71), 14: (72, 78), 15: (79, 83), 16: (84, 89), 17: (90, 94), 18: (95, 101),
    19: (102, 107), 20: (108, 112), 21: (113, 117), 22: (118, 123), 23: (124, 127),
    24: (128, 132), 25: (133, 137), 26: (138, 142), 27: (143, 147),
}

ENVS = ["definition", "example", "theorem", "proposition", "lemma", "corollary",
        "remark", "warning", "question", "conjecture", "notation", "fact",
        "exercise", "construction", "hope"]
BAN = ["错致层"]

ITEM = re.compile(r"^(?:Deﬁnition|Definition|Theorem|Proposition|Lemma|Corollary|Remark|Example|Warning|Question|Conjecture|Notation|Fact|Exercise|Construction|Hope)\s+(\d+)\.(\d+)")

# 中文条目名 -> 环境名
CN = {"定义": "definition", "定理": "theorem", "命题": "proposition", "引理": "lemma",
      "推论": "corollary", "注": "remark", "例": "example", "警告": "warning",
      "问": "question", "猜想": "conjecture", "记号": "notation"}
# 「定理 3.3」「命题 5.14」这样的回指
REF = re.compile(r"(定义|定理|命题|引理|推论|注|例|警告|猜想|记号)\s*(\d{1,2})\.(\d{1,3})(?![\d.])")


def src_items(lo, hi, n):
    """本讲的编号条目：收集 p 页内出现的 n.k（k 连续 1..K）。

    只认「类型 n.k.」形式（数字后紧跟句点），故行中的回指「Theorem 19.9 is a
    consequence…」不会误计；再按 k 去重，K 即条目总数。返回 [(页码, 首行)]，
    页码取该编号首次出现的页。
    """
    seen = {}
    pat = re.compile(ITEM.pattern.replace("^", ""))
    for p_ in range(lo, hi + 1):
        f = SRC / ("p%03d.txt" % p_)
        if not f.exists():
            continue
        for line in f.read_text(encoding="utf-8").splitlines():
            for m in pat.finditer(line):
                if int(m.group(1)) != n:
                    continue
                k = int(m.group(2))
                seen.setdefault(k, (p_, line.strip()[:40]))
    out = [seen[k] for k in sorted(seen)]
    return out


def texfile(n):
    return next(PROJ.glob("源码/sections/s%02d-*.tex" % n), None)


def env_seq(n):
    """第 n 讲按出现顺序的条目环境名列表（即 n.1, n.2, ...）。"""
    f = texfile(n)
    if f is None:
        return []
    t = f.read_text(encoding="utf-8")
    return [m.group(1) for m in re.finditer(
        r"\\begin\{(definition|theorem|proposition|lemma|corollary|remark|example|warning|question|conjecture|notation|fact|exercise|construction|hope)\}", t)]


def check(n):
    lo, hi = RANGE[n]
    f = texfile(n)
    if f is None:
        return ["缺文件 s%02d-*.tex" % n]
    t = f.read_text(encoding="utf-8")
    probs = []
    pages = [int(x) for x in re.findall(r"\\srcpage\{(\d+)\}", t)]
    want = list(range(lo, hi + 1))
    if pages != want:
        probs.append("页锚 %s ≠ 期望 %s" % (pages, want))
    n_src = len(src_items(lo, hi, n))
    n_env = 0
    for e in ENVS:
        b = len(re.findall(r"\\begin\{%s\}" % e, t))
        en = len(re.findall(r"\\end\{%s\}" % e, t))
        if b != en:
            probs.append("环境 %s begin %d ≠ end %d" % (e, b, en))
        n_env += b
    if n_src != n_env:
        probs.append("编号条目 源 %d ≠ 译 %d（差 %+d）" % (n_src, n_env, n_env - n_src))
    if t.count("$") % 2:
        probs.append("$ 计数为奇数 %d" % t.count("$"))
    for bad in (r"\usepackage", r"\documentclass", r"\begin{document}"):
        if bad in t:
            probs.append("出现 " + bad)
    for bad in (r"\eqref", r"\ref{", r"\label", r"\cite"):
        if bad in t:
            probs.append("出现 %s（禁用：公式一律不编号）" % bad)
    hit = [b for b in BAN if b in t]
    if hit:
        probs.append("出现 %s（只许在译注内，人工确认）" % hit)
    return probs


def check_refs(n):
    """交叉引用核验：文中「定理 x.y」等回指，第 x 讲的第 y 条必须是同类条目。"""
    f = texfile(n)
    if f is None:
        return []
    t = f.read_text(encoding="utf-8")
    # 去掉译注与脚注内容，只看正文
    body = re.sub(r"\\yizhu\{.*?\}\{.*?\}", "", t, flags=re.S)
    probs = []
    for m in REF.finditer(body):
        kind = CN[m.group(1)]
        lec, num = int(m.group(2)), int(m.group(3))
        seq = env_seq(lec)
        if not seq:
            continue  # 该讲还没译，暂不判定
        if num > len(seq):
            probs.append("回指「%s」超出第 %d 讲条目数 %d" % (m.group(0), lec, len(seq)))
        elif seq[num - 1] != kind:
            probs.append("回指「%s」但第 %d 讲第 %d 条是 %s" % (m.group(0), lec, num, seq[num - 1]))
    return probs


def main():
    nums = [int(a) for a in sys.argv[1:]] or sorted(RANGE)
    bad = 0
    for n in nums:
        probs = check(n) + check_refs(n)
        if probs:
            bad += 1
            print("第 %d 讲：" % n)
            for p in probs:
                print("   - " + p)
        else:
            print("第 %d 讲：OK" % n)
    print("\n%d/%d 讲有待修问题" % (bad, len(nums)))


if __name__ == "__main__":
    main()
