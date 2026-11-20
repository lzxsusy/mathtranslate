import os, re, glob, collections
ROOT = r"C:\Users\admin\Downloads\_mirror_review"
CH = os.path.join(ROOT, "chapters")
ORDER = ["preface","notation","chapter01","chapter02","chapter03","chapter04","chapter05",
         "chapter06","chapter07","chapter08","chapter09","chapter10","chapter11",
         "chapter12","appendixA","appendixB"]
seen = []
for name in ORDER:
    txt = open(os.path.join(CH, name + ".tex"), encoding="utf-8").read()
    ps = [int(x) for x in re.findall(r"\\SourcePage\{(\d+)\}", txt)]
    seen += ps
    # duplicates / non-monotone
    bad = [(a,b) for a,b in zip(ps, ps[1:]) if b < a]
    dup = [p for p,c in collections.Counter(ps).items() if c > 1]
    print(f"{name}: {len(ps)} pages {ps[0] if ps else '-'}..{ps[-1] if ps else '-'}"
          + (f" NONMONO {bad[:5]}" if bad else "") + (f" DUP {dup[:5]}" if dup else ""))
allpages = set(seen)
missing = [p for p in range(14, 493) if p not in allpages]
print("total markers", len(seen), "unique", len(allpages))
print("MISSING pages:", missing)
