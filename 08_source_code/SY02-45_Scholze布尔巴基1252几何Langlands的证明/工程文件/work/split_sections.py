# -*- coding: utf-8 -*-
"""按节标题切分底本 all.txt -> 工程文件/work/src-sNN.txt（保留 `1252–NN` 页界行），并清点编号条目。"""
import io, os, re, json

ROOT = os.path.dirname(os.path.abspath(__file__))
ALL = r"C:\Users\admin\Downloads\bz_gl_work\bourbaki\all.txt"
OUT = os.path.join(ROOT, "src")
WORK = ROOT

HEADS = [
    (1,  "1. Introduction"),
    (2,  "2. The geometric Langlands equivalence"),
    (3,  "3. Sheaves on BunG"),
    (4,  "4. The stack of local systems"),
    (5,  "5. Spectral action"),
    (6,  "6. The case of G = Gm"),
    (7,  "7. Beilinson’s spectral projector"),
    (8,  "8. Trace of Frobenius"),
    (9,  "9. Whittaker coefficients"),
    (10, "10. Eisenstein series"),
    (11, "11. Kac–Moody localization"),
    (12, "12. Cusp forms"),
    (13, "References"),
]

lines = io.open(ALL, encoding="utf-8").read().split("\n")
pos = {}
for n, h in HEADS:
    idx = [i for i, L in enumerate(lines) if L.strip() == h]
    if len(idx) != 1:
        raise SystemExit("heading %r found %d times: %r" % (h, len(idx), idx))
    pos[n] = idx[0]

items_sorted = sorted(pos.items())
bounds = []
for k, (n, i) in enumerate(items_sorted):
    start = i + 1
    end = items_sorted[k + 1][1] if k + 1 < len(items_sorted) else len(lines)
    bounds.append((n, i, start, end))

os.makedirs(OUT, exist_ok=True)
TYPES = ("Theorem", "Remark", "Definition", "Proposition", "Corollary", "Lemma", "Example", "Conjecture")
pat = re.compile(r"^(%s)\s+(\d+)\.(\d+)" % "|".join(TYPES))
pat_page = re.compile(r"^1252–(\d+)$")

report = []
for n, hi, start, end in bounds:
    body = lines[start:end]
    while body and not body[-1].strip():
        body.pop()
    pages = [int(pat_page.match(L.strip()).group(1)) for L in body if pat_page.match(L.strip())]
    found = {}
    for L in body:
        m = pat.match(L.strip())
        if m and int(m.group(2)) == n:
            k = int(m.group(3))
            if k in found:
                print("!! dup %d.%d: %s" % (n, k, L[:60]))
            found[k] = m.group(1)
    missing = [k for k in range(1, (max(found) if found else 0) + 1) if k not in found]
    cnt = {}
    for v in found.values():
        cnt[v] = cnt.get(v, 0) + 1
    out = os.path.join(OUT, "src-s%02d.txt" % n)
    head_page = int(pat_page.match(lines[hi].strip()).group(1)) if pat_page.match(lines[hi].strip()) else None
    io.open(out, "w", encoding="utf-8").write("\n".join(body) + "\n")
    report.append(dict(sec=n, head=HEADS[n-1][1], pages=pages, n_pages=len(pages),
                       chars=len("\n".join(body)), items=len(found), by_type=cnt,
                       missing=missing,
                       seq=[(found[k], "%d.%d" % (n, k)) for k in sorted(found)]))

tot = {}
for r in report:
    for k, v in r["by_type"].items():
        tot[k] = tot.get(k, 0) + v
print(json.dumps(dict(sections=[{k: v for k, v in r.items() if k != "seq"} for r in report],
                      totals=tot, total_items=sum(r["items"] for r in report)),
                 ensure_ascii=False, indent=1))
io.open(os.path.join(WORK, "sections.json"), "w", encoding="utf-8").write(
    json.dumps(report, ensure_ascii=False, indent=1))
