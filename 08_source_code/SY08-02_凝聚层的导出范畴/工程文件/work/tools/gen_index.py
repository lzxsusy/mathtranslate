# -*- coding: utf-8 -*-
"""扫描 src/chunks/*.tex，生成 src/chunks/appendix_d.tex（附录 D 定理与定义索引）。

抽出两类可自动索引的东西：
  1. 带原书编号的陈述（\\begin{theorem}{2.1.8} 之类）
  2. 带 \\tag{N} 的编号公式（原书共 (1)--(31)）
位置一律取该条目之前最近的 `% [原文 p.N]` 页标记。
"""
import io, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(ROOT, 'src', 'chunks')
OUT = os.path.join(CH, 'appendix_d.tex')

ORDER = ['ch00a', 'ch01a', 'ch01b', 'ch02a', 'ch02b', 'ch03a', 'ch03b',
         'ch03c', 'ch03d', 'ch04', 'ch05a', 'ch05b']

CHAPTER_OF = {
    'ch00a': '引言', 'ch01a': '1.1', 'ch01b': '1.2--1.3',
    'ch02a': '2.1', 'ch02b': '2.2',
    'ch03a': '3.1--3.2', 'ch03b': '3.3', 'ch03c': '3.4', 'ch03d': '3.5',
    'ch04': '4.1--4.2', 'ch05a': '5.1', 'ch05b': '5.2--5.3',
}

TYPE_ZH = {
    'theorem': '定理', 'proposition': '命题', 'lemma': '引理',
    'corollary': '推论', 'definition': '定义', 'example': '例',
    'remark': '注', 'note': '注', 'notation': '记号', 'question': '问题',
    'problem': '问题', 'conjecture': '猜想', 'assumption': '假设',
    'formulaenv': '公式', 'counterexample': '反例',
}

PAGE = re.compile(r'%\s*\[原文\s*p\.(\d+)\]')
STMT = re.compile(r'\\begin\{(theorem|proposition|lemma|corollary|definition|'
                  r'example|remark|notation|question|problem|conjecture|'
                  r'assumption|counterexample)p?\}'
                  r'(?:\[(?:[^\[\]]|\[[^\[\]]*\])*\])?\{([^}]*)\}')
TAG = re.compile(r'\\tag\{([^}]*)\}')


def main():
    stmts, tags = [], []
    for tag in ORDER:
        p = os.path.join(CH, tag + '.tex')
        if not os.path.exists(p):
            continue
        src = io.open(p, encoding='utf-8').read()
        marks = [(m.start(), int(m.group(1))) for m in PAGE.finditer(src)]

        def page_at(pos):
            v = None
            for s, x in marks:
                if s <= pos:
                    v = x
                else:
                    break
            return v

        for m in STMT.finditer(src):
            stmts.append((m.group(2), TYPE_ZH.get(m.group(1), m.group(1)),
                          page_at(m.start()), CHAPTER_OF.get(tag, tag), tag))
        for m in TAG.finditer(src):
            tags.append((m.group(1), page_at(m.start()), CHAPTER_OF.get(tag, tag)))

    def numkey(n):
        try:
            return tuple(int(x) for x in re.findall(r'\d+', n))
        except Exception:
            return (999,)


    out = []
    w = out.append
    w('% ============================================================')
    w('% 附录 D：定理与定义索引（由 tools/gen_index.py 自动生成，勿手改）')
    w('% ============================================================')
    w(r'\chapter{定理与定义索引}')
    w(r'\label{app:index}')
    w('')
    w('本索引按原书编号排列，共收陈述 %d 条、编号公式 %d 个。' % (len(stmts), len(tags)))
    w('第二栏为原书页码（与本译本页边的页标记一致），第三栏为本译本中的位置。')
    w('编号一律照抄原书，未作任何重排：原书若有两处同号（例如 1.3 既指定义又指')
    w('节号），本索引照录，并在正文相应处以译注说明。')
    w('')
    w(r'\section*{一、带编号的陈述}')
    w(r'\addcontentsline{toc}{section}{一、带编号的陈述}')
    w('')
    w(r'\begin{termlist}')
    last = None
    for num, typ, page, sec, _ in stmts:
        if num != last:
            w(r'\item[]\hspace*{-2.2em}\textbf{%s}' % num)
            last = num
        w(r'\item[]\hspace*{1.2em}{\small %s\quad 原书 p.%s\quad 本译本 §%s}'
          % (typ, page if page else '—', sec))
    w(r'\end{termlist}')
    w('')
    w(r'\section*{二、编号公式}')
    w(r'\addcontentsline{toc}{section}{二、编号公式}')
    w('')
    w(r'\begin{termlist}')
    for num, page, sec in tags:
        w(r'\item[(%s)] 原书 p.%s\quad 本译本 §%s' % (num, page if page else '—', sec))
    w(r'\end{termlist}')
    w('')

    with io.open(OUT, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out))
    print('wrote', OUT, len(stmts), 'statements,', len(tags), 'tags')


main()
