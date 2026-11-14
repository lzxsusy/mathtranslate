# -*- coding: utf-8 -*-
"""给 nLab 对照表加“最后修订”一列；并把 S-duality 段落里误插的一句撤掉。"""
import re

p = r'C:\Users\admin\Downloads\GL_work\源码\chunks\notes.tex'
s = open(p, encoding='utf-8').read()

# 1) 撤掉误插
s = s.replace('，最后修订 2026-09-18）', '）')

DATES = {
    'geometric+Langlands+correspondence': '2026-04-11',
    'geometric+Satake+equivalence': '2024-07-22',
    'Tannaka+duality': '2025-07-28',
    'Langlands+dual+group': '2014-09-07',
    'six+operations': '2026-09-30',
    'moduli+stack': '2023-04-16',
    'affine+Grassmannian': '2023-08-15',
    'Weil+uniformization+theorem': '2023-04-04',
    'geometric+class+field+theory': '2025-05-11',
    'D-module': '2024-07-27',
    'Riemann-Hilbert+correspondence': '2024-08-09',
    'Hecke+eigensheaf': '—',
    'ind-coherent+sheaves': '2015-10-05',
    'factorization+algebra': '2026-08-16',
    'factorization+homology': '2026-05-30',
    'Hitchin+fibration': '2023-11-01',
    'Kapustin-Witten+TQFT': '2026-09-28',
    'S-duality': '2026-09-18',
    'Fargues-Fontaine+curve': '2022-07-04',
    'function+field+analogy': '2024-06-03',
    'quantum+geometric+Langlands+correspondence': '2026-04-06',
    'Kac-Moody+algebra': '2026-11-06',
    'Eisenstein+series': '2014-03-26',
    'Whittaker+function': '2023-06-14',
    'automorphic+form': '2026-09-09',
    'Langlands+program': '2024-03-28',
    'perverse+sheaf': '2026-10-16',
    'chiral+algebra': '2026-11-02',
    'Beilinson-Drinfeld+algebra': '2022-10-18',
    'characteristic+variety': '2017-08-29',
}

def norm(cell):
    c = cell.replace('\u200b', '').replace('\\allowbreak{}', '').replace('\\allowbreak', '')
    return re.sub(r'\s+', '', c)

# 2) 表头：三列 → 四列
s = s.replace(
    r'\begin{longtable}{@{}>{\raggedright\arraybackslash}p{0.30\linewidth}>{\raggedright\arraybackslash}p{0.28\linewidth}>{\raggedright\arraybackslash}p{0.34\linewidth}@{}}',
    r'\begin{longtable}{@{}>{\raggedright\arraybackslash}p{0.28\linewidth}>{\raggedright\arraybackslash}p{0.26\linewidth}>{\raggedright\arraybackslash}p{0.09\linewidth}>{\raggedright\arraybackslash}p{0.26\linewidth}@{}}')
s = s.replace('概念（中／英） & nLab 词条（URL 末段） & 在文中的位置与作用 \\\\',
              '概念（中／英） & nLab 词条（URL 末段） & 最后修订 & 在文中的位置与作用 \\\\')

# 3) 数据行：插一列
out = []
hit = 0
for line in s.split('\n'):
    if line.rstrip().endswith('\\\\') and line.count('&') == 2:
        a, b, c = [x.strip() for x in line.rstrip()[:-2].split('&')]
        slug = norm(b)
        date = DATES.get(slug)
        if date is None:
            print('  unknown slug:', slug)
            date = '—'
        out.append('%s & %s & %s & %s \\\\' % (a, b, date, c))
        hit += 1
    else:
        out.append(line)

open(p, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
print('rows updated:', hit)
