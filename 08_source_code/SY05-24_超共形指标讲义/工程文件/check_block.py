r"""check_block.py — SY05-24 单块静态自检（交稿前必须跑到 OK）

用法（在 工程文件\ 目录下）： python check_block.py sec2a.tex
检查：1) \tag 集合与分块任务一致   2) 编号习题（exercise）与原文一致
      3) 花括号 / begin-end 配对     4) $ 成对
      5) 禁用命令（\section/…，refs.tex 例外）
      6) UTF-8 无 BOM + 无 CRLF      7) 正文里的非 ASCII 数学符号
      8) 页标记 % [原文 p.N] 覆盖（仅警告）
      9) 表格任务：sec2a/sec2b 应各含一张 tabular（仅警告）
"""
import sys, os, re
from collections import Counter

ROOT = os.path.dirname(os.path.abspath(__file__))

# 页标记与分块：页码 = PDF 页序（1–32）；印刷页码 = PDF 页 − 1
BLOCK_PAGES = {
    "abstract.tex": (1, 1),
    "sec0.tex":     (2, 2),
    "sec1a.tex":    (3, 5),
    "sec1b.tex":    (6, 7),
    "sec2a.tex":    (8, 12),
    "sec2b.tex":    (13, 18),
    "sec3a.tex":    (19, 22),
    "sec3b.tex":    (23, 25),
    "sec4.tex":     (26, 30),
    "refs.tex":     (31, 32),
}

def rng(a, b):
    return ["%d.%d" % (a, i) for i in range(1, b + 1)]

BLOCK_TAGS = {
    "abstract.tex": [],
    "sec0.tex":     [],
    "sec1a.tex":    rng(1, 17),
    "sec1b.tex":    rng(1, 30)[17:],          # (1.18)–(1.30)
    "sec2a.tex":    rng(2, 16),               # (2.1)–(2.16)
    "sec2b.tex":    rng(2, 29)[16:],          # (2.17)–(2.29)
    "sec3a.tex":    rng(3, 19),               # (3.1)–(3.19)
    "sec3b.tex":    rng(3, 35)[19:],          # (3.20)–(3.35)
    "sec4.tex":     rng(4, 16),               # (4.1)–(4.16)
    "refs.tex":     [],
}

# 编号习题（原文节内编号）：file -> [(编号)]
BLOCK_ENVS = {
    "abstract.tex": [], "sec0.tex": [], "sec1a.tex": [],
    "sec1b.tex":    ["1.1"],
    "sec2a.tex":    ["1.2", "2.1"],
    "sec2b.tex":    ["2.2", "2.3"],
    "sec3a.tex":    ["3.1", "3.2"],
    "sec3b.tex":    [],
    "sec4.tex":     ["4.1"],
    "refs.tex":     [],
}

ENV_ALL = "exercise|definition|example|theorem|proposition|lemma|corollary|remark|solution"

FORBIDDEN = [
    r"\documentclass", r"\usepackage", r"\begin{document}", r"\end{document}",
    r"\newcommand", r"\renewcommand", r"\providecommand", r"\DeclareMathOperator",
    r"\input", r"\include", r"\includegraphics", r"\tableofcontents",
    r"\maketitle", r"\newtheorem", r"\def", r"\section",
]
MATH_UNI = set("αβγδεζηθικλμνξπρστυφχψωΓΔΘΛΞΠΣΦΨΩ≤≥≠→←↔∞∑∏∫∂∇±×÷⋅∘≅≃≈≡⊂⊃∈∉∪∩∅"
              "ℳℋℱℒ𝒪ℂℤℚℝℕℙħℏℓ")


def strip_comments(s):
    out = []
    for line in s.splitlines():
        i, cut = 0, None
        while i < len(line):
            if line[i] == "\\":
                i += 2; continue
            if line[i] == "%":
                cut = i; break
            i += 1
        out.append(line if cut is None else line[:cut])
    return "\n".join(out)


def key(n):
    a, b = n.split(".")
    return (int(a), int(b))


def main():
    name = sys.argv[1] if len(sys.argv) > 1 else ""
    base = os.path.basename(name)
    if base not in BLOCK_PAGES:
        print("unknown block file:", base, "| known:", ", ".join(BLOCK_PAGES)); sys.exit(2)
    path = name if os.path.isabs(name) else os.path.join(ROOT, "..", "源码", base)
    raw = open(path, "rb").read()
    problems, warns = [], []

    if raw.startswith(b"\xef\xbb\xbf"):
        problems.append("BOM: 文件带 UTF-8 BOM")
    if b"\r\n" in raw:
        problems.append("CRLF: 存在 Windows 换行")
    s = raw.decode("utf-8", "replace")
    body = strip_comments(s)

    # 1) \tag
    exp = BLOCK_TAGS[base]
    got = [t.strip() for t in re.findall(r"<本地路径>]*)\}", body)]
    cg, ce = Counter(got), Counter(exp)
    miss = [t for t in exp if cg[t] < ce[t]]
    extra = [t for t in cg if t not in ce]
    dup = sorted([t for t, c in cg.items() if c > 1])
    if miss: problems.append("MISSING tag: %s" % miss)
    if extra: problems.append("EXTRA tag: %s" % extra)
    if dup: problems.append("DUPLICATE tag: %s" % dup)
    order_ok = [t for t in got if t in ce] == sorted([t for t in got if t in ce], key=key) if got else True
    if not order_ok: problems.append("tag 顺序与原文不符：%s" % got)

    # 2) 编号习题
    gotenv = [m.group(1) for m in re.finditer(r"<本地路径>?:" + ENV_ALL + r")\}\[([0-9]+\.[0-9]+)", body)]
    cge, cee = Counter(gotenv), Counter(BLOCK_ENVS[base])
    e_miss = [k for k in cee if cge[k] < cee[k]]
    e_extra = [k for k in cge if k not in cee]
    if e_miss: problems.append("MISSING env: %s" % e_miss)
    if e_extra: problems.append("EXTRA env: %s" % e_extra)

    # 3) 花括号
    depth, bad = 0, False
    for ch in body:
        if ch == "{": depth += 1
        elif ch == "}":
            depth -= 1
            if depth < 0: bad = True; break
    if depth != 0 or bad: problems.append("BRACES 不平衡（depth=%d）" % depth)

    # 4) begin/end 配对与嵌套
    b = re.findall(r"<本地路径>]*)\}", body)
    e = re.findall(r"<本地路径>]*)\}", body)
    if Counter(b) != Counter(e):
        problems.append("ENV 不配对: begin-extra=%s end-extra=%s" % (
            dict(Counter(b) - Counter(e)), dict(Counter(e) - Counter(b))))
    stack = []
    for m in re.finditer(r"\\(begin|end)\{([^}]*)\}", body):
        if m.group(1) == "begin":
            stack.append(m.group(2))
        else:
            if not stack or stack[-1] != m.group(2):
                problems.append("ENV 嵌套错误：位置 %d \\end{%s}" % (m.start(), m.group(2))); break
            stack.pop()

    # 5) $ 成对
    nd = len(re.findall(r"(?<!\\)\$", body))
    if nd % 2: problems.append("DOLLAR: 未转义 $ 数量为奇数 (%d)" % nd)

    # 6) 禁用命令（refs.tex 允许 \section*）
    forb = list(FORBIDDEN)
    if base == "refs.tex":
        forb = [f for f in forb if f != r"\section"]
    for cmd in forb:
        if re.search(re.escape(cmd), body):
            problems.append("FORBIDDEN: 出现 %s" % cmd)

    # 7) markdown 粗体 / 非 ASCII 数学
    if re.search(r"\*\*[^*\n]+\*\*", body):
        problems.append("MARKDOWN: 出现 **粗体**")
    uni = sorted(set(ch for ch in body if ch in MATH_UNI))
    if uni: problems.append("UNICODE MATH: 正文出现非 ASCII 数学符号 %s" % "".join(uni))

    # 8) 页标记（警告）
    lo, hi = BLOCK_PAGES[base]
    pages = set(int(x) for x in re.findall(r"%\s*\[原文 p\.(\d+)\]", s))
    missing = [p for p in range(lo, hi + 1) if p not in pages]
    if missing and base not in ("refs.tex",):
        warns.append("缺少页标记: %s" % missing)

    # 9) 表格（警告）
    if base in ("sec2a.tex", "sec2b.tex"):
        if "tabular" not in body:
            warns.append("本块应有一张 tabular（原文 Table 1/2）")

    if problems:
        print("FAIL %s  (tags %d/%d, env %d/%d)" % (base, len(got), len(exp), len(gotenv), len(BLOCK_ENVS[base])))
        for p in problems: print("  -", p)
        for w in warns: print("  ! ", w)
        sys.exit(1)
    print("OK %s  | tags %d/%d | env %d/%d | 批注 %d 条 | 行数 %d" % (
        base, len(got), len(exp), len(gotenv), len(BLOCK_ENVS[base]),
        s.count("[Tutor Note:"), s.count("\n") + 1))
    for w in warns: print("  ! ", w)


if __name__ == "__main__":
    main()
