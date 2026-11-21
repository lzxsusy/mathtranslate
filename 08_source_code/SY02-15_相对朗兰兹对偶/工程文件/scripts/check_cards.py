# -*- coding: utf-8 -*-
"""检查资料卡里引用的编号是否都真实存在于 section_index（167 项）。"""
import io, json, os, re

os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
idx = json.load(io.open('工程文件/work/section_index.json', encoding='utf-8'))
labels = set(e['label'] for e in idx)
bynum = {}
for e in idx:
    bynum.setdefault(e['label'], e)

pat_eq = re.compile(r'\((\d{1,2}\.\d{1,2})\)')
pat_th = re.compile(r'(注|例|定义|定理|猜想|命题|引理|练习)\s*(\d{1,2}\.\d{1,2})')

bad = []
for fn in ['00-速览.md', '01-结果清单.md', '02-论证地图.md', '04-术语文献勘误.md']:
    t = io.open('资料卡/' + fn, encoding='utf-8').read()
    for m in pat_eq.finditer(t):
        lab = '(' + m.group(1) + ')'
        if lab not in labels:
            bad.append((fn, lab, t[max(0, m.start()-30):m.start()+10].replace('\n', ' ')))
    for m in pat_th.finditer(t):
        lab = '(' + m.group(2) + ')'
        if lab not in labels:
            bad.append((fn, m.group(0), t[max(0, m.start()-30):m.start()+10].replace('\n', ' ')))
        else:
            kind = bynum[lab]['kind']
            if kind != m.group(1):
                bad.append((fn, 'TYPE %s vs %s' % (m.group(0), kind),
                            t[max(0, m.start()-30):m.start()+10].replace('\n', ' ')))

out = io.open('工程文件/work/card_check.txt', 'w', encoding='utf-8')
out.write('labels=%d\n' % len(labels))
for b in bad:
    out.write('%s :: %s :: ...%s\n' % b)
out.write('bad=%d\n' % len(bad))
out.close()
print('done', len(bad))
