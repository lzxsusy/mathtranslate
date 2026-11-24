# -*- coding: utf-8 -*-
r"""Find untranslated English prose inside the Chinese TeX chapters.

Heuristic: strip math ($...$, \[...\], equation envs), strip TeX commands/braces,
then look for runs of >=5 ASCII words (letters only, at least 4 of them lowercase-length>=3).
Legitimate leftovers: proper names, titles of cited works, English terms kept on purpose.
The report lists them so a human can judge; Chinese content is the norm.
"""
import os, re, io

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(os.path.dirname(BASE), '..', '\u6e90\u7801', 'chapters')

def strip_tex(txt):
    txt = re.sub(r'\\begin\{(equation\*?|align\*?|gather\*?|eqnarray\*?)\}.*?\\end\{\1\}', ' ', txt, flags=re.S)
    txt = re.sub(r'\\\[.*?\\\]', ' ', txt, flags=re.S)
    txt = re.sub(r'\$\$.*?\$\$', ' ', txt, flags=re.S)
    txt = re.sub(r'(?<!\\)\$[^$]*\$', ' ', txt)
    txt = re.sub(r'\\(begin|end)\{[^}]*\}(\[[^\]]*\])?', ' ', txt)
    txt = re.sub(r'\\[a-zA-Z]+\*?', ' ', txt)
    txt = re.sub(r'[{}\\]', ' ', txt)
    return txt

WORD = re.compile(r'[A-Za-z][A-Za-z\'\-]{2,}')
CJK = re.compile(r'[\u4e00-\u9fff]')

lines = []
total = 0
for i in range(1, 13):
    nn = '%02d' % i
    path = os.path.join(SRC, 'ch%s.tex' % nn)
    raw = io.open(path, encoding='utf-8').read().split('\n')
    hits = []
    for no, line in enumerate(raw, 1):
        s = strip_tex(line)
        # split into candidate sentences
        for chunk in re.split(r'[。；：、，（）“”「」]', s):
            words = WORD.findall(chunk)
            if len(words) >= 5 and sum(1 for w in words if w[0].islower() and len(w) >= 3) >= 3:
                hits.append((no, ' '.join(words)[:200]))
    # dedupe by line
    seen = set()
    uniq = []
    for no, t in hits:
        if no in seen:
            continue
        seen.add(no)
        uniq.append((no, t))
    total += len(uniq)
    lines.append('CH %s: %d candidate lines' % (nn, len(uniq)))
    for no, t in uniq:
        lines.append('   L%d: %s' % (no, t))

io.open(os.path.join(BASE, 'english_leftovers.txt'), 'w', encoding='utf-8').write('\n'.join(lines))
print('total candidate lines:', total)
