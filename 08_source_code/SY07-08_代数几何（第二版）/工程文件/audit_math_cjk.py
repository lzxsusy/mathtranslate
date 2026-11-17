# -*- coding: utf-8 -*-
"""审计：1) 数学模式里的中日韩字符/标点  2) Overfull 定位（按 chunk 归属 main.log）"""
import glob, os, re, sys

SRC = r"C:\Users\admin\Desktop\数译发布\shuyi\translations\SY07-08\源码"
CJK = re.compile(r"[\u3000-\u303f\u4e00-\u9fff\uff00-\uffef]")

def strip_comments(s):
    out = []
    for line in s.split("\n"):
        # 去掉未转义的 %
        idx = None
        i = 0
        while i < len(line):
            if line[i] == "\\":
                i += 2
                continue
            if line[i] == "%":
                idx = i
                break
            i += 1
        out.append(line if idx is None else line[:idx])
    return "\n".join(out)

def segments(s):
    """返回 (kind, text, lineno)；kind: inline / display / env"""
    res = []
    # \[ ... \]
    for m in re.finditer(r"\\\[(.*?)\\\]", s, re.S):
        res.append(("display", m.group(1), s.count("\n", 0, m.start()) + 1))
    # equation/align/gather 环境
    for m in re.finditer(r"\\begin\{(equation\*?|align\*?|gather\*?|multline\*?|eqnarray\*?|tikzcd)\}(.*?)\\end\{\1\}", s, re.S):
        res.append(("env:" + m.group(1), m.group(2), s.count("\n", 0, m.start()) + 1))
    # inline $...$ （跳过 \$ 与 display 已覆盖部分较麻烦，这里只做逐行）
    for ln, line in enumerate(s.split("\n"), 1):
        # 去掉 \[ \] 单行
        for m in re.finditer(r"(?<!\\)\$(?!\$)([^$]*?)(?<!\\)\$", line):
            res.append(("inline", m.group(1), ln))
    return res

for f in sorted(glob.glob(os.path.join(SRC, "chunks", "c*.tex"))):
    s = strip_comments(open(f, encoding="utf-8").read())
    hits = []
    for kind, text, ln in segments(s):
        if kind.startswith("env:equation") or kind.startswith("env:align") or kind.startswith("env:gather") or kind == "tikzcd" or kind == "display":
            bad = CJK.findall(text)
            # \text{中文} 是合法的
            text2 = re.sub(r"\\text\{[^}]*\}", "", text)
            bad = CJK.findall(text2)
            if bad:
                hits.append((kind, ln, "".join(sorted(set(bad)))[:12], text.strip()[:70]))
        elif kind == "inline":
            text2 = re.sub(r"\\text\{[^}]*\}", "", text)
            bad = CJK.findall(text2)
            if bad and any(c in text2 for c in "，。；：、（）「」"):
                hits.append((kind, ln, "".join(sorted(set(bad)))[:12], text.strip()[:70]))
    if hits:
        print(f"\n### {os.path.basename(f)}  ({len(hits)} 处)")
        for kind, ln, bad, txt in hits[:20]:
            print(f"  L{ln:5d} [{kind}] 字符={bad} :: {txt}")
