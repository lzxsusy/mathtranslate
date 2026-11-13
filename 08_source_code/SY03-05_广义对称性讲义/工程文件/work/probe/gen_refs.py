# -*- coding: utf-8 -*-
"""从原文 pp.139-150 自动转录参考文献（221 条）为 LaTeX 片段 chunks/c-refs.tex。
文本层对参考文献是可靠的（纯文本 + 少量数学被拍平），仅做 ligature/特殊字符处理。
"""
import sys, re, io, os
sys.stdout.reconfigure(encoding='utf-8')
import pymupdf as fitz

ROOT = r"<本地路径>"
SRC = os.path.join(ROOT, "2307.07547v2.pdf")
OUT = os.path.join(ROOT, "work", "src", "chunks", "c-refs.tex")
doc = fitz.open(SRC)

raw = []
for i in range(138, len(doc)):          # p139..p150 (0-based 138..149)
    raw.append(doc[i].get_text())
text = "\n".join(raw)

m = re.search(r"(?m)^\[1\]$", text)
if m:
    text = text[m.start():]

REPL = {
    "\ufb00": "ff", "\ufb01": "fi", "\ufb02": "fl", "\ufb03": "ffi", "\ufb04": "ffl",
    "\ufb05": "st", "\ufb06": "st",
    "\u2019": "'", "\u2018": "`", "\u201c": "``", "\u201d": "''",
    "\u2013": "--", "\u2014": "---", "\u00ad": "",
    "\u00a0": " ",
}
for a, b in REPL.items():
    text = text.replace(a, b)

lines = []
for ln in text.splitlines():
    s = ln.strip()
    if re.fullmatch(r"\d{1,3}", s):
        continue
    if s in ("References",):
        continue
    lines.append(s)

body_text = "\n".join(lines)
pat = re.compile(r"(?m)^\[(\d+)\]\s*")
ms = list(pat.finditer(body_text))
entries = []
for k, mm in enumerate(ms):
    start = mm.end()
    end = ms[k + 1].start() if k + 1 < len(ms) else len(body_text)
    entries.append((int(mm.group(1)), body_text[start:end]))

parsed = []
for num, parts in entries:
    body = re.sub(r"\s+", " ", parts).strip()
    parsed.append((num, body))

print("entries:", len(parsed), "first:", parsed[0][0], "last:", parsed[-1][0])
nums = [n for n, _ in parsed]
missing = [n for n in range(1, nums[-1] + 1) if n not in set(nums)]
print("missing numbers:", missing, "count", len(missing))
dups = [n for n in set(nums) if nums.count(n) > 1]
print("dups:", sorted(dups), "count", len(dups))

GREEK = {
    "\u03b1": r"\alpha", "\u03b2": r"\beta", "\u03b3": r"\gamma", "\u03b4": r"\delta",
    "\u03b5": r"\varepsilon", "\u03f5": r"\epsilon", "\u03b6": r"\zeta", "\u03b7": r"\eta",
    "\u03b8": r"\theta", "\u03b9": r"\iota", "\u03ba": r"\kappa", "\u03bb": r"\lambda",
    "\u03bc": r"\mu", "\u03bd": r"\nu", "\u03be": r"\xi", "\u03c0": r"\pi", "\u03c1": r"\rho",
    "\u03c3": r"\sigma", "\u03c4": r"\tau", "\u03c5": r"\upsilon", "\u03c6": r"\phi",
    "\u03c7": r"\chi", "\u03c8": r"\psi", "\u03c9": r"\omega",
    "\u0393": r"\Gamma", "\u0394": r"\Delta", "\u0398": r"\Theta", "\u039b": r"\Lambda",
    "\u039e": r"\Xi", "\u03a0": r"\Pi", "\u03a3": r"\Sigma", "\u03a6": r"\Phi",
    "\u03a8": r"\Psi", "\u03a9": r"\Omega",
    "\u22c6": r"\star", "\u2a7e": r"\ge", "\u2a7d": r"\le", "\u2261": r"\equiv",
    "\u2243": r"\simeq", "\u2260": r"\ne", "\u2282": r"\subset", "\u2283": r"\supset",
    "\u2297": r"\otimes", "\u2295": r"\oplus", "\u2192": r"\to", "\u21d2": r"\Rightarrow",
    "\u2190": r"\leftarrow", "\u2212": "-", "\u221e": r"\infty", "\u2113": r"\ell",
    "\u2202": r"\partial", "\u222b": r"\int", "\u2264": r"\le", "\u2265": r"\ge",
    "\u00d7": r"\times", "\u00b1": r"\pm", "\u2217": r"\ast", "\u2032": r"'",
}


def esc(s):
    s = s.replace("\\", r"\textbackslash{}")
    for ch, rep in (("&", r"\&"), ("%", r"\%"), ("#", r"\#"), ("_", r"\_"),
                    ("$", r"\$"), ("{", r"\{"), ("}", r"\}"), ("~", r"\textasciitilde{}"),
                    ("^", r"\textasciicircum{}")):
        s = s.replace(ch, rep)
    for ch, rep in GREEK.items():
        if ch in s:
            s = s.replace(ch, "$" + rep + "$")
    return s


out = []
out.append(r"% =====================================================================")
out.append(r"%  c-refs.tex —— 参考文献（原文 pp.139–150，共 221 条）")
out.append(r"%  由 work/probe/gen_refs.py 从原文 PDF 文字层自动转录，未逐条人工校对；")
out.append(r"%  原文标题中的数学符号在文字层中被拍平，仅作检索用。全部条目保留英文原貌（学术惯例：参考文献不译）。")
out.append(r"% =====================================================================")
out.append(r"\clearpage")
out.append(r"\section*{参考文献}")
out.append(r"\addcontentsline{toc}{section}{参考文献}")
out.append(r"{\small")
out.append(r"\begin{multicols}{2}")
out.append(r"\raggedright")
out.append(r"\setlength{\parindent}{0pt}")
out.append(r"\setlength{\parskip}{2.2pt}")
for num, body in parsed:
    out.append(r"\refitem{%d}{%s}" % (num, esc(body)))
out.append(r"\end{multicols}")
out.append(r"}")
with io.open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    fh.write("\n".join(out) + "\n")
print("written", OUT, os.path.getsize(OUT), "bytes")
