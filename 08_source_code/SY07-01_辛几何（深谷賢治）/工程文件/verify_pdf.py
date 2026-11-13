# -*- coding: utf-8 -*-
"""Gate 3 成品 PDF 回读：tag 是否全部出现 / 章标题 / 图题 / 字体嵌入 / 异常字符"""
import os, re, sys

ROOT = r"<本地路径>"
PDF = os.path.join(ROOT, "src", "main.pdf")
TAGS = os.path.join(ROOT, "work", "tags.txt")

def load_tags():
    tags = []
    if not os.path.exists(TAGS):
        return tags
    for line in open(TAGS, encoding="utf-8"):
        if line.strip() and not line.startswith("#"):
            tags.append(line.split("\t")[0].strip())
    return tags

def main():
    import pymupdf
    doc = pymupdf.open(PDF)
    full = "".join(p.get_text("text") for p in doc)
    print("pages:", doc.page_count, "chars:", len(full))
    tags = load_tags()
    missing = [t for t in tags if f"({t})" not in full]
    print(f"tags: {len(tags)-len(missing)}/{len(tags)} present")
    if missing:
        print("  MISSING tags:", missing)
    for i in range(1, 7):
        ok = re.search(rf'第\s*{i}\s*章', full) is not None
        print(f"chapter {i}: {'OK' if ok else 'MISSING'}")
    figs = [l.split("\t")[0] for l in open(os.path.join(ROOT, "work", "figures.tsv"), encoding="utf-8").read().splitlines() if l and not l.startswith("#")]
    figmiss = [f for f in figs if re.search(rf'图\s*{re.escape(f)}', full) is None]
    print(f"figures: {len(figs)-len(figmiss)}/{len(figs)} present")
    if figmiss:
        print("  MISSING figs:", figmiss)
    for bad in ["\ufffd", "??"]:
        n = full.count(bad)
        if n: print(f"  suspicious {bad!r}: {n}")
    bad_fonts = set()
    for p in doc:
        for f in p.get_fonts(full=True):
            if f[1] == "" or "Type3" in (f[2] or ""):
                bad_fonts.add(f[3])
    print("non-embedded/Type3 fonts:", bad_fonts if bad_fonts else "none")
    # 章标题出现页
    doc.close()
    return 0

if __name__ == "__main__":
    sys.exit(main())
