# -*- coding: utf-8 -*-
"""Build the merged manuscript markdown from v2 chapter files, then (optionally) the PDF.

Usage:
  python make_book.py          # merge only
  python make_book.py --pdf    # merge + pandoc/xelatex PDF
"""
import io, os, re, sys, subprocess

BASE = r'C:\Users\admin\Desktop\待翻译\译注_Elliott2016'
V2 = os.path.join(BASE, 'v2')

YAML = """---
title: "几何朗兰兹对应的规范场论面向"
subtitle: "Gauge Theoretic Aspects of the Geometric Langlands Correspondence"
author: "Chris Elliott　著　｜　中译校注本"
date: "2016 年 6 月（西北大学博士学位论文）　·　中译本 2026 年 11 月"
lang: zh-CN
---
"""

ORDER = ['01_前置.md', '02_第1章.md', '03_第1部分.md', '04_第2部分.md',
         '05_第3部分.md', '06_附录.md', '07_参考文献.md', '08_校订说明.md']

# Figures: the Markdown embeds a PNG so it shows up in ordinary viewers, but the PDF gets
# the vector TikZ (traced from the source paths) in its place.
TIKZ_DIR = r'C:\Users\admin\Desktop\待翻译\_work\tikz'
FIG_SCALE = {'fig-5-1': 0.96, 'fig-6-1': 1.0, 'fig-6-2': 1.12, 'fig-6-3': 0.98}
IMG_RE = re.compile(r'^!\[\]\(images/(fig-[0-9-]+)\.png\)\s*$', re.M)


def figures_to_tikz(s):
    def sub(m):
        name = m.group(1)
        tex = io.open(os.path.join(TIKZ_DIR, name + '.tex'), encoding='utf-8').read()
        body = tex[tex.index('\\begin{tikzpicture}'):].strip()
        scale = FIG_SCALE.get(name, 1.0)
        body = body.replace('[x=1cm,y=1cm,', '[x=1cm,y=1cm,scale=%.2f,' % scale, 1)
        return '\\begin{center}\n' + body + '\n\\end{center}'
    return IMG_RE.sub(sub, s)


# unicode-math is loaded by pandoc's template (because CJKmainfont/mainfont are given),
# and its \mathbb & friends want a braced argument when they appear as a script.
SCRIPT = re.compile(r'([_^])(\\(?:mathbb|mathbf|mathcal|mathrm|mathfrak|mathsf|operatorname)\s*\{[^{}]*\})')


def brace_scripts(s):
    out, n, pos = [], 0, 0
    for m in SCRIPT.finditer(s):
        # skip when the script is already braced: _{...}
        before = s[max(0, m.start() - 1):m.start()]
        if before == '{':
            continue
        out.append(s[pos:m.start()])
        out.append(m.group(1) + '{' + m.group(2) + '}')
        pos = m.end()
        n += 1
    out.append(s[pos:])
    return ''.join(out), n


def main():
    have = [n for n in ORDER if os.path.exists(os.path.join(V2, n))]
    chunks = [YAML]
    for n in have:
        t = io.open(os.path.join(V2, n), encoding='utf-8').read().strip('\n')
        chunks.append(t)
    text = '\n\n\\newpage\n\n'.join(chunks) + '\n'
    nfig = len(IMG_RE.findall(text))
    text, nfix = brace_scripts(text)
    out = os.path.join(V2, 'Elliott2016_中文译注本_v2.md')
    io.open(out, 'w', encoding='utf-8').write(text)
    cjk = len(re.findall(r'[\u4e00-\u9fff]', text))
    print('merged ->', out)
    print('  chars', len(text), 'cjk', cjk, 'script-braced', nfix, 'figures', nfig, 'files', have)

    if '--pdf' in sys.argv:
        # The PDF build gets the vector TikZ in place of the Markdown PNG references.
        build = os.path.join(V2, 'Elliott2016_中文译注本_v2_build.md')
        io.open(build, 'w', encoding='utf-8').write(figures_to_tikz(text))
        pdf = os.path.join(V2, 'Elliott2016_中文译注本_v2.pdf')
        cmd = ['pandoc', os.path.basename(build), '-o', os.path.basename(pdf),
               '--pdf-engine=xelatex',
               '-V', 'CJKmainfont=Microsoft YaHei',
               '-V', 'mainfont=Times New Roman',
               '-V', 'fontsize=11pt',
               '-V', 'geometry:margin=2.5cm',
               '--toc', '-V', 'toc-title=目录',
               '-V', r'header-includes=\usepackage{mathtools}\usepackage{tikz}']
        env = dict(os.environ)
        env['PATH'] = r'C:\Users\admin\AppData\Local\Programs\MiKTeX\miktex\bin\x64;' + env.get('PATH', '')
        print('running pandoc ->', os.path.basename(pdf))
        r = subprocess.run(cmd, cwd=V2, env=env, capture_output=True, text=True, encoding='utf-8', errors='replace')
        if os.path.exists(pdf):
            print('  PDF OK', os.path.getsize(pdf), 'bytes')
        else:
            print('  PDF FAILED')
            print((r.stdout or '')[-3000:])
            print((r.stderr or '')[-3000:])


if __name__ == '__main__':
    main()
