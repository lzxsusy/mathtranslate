# -*- coding: utf-8 -*-
"""译稿 CJK 排版体检：汉字间多余空格、重复标点、混排可疑项。"""
import re
import glob
import sys
import os

CJK = r'[\u4e00-\u9fff]'
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(BASE)

files = sorted(glob.glob('源码/chunks/ch*.tex'))
pat_space = re.compile(CJK + r'[ \t]+' + CJK)
pat_dblpunct = re.compile(r'[，。、；：]{2,}')
pat_latin_gap = re.compile(CJK + r' +[A-Za-z]|[A-Za-z] +' + CJK)

out = []
for f in files:
    t = open(f, encoding='utf-8').read()
    for i, ln in enumerate(t.split('\n'), 1):
        if ln.lstrip().startswith('%'):
            continue
        for m in pat_space.finditer(ln):
            out.append((f, i, 'CJK_SPACE', ln[max(0, m.start() - 14):m.end() + 14]))
        for m in pat_dblpunct.finditer(ln):
            out.append((f, i, 'DBLPUNCT', ln[max(0, m.start() - 16):m.end() + 12]))

report = os.path.join(BASE, '工程文件', 'work', 'lint_cjk.txt')
with open(report, 'w', encoding='utf-8') as fh:
    fh.write('共 %d 条\n' % len(out))
    for f, i, k, c in out:
        fh.write('%s:%d\t%s\t%s\n' % (f, i, k, c))
print('FOUND', len(out))
for f, i, k, c in out[:80]:
    print('%s:%d\t%s\t%s' % (f, i, k, c))
