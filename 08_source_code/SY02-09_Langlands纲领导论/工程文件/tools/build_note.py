# -*- coding: utf-8 -*-
"""把 work/读书笔记.md 编成独立 PDF（与译本同风格的排印），供入库成品使用。

用法: python build_note.py
输出: note/读书笔记.pdf
"""
import io
import os
import re
import subprocess
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
WORK = BASE
NOTE = os.path.join(os.path.dirname(BASE), 'note')
os.makedirs(NOTE, exist_ok=True)

MIK = r'<本地路径>'
PANDOC = r'<本地路径>'

md_path = os.path.join(WORK, '读书笔记.md')
src = io.open(md_path, encoding='utf-8').read()

# 去掉一级标题（标题由 wrapper 生成），并抽出正文
lines = src.split('\n')
assert lines[0].startswith('# '), lines[0]
title = lines[0][2:].strip()
body_md = '\n'.join(lines[1:]).lstrip('\n')
# 字体缺字替换：制表线 → em dash；双向箭头 → 数学符号
body_md = body_md.replace('\u2500', '\u2014').replace('\u2194', '$\\leftrightarrow$')
body_md = body_md.replace('\u2245', '$\\cong$').replace('\u2260', '$\\neq$')
# 制表符统一降级为 ASCII（等宽字体未必覆盖全部框线字符）
for _a, _b in (('\u250c', '+'), ('\u2510', '+'), ('\u2514', '+'), ('\u2518', '+'),
               ('\u251c', '+'), ('\u2524', '+'), ('\u252c', '+'), ('\u2534', '+'),
               ('\u253c', '+'), ('\u2502', '|'), ('\u2501', '-')):
    body_md = body_md.replace(_a, _b)
body_md = body_md.replace('一般 $G$ 的线', '一般 G 的线')
tmp_md = os.path.join(NOTE, '_body.md')
io.open(tmp_md, 'w', encoding='utf-8').write(body_md)

# pandoc: markdown -> latex body
body_tex = os.path.join(NOTE, '_body.tex')
subprocess.run([PANDOC, tmp_md, '-f', 'markdown', '-t', 'latex',
                '--top-level-division=section', '-o', body_tex], check=True)

WRAP = r'''\documentclass[11pt,a4paper]{ctexart}
\usepackage{geometry}
\geometry{left=2.6cm,right=2.6cm,top=2.6cm,bottom=2.4cm}
\usepackage{xeCJK}
\setCJKmainfont{SimSun}[BoldFont=SimHei,ItalicFont=KaiTi]
\setCJKsansfont{SimHei}
\setCJKmonofont{FangSong}
\setmonofont{Consolas}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{unicode-math}
\setmathfont{NewCMMath-Regular.otf}
\usepackage{xcolor}
\usepackage{longtable,booktabs,array}
\usepackage{calc}
\usepackage{titlesec}
\usepackage{enumitem}
\usepackage{xurl}
\usepackage[hidelinks]{hyperref}
\definecolor{ebblue}{RGB}{31,95,191}
\definecolor{ebgray}{RGB}{90,90,90}
\titleformat{\section}{\Large\bfseries\color{ebblue}}{\thesection}{0.6em}{}
\titlespacing*{\section}{0pt}{2.2ex plus .4ex}{1.0ex plus .2ex}
\titleformat{\subsection}{\large\bfseries\color{ebblue}}{\thesubsection}{0.5em}{}
\titlespacing*{\subsection}{0pt}{1.8ex plus .3ex}{0.8ex plus .2ex}
\setlength{\parindent}{2em}
\linespread{1.28}
\setlist[itemize]{leftmargin=2.2em,itemsep=0.15em,topsep=0.3em}
\setlist[enumerate]{leftmargin=2.4em,itemsep=0.15em,topsep=0.3em}
\renewenvironment{quote}{\begin{list}{}{\leftmargin=2em\rightmargin=1.5em}\item\relax\small\color{ebgray}}{\end{list}}
\newcommand{\znotetitle}[1]{}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\newcounter{none}
\usepackage{etoolbox}
\AtBeginEnvironment{longtable}{\small}
\setcounter{secnumdepth}{-1}
\pagestyle{plain}
\begin{document}
\begin{center}
{\LARGE\bfseries\color{ebblue} %(title)s\par}
\vspace{0.7em}
{\large\color{ebgray} 读书笔记 · 概念地图与核心框架\par}
\vspace{0.4em}
{\small\color{ebgray} 依据 Yao YUAN《Langlands Program: an introduction》(2020 春, 23 讲, 原稿 198 页) 中文译注本\par}
\end{center}
\vspace{0.6em}
\input{_body}
\end{document}
'''

tex_path = os.path.join(NOTE, '读书笔记.tex')
io.open(tex_path, 'w', encoding='utf-8').write(WRAP.replace('%(title)s', title))

env = dict(os.environ)
env['PATH'] = MIK + ';' + env['PATH']
for i in range(2):
    r = subprocess.run(['xelatex', '-interaction=nonstopmode', '-halt-on-error',
                        '读书笔记.tex'], cwd=NOTE, env=env,
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if r.returncode != 0:
        out = r.stdout.decode('utf-8', 'replace')
        print(out[-3000:])
        sys.exit(1)
print('ok', tex_path)
