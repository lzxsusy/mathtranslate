# -*- coding: utf-8 -*-
import re, glob, io
CJK = r"\u4e00-\u9fff"
def strip(t):
    t = re.sub(r"\\\[.*?\\\]", " ", t, flags=re.S)
    t = re.sub(r"\$[^$]*\$", " ", t, flags=re.S)
    t = re.sub(r"\\begin\{(tikzcd|aligned|equation\*?|align\*?)\}.*?\\end\{\1\}", " ", t, flags=re.S)
    t = re.sub(r"\\[a-zA-Z@]+\*?", " ", t)
    t = re.sub(r"[{}\\]", " ", t)
    return t
out = []
for f in sorted(glob.glob("s*.tex")):
    lines = io.open(f, encoding="utf-8").read().split("\n")
    for i, ln in enumerate(lines, 1):
        s = strip(ln).strip()
        for p in re.split(r"[。！？；]", s):
            n = len(re.findall("[" + CJK + "]", p))
            if n > 70:
                out.append(f"{f}:{i} [{n}] {p.strip()[:120]}")
io.open(r"C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-45_Scholze布尔巴基1252几何Langlands的证明\工程文件\work\longsents.txt", "w", encoding="utf-8").write("\n".join(out))
print(len(out))
