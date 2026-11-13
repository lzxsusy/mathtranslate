# -*- coding: utf-8 -*-
r"""静态检查（每次改动后跑）：python tools/check.py
检查项：
  1. 编号公式集合：tex 里 \tag{} 与 tags.txt（原文实测 57 条）比对 → MISSING/EXTRA/DUPLICATE
  2. 花括号平衡（去注释后）
  3. \begin/\end 环境配对
  4. $ 数量为偶（去注释后）
  5. 禁用命令扫描：\documentclass \usepackage \begin{document} \newcommand \cite \tableofcontents
  6. U+FFFD 乱码、BOM、CRLF
  7. markdown 粗体 **
  8. 每块文件的分类统计
"""
import sys, re, io, os, glob
sys.stdout.reconfigure(encoding="utf-8")

ROOT = r"<本地路径>"
CHUNKS = os.path.join(ROOT, "src", "chunks")
TAGS_TXT = os.path.join(ROOT, "tags.txt")

expected = []
seen = set()
for ln in io.open(TAGS_TXT, encoding="utf-8"):
    ln = ln.strip()
    if not ln or ln.startswith("#"):
        continue
    t = ln.split("\t")[0]
    if t and t not in seen:
        seen.add(t)
        expected.append(t)

files = sorted(glob.glob(os.path.join(CHUNKS, "*.tex")))
files = [f for f in files if os.path.basename(f) != "_order.tex"]
print("chunk files:", len(files))

tags = []
problems = []
for f in files:
    raw = io.open(f, "rb").read()
    if raw.startswith(b"\xef\xbb\xbf"):
        problems.append(("BOM", os.path.basename(f), 0))
    if b"\r\n" in raw:
        problems.append(("CRLF", os.path.basename(f), 0))
    txt = raw.decode("utf-8", errors="replace")
    if "\ufffd" in txt:
        problems.append(("U+FFFD", os.path.basename(f), txt.count("\ufffd")))
    stripped = []
    for i, ln in enumerate(txt.splitlines(), 1):
        code = re.sub(r"(?<!\\)%.*$", "", ln)
        code = re.sub(r"<本地路径>|[^|]*\|", "", code)
        stripped.append(code)
        for m in re.finditer(r"<本地路径>", code):
            if m.group(1).strip():
                tags.append((m.group(1).strip(), os.path.basename(f), i))
    code_txt = "\n".join(stripped)
    for bad in (r"\documentclass", r"\usepackage", r"\begin{document}", r"\newcommand",
                r"\def\\", r"\cite", r"\tableofcontents", r"\appendix"):
        for _ in re.finditer(re.escape(bad), code_txt):
            problems.append(("FORBIDDEN", os.path.basename(f), bad))
    ob, cb = code_txt.count("{"), code_txt.count("}")
    if ob != cb:
        problems.append(("BRACES", os.path.basename(f), f"{ob} vs {cb}"))
    d = code_txt.replace(r"\$", "")
    if d.count("$") % 2:
        problems.append(("DOLLAR", os.path.basename(f), d.count("$")))
    begins = re.findall(r"<本地路径>]+)\}", code_txt)
    ends = re.findall(r"<本地路径>]+)\}", code_txt)
    from collections import Counter
    bc, ec = Counter(begins), Counter(ends)
    for k in set(bc) | set(ec):
        if bc[k] != ec[k]:
            problems.append(("ENV", os.path.basename(f), f"{k}: begin {bc[k]} / end {ec[k]}"))
    if re.search(r"(?<!\\)\*\*[^*\n]+\*\*", code_txt):
        problems.append(("MD_BOLD", os.path.basename(f), "**"))
    # Unicode 数学符号出现在正文（数学模式外）→ 编译必然 "Missing character"
    for sym in "≥≤×→⊗≃≅⊂∈∘±∑∫≠≈≡⇒⇔∂√∞∓⊥":
        n = code_txt.count(sym)
        if n:
            problems.append(("UNICODE_MATH", os.path.basename(f), f"{sym} ×{n}"))

from collections import Counter
print("\n=== 1. 公式编号 ===")
tagvals = [t[0] for t in tags]
tc = Counter(tagvals)
dup = sorted([k for k, v in tc.items() if v > 1])
found = set(tagvals)
missing = [t for t in expected if t not in found]
extra = [t for t in tagvals if t not in seen]
print(f"原文 tag 数: {len(expected)}；tex 中 \\tag 数: {len(tags)}")
print("MISSING:", missing if missing else "无")
print("EXTRA:", extra if extra else "无")
print("DUPLICATE:", dup if dup else "无")

print("\n=== 2-7. 其他检查 ===")
if problems:
    for p in problems:
        print("  ", p)
else:
    print("  无问题")

print("\n=== 按文件 tag 统计 ===")
byfile = {}
for v, f, ln in tags:
    byfile.setdefault(f, []).append(v)
for f in sorted(byfile):
    vs = byfile[f]
    print(f"  {f}: {len(vs)} 条, {vs[0]} … {vs[-1]}")

print("\n=== 各块交付情况（文件数 / 行数） ===")
stat = {}
for f in files:
    n = len(io.open(f, encoding="utf-8", errors="replace").read().splitlines())
    key = os.path.basename(f).split("-")[0].replace(".tex", "")
    stat.setdefault(key, [0, 0])
    stat[key][0] += 1
    stat[key][1] += n
for k in sorted(stat):
    print(f"  {k}: {stat[k][0]} files, {stat[k][1]} lines")
