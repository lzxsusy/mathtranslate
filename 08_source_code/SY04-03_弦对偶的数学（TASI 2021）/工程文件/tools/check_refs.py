#!/usr/bin/env python
"""Cross-check generated s08-refs entries vs PDF text layer."""
import re
import sys
sys.path.insert(0, 'asi2204-zh/tools')
import gen_refs

pages = gen_refs.extract()
gen = {n: t for p in pages for n, t in pages[p]}

tl = {}
for p in range(77, 86):
    s = open(f'asi2204-zh/text/page-{p:02d}.txt', 'rb').read().decode('utf-8', 'replace').replace('\x0c', '')
    lines = [l.strip() for l in s.splitlines()]
    lines = [l for l in lines if l and l not in
             ('TASI Lectures on the Mathematics of String Dualities', 'Natalie M. Paquette', 'References')
             and not re.fullmatch(r'\d{1,2}', l)]
    body = re.sub(r' +', ' ', ' '.join(lines))
    for part in re.split(r'(?=\[\d{1,3}\]\s)', body):
        m = re.match(r'\[(\d{1,3})\]\s*(.*)$', part, re.S)
        if m:
            tl[int(m.group(1))] = m.group(2).strip()


def norm(s):
    for a, b in gen_refs.LIG.items():
        s = s.replace(a, b)
    s = s.replace('\u2019', "'").replace('\u2013', '--')
    s = s.replace('\\textbf{', '').replace('\\mathbf{Z}_2', 'Z2')
    s = s.replace('\\mathbf', '')
    s = re.sub(r'\$([^$]*)\$', r'\1', s)
    s = s.replace('$', '').replace('{', '').replace('}', '')
    return re.sub(r'\s+', ' ', s).strip()


bad = 0
for n in range(1, 152):
    a = norm(gen[n])
    b = norm(tl[n])
    if a != b:
        bad += 1
        print('DIFF', n)
        print('  G:', a)
        print('  T:', b)
print('total diffs', bad)
