# -*- coding: utf-8 -*-
"""把正文里的 U+2013/U+2014 换成 LaTeX 的 --/---（ctex 会把 U+2013 当全角标点处理，
   造成「Jones – Witten」这类怪异间距）。只在文本层替换；统计每条替换数。
   注意：若 U+2013 出现在数学模式或文件名中会误伤，先打印上下文供核对。"""
import os, re, sys

CH = r"<本地路径>"
DRY = "--apply" not in sys.argv

total = {}
for f in sorted(os.listdir(CH)):
    if not f.endswith(".tex"):
        continue
    p = os.path.join(CH, f)
    t = open(p, encoding="utf-8").read()
    n13 = t.count("\u2013")
    n14 = t.count("\u2014")
    if n13 or n14:
        # 打印上下文（各前 3 例）
        for ch in ("\u2013", "\u2014"):
            for m in list(re.finditer(re.escape(ch), t))[:3]:
                a = t[max(0, m.start()-25):m.start()]
                b = t[m.end():m.end()+25]
                print(f"  {f}: ...{a!r}[{hex(ord(ch))}]{b!r}")
        t2 = t.replace("\u2013", "--").replace("\u2014", "---")
        total[f] = (n13, n14)
        if not DRY:
            open(p, "w", encoding="utf-8").write(t2)
print("files:", len(total), "U+2013:", sum(v[0] for v in total.values()),
      "U+2014:", sum(v[1] for v in total.values()))
print("DRY-RUN" if DRY else "APPLIED")
