# -*- coding: utf-8 -*-
"""自动补齐 macros.tex：从 chk_*.log 里读出「Undefined control sequence」的宏名，
   到 src_orig/glshort.tex（全文，含正文中段 \def）里找定义，抽取后追加到 macros.tex。
   找不到定义的列出来，人工写 shim。
   用法： python tools/autofix_macros.py
"""
import io, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'src_orig', 'glshort.tex')
MAC = os.path.join(ROOT, 'macros.tex')


def undefined_names():
    names = []
    for f in sorted(os.listdir(ROOT)):
        if not (f.startswith('chk_') and f.endswith('.log')):
            continue
        s = io.open(os.path.join(ROOT, f), encoding='utf-8', errors='replace').read().replace('\r', '')
        for m in re.finditer(r'<recently read> \\([A-Za-z@]+)', s):
            names.append(m.group(1))
    seen, out = set(), []
    for n in names:
        if n not in seen:
            seen.add(n)
            out.append(n)
    return out


def balanced(s, i):
    """s[i] == '{' -> 返回匹配 '}' 之后的下标"""
    d = 0
    j = i
    while j < len(s):
        c = s[j]
        if c == '\\':
            j += 2
            continue
        if c == '{':
            d += 1
        elif c == '}':
            d -= 1
            if d == 0:
                return j + 1
        j += 1
    raise ValueError('unbalanced')


def find_def(src, name):
    """返回 def 语句的完整文本（参数文本 + 花括号体），找不到返回 None"""
    pat = re.compile(r'\\(?:def|gdef|edef|xdef)\s*\\' + re.escape(name) + r'(?![A-Za-z])')
    m = pat.search(src)
    if not m:
        return None
    i = m.end()
    # 跳过空白/可选的参数文本，直到遇到第一层 '{'
    j = i
    while j < len(src) and src[j] not in '{':
        if src[j] == '\\':
            j += 2 if j + 1 < len(src) and not src[j + 1].isalpha() else 1
            while j < len(src) and src[j].isalpha():
                j += 1
            continue
        j += 1
    if j >= len(src):
        return None
    end = balanced(src, j)
    return src[m.start():end]


def main():
    src = io.open(SRC, encoding='utf-8').read()
    mac = io.open(MAC, encoding='utf-8').read()
    names = undefined_names()
    if not names:
        print('no undefined macro in chk logs')
        return
    added, missing = [], []
    for n in names:
        if re.search(r'\\(?:def|gdef|edef|xdef)\s*\\' + re.escape(n) + r'(?![A-Za-z])', mac):
            continue
        d = find_def(src, n)
        if d and len(d) < 3000:
            mac += '\n' + d + '   %% [autofix]'
            added.append(n)
        else:
            missing.append(n)
    if added:
        io.open(MAC, 'w', encoding='utf-8').write(mac + '\n')
    print('added:', added)
    print('missing (需手写 shim):', missing)


if __name__ == '__main__':
    main()
