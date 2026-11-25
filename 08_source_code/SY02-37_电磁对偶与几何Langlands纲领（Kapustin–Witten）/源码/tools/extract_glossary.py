# -*- coding: utf-8 -*-
"""从解经本 40_layer3_terms.tex 的术语表抽取 GLOSSARY.tsv（英文/中文/一句话/首现/易混）。"""
import io
import re
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = r"C:\Users\admin\Desktop\数译发布\gitee_shuyi\05_seminar_witten\seminars\SEM-0604151\manuscript\sections\40_layer3_terms.tex"

s = io.open(SRC, encoding='utf-8').read()
a = s.find('\\subsection{术语表}')
b = s.find('\\subsection{', a + 10)
seg = s[a:b]

rows = []
group = ''
for line in seg.splitlines():
    t = line.strip()
    if not t or t.startswith('%') or t.startswith('\\'):
        m = re.match(r'\\multicolumn\{5\}\{@\{\}l\}\{\\tabhead\{(.*?)\}\}', t)
        if m:
            group = m.group(1).replace('\\quad', ' ').replace('\\\\', '')
        continue
    if ' & ' not in t:
        continue
    t = t.rstrip().rstrip('\\').strip()
    cells = [c.strip() for c in t.split(' & ')]
    if len(cells) < 5:
        continue

    def clean(x):
        for k, v in (('\\S', '§'), ('\\ii', 'i'), ('\\dd', 'd'), ('\\CC', 'ℂ'),
                     ('\\ZZ', 'ℤ'), ('\\RR', 'ℝ'), ('\\MH', 'M_H'), ('\\MC', 'M_C'),
                     ('\\Ldual', 'L_G'), ('\\Dmod', 'D'), ('\\gC', 'g_C'),
                     ('\\LdualC', 'L_{G,ℂ}'), ('\\bm', '')):
            x = x.replace(k, v)
        return re.sub(r'\s+', ' ', x).strip()

    rows.append([clean(group)] + [clean(c) for c in cells])

out = os.path.join(ROOT, 'brief', 'GLOSSARY.tsv')
with io.open(out, 'w', encoding='utf-8') as f:
    f.write('组\t英文\t中文\t一句话定义\t首现\t易混淆点\n')
    for r in rows:
        f.write('\t'.join(r) + '\n')
print('rows', len(rows), '->', out)
