# -*- coding: utf-8 -*-
r"""Compare book section headings with TeX \section/\subsection titles, per chapter.
Writes a UTF-8 report to sections_report.txt (console is GBK -> avoid printing CJK)."""
import os, re, io

BASE = os.path.dirname(os.path.abspath(__file__))
EN = os.path.join(BASE, 'en')
SRC = os.path.join(os.path.dirname(BASE), '..', '\u6e90\u7801', 'chapters')

AUTHOR_HEAD = re.compile(r'^\d{1,2}\s+[A-Z]\.\s+[A-Z][a-z]+$')

def raw_sections(path):
    out = []
    txt = io.open(path, encoding='utf-8').read()
    for line in txt.split('\n'):
        if line.startswith('====='):
            continue
        s = line.strip()
        if AUTHOR_HEAD.match(s):
            continue
        m = re.match(r'^(\d{1,2})(?:\.(\d{1,2}))?\s+([A-Z][^\n]{2,70})$', s)
        if m:
            title = m.group(3)
            words = title.split()
            if title.endswith('.') or len(words) > 12:
                continue
            # require at least half the words to start with a capital or be short func words
            caps = sum(1 for w in words if w[:1].isupper())
            if caps * 2 < len(words):
                continue
            if re.search(r'[=\\]', title):
                continue
            out.append((m.group(1), m.group(2) or '', title))
    return out

def tex_sections(path):
    txt = io.open(path, encoding='utf-8').read()
    return [(m.group(1), m.group(2)) for m in
            re.finditer(r'\\(chapter|section|subsection)\*?\{([^}]*)\}', txt)]

def count_eq_raw(path):
    txt = io.open(path, encoding='utf-8').read()
    return sorted({(int(m.group(1)), int(m.group(2)))
                   for m in re.finditer(r'[\(\[ ](\d{1,2})\.(\d{1,2})\)', txt)})

def ob_ids(path):
    txt = io.open(path, encoding='utf-8').read()
    return [m.group(1) for m in re.finditer(r'\\ob\{([^}]*)\}\{', txt)]

lines = []
for i in range(1, 13):
    nn = '%02d' % i
    rp = os.path.join(EN, 'ch%s_raw.txt' % nn)
    tp = os.path.join(SRC, 'ch%s.tex' % nn)
    rs, ts, eqs, obs = raw_sections(rp), tex_sections(tp), count_eq_raw(rp), ob_ids(tp)
    lines.append('=' * 70)
    lines.append('CH %s : raw headings %d | tex sect %d | eq nums in raw %d (max %s) | \\ob ids %d'
                 % (nn, len(rs), len(ts), len(eqs),
                    max([e[1] for e in eqs]) if eqs else '-', len(obs)))
    lines.append('-- RAW headings --')
    for a, b, t in rs:
        lines.append('  %s%s %s' % (a, ('.' + b) if b else '', t))
    lines.append('-- TEX sections --')
    for kind, t in ts:
        lines.append('  [%s] %s' % (kind, t))
    lines.append('-- raw eq numbers --')
    lines.append('  ' + ' '.join('%d.%d' % e for e in eqs))
    lines.append('-- \\ob ids --')
    lines.append('  ' + ' '.join(obs))

io.open(os.path.join(BASE, 'sections_report.txt'), 'w', encoding='utf-8').write('\n'.join(lines))
print('written', len(lines), 'lines')
