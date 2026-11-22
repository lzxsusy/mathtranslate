# -*- coding: utf-8 -*-
"""把 amsrefs 的 \\bib{key}{type}{...} 条目转成 thebibliography 环境。
用法：python bib2tex.py  → 写出 源码/chunks/ch18.tex
"""
import re, os, sys, io

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(os.path.dirname(HERE))   # 工程根
SRC = os.path.join(PROJ, '工程文件', 'work', 'src', 'ZhiweiYunPCMI.tex')
OUT = os.path.join(PROJ, '源码', 'chunks', 'ch18.tex')

text = io.open(SRC, encoding='utf-8').read()

# 抓 biblist 段
m = re.search(r'\\begin\{biblist\}(.*?)\\end\{biblist\}', text, re.S)
assert m, 'biblist not found'
body = m.group(1)


def split_fields(block):
    """把 {...} 字段拆成列表 [(name, value)]，支持嵌套括号。"""
    out = []
    i = 0
    n = len(block)
    while i < n:
        # 跳过空白与逗号
        while i < n and block[i] in ' \t\r\n,':
            i += 1
        if i >= n:
            break
        # 字段名
        j = block.find('=', i)
        if j < 0:
            break
        name = block[i:j].strip()
        k = j + 1
        while k < n and block[k] in ' \t\r\n':
            k += 1
        if k >= n or block[k] != '{':
            break
        # 匹配花括号
        depth = 0
        start = k
        while k < n:
            if block[k] == '{':
                depth += 1
            elif block[k] == '}':
                depth -= 1
                if depth == 0:
                    break
            k += 1
        val = block[start + 1:k]
        out.append((name, val))
        i = k + 1
    return out


def clean(s):
    s = s.replace('\n', ' ')
    s = re.sub(r'\s+', ' ', s).strip()
    # amsrefs 的 \MR 之类不要
    return s


def fmt_entry(key, typ, fields):
    d = {}
    authors = []
    nested = {}
    for name, val in fields:
        val = clean(val)
        if name == 'author':
            authors.append(val)
        elif name in ('book', 'conference'):
            nested[name] = val
        else:
            d[name] = val

    def sub(field, subfield):
        raw = nested.get(field, '') if field in nested else d.get(field, '')
        for nm, v in split_fields(raw):
            if nm == subfield:
                return clean(v)
        return ''

    def pick(name):
        v = d.get(name, '')
        if v:
            return v
        return sub('book', name)

    auth = ', '.join(authors) if authors else ''
    title = d.get('title', '')
    date = d.get('date', '')
    pages = d.get('pages', '')
    series = pick('series')
    volume = pick('volume')
    publisher = pick('publisher')
    journal = d.get('journal', '')
    number = d.get('number', '')
    conf_title = sub('conference', 'title')

    parts = []
    if auth:
        parts.append(auth)
    if title:
        parts.append('\\emph{%s}' % title)
    if journal:
        s = journal
        if volume:
            s += ' \\textbf{%s}' % volume
        if date:
            s += ' (%s)' % date
        if number:
            s += ', no. %s' % number
        if pages:
            s += ', %s' % pages
        parts.append(s)
    else:
        if conf_title:
            s = conf_title
            if series:
                s += ', ' + series
                if volume:
                    s += ' \\textbf{%s}' % volume
            parts.append(s)
        elif series:
            s = series
            if volume:
                s += ' \\textbf{%s}' % volume
            parts.append(s)
        if publisher:
            parts.append(publisher)
        if date:
            parts.append(date)
        if pages:
            parts.append(pages)

    out = '\\bibitem{%s} %s.\n' % (key, ', '.join([p for p in parts if p]))
    # 去掉末尾可能的 ".."
    out = out.replace('..\n', '.\n')
    return out


# 解析所有 \bib
entries = re.findall(r'\\bib\{([^}]*)\}\{([a-z]*)\}\{(.*?)\n\}', body, re.S)
print('entries:', len(entries))

lines = ['\\begin{thebibliography}{99}', '']
for key, typ, block in entries:
    lines.append(fmt_entry(key, typ, split_fields(block)))
lines.append('\\end{thebibliography}')
lines.append('')

io.open(OUT, 'w', encoding='utf-8').write('\n'.join(lines))
print('written', OUT)
