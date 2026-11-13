# -*- coding: utf-8 -*-
"""底本普查：页数、页码映射、图/表/公式编号计数"""
import pymupdf, re, json, collections
SRC = r"<本地路径> (深谷賢治 Kenji Fukaya) (z-library.sk  1lib.sk  z-lib.sk).pdf"
doc = pymupdf.open(SRC)

pages = []
for i in range(doc.page_count):
    pages.append(doc[i].get_text("text"))

# 1) 检查每页首行里的印刷页码
print("=== first line samples (printed page detection) ===")
for i in [10, 11, 19, 20, 49, 50, 99, 100, 199, 200, 299, 300, 399, 400, 419, 424]:
    first = pages[i].strip().splitlines()[:2]
    print(f"PDF {i+1}: {first}")

# 2) 图/表 普查
fig_re = re.compile(r'図\s*([0-9]{1,2})[\.\s]\s*([0-9]{1,2})')
tab_re = re.compile(r'表\s*([0-9]{1,2})[\.\s]\s*([0-9]{1,2})')
figs = collections.Counter()
tabs = collections.Counter()
for i, t in enumerate(pages):
    for m in fig_re.finditer(t):
        figs[(int(m.group(1)), int(m.group(2)))] += 1
    for m in tab_re.finditer(t):
        tabs[(int(m.group(1)), int(m.group(2)))] += 1
print("\n=== figures (ch.sec) ===")
print(sorted(figs.items()))
print("\n=== tables (ch.sec) ===")
print(sorted(tabs.items()))

# 3) 公式编号：整行形如 (2.14) 的行
eq_re = re.compile(r'^\s*[（(]?\s*([0-9]{1,2})\s*[\.．]\s*([0-9]{1,3})\s*[)）]\s*$')
eqs = collections.defaultdict(set)
for i, t in enumerate(pages):
    for line in t.splitlines():
        m = eq_re.match(line.strip())
        if m:
            eqs[int(m.group(1))].add(int(m.group(2)))
print("\n=== equation tags per chapter ===")
for ch in sorted(eqs):
    s = sorted(eqs[ch])
    print(f"ch{ch}: n={len(s)} max={max(s) if s else 0}")

# 4) 每页文本量
print("\n=== chars/page min/avg ===")
import statistics
lens = [len(t.strip()) for t in pages]
print(min(lens), statistics.mean(lens), max(lens))
doc.close()
