# -*- coding: utf-8 -*-
"""statement 页码定位 + 页码->源码行映射。"""
import io, re, json

SRC = r"<本地路径>"
TEXT = r"<本地路径>"

def read_lines(p):
    with io.open(p, encoding="utf-8") as f:
        return f.read().split("\n")

def strip_comment(line):
    out = []; i = 0
    while i < len(line):
        c = line[i]
        if c == "\\" and i + 1 < len(line):
            out.append(line[i:i+2]); i += 2; continue
        if c == "%":
            break
        out.append(c); i += 1
    return "".join(out)

src = read_lines(SRC)
stoks = []
for no, raw in enumerate(src, 1):
    line = strip_comment(raw)
    line = re.sub(r"\\\[.*?\\\]", " ", line)
    line = re.sub(r"\$[^$]*\$", " ", line)
    line = re.sub(r"\\[a-zA-Z@]+\*?", " ", line)
    line = re.sub(r"[{}$&~^_]", " ", line)
    for m in re.finditer(r"[A-Za-z][A-Za-z\-']{1,}", line):
        stoks.append((m.group(0).lower(), no))

index = {}
for i, (w, l) in enumerate(stoks):
    index.setdefault(w, []).append(i)
freq = {w: len(v) for w, v in index.items()}

pages = []
cur = None
for line in read_lines(TEXT):
    m = re.match(r"===== PDF PAGE (\d+) =====", line)
    if m:
        cur = {"page": int(m.group(1)), "lines": []}
        pages.append(cur)
    elif cur is not None:
        cur["lines"].append(line)
pagelines = {pg["page"]: pg["lines"] for pg in pages}

def words_of(txt):
    return [w.lower() for w in re.findall(r"[A-Za-z][A-Za-z\-']{1,}", txt)]

bib_line = None
for i, l in enumerate(src, 1):
    if "\\bibliography{" in l:
        bib_line = i
        break

# ---------- 1. statement 页码 ----------
stmts = json.load(io.open(r"<本地路径>", encoding="utf-8"))
anchors = []          # (page, line, why)
for st in stmts:
    pat = re.compile(r"(?<![0-9.])" + re.escape(st["num"]) + r"\s+" + st["name"])
    hit = None
    for pg in pages:
        txt = "\n".join(pagelines[pg["page"]])
        if pat.search(txt):
            hit = pg["page"]
            break
    if hit:
        anchors.append((hit, st["line"], "%s %s" % (st["num"], st["name"])))
    else:
        print("MISS", st["num"], st["name"], st["line"])

# ---------- 2. 章节标题页码（TOC 给出） ----------
sec_anchor = {1: 171, 2: 365, 3: 516, 4: 1055, 5: 1805, 6: 3291, 7: 4656}
sec_page = {1: 2, 2: 9, 3: 14, 4: 20, 5: 30, 6: 40, 7: 47}
for k, ln in sec_anchor.items():
    anchors.append((sec_page[k], ln, "sec %d" % k))

anchors.sort()
json.dump(anchors, io.open(r"<本地路径>", "w", encoding="utf-8"), ensure_ascii=False)

# ---------- 3. 每页上下界 ----------
lo = {}; hi = {}
for p in range(1, 57):
    lo[p] = 1
    hi[p] = 5564
for pg, ln, why in anchors:
    if pg <= 51:
        for q in range(pg + 1, 52):
            lo[q] = max(lo[q], ln + 1)
            break
        hi[pg] = min(hi[pg], ln)
    # 该页之前页的上界也受限
for p in range(1, 52):
    # 若 p 页有 anchor，其起点必须 <= 该 anchor
    pass
# 传播：hi[p] <= hi[p+1] 的约束由起点递增保证，简化处理
for p in range(2, 52):
    lo[p] = max(lo[p], lo[p - 1] + 1)

# ---------- 4. 页首词定位 ----------
def locate(ws, lmin, lmax, lo_tok):
    votes = {}
    for w in ws:
        if w not in index or freq[w] > 300 or len(w) < 3:
            continue
        wt = 1.0 / (1.0 + freq[w] / 20.0)
        for i in index[w]:
            ln = stoks[i][1]
            if ln < lmin or ln > lmax or i < lo_tok:
                continue
            votes[i // 4] = votes.get(i // 4, 0.0) + wt
    if not votes:
        return None
    best = max(votes.items(), key=lambda kv: kv[1])[0] * 4
    # 向前找该窗口内最小 token 位置
    j = max(lo_tok, best - 12)
    while j > lo_tok and j > best - 40 and stoks[j][1] >= lmin:
        j -= 1
    return j

start_line = {}
prev_tok = 0
for pg in pages:
    p = pg["page"]
    if p == 1:
        start_line[p] = 156
        continue
    if p == 2:
        start_line[p] = 171
        continue
    if p >= 52:
        start_line[p] = bib_line
        continue
    txt = "\n".join(pagelines[p])
    ws = words_of(txt)[:80]
    a = lo[p]; b = hi[p]
    if a >= b:
        b = min(5564, a + 120)
    pos = locate(ws, a, b, prev_tok)
    if pos is None:
        print("WARN page", p, "range", a, b)
        start_line[p] = a
        continue
    start_line[p] = stoks[pos][1]
    prev_tok = pos

# 单调化
last = 0
for p in range(1, 52):
    if start_line[p] < last:
        start_line[p] = last
    last = start_line[p]

out = io.open(r"<本地路径>", "w", encoding="utf-8", newline="\n")
out.write("pdf_page\tsource_line\tlo\thi\n")
for p in range(1, 57):
    out.write("%d\t%d\t%d\t%d\n" % (p, start_line[p], lo[p], hi[p]))
out.close()
json.dump(start_line, io.open(r"<本地路径>", "w", encoding="utf-8"), ensure_ascii=False)
print([(p, start_line[p]) for p in range(1, 57)])
