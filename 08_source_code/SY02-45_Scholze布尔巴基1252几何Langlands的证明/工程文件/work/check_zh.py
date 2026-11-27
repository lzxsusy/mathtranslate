# -*- coding: utf-8 -*-
import re, glob, os, sys
base = r"C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-45_Scholze布尔巴基1252几何Langlands的证明\源码\sections"
files = sorted(glob.glob(os.path.join(base, "s*.tex")))
CJK = r"\u4e00-\u9fff"
def strip_math(s):
    s = re.sub(r"\\\[.*?\\\]", " ", s, flags=re.S)
    s = re.sub(r"\\\(.*?\\\)", " ", s, flags=re.S)
    s = re.sub(r"\$[^$]*\$", " ", s, flags=re.S)
    s = re.sub(r"\\begin\{(tikzcd|aligned|equation\*?|align\*?|array|matrix)\}.*?\\end\{\1\}", " ", s, flags=re.S)
    return s
def strip_cmds(s):
    # remove control words but keep their braces content
    s = re.sub(r"\\[a-zA-Z@]+\*?", " ", s)
    return s
for f in files:
    txt = open(f, encoding="utf-8").read()
    lines = txt.split("\n")
    for i, ln in enumerate(lines, 1):
        raw = ln
        if ln.strip().startswith("%"):
            continue
        s = strip_math(ln)
        s = strip_cmds(s)
        # CJK immediately adjacent to ASCII letter/digit
        for m in re.finditer(r"([" + CJK + r"])([A-Za-z0-9])", s):
            print(f"{os.path.basename(f)}:{i}: CJK|ASCII  {m.group(0)!r}  :: {raw.strip()[:90]}")
        for m in re.finditer(r"([A-Za-z0-9])([" + CJK + r"])", s):
            print(f"{os.path.basename(f)}:{i}: ASCII|CJK  {m.group(0)!r}  :: {raw.strip()[:90]}")
        # halfwidth punctuation between CJK
        for m in re.finditer(r"[" + CJK + r"]\s*([,;:!?])\s*[" + CJK + r"]", s):
            print(f"{os.path.basename(f)}:{i}: HALFPUNCT {m.group(0)!r} :: {raw.strip()[:90]}")
