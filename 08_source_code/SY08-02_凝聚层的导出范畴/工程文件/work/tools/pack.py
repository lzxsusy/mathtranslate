# -*- coding: utf-8 -*-
"""生成交付物：术语对照表.tsv、译注汇总.md、统计数据.txt、阅读参考指南骨架。

数据来源：
  * 术语：src/chunks/appendix_a.tex 的 \termitem{中文}{英文}
  * 译注：src/chunks/*.tex 里的 % [Tutor Note: ...] 与 \yizhu{...}
  * 统计：chunks 行数、陈述数、公式数、页标记数
输出目录：工程文件/deliverable/
"""
import io, os, re, glob, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(ROOT, 'src', 'chunks')
OUT = os.path.join(ROOT, '工程文件', 'deliverable')
os.makedirs(OUT, exist_ok=True)

ORDER = ['ch00a', 'ch01a', 'ch01b', 'ch02a', 'ch02b', 'ch03a', 'ch03b',
         'ch03c', 'ch03d', 'ch04', 'ch05a', 'ch05b', 'refs',
         'appendix_a', 'appendix_b', 'appendix_c', 'appendix_d']

CHNAME = {
    'ch00a': '引言', 'ch01a': '1.1', 'ch01b': '1.2–1.3', 'ch02a': '2.1',
    'ch02b': '2.2', 'ch03a': '3.1–3.2', 'ch03b': '3.3', 'ch03c': '3.4',
    'ch03d': '3.5', 'ch04': '第 4 章', 'ch05a': '5.1', 'ch05b': '5.2–5.3',
    'refs': '参考文献', 'appendix_a': '附录 A', 'appendix_b': '附录 B',
    'appendix_c': '附录 C', 'appendix_d': '附录 D',
}

PAGE = re.compile(r'%\s*\[原文\s*p\.(\d+)\]')
NOTE = re.compile(r'%\s*\[Tutor Note:(.*?)\]', re.S)
YIZHU = re.compile(r'\\yizhu\{')
STMT = re.compile(r'\\begin\{(theorem|proposition|lemma|corollary|definition|'
                  r'example|remark|notation|question|problem|conjecture|'
                  r'assumption|counterexample)p?\}'
                  r'(?:\[(?:[^\[\]]|\[[^\[\]]*\])*\])?\{([^}]*)\}')


def balanced(s, i):
    """s[i] == '{'，返回配平的右括号下标。"""
    d = 0
    for j in range(i, len(s)):
        if s[j] == '{':
            d += 1
        elif s[j] == '}':
            d -= 1
            if d == 0:
                return j
    return -1


def yizhus(src):
    out = []
    for m in YIZHU.finditer(src):
        i = m.end() - 1
        j = balanced(src, i)
        if j > 0:
            out.append(src[i + 1:j])
    return out


def page_of(src, pos):
    v = None
    for m in PAGE.finditer(src):
        if m.start() <= pos:
            v = int(m.group(1))
        else:
            break
    return v


def main():
    stats = {}
    terms = []
    notes_rows = []
    for p in sorted(glob.glob(os.path.join(CH, '*.tex'))):
        s = io.open(p, encoding='utf-8').read()
        if os.path.basename(p).startswith('_'):
            continue
        name = os.path.splitext(os.path.basename(p))[0]
        stats[name] = dict(
            lines=s.count('\n') + 1,
            chars=len(s),
            pages=len(PAGE.findall(s)),
            stmts=len(STMT.findall(s)),
            tags=len(re.findall(r'\\tag\{', s)),
            yizhu=len(yizhus(s)),
            tutor=len(NOTE.findall(s)),
        )

    # 术语对照表
    a = os.path.join(CH, 'appendix_a.tex')
    if os.path.exists(a):
        s = io.open(a, encoding='utf-8').read()
        for m in re.finditer(r'\\termitem\{([^}]*)\}\{([^}]*)\}', s):
            terms.append((m.group(2).strip(), m.group(1).strip()))
    with io.open(os.path.join(OUT, '术语对照表.tsv'), 'w', encoding='utf-8') as f:
        f.write('英文\t中文\n')
        for en, zh in sorted(set(terms)):
            f.write('%s\t%s\n' % (en, zh))

    # 译注汇总
    rows = []
    for tag in ORDER:
        p = os.path.join(CH, tag + '.tex')
        if not os.path.exists(p):
            continue
        s = io.open(p, encoding='utf-8').read()
        for m in NOTE.finditer(s):
            rows.append((tag, page_of(s, m.start()), '校勘', m.group(1).strip()))
        for m in YIZHU.finditer(s):
            i = m.end() - 1
            j = balanced(s, i)
            body = s[i + 1:j] if j > 0 else ''
            rows.append((tag, page_of(s, i), '译注', body))
    with io.open(os.path.join(OUT, '译注汇总.md'), 'w', encoding='utf-8') as f:
        f.write('# 译注与校勘汇总\n\n共 %d 条（其中正文可见译注 %d 条、内部校勘 %d 条）。\n\n'
                % (len(rows), sum(1 for r in rows if r[2] == '译注'),
                   sum(1 for r in rows if r[2] == '校勘')))
        cur = None
        for tag, page, kind, body in rows:
            if tag != cur:
                f.write('\n## %s\n\n' % CHNAME.get(tag, tag))
                cur = tag
            body = re.sub(r'\s+', ' ', body)
            f.write('- **[%s]** 原书 p.%s — %s\n' % (kind, page if page else '?', body))

    # 统计
    tot = lambda k: sum(v[k] for v in stats.values())
    lines = ['# 统计数据', '', '| 块 | 中文节 | 行数 | 字符 | 页标记 | 陈述 | 编号公式 | 译注 | 校勘 |',
             '| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |']
    for tag in ORDER:
        v = stats.get(tag)
        if not v:
            continue
        lines.append('| %s | %s | %d | %d | %d | %d | %d | %d | %d |'
                     % (tag, CHNAME.get(tag, tag), v['lines'], v['chars'], v['pages'],
                        v['stmts'], v['tags'], v['yizhu'], v['tutor']))
    lines += ['', '合计：%d 行、%d 字符、%d 个页标记、%d 条陈述、%d 个编号公式、'
              '%d 条译注、%d 条校勘。'
              % (tot('lines'), tot('chars'), tot('pages'), tot('stmts'),
                 tot('tags'), tot('yizhu'), tot('tutor'))]
    with io.open(os.path.join(OUT, '统计数据.txt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')

    print('\n'.join(lines[-1:]))
    print('terms:', len(terms), 'notes:', len(rows))


main()
