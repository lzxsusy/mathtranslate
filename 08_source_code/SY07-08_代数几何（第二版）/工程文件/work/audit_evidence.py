# -*- coding: utf-8 -*-
import os, re, json

root = r'C:\Users\admin\Desktop\数译发布\shuyi\translations\SY07-08'
work = os.path.join(root, '工程文件', 'work')
notes = json.load(open(os.path.join(work, 'tnote_raw.json'), encoding='utf-8'))

def ocr_lines(bookpage, n=2):
    p = os.path.join(work, 'en', 'p%03d.txt' % (bookpage + 7))
    if not os.path.exists(p):
        return ['<no ocr>']
    lines = [l.strip() for l in open(p, encoding='utf-8', errors='ignore').read().split('\n') if l.strip()]
    return lines[:n]

for n in notes:
    t = re.sub(r'\s+', ' ', n['text']).strip()
    pages = []
    for a, b in n['pages']:
        a = int(a); pages.append(a)
        if b:
            for x in range(a, int(b) + 1):
                pages.append(x)
    pages = sorted(set(pages))
    print('=' * 8, n['file'] + ':' + str(n['line']), '| pages', pages)
    print(t)
    for p in pages:
        print('  [p%d→pdf%03d]' % (p, p + 7), ' / '.join(ocr_lines(p)))
