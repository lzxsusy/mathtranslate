# -*- coding: utf-8 -*-
"""由各 chunk 的 `% [Tutor Note: ...]` 注释生成 src/chunks/appendix_notes.tex（译校批注汇集）。
用法: python gen_appendix_notes.py
"""
import io
import os
import re

ROOT = r"<本地路径>"
CH = os.path.join(ROOT, "src", "chunks")
OUT = os.path.join(ROOT, "src", "chunks", "appendix_notes.tex")

GROUPS = [
    (["ch01"], "第 1 章 序章"),
    (["ch02a", "ch02b"], "第 2 章 分析力学"),
    (["ch03"], "第 3 章 G 结构的几何学"),
    (["ch04"], "第 4 章 各种辛流形"),
    (["ch05"], "第 5 章 动量映射与辛商"),
    (["ch06a", "ch06b"], "第 6 章 完全可积系统"),
    (["ch07"], "第 7 章 Hamilton 动力系统"),
    (["ch08"], "第 8 章 环面流形"),
    (["ch09a", "ch09b"], "第 9 章 二维规范理论"),
    (["ch10"], "第 10 章 全纯辛流形"),
    (["afterword"], "后记"),
]

def read(p):
    with io.open(p, encoding="utf-8") as f:
        return f.read().replace("\r\n", "\n")

def flush(items, page, buf):
    """收尾一条批注：去掉末尾的 `]`，空则丢弃。"""
    if not buf:
        return None
    txt = "".join(buf).strip()
    if txt.endswith("]"):
        txt = txt[:-1].strip()
    if txt:
        items.append((page, txt))
    return None


def collect(path):
    """返回 [(页码, 批注正文), ...]

    批注有两种写法：单行 `% [Tutor Note: …… ]`，或多行（每条续行也以 `%` 开头）。
    末尾的 `]` 可能缺（不少译者写成 `% [Tutor Note: ……。` 而不收尾），
    所以遇到第一条非注释行/新的批注/文件末尾时都要 flush，而不是丢弃。
    """
    items = []
    page = ""
    buf = None
    for ln in read(path).split("\n"):
        s = ln.strip()
        m = re.match(r"^%\s*\[原文 p\.(\d+)\]", s)
        if m:
            buf = flush(items, page, buf)
            page = m.group(1)
            continue
        m = re.match(r"^%\s*\[Tutor Note:\s*(.*)$", s)
        if m:
            buf = flush(items, page, buf)
            buf = [m.group(1)]
            if buf[0].rstrip().endswith("]"):
                buf[0] = buf[0].rstrip()[:-1]
                buf = flush(items, page, buf)
            continue
        if buf is not None:
            if s.startswith("%"):
                cont = s.lstrip("%").strip()
                if cont.endswith("]"):
                    buf.append(cont[:-1].strip())
                    buf = flush(items, page, buf)
                else:
                    buf.append(cont)
            else:
                buf = flush(items, page, buf)
    flush(items, page, buf)
    return items

def fix_math(s):
    """把数学模式之外出现的 _ ^ & % # 转义，避免批注里的行内符号破坏排版。"""
    out = []
    inmath = False
    i = 0
    while i < len(s):
        ch = s[i]
        if ch == "\\" and i + 1 < len(s):
            out.append(s[i:i + 2])
            i += 2
            continue
        if ch == "$":
            inmath = not inmath
            out.append(ch)
        elif not inmath and ch in "_^&#%":
            out.append("\\" + ch)
        else:
            out.append(ch)
        i += 1
    return "".join(out)

out = []
out.append("% 自动生成：work/gen_appendix_notes.py —— 由各 chunk 的 % [Tutor Note: ...] 汇集，勿手工编辑")
out.append("\\chapter*{附录 A\\quad 译校批注}")
out.append("\\addcontentsline{toc}{chapter}{附录 A\\quad 译校批注}")
out.append("\\markboth{附录 A\\quad 译校批注}{附录 A\\quad 译校批注}")
out.append("")
out.append("本附录按章汇集正文中的译校批注，便于读者把批注与原文对照阅读。"
           "批注分三类，均在条目开头标明：\\textbf{背景}给出原文未及展开的史实、人物与文献线索；"
           "\\textbf{难点}说明推导中省略的中间步骤、约定与可能的误区；"
           "\\textbf{校勘}记录与原文（或与通行文献）不一致之处及本译本的处理。"
           "批注编号中的\\textbf{原书 p.$N$}表示该批注对应的日文原书页码（原书页码 $=$ PDF 页码 $-\\,9$）。<本地路径>")
out.append("")

secno = 0
total = 0
for chunks, title in GROUPS:
    items = []
    for c in chunks:
        p = os.path.join(CH, c + ".tex")
        if os.path.exists(p):
            items += collect(p)
    if not items:
        continue
    secno += 1
    total += len(items)
    out.append("\\section*{A.%d %s}" % (secno, title))
    out.append("\\addcontentsline{toc}{section}{A.%d %s}" % (secno, title))
    out.append("\\begin{itemize}[leftmargin=2.4em,itemsep=4pt,label={\\textbullet}]")
    for page, txt in items:
        txt = fix_math(txt.replace("\n", " "))
        if txt.count("$") % 2:          # 定界符落单：补一个 `$` 兜底，避免整章排版崩坏
            print("WARN odd $ :", txt[:60])
            txt += "$"
        tag = ("原书 p.%s" % page) if page else "原书"
        out.append("\\item \\textbf{%s} %s" % (tag, txt))
    out.append("\\end{itemize}")
    out.append("")

body = "\n".join(out)
with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write(body)
print("sections:", secno, "notes:", total, "->", OUT)

