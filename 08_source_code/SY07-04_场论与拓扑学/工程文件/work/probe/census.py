# -*- coding: utf-8 -*-
"""Deck check for 場の理論とトポロジー (Kohno)."""
import pymupdf, os, re, json, collections
ROOT = r"<本地路径>"
PDF = os.path.join(ROOT, "src.pdf")
doc = pymupdf.open(PDF)
N = len(doc)
print("pages", N)

# 1) page geometry and image/drawing counts
geo = collections.Counter()
for p in doc:
    geo[(round(p.rect.width), round(p.rect.height))] += 1
print("sizes", geo)

# 2) printed page numbers: look at top/bottom 70pt for pure-number tokens
def printed_no(page):
    d = page.get_text("dict")
    cands = []
    for b in d["blocks"]:
        for l in b.get("lines", []):
            txt = "".join(s["text"] for s in l["spans"]).strip()
            y = l["bbox"][1]
            if y < 70 or y > page.rect.height - 70:
                m = re.fullmatch(r"[0-9]{1,3}", txt)
                if m:
                    cands.append((y, int(txt)))
    if cands:
        return cands[0][1]
    return None

rows = []
for i, p in enumerate(doc):
    rows.append((i + 1, printed_no(p), len(p.get_images()), len(p.get_drawings()), len(p.get_text().strip())))

print("\nPDFpage printed imgs draws textlen")
for r in rows:
    print(*r)

# 3) sections / chapters from text
txts = [p.get_text() for p in doc]
secs = []
for i, t in enumerate(txts):
    for line in t.split("\n"):
        ls = line.strip()
        m = re.match(r"^§\s*([0-9]+\.[0-9]+)\s*(.+)$", ls)
        if m:
            secs.append((i + 1, "sec", m.group(1), m.group(2)[:40]))
        if re.match(r"^第\s*[0-9]+\s*章", ls):
            secs.append((i + 1, "ch", "", ls[:40]))
print("\n--- sections/chapters (dedup consecutive) ---")
seen = set()
for s in secs:
    k = (s[1], s[2], s[3])
    if k in seen:
        continue
    seen.add(k)
    print(s)

# 4) figure captions
figs = []
for i, t in enumerate(txts):
    for m in re.finditer(r"図\s*([0-9]+[\.\-][0-9]+)", t):
        figs.append((i + 1, m.group(1)))
cnt = collections.Counter(figs)
print("\n--- 図 captions (page, numbers) ---")
for k, v in cnt.items():
    print(k, v)
print("fig caption occurrences:", len(figs), "unique:", len(set(f[1] for f in figs)))

# 5) tables
tabs = [(i + 1, m.group(1)) for i, t in enumerate(txts) for m in re.finditer(r"表\s*([0-9]+[\.\-][0-9]+)", t)]
print("\n--- 表 captions ---", tabs)

# 6) equation numbers (x.y) at right margin
eqs = []
for i, p in enumerate(doc):
    W = p.rect.width
    d = p.get_text("dict")
    for b in d["blocks"]:
        for l in b.get("lines", []):
            s = "".join(sp["text"] for sp in l["spans"]).strip()
            if not s:
                continue
            x1 = l["bbox"][2]
            if x1 > 0.80 * W:
                m = re.fullmatch(r"[\(（]\s*([0-9]+\.[0-9]+)\s*[\)）]", s)
                if m:
                    eqs.append((i + 1, m.group(1)))
print("\n--- equations at right margin ---")
print("count", len(eqs))
print("unique", len(set(e[1] for e in eqs)))
print(eqs[:80])

# 7) keywords / back matter
for kw in ["参考文献", "索", "要約", "今後の方向", "あとがき", "記号"]:
    pgs = [i + 1 for i, t in enumerate(txts) if kw in t]
    print(kw, pgs[:25])
