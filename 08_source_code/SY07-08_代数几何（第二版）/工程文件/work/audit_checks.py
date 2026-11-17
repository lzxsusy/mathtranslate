# -*- coding: utf-8 -*-
import os, re, json, csv

root = r'C:\Users\admin\Desktop\数译发布\shuyi\translations\SY07-08'
work = os.path.join(root, '工程文件', 'work')
notes = json.load(open(os.path.join(work, 'tnote_raw.json'), encoding='utf-8'))

# item index: (ch,sec,num) -> bookpage
items = {}
with open(os.path.join(work, 'items.tsv'), encoding='utf-8') as f:
    rd = csv.DictReader(f, delimiter='\t')
    for row in rd:
        try:
            key = (int(row['ch']), int(row['sec']), int(row['num']))
        except Exception:
            continue
        items.setdefault(key, []).append((int(row['bookpage']), int(row['pdfpage']), row['kind']))

black = ['zhihu', '知乎', 'baike.baidu', '百度百科', 'csdn', 'CSDN', 'jianshu', '简书',
         'weixin', 'mp.weixin', '公众号', 'bilibili', 'B站', 'blog', '博客']

def ocr_text(bookpage):
    p = os.path.join(work, 'en', 'p%03d.txt' % (bookpage + 7))
    if not os.path.exists(p):
        return None
    return open(p, encoding='utf-8', errors='ignore').read()

def toks(s):
    # ascii-ish math tokens
    s = re.sub(r'\\[a-zA-Z]+', ' ', s)
    s = re.sub(r'[^A-Za-z0-9\.\-]+', ' ', s)
    return [t for t in s.split() if len(t) >= 3]

rows = []
for n in notes:
    t = n['text']
    marker_kind = 'none'
    m = re.search(r'\[(依据|来源|译者按)', t)
    if m:
        marker_kind = m.group(1)
    pages = []
    for a, b in n['pages']:
        a = int(a)
        if a not in pages:
            pages.append(a)
        if b:
            b = int(b)
            for x in range(a, b + 1):
                if x not in pages:
                    pages.append(x)
    refs = re.findall(r'\\ref\{it:(\d+)\.(\d+)\.(\d+)\}', t)
    item_pages = []
    for ch, sec, num in refs:
        k = (int(ch), int(sec), int(num))
        if k in items:
            item_pages.append((f'{ch}.{sec}.{num}', min(p for p, _, _ in items[k])))
    # blacklist
    bl = [b for b in black if b.lower() in t.lower()]
    # token match on cited pages
    tk = toks(t)
    tk = [x for x in tk if not x.replace('.', '').isdigit()]
    hit = {}
    for pg in pages:
        txt = ocr_text(pg)
        if txt is None:
            hit[pg] = 'noocr'
            continue
        low = txt.lower()
        found = [x for x in tk if x.lower() in low]
        hit[pg] = f'{len(found)}/{len(tk)}'
    first = re.sub(r'\s+', ' ', t).strip()[:36]
    rows.append({
        'file': n['file'], 'line': n['line'], 'marker': marker_kind,
        'pages': ','.join(str(p) for p in pages),
        'refs': ';'.join(f'{a}->p{b}' for a, b in item_pages),
        'black': ','.join(bl),
        'ocr': ';'.join(f'p{p}:{v}' for p, v in hit.items()),
        'first': first,
        'len': len(t),
    })

out = os.path.join(work, 'tnote_audit.tsv')
with open(out, 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), delimiter='\t')
    w.writeheader()
    for r in rows:
        w.writerow(r)

print('rows', len(rows))
from collections import Counter
print(Counter(r['marker'] for r in rows))
print('no marker:', [(r['file'], r['line']) for r in rows if r['marker'] == 'none'])
print('black:', [(r['file'], r['line'], r['black']) for r in rows if r['black']])
print('pages total unique:', len({p for r in rows for p in r['pages'].split(',') if p}))
