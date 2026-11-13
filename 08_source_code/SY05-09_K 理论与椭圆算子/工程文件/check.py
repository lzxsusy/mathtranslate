#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""EN47 交付前审计：源文件自检 + 整书编译统计。

用法（工程根或任意目录）：
  python check.py

检查项：
  1) 禁用句式、禁用的 LaTeX 写法（\\tag / \\cite / \\begin{transnote} / equation 环境）
  2) 每块小节数、定理环境数、\\transnote 数、展示公式数
  3) 花式引号、半角中文标点残留、连字 ﬁ/ﬀ/ﬂ 残留
  4) 整书编译（两遍 xelatex）后 errors / overfull / undefined / missing char
输出以 VERDICT: PASS / FAIL 结尾。
"""
import os, re, subprocess, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src")
CH = os.path.join(SRC, "chunks")

BANNED = ["被", "进行", "对于", "关于", "使得", "起到了", "有着", "众所周知", "不难发现"]
BANNED_PATTERNS = [
    (r"被[^，。；]{0,20}所", "被……所"),
    (r"进行[^，。；]{0,10}的", "进行……的"),
    (r"对于[^，。；]{0,15}而言", "对于……而言"),
    (r"关于[^，。；]{0,15}的讨论", "关于……的讨论"),
    (r"使得[^，。；]{0,15}得以", "使得……得以"),
    (r"起到了[^，。；]{0,15}的作用", "起到了……的作用"),
    (r"有着[^，。；]{0,15}的意义", "有着……的意义"),
    (r"众所周知", "众所周知"),
    (r"不难发现", "不难发现"),
    (r"值得注意的是", "值得注意的是"),
]
BAD_LATEX = [
    (r"<本地路径>", "equation 环境（原文无编号，应用 \\[...\\]）"),
    (r"<本地路径>", "\\tag（原文无编号）"),
    (r"<本地路径>", "\\cite（原文用字面 [n]）"),
    (r"<本地路径>", "\\begin{transnote}（应用 \\transnote{}）"),
    (r"\\documentclass", "块内出现 \\documentclass"),
]
LIGATURES = {"ﬁ": "fi", "ﬀ": "ff", "ﬂ": "fl", "ﬃ": "ffi", "ﬄ": "ffl"}

fail = 0


def report(ok, msg):
    global fail
    if not ok:
        fail += 1
        print("[FAIL] " + msg)
    else:
        print("[ ok ] " + msg)


def main():
    files = sorted(f for f in os.listdir(CH) if re.match(r"c\d\d\.tex$", f))
    report(bool(files), "找到块文件 %d 个" % len(files))
    total_tn = 0
    for f in files:
        path = os.path.join(CH, f)
        t = open(path, encoding="utf-8").read()
        tn = len(re.findall(r"<本地路径>", t))
        total_tn += tn
        nsec = len(re.findall(r"<本地路径>", t))
        nsub = len(re.findall(r"<本地路径>", t))
        nenv = len(re.findall(r"<本地路径>|theorem|proposition|claim|example|corollary|problem)\}", t))
        ndisp = len(re.findall(r"\\\[", t))
        print("--- %s: section=%d subsection=%d env=%d display=%d transnote=%d (%d 字)"
              % (f, nsec, nsub, nenv, ndisp, tn, len(t)))
        for pat, name in BAD_LATEX:
            if re.search(pat, t):
                report(False, "%s 出现禁用写法：%s" % (f, name))
        for lig, rep in LIGATURES.items():
            if lig in t:
                report(False, "%s 残留连字 %s（应为 %s）" % (f, lig, rep))
        # 半角标点夹在汉字之间
        m = re.search(r"[\u4e00-\u9fff][,;:!?][\u4e00-\u9fff]", t)
        if m:
            report(False, "%s 汉字间用了半角标点：%r" % (f, m.group(0)))
        # 禁用句式（跳过注释行）
        body = "\n".join(l for l in t.splitlines() if not l.lstrip().startswith("%"))
        for pat, name in BANNED_PATTERNS:
            for mm in re.finditer(pat, body):
                s = max(0, mm.start() - 30)
                report(False, "%s 禁用句式「%s」：…%s…" % (f, name, body[s:mm.end() + 20].replace("\n", " ")))
    report(total_tn > 0, "\\transnote 合计 %d 条" % total_tn)

    # 整书编译
    out = os.path.join(ROOT, "work", "check_build")
    os.makedirs(out, exist_ok=True)
    for _ in range(2):
        subprocess.run(["xelatex", "-interaction=nonstopmode",
                        "-output-directory=" + out, "main.tex"],
                       cwd=SRC, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    log = os.path.join(out, "main.log")
    if not os.path.exists(log):
        report(False, "整书编译未产生 log")
    else:
        txt = open(log, encoding="utf-8", errors="replace").read()
        errs = len(re.findall(r"^!", txt, re.M))
        over = len(re.findall(r"^Overfull", txt, re.M))
        und = len(re.findall(r"undefined", txt, re.I))
        mis = len(re.findall(r"Missing character", txt))
        pages = re.search(r"Output written on main\.pdf \((\d+) pages", txt)
        print("整书：pages=%s errors=%d overfull=%d undefined=%d missing_char=%d"
              % (pages.group(1) if pages else "?", errs, over, und, mis))
        report(errs == 0, "errors=0")
        report(over == 0, "overfull=0")
        report(und == 0, "undefined=0")
        report(mis == 0, "missing_char=0")
        if errs:
            m = re.search(r"^!.*(?:\n.*){0,8}", txt, re.M)
            print(m.group(0) if m else "")

    print("\nVERDICT: %s" % ("PASS" if fail == 0 else "FAIL (%d 项)" % fail))


if __name__ == "__main__":
    main()
