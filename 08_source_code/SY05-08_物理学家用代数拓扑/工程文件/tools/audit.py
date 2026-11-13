#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Gate1 静态审查：页锚点 / 陈述编号 / 公式编号 / 图 / 批注。

用法：
  python tools/audit.py ch02        # 审查一个 chunk
  python tools/audit.py --all       # 审查全部已存在的 chunk

判据（全部通过才打印 PASS）：
  1. 页锚点：章内每一页都有 "% [原文 p.N]"，且顺序递增无重号；
  2. 陈述编号：tex 中 \begin{env}{X.Y} 的编号集合 == work\statements.txt 中该章编号集合；
  3. 公式编号：tex 中 \tag{X.Y} 的编号集合 ⊇ 原书该章页面上出现的 (X.Y)；
  4. 图：\includegraphics 数量 == 该章 figures_index 中图数，且文件存在；
  5. 批注：% [Tutor Note 数量 / 千汉字 ≤ 1.0。
"""
import os
import re
import sys
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CHAPTERS = {
    'ch01': (5, 10), 'ch02': (10, 27), 'ch03': (28, 45), 'ch04': (45, 73),
    # 章界以「章正文归属」为准：ch06 含 p.102 上半（Theorem 6.51/Example 6.52/(6.53)），
    # ch07 从 p.102 的 \chapter 起；ch09 含 p.141 上半（§9.5 与 (9.43)–(9.45)），ch10 从 p.141 的 \chapter 起。
    'ch05': (74, 88), 'ch06': (89, 102), 'ch07': (102, 117), 'ch08': (118, 128),
    'ch09': (130, 141), 'ch10': (141, 151), 'ch11': (152, 169), 'ch12': (170, 188),
    'ch13': (189, 201), 'ch99_refs': (202, 206),
}

ENVS = ('definition', 'theorem', 'lemma', 'proposition', 'corollary', 'example',
        'remark', 'assumption', 'notation', 'question', 'problem', 'exercise',
        'conjecture', 'claim', 'note')

# 已明确归属上一章的编号陈述：本章 chunk 里不应再出现（否则整书合并会重复）
# ch03 页段含 p.45 上半（第 3 章末段，含式 3.57），但 p.45 的编号陈述属第 4 章 §4.1
EXCLUDE_STMT = {'ch07': {'6.51', '6.52'}}
EXCLUDE_STMT['ch03'] = {'4.1', '4.3', '4.4', '4.5'}

# 章末/章首跨页内容归属本章、但页段外仍有公式的例外页（只参与公式编号核对，不要求页锚点）
EXTRA_TAG_PAGES = {'ch08': [118], 'ch11': [170], 'ch13': [202]}

# 该章允许「图数量」与 figures_index 不一致（ch13 有 6 处网格/谱序列图被原书编号为公式，按原图裁切保留）
ALLOW_EXTRA_FIG = {'ch13'}

RE_ANCHOR = re.compile(r'%\s*\[\u539f\u6587\s*p\.\s*(\d+)\]')
RE_TAG = re.compile(r'<本地路径>]+\.[0-9]+)\}')
RE_STMT = re.compile(r'<本地路径>' + '|'.join(ENVS) + r')\*?\}\{([0-9]+\.[0-9]+)\}')
RE_EQ_PAGE = re.compile(r'\(([0-9]+\.[0-9]+)\)')
RE_INCLUDE = re.compile(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}')
RE_NOTE = re.compile(r'%\s*\[Tutor Note')
RE_CJK = re.compile(r'[\u4e00-\u9fff]')


def load_statements():
    """work/statements.txt -> {(page, num): type}"""
    out = {}
    path = os.path.join(ROOT, 'work', 'statements.txt')
    if not os.path.exists(path):
        return out
    with open(path, encoding='utf-8') as f:
        for line in f:
            parts = line.rstrip('\n').split('\t')
            if len(parts) < 3:
                continue
            try:
                page = int(parts[0].strip())
            except ValueError:
                continue
            out[(page, parts[2].strip())] = parts[1].strip()
    return out


def load_tsv(name, key='page'):
    """work/<name>.tsv -> list of dict（第一行是表头）"""
    path = os.path.join(ROOT, 'work', name)
    rows = []
    if not os.path.exists(path):
        return rows
    with open(path, encoding='utf-8') as f:
        header = f.readline().rstrip('\n').split('\t')
        for line in f:
            parts = line.rstrip('\n').split('\t')
            if len(parts) < len(header):
                continue
            rows.append(dict(zip(header, parts)))
    return rows


def expected_tags(pages):
    """原文该章各页文字层里出现的 (X.Y) 编号集合（含正文交叉引用，取并集）"""
    got = set()
    for p in pages:
        path = os.path.join(ROOT, 'work', 'split', 'p%03d.txt' % p)
        if not os.path.exists(path):
            continue
        with open(path, encoding='utf-8', errors='replace') as f:
            got |= set(RE_EQ_PAGE.findall(f.read()))
    return got


def audit(chunk):
    tex = os.path.join(ROOT, 'src', 'chunks', chunk + '.tex')
    if not os.path.exists(tex):
        return None
    if chunk not in CHAPTERS:
        return None
    lo, hi = CHAPTERS[chunk]
    pages = list(range(lo, hi + 1))
    src = open(tex, encoding='utf-8').read()

    problems = []

    # 1 页锚点
    anchors = [int(m) for m in RE_ANCHOR.findall(src)]
    missing_pages = [p for p in pages if p not in anchors]
    bad_order = [a for i, a in enumerate(anchors) if i and a < anchors[i - 1]]
    dup = sorted({a for a in anchors if anchors.count(a) > 1})
    if missing_pages:
        problems.append('缺页锚点: %s' % missing_pages)
    if bad_order:
        problems.append('页锚点顺序错: %s' % bad_order[:6])
    if dup:
        problems.append('页锚点重复: %s' % dup)

    # 2 陈述编号
    stmts = load_statements()
    # 按页段收集应译的编号陈述；章首跨页内容（如 p.74 上半的 Question 4.74–4.76）默认归本章，
    # 但若该编号已明确归上一章（见 EXCLUDE_STMT），则不要求本章重复译出。
    want = {num for (pg, num) in stmts if lo <= pg <= hi}
    want -= EXCLUDE_STMT.get(chunk, set())
    have = set(RE_STMT.findall(src) and [n for _, n in RE_STMT.findall(src)])
    miss_st = sorted(want - have, key=lambda s: [int(x) for x in s.split('.')])
    extra_st = sorted(have - want, key=lambda s: [int(x) for x in s.split('.')])
    if miss_st:
        problems.append('缺陈述编号: %s' % miss_st)
    if extra_st:
        problems.append('多出陈述编号: %s' % extra_st)

    # 3 公式编号
    want_tag = {t for t in expected_tags(pages) if t.split('.')[0] == chunk[2:4].lstrip('0')}
    # 允许章号不匹配的残余（原文引用他章公式），只报本章缺失
    have_tag = set(RE_TAG.findall(src))
    tag_pages = pages + EXTRA_TAG_PAGES.get(chunk, [])
    miss_tag = sorted(want_tag - have_tag, key=lambda s: [int(x) for x in s.split('.')])
    extra_tag = sorted(have_tag - (want_tag | set()), key=lambda s: [int(x) for x in s.split('.')])
    # 额外 tag 只在完全不在原章页面上出现时才算可疑
    all_page_tags = expected_tags(tag_pages)
    extra_tag = [t for t in extra_tag if t not in all_page_tags]
    if miss_tag:
        problems.append('缺公式编号: %s' % miss_tag)
    if extra_tag:
        problems.append('可疑公式编号(页面未见): %s' % extra_tag)

    # 4 图
    figs = [r for r in load_tsv('figures_index.tsv') if int(r['page']) in pages]
    incs = RE_INCLUDE.findall(src)
    if len(incs) != len(figs) and chunk not in ALLOW_EXTRA_FIG:
        problems.append('图数量: tex=%d 原书=%d' % (len(incs), len(figs)))
    for inc in incs:
        fp = os.path.join(ROOT, 'src', inc.strip())
        if not os.path.exists(fp):
            problems.append('图文件缺失: %s' % inc)

    # 5 批注密度
    n_note = len(RE_NOTE.findall(src))
    n_cjk = len(RE_CJK.findall(src))
    dens = (n_note * 1000.0 / n_cjk) if n_cjk else 0
    if dens > 1.0:
        problems.append('批注过密: %d 条 / %d 汉字 = %.2f‰' % (n_note, n_cjk, dens))

    return {
        'chunk': chunk,
        'pages': '%d-%d' % (lo, hi),
        'anchors': '%d/%d' % (len(set(anchors) & set(pages)), len(pages)),
        'statements': '%d/%d' % (len(have), len(want)),
        'tags': '%d (原书 %d)' % (len(have_tag), len(want_tag)),
        'figures': '%d/%d' % (len(incs), len(figs)),
        'notes': n_note,
        'cjk': n_cjk,
        'problems': problems,
    }


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('-')]
    if '--all' in sys.argv or not args:
        chunks = sorted(CHAPTERS)
    else:
        chunks = args
    rows = []
    for c in chunks:
        r = audit(c)
        if r:
            rows.append(r)
    if not rows:
        print('no chunk found')
        return 1
    hdr = ('chunk', 'pages', 'anchors', 'statements', 'tags', 'figures', 'notes', 'cjk')
    print('\t'.join(hdr) + '\tstatus')
    fails = 0
    for r in rows:
        status = 'PASS' if not r['problems'] else 'FAIL'
        if r['problems']:
            fails += 1
        print('\t'.join(str(r[k]) for k in hdr) + '\t' + status)
        for p in r['problems']:
            print('    ! ' + p)
    print()
    print('AUDIT %s (%d/%d chunks clean)' % ('PASS' if fails == 0 else 'FAIL', len(rows) - fails, len(rows)))
    return 0 if fails == 0 else 2


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.exit(main())
