# -*- coding: utf-8 -*-
"""QA checker for the Kapustin-Witten lecture notes.

Checks per section file:
  - the four tcolorbox blocks exist (goals / follow / keybox / checkbox)
  - Chinese character count within the expected range
  - number of \\src{} anchors and \\cite{} keys
  - at least one figure/table per lecture
  - no absolute local paths, no \\usepackage, no new \\newcommand, no Markdown **bold**
Usage:
  python tools/check_lectures.py            # all files, print table
  python tools/check_lectures.py --strict   # exit 1 on error
"""
import io
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEC = ROOT / "sections"

# lecture file -> (min hanzi, max hanzi, expectation label)
EXPECT = {
    "00_guide.tex": (0, 4000, "guide"),
    "01_stage.tex": (1700, 3600, "L1"),
    "02_physics.tex": (1700, 3600, "L2"),
    "03_twist.tex": (1700, 3600, "L3"),
    "04_compact.tex": (1700, 3600, "L4"),
    "05_branes.tex": (1700, 3600, "L5"),
    "06_hecke.tex": (1700, 3600, "L6"),
    "07_dmod.tex": (1700, 3600, "L7"),
    "08_outlook.tex": (1700, 3600, "L8"),
    "90_terms.tex": (0, 20000, "terms"),
    "91_exercises.tex": (0, 20000, "exercises"),
    "92_refs.tex": (0, 20000, "refs"),
}

BOXES = ["goals", "follow", "keybox", "checkbox"]
ABSPATH = re.compile(r"(?:[A-Za-z]:\\+(?:Users|admin|Desktop|dsh|Program|Windows)|C:/Users|/c/Users|file:///)")
CJK = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")


def hanzi(s: str) -> int:
    return len(CJK.findall(s))


def check_file(p: Path, lo: int, hi: int, label: str):
    s = io.open(p, encoding="utf-8").read()
    issues = []
    n = hanzi(s)
    if label.startswith("L") and not (lo <= n <= hi):
        issues.append(f"汉字 {n} 超出 [{lo},{hi}]")
    for b in BOXES:
        if label.startswith("L") and f"\\begin{{{b}}}" not in s:
            issues.append(f"缺少 {b} 盒")
    figs = s.count("\\begin{tikzpicture}") + s.count("\\begin{tikzcd}") + s.count("\\begin{tabular}") + s.count("\\begin{longtable}")
    if label.startswith("L") and figs == 0:
        issues.append("没有图或表")
    if ABSPATH.search(s):
        issues.append("含本机绝对路径")
    if "\\usepackage" in s:
        issues.append("含 \\usepackage")
    if re.search(r"\\newcommand|\\renewcommand", s):
        issues.append("含 \\newcommand")
    if "**" in s:
        issues.append("含 Markdown ** 粗体")
    return dict(file=p.name, label=label, hanzi=n, anchors=s.count("\\src{"),
                cites=len(re.findall(r"\\cite\{", s)), figs=figs, issues=issues)


def main() -> int:
    strict = "--strict" in sys.argv
    rows = []
    for name, (lo, hi, label) in EXPECT.items():
        p = SEC / name
        if not p.exists():
            rows.append(dict(file=name, label=label, hanzi=0, anchors=0, cites=0, figs=0,
                             issues=["文件不存在"]))
            continue
        rows.append(check_file(p, lo, hi, label))

    hdr = f"{'file':18s} {'kind':10s} {'hanzi':>6s} {'src':>4s} {'cite':>4s} {'figs':>4s}  issues"
    print(hdr)
    print("-" * len(hdr))
    total_issues = 0
    for r in rows:
        total_issues += len(r["issues"])
        print(f"{r['file']:18s} {r['label']:10s} {r['hanzi']:6d} {r['anchors']:4d} "
              f"{r['cites']:4d} {r['figs']:4d}  {'; '.join(r['issues'])}")
    print("-" * len(hdr))
    print(f"files={len(rows)} issues={total_issues}")
    if strict and total_issues:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
