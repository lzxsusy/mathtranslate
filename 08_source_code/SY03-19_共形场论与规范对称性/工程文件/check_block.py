# -*- coding: utf-8 -*-
"""单块静态自检。用法: python check_block.py src/b01.tex
检查: BOM / CRLF / 花括号 / 环境配对 / $ 配对 / 禁用命令 / 非 ASCII 数学符号 /
      数学中的中文 / \tag 格式与重复 / Tutor Note 计数 / TODO 计数。
全部通过输出 OK，否则输出 PROBLEM 行并以退出码 1 结束。
"""
import sys, re, os

BANNED = [r"\documentclass", r"\usepackage", r"\newcommand", r"\renewcommand",
          r"\providecommand", r"\DeclareMathOperator", r"\begin{document}",
          r"\end{document}", r"\input", r"\include{", r"\includegraphics",
          r"\tableofcontents", r"\maketitle", r"\section", r"\chapter",
          r"\bibliography", r"\pagestyle", r"\label{", r"\eqref"]

BAD_ASCII_MATH = set("≤≥≠→←↔⇒⇔∞∑∫∏∂∇∈∉⊂⊃⊆⊇∪∩±×÷≈∼≅√∝⊥⟨⟩ℂℝℤℕℙℍ")

def strip_comments(line):
    out, i, n = [], 0, len(line)
    while i < n:
        c = line[i]
        if c == "\\" and i + 1 < n:
            out.append(line[i:i+2]); i += 2; continue
        if c == "%":
            break
        out.append(c); i += 1
    return "".join(out)

def main(path):
    probs = []
    raw = open(path, "rb").read()
    if raw.startswith(b"\xef\xbb\xbf"):
        probs.append("BOM: 文件有 UTF-8 BOM")
        raw = raw[3:]
    if b"\r" in raw:
        probs.append("CRLF: 文件含 CR（需 LF 换行）")
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as e:
        print("PROBLEM 编码: 不是合法 UTF-8: %s" % e); return 1

    lines = text.split("\n")
    body = "\n".join(strip_comments(l) for l in lines)

    # 花括号
    depth = 0; mind = 0
    i = 0
    while i < len(body):
        c = body[i]
        if c == "\\":
            i += 2; continue
        if c == "{": depth += 1
        elif c == "}":
            depth -= 1
            if depth < 0 and mind == 0:
                ln = body[:i].count("\n") + 1
                probs.append("BRACE: 第 %d 行附近出现多余的 }" % ln); mind = 1
        i += 1
    if depth != 0:
        probs.append("BRACE: 花括号不平衡（多出 %d 个 {）" % depth)

    # 环境配对
    stack = []
    for m in re.finditer(r"\\(begin|end)\{([^}]+)\}", body):
        kind, env = m.group(1), m.group(2)
        ln = body[:m.start()].count("\n") + 1
        if kind == "begin":
            stack.append((env, ln))
        else:
            if not stack:
                probs.append("ENV: 第 %d 行 \\end{%s} 没有对应的 \\begin" % (ln, env))
            elif stack[-1][0] != env:
                probs.append("ENV: 第 %d 行 \\end{%s} 与第 %d 行 \\begin{%s} 不匹配"
                             % (ln, env, stack[-1][1], stack[-1][0]))
                stack.pop()
            else:
                stack.pop()
    for env, ln in stack:
        probs.append("ENV: 第 %d 行 \\begin{%s} 未闭合" % (ln, env))

    # $ 配对
    ndollar = 0
    i = 0
    while i < len(body):
        if body[i] == "\\":
            i += 2; continue
        if body[i] == "$":
            ndollar += 1
        i += 1
    if ndollar % 2:
        probs.append("DOLLAR: 全文 $ 个数为奇数（%d）" % ndollar)

    # 禁用命令
    for b in BANNED:
        if b in body:
            cnt = body.count(b)
            probs.append("BANNED: 出现禁用命令 %s（%d 次）" % (b, cnt))

    # 非 ASCII 数学符号（正文/公式里）
    for ln_no, l in enumerate(lines, 1):
        s = strip_comments(l)
        for ch in s:
            if ch in BAD_ASCII_MATH:
                probs.append("UNICODE: 第 %d 行出现 Unicode 数学符号 %r（应写 LaTeX 命令）" % (ln_no, ch))
                break
        if "\ufffd" in s:
            probs.append("UNICODE: 第 %d 行含替换字符 U+FFFD" % ln_no)

    # 数学里出现中文
    for m in re.finditer(r"\$([^$]*)\$", body):
        seg = m.group(1)
        if re.search(r"[\u4e00-\u9fff]", seg) and ("\\mbox" not in seg and "\\text" not in seg):
            ln = body[:m.start()].count("\n") + 1
            probs.append("CJK-IN-MATH: 第 %d 行行内数学里有中文: %s" % (ln, seg[:40]))

    # markdown 粗体
    for ln_no, l in enumerate(lines, 1):
        if "**" in strip_comments(l):
            probs.append("MARKDOWN: 第 %d 行出现 **（用 \\emph/\\textbf）" % ln_no)

    # \tag
    tags = re.findall(r"<本地路径>]*)\}", body)
    seen = {}
    for t in tags:
        # 允许章号是数字或单字母（附录为 A.39 这类）
        if not re.fullmatch(r"(?:\d+|[A-Z])\.\d+", t.strip()):
            probs.append("TAG: \\tag{%s} 格式应为 章.序 或 A.序" % t)
        seen[t] = seen.get(t, 0) + 1
    for t, c in seen.items():
        if c > 1:
            probs.append("TAG: \\tag{%s} 出现 %d 次（重复）" % (t, c))
    # 用 (章, 序) 二元组比较，不能转 float（1.10 会被当成 1.1）
    def key(t):
        a, b = t.strip().split(".")
        return (a if a.isalpha() else int(a), int(b))

    nums = [key(t) for t in tags if re.fullmatch(r"(?:\d+|[A-Z])\.\d+", t.strip())]
    # 按出现顺序，同一章内应递增
    prev = None
    for n in nums:
        if prev is not None and n <= prev:
            probs.append("TAG: 编号顺序异常 %s.%s -> %s.%s（不是递增）"
                         % (prev[0], prev[1], n[0], n[1]))
        prev = n

    notes = len(re.findall(r"%\s*\[Tutor Note", text))
    todos = len(re.findall(r"%\s*\[TODO-LEAD", text))
    figs = len(re.findall(r"\\figomit", body))
    pages = len(re.findall(r"%\s*\[原文 p\.\d+\]", text))

    name = os.path.basename(path)
    print("FILE %s | 行 %d | \\tag %d 条 | 环境 %d | 批注 %d | TODO %d | 图略 %d | 页标 %d"
          % (name, len(lines), len(tags), len(stack) and 0 or len(re.findall(r"<本地路径>", body)),
             notes, todos, figs, pages))
    if tags:
        print("TAGS: %s" % ", ".join(tags))
    if notes < 5:
        probs.append("NOTE: 批注只有 %d 条（要求 8–20 条）" % notes)
    if pages == 0:
        probs.append("PAGE: 没有任何 `% [原文 p.N]` 页标记")
    if probs:
        for p in probs:
            print("PROBLEM " + p)
        return 1
    print("OK")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
