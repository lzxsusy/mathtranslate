# -*- coding: utf-8 -*-
import re, sys, io
sys.stdout.reconfigure(encoding='utf-8')
BS = "\\"

# 1) preamble: backsection 加 \phantomsection
p = r"<本地路径>"
t = open(p, encoding="utf-8").read()
if "<本地路径>" not in t:
    t = t.replace("\\addcontentsline{toc}{section}{#1}\\markright{#1}",
                  "<本地路径>")
    open(p, "w", encoding="utf-8", newline="\n").write(t)
    print("preamble patched")
else:
    print("preamble already ok")

# 2) kaisetsu 章节锚点
p = r"<本地路径>"
t = open(p, encoding="utf-8").read()
if "\\phanchapter" in t:
    pass
t = t.replace("\\chapter*{监译者解说}\n\\addcontentsline",
              "\\chapter*{监译者解说}\n<本地路径>")
open(p, "w", encoding="utf-8", newline="\n").write(t)
print("kaisetsu phantomsection:", "\\phantomsection" in t)

# 3) gen_notes.py: chapter 正则支持可选短标题；译校批注加 phantomsection
p = r"<本地路径>"
t = open(p, encoding="utf-8").read()
t = t.replace('CHAP_RE = re.compile(r\'\\<本地路径>*?\\{([^}]*)\\}\')',
              'CHAP_RE = re.compile(r\'\\<本地路径>*?(?:\\[[^\\]]*\\])?\\{([^}]*)\\}\')')
t = t.replace('"\\\\chapter*{译校批注}",\n             "\\\\addcontentsline',
              '"\\\\chapter*{译校批注}",\n             "\\<本地路径>')
open(p, "w", encoding="utf-8", newline="\n").write(t)
print("gen_notes patched:", "(?:\\[" in t, "phantomsection" in t)
