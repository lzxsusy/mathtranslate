import os, re, json, sys
sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(__file__)
SECT = os.path.join(HERE, '..', '..', '..', '源码', 'sections')
TOC = os.path.join(HERE, '..', '..', '..', '源码', 'main.toc')

def clean_title(t):
    t = t.replace('\\texorpdfstring', '')
    t = re.sub(r'\{([^{}]*)\}\{([^{}]*)\}', r'\1', t)
    t = t.replace('$', '')
    t = t.replace('\\mathbb', '')
    t = re.sub(r'\\[a-zA-Z]+', '', t)
    t = t.replace('{', '').replace('}', '').replace('_', '')
    return re.sub(r'\s+', ' ', t).strip()

# toc: number -> page
toc = {}
for line in open(TOC, encoding='utf-8'):
    m = re.search(r'\\numberline \{([^}]*)\}(.*?)\}\{(\d+)\}', line)
    if m:
        num = m.group(1).strip()
        title = clean_title(m.group(2))
        toc[num] = (int(m.group(3)), title)

files = sorted([f for f in os.listdir(SECT) if f.endswith('.tex') and re.match(r's\d', f)])
rows = []
for fn in files:
    lines = open(os.path.join(SECT, fn), encoding='utf-8').read().splitlines()
    page = None
    for i, line in enumerate(lines, 1):
        m = re.search(r'原文 PDF 第\s*(\d+)\s*页', line)
        if m:
            page = int(m.group(1))
        m = re.match(r'\\(section|subsection|subsubsection)\{(.+?)\}\s*$', line)
        if m:
            level = {'section': 1, 'subsection': 2, 'subsubsection': 3}[m.group(1)]
            title = clean_title(m.group(2))
            rows.append((fn, i, level, title, page))

print('## HEADINGS')
for fn, i, level, title, page in rows:
    if level == 1:
        num = re.search(r'\\numberline \{([^}]*)\}', open(os.path.join(SECT, fn), encoding='utf-8').read()) if False else None
    print(f'{fn}\t{i}\t{level}\t{title}\t{page}')

print('\n## FOOTNOTES')
for fn in files:
    lines = open(os.path.join(SECT, fn), encoding='utf-8').read().splitlines()
    page = None
    for i, line in enumerate(lines, 1):
        m = re.search(r'原文 PDF 第\s*(\d+)\s*页', line)
        if m:
            page = int(m.group(1))
        if '\\footnote{' in line:
            # first footnote text on this line, rough
            idx = line.find('\\footnote{')
            txt = line[idx:idx+120]
            txt = re.sub(r'\s+', ' ', txt)
            print(f'{fn}\t{i}\t{page}\t{txt}')

print('\n## NAMED')
for fn in files:
    lines = open(os.path.join(SECT, fn), encoding='utf-8').read().splitlines()
    page = None
    for i, line in enumerate(lines, 1):
        m = re.search(r'原文 PDF 第\s*(\d+)\s*页', line)
        if m:
            page = int(m.group(1))
        m = re.search(r'\\begin\{(named\w+)\}\{([^}]*)\}', line)
        if m:
            print(f'{fn}\t{i}\t{page}\t{m.group(1)}\t{m.group(2)}')

print('\n## TAGS')
for fn in files:
    lines = open(os.path.join(SECT, fn), encoding='utf-8').read().splitlines()
    page = None
    tags = []
    for i, line in enumerate(lines, 1):
        m = re.search(r'原文 PDF 第\s*(\d+)\s*页', line)
        if m:
            page = int(m.group(1))
        m = re.search(r'\\tag\{([^}]*)\}', line)
        if m:
            tags.append((m.group(1), page))
    print(f'{fn}\t{len(tags)}\t{tags[0] if tags else ""}\t{tags[-1] if tags else ""}')

print('\n## NOTES')
for fn in files:
    lines = open(os.path.join(SECT, fn), encoding='utf-8').read().splitlines()
    counts = {'Tutor': 0, '原文疑误': 0, '存疑': 0, '背景补充': 0}
    for line in lines:
        if line.lstrip().startswith('% [Tutor Note:'):
            counts['Tutor'] += 1
        elif line.lstrip().startswith('% [原文疑误:'):
            counts['原文疑误'] += 1
        elif line.lstrip().startswith('% [存疑:'):
            counts['存疑'] += 1
        elif line.lstrip().startswith('% [背景补充:'):
            counts['背景补充'] += 1
    print(f'{fn}\t{counts}')
