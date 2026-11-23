# -*- coding: utf-8 -*-
"""从 main.tex 生成 partial.tex：把所有 \\input{chunks/...} 包进 \\IfFileExists，
这样已完成的 chunk 可以先编译审校，缺片不报错。
用法: python build_partial.py
"""
import io, os, re

root = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(root, "..", "源码")
main = io.open(os.path.join(src, "main.tex"), encoding="utf-8").read()

def repl(m):
    path = m.group(1)
    return r"\IfFileExists{%s}{\input{%s}}{\relax}" % (path, path)

out = re.sub(r"\\input\{([^}]*)\}", repl, main)
io.open(os.path.join(src, "partial.tex"), "w", encoding="utf-8", newline="\n").write(out)
print("wrote partial.tex")
