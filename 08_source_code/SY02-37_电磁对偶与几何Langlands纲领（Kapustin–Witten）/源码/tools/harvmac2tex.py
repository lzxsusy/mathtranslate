# -*- coding: utf-8 -*-
"""KW06 (hep-th/0604151) harvmac -> LaTeX 脚手架转换器。

输入：src_orig/glshort.tex、src_orig/glshortspare.defs
输出：skel/NN-*.tex（英文正文 + 锁定公式/编号/引用，待译）、macros.tex、refs.tex、
      figures/map.json（EPS 引用表）、shards.json（分片索引 + 原文行号区间）
"""
import io, os, re, json

ROOT = r'C:\Users\admin\Downloads\KW06_work'
SRC = os.path.join(ROOT, 'src_orig', 'glshort.tex')
DEFS = os.path.join(ROOT, 'src_orig', 'glshortspare.defs')

def read(p):
    return io.open(p, encoding='utf-8', errors='replace').read()

# ---------------------------------------------------------------- defs 解析
EQ, SEC, BIB = {}, {}, {}
for line in read(DEFS).splitlines():
    m = re.match(r'\\def\\([A-Za-z][A-Za-z0-9]*)\{(.*)\}\s*$', line)
    if not m:
        continue
    name, val = m.group(1), m.group(2)
    m2 = re.match(r'^\(\s*\\hyperref\s*\{\}\{equation\}\{([^}]*)\}\{[^}]*\}\)$', val)
    if m2:
        EQ[name] = m2.group(1)
        continue
    m2 = re.match(r'^\\hyperref\s*\{\}\{(section|subsection|subsubsection)\}\{([^}]*)\}\{[^}]*\}$', val)
    if m2:
        SEC[name] = (m2.group(1), m2.group(2))
        continue
    m2 = re.match(r'^\[\s*\\hyperref\s*\{\}\{reference\}\{(\d+)\}\{\d+\}\]$', val)
    if m2:
        BIB[name] = int(m2.group(1))

# ---------------------------------------------------------------- 工具函数
def balanced(text, i):
    """text[i]=='{' -> (content, index_after_closing_brace)"""
    assert text[i] == '{', (i, text[i:i+20])
    depth, j, n = 0, i, len(text)
    while j < n:
        c = text[j]
        if c == '\\':
            j += 2
            continue
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                return text[i + 1:j], j + 1
        j += 1
    raise ValueError('unbalanced braces')

def find_group(text, start):
    """从 start 起找第一个 '{'，返回 (content, after)；找不到返回 (None, start)"""
    i = start
    while i < len(text) and text[i] in ' \t\n':
        i += 1
    if i < len(text) and text[i] == '{':
        try:
            return balanced(text, i)
        except ValueError:
            return None, start
    return None, start

def conv_math(m):
    """数学块内 harvmac -> LaTeX"""
    m = m.replace('\\cr', '\\\\')
    out, i = '', 0
    while i < len(m):
        cands = []
        for macro, env in (('\\eqalign', 'aligned'), ('\\matrix', 'matrix')):
            j = m.find(macro + '{', i)
            if j >= 0:
                cands.append((j, macro, env))
        if not cands:
            out += m[i:]
            break
        j, macro, env = min(cands)
        out += m[i:j]
        body, k = balanced(m, j + len(macro))
        out += '\\begin{%s}%s\\end{%s}' % (env, body, env)
        i = k
    m = out
    m = re.sub(r'\\noalign\{([^{}]*)\}', '', m)
    return m

def strip_vspace(t):
    t = t.replace('\\noindent', '')
    t = re.sub(r'\\(bigskip|medskip|smallskip|vskip\s*[0-9.]+\s*(in|cm|mm|pt))\b',
               r'\\par\\medskip', t)
    t = t.replace('\\nobreak', '')
    return t

# ---------------------------------------------------------------- 主流程
src = read(SRC)
lines = src.split('\n')
# 正文起点：第一个 \newsec
start = next(i for i, l in enumerate(lines) if l.startswith('\\newsec'))
body = '\n'.join(lines[start:])
# 去掉结尾 \listrefs \end
body = body[:body.rindex('\\listrefs')]
# 去掉 TeX 注释（\% 转义除外），避免注释里的花括号干扰解析
body = re.sub(r'(?<!\\)%[^\n]*', '', body)

BIBTEXT = {}
FIGS = []
EQS = []          # [(label, number)]
EMITTED = set()
plot_q = []       # equation placeholders

def protect_eq(text):
    out = ''
    i = 0
    while True:
        j = text.find('\\eqn\\', i)
        if j < 0:
            out += text[i:]
            break
        out += text[i:j]
        k = j + len('\\eqn\\')
        m = re.match(r'[A-Za-z][A-Za-z0-9]*', text[k:])
        name = m.group(0)
        k += len(name)
        g, k2 = find_group(text, k)
        if g is None:
            out += text[j:k]
            i = k
            continue
        num = EQ.get(name)
        body_math = conv_math(g).strip()
        if num is None or name in EMITTED:
            out += '%% [WARN] 公式 \\eqn\\%s 无编号或重复\n' % name
            if num:
                out += '\\begin{equation*}\n\\tag*{(%s)}\n%s\n\\end{equation*}\n' % (num, body_math)
            else:
                out += '\\begin{equation*}\n%s\n\\end{equation*}\n' % body_math
            EMITTED.add(name)
        else:
            out += '%% 式 (%s)\n\\setcounter{equation}{%d}\n\\begin{equation}\\label{eq:%s}\n%s\n\\end{equation}\n' % (
                num, int(float(num.split('.')[-1])) - 1, name, body_math)
            EQS.append((name, num))
            EMITTED.add(name)
        i = k2
    return out

def protect_figs(text):
    out, i = '', 0
    while True:
        j = text.find('\\ifig\\', i)
        if j < 0:
            out += text[i:]
            break
        out += text[i:j]
        k = j + len('\\ifig\\')
        m = re.match(r'[A-Za-z][A-Za-z0-9]*', text[k:])
        name = m.group(0)
        k += len(name)
        cap, k = find_group(text, k)
        fig, k = find_group(text, k)
        num = len(FIGS) + 1
        FIGS.append({'label': name, 'num': num, 'caption': cap.strip(), 'fig': (fig or '').strip()})
        eps = re.search(r'\\epsfbox\{([^}]*)\}', fig or '')
        incl = ''
        if eps:
            fn = eps.group(1).replace('.eps', '')
            incl = '\\includegraphics[width=0.75\\linewidth]{figures/%s.png}' % fn
        out += ('\n\\begin{figure}[htbp]\n\\centering\n%s\n'
                '\\caption{%s（原文 Fig.~%d）}\n\\label{fig:%s}\n\\end{figure}\n'
                % (incl, re.sub(r'\s+', ' ', cap.strip()), num, name))
        i = k
    return out

def protect_foot(text):
    out, i = '', 0
    while True:
        j = text.find('\\foot{', i)
        if j < 0:
            out += text[i:]
            break
        out += text[i:j]
        g, k = balanced(text, j + len('\\foot'))
        out += '\\footnote{%s}' % convert_inline(g, 0)
        i = k
    return out

def refs_list(text):
    """\\refs{\\a,\\b} / \\refs{\\a-\\b} -> \\cite{refN,...}"""
    out, i = '', 0
    while True:
        j = text.find('\\refs{', i)
        if j < 0:
            out += text[i:]
            break
        out += text[i:j]
        g, k = balanced(text, j + len('\\refs'))
        nums = []
        for it in g.split(','):
            m = re.match(r'\s*\\?([A-Za-z][A-Za-z0-9]*)\s*(?:-|\u2013)\s*\\?([A-Za-z][A-Za-z0-9]*)\s*$', it)
            if m and m.group(1) in BIB and m.group(2) in BIB:
                a, b = BIB[m.group(1)], BIB[m.group(2)]
                nums += list(range(min(a, b), max(a, b) + 1))
            else:
                t = it.strip().lstrip('\\')
                if t in BIB:
                    nums.append(BIB[t])
        out += ('\\cite{%s}' % ','.join('ref%d' % n for n in nums)) if nums else '@@REFS@@'
        i = k
    return out

def convert_inline(text, depth):
    """正文（含行内数学）里的 harvmac 宏转换，depth 用于递归"""
    if depth > 3:
        return text
    # 1. 引用：\nref\KEY{...} / \lref\KEY{...} / \ref\KEY{...}
    out, i = '', 0
    pat = re.compile(r'\\(nref|lref|ref)\\')
    while True:
        m = pat.search(text, i)
        if not m:
            out += text[i:]
            break
        out += text[i:m.start()]
        kind = m.group(1)
        k = m.end()
        mm = re.match(r'[A-Za-z][A-Za-z0-9]*', text[k:])
        name = mm.group(0) if mm else ''
        k += len(name)
        g, k2 = find_group(text, k)
        if g is not None:
            k = k2
        if name in BIB:
            n = BIB[name]
            if n not in BIBTEXT:
                BIBTEXT[n] = g or ''
            if kind in ('lref', 'nref'):
                out += ''          # \lref/\nref = 静默参考文献，正文不打印编号（与已出版 PDF 一致；
                                   # 已逐页核实：\nref 只登记文献表，不打印 [N]）
            else:
                out += '\\cite{ref%d}' % n
        elif kind == 'lref':
            out += ''              # 未定义的 \lref（出版版里被删去）整块丢弃
        elif name in EQ:
            out += '\\eqref{eq:%s}' % name
        elif name in SEC:
            out += '第~\\ref{sec:%s}~节' % name
        else:
            out += '@@UNKNOWNREF:%s@@' % name
        i = k
    text = out
    text = refs_list(text)
    # 2. 裸宏
    def bare(m):
        name = m.group(1)
        if name in EQ:
            return '\\eqref{eq:%s}' % name
        if name in BIB:
            return '\\cite{ref%d}' % BIB[name]
        if name in SEC:
            return '第~\\ref{sec:%s}~节' % name
        return m.group(0)
    text = re.sub(r'\\([A-Za-z][A-Za-z0-9]*)', bare, text)
    return text

def convert_section_structure(text):
    text = re.sub(r'\\newsec\{', r'\\section{', text)
    text = re.sub(r'\\seclab\\([A-Za-z][A-Za-z0-9]*)', r'\\label{sec:\1}', text)
    text = re.sub(r'\\subsec\{', r'\\subsection{', text)
    text = re.sub(r'\\subseclab\\([A-Za-z][A-Za-z0-9]*)', r'\\label{sec:\1}', text)
    text = re.sub(r'\\subsubsec\{', r'\\subsubsection{', text)
    return text

# ---- 依次处理：结构 → 公式 → 图 → 脚注 → 行内引用
body = convert_section_structure(body)
body = protect_eq(body)
body = protect_figs(body)
# 把行内数学与已生成的公式环境遮罩起来，避免引用替换误伤
MASK = []
def _mask(m):
    key = '@@M%d@@' % len(MASK)
    MASK.append((key, m.group(0)))
    return key
body = re.sub(r'\$[^$]*\$', _mask, body)
body = re.sub(r'\\begin\{equation\}.*?\\end\{equation\}', _mask, body, flags=re.S)
body = protect_foot(body)
body = convert_inline(body, 0)
for key, val in MASK:
    body = body.replace(key, val)
body = re.sub(r'@@M(\d+)@@', lambda m: MASK[int(m.group(1))][1], body)
body = strip_vspace(body)
# 清理多余空行
body = re.sub(r'\n{3,}', '\n\n', body)

# ---------------------------------------------------------------- 分片
# 找 section 起点（在原始行号里）
sec_titles, sec_lines = [], []
pos = 0
while True:
    j = src.find('\\newsec{', pos)
    if j < 0:
        break
    g, pos = balanced(src, j + len('\\newsec'))
    sec_titles.append(re.sub(r'\s+', ' ', g).strip())
    sec_lines.append(src[:j].count('\n') + 1)

# 在转换后正文里重新按 \section 切
chunks = re.split(r'(?=\\section\{)', body)
chunks = [c for c in chunks if c.strip()]
assert len(chunks) == 12, len(chunks)

# 每节内按 \subsection 再切，控制每片行数 <= 850
shards = []
for si, ch in enumerate(chunks, 1):
    subs = re.split(r'(?=\\subsection\{)', ch)
    subs = [s for s in subs if s.strip()]
    cur = ''
    for s in subs:
        if cur and len((cur + s).split('\n')) > 480:
            shards.append((si, cur))
            cur = s
        else:
            cur += s
    if cur:
        shards.append((si, cur))

os.makedirs(os.path.join(ROOT, 'skel'), exist_ok=True)
index = []
for n, (si, txt) in enumerate(shards, 1):
    fname = '%02d-s%02d.tex' % (n, si)
    head = ('%%%% ============================================================\n'
            '%%%% 分片 %02d：原文第 %d 节「%s」（原文 glshort.tex 起于第 %d 行）\n'
            '%%%% 由 tools/harvmac2tex.py 从 arXiv 源码（hep-th/0604151v3）自动生成。\n'
            '%%%% 只译英文散文；公式、编号、\\label、\\cite 一律不改。\n'
            '%%%% ============================================================\n\n') % (n, si, sec_titles[si - 1], sec_lines[si - 1])
    io.open(os.path.join(ROOT, 'skel', fname), 'w', encoding='utf-8').write(head + txt.strip() + '\n')
    index.append({'shard': fname, 'section': si, 'title': sec_titles[si-1],
                  'lines': len(txt.split('\n')), 'chars': len(txt)})

# ---------------------------------------------------------------- refs.tex
order = sorted(BIBTEXT)
buf = []
for n in order:
    txt = BIBTEXT[n]
    txt = convert_inline(txt, 1)
    for _k, _v in MASK:
        txt = txt.replace(_k, _v)
    txt = strip_vspace(txt)
    txt = re.sub(r'\s+', ' ', txt).strip().rstrip(',').strip()
    buf.append('\\bibitem{ref%d} %s' % (n, txt))
io.open(os.path.join(ROOT, 'refs.tex'), 'w', encoding='utf-8').write(
    '%% 参考文献：由 harvmac 的 \\nref 条目自动抽取，编号 = 原文 [N]\n'
    '\\begin{thebibliography}{146}\n' + '\n'.join(buf) + '\n\\end{thebibliography}\n')

# ---------------------------------------------------------------- macros.tex
# 从源码前导区与 defs 抽取非引用类 \def
pre = '\n'.join(lines[:start])
mdefs = {}
for m in re.finditer(r'\\def\\([A-Za-z][A-Za-z0-9]*)\{', pre):
    name = m.group(1)
    try:
        g, _ = balanced(pre, m.end() - 1)
    except Exception:
        continue
    mdefs[name] = g
for line2 in read(DEFS).splitlines():
    m = re.match(r'\\def\\([A-Za-z][A-Za-z0-9]*)\{(.*)\}\s*$', line2)
    if not m:
        continue
    name, val = m.group(1), m.group(2)
    if '\\hyperref' in val:
        continue
    mdefs.setdefault(name, val)
# 过滤掉排版类、字体类宏
BAD = re.compile(r'\\(font|newfam|textfont|scriptfont|scriptscriptfont|skewchar|input|writedefs|'
                 r'listtoc|writetoc|Title|Date|listrefs|end|bye|vbox|hsize|halign|figinsert|ifig|'
                 r'filbreak|midinsert|endinsert|footnotefont|leftbracket|goodbreak|noblackbox)')
mac = ['%% KW06 记号宏：由 tools/harvmac2tex.py 自动抽取（勿手改；新增请写 macros-extra.tex）',
       '\\def\\Bbb#1{\\mathbb{#1}}',
       '\\def\\frak#1{\\mathfrak{#1}}',
       '\\def\\cal#1{\\mathcal{#1}}',
       '\\def\\bf#1{\\mathbf{#1}}',
       '\\def\\it#1{\\textit{#1}}',
       '\\def\\rm#1{\\mathrm{#1}}']
for name in sorted(mdefs):
    val = mdefs[name]
    if BAD.search(val) or len(val) > 200:
        continue
    mac.append('\\def\\%s{%s}' % (name, val))
io.open(os.path.join(ROOT, 'macros.tex'), 'w', encoding='utf-8').write('\n'.join(mac) + '\n')

# ---------------------------------------------------------------- 报告
json.dump(index, io.open(os.path.join(ROOT, 'shards.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
json.dump(FIGS, io.open(os.path.join(ROOT, 'figures_map.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('EQ=%d SEC=%d BIB=%d  BIBTEXT=%d  FIGS=%d  EQS=%d' %
      (len(EQ), len(SEC), len(BIB), len(BIBTEXT), len(FIGS), len(EQS)))
print('shards=%d' % len(index))
for it in index:
    print('  %-12s §%-2d %-5d lines %7d chars  %s' %
          (it['shard'], it['section'], it['lines'], it['chars'], it['title'][:40]))
missing = [n for n in range(1, max(BIB.values()) + 1) if n not in BIBTEXT]
print('missing bib entries:', missing[:20], '...' if len(missing) > 20 else '')
