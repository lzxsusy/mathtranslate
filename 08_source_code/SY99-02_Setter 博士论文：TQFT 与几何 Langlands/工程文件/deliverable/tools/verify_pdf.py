# -*- coding: utf-8 -*-
r"""成品 PDF 回读验证（编译通过 ≠ 内容对）。用法：python tools/verify_pdf.py [main.pdf] [渲染页号,...]
检查：
  1. 57 条编号公式是否都出现在 PDF 文本中
  2. 图 1.1、2.1、4.1–4.7、6.1 的图注是否存在；参考文献 64 条
  3. 页数、字体是否嵌入
  4. 异常文本（??、Undefined、\tag、MISSING、TODO、**）
  5. 目录结构（章/节）与前 20 条书签
  6. 可选：渲染指定页 PNG 供目视
"""
import sys, re, io, os
sys.stdout.reconfigure(encoding="utf-8")
import pymupdf

ROOT = r"<本地路径>"
PDF = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "src", "main.pdf")

doc = pymupdf.open(PDF)
print("pages:", len(doc))
full = "\n".join(p.get_text() for p in doc)

expected = []
seen = set()
for ln in io.open(os.path.join(ROOT, "tags.txt"), encoding="utf-8"):
    t = ln.strip().split("\t")[0]
    if t and not t.startswith("#") and t not in seen:
        seen.add(t)
        expected.append(t)

print(f"\n1) 编号公式：期望 {len(expected)} 条")
missing = []
for t in expected:
    # 编号可能被抽成 "(1.1)"，也可能在行内被空格分开；宽松处理
    if f"({t})" not in full:
        missing.append(t)
print("   PDF 文本中缺失:", missing if missing else "无")

print("\n2) 图注 / 参考文献：")
for fig in ("1.1", "2.1", "4.1", "4.2", "4.3", "4.4", "4.5", "4.6", "4.7", "6.1"):
    ok = re.search(rf"图\s*{re.escape(fig)}\s*[：:]", full) is not None
    print(f"   图 {fig}: {'OK' if ok else 'MISSING'}")
nref = len(re.findall(r"^\s*\[\d+\]", full, re.M))
print(f"   参考文献条目（行首 [N] 计数）: {nref}（原文 64 条）")

print("\n3) 字体嵌入：")
bad = set()
for p in doc:
    for f in p.get_fonts(full=True):
        name = f[3]
        if not re.match(r"^[A-Z]{6}\+", name) and f[2] not in ("Type1C",):
            bad.add(name)
print("   未嵌前缀字体:", sorted(bad)[:10] if bad else "无（全部子集嵌入）")

print("\n4) 异常文本：")
for pat in ("??", "Undefined", "\\tag", "MISSING", "TODO", "FIXME", "**"):
    n = full.count(pat)
    if n:
        print(f"   {pat!r}: {n} 次")

print("\n5) 目录（前 25 条）：")
for lvl, title, pg in doc.get_toc()[:25]:
    print(f"   {'  ' * (lvl - 1)}{title}  ...p{pg}")

render = []
if len(sys.argv) > 2:
    render = [int(x) for x in sys.argv[2].split(",") if x.strip()]
for pno in render:
    out = os.path.join(ROOT, "build", f"verify_p{pno}.png")
    doc[pno - 1].get_pixmap(dpi=110).save(out)
    print(f"   rendered p{pno} -> {out}")
