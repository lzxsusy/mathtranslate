# -*- coding: utf-8 -*-
"""nLab 本地缓存抓取器。

用法:
  python nlab_fetch.py list.tsv
  list.tsv 每行: <本地文件名>\t<candidate-slug>[,<candidate-slug>...]
输出:
  work/nlab/<本地文件名>.md      (标题 + 规范 URL + Last revised + 正文 markdown)
  work/nlab/INDEX.tsv            (file, slug, url, last_revised, title, chars, status)

正文 = Instiki 源码 textarea 里从第一个标题行开始的 markdown（保留 $...$ 与 [[...]] 链接），
去掉 =-- 围起来的侧栏 include、[[!redirects]]/[[!category]] 行，截断 6000 字符。
"""
import urllib.request, urllib.error, re, sys, os, html
from concurrent.futures import ThreadPoolExecutor

UA = {'User-Agent': 'Mozilla/5.0 (research; nlab-cache)'}
BASE = 'https://ncatlab.org/nlab/'
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'nlab')
os.makedirs(OUT, exist_ok=True)
MAXCHARS = 6000
MON = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06',
       'July': '07', 'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12'}


def get(url, timeout=45, tries=3):
    last = None
    for _ in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read().decode('utf-8', 'replace')
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            last = e
        except Exception as e:
            last = e
    if last:
        raise last
    return None


def clean_source(raw):
    body = raw.replace('\r\n', '\n')
    out = []
    fence = False
    for line in body.split('\n'):
        if line.strip() == '=--':
            fence = not fence
            continue
        if fence:
            continue
        out.append(line)
    body = '\n'.join(out)
    # 从第一个标题行开始
    lines = body.split('\n')
    start = 0
    for i, l in enumerate(lines):
        if re.match(r'^#{1,4} +\S', l):
            start = i
            break
    body = '\n'.join(lines[start:])
    body = re.sub(r'^#+\s*Contents\s*#*\s*$', '', body, flags=re.M)
    body = re.sub(r'^\{:\s*toc\s*\}\s*$', '', body, flags=re.M)
    body = re.sub(r'^\[\[!redirects?[^\n]*\]\]\s*$', '', body, flags=re.M)
    body = re.sub(r'^\[\[!category[^\n]*\]\]\s*$', '', body, flags=re.M)
    body = re.sub(r'\n{3,}', '\n\n', body).strip()
    return body


def fetch_source(slug):
    t = get(BASE + 'source/' + slug)
    if not t:
        return None
    m = re.search(r'<textarea[^>]*>(.*?)</textarea>', t, re.S)
    if not m:
        return None
    body = clean_source(html.unescape(m.group(1)))
    return body or None


def meta(slug):
    t = get(BASE + 'show/' + slug)
    if not t:
        return ('', '')
    m = re.search(r'<title>\s*(.*?)\s*in nLab\s*</title>', t, re.S)
    title = html.unescape(m.group(1)).strip() if m else slug
    r = re.search(r'Last revised on ([A-Z][a-z]+ +\d{1,2}, \d{4})', t)
    rev = ''
    if r:
        mm = re.match(r'([A-Z][a-z]+) +(\d{1,2}), (\d{4})', r.group(1))
        if mm:
            rev = '%s-%s-%02d' % (mm.group(3), MON.get(mm.group(1), '00'), int(mm.group(2)))
    return (title, rev)


def one(item):
    name, cands = item
    slug = body = None
    for c in cands:
        c = c.strip()
        if not c:
            continue
        try:
            b = fetch_source(c)
        except Exception:
            b = None
        if b and len(b) > 60:
            slug, body = c, b
            break
    if not body:
        return dict(name=name, slug='', url='', last_revised='', title='', chars=0, status='NOTFOUND')
    title, rev = meta(slug)
    if len(body) > MAXCHARS:
        body = body[:MAXCHARS] + '\n\n[... 正文截断于 %d 字符 ...]' % MAXCHARS
    url = BASE + 'show/' + slug
    with open(os.path.join(OUT, name + '.md'), 'w', encoding='utf-8') as f:
        f.write('# %s\n\nurl: %s\nlast_revised: %s\n---\n\n%s\n' % (title, url, rev, body))
    return dict(name=name, slug=slug, url=url, last_revised=rev, title=title, chars=len(body), status='OK')


def main():
    with open(sys.argv[1], encoding='utf-8') as f:
        lines = [l.rstrip('\n') for l in f if l.strip() and not l.lstrip().startswith('#')]
    items = []
    for l in lines:
        p = l.split('\t')
        if len(p) >= 2:
            items.append((p[0].strip(), p[1].split(',')))
    print('total', len(items), flush=True)
    rows = []
    with ThreadPoolExecutor(max_workers=6) as ex:
        for k, r in enumerate(ex.map(one, items), 1):
            rows.append(r)
            print('%3d/%d %-8s %-10s %s' % (k, len(items), r['status'], r['last_revised'], r['name']), flush=True)
    idx = os.path.join(OUT, 'INDEX.tsv')
    have = {}
    if os.path.exists(idx):
        for l in open(idx, encoding='utf-8').read().splitlines()[1:]:
            p = l.split('\t')
            if len(p) >= 6:
                have[p[0]] = p[:7]
    for r in rows:
        have[r['name']] = [r['name'], r['slug'], r['url'], r['last_revised'], r['title'], str(r['chars']), r['status']]
    with open(idx, 'w', encoding='utf-8') as f:
        f.write('file\tslug\turl\tlast_revised\ttitle\tchars\tstatus\n')
        for k in sorted(have):
            f.write('\t'.join(have[k]) + '\n')
    nf = [r for r in rows if r['status'] != 'OK']
    print('OK', len(rows) - len(nf), 'NOTFOUND', len(nf))
    for r in nf:
        print('  MISS', r['name'])


if __name__ == '__main__':
    main()
