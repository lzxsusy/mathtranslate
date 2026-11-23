import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(__file__)
SECT = os.path.join(HERE, '..', '..', '..', '源码', 'sections')
TOC = os.path.join(HERE, '..', '..', '..', '源码', 'main.toc')

def clean_title(t):
    t = re.sub(r'\\texorpdfstring\s*\{([^{}]*)\}\{[^{}]*\}', r'\1', t)
    t = t.replace('$', '')
    t = t.replace('\\mathbb {C}', 'C').replace('\\mathbb{C}', 'C')
    t = t.replace('\\mathbb {F}_q', 'F_q').replace('\\mathbb{F}_q', 'F_q')
    t = re.sub(r'\\[a-zA-Z]+\s*', '', t)
    t = t.replace('{', '').replace('}', '')
    t = t.replace('_', '_')
    return re.sub(r'\s+', ' ', t).strip()

toc = {}
for line in open(TOC, encoding='utf-8'):
    m = re.search(r'\\contentsline \{(section|subsection|subsubsection)\}\{\\numberline \{([^}]*)\}(.*?)\}\{(\d+)\}', line)
    if m:
        toc[m.group(2).strip()] = (int(m.group(4)), clean_title(m.group(3)))

files = sorted([f for f in os.listdir(SECT) if f.endswith('.tex') and re.match(r's\d', f)])
sec = sub = subsub = 0
for fn in files:
    lines = open(os.path.join(SECT, fn), encoding='utf-8').read().splitlines()
    page = None
    for i, line in enumerate(lines, 1):
        m = re.search(r'原文 PDF 第\s*(\d+)\s*页', line)
        if m:
            page = int(m.group(1))
        m = re.match(r'\\(section|subsection|subsubsection)\{(.+?)\}\s*$', line)
        if not m:
            continue
        level = {'section': 1, 'subsection': 2, 'subsubsection': 3}[m.group(1)]
        title = clean_title(m.group(2))
        if level == 1:
            sec += 1; sub = 0; subsub = 0
            num = str(sec)
        elif level == 2:
            sub += 1; subsub = 0
            num = f'{sec}.{sub}'
        else:
            subsub += 1
            num = f'{sec}.{sub}.{subsub}'
        tpage, ttitle = toc.get(num, ('?', ''))
        print(f'{num}\t{level}\t{title}\t{page}\t{tpage}\t{fn}:{i}')
