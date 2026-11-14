# -*- coding: utf-8 -*-
"""建 nLab 全站条目名索引：work/nlab/_allpages.txt（一行一个 slug）
再提供本地模糊查找：python nlab_index.py <关键词>   → 打印含该词的 slug
"""
import urllib.request, re, sys, os, html

UA = {'User-Agent': 'Mozilla/5.0 (research; nlab-cache)'}
BASE = 'https://ncatlab.org/nlab/'
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'nlab', '_allpages.txt')


def build():
    t = urllib.request.Request(BASE + 'all_pages', headers=UA)
    with urllib.request.urlopen(t, timeout=120) as r:
        h = r.read().decode('utf-8', 'replace')
    print('html len', len(h))
    slugs = []
    for m in re.finditer(r'href="/nlab/show/([^"#?]+)"', h):
        s = html.unescape(m.group(1))
        if s not in slugs:
            slugs.append(s)
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write('\n'.join(slugs))
    print('slugs', len(slugs), '->', OUT)


if __name__ == '__main__':
    if not os.path.exists(OUT) or '--rebuild' in sys.argv:
        build()
    if len(sys.argv) > 1 and sys.argv[1] != '--rebuild':
        kw = [w.lower() for w in sys.argv[1:] if not w.startswith('--')]
        slugs = open(OUT, encoding='utf-8').read().split('\n')
        hits = []
        for s in slugs:
            low = s.lower().replace('+', ' ').replace('_', ' ').replace('-', ' ')
            if all(k in low for k in kw):
                hits.append(s)
        print(len(hits), 'hits')
        for s in hits[:40]:
            print(' ', s)
