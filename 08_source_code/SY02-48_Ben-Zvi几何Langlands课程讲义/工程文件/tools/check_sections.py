# -*- coding: utf-8 -*-
"""SY02-48 分讲自检：页锚 / 编号条目 / 环境配对 / 禁用命令 / 交叉引用。

用法：
  python 工程文件/tools/check_sections.py          # 全部讲
  python 工程文件/tools/check_sections.py 07 08    # 指定讲
"""
import re, sys, pathlib

PROJ = pathlib.Path(__file__).resolve().parents[2]
LEC = PROJ / "lectures"
SEC = PROJ / "源码" / "sections"

ENVS = ["definition", "example", "theorem", "proposition", "lemma", "corollary",
        "remark", "warning", "question", "conjecture", "notation", "fact",
        "exercise", "construction", "hope"]

ITEM = re.compile(
    r"^(?:Deﬁnition|Definition|Theorem|Proposition|Lemma|Corollary|Remark|Example|"
    r"Warning|Question|Conjecture|Notation|Fact|Exercise|Construction|Hope)\s+(\d+)\.(\d+)",
    re.M)

CN = {"定义": "definition", "定理": "theorem", "命题": "proposition", "引理": "lemma",
      "推论": "corollary", "注": "remark", "例": "example", "警告": "warning",
      "问": "question", "猜想": "conjecture", "记号": "notation"}

REF = re.compile(r"(定义|定理|命题|引理|推论|注|例|警告|猜想|记号)\s*(\d{1,2})\.(\d{1,3})(?![\d.])")

SRCPAGE = re.compile(r"\\srcpage\{(\d+)\}")
SRCPAGEINL = re.compile(r"\\srcpageinl\{(\d+)\}")
PAGEMARK = re.compile(r"原文 p(\d+) =====")


def texfile(n):
    return next(PROJ.glob("源码/sections/s%02d-*.tex" % n), None)


def lecfile(n):
    return LEC / ("L%02d.txt" % n)


def src_pages(n):
    return [int(x) for x in PAGEMARK.findall(lecfile(n).read_text(encoding="utf-8"))]


def src_items(n):
    t = lecfile(n).read_text(encoding="utf-8")
    seen = set()
    for m in ITEM.finditer(t):
        if int(m.group(1)) == n:
            seen.add(int(m.group(2)))
    return len(seen)


def env_seq(n):
    f = texfile(n)
    if f is None:
        return []
    t = f.read_text(encoding="utf-8")
    return [m.group(1) for m in re.finditer(
        r"\\begin\{(definition|theorem|proposition|lemma|corollary|remark|example|warning|"
        r"question|conjecture|notation|fact|exercise|construction|hope)\}", t)]


def check(n):
    f = texfile(n)
    if f is None:
        return ["缺文件 s%02d-*.tex" % n]
    t = f.read_text(encoding="utf-8")
    probs = []
    body = lecfile(n).read_text(encoding="utf-8")
    empty = len(re.sub(r"%%%%%.*", "", body).strip()) < 200
    if not empty:
        pages = [int(x) for x in SRCPAGE.findall(t)]
        want = src_pages(n)
        if pages != want:
            probs.append("页锚 %s ≠ 期望 %s" % (pages, want))
        n_src = src_items(n)
        n_env = sum(len(re.findall(r"\\begin\{%s\}" % e, t)) for e in ENVS)
        if n_src != n_env:
            probs.append("编号条目 源 %d ≠ 译 %d（差 %+d）" % (n_src, n_env, n_env - n_src))
    for e in ENVS:
        b = len(re.findall(r"\\begin\{%s\}" % e, t))
        en = len(re.findall(r"\\end\{%s\}" % e, t))
        if b != en:
            probs.append("环境 %s begin %d ≠ end %d" % (e, b, en))
    if t.count("$") % 2:
        probs.append("$ 计数为奇数 %d" % t.count("$"))
    if t.count("\\[") != t.count("\\]"):
        probs.append("\\[ %d ≠ \\] %d" % (t.count("\\["), t.count("\\]")))
    for bad in ("\\usepackage", "\\documentclass", "\\begin{document}", "\\section*"):
        if bad in t:
            probs.append("出现 " + bad)
    for bad in ("\\eqref", "\\ref{", "\\label", "\\cite"):
        if bad in t:
            probs.append("出现 %s（禁用）" % bad)
    if not re.search(r"\\section\[", t):
        probs.append("首行缺 \\section[短名]{标题}")
    return probs


def check_refs(n):
    f = texfile(n)
    if f is None:
        return []
    t = f.read_text(encoding="utf-8")
    body = re.sub(r"\\yizhu\{.*?\}\{.*?\}", "", t, flags=re.S)
    probs = []
    for m in REF.finditer(body):
        kind = CN[m.group(1)]
        lec, num = int(m.group(2)), int(m.group(3))
        if lec > 31:
            continue
        seq = env_seq(lec)
        if not seq:
            continue
        if num > len(seq):
            probs.append("回指「%s」超出第 %d 讲条目数 %d" % (m.group(0), lec, len(seq)))
        elif seq[num - 1] != kind:
            probs.append("回指「%s」但第 %d 讲第 %d 条是 %s" % (m.group(0), lec, num, seq[num - 1]))
    return probs


def main():
    nums = [int(a) for a in sys.argv[1:]] or list(range(1, 32))
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
