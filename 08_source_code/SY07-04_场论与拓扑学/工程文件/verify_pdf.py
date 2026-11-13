# -*- coding: utf-8 -*-
"""Gate 3 成品 PDF 回读：tag 是否全部出现 / 章标题 / 图题 / 字体嵌入 / 异常字符"""
import os, re, sys

ROOT = r"<本地路径>"
PDF = os.path.join(ROOT, "src", "main.pdf")
TAGS = os.path.join(ROOT, "work", "tags.txt")
FIGS = os.path.join(ROOT, "work", "figures.tsv")

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
    # 章标题（不含数字的模糊匹配）
    chapters = ["共形场理论的几何", "Jones", "Witten 理论", "Chern", "Simons 微扰理论"]
    for c in chapters:
        ok = c in full
        print(f"chapter/key {c!r}: {'OK' if ok else 'MISSING'}")
    # 图
    if os.path.exists(FIGS):
        figs = []
        for l in open(FIGS, encoding="utf-8"):
            if l.strip() and not l.startswith("#"):
                figs.append(l.split("\t")[0].strip())
        figmiss = [f for f in figs if re.search(rf'图\s*{re.escape(f)}', full) is None]
        print(f"figures: {len(figs)-len(figmiss)}/{len(figs)} present")
        if figmiss:
            print("  MISSING figs:", figmiss)
    # 异常文本
    for bad in ["\ufffd", "??"]:
        n = full.count(bad)
        if n:
            print(f"  suspicious {bad!r}: {n}")
    # 残留日文假名（整段未译的迹象）
    kana = len(re.findall(r'[\u3040-\u309f\u30a0-\u30ff]', full))
    print("  kana chars in PDF:", kana)
    bad_fonts = set()
    for p in doc:
        for f in p.get_fonts(full=True):
            if f[1] == "" or "Type3" in (f[2] or ""):
                bad_fonts.add(f[3])
    print("non-embedded/Type3 fonts:", bad_fonts if bad_fonts else "none")
    doc.close()
    return 0

if __name__ == "__main__":
    sys.exit(main())
