# -*- coding: utf-8 -*-
"""从 src/chunks/*.tex 汇总译注，生成 src/appendix_b.tex（附录 B 译注汇编）。

收录两类：
  1. `% [Tutor Note: ...]`  —— 校勘性批注，正文不印（可能跨行，以 `]` 收尾）
  2. `\\yizhu{...}`         —— 概念性批注，正文可见（可含嵌套花括号）

每条注明它在原书哪一页（取该条之前最近的 `% [原文 p.N]` 标记）与所在章。
"""
import io, os, re, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(ROOT, 'src', 'chunks')
OUT = os.path.join(ROOT, 'src', 'chunks', 'appendix_b.tex')

ORDER = ['ch00a', 'ch01a', 'ch01b', 'ch02a', 'ch02b', 'ch03a', 'ch03b',
         'ch03c', 'ch03d', 'ch04', 'ch05a', 'ch05b', 'refs']

CHAPTER_OF = {
    'ch00a': '引言', 'ch01a': '第 1 章', 'ch01b': '第 1 章',
    'ch02a': '第 2 章', 'ch02b': '第 2 章',
    'ch03a': '第 3 章', 'ch03b': '第 3 章', 'ch03c': '第 3 章', 'ch03d': '第 3 章',
    'ch04': '第 4 章', 'ch05a': '第 5 章', 'ch05b': '第 5 章', 'refs': '参考文献',
}

PAGE = re.compile(r'%\s*\[原文\s*p\.(\d+)\]')


def balanced(s, start, op='{', cl='}'):
    """s[start] == op; 返回 (内容, 结束位置后一位)。"""
    depth, i = 0, start
    while i < len(s):
        c = s[i]
        if c == '\\':
            i += 2
            continue
        if c == op:
            depth += 1
        elif c == cl:
            depth -= 1
            if depth == 0:
                return s[start + 1:i], i + 1
        i += 1
    return s[start + 1:], len(s)


def clean(t):
    t = re.sub(r'\s+', ' ', t).strip()
    t = t.replace('--', '–')
    return t


def scan(path, tag):
    src = io.open(path, encoding='utf-8').read()
    items = []          # (page, kind, text)
    page = None

    # 逐位置扫描，维护最近的页标记
    marks = [(m.start(), int(m.group(1))) for m in PAGE.finditer(src)]

    def page_at(pos):
        p = None
        for s, v in marks:
            if s <= pos:
                p = v
            else:
                break
        return p

    # 1) Tutor Note（注释行，可能跨行，到首个 ']' 或行尾 ']'）
    for m in re.finditer(r'%\s*\[Tutor Note:(.*?)\]\s*$', src, re.S | re.M):
        body = clean(m.group(1))
        if body:
            items.append((page_at(m.start()), 'note', body))

    # 2) \yizhu{...}
    for m in re.finditer(r'\\yizhu\s*\{', src):
        body, _ = balanced(src, m.end() - 1)
        body = clean(body)
        if body:
            items.append((page_at(m.start()), 'show', body))

    return items


def esc(t):
    t = t.replace('\\', r'\textbackslash{}')
    for a, b in (('&', r'\&'), ('%', r'\%'), ('#', r'\#'), ('_', r'\_'),
                 ('{', r'\{'), ('}', r'\}')):
        t = t.replace(a, b)
    return t


def main():
    groups = []
    total = 0
    for tag in ORDER:
        p = os.path.join(CH, tag + '.tex')
        if not os.path.exists(p):
            continue
        items = scan(p, tag)
        if not items:
            continue
        ch = CHAPTER_OF.get(tag, tag)
        if groups and groups[-1][0] == ch:
            groups[-1][1].extend(items)
        else:
            groups.append((ch, list(items)))
        total += len(items)

    out = []
    w = out.append
    w('% ============================================================')
    w('% 附录 B：译注汇编（由 tools/gen_notes.py 自动生成，勿手改）')
    w('% 数据源：src/chunks/*.tex 中的 % [Tutor Note: ...] 与 \\yizhu{...}')
    w('% ============================================================')
    w(r'\chapter{译注汇编}')
    w(r'\label{app:notes}')
    w('')
    w('本附录收录全书的批注，共 %d 条，按原书页码排列。' % total)
    w('它们分两类。')
    w('')
    w(r'\begin{itemize}[leftmargin=2.6em,itemsep=1pt,topsep=2pt]')
    w(r'  \item \textbf{校勘性批注}（原书笔误、文字层与页面图像不一致、'
      r'术语取舍的理由、跨页句子的切分）。这类批注在正文中以源码注释形式存在，'
      r'不出现在版面上，只在此处汇总，以免打断阅读。')
    w(r'  \item \textbf{概念性批注}（某个概念在通行文献里的另一种说法、'
      r'与 nLab 视角的差异、值得补充的背景）。这类批注在正文中已经印出，'
      r'此处再次汇总，方便通读与检索。')
    w(r'\end{itemize}')
    w('')
    w('每条前的方括号标明它所在的章节与原书页码；页码与原书（Russian Math.')
    w('Surveys 58:3）一致，便于对照原文核查。')
    w('')

    for ch, items in groups:
        items.sort(key=lambda x: (x[0] is None, x[0]))
        pgs = [i[0] for i in items if i[0] is not None]
        first = min(pgs) if pgs else '—'
        w(r'\section*{%s（原书 p.%s）}' % (ch, first))
        w(r'\addcontentsline{toc}{section}{%s（原书 p.%s）}' % (ch, first))
        w('')
        last_page = None
        for page, kind, body in items:
            if page is not None and page != last_page:
                w(r'\medskip\noindent\textbf{原书 p.%d}\par' % page)
                last_page = page
            label = '校勘' if kind == 'note' else '概念'
            w(r'\noindent{\small\textbf{［%s］}%s}\par\smallskip' % (label, body))
        w('')

    with io.open(OUT, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out))
    print('wrote', OUT, total, 'notes in', len(groups), 'groups')


main()
