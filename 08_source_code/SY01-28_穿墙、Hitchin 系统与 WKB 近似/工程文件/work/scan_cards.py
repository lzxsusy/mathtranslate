# -*- coding: utf-8 -*-
"""扫描 GMN2 译本：式号、页码、图号、译注、TODO。"""
import re, subprocess, collections, io, sys

ROOT = r"C:\Users\admin\Desktop\GMN系列\01_翻译\GMN2_0907.3987"
SRC = ROOT + r"\源码"
PDF = ROOT + r"\成品\GMN2_穿墙_Hitchin与WKB_v1.0.pdf"
OUT = ROOT + r"\工程文件\work\scan_out.txt"

lines = []
def p(*a):
    s = " ".join(str(x) for x in a)
    lines.append(s)

# 1) aux labels
aux = io.open(SRC + r"\main.aux", encoding="utf-8", errors="replace").read()
labels = re.findall(r"\\newlabel\{([^}]*)\}\{\{([^}]*)\}\{([^}]*)\}", aux)
p("AUX newlabel total:", len(labels))
eqs = [(num, pg, lab) for lab, num, pg in labels if lab.startswith("eq:")]
p("eq labels:", len(eqs))

# 2) toc
toc = io.open(SRC + r"\main.toc", encoding="utf-8", errors="replace").read()
p("=== TOC ===")
for m in re.finditer(r"\\contentsline \{(\w+)\}\{(.*?)\}\{(\d+)\}", toc):
    lvl, title, pg = m.groups()
    if lvl in ("section", "subsection"):
        p(lvl, pg, re.sub(r"\\numberline \{([^}]*)\}", r"\1 ", title))

# 3) PDF text
txt = subprocess.run(["pdftotext", "-layout", PDF, "-"], capture_output=True).stdout.decode("utf-8", "replace")
io.open(OUT, "w", encoding="utf-8").write(txt)
p("PDF text chars:", len(txt), "pages approx:", txt.count("\f"))

# 4) equation numbers at line end
pat = re.compile(r"\((\d{1,2}\.\d{1,3}[a-z]?|[A-E]\.\d{1,3}[a-z]?)\)\s*$")
found = collections.Counter()
order = []
for line in txt.split("\n"):
    m = pat.search(line)
    if m:
        found[m.group(1)] += 1
        if m.group(1) not in order:
            order.append(m.group(1))
p("eq numbers seen (unique):", len(found), "occurrences:", sum(found.values()))

# per-section max and count
secs = collections.defaultdict(list)
for k in found:
    mm = re.match(r"([A-E]|\d+)\.(\d+)", k)
    if mm:
        secs[mm.group(1)].append((int(mm.group(2)), k))
p("=== per-section eq numbers (max, count unique, missing) ===")
for s in sorted(secs, key=lambda x: (x.isdigit() is False, x)):
    nums = sorted(set(n for n, k in secs[s]))
    missing = [i for i in range(1, max(nums) + 1) if i not in nums]
    p(s, "max", max(nums), "uniq", len(nums), "missing", missing[:20])

# 5) figure captions
figs = re.findall(r"图\s*(\d{1,2})\s*[:：]", txt)
p("figure caption numbers found:", len(set(figs)), "max", max(map(int, figs)) if figs else 0)
p("fig set sample:", sorted(set(map(int, figs)))[:10], "...", sorted(set(map(int, figs)))[-5:])

# 6) yizhu
p("=== YIZHU ===")
import glob, os
for f in sorted(glob.glob(SRC + r"\chunks\*.tex")):
    s = io.open(f, encoding="utf-8").read()
    for m in re.finditer(r"\\begin\{yizhu\}(.*?)\\end\{yizhu\}", s, re.S):
        body = re.sub(r"\s+", " ", m.group(1)).strip()
        p(os.path.basename(f), "|", body[:400])

# 7) TODO
p("=== TODO (unique-ish) ===")
todo = []
for f in sorted(glob.glob(SRC + r"\chunks\*.tex")):
    s = io.open(f, encoding="utf-8").read()
    for i, ln in enumerate(s.split("\n"), 1):
        if "% TODO" in ln:
            todo.append((os.path.basename(f), i, ln.strip()[:160]))
p("TODO lines:", len(todo))

io.open(OUT, "w", encoding="utf-8").write("\n".join(lines))
print("\n".join(lines))
