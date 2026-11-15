# -*- coding: utf-8 -*-
"""把 tools/nlab 抓到的新页并入 pages/ 并重建 INDEX.tsv（file slug url last_revised title）。"""
import os, re, shutil

ROOT = r'<HOME>\Desktop\数译发布\gitee_shuyi\07_refs_nlab'
SRC = os.path.join(ROOT, 'tools', 'nlab')
PAGES = os.path.join(ROOT, 'pages')
IDX = os.path.join(ROOT, 'INDEX.tsv')

# 1) 复制新页（已存在的跳过）
copied, skipped = [], []
for fn in sorted(os.listdir(SRC)):
    if not fn.endswith('.md'):
        continue
    dst = os.path.join(PAGES, fn)
    if os.path.exists(dst):
        skipped.append(fn)
        continue
    shutil.copy2(os.path.join(SRC, fn), dst)
    copied.append(fn)

# 2) 从每个页的头四行解析
def parse(p):
    head = []
    with open(p, encoding='utf-8') as f:
        for _ in range(6):
            line = f.readline()
            if not line:
                break
            head.append(line.rstrip('\n'))
    title = head[0].lstrip('# ').strip() if head else p
    url = ''
    rev = ''
    for h in head:
        if h.startswith('url:'):
            url = h[4:].strip()
        elif h.startswith('last_revised:'):
            rev = h[13:].strip()
    slug = url.rsplit('/show/', 1)[-1] if '/show/' in url else ''
    return title, url, rev, slug

rows = []
for fn in sorted(os.listdir(PAGES)):
    if not fn.endswith('.md'):
        continue
    title, url, rev, slug = parse(os.path.join(PAGES, fn))
    rows.append((fn, slug, url, rev, title))

rows.sort(key=lambda r: r[0].lower())
with open(IDX, 'w', encoding='utf-8', newline='\n') as f:
    f.write('file\tslug\turl\tlast_revised\ttitle\n')
    for r in rows:
        f.write('\t'.join(r) + '\n')

print('copied', len(copied), 'skipped', len(skipped), 'total rows', len(rows))
print('new:', ', '.join(copied))
