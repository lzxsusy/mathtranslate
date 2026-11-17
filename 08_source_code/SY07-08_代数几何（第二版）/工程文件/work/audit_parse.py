# -*- coding: utf-8 -*-
import os, re, json, glob

root = r'C:\Users\admin\Desktop\数译发布\shuyi\translations\SY07-08'
chunk_dir = os.path.join(root, '源码', 'chunks')

files = sorted(glob.glob(os.path.join(chunk_dir, '*.tex')))
out = []
for f in files:
    name = os.path.basename(f)
    lines = open(f, encoding='utf-8').read().split('\n')
    i = 0
    while i < len(lines):
        if '\\begin{tnote}' in lines[i]:
            start = i + 1  # 1-based
            body = []
            j = i
            # collect until end{tnote}
            first = lines[i].split('\\begin{tnote}', 1)[1]
            body.append(first)
            while '\\end{tnote}' not in lines[j] or j == i:
                j += 1
                if j >= len(lines):
                    break
                body.append(lines[j])
            text = '\n'.join(body)
            text = text.replace('\\end{tnote}', '')
            # source markers
            srcs = re.findall(r'\[(依据|来源|译者按)[^\]]*\]', text)
            pages = re.findall(r'原书\s*p\.\s*(\d+)(?:\s*[–-]\s*(\d+))?', text)
            pages += re.findall(r'p\.(\d+)(?:\s*[–-]\s*(\d+))?', text)
            out.append({
                'file': name,
                'line': start,
                'text': text.strip(),
                'markers': srcs,
                'pages': [tuple(p) for p in pages],
            })
            i = j
        i += 1

print('total tnote:', len(out))
json.dump(out, open(os.path.join(root, '工程文件', 'work', 'tnote_raw.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for n in out:
    first = re.sub(r'\s+', ' ', n['text'])[:40]
    print(f"{n['file']}:{n['line']}\t{n['markers']}\t{n['pages']}\t{first}")
