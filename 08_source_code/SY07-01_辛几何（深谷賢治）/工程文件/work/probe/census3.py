# -*- coding: utf-8 -*-
"""图清单 + 脚注普查"""
import pymupdf, re, collections
SRC = r"<本地路径> (深谷賢治 Kenji Fukaya) (z-library.sk  1lib.sk  z-lib.sk).pdf"
doc = pymupdf.open(SRC)
pages = [doc[i].get_text("text") for i in range(doc.page_count)]

# 图 caption: 行首 "図X.Y"
cap_re = re.compile(r'^\s*図\s*([0-9]{1,2})\s*[\.．]\s*([0-9]{1,2})')
print("=== figure captions ===")
figs = []
for i, t in enumerate(pages):
    for line in t.splitlines():
        m = cap_re.match(line)
        if m:
            figs.append((i+1, i+1-10, f"{m.group(1)}.{m.group(2)}", line.strip()[:70]))
for f in figs:
    print(f"PDF{f[0]:>4} printed{f[1]:>4} fig{f[2]}: {f[3]}")
print("total caption lines:", len(figs))
seen = {}
for f in figs:
    seen.setdefault(f[2], []).append((f[0], f[3]))
print("\nunique figs:", len(seen))
for k in sorted(seen, key=lambda x: (int(x.split('.')[0]), int(x.split('.')[1]))):
    print(f"fig {k}: pages {[s[0] for s in seen[k]]}")

# 脚注：行首 *数字
print("\n=== footnotes ===")
fn_re = re.compile(r'^\s*[*＊]\s*([0-9]{1,2})\s')
tot = 0
for i, t in enumerate(pages):
    ms = fn_re.findall(t)
    if ms:
        tot += len(ms)
        print(f"PDF {i+1}: {ms}")
print("total footnote markers:", tot)
doc.close()
