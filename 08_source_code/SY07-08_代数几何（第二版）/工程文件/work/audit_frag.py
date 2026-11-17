# -*- coding: utf-8 -*-
import os, re, json

root = r'C:\Users\admin\Desktop\数译发布\shuyi\translations\SY07-08'
work = os.path.join(root, '工程文件', 'work')
notes = json.load(open(os.path.join(work, 'tnote_raw.json'), encoding='utf-8'))

def ocr(bookpage):
    p = os.path.join(work, 'en', 'p%03d.txt' % (bookpage + 7))
    if not os.path.exists(p):
        return ''
    return open(p, encoding='utf-8', errors='ignore').read()

def norm(s):
    s = s.replace('$', ' ')
    s = re.sub(r'\\[a-zA-Z]+', ' ', s)
    s = s.lower()
    s = re.sub(r'[^a-z0-9]+', '', s)
    return s

out = []
for n in notes:
    t = re.sub(r'\s+', ' ', n['text']).strip()
    pages = []
    for a, b in n['pages']:
        pages.append(int(a))
    # also expand '--' ranges manually
    for a, b in re.findall(r'p\.(\d+)\s*-+\s*(\d+)', t):
        pages += list(range(int(a), int(b) + 1))
    pages = sorted(set(pages))
    # quoted fragments: inside 「...」 with ascii math/words, or inside $...$
    frags = re.findall(r'「([^」]{3,120})」', t)
    frags += re.findall(r'\$([^$]{2,80})\$', t)
    frags += re.findall(r'“([^”]{3,120})”', t)
    res = []
    for f in frags:
        nf = norm(f)
        if len(nf) < 4:
            continue
        where = []
        for p in pages:
            txt = norm(ocr(p))
            if nf and nf in txt:
                where.append(p)
        # also try whole-book scan if not found on cited pages
        if not where:
            for q in range(1, 250):
                if q in pages:
                    continue
                txt = norm(ocr(q))
                if nf and nf in txt:
                    where.append(-q)  # negative = found elsewhere
                    break
        res.append((f[:40], where))
    out.append({'file': n['file'], 'line': n['line'], 'pages': pages, 'frags': res,
                'text': t})

json.dump(out, open(os.path.join(work, 'tnote_fragcheck.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

for o in out:
    print('=' * 6, o['file'] + ':' + str(o['line']), 'pages', o['pages'])
    if not o['frags']:
        print('   (无可比对引文)')
    for f, w in o['frags']:
        print('   ', ('OK@' + str([x for x in w if x > 0]) if [x for x in w if x > 0] else
                      ('ELSE@' + str([-x for x in w if x < 0]) if w else 'NOTFOUND')),
              '|', f)
