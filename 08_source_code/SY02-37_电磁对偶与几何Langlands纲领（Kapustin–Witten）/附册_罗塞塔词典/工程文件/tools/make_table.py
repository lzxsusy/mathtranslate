#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""make_table.py — 从 entries/*.tex 生成附录 A（一行一对总表）

用法（在 rosetta 目录）：python tools/make_table.py
输出：appendix-table.tex（覆盖生成）

表格第三列 = 该词条 \\bridge{...} 段的首句骨架：
  * 删掉所有 \\begin{env}...\\end{env}（pmatrix/aligned 等，含 & 与 \\\\，会破坏列结构）；
  * 行内数学 $...$ 只有当内部不含 & / \\\\ 且长度 <= 40 时保留，否则整段删去；
  * 截到第一个句号（不切在数学中途）。
"""
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TRACKS = [
    ('t1-duality', u'T1 对偶、群论与耦合常数'),
    ('t2-twist', u'T2 超对称、扭化与拓扑场论'),
    ('t3-hitchin', u'T3 Hitchin 模空间与超凯勒几何'),
    ('t4-branes', u'T4 广义复几何、sigma 模型与膜'),
    ('t5-operators', u'T5 线算子、特征膜、单极子与 Hecke'),
    ('t6-langlands', u'T6 Langlands 对应、$\\mathcal D$-模与几何背景'),
    ('t7-deep', u'T7 深水区：盲测指出的四处机制补篇'),
]

BACKGROUND = u'Nahm 方程、Nahm 定理、相干层、导出范畴、环路群、opers、Dolbeault 上同调、Kac--Moody 代数'


def balanced_arg(text, start):
    """text[start] == '{'，返回括号内内容与结束位置。"""
    depth = 0
    i = start
    while i < len(text):
        ch = text[i]
        if ch == '\\':
            i += 2
            continue
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0:
                return text[start + 1:i], i + 1
        i += 1
    return '', len(text)


def find_macro(text, name):
    idx = text.find('\\' + name + '{')
    if idx < 0:
        return None
    return balanced_arg(text, idx + len(name) + 1)[0]


def strip_envs(s):
    for _ in range(30):
        m = re.search(r'\\begin\{([a-zA-Z*]+)\}', s)
        if not m:
            break
        env = m.group(1)
        end = s.find('\\end{%s}' % env)
        if end < 0:
            s = s[:m.start()]
            break
        s = s[:m.start()] + ' ' + s[end + len('\\end{%s}' % env):]
    return s


def clean_bridge(s):
    s = strip_envs(s)
    s = s.replace('$$', ' ')
    s = re.sub(r'\$\s*\$', ' ', s)
    # 处理行内数学
    parts = re.split(r'(\$[^$]*\$)', s)
    buf = []
    for part in parts:
        if part.startswith('$') and part.endswith('$') and len(part) > 2:
            inner = part[1:-1]
            if ('&' in inner) or ('\\\\' in inner) or len(inner) > 40:
                buf.append(' ')
            else:
                buf.append(part)
        else:
            part = re.sub(r'\\[a-zA-Z]+\*?', ' ', part)
            part = part.replace('~', ' ')
            part = part.replace('{', '').replace('}', '')
            buf.append(part)
    s = ''.join(buf)
    s = re.sub(r'\$\s*\$', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    # 截到第一个句号/分号（数学内的标点不会出现在这里：$..$ 段整体保留，内部无 。）
    cut = None
    for ch in (u'。', u'；'):
        p = s.find(ch)
        if p >= 0 and (cut is None or p < cut):
            cut = p
    if cut is not None:
        s = s[:cut]
    s = s.strip()
    if not s:
        return u'（见正文词条）'
    return s


def escape_cell(s, limit=70):
    """按数学状态逐字转义 & % # _，并做长度控制（不切在 $ 内）。"""
    out = []
    in_math = False
    for ch in s:
        if ch == '$':
            in_math = not in_math
            out.append(ch)
        elif not in_math and ch in '&%#_':
            out.append('\\' + ch)
        else:
            out.append(ch)
    t = ''.join(out)
    if in_math:                      # 平衡掉落单的 $
        t += '$'
    if len(t) > limit:
        # 找 limit 之前最后一个 $ 数为偶的位置
        cnt = 0
        pos = limit
        for i, ch in enumerate(t[:limit]):
            if ch == '$':
                cnt += 1
        if cnt % 2 == 1:
            prev = t.rfind('$', 0, limit)
            pos = prev if prev > 20 else limit
        t = t[:pos].rstrip()
        t = re.sub(u'[，、：；—（(\\s]+$', u'', t)
        t += u'……'
    return t


def main():
    rows = []
    for fname, title in TRACKS:
        path = os.path.join(ROOT, 'entries', fname + '.tex')
        if not os.path.exists(path):
            print('MISSING %s' % path)
            continue
        text = io.open(path, encoding='utf-8').read()
        for m in re.finditer(r'\\begin\{word\}\{([^{}]*)\}\{([^{}]*)\}\{([^{}]*)\}\{([^{}]*)\}', text):
            zh, en, anchor = m.group(1), m.group(2), m.group(4)
            body = text[m.end():]
            bridge = find_macro(body, 'bridge') or ''
            rows.append((title, zh.strip(), en.strip().replace('\\', ''),
                         escape_cell(clean_bridge(bridge))))

    out = [u'% rosetta/appendix-table.tex — 附录 A：一行一对的总表（由 tools/make_table.py 生成，勿手改）',
           r'\section{对照总表：一行一对}',
           r'\label{app:table}',
           '',
           u'本表把正文 %d 条词条压成一行一对（第一列词条名即「数学侧」，第二列为其英文原词，'
           u'第三列取该词条 \\texttt{bridge}（对应）段首句的骨架，长公式从略），供快速检索；'
           u'定义、例子、直觉与易错点见正文各轨道词条。' % len(rows),
           '',
           u'另有 %s 等 8 条原文只引用而未实质使用的背景术语（\\S 9.3 标 $\\dagger$），其最小可用定义见附录 B。' % BACKGROUND,
           '',
           r'\begingroup',
           r'\footnotesize',
           r'\renewcommand{\arraystretch}{1.12}',
           r'\begin{longtable}{@{}p{4.3cm}p{2.6cm}p{8.8cm}@{}}',
           r'\toprule',
           r'\bfseries 词条（数学侧） & \bfseries 英文原词 & \bfseries 一句话对应 \\',
           r'\midrule',
           r'\endfirsthead',
           r'\toprule',
           r'\bfseries 词条（数学侧） & \bfseries 英文原词 & \bfseries 一句话对应 \\',
           r'\midrule',
           r'\endhead',
           r'\bottomrule',
           r'\endlastfoot',
           '']
    cur = None
    for title, zh, en, summary in rows:
        if title != cur:
            cur = title
            out.append(u'\\multicolumn{3}{@{}l}{\\bfseries %s}\\\\' % title)
            out.append(r'\addlinespace[2pt]')
        out.append(u'%s & %s & %s \\\\' % (zh, en, summary))
    out += [r'\end{longtable}', r'\endgroup', '']

    dst = os.path.join(ROOT, 'appendix-table.tex')
    io.open(dst, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
    print('rows=%d -> %s' % (len(rows), dst))


if __name__ == '__main__':
    main()
