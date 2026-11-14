# -*- coding: utf-8 -*-
import io, os, re, subprocess, sys

ROOT = r'<本地路径>'
SRC = os.path.join(ROOT, 'src')
MD = r'<本地路径>'
EPS = r'<本地路径>'
PANDOC = r'<本地路径>'
os.makedirs(SRC, exist_ok=True)

s = io.open(MD, encoding='utf-8').read()
s = re.sub(r'^---\n.*?\n---\n', '', s, count=1, flags=re.S)
s = re.sub(r'::: \{custom-style="Note"\}.*?\n:::\n', '', s, count=1, flags=re.S)
s = s.replace('COVERBREAKMARKER', '')

figs = re.findall(r'\[图：([^\]]*)\]', s)
assert len(figs) == 12, len(figs)
for i, cap in enumerate(figs, 1):
    s = s.replace('[图：%s]' % cap, '\n\nFIGPLACEHOLDER%d\n\n' % i, 1)

# collapse blank lines inside $$ ... $$ (pandoc turns them into paragraph breaks)
s = re.sub(r'\$\$(.*?)\$\$', lambda m: '$$' + re.sub(r'\n\s*\n', '\n', m.group(1)) + '$$', s, flags=re.S)
# straight double quotes -> Chinese quotes (paired within a line)
s = re.sub(r'"([^"\n]{1,80})"', lambda m: '“%s”' % m.group(1), s)

clean = os.path.join(SRC, 'moore_clean.md')
io.open(clean, 'w', encoding='utf-8').write(s)
body = subprocess.check_output([PANDOC, '-f', 'markdown', '-t', 'latex', '--wrap=none',
                                '--shift-heading-level-by=-1', clean], cwd=SRC).decode('utf-8')

# figure blocks
fig_files = ['pantsinteraction2bw.eps', 'openinteractionbw.eps', 'cardycondition1bw.eps',
             'cardycondition2bw.eps', 'anomcancellationbw.eps', 'Dinstabilitybw.eps',
             'D0violation1bw.eps', 'D0violation2bw.eps', 'D0violation3bw.eps',
             'verlindeclassesbw.eps', 'D0distancebw.eps', 'rotatedbranebw.eps']
for i in range(12, 0, -1):
    cap = figs[i - 1]
    pdf = os.path.join(SRC, 'fig%02d.pdf' % i)
    block = ('\\begin{figure}[tbp]\n\\centering\n\\includegraphics[width=0.28\\textwidth,height=0.22\\textheight,keepaspectratio]{%s}\n'
             '\\caption{%s}\n\\end{figure}\n' % (os.path.basename(pdf), cap))
    body = body.replace('FIGPLACEHOLDER%d' % i, block)

# placeholder replacements, in order (27)
reps = [
    '上式',                      # 1 由(式)可知 after g=rank(E)
    '上述边界相互作用',            # 2
    '上述边界数据',               # 3
    '上式',                      # 4 如(式)所示
    '上式',                      # 5 在(式)上诱导
    '上述极限',                  # 6 极限(式)
    '所需表达式',                 # 7 即得(式)
    '上式',                      # 8 由(式)得到
    '前者',                      # 9 虽然(式)显然
    '后者',                      # 10 (式)却有明确含义
    '上述方程',                  # 11 利用方程(式)
    '上述公式',                  # 12 涵盖(式)中
    '上述公式',                  # 13 类似(式)的极限
    '上述表达式',                 # 14 计算(式)的 q_o
    '上式',                      # 15 (式)里 q_o
    '上述公式',                  # 16 公式(式)恰好
    '上述公式',                  # 17 玻色情形(式)
    '上式',                      # 18 根据(式)可知
    '见上式',                    # 19 g-函数(式)
    '上述 Chan-Paton 线丛',        # 20
    '上面的公式',                 # 21 与上面的(式)
    '上述受微扰的作用量',          # 22
    '上式',                      # 23 (式)中第三项
    '上述公式',                  # 24 证明(式)的简便方法
    '上述公式',                  # 25 给出(式)的直接证明
    '上述公式',                  # 26 (式)右边多于一项
    '上述公式',                  # 27 可用(式)确定
]
n = body.count('（式）')
assert n == 27, n
out = []
idx = 0
for k, m in enumerate(re.finditer('（式）', body)):
    out.append(body[idx:m.start()])
    out.append(reps[k])
    idx = m.end()
out.append(body[idx:])
body = ''.join(out)
for a in ['上式', '上述方程', '上述公式', '上述表达式', '上述极限', '上述边界相互作用', '上述边界数据', '上述受微扰的作用量']:
    body = body.replace('（%s）' % a, a)

# fix figure cross-references that were wrong in the old translation
fig_fix = [
    ('的 D-膜上，如图 1 所示', '的 D-膜上，如图 5 所示'),
    ('半无限区间，如图 2 所示。', '半无限区间，如图 6 所示。'),
    ('图 2 提示了一个清晰的物理解释', '图 6 提示了一个清晰的物理解释'),
    ('但图 2 所描绘的过程', '但图 6 所描绘的过程'),
    ('破坏 D0-膜荷，如图 3 所示', '破坏 D0-膜荷，如图 7 所示'),
    ('由于图 4 的标准过程', '由于图 8 的标准过程'),
    ('如图 5 所示：其中一条 3-链', '如图 9 所示：其中一条 3-链'),
    ('可如（图 2）所描绘', '可如（图 11）所描绘'),
    ('如（图 1）那样一次缠绕', '如（图 10）那样一次缠绕'),
    ('如（图 3）所示。让我们问', '如（图 12）所示。让我们问'),
]
for a, b in fig_fix:
    if a in body:
        body = body.replace(a, b)
    else:
        print('FIGREF MISS:', a)

body = body.replace('给定上述边界数据中的边界数据', '给定边界数据')
for n in (10, 11, 12):
    body = body.replace('（图 %d）' % n, '图 %d' % n)

# citation placeholders [文献]
body = body.replace('{[}文献{]}}', '文献')
body = body.replace('{[}文献{]}', '文献')
body = body.replace('{[}文献{]', '文献')
body = body.replace('[文献]', '文献')
body = body.replace('文献}', '文献')

# parenthetical footnotes
body = re.sub(r'（脚注：([^）]*)）', lambda m: '\\TN{%s}' % m.group(1), body)

# tightlist macro for pandoc lists
body = '\\providecommand{\\tightlist}{\\setlength{\\itemsep}{0pt}\\setlength{\\parskip}{0pt}}\n' + body

# section page anchors (insert before the 1st..6th \section, regardless of texorpdfstring)
anchors = ['\\SrcRange{2}{2}', '\\SrcRange{3}{6}', '\\SrcRange{7}{15}',
           '\\SrcRange{16}{22}', '\\SrcRange{23}{36}', '\\SrcRange{37}{37}']
pos = [m.start() for m in re.finditer(r'\\section\{', body)]
print('sections', len(pos))
assert len(pos) == 6, len(pos)
for p, a in reversed(list(zip(pos, anchors))):
    body = body[:p] + a + '\n' + body[p:]

# references
raw = ''
for i in range(38, 45):
    t = io.open(os.path.join(ROOT, os.pardir, '原文', 'moore', 'p%02d.txt' % i), encoding='utf-8').read()
    t = re.sub(r'^\s*\d{1,3}\s*$', '', t, flags=re.M)
    raw += t
raw = raw.replace('References', '', 1)
parts = re.split(r'\[(\d+)\]', raw)
refs = []
for j in range(1, len(parts), 2):
    num = parts[j]
    txt = re.sub(r'\s+', ' ', parts[j+1]).strip()
    refs.append((num, txt))
print('refs', len(refs))

def esc(t):
    t = t.replace('ﬁ', 'fi').replace('ﬂ', 'fl').replace('ﬀ', 'ff').replace('ﬃ', 'ffi')
    t = t.replace('\\', '')
    for a, b in [('&', '\\&'), ('%', '\\%'), ('#', '\\#'), ('_', '\\_')]:
        t = t.replace(a, b)
    return t

reftex = ['', '\\section*{参考文献}',
          '\\noindent{\\footnotesize 译注：参考文献保留原文英文条目，编号与原文一致；未逐条中译，以免二次转写失真。}\\par\\smallskip',
          '\\begin{enumerate}[label={[\\arabic*]},leftmargin=*,itemsep=2pt]']
for num, txt in refs:
    reftex.append('\\item ' + esc(txt))
reftex.append('\\end{enumerate}')
body += '\n\n' + '\n'.join(reftex) + '\n'

preamble = r'''\documentclass[11pt,a4paper]{ctexart}
\usepackage[margin=2.45cm,marginparwidth=1.35cm,marginparsep=0.18cm]{geometry}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{graphicx}
\usepackage{float}
\usepackage[font=small,labelsep=quad]{caption}
\usepackage{fancyhdr}
\usepackage{enumitem}
\usepackage[colorlinks=false,hidelinks]{hyperref}
\linespread{1.28}
\setlength{\parindent}{2em}
\pagestyle{fancy}\fancyhf{}\fancyfoot[C]{\thepage}\renewcommand{\headrulewidth}{0pt}
\newcommand{\SourcePage}[1]{\marginpar{\raggedright\footnotesize 原文 p.#1}}
\newcommand{\SrcRange}[2]{\ifnum#1=#2\marginpar{\raggedright\footnotesize 原文 p.#1}\else\marginpar{\raggedright\footnotesize 原文 pp.#1--#2}\fi}
\newcommand{\TN}[1]{\footnote{译注：#1}}
\allowdisplaybreaks
\begin{document}
\begin{center}
{\LARGE\bfseries 从物理视角看 $K$-理论}\\[6pt]
{\large K-Theory from a Physical Perspective}\\[6pt]
Gregory Moore\\[2pt]
{\small arXiv:hep-th/0304018}\\[8pt]
{\small 中文译注本 v2.0 重制版（2026-11-14）}
\end{center}
\vspace{0.6em}
\noindent{\small\bfseries 重制说明.} 本册按《数学文献翻译纪律》v2.0 重制：以原文为底本逐段核对，公式、图、文献与页锚点均回查原文；旧版（Markdown→DOCX→PDF）已隔离。页边注「原文 pp.N--M」标出该节对应的原文页码范围；文献保留英文条目与原文编号。凡属译者补充而原文无者，均注明依据或标「译者按（无外部依据）」。
\vspace{1em}

'''
tex = preamble + body + '\n\\end{document}\n'

def collapse_disp_blank_lines(t):
    out = []
    in_disp = False
    for line in t.splitlines():
        if not in_disp and re.search(r'(?<!\\)\\\[', line):
            in_disp = True
        if in_disp and line.strip() == '':
            continue
        out.append(line)
        if in_disp and '\\]' in line:
            in_disp = False
    return '\n'.join(out) + '\n'

tex = collapse_disp_blank_lines(tex)
io.open(os.path.join(SRC, 'moore.tex'), 'w', encoding='utf-8').write(tex)
print('written', len(tex))
