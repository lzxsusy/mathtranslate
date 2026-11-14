# -*- coding: utf-8 -*-
"""从 chapters/lectureNN.tex 里抽出所有 \znote / \znoteplain，打印行号、等级、URL、修订日期。
用于 Lead 建 notes_NN.tsv 与审计，也可给施工员自查。
用法：python extract_notes.py 01   或   python extract_notes.py all
"""
import re, os, sys, glob

SRC = r'<本地路径>'

def parse(path):
    txt = open(path, encoding='utf-8').read()
    lines = txt.split('\n')
    out = []
    for i, ln in enumerate(lines, 1):
        for m in re.finditer(r'\\(znote|znoteplain)\{', ln):
            kind = m.group(1)
            # 取该命令的括号配对内容（可能跨行，这里只处理单行）
            j = m.end()
            depth = 1
            buf = []
            while j < len(ln) and depth:
                c = ln[j]
                if c == '{':
                    depth += 1
                elif c == '}':
                    depth -= 1
                    if depth == 0:
                        break
                buf.append(c)
                j += 1
            body = ''.join(buf)
            url = ''
            mu = re.search(r'\\url\{([^}]*)\}', body)
            if mu:
                url = mu.group(1)
            md = re.search(r'Last revised\s+(\d{4}-\d{2}-\d{2})', body)
            date = md.group(1) if md else ''
            # 来源等级
            if kind == 'znoteplain':
                level = 'I/译者按'
            elif 'nLab' in body:
                level = 'B/nLab'
            elif 'Stacks' in body:
                level = 'B/Stacks'
            elif 'MathWorld' in body:
                level = 'B/MathWorld'
            elif '来源：' in body:
                level = 'A/教材'
            else:
                level = '?无来源'
            out.append((i, kind, level, url, date, len(body), body[:60].replace('\n', ' ')))
    return out

def tutor_notes(path):
    txt = open(path, encoding='utf-8').read()
    res = []
    for i, ln in enumerate(txt.split('\n'), 1):
        s = ln.strip()
        if s.startswith('% [Tutor Note') or 'Tutor Note:' in s:
            res.append((i, s[:100]))
    return res

targets = sys.argv[1:] or ['all']
files = []
if targets == ['all']:
    files = sorted(glob.glob(os.path.join(SRC, 'lecture*.tex')))
else:
    for t in targets:
        files.append(os.path.join(SRC, 'lecture%s.tex' % t.zfill(2)))

for f in files:
    name = os.path.basename(f)
    zs = parse(f)
    ts = tutor_notes(f)
    print('=' * 70)
    print('%s : znote %d, znoteplain %d, tutor-note %d' % (
        name,
        sum(1 for z in zs if z[1] == 'znote'),
        sum(1 for z in zs if z[1] == 'znoteplain'),
        len(ts)))
    for (ln, kind, level, url, date, n, prev) in zs:
        print('  L%-4d %-11s %-11s %-22s %s' % (ln, kind, level, date, url or '(无URL)'))
        print('        %s...' % prev)
    for (ln, s) in ts:
        print('  L%-4d TUTOR %s' % (ln, s))
