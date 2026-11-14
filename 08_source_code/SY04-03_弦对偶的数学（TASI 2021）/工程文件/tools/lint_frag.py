#!/usr/bin/env python
"""Static checks for a translated LaTeX fragment (SPEC section 9).

Usage:
  python lint_frag.py path/to/section.tex [--expect-tags "2.1-2.7"] [-v]

Exit code 0 iff no errors. Warnings do not fail the run.
"""
import argparse
import re
import sys

ERR, WARN = [], []

TAG_RE = re.compile(r"^(?:\d+\.\d+|[ABC]\.\d+)$")


def err(msg, line=None):
    ERR.append(f"ERROR line {line}: {msg}" if line else f"ERROR: {msg}")


def warn(msg, line=None):
    WARN.append(f"WARN  line {line}: {msg}" if line else f"WARN: {msg}")


def strip_comments(text):
    out = []
    for ln in text.splitlines():
        m = re.search(r"(?<!\\)%", ln)
        out.append(ln[:m.start()] if m else ln)
    return "\n".join(out)


def expand_range(spec):
    """'2.1-2.7' -> ['2.1',...,'2.7']; 'A.1-A.9' works too."""
    spec = spec.strip()
    if not spec:
        return []
    if "-" not in spec:
        return [spec]
    a, b = spec.split("-", 1)
    pa, na = a.split(".")
    pb, nb = b.split(".")
    pa = pa or ""
    if pa != pb:
        return [spec]  # cross-prefix ranges (e.g. B.26-C.16) unsupported
    return [f"{pa}.{i}" for i in range(int(na), int(nb) + 1)]


def check(code, text, expect):
    lines = code.splitlines()

    for i, ln in enumerate(lines, 1):
        if re.search(r"\\documentclass", ln):
            err("fragment must not contain \\documentclass", i)
        if re.search(r"\\begin\{document\}", ln):
            err("fragment must not contain \\begin{document}", i)
        if re.search(r"\\input\{", ln) or re.search(r"\\include\{", ln):
            err("fragment must not \\input/\\include other files", i)
        if re.search(r"\\newcommand|\\def\\", ln):
            warn("custom macro definition is discouraged (SPEC 11)", i)

    # brace balance
    depth = 0
    for i, ln in enumerate(lines, 1):
        for ch in re.sub(r"\\[{}]", "", ln):
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
            if depth < 0:
                err("unbalanced closing brace", i)
                depth = 0
    if depth != 0:
        err(f"unbalanced braces at EOF (depth {depth})")

    # environments
    stack = []
    for i, ln in enumerate(lines, 1):
        for m in re.finditer(r"\\begin\{([A-Za-z*]+)\}", ln):
            stack.append((m.group(1), i))
        for m in re.finditer(r"\\end\{([A-Za-z*]+)\}", ln):
            name = m.group(1)
            if not stack:
                err(f"\\end{{{name}}} without matching \\begin", i)
            elif stack[-1][0] != name:
                err(f"\\end{{{name}}} closes \\begin{{{stack[-1][0]}}} (line {stack[-1][1]})", i)
                stack.pop()
            else:
                stack.pop()
    for name, i in stack:
        err(f"unclosed \\begin{{{name}}}", i)

    # dollar balance
    for i, ln in enumerate(lines, 1):
        s = re.sub(r"\\\$", "", ln)
        s = re.sub(r"\\\[|\\\]", "", s)
        if s.count("$") % 2:
            warn("odd number of $ on line (may span lines, verify)", i)

    # tags
    tags = re.findall(r"\\tag\{([^}]*)\}", code)
    seen = {}
    for t, ln_no in zip(tags, [i for i, ln in enumerate(lines, 1) if "\\tag{" in ln]):
        t = t.strip()
        if not TAG_RE.match(t):
            err(f"tag format must be 2.1 / A.1 / B.12 / C.9, got {t!r}", ln_no)
        if t in seen:
            err(f"duplicate tag ({t}) also at line {seen[t]}", ln_no)
        seen[t] = ln_no
    for i, ln in enumerate(lines, 1):
        if "\\tag{" in ln:
            window = "\n".join(lines[max(0, i - 3):i + 1])
            if "\\begin{equation" not in window and "\\begin{align" not in window:
                warn("\\tag outside equation/align (should be inside equation env)", i)

    if expect:
        want = []
        for piece in expect.split(","):
            want += expand_range(piece)
        got = [t.strip() for t in tags]
        missing = [t for t in want if t not in got]
        extra = [t for t in got if t not in want]
        if missing:
            err(f"missing equation tags: {missing}")
        if extra:
            err(f"unexpected equation tags: {extra}")

    # Unicode math / typography symbols in code
    bad = ("αβγδεζηθικλμνξπρστυφχψωΓΔΘΛΞΠΣΥΦΨΩ∑∏∫√∞≤≥≠≈∼→←↔⇒⇔∂∇±×÷·∈∉⊂⊃∪∩⊗⊕⟨⟩†‡"
           "≃≅≡⊆⊇∅ℝℂℤℍℓħ")
    for i, ln in enumerate(lines, 1):
        code_part = ln.split("%")[0]
        for ch in code_part:
            if ch in bad:
                err(f"Unicode math/typographic symbol {ch!r} must be replaced by LaTeX", i)
                break

    # Chinese inside math
    for i, ln in enumerate(lines, 1):
        s = ln.split("%")[0]
        s = re.sub(r"\\text\{[^}]*\}|\\mbox\{[^}]*\}", "", s)
        for m in re.finditer(r"\$([^$]*)\$", s):
            if any("\u4e00" <= ch <= "\u9fff" for ch in m.group(1)):
                err("Chinese characters inside math mode (use \\text{...})", i)
                break

    # literal refs
    for i, ln in enumerate(lines, 1):
        if re.search(r"\\(eq)?ref\{|\\cite\{", ln):
            warn("use literal numbers (SPEC 5.8), not \\ref/\\cite", i)

    # leftover English prose (skip display-math blocks and alignment lines)
    math_envs = {"equation", "equation*", "align", "align*", "gather", "gather*",
                 "multline", "multline*", "eqnarray", "eqnarray*", "aligned",
                 "cases", "split", "array", "matrix", "pmatrix", "bmatrix"}
    in_math = 0
    math_line = [False] * (len(lines) + 1)
    for i, ln in enumerate(lines, 1):
        if "\\[" in ln:
            in_math += 1
        for m in re.finditer(r"\\begin\{([A-Za-z*]+)\}", ln):
            if m.group(1) in math_envs:
                in_math += 1
        math_line[i] = in_math > 0
        if "\\]" in ln and in_math > 0:
            in_math -= 1
        for m in re.finditer(r"\\end\{([A-Za-z*]+)\}", ln):
            if m.group(1) in math_envs and in_math > 0:
                in_math -= 1
    for i, ln in enumerate(lines, 1):
        if math_line[i]:
            continue
        s = ln.split("%")[0].strip()
        if not s or s.startswith("\\") or s.startswith("&") or "$" in s:
            continue
        letters = [c for c in s if c.isalpha()]
        if not letters:
            continue
        ascii_share = sum(c.isascii() for c in letters) / len(letters)
        words = re.findall(r"[A-Za-z][A-Za-z'\-]+", s)
        if ascii_share > 0.8 and len(words) >= 6 and not all(w[0].isupper() for w in words):
            warn("possible untranslated English prose", i)

    # annotations
    n_tutor = len(re.findall(r"%\s*\[Tutor Note", text))
    n_typo = len(re.findall(r"%\s*\[原文疑误", text))
    n_susp = len(re.findall(r"%\s*\[存疑", text))
    n_bg = len(re.findall(r"%\s*\[背景补充", text))
    if n_tutor == 0:
        err("no % [Tutor Note: ...] annotations found (SPEC 7)")

    anchors = re.findall(r"%\s*====\s*原文 PDF 第\s*(\d+)\s*页", text)
    if not anchors:
        warn("no page anchor comments found (SPEC 4)")
    return n_tutor, n_typo, n_susp, n_bg, anchors


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--expect-tags", default="")
    ap.add_argument("-v", "--verbose", action="store_true")
    a = ap.parse_args()
    text = open(a.path, encoding="utf-8").read()
    code = strip_comments(text)
    n_tutor, n_typo, n_susp, n_bg, anchors = check(code, text, a.expect_tags)
    for w in WARN:
        print(w)
    for e in ERR:
        print(e)
    print(f"--- {a.path}")
    print(f"tags: {len(re.findall(r'\\tag{', code))}, tutor notes: {n_tutor}, "
          f"typo notes: {n_typo}, doubt notes: {n_susp}, background notes: {n_bg}")
    print(f"page anchors: {sorted(set(int(x) for x in anchors))}")
    print(f"{len(ERR)} error(s), {len(WARN)} warning(s)")
    return 1 if ERR else 0


if __name__ == "__main__":
    sys.exit(main())
