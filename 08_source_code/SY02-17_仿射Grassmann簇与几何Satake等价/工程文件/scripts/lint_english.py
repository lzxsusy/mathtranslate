# -*- coding: utf-8 -*-
"""扫译稿正文里残留的英文散文词（英文术语单靠 math 模式不算，这里只报散文词汇）。"""
import re
import glob
import os

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(BASE)

WORDS = [
    'strata', 'stratum', 'the', 'of', 'and', 'with', 'see', 'for', 'from', 'such',
    'that', 'this', 'these', 'those', 'we', 'is', 'are', 'be', 'by', 'on', 'in',
    'as', 'to', 'which', 'where', 'when', 'let', 'then', 'hence', 'thus', 'so',
    'proof', 'remark', 'example', 'definition', 'theorem', 'lemma', 'proposition',
    'corollary', 'if', 'only', 'not', 'note', 'also', 'same', 'case', 'general',
    'following', 'above', 'below', 'respectively', 'moreover', 'furthermore',
    'indeed', 'since', 'because', 'therefore', 'namely', 'i.e', 'e.g', 'cf',
    'cf.', 'resp', 'resp.', 'vs', 'vs.', 'via', 'mod', 'up', 'out', 'over',
    'under', 'onto', 'into', 'about', 'among', 'between', 'each', 'every', 'some',
    'any', 'all', 'no', 'one', 'two', 'first', 'second', 'last', 'next', 'previous',
    'above.', 'namely,', 'ind-scheme', 'torsor', 'lattice', 'sheaf', 'perverse',
]
pat = re.compile(r'(?<![A-Za-z\\{])(%s)(?![A-Za-z])' % '|'.join(re.escape(w) for w in WORDS))

hits = []
for f in sorted(glob.glob('源码/chunks/ch*.tex')):
    for i, ln in enumerate(open(f, encoding='utf-8').read().split('\n'), 1):
        if ln.lstrip().startswith('%'):
            continue
        # drop inline/display math crudely
        s = re.sub(r'\$[^$]*\$', ' ', ln)
        s = re.sub(r'\\\[[^\]]*\\\]', ' ', s)
        for m in pat.finditer(s):
            ctx = s[max(0, m.start() - 20):m.end() + 20]
            if re.search(r'[\u4e00-\u9fff]', ctx):
                hits.append((f, i, m.group(1), ctx))

out = os.path.join(BASE, '工程文件', 'work', 'lint_english.txt')
with open(out, 'w', encoding='utf-8') as fh:
    fh.write('共 %d 条\n' % len(hits))
    for f, i, w, c in hits:
        fh.write('%s:%d\t%s\t%s\n' % (f, i, w, c))
print('HITS', len(hits))
for h in hits[:60]:
    print('%s:%d\t%s\t%s' % h)
