#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""check_track.py — 罗塞塔词典单轨道自检：编译 + 规范 lint

用法：
    python tools/check_track.py entries/t1-duality.tex

输出：errors=N warnings=M，并列出具体问题（file:line）。
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
XELATEX = r'C:\Users\admin\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe'

REQUIRED = ['mathdef', 'mathex', 'physdef', 'physex', 'bridge', 'intuit', 'pitfall']
UNICODE_MATH = '−×≤≥≠∈∀∃∑∫∞∂∇√±⊗⊕⟨⟩⊂⊃→⇒↦≅≈∖'
FORBIDDEN = [r'\usepackage', r'\documentclass', r'\newcommand', r'\input{', r'\begin{table}', r'\begin{figure}']


def lint(path):
    text = open(path, encoding='utf-8').read()
    problems = []
    # 环境配对
    nb, ne = text.count(r'\begin{word}'), text.count(r'\end{word}')
    if nb != ne:
        problems.append('P1 word 环境不配对：begin=%d end=%d' % (nb, ne))
    # 按词条切分，逐条检查
    chunks = re.split(r'\\begin\{word\}', text)[1:]
    for i, ch in enumerate(chunks, 1):
        head = ch.split('\n', 1)[0][:80]
        missing = [m for m in REQUIRED if ('\\' + m + '{') not in ch]
        if missing:
            problems.append('P1 第 %d 个词条缺区块 %s（%s）' % (i, ','.join(missing), head))
        # 计数：每个区块应恰好一次
        for m in REQUIRED:
            c = ch.count('\\' + m + '{')
            if c > 1:
                problems.append('P2 第 %d 个词条 %s 出现 %d 次（%s）' % (i, m, c, head))
        # 未闭合花括号粗检
        depth = 0
        for j, chr_ in enumerate(ch):
            if chr_ == '{' and (j == 0 or ch[j - 1] != '\\'):
                depth += 1
            elif chr_ == '}' and (j == 0 or ch[j - 1] != '\\'):
                depth -= 1
            if depth < 0:
                problems.append('P1 第 %d 个词条花括号提前闭合（%s）' % (i, head))
                break
        if depth != 0:
            problems.append('P1 第 %d 个词条花括号不配平 depth=%d（%s）' % (i, depth, head))
        # 词条字数（粗估：中文字符数）
        zh = len(re.findall(u'[\u4e00-\u9fff]', ch))
        if zh < 250:
            problems.append('P2 第 %d 个词条中文仅 %d 字（<250，%s）' % (i, zh, head))
    # 禁用命令
    for pat in FORBIDDEN:
        if re.search(re.escape(pat), text):
            problems.append('P1 出现禁用命令 %s' % pat)
    # Unicode 数学符号
    for chx in UNICODE_MATH:
        if chx in text:
            ln = text[:text.index(chx)].count('\n') + 1
            problems.append(u'P1 第 %d 行出现 Unicode 数学符号 %s' % (ln, chx))
    return problems, nb


def compile_track(path):
    os.chdir(ROOT)
    wrap = os.path.join(ROOT, 'chk_track.tex')
    open(wrap, 'w', encoding='utf-8').write(
        '\\input{preamble}\n\\begin{document}\n\\input{%s}\n\\end{document}\n'
        % os.path.splitext(path.replace('\\', '/'))[0])
    env = dict(os.environ)
    env['PATH'] = r'C:\Users\admin\AppData\Local\Programs\MiKTeX\miktex\bin\x64;' + env.get('PATH', '')
    p = subprocess.run([XELATEX, '-interaction=batchmode', '-file-line-error', 'chk_track.tex'],
                       cwd=ROOT, capture_output=True, text=True, encoding='utf-8', errors='replace')
    log = os.path.join(ROOT, 'chk_track.log')
    errors = []
    if os.path.exists(log):
        for line in open(log, encoding='utf-8', errors='replace').read().split('\n'):
            if re.match(r'^(?:\./)?\S+?:\d+: ', line) or line.startswith('!'):
                errors.append(line.strip()[:200])
    return errors


def main():
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
    if len(sys.argv) < 2:
        print('usage: python tools/check_track.py entries/t1-duality.tex')
        return 2
    path = sys.argv[1]
    if not os.path.isabs(path):
        path = os.path.join(ROOT, path)
    if not os.path.exists(path):
        print('file not found:', path)
        return 2
    problems, nb = lint(path)
    errors = compile_track(sys.argv[1])
    p1 = [p for p in problems if p.startswith('P1')]
    print('file: %s' % sys.argv[1])
    print('entries: %d' % nb)
    print('errors: %d  warnings: %d' % (len(p1) + len(errors), len(problems) - len(p1)))
    for e in errors:
        print('  [TeX] %s' % e)
    for p in problems:
        print('  [lint] %s' % p)
    return 0 if (not p1 and not errors) else 1


if __name__ == '__main__':
    sys.exit(main())
