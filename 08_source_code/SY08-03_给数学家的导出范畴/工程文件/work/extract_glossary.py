# -*- coding: utf-8 -*-
"""从 90_appendix.tex 的附录 A 抽术语表 -> work/glossary.tsv"""
import re, io, os

REF = {
    'sec:intro': '1', 'sec:cx': '2', 'sec:qi': '3', 'sec:cat': '4',
    'sec:cone': '5', 'sec:df': '6',
    'def:additive': '4.1', 'def:db': '4.2', 'rem:four': '4.3',
    'def:adapted': '6.1', 'eg:tor': '6.2', 'eg:rhom': '6.3',
    'eg:composition': '6.4', 'eg:duality': '6.5', 'eg:derham': '6.6',
    'tab:intersection': '1', 'fig:cone': '1', 'fig:doldpuppe': '2',
    'eq:co': '2.1', 'eq:div': '2.2', 'eq:wh': '2.3',
    'eq:dot': '3.1', 'eq:sp': '5.1', 'eq:les': '5.2',
    'fig:roof': '屋顶图',
}

src = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '源码', 'sections', '90_appendix.tex'))
text = open(src, encoding='utf-8').read()
block = text[text.index('\\section{术语对照表}'):text.index('\\section{校勘记}')]


def resolve(s):
    def rep(m):
        return REF.get(m.group(1), m.group(1))
    s = re.sub(r'\\(?:eq)?ref\{([^}]*)\}', rep, s)
    return s


def clean(s):
    s = resolve(s.strip())
    s = s.replace('\\ldots', '…').replace('$\\to$', '→').replace('$\\mapsto$', '↦')
    s = re.sub(r'\$([^$]*)\$', lambda m: m.group(1), s)
    s = s.replace('\\S', '§').replace('\\,', ' ').replace('\\ ', ' ')
    s = s.replace('\\texttt{', '').replace('\\emph{', '').replace('\\term{', '')
    s = s.replace('{', '').replace('}', '')
    s = s.replace('~', ' ')
    s = re.sub(r'\s+', ' ', s)
    return s.strip()


rows = []
for line in block.splitlines():
    if '&' not in line or 'multicolumn' in line or '中文' in line:
        continue
    if not line.rstrip().endswith('\\\\'):
        continue
    parts = line.rstrip().rstrip('\\').split('&')
    if len(parts) < 3:
        continue
    zh, en, first = clean(parts[0]), clean(parts[1]), clean(parts[2])
    if zh and en:
        rows.append((zh, en, first))

out = os.path.join(os.path.dirname(__file__), 'glossary.tsv')
with io.open(out, 'w', encoding='utf-8', newline='\n') as f:
    f.write('中文\t英文\t首次出现\n')
    for r in rows:
        f.write('\t'.join(r) + '\n')
print(len(rows), 'rows')
