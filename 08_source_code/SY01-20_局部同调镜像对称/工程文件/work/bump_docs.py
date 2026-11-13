import glob
import io
import os

D = r"<本地路径>"
subs = [
    ("80 页", "82 页"),
    ("996 KB", "1004 KB"),
    ("23 个概念框", "25 个概念框"),
    ("23 个概念回顾", "25 个概念回顾"),
]
for p in glob.glob(os.path.join(D, "*.md")):
    s = io.open(p, encoding="utf-8").read()
    t = s
    for a, b in subs:
        t = t.replace(a, b)
    if t != s:
        io.open(p, "w", encoding="utf-8").write(t)
        print("updated", os.path.basename(p))
