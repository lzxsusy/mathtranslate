# -*- coding: utf-8 -*-
r"""check_block.py — 单块静态自检（交稿前必须跑到 OK）

用法（在 工程文件\ 目录下）： python check_block.py sec2.tex
检查：1) \\tag 集合与分块任务一致   2) 编号环境（类型+编号）与原文一致
      3) 花括号 / begin-end 配对     4) $ 成对
      5) 禁用命令（\\section/\\usepackage/\\newcommand…）
      6) UTF-8 无 BOM + 无 CRLF      7) 正文里的非 ASCII 数学符号
      8) 页标记 % [原文 p.N] 覆盖（仅警告）
"""
import sys, os, re
from collections import Counter

ROOT = os.path.dirname(os.path.abspath(__file__))

BLOCK_PAGES = {
    "sec1.tex":  (1, 5),
    "sec2.tex":  (6, 13),
    "sec3.tex":  (13, 19),
    "sec4a.tex": (20, 25),
    "sec4b.tex": (25, 30),
    "refs.tex":  (30, 34),
}

BLOCK_TAGS = {
    "sec1.tex":  list(range(1, 6)),
    "sec2.tex":  list(range(6, 21)),
    "sec3.tex":  list(range(21, 39)),
    "sec4a.tex": list(range(39, 51)),
    "sec4b.tex": list(range(51, 57)),
    "refs.tex":  [],
}

D, T, P, C, E, R, CO = "definition", "theorem", "proposition", "corollary", "example", "remark", "conjecture"
H, Q = "hypothesis", "question"
BLOCK_ENVS = {
    "sec1.tex":  [(CO,"1.1"),(R,"1.2"),(E,"1.3"),(E,"1.4"),(D,"1.5"),(R,"1.6"),
                  (E,"1.7"),(E,"1.8"),(D,"1.9"),(D,"1.10"),(CO,"1.11"),(R,"1.12")],
    "sec2.tex":  [(D,"2.1"),(R,"2.2"),(D,"2.3"),(D,"2.4"),(E,"2.5"),(R,"2.6"),(P,"2.7"),
                  (D,"2.8"),(R,"2.9"),(E,"2.10"),(E,"2.11"),(R,"2.12"),(D,"2.13"),(H,"2.14"),
                  (R,"2.15"),(C,"2.16"),(E,"2.17"),(E,"2.18"),(E,"2.19"),(E,"2.20"),
                  (E,"2.21"),(E,"2.22"),(R,"2.23"),(E,"2.24")],
    "sec3.tex":  [(CO,"3.1"),(E,"3.2"),(D,"3.3"),(D,"3.4"),(R,"3.5"),(D,"3.6"),(D,"3.7"),
                  (D,"3.8"),(D,"3.9"),(T,"3.10"),(E,"3.11"),(P,"3.12"),(E,"3.13"),(R,"3.14"),
                  (E,"3.15"),(R,"3.16"),(R,"3.17"),(D,"3.18"),(R,"3.19"),(H,"3.20"),
                  (R,"3.21"),(E,"3.22"),(E,"3.23"),(R,"3.24"),(R,"3.25"),(E,"3.26")],
    "sec4a.tex": [(R,"4.1"),(E,"4.2"),(E,"4.3"),(R,"4.4"),(R,"4.5"),(D,"4.6"),(P,"4.7"),
                  (R,"4.8"),(D,"4.9"),(T,"4.10"),(T,"4.11"),(R,"4.12"),(C,"4.13")],
    "sec4b.tex": [(R,"4.14"),(D,"4.15"),(R,"4.16"),(R,"4.17"),(H,"4.18"),(E,"4.19"),(E,"4.20"),(E,"4.21")],
    "refs.tex":  [],
}

FORBIDDEN = [
    r"\documentclass", r"\usepackage", r"\begin{document}", r"\end{document}",
    r"\newcommand", r"\renewcommand", r"\providecommand", r"\DeclareMathOperator",
    r"\input", r"\include", r"\includegraphics", r"\tableofcontents",
    r"\maketitle", r"\newtheorem", r"\def", r"\section", r"\subsection*{",
]
MATH_UNI = set("αβγδεζηθικλμνξπρστυφχψωΓΔΘΛΞΠΣΦΨΩ≤≥≠→←↔∞∑∏∫∂∇±×÷⋅∘≅≃≈≡⊂⊃∈∉∪∩∅"
              "ℳℋℱℒ𝒪ℂℤℚℝℕℙħℏℓ")
ENV_ALL = "|".join([D, T, P, C, E, R, CO, H, Q, "lemma"])


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
        problems.append("BOM: 文件带 UTF-8 BOM（用 Python encoding='utf-8' 重写）")
    if b"\r\n" in raw:
        problems.append("CRLF: 存在 Windows 换行（用 newline='\\n' 重写）")
    s = raw.decode("utf-8", "replace")
    body = strip_comments(s)

    # 1) 公式号
    exp = [str(x) for x in BLOCK_TAGS[base]]
    got = re.findall(r"<本地路径>]*)\}", body)
    cg, ce = Counter(got), Counter(exp)
    miss = sorted([t for t in ce if cg[t] < ce[t]], key=lambda x: int(x) if x.isdigit() else 0)
    extra = sorted([t for t in cg if t not in ce])
    dup = sorted([t for t in cg if cg[t] > 1])
    if miss: problems.append("MISSING tag: %s" % miss)
    if extra: problems.append("EXTRA tag: %s" % extra)
    if dup: problems.append("DUPLICATE tag: %s" % dup)

    # 2) 编号环境
    gotenv = [(m.group(1), m.group(2)) for m in
              re.finditer(r"<本地路径>" + ENV_ALL + r")\}\[\{?([0-9]+\.[0-9]+)", body)]
    cge, cee = Counter(gotenv), Counter(BLOCK_ENVS[base])
    e_miss = sorted([k2 for k2 in cee if cge[k2] < cee[k2]], key=lambda x: key(x[1]))
    e_extra = sorted([k2 for k2 in cge if k2 not in cee], key=lambda x: key(x[1]))
    if e_miss: problems.append("MISSING env: %s" % e_miss)
    if e_extra: problems.append("EXTRA/错编号 env: %s" % e_extra)
    nums = [n for _, n in gotenv]
    if len(set(nums)) != len(nums):
        problems.append("DUPLICATE env 编号: %s" % sorted([n for n, c in Counter(nums).items() if c > 1]))
    if nums != sorted(nums, key=key):
        problems.append("env 编号非升序：%s" % nums)

    # 3) 花括号
    depth, bad = 0, False
    for ch in body:
        if ch == "{": depth += 1
        elif ch == "}":
            depth -= 1
            if depth < 0: bad = True; break
    if depth != 0 or bad: problems.append("BRACES 不平衡（depth=%d）" % depth)

    # 4) begin/end 配对
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
                problems.append("ENV 嵌套错误：位置 %d 遇到 \\end{%s}" % (m.start(), m.group(2))); break
            stack.pop()

    # 5) $ 成对
    nd = len(re.findall(r"(?<!\\)\$", body))
    if nd % 2: problems.append("DOLLAR: 未转义 $ 数量为奇数 (%d)" % nd)

    # 6) 禁用命令
    forb = list(FORBIDDEN)
    if base == "refs.tex":  # 唯一例外：参考文献标题
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
    if missing and base != "refs.tex":
        warns.append("缺少页标记: %s" % missing)

    notag = len(got)
    if problems:
        print("FAIL %s  (tags %d/%d, env %d/%d)" % (base, notag, len(exp), len(gotenv), len(BLOCK_ENVS[base])))
        for p in problems: print("  -", p)
        for w in warns: print("  ! ", w)
        sys.exit(1)
    print("OK %s  | tags %d/%d | env %d/%d | 批注 %d 条 | 行数 %d" % (
        base, notag, len(exp), len(gotenv), len(BLOCK_ENVS[base]),
        s.count("[Tutor Note:"), s.count("\n") + 1))
    for w in warns: print("  ! ", w)


if __name__ == "__main__":
    main()
