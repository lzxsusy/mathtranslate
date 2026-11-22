# -*- coding: utf-8 -*-
"""统一「Archimedes 局部域」→「阿基米德局部域」（仓库主流译法，136 vs 11），并重编译核对页数。"""
import os
import re
import subprocess

BASE = r"C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code"
XEL = r"C:\Users\admin\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe"

projs = [
    ("SY02-16_算术与几何朗兰兹纲领", 34),
    ("SY02-17_仿射Grassmann簇与几何Satake等价", 89),
    ("SY02-18_shtuka及其模空间导论", 46),
]

for name, expect in projs:
    src = os.path.join(BASE, name, "源码")
    hits = []
    for root, _, files in os.walk(src):
        for fn in files:
            if fn.endswith(".tex"):
                p = os.path.join(root, fn)
                with open(p, encoding="utf-8") as f:
                    s = f.read()
                if "Archimedes" in s:
                    with open(p, "w", encoding="utf-8") as f:
                        f.write(s.replace("Archimedes", "阿基米德"))
                    hits.append(os.path.relpath(p, src))
    print(name, "edited:", hits)

    for _ in range(2):
        subprocess.run([XEL, "-interaction=nonstopmode", "main.tex"], cwd=src,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    log = open(os.path.join(src, "main.log"), encoding="utf-8", errors="ignore").read()
    m = re.search(r"Output written on main\.pdf \((\d+) pages", log)
    pages = int(m.group(1)) if m else -1
    bad = [l for l in log.splitlines() if l.startswith("!") or "Overfull" in l or "Missing character" in l]
    print("   pages=%d (expect %d) issues=%d" % (pages, expect, len(bad)))
