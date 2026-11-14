#!/usr/bin/env python
"""Book-level fidelity checks over witten9301042-zh/sections/*.tex.

Checks
  1. equation tags: per section prefix, must be exactly 1..N with no gaps/dups
     (Witten numbers displayed equations contiguously within each section)
  2. page anchors: coverage of pages 2..92, reporting gaps
  3. mandatory \\section / \\subsection presence
  4. forbidden constructs (documentclass, begin{document}, unicode math)
  5. note counts

Usage: python tools/check_book.py [-v]
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECT = os.path.join(ROOT, "sections")

EXPECTED = {
    "s01-intro.tex": ["\\section"],
    "s02a-fieldtheory.tex": ["\\section"],
    "s02b-fieldtheory.tex": [],
    "s03a-model.tex": ["\\section", "\\subsection"],
    "s03b-singularity.tex": ["\\subsection"],
    "s03c-applications.tex": ["\\subsection"],
    "s03d-twisted.tex": ["\\subsection"],
    "s04-geometry.tex": ["\\section"],
    "s05a-wps-toric.tex": ["\\section", "\\subsection"],
    "s05b-grassmann-intersect.tex": ["\\subsection"],
    "s05c-topology.tex": ["\\subsection"],
    "s06a-superfields.tex": ["\\section", "\\subsection"],
    "s06b-models.tex": ["\\subsection"],
    "s07-references.tex": ["thebibliography"],
}

UNICODE_MATH = "αβγδεζηθικλμνξπρστυφχψωΓΔΘΛΞΠΣΥΦΨΩ∑∏∫√∞≤≥≠≈→←↔⇒⇔∂∇±×÷·∈∉⊂⊃∪∩⊗⊕"

errors, warns = [], []


def main():
    files = sorted(glob.glob(os.path.join(SECT, "*.tex")))
    if not files:
        print("no section files yet")
        return 1
    all_text = {}
    tags_by_prefix = {}
    anchors = set()
    for path in files:
        name = os.path.basename(path)
        raw = open(path, encoding="utf-8").read()
        all_text[name] = raw
        for m in re.finditer(r"\\tag\{([^}]*)\}", raw):
            t = m.group(1).strip()
            mm = re.fullmatch(r"(\d+)\.(\d+)", t)
            if not mm:
                errors.append(f"{name}: bad tag format {t!r}")
                continue
            tags_by_prefix.setdefault(mm.group(1), []).append((int(mm.group(2)), t, name))
        for m in re.finditer(r"原文 PDF 第\s*(\d+)\s*页", raw):
            anchors.add(int(m.group(1)))
        for pat in ("\\documentclass", "\\begin{document}"):
            if pat in raw:
                errors.append(f"{name}: forbidden {pat}")
        # unicode math symbols are forbidden in code; in %-comments they are
        # tolerated (they are human-readable annotations) but reported once.
        code_lines = []
        for ln in raw.splitlines():
            m = re.search(r"(?<!\\)%", ln)
            code_lines.append(ln[:m.start()] if m else ln)
        for ch in "\n".join(code_lines):
            if ch in UNICODE_MATH:
                errors.append(f"{name}: unicode math char {ch!r} in code")
                break
        for need in EXPECTED.get(name, []):
            if need not in raw:
                errors.append(f"{name}: missing {need}")

    # missing files
    for name in EXPECTED:
        if name not in all_text:
            warns.append(f"missing fragment: {name}")

    # tags contiguity
    total_eq = 0
    for prefix in sorted(tags_by_prefix, key=int):
        items = sorted(tags_by_prefix[prefix])
        total_eq += len(items)
        nums = [n for n, _, _ in items]
        dup = sorted({x for x in nums if nums.count(x) > 1})
        if dup:
            errors.append(f"section {prefix}: duplicate tags {dup}")
        missing = [n for n in range(1, max(nums) + 1) if n not in nums]
        if missing:
            errors.append(f"section {prefix}: missing tags {missing} "
                          f"(have {len(nums)} eqs, max {max(nums)})")

    pages_missing = [p for p in range(2, 93) if p not in anchors]
    if pages_missing:
        warns.append(f"page anchors missing: {pages_missing}")

    n_tutor = len(re.findall(r"%\s*\[Tutor Note", "".join(all_text.values())))
    n_typo = len(re.findall(r"%\s*\[原文疑误", "".join(all_text.values())))
    n_doubt = len(re.findall(r"%\s*\[存疑", "".join(all_text.values())))

    print(f"fragments: {len(files)}/14   equations tagged: {total_eq}   "
          f"tutor notes: {n_tutor}   typo notes: {n_typo}   doubt notes: {n_doubt}")
    print(f"pages covered: {len(anchors)}/91  (2..92)")
    for p in sorted(tags_by_prefix, key=int):
        items = sorted(tags_by_prefix[p])
        print(f"  section {p}: {len(items)} eqs, tags {p}.{items[0][0]} .. {p}.{items[-1][0]}")
    for w in warns:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    print(f"{len(errors)} error(s), {len(warns)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
