# -*- coding: utf-8 -*-
"""给 12 条 nLab 译注补上词条的 last_revised（取自 07_refs_nlab 缓存抓取结果）。"""
import os, re, sys

CH = r'<HOME>\Downloads\GL_work\源码\chunks'
DATES = {
    'Tannaka+duality': '2025-07-28',
    'Langlands+dual+group': '2014-09-07',
    'S-duality': '2026-09-18',
    'Kapustin-Witten+TQFT': '2026-09-28',
    'six+operations': '2026-09-30',
    'Weil+uniformization+theorem': '2023-04-04',
    'geometric+class+field+theory': '2025-05-11',
    'ind-coherent+sheaves': '2015-10-05',
    'factorization+homology': '2026-05-30',
    'geometric+Satake+equivalence': '2024-07-22',
    'geometric+Langlands+correspondence': '2026-04-11',
    'relative+Langlands+program': '2025-04-29',
}

def pat(slug):
    return slug.replace('+', r'+\allowbreak{}')

total = 0
for fn in ('ch1.tex', 'ch2.tex', 'ch3.tex', 'ch4.tex', 'ch5.tex'):
    p = os.path.join(CH, fn)
    lines = open(p, encoding='utf-8').read().split('\n')
    changed = 0
    for i, line in enumerate(lines):
        if 'ncatlab' not in line:
            continue
        for slug, date in DATES.items():
            frag = pat(slug)
            if frag not in line:
                continue
            if '最后修订' in line:      # 已经加过
                continue
            # 该 slug 之后第一处 "}}。"（href 结束 + 句号）
            j = line.find(frag)
            k = line.find('}}。', j)
            if k < 0:
                print('  !! 找不到结束位置', fn, i + 1, slug)
                continue
            ins = '（最后修订 %s）' % date
            # 把 "}}。" 拆成 "}}" + ins + "。"
            line = line[:k + 2] + ins + line[k + 2:]
            lines[i] = line
            changed += 1
            total += 1
    if changed:
        open(p, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines))
        print('%s: +%d' % (fn, changed))
print('total', total)
