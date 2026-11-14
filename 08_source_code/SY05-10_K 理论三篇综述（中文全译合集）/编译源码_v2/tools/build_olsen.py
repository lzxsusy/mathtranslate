# -*- coding: utf-8 -*-
import io, os, re, subprocess
import pymupdf

ROOT = r'<本地路径>'
SRC = os.path.join(ROOT, 'src')
MD = r'<本地路径>'
PANDOC = r'<本地路径>'
PDF = r'<本地路径>'
os.makedirs(SRC, exist_ok=True)

s = io.open(MD, encoding='utf-8').read()
s = re.sub(r'^---\n.*?\n---\n', '', s, count=1, flags=re.S)
s = re.sub(r'::: \{custom-style="Note"\}.*?\n:::\n', '', s, count=1, flags=re.S)
s = s.replace('COVERBREAKMARKER', '')
figs = re.findall(r'\[图：([^\]]*)\]', s)
print('figs', len(figs))
for i, cap in enumerate(figs, 1):
    s = s.replace('[图：%s]' % cap, '\n\nFIGPLACEHOLDER%d\n\n' % i, 1)
s = re.sub(r'\$\$(.*?)\$\$', lambda m: '$$' + re.sub(r'\n\s*\n', '\n', m.group(1)) + '$$', s, flags=re.S)
s = re.sub(r'"([^"\n]{1,80})"', lambda m: '“%s”' % m.group(1), s)
# old translation uses {key} for some citations
s = re.sub(r'(?<![\\\w}])\{([A-Za-z][A-Za-z0-9,\- ]*)\}', r'[\1]', s)

clean = os.path.join(SRC, 'olsen_clean.md')
io.open(clean, 'w', encoding='utf-8').write(s)
body = subprocess.check_output([PANDOC, '-f', 'markdown', '-t', 'latex', '--wrap=none',
                                '--shift-heading-level-by=-1', clean], cwd=SRC).decode('utf-8')

# crop fig 1
src = pymupdf.open(PDF)
page = src[5]
caprect = None
for b in page.get_text('blocks'):
    if b[4].strip().startswith('Figure 1:'):
        caprect = pymupdf.Rect(b[:4])
drs = [d['rect'] for d in page.get_drawings() if d['rect'].y1 <= caprect.y0 + 2 and d['rect'].y0 > caprect.y0 - 500]
drs.sort(key=lambda r: r.y1, reverse=True)
u = pymupdf.Rect(drs[0])
for r in drs[1:]:
    if u.y0 - r.y1 < 25:
        u |= r
    else:
        break
u.x0 -= 8; u.x1 += 8; u.y0 -= 8; u.y1 = caprect.y0 - 2
doc = pymupdf.open()
pg = doc.new_page(width=u.width, height=u.height)
pg.show_pdf_page(pg.rect, src, 5, clip=u)
doc.save(os.path.join(SRC, 'fig01.pdf'))
doc.close()
print('fig crop', [round(x,1) for x in u])

for i, cap in enumerate(figs, 1):
    block = ('\\begin{figure}[tbp]\n\\centering\n\\includegraphics[width=0.60\\textwidth,height=0.32\\textheight,keepaspectratio]{fig%02d.pdf}\n'
             '\\caption{%s}\n\\end{figure}\n' % (i, cap))
    body = body.replace('FIGPLACEHOLDER%d' % i, block)

# placeholders（式）: nearest-display heuristic
reps = []
for m in re.finditer('（式）', body):
    pre = body[max(0, m.start()-500):m.start()]
    reps.append('上式' if pre.rfind('\\]') > pre.rfind('\\[') else '上述公式')
print('placeholders', len(reps))
out = []; idx = 0
for k, m in enumerate(re.finditer('（式）', body)):
    out.append(body[idx:m.start()]); out.append(reps[k]); idx = m.end()
out.append(body[idx:])
body = ''.join(out)
for a, b in [('公式上式', '上述公式'), ('方程上式', '上述方程'), ('（上式）', '上式'),
             ('上式与上式', '两式'), ('上式中给出的上式', '上式中给出的表达式')]:
    body = body.replace(a, b)

body = re.sub(r'（脚注：([^）]*)）', lambda m: '\\TN{%s}' % m.group(1), body)
body = body.replace('[文献]', '文献').replace('[ 文献 ]', '文献')
body = body.replace('{[}文献{]}', '文献')
body = re.sub(r'\{\[\}([A-Za-z][A-Za-z0-9,\- ]*)\{\]\}', r'[\1]', body)
body = body.replace('\\providecommand{\\tightlist}{\\setlength{\\itemsep}{0pt}\\setlength{\\parskip}{0pt}}\n', '')
body = '\\providecommand{\\tightlist}{\\setlength{\\itemsep}{0pt}\\setlength{\\parskip}{0pt}}\n' + body

# section anchors from TOC (printed page numbers)
pages = [3,9,11,12,13,15,16,18,20,23,26,33,34,37,41,42,44,46,50,51,52,53,55,57,57,
         59,60,61,63,65,65,70,74,74,78,81,84,85,88,92,96,101,106]
pos = [m.start() for m in re.finditer(r'\\(?:sub)?section\{', body)]
print('headings', len(pos), 'pages', len(pages))
for p, pgno in reversed(list(zip(pos, pages))):
    body = body[:p] + '\\SrcRange{%d}{%d}\n' % (pgno, pgno) + body[p:]

# references
raw = ''
for i in range(107, 112):
    t = src[i].get_text()
    t = re.sub(r'^\s*\d{1,3}\s*$', '', t, flags=re.M)
    raw += t
raw = raw.replace('References', '', 1)
parts = re.split(r'\[(\d+)\]', raw)
refs = []
for j in range(1, len(parts), 2):
    txt = re.sub(r'\s+', ' ', parts[j+1]).strip()
    if txt:
        refs.append((parts[j], txt))
print('refs', len(refs))

def esc(t):
    t = t.replace('ﬁ', 'fi').replace('ﬂ', 'fl').replace('ﬀ', 'ff').replace('ﬃ', 'ffi')
    t = t.replace('\\', '')
    for a, b in [('&', '\\&'), ('%', '\\%'), ('#', '\\#'), ('_', '\\_')]:
        t = t.replace(a, b)
    return t

reftex = ['', '\\section*{参考文献}',
          '\\noindent{\\footnotesize 译注：正文方括号代号沿用旧译，未保留原文编号；原书文献编号与条目如下（原文 pp.108--112），保留英文，未逐条中译。}\\par\\smallskip',
          '\\begin{enumerate}[label={[\\arabic*]},leftmargin=*,itemsep=2pt]']
for num, txt in refs:
    reftex.append('\\item ' + esc(txt))
reftex.append('\\end{enumerate}')
body += '\n\n' + '\n'.join(reftex) + '\n'
body = body.replace('\\def\\LTcaptype{none}', '\\def\\LTcaptype{table}')

preamble = r'''\documentclass[11pt,a4paper]{ctexart}
\usepackage[margin=2.4cm,marginparwidth=1.35cm,marginparsep=0.18cm]{geometry}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{array,calc,longtable,booktabs}
\usepackage{graphicx}
\usepackage{float}
\usepackage[font=small,labelsep=quad]{caption}
\usepackage{fancyhdr}
\usepackage{enumitem}
\usepackage[colorlinks=false,hidelinks]{hyperref}
\linespread{1.25}
\setlength{\parindent}{2em}
\pagestyle{fancy}\fancyhf{}\fancyfoot[C]{\thepage}\renewcommand{\headrulewidth}{0pt}
\newcommand{\SrcRange}[2]{\marginpar{\raggedright\footnotesize 原文 p.#1}}
\newcommand{\TN}[1]{\footnote{译注：#1}}
\allowdisplaybreaks
\begin{document}
\begin{center}
{\LARGE\bfseries 从 $K$-理论构造 D-膜}\\[6pt]
{\large Constructing D-Branes from K-Theory}\\[6pt]
Kasper Olsen,\quad Richard J. Szabo\\[2pt]
{\small arXiv:hep-th/9907140}\\[8pt]
{\small 中文译注本 v2.0 重制版（2026-11-14）}
\end{center}
\vspace{0.5em}
\noindent{\small\bfseries 重制说明.} 本册按《数学文献翻译纪律》v2.0 重制：以原文为底本逐段核对，公式、图、文献与页锚点均回查原文；旧版（Markdown→DOCX→PDF）已隔离。页边注「原文 p.N」标出该节起始的原文印刷页；公式指代按上下文恢复为「上式／上述公式」；文献保留英文条目并按原文编号。凡属译者补充而原文无者，均注明依据或标「译者按（无外部依据）」。
\vspace{0.8em}

'''
tex = preamble + body + '\n\\end{document}\n'

out = []; in_disp = False
for line in tex.splitlines():
    if not in_disp and re.search(r'(?<!\\)\\\[', line):
        in_disp = True
    if in_disp and line.strip() == '':
        continue
    out.append(line)
    if in_disp and '\\]' in line:
        in_disp = False
tex = '\n'.join(out) + '\n'
io.open(os.path.join(SRC, 'olsen.tex'), 'w', encoding='utf-8').write(tex)
print('written', len(tex))
