#!/usr/bin/env python
"""Static checks for a translated LaTeX fragment (SPEC section 8).

Usage:
  python lint_frag.py path/to/section.tex [-v]

Exit code 0 iff no errors. Warnings are printed but do not fail the run.
"""
import argparse
import re
import sys
import unicodedata

ERR, WARN = [], []


def err(msg, line=None):
    ERR.append(f"ERROR line {line}: {msg}" if line else f"ERROR: {msg}")


def warn(msg, line=None):
    WARN.append(f"WARN  line {line}: {msg}" if line else f"WARN: {msg}")


def strip_comments(text):
    """Return text with %-comments removed (not escaping \\%)."""
    out = []
    for ln in text.splitlines():
        m = re.search(r"(?<!\\)%", ln)
        out.append(ln[:m.start()] if m else ln)
    return "\n".join(out)


def check(code, text):
    lines = code.splitlines()

    for i, ln in enumerate(lines, 1):
        if re.search(r"\\documentclass", ln):
            err("fragment must not contain \\documentclass", i)
        if re.search(r"\\begin\{document\}", ln):
            err("fragment must not contain \\begin{document}", i)
        if re.search(r"\\input\{", ln) or re.search(r"\\include\{", ln):
            err("fragment must not \\input/\\include other files", i)
        if re.search(r"\\newcommand|\\def\\", ln):
            warn("custom macro definition is discouraged (SPEC 10)", i)

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

    # dollar balance (display \[..\] handled separately)
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
        if not re.fullmatch(r"\d+\.\d+", t):
            err(f"tag format must be N.M, got {t!r}", ln_no)
        if t in seen:
            err(f"duplicate tag ({t}) also at line {seen[t]}", ln_no)
        seen[t] = ln_no
    for i, ln in enumerate(lines, 1):
        if "\\tag{" in ln:
            window = "\n".join(lines[max(0, i - 3):i + 1])
            if "\\begin{equation" not in window and "\\begin{align" not in window:
                warn("\\tag outside equation/align (should be inside equation env)", i)

    # Unicode math symbols
    bad = "αβγδεζηθικλμνξπρστυφχψωΓΔΘΛΞΠΣΥΦΨΩ∑∏∫√∞≤≥≠≈∼→←↔⇒⇔∂∇±×÷·∈∉⊂⊃∪∩⊗⊕⟨⟩†‡"
    for i, ln in enumerate(lines, 1):
        code_part = ln.split("%")[0]
        for ch in code_part:
            if ch in bad:
                err(f"Unicode math/typographic symbol {ch!r} must be replaced by LaTeX", i)
                break
        if any("\u4e00" <= ch <= "\u9fff" for ch in code_part):
            # Chinese outside comments: acceptable only in bare text, not math
            pass

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
            warn("use literal numbers (SPEC 4.8), not \\ref/\\cite", i)

    # leftover English prose (rough heuristic)
    for i, ln in enumerate(lines, 1):
        s = ln.split("%")[0].strip()
        if not s or s.startswith("\\") or "$" in s:
            continue
        letters = [c for c in s if c.isalpha()]
        if not letters:
            continue
        ascii_share = sum(c.isascii() for c in letters) / len(letters)
        words = re.findall(r"[A-Za-z][A-Za-z'\-]+", s)
        if ascii_share > 0.8 and len(words) >= 6 and not all(w[0].isupper() for w in words):
            warn("possible untranslated English prose", i)

    # notes: comments were stripped from `code`, so count on the raw `text`
    n_tutor = len(re.findall(r"%\s*\[Tutor Note", text))
    n_typo = len(re.findall(r"%\s*\[原文疑误", text))
    n_susp = len(re.findall(r"%\s*\[存疑", text))
    has_tutor = n_tutor > 0
    if not has_tutor:
        err("no % [Tutor Note: ...] annotations found (SPEC 6)")

    # page anchors (also comments -> count on raw text)
    anchors = re.findall(r"%\s*====\s*原文 PDF 第\s*(\d+)\s*页", text)
    if not anchors:
        warn("no page anchor comments found (SPEC 3)")
    return n_tutor, n_typo, n_susp, anchors


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("-v", "--verbose", action="store_true")
    a = ap.parse_args()
    text = open(a.path, encoding="utf-8").read()
    code = strip_comments(text)
    n_tutor, n_typo, n_susp, anchors = check(code, text)
    for w in WARN:
        print(w)
    for e in ERR:
        print(e)
    print(f"--- {a.path}")
    print(f"tags: {len(re.findall(r'\\tag{', code))}, "
          f"tutor notes: {n_tutor}, typo notes: {n_typo}, doubt notes: {n_susp}")
    print(f"page anchors: {sorted(set(int(x) for x in anchors))}")
    print(f"{len(ERR)} error(s), {len(WARN)} warning(s)")
    return 1 if ERR else 0


if __name__ == "__main__":
    sys.exit(main())
