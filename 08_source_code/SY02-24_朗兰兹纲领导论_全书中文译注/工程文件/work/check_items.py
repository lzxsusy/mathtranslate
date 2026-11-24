# -*- coding: utf-8 -*-
r"""Numbered-statement parity: original (raw txt) vs TeX bold labels.
Original: 'Example 5.5.' / 'Lemma 6.1.' / 'Theorem 3.2.' at line starts.
TeX: \textbf{例 5.5} / \textbf{引理 6.1} / \textbf{定理 3.2} etc.
Also: subsection headings ('2.1 Title') vs \subsection, and footnote/annote counts."""
import os, re, io

BASE = os.path.dirname(os.path.abspath(__file__))
EN = os.path.join(BASE, 'en')
SRC = os.path.join(os.path.dirname(BASE), '..', '\u6e90\u7801', 'chapters')

EN_KINDS = r'Example|Lemma|Theorem|Proposition|Corollary|Remark|Definition|Claim|Problem|Question|Conjecture'
ZH_KINDS = r'\u4f8b|\u5f15\u7406|\u5b9a\u7406|\u547d\u9898|\u63a8\u8bba|\u6ce8|\u5b9a\u4e49|\u65ad\u8a00|\u95ee\u9898|\u731c\u60f3'

def key(s):
    a, b = s.split('.')
    return (int(a), int(b))

def raw_items(txt):
    got = {}
    for m in re.finditer(r'(?:^|\n)\s*(%s)\s+(\d{1,2})\.(\d{1,2})\.?' % EN_KINDS, txt):
        got['%s.%s' % (m.group(2), m.group(3))] = m.group(1)
    # also inline occurrences 'Lemma 6.1.' after sentence
    return got

def tex_items(txt):
    got = {}
    for m in re.finditer(r'\\textbf\{(%s)\s*(\d{1,2})\.(\d{1,2})\s*[.\uff0e]?\}' % ZH_KINDS, txt):
        got['%s.%s' % (m.group(2), m.group(3))] = m.group(1)
    for m in re.finditer(r'\\begin\{(othm|example|lemma|theorem|prop|cor|rem|defn)\}', txt):
        pass
    return got

lines = []
for i in range(1, 13):
    nn = '%02d' % i
    r = io.open(os.path.join(EN, 'ch%s_raw.txt' % nn), encoding='utf-8').read()
    t = io.open(os.path.join(SRC, 'ch%s.tex' % nn), encoding='utf-8').read()
    ri, ti = raw_items(r), tex_items(t)
    oraw = sorted(set(ri) - set(ti), key=key)
    otex = sorted(set(ti) - set(ri), key=key)
    lines.append('CH %s raw_items=%d tex_items=%d  only_raw=%d only_tex=%d'
                 % (nn, len(ri), len(ti), len(oraw), len(otex)))
    if oraw:
        lines.append('  only_raw: ' + ' '.join('%s(%s)' % (k, ri[k]) for k in oraw))
    if otex:
        lines.append('  only_tex: ' + ' '.join('%s(%s)' % (k, ti[k]) for k in otex))

io.open(os.path.join(BASE, 'items_report.txt'), 'w', encoding='utf-8').write('\n'.join(lines))
print('ok')
