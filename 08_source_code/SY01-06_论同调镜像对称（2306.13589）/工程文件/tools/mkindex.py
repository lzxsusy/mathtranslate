# -*- coding: utf-8 -*-
"""Minimal makeindex replacement: produce <job>.ind from <job>.idx.

Supports: hierarchical entries via '!', explicit sort keys via '@',
deduplication and numeric page sorting.  Output uses the standard
\\item/\\subitem/\\subsubitem markup of LaTeX's theindex environment.
"""
import io, os, re, sys
from collections import defaultdict

WS = r"<本地路径>"
OUTDIR = os.path.join(WS, 'work', 'zh', 'out')
JOB = sys.argv[1] if len(sys.argv) > 1 else 'master'

IDX = os.path.join(OUTDIR, JOB + '.idx')
IND = os.path.join(WS, 'work', 'zh', JOB + '.ind')   # next to sources, so \input finds it

ENTRY = re.compile(r'\\indexentry\{(.*?)\}\{(\d*)\}', re.S)

def split_level(comp):
    """'sort@display' -> (sort, display)"""
    if '@' in comp:
        s, d = comp.split('@', 1)
        return s, d
    return comp, comp

def main():
    if not os.path.exists(IDX):
        print('no .idx at', IDX); return 1
    raw = io.open(IDX, encoding='utf-8').read()
    entries = defaultdict(set)          # tuple(display path) -> set(pages)
    sorts = {}
    for m in ENTRY.finditer(raw):
        key, page = m.group(1), m.group(2)
        key = key.split('|')[0]        # drop makeindex encapsulation (|hyperpage etc.)
        levels = key.split('!')
        disps, sk = [], []
        for comp in levels:
            s, d = split_level(comp)
            sk.append(s.strip().lower())
            disps.append(d.strip())
        t = tuple(disps)
        entries[t].add(page)
        sorts[t] = tuple(sk)

    # group: level1 -> [(sortkey_level1, disp1, {subpath: pages})]
    groups = defaultdict(list)
    for t, pages in entries.items():
        groups[sorts[t][0]].append((sorts[t], t, pages))

    lines = [r'\begin{theindex}']
    prev_letter = None
    for g in sorted(groups):
        letter = g[:1]
        if prev_letter is not None and letter != prev_letter:
            lines.append('  \\indexspace')
        prev_letter = letter
        # things directly at level 1
        direct = [x for x in groups[g] if len(x[1]) == 1]
        subs = [x for x in groups[g] if len(x[1]) > 1]
        # level-1 display: prefer the direct one, else derive from a subentry
        disp1 = direct[0][1][0] if direct else subs[0][1][0]
        pg = set()
        for x in direct:
            pg |= x[2]
        def pagestr(s):
            def k(p):
                try: return (0, int(p))
                except Exception: return (1, 0)
            return ', '.join(p for p in sorted(s, key=k) if p)
        item = r'\item ' + disp1
        if pg:
            item += ', ' + pagestr(pg)
        lines.append(item)
        for sk, t, pages in sorted(subs, key=lambda x: (x[0][1:], x[0])):
            prefix = r'\subitem' if len(t) == 2 else r'\subsubitem'
            lines.append('  ' + prefix + ' ' + t[1] + ', ' + pagestr(pages))
    lines.append(r'\end{theindex}')
    io.open(IND, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    print('wrote', IND, 'level1 groups:', len(groups), 'entries:', len(entries))
    return 0

if __name__ == '__main__':
    sys.exit(main())
