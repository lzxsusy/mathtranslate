# -*- coding: utf-8 -*-
"""术语全局修正（Lead 执行，只跑一次）：圆分域→分圆域，投有限→射有限。
同时更新 terminology.tsv。备份到 work/backup_chapters/。
"""
import glob, os, shutil, io

WORK = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(WORK)
SRC = os.path.join(ROOT, 'src')
BAK = os.path.join(ROOT, 'work', 'backup_chapters')
os.makedirs(BAK, exist_ok=True)

FIX = [('圆分域', '分圆域'), ('投有限', '射有限')]

files = sorted(glob.glob(os.path.join(SRC, 'chapters', '*.tex')))
total = {}
for f in files:
    t = io.open(f, encoding='utf-8').read()
    orig = t
    for a, b in FIX:
        c = t.count(a)
        if c:
            total[a] = total.get(a, 0) + c
            t = t.replace(a, b)
    if t != orig:
        shutil.copy2(f, os.path.join(BAK, os.path.basename(f)))
        io.open(f, 'w', encoding='utf-8').write(t)
        print('fixed', os.path.basename(f))
print('counts', total)

# terminology.tsv
tp = os.path.join(SRC, 'terminology.tsv')
t = io.open(tp, encoding='utf-8').read()
for a, b in FIX:
    t = t.replace(a, b)
add = []
if 'cyclotomic field' not in t:
    add.append('cyclotomic field\t分圆域')
if add:
    if not t.endswith('\n'):
        t += '\n'
    t += '\n'.join(add) + '\n'
shutil.copy2(tp, os.path.join(BAK, 'terminology.tsv'))
io.open(tp, 'w', encoding='utf-8').write(t)
print('terminology updated; added', add)
