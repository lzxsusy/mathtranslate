# -*- coding: utf-8 -*-
"""修 make_bib.py：允许 \bib{..}{type} 与 { 之间有空白；字段名大小写不敏感；
无期刊时用 eprint/url 渲染 “available at ...”。"""
import io
import os

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p = os.path.join(root, "scripts", "make_bib.py")
s = io.open(p, encoding="utf-8").read()

s = s.replace(r'r"\\bib\{([^}]*)\}\{([a-zA-Z]+)\}\{"',
              r'r"\\bib\{([^}]*)\}\s*\{([a-zA-Z]+)\}\s*\{"')
s = s.replace(r'for m in re.finditer(r"([a-z]+)=\{", body):',
              r'for m in re.finditer(r"([A-Za-z]+)\s*=\s*\{", body):')
s = s.replace('        name = m.group(1)', '        name = m.group(1).lower()')

# 在 article 分支尾部，若没有期刊信息则用 eprint/url 兜底
old = '''        if s2:
            parts.append(s2 + ".")'''
new = '''        if s2.strip():
            parts.append(s2 + ".")
        else:
            link = f.get("eprint", [""])[0] or f.get("url", [""])[0]
            if link:
                parts.append("available at %s." % link)'''
assert old in s
s = s.replace(old, new)
io.open(p, "w", encoding="utf-8", newline="\n").write(s)
print("patched")
