# -*- coding: utf-8 -*-
"""check_block.py — 单块静态自检（队友交稿前必须跑到 OK）

用法：  python check_block.py sec21.tex
检查：1) \\tag 集合与任务书一致  2) 花括号平衡  3) begin/end 配对
      4) $ 偶数  5) 禁用命令  6) UTF-8 无 BOM + 无 CRLF  7) 正文里的非 ASCII 数学符号
"""
import sys, os, re, io

ROOT = r"<本地路径>"

# 块 -> 该块负责的 PDF 页区间（tags.txt 依据）
BLOCK_PAGES = {
    "sec1.tex":   (2, 3),
    "sec21.tex":  (4, 9),
    "sec22.tex":  (10, 15),
    "sec23a.tex": (16, 20),
    "sec23b.tex": (21, 26),
    "sec31.tex":  (27, 30),
    "sec32.tex":  (31, 34),
    "sec33.tex":  (35, 37),
    "sec4.tex":   (38, 42),
    "refs.tex":   (43, 46),
}

FORBIDDEN = [
    r"\documentclass", r"\usepackage", r"\begin{document}", r"\end{document}",
    r"\newcommand", r"\renewcommand", r"\providecommand", r"\DeclareMathOperator",
    r"\input", r"\include", r"\includegraphics", r"\tableofcontents",
    r"\maketitle", r"\newtheorem", r"\def",
]

MATH_UNI = set("αβγδεζηθικλμνξπρστυφχψωΓΔΘΛΞΠΣΦΨΩ≤≥≠→←↔∞∑∏∫∂∇±×÷⋅∘≅≃≈≡⊂⊃∈∉∪∩∅"
              "ℳℋℱℒ𝒪ℂℤℚℝℕℙħℏℓ")

def expected_tags(pages):
    lo, hi = pages
    exp = []
    for line in open(os.path.join(ROOT, "tags.txt"), encoding="utf-8"):
        p, tg = line.strip().split("\t")
        pno = int(p[1:])
        if lo <= pno <= hi:
            exp.append(tg)
    return exp

def strip_comments(s):
    out = []
    for line in s.splitlines():
        # remove from first unescaped %
        i = 0
        cut = None
        while i < len(line):
            if line[i] == "\\":
                i += 2
                continue
            if line[i] == "%":
                cut = i
                break
            i += 1
        out.append(line if cut is None else line[:cut])
    return "\n".join(out)

def main():
    name = sys.argv[1] if len(sys.argv) > 1 else ""
    base = os.path.basename(name)
    if base not in BLOCK_PAGES:
        print("unknown block file:", base, "| known:", ", ".join(BLOCK_PAGES)); sys.exit(2)
    path = name if os.path.isabs(name) else os.path.join(ROOT, "src", base)
    raw = open(path, "rb").read()

    problems = []
    if raw.startswith(b"\xef\xbb\xbf"):
        problems.append("BOM: 文件带 UTF-8 BOM（用 Python encoding='utf-8' 重写）")
    if b"\r\n" in raw:
        problems.append("CRLF: 存在 Windows 换行（用 newline='\\n' 重写）")
    s = raw.decode("utf-8", "replace")
    body = strip_comments(s)

    # 1) tags
    exp = expected_tags(BLOCK_PAGES[base])
    got = re.findall(r"<本地路径>]*)\}", body)
    from collections import Counter
    cg, ce = Counter(got), Counter(exp)
    miss = sorted([t for t in ce if cg[t] < ce[t]], key=lambda x: (int(x.split('.')[0]), int(x.split('.')[1])))
    extra = sorted([t for t in cg if t not in ce], key=lambda x: (int(x.split('.')[0]), int(x.split('.')[1])))
    dup = sorted([t for t in cg if cg[t] > 1])
    if miss: problems.append("MISSING tag: %s" % miss)
    if extra: problems.append("EXTRA tag: %s" % extra)
    if dup: problems.append("DUPLICATE tag: %s" % dup)

    # 2) braces
    depth = 0
    bad_at = None
    for i, ch in enumerate(body):
        if ch == "{": depth += 1
        elif ch == "}":
            depth -= 1
            if depth < 0:
                bad_at = i; break
    if depth != 0 or bad_at is not None:
        problems.append("BRACES 不平衡（depth=%d）" % depth)

    # 3) begin/end
    b = re.findall(r"<本地路径>]*)\}", body)
    e = re.findall(r"<本地路径>]*)\}", body)
    if Counter(b) != Counter(e):
        problems.append("ENV 不配对: begin=%s end=%s" % (dict(Counter(b) - Counter(e)), dict(Counter(e) - Counter(b))))
    # nesting order
    stack = []
    for m in re.finditer(r"\\(begin|end)\{([^}]*)\}", body):
        if m.group(1) == "begin":
            stack.append(m.group(2))
        else:
            if not stack or stack[-1] != m.group(2):
                problems.append("ENV 嵌套错误：在 %s 处遇到 \\end{%s}" % (m.start(), m.group(2)))
                break
            stack.pop()

    # 4) $ 偶数
    nd = len(re.findall(r"(?<!\\)\$", body))
    if nd % 2:
        problems.append("DOLLAR: 未转义 $ 数量为奇数 (%d)" % nd)

    # 5) forbidden
    for cmd in FORBIDDEN:
        if re.search(re.escape(cmd), body):
            problems.append("FORBIDDEN: 出现了 %s" % cmd)

    # 6) markdown bold
    if re.search(r"\*\*[^*\n]+\*\*", body):
        problems.append("MARKDOWN: 出现 **粗体**（会被原样印出星号）")

    # 7) 非 ASCII 数学符号（在正文里）
    uni = sorted(set(ch for ch in body if ch in MATH_UNI))
    if uni:
        problems.append("UNICODE MATH: 正文里出现非 ASCII 数学符号 %s（改用 LaTeX 命令）" % "".join(uni))

    # 8) 每页标注
    pages = set(int(x) for x in re.findall(r"%\s*\[原文 p\.(\d+)\]", s))
    if BLOCK_PAGES[base] != (43, 46) and BLOCK_PAGES[base][0] != 2:
        pass

    ntag = len(got)
    if problems:
        print("FAIL %s  (tags %d/%d)" % (base, ntag, len(exp)))
        for p in problems:
            print("  -", p)
        sys.exit(1)
    print("OK %s  | tags %d/%d | 批注 %d 条 | 行数 %d" % (
        base, ntag, len(exp), s.count("[Tutor Note:"), s.count("\n") + 1))

if __name__ == "__main__":
    main()
