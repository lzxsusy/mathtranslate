# -*- coding: utf-8 -*-
"""从 zh/*.tex 抽取 keytakeaways 与 yizhu，汇编成注疏交付物。

用法:  python tools/extract_notes.py
输出:  注疏/译注汇编.md, 注疏/原文疑误表.md, 注疏/译注汇编.tex, 注疏/stats.json
"""
import io, os, re, json, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ZH = os.path.join(ROOT, 'zh')
OUT = os.path.join(ROOT, '注疏')
os.makedirs(OUT, exist_ok=True)

SEC_TITLES = {}  # shard -> section title found in file


def balanced(s, i):
    """s[i] 指向 '{'，返回匹配的 '}' 之后的位置。"""
    depth = 0
    while i < len(s):
        if s[i] == '{':
            depth += 1
        elif s[i] == '}':
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    return -1


def sec_title(text):
    i = text.find('\\section{')
    if i < 0:
        return ''
    j = balanced(text, i + len('\\section'))
    if j < 0:
        return ''
    return text[i + len('\\section{'):j - 1].strip()


def find_blocks(text, env):
    """返回 [(opt, body)]，支持 \begin{env}[opt] ... \end{env}"""
    out = []
    for m in re.finditer(r'\\begin\{%s\}(?:\[([^\]]*)\])?(.*?)\\end\{%s\}' % (env, env), text, re.S):
        out.append((m.group(1) or '', m.group(2).strip()))
    return out


def clean(s):
    s = re.sub(r'\\emph\{([^{}]*)\}', r'*\1*', s)
    s = re.sub(r'\\textbf\{([^{}]*)\}', r'**\1**', s)
    return s.strip()


rows = []
takeaways = []
for path in sorted(glob.glob(os.path.join(ZH, '*.tex'))):
    name = os.path.basename(path)[:-4]
    text = io.open(path, encoding='utf-8').read()
    title = sec_title(text)
    SEC_TITLES[name] = title
    for opt, body in find_blocks(text, 'keytakeaways'):
        takeaways.append({'shard': name, 'section': title, 'body': clean(body), 'raw': body})
    for opt, body in find_blocks(text, 'yizhu'):
        kind = opt.strip() or '其他'
        rows.append({'shard': name, 'section': title, 'kind': kind,
                     'body': clean(body), 'raw': body})

TYPES = ['易错点', '含糊点拨', '物理图像', '原文疑误', '其他']

# ---------- 译注汇编.md ----------
md = []
md.append('# KW06 中译本 · 译注汇编\n')
md.append('> 本文件由 `tools/extract_notes.py` 自动从 `zh/*.tex` 抽取，**不要手改**。\n')
md.append('> 译注体例：以「按：」起首，来源等级 [A] 原文明确 / [B] 权威综述或百科 / [I] 译者推断。\n')
md.append('\n## 统计\n')
cnt = {}
for r in rows:
    cnt[r['kind']] = cnt.get(r['kind'], 0) + 1
md.append('| 类型 | 条数 |\n|---|---|')
for k in TYPES:
    if k in cnt:
        md.append('| %s | %d |' % (k, cnt[k]))
md.append('| **合计** | **%d** |\n' % len(rows))
md.append('\n## 本节重点（keytakeaways）\n')
for t in takeaways:
    md.append('\n### %s · %s\n' % (t['shard'], t['section'] or '（节首）'))
    md.append(t['body'] + '\n')

for k in TYPES:
    sel = [r for r in rows if r['kind'] == k]
    if not sel:
        continue
    md.append('\n---\n\n## %s（%d 条）\n' % (k, len(sel)))
    for r in sel:
        md.append('\n**[%s]** %s\n' % (r['shard'], r['body']))
io.open(os.path.join(OUT, '译注汇编.md'), 'w', encoding='utf-8').write('\n'.join(md))

# ---------- 原文疑误表.md ----------
errs = [r for r in rows if r['kind'] == '原文疑误']
m2 = ['# KW06 原文疑误表\n',
      '> 原文笔误照录于译文，另加「[原文疑误]」译注说明。本表汇总全部疑误条。\n',
      '> 共 %d 条。\n' % len(errs)]
if errs:
    m2.append('| # | 分片 | 说明 |\n|---|---|---|')
    for i, r in enumerate(errs, 1):
        body = r['body'].replace('|', '\\|').replace('\n', ' ')
        m2.append('| %d | %s | %s |' % (i, r['shard'], body))
else:
    m2.append('\n（暂无条目）')
io.open(os.path.join(OUT, '原文疑误表.md'), 'w', encoding='utf-8').write('\n'.join(m2) + '\n')

# ---------- 译注汇编.tex ----------


def tex_title(t):
    """把分片标题放进 \\subsection* 参数：简单情况直接用，带数学时加保护。"""
    return t if t else '节首'

tex = [r'''\documentclass[11pt,a4paper]{article}
\usepackage[UTF8,fontset=windows,heading=true]{ctex}
\usepackage[margin=2.5cm]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{xcolor}
\usepackage{enumitem}
\usepackage[colorlinks,linkcolor=blue!50!black]{hyperref}
\input{../macros}
\input{../macros-extra}
\linespread{1.15}
\title{\bfseries Kapustin--Witten (2006) 中译本\\[4pt]\large 译注汇编}
\author{译本附册}
\date{2026 年 11 月}
\begin{document}
\maketitle
\tableofcontents
\newpage
''']
tex.append('\n\\section*{本节重点}\n\\addcontentsline{toc}{section}{本节重点}\n')
cur = None
for t in takeaways:
    tex.append('\n\\subsection*{%s · %s}\n%s\n' % (t['shard'], tex_title(t['section']), t['raw']))
for k in TYPES:
    sel = [r for r in rows if r['kind'] == k]
    if not sel:
        continue
    head = '\n\\section*{%s}\n\\addcontentsline{toc}{section}{%s}\n' % (k, k)
    body = ''.join('\n\\noindent\\textbf{[%s]} %s\\par\\smallskip\n' % (r['shard'], r['body']) for r in sel)
    tex.append(head + body)
tex.append('\n\\end{document}\n')
io.open(os.path.join(OUT, '译注汇编.tex'), 'w', encoding='utf-8').write('\n'.join(tex))

json.dump({'total_notes': len(rows), 'by_kind': cnt, 'takeaways': len(takeaways),
           'shards': sorted({r['shard'] for r in rows})},
          io.open(os.path.join(OUT, 'stats.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('notes=%d takeaways=%d kinds=%s' % (len(rows), len(takeaways), cnt))
