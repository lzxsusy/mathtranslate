"""从 xelatex 日志里抽出 Overfull/Underfull，定位到具体 chunk 与行号。

日志里的「in paragraph at lines A--B」是当前正在读入的文件（而非主文件），
所以需要跟踪 `(./chunks/ch-xxx.tex` 这样的入栈标记来还原文件归属。
"""
import re
import sys
from pathlib import Path

LOG = Path(sys.argv[1] if len(sys.argv) > 1 else "partial.log")
SRC = Path(".")

file_re = re.compile(r"\((?:\./)?((?:chunks|front)/[^\s()]+\.tex)")
over_re = re.compile(r"(Overfull|Underfull) \\[hv]box \(([\d.]+)pt too (?:wide|high)\) (?:in paragraph|while \\output is active) at lines (\d+)--(\d+)")

cur = "<main>"
stack = []
hits = []
for raw in LOG.read_text(encoding="utf-8", errors="replace").splitlines():
    for m in file_re.finditer(raw):
        cur = m.group(1)
    m = over_re.search(raw)
    if m:
        hits.append((m.group(1), float(m.group(2)), int(m.group(3)), int(m.group(4)), cur))
        continue
    # 没有 "at lines" 的 overfull（多为单个盒子）
    m2 = re.search(r"(Overfull|Underfull) \\[hv]box \(([\d.]+)pt too (?:wide|high)\) detected at line (\d+)", raw)
    if m2:
        hits.append((m2.group(1), float(m2.group(2)), int(m2.group(3)), int(m2.group(3)), cur))

rows = []
for kind, amt, a, b, f in hits:
    p = Path(f)
    line_txt = ""
    if p.exists():
        lines = p.read_text(encoding="utf-8", errors="replace").splitlines()
        if 1 <= a <= len(lines):
            line_txt = lines[a - 1].strip()[:110]
    rows.append((kind, amt, f, a, b, line_txt))

out = []
out.append(f"# 排版审计：{LOG.name}\n")
out.append(f"Overfull 总数 {sum(1 for r in rows if r[0]=='Overfull')}，"
           f"Underfull 总数 {sum(1 for r in rows if r[0]=='Underfull')}\n")
out.append("| 类型 | 超出 | 文件 | 行 | 行首内容 |\n|---|---|---|---|---|")
for kind, amt, f, a, b, txt in sorted(rows, key=lambda r: -r[1]):
    out.append(f"| {kind} | {amt:.1f}pt | `{f}` | {a}–{b} | {txt.replace('|', '/')} |")

Path("overfull.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print("wrote overfull.md:", len(rows), "hits")
