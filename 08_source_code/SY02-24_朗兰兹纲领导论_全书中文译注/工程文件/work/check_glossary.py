# -*- coding: utf-8 -*-
r"""Cross-check glossary.tsv (English<TAB>Chinese) against ch99_glossary.tex longtable rows,
and report how often each Chinese term actually occurs in ch01..ch12."""
import os, re, io, glob

BASE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(os.path.dirname(BASE))
SRC = os.path.join(PROJ, '\u6e90\u7801', 'chapters')

tsv = {}
for line in io.open(os.path.join(os.path.dirname(BASE), 'glossary.tsv'), encoding='utf-8'):
    line = line.rstrip('\r\n')
    if not line or line.startswith('\u672f\u8bed'):  # header 术语
        continue
    parts = line.split('\t')
    if len(parts) >= 2 and parts[0].strip():
        tsv[parts[0].strip().lower()] = parts[1].strip()

texrows = {}
gtxt = io.open(os.path.join(SRC, 'ch99_glossary.tex'), encoding='utf-8').read()
for m in re.finditer(r'^(.*?)\s*&\s*(.*?)\s*\\\\\s*$', gtxt, flags=re.M):
    en, zh = m.group(1).strip(), m.group(2).strip()
    texrows[en.lower()] = zh

lines = []
lines.append('tsv entries: %d ; tex rows: %d' % (len(tsv), len(texrows)))
lines.append('--- only in TSV ---')
for k in sorted(set(tsv) - set(texrows)):
    lines.append('  %s -> %s' % (k, tsv[k]))
lines.append('--- only in TEX ---')
for k in sorted(set(texrows) - set(tsv)):
    lines.append('  %s -> %s' % (k, texrows[k]))
lines.append('--- Chinese mismatch for same English ---')
for k in sorted(set(tsv) & set(texrows)):
    if tsv[k] != texrows[k]:
        lines.append('  %s : tsv=%s | tex=%s' % (k, tsv[k], texrows[k]))

# occurrence counts of each tex glossary Chinese term in chapters
chap = {}
for i in range(1, 13):
    nn = '%02d' % i
    chap[nn] = io.open(os.path.join(SRC, 'ch%s.tex' % nn), encoding='utf-8').read()
lines.append('--- terms whose Chinese never appears in any chapter body ---')
for en, zh in sorted(texrows.items()):
    core = re.sub(r'[\s/／，、（）()]', '', zh)
    if len(core) < 2:
        continue
    hits = sum(t.count(zh) for t in chap.values())
    if hits == 0:
        lines.append('  %s -> %s (0)' % (en, zh))

io.open(os.path.join(BASE, 'glossary_check.txt'), 'w', encoding='utf-8').write('\n'.join(lines))
print('ok', len(tsv), len(texrows))
