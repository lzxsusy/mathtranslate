src = open(r"C:\Users\admin\Downloads\_hausel_src\HauselICM-arxiv.tex", encoding="latin-1").read().splitlines()
pre = open("preamble.tex", encoding="utf-8").read()
i = pre.index("以下宏定义")
j = pre.rindex("% ====", 0, i)
head = pre[:pre.rindex("\n", 0, j) + 1].rstrip() + "\n\n"

lines = []
for ln in src[99:394]:
    s = ln.rstrip(); t = s.strip()
    if not t or t.startswith("%"):
        continue
    if t.startswith(("\\usepackage", "\\newtheorem", "\\newenvironment")):
        continue
    lines.append(s)

chunks, cur, depth = [], [], 0
for ln in lines:
    if depth == 0 and cur and ln.startswith("\\"):
        chunks.append("\n".join(cur)); cur = []
    cur.append(ln)
    depth += ln.count("{") - ln.count("}")
chunks.append("\n".join(cur))
chunks = [c for c in chunks if c.strip()]

out = (head
       + "% ============================================================\n"
       + "%  以下宏定义逐条照录原文 preamble（第 100--394 行），保证公式与原文完全一致\n"
       + "% ============================================================\n"
       + "\n".join(chunks) + "\n\n\\setcounter{tocdepth}{2}\n")
open("preamble.tex", "w", encoding="utf-8").write(out)
print("chunks:", len(chunks), "| multi-line:", sum(1 for c in chunks if "\n" in c))
print("hookuparrow:" , "\\hookuparrow" in pre, "| div:", "\\renewcommand{\\div}" in pre)
