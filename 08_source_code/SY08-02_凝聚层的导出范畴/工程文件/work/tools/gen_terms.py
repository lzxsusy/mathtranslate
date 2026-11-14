# -*- coding: utf-8 -*-
"""由 work/glossary.tsv 生成 src/appendix_a.tex（附录 A 术语对照表）。"""
import io, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TSV = os.path.join(ROOT, 'work', 'glossary.tsv')
OUT = os.path.join(ROOT, 'src', 'chunks', 'appendix_a.tex')

rows = []
with io.open(TSV, encoding='utf-8') as f:
    header = f.readline()
    for line in f:
        line = line.rstrip('\n')
        if not line.strip():
            continue
        parts = line.split('\t')
        while len(parts) < 4:
            parts.append('')
        en, zh, lvl, note = parts[0].strip(), parts[1].strip(), parts[2].strip(), parts[3].strip()
        rows.append((en, zh, lvl, note))

rows.sort(key=lambda r: r[0].lower())

def esc(s):
    s = s.replace('&', r'\&').replace('%', r'\%').replace('#', r'\#')
    s = s.replace('_', r'\_').replace('–', '--')
    return s

nA = sum(1 for r in rows if r[2].startswith('A'))
nB = sum(1 for r in rows if r[2].startswith('B'))
nI = sum(1 for r in rows if r[2].startswith('I'))

out = []
w = out.append
w('% ============================================================')
w('% 附录 A：英中术语对照表（由 work/tools/gen_terms.py 自动生成，勿手改）')
w('% 数据源：work/glossary.tsv（英文 / 中文 / 依据等级 / 备注）')
w('% ============================================================')
w(r'\chapter{英中术语对照表}')
w(r'\label{app:terms}')
w('')
w('本表收录正文中译名已固定下来的术语，共 %d 条，按英文条目的字母序排列。' % len(rows))
_g = ['A 级为原始论文或经典教材（%d 条）' % nA]
if nB:
    _g.append('B 级为 nLab、Stacks Project 一类可复核的参考（%d 条）' % nB)
if nI:
    _g.append('I 级为本库既往译本与术语库（%d 条）' % nI)
if nB or nI:
    w('确定译名时所依据的来源等级：' + '，'.join(_g) + '。')
else:
    w('确定译名时所依据的来源一律为原始论文或经典教材（%d 条）：'
      'nLab、Stacks Project 只用于校验，不作为定名依据。' % nA)
w('凡中文栏保留西文者，表示该术语在中文文献中尚无稳定通行译名，'
  '或两种译名并行、强行统一反而妨碍检索；此时正文一律照写西文。')
w('')
w(r'\section{译名取舍的几条原则}')
w('')
w(r'\begin{enumerate}')
w(r'  \item \textbf{有稳定通行译名者一律用中文}，并尽量采用国内教材的写法。'
  r'“三角范畴”“特异三角”“正合函子”“厚子范畴”均属此类；'
  r'其中 distinguished triangle 一词，国内有“特异三角”“ distinguished 三角”'
  r'“正合三角”几种写法，本稿统一取“特异三角”，因为 exact triangle 在原文中'
  r'另有所指（无特异结构时的三角），两者不宜混用。')
w(r'  \item \textbf{无稳定译名或两种译名并行者保留西文}。flop 即属此类：'
  r'国内有“翻转”“翻折”“弗洛普”等写法，无一通行，故正文一律写 flop，'
  r'首次出现时以译注说明其含义（极小模型理论中的一种双有理变换，'
  r'与 flip“翻转”相对）。')
w(r'  \item \textbf{人名一律保留拉丁字母}，不音译。Fourier--Mukai、Postnikov、'
  r'Koszul、Verdier、Serre、Grothendieck、Bondal--Orlov 等均照写；'
  r'首次出现时给出全名（如“Mukai 的 Fourier 变换”）。')
w(r'  \item \textbf{同一英文词在不同语境下的译法若确有分别，则分别固定}，'
  r'并在注释中标明。例如 complex 在链复形语境下译“复形”，在概形语境下'
  r'（与 real 相对）译“复的”，本稿以“复形”“复流形”区分。')
w(r'  \item \textbf{译名一经固定，并行施工期间只读不改}。凡施工中发现新的、'
  r'更合适的译法，先提案，待全稿统一处理，不在单章内擅自更改。')
w(r'\end{enumerate}')
w('')
w(r'\section{术语一览}')
w('')
w(r'\begin{termlist}')
for en, zh, lvl, note in rows:
    en_s = esc(en)
    zh_s = esc(zh)
    w(r'\termitem{%s}{%s}' % (zh_s, en_s))
w(r'\end{termlist}')
w('')
w(r'\section*{按中文检索}')
w(r'\addcontentsline{toc}{section}{按中文检索}')
w('')
w('若手边只有中文译名，可按下表回查英文。表中只列中文栏非西文者。')
w('')
w(r'\begin{termlist}')
for en, zh, lvl, note in sorted(rows, key=lambda r: r[1]):
    if en == '': continue
    w(r'\termitem{%s}{%s}' % (esc(zh), esc(en)))
w(r'\end{termlist}')
w('')
w(r'\section{未收入本表的词}')
w('')
w('原文中另有若干词只出现一两次、且不影响论证，本表未收；'
  '这类词在正文首次出现处已有就地解释或页边译注，按正文检索即可。')
w('')

with io.open(OUT, 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))
print('wrote', OUT, len(rows), 'terms')
