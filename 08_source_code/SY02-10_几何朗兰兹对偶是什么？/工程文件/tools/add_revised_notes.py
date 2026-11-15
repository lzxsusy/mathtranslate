# -*- coding: utf-8 -*-
"""notes.tex：给附录 12 条译注补 last_revised；更新对照表说明句。"""
p = r'<HOME>\Downloads\GL_work\源码\chunks\notes.tex'
s = open(p, encoding='utf-8').read()

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

n = 0
for slug, date in DATES.items():
    frag = slug.replace('+', '+\u200b\\allowbreak ')
    if frag not in s:
        print('  miss', slug)
        continue
    if '最后修订' in s:
        # 已处理过的行跳过
        pass
    j = s.find(frag)
    k = s.find('}}）。', j)
    if k < 0:
        print('  !! no tail', slug)
        continue
    s = s[:k + 2] + '，最后修订 ' + date + s[k + 2:]
    n += 1

old = '下表把文中反复出现、且 nLab 上有专门词条的概念集中列出，供读者按图索骥（词条可访问性核对于 2026 年 11 月，均为 B 级来源）。'
new = ('下表把文中反复出现、且 nLab 上有专门词条的概念集中列出，供读者按图索骥（均为 B 级来源；'
       '可访问性核对于 2026 年 11 月，修订日期取自本机 \\texttt{07\\_refs\\_nlab} 缓存，抓取于 2026-11-15）。'
       'nLab 无独立词条的概念（如 opers、分歧情形）此处不作强行对应。')
if old in s:
    s = s.replace(old, new)
    print('intro updated')

open(p, 'w', encoding='utf-8', newline='\n').write(s)
print('dates inserted:', n)
