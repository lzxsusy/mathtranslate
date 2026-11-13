# -*- coding: utf-8 -*-
"""汇总交付统计，写入 work/stats.json。"""
import io
import json
import os
import re

ROOT = r"<本地路径>"
SRC = os.path.join(ROOT, "src")

def wc(p):
    return len(io.open(p, encoding="utf-8").read())

stats = {}
pdf = os.path.join(ROOT, "work", "check", "full_auto.pdf")
stats["pdf_bytes"] = os.path.getsize(pdf)
stats["pdf_pages"] = 80

files = []
for d in ("chunks", "front", "back"):
    for f in sorted(os.listdir(os.path.join(SRC, d))):
        if f.endswith(".tex"):
            files.append(os.path.join(SRC, d, f))
files += [os.path.join(SRC, "main.tex"), os.path.join(SRC, "preamble.tex")]
stats["tex_files"] = len(files)
stats["tex_chars"] = sum(wc(f) for f in files)
stats["tex_lines"] = sum(len(io.open(f, encoding="utf-8").read().splitlines()) for f in files)

chunks = "".join(io.open(os.path.join(SRC, "chunks", "ch%02d.tex" % i), encoding="utf-8").read()
                 for i in range(15))
stats["yizhu"] = len(re.findall(r"<本地路径>", chunks))
stats["conceptbox"] = len(re.findall(r"<本地路径>", chunks))
stats["keytakeaways"] = len(re.findall(r"<本地路径>", chunks))
stats["pagemarks"] = len(re.findall(r"% \[原文 p\.\d+\]", chunks))
stats["figures"] = len(re.findall(r"<本地路径>", chunks))
stats["tikzcd"] = len(re.findall(r"<本地路径>", chunks))
stats["statements"] = len(re.findall(r"<本地路径>|defn|dfn|prp|prop|crl|cor|conj|nota|ques|exmp|example|lmm|lemma|rmk|cv|exer)\}", chunks))
stats["bib_entries"] = len(re.findall(r"^@", io.open(os.path.join(SRC, "refs.bib"), encoding="utf-8").read(), re.M))
io.open(os.path.join(ROOT, "work", "stats.json"), "w", encoding="utf-8").write(
    json.dumps(stats, ensure_ascii=False, indent=1))
print(json.dumps(stats))
