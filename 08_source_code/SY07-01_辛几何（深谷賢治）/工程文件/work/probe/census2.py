# -*- coding: utf-8 -*-
"""底本尽调 v2：陈述编号普查 + 图清单 + 公式编号精细提取"""
import pymupdf, re, collections, json
SRC = r"<本地路径> (深谷賢治 Kenji Fukaya) (z-library.sk  1lib.sk  z-lib.sk).pdf"
doc = pymupdf.open(SRC)
pages = [doc[i].get_text("text") for i in range(doc.page_count)]

# --- 陈述编号（定義/定理/補題/命題/系/例/注意/問/演習/予想/反例/記号） ---
kind_re = re.compile(r'(定義|定理|補題|命題|系|例|注意|問|問題|演習|予想|反例|記号|公式)\s*([0-9]{1,2})\s*[\.．]\s*([0-9]{1,3})')
kinds = collections.defaultdict(lambda: collections.defaultdict(set))  # kind -> ch -> set
for i, t in enumerate(pages):
    for m in kind_re.finditer(t):
        k, ch, num = m.group(1), int(m.group(2)), int(m.group(3))
        kinds[k][ch].add(num)
print("=== statement numbering ===")
for k in kinds:
    print(f"-- {k} --")
    for ch in sorted(kinds[k]):
        s = sorted(kinds[k][ch])
        print(f"  ch{ch}: n={len(s)} range={min(s)}..{max(s)} missing={[x for x in range(min(s),max(s)+1) if x not in s]}")

# --- 所有陈述编号的并集（同一计数器）---
allnums = collections.defaultdict(set)
for k in kinds:
    for ch, s in kinds[k].items():
        allnums[ch] |= s
print("\n=== union per chapter ===")
for ch in sorted(allnums):
    s = sorted(allnums[ch])
    print(f"ch{ch}: count={len(s)} range={min(s)}..{max(s)} missing={[x for x in range(1,max(s)+1) if x not in s][:40]}")

# --- 公式编号：用 span 方式，取行尾 (a.b) ---
eq_re = re.compile(r'[（(]\s*([0-9]{1,2})\s*[\.．]\s*([0-9]{1,3})\s*[)）]')
eqs = collections.defaultdict(set)
for i, t in enumerate(pages):
    for m in eq_re.finditer(t):
        ch, num = int(m.group(1)), int(m.group(2))
        eqs[ch].add(num)
print("\n=== equation nums (inline scan) ===")
for ch in sorted(eqs):
    s = sorted(eqs[ch])
    print(f"ch{ch}: n={len(s)} range={min(s)}..{max(s)} missing={[x for x in range(1,max(s)+1) if x not in s][:30]}")

# --- 图清单：单行 图X.Y 作为 caption 起始 ---
print("\n=== figure captions (page, text) ===")
figs = []
cap_re = re.compile(r'^\s*図\s*([0-9]{1,2})\s*[\.．]\s*([0-9]{1,2})')
for i, t in enumerate(pages):
    for line in t.splitlines():
        m = cap_re.match(line)
        if m:
            figs.append((i+1, i+1-10, f"{m.group(1)}.{m.group(2)}", line.strip()[:60]))
for f in figs:
    print(f"PDF{p[0]:>4} printed{p[1]:>4} 図{f[2]}: {f[3]}")

# --- 脚注数 ---
fn_re = re.compile(r'^\s*\*\s*([0-9]{1,2})\s', re.M)
fn = 0
for t in pages:
    fn += len(fn_re.findall(t))
print("\nfootnote lines:", fn)

doc.close()
