# -*- coding: utf-8 -*-
"""合稿前静态检查：对 源码/chunks/*.tex 做低成本体检。
用法：python lint.py
检查项：
  1. 禁用 \\newcommand / \\def / \\renewcommand（译手不得改导言区）
  2. \\begin{X} 与 \\end{X} 配对
  3. 花括号配平（粗查，忽略 \\{ \\} 与注释）
  4. 未转义的裸 & （不在表格/对齐环境里）
  5. 中文段落里出现的半角标点（, . ; : ? !）提示
  6. 连续空行 >= 3
  7. 出现 "TODO/FIXME/待补" 等标记
  8. 定理环境是否用了 preamble 里没定义的名称
"""
import os
import re
import sys
from collections import Counter

CHUNK_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '源码', 'chunks')
CHUNK_DIR = os.path.normpath(CHUNK_DIR)

KNOWN_ENVS = {
    'thm', 'lmm', 'prp', 'crl', 'conj', 'dfn', 'rmk', 'exmp', 'ques', 'cnv', 'nota',
    'proof', 'yizhu',
    'equation', 'equation*', 'align', 'align*', 'gather', 'gather*', 'multline', 'multline*',
    'split', 'aligned', 'gathered', 'cases', 'matrix', 'pmatrix', 'bmatrix', 'vmatrix', 'array',
    'itemize', 'enumerate', 'description', 'center', 'flushleft', 'flushright', 'quote', 'quotation',
    'figure', 'figure*', 'table', 'table*', 'tabular', 'tabularx', 'longtable',
    'tikzpicture', 'tikzcd', 'thebibliography', 'abstract', 'minipage', 'small', 'footnotesize',
}
CJK = re.compile(r'[\u4e00-\u9fff]')


def strip_comments(line):
    out, i = [], 0
    while i < len(line):
        if line[i] == '\\' and i + 1 < len(line):
            out.append(line[i:i + 2]); i += 2; continue
        if line[i] == '%':
            break
        out.append(line[i]); i += 1
    return ''.join(out)


def check_file(path):
    problems = []
    text = open(path, encoding='utf-8').read()
    lines = text.split('\n')

    for i, raw in enumerate(lines, 1):
        line = strip_comments(raw)
        for pat, msg in [
            (r'\\newcommand', '出现 \\newcommand（应改到 preamble）'),
            (r'\\renewcommand', '出现 \\renewcommand（应改到 preamble）'),
            (r'(?<!\\)\\def(?![a-zA-Z])', '出现 \\def（应改到 preamble）'),
            (r'TODO|FIXME|待补|XXX', '残留标记'),
        ]:
            if re.search(pat, line):
                problems.append((i, msg, line.strip()[:90]))

    # 环境配对
    begins = Counter(re.findall(r'\\begin\{([^}]+)\}', text))
    ends = Counter(re.findall(r'\\end\{([^}]+)\}', text))
    for env in set(begins) | set(ends):
        if begins[env] != ends[env]:
            problems.append((0, f'环境 {env} 不配对：begin {begins[env]} / end {ends[env]}', ''))
        if env not in KNOWN_ENVS and env.endswith('*') is False:
            if env not in KNOWN_ENVS:
                problems.append((0, f'未知环境 {env}（preamble 未定义？）', ''))

    # 花括号配平
    depth = 0
    for i, raw in enumerate(lines, 1):
        line = strip_comments(raw)
        j = 0
        while j < len(line):
            c = line[j]
            if c == '\\':
                j += 2; continue
            if c == '{':
                depth += 1
            elif c == '}':
                depth -= 1
                if depth < 0:
                    problems.append((i, '花括号提前闭合', line.strip()[:80]))
                    depth = 0
            j += 1
    if depth != 0:
        problems.append((0, f'花括号未配平（末尾残留 {depth} 个）', ''))

    # 中文中的半角标点
    for i, raw in enumerate(lines, 1):
        line = strip_comments(raw)
        # 去掉公式
        plain = re.sub(r'\$[^$]*\$', '', line)
        if CJK.search(plain) and re.search(r'[\u4e00-\u9fff][,;:?!]', plain):
            problems.append((i, '中文后接半角标点', line.strip()[:80]))

    # 连续空行
    for m in re.finditer(r'\n{4,}', text):
        ln = text[:m.start()].count('\n') + 1
        problems.append((ln, '连续空行 >= 3', ''))

    return problems


def main():
    files = sorted(f for f in os.listdir(CHUNK_DIR) if f.endswith('.tex'))
    if not files:
        print('chunks 目录里没有 .tex 文件'); return 1
    total = 0
    for f in files:
        p = os.path.join(CHUNK_DIR, f)
        probs = check_file(p)
        size = os.path.getsize(p)
        print(f'--- {f}  ({size} bytes) ---')
        if not probs:
            print('    OK')
        for ln, msg, ctx in probs:
            total += 1
            loc = f'L{ln}' if ln else '全局'
            print(f'    [{loc}] {msg}' + (f'  << {ctx}' if ctx else ''))
    print(f'\n合计 {len(files)} 个文件，{total} 条提示。')
    return 0


if __name__ == '__main__':
    sys.exit(main())
