# -*- coding: utf-8 -*-
"""Build page-aligned EN/ZH review files for SY01-07.

Original: arXiv:0710.5939v3 PDF (130 pp, PDF page == printed page).
Translation: 源码/sections/*.tex with '% ==== 原文 PDF 第 N 页' anchors.
Output: work/audit/review/pNNN.txt + manifest.tsv
"""
import os, re, sys, json, csv
import pymupdf

HERE = os.path.dirname(__file__)
PROJ = os.path.join(HERE, "..", "..", "..")
SEC = os.path.join(PROJ, "源码", "sections")
OUT = os.path.join(HERE, "review")
PDF = sys.argv[1] if len(sys.argv) > 1 else r"C:\Users\admin\Desktop\GMN系列\05_文献库\GMW2_红外代数\027_0710.5939_Geometric-endoscopy-and-mirror.pdf"

FILES = [
    "s01-intro.tex", "s02-duality.tex", "s03a-genus1.tex", "s03b-genus1.tex",
    "s04a-branes.tex", "s04b-branes.tex", "s05a-spectral.tex", "s05b-hecke.tex",
    "s06-categories.tex", "s07-classical.tex", "s08-functions.tex", "s09-other.tex",
    "s10-gerbes.tex", "s11-appendix.tex", "references.tex",
]

ANCHOR = re.compile(r"^%\s*====\s*原文 PDF 第\s*(\d+)\s*页.*====\s*$", re.M)

def strip_comments(tex: str) -> str:
    out = []
    for line in tex.splitlines():
        # remove unescaped % comments (keep \%)
        res = []
        i = 0
        while i < len(line):
            if line[i] == "%" and (i == 0 or line[i-1] != "\\"):
                break
            res.append(line[i]); i += 1
        out.append("".join(res))
    return "\n".join(out)

def detex(s: str) -> str:
    s = strip_comments(s)
    # remove translator-added blocks, they are not part of the original text
    s = re.sub(r"\\begin\{keytakeaway\}.*?\\end\{keytakeaway\}", "", s, flags=re.S)
    s = re.sub(r"\\begin\{translatornote\}.*?\\end\{translatornote\}", "", s, flags=re.S)
    # drop layout-only commands
    s = re.sub(r"\\label\{[^}]*\}", "", s)
    s = re.sub(r"\\index\{[^}]*\}", "", s)
    s = re.sub(r"\\tag\{([^}]*)\}", r"(\1)", s)
    s = re.sub(r"\\(?:cite|BookCite)\{([^}]*)\}", r"[\1]", s)
    s = re.sub(r"\\(?:ref|BookRef|eqref)\{([^}]*)\}", r"(\1)", s)
    s = re.sub(r"\\footnote\{", "（脚注：", s)
    # section headings
    s = re.sub(r"\\(section|subsection|subsubsection)\*?\{([^}]*)\}", r"\n\n## \2\n", s)
    # inline formatting -> content (leave math commands untouched)
    for cmd in ["textbf", "emph", "textit", "text", "mbox", "hbox"]:
        s = re.sub(r"\\" + cmd + r"\{([^{}]*)\}", r"\1", s)
    s = s.replace("\\[", "\n$$\n").replace("\\]", "\n$$\n")
    s = s.replace("\\(", "$").replace("\\)", "$")
    s = re.sub(r"\\begin\{([^}]*)\}(\[[^]]*\])?", r"\n[begin \1]\n", s)
    s = re.sub(r"\\end\{([^}]*)\}", r"\n[end \1]\n", s)
    s = re.sub(r"\\frag\{[^}]*\}", "", s)
    s = re.sub(r"\\item\b", "\n- ", s)
    s = s.replace("~", " ")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()

# ---- original pages (pdftotext -layout keeps reading order much better) ----
import subprocess
raw = subprocess.run(["pdftotext", "-layout", "-enc", "UTF-8", PDF, "-"],
                     check=True, capture_output=True).stdout.decode("utf-8")
pages = raw.split("\f")
if pages and not pages[-1].strip():
    pages = pages[:-1]
en = {i + 1: p.strip() for i, p in enumerate(pages)}

# ---- Chinese pages ----
zh = {}
zh_meta = {}
order = []
for fn in FILES:
    p = os.path.join(SEC, fn)
    t = open(p, encoding="utf-8").read()
    ms = list(ANCHOR.finditer(t))
    for j, m in enumerate(ms):
        n = int(m.group(1))
        body = t[m.end(): ms[j + 1].start() if j + 1 < len(ms) else len(t)]
        lstart = t.count("\n", 0, m.end()) + 2
        lend = lstart + body.count("\n")
        zh_meta.setdefault(n, []).append((fn, lstart, lend, body))
        zh.setdefault(n, []).append(detex(body))
        order.append((n, fn))

os.makedirs(OUT, exist_ok=True)
manifest = []
for n in range(1, 131):
    e = en.get(n, "")
    z = "\n\n".join(x for x in zh.get(n, []) if x.strip())
    path = os.path.join(OUT, f"p{n:03d}.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"### ORIGINAL PDF p.{n}\n\n{e}\n\n### CHINESE TRANSLATION\n\n{z}\n")
    ew = len(re.findall(r"[A-Za-z][A-Za-z'\-]+", e))
    zc = len(re.findall(r"[\u4e00-\u9fff]", z))
    ep = len([x for x in re.split(r"\n\s*\n", e) if x.strip()])
    zp = len([x for x in re.split(r"\n\s*\n", z) if x.strip()])
    manifest.append((n, ew, zc, round(zc / ew, 2) if ew else "", ep, zp))

with open(os.path.join(OUT, "manifest.tsv"), "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter="\t")
    w.writerow(["page", "en_words", "zh_chars", "ratio", "en_paras", "zh_paras"])
    w.writerows(manifest)

missing = [n for n in range(3, 128) if n not in zh]
print("pages with anchors:", len(zh), "missing 3-127:", missing)
print("pages written:", len(manifest))
print("total en words:", sum(x[1] for x in manifest), "total zh chars:", sum(x[2] for x in manifest))

# ---- 10-page review chunks ----
CH = os.path.join(OUT, "chunks")
os.makedirs(CH, exist_ok=True)
chunks = []
start = 3
while start <= 127:
    end = min(start + 9, 127)
    chunks.append((start, end))
    start = end + 1
idx = []
for a, b in chunks:
    name = f"p{a:03d}-{b:03d}.txt"
    with open(os.path.join(CH, name), "w", encoding="utf-8") as f:
        f.write(f"# SY01-07《几何内窥与镜像对称》整书对照审校块 p.{a}–{b}\n")
        f.write("# 底本：Frenkel–Witten, arXiv:0710.5939v3（PDF 页 = 印刷页）\n")
        f.write("# 译文：源码/sections/*.tex；中文行号见 [Lstart-Lend]\n")
        f.write("# 页边界处段落跨页，中文可能挂在上一页锚点下；请按整块核对。\n\n")
        for n in range(a, b + 1):
            f.write(f"\n{'='*20} PDF p.{n} {'='*20}\n\n")
            f.write("----- ENGLISH -----\n")
            f.write((en.get(n, "") or "(page not extracted)") + "\n\n")
            f.write("----- CHINESE -----\n")
            if zh_meta.get(n):
                for fn, ls, le, body in zh_meta[n]:
                    f.write(f"--- {fn}:L{ls}-L{le} ---\n")
                    f.write(detex(body) + "\n\n")
            else:
                f.write("(no Chinese anchor for this page)\n\n")
    idx.append((a, b, name, os.path.getsize(os.path.join(CH, name))))
with open(os.path.join(CH, "index.tsv"), "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter="\t")
    w.writerow(["page_start", "page_end", "file", "bytes"])
    w.writerows(idx)
print("chunks written:", len(idx))
for row in idx:
    print(row)
