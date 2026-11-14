# -*- coding: utf-8 -*-
"""由 work/notes/notes_NN.tsv 生成 src/chapters/appendix_zhusi.tex（附录 A 译注来源总表 + 附录 B 笔误登记）。

用法：python gen_appendix.py
输出：src/chapters/appendix_zhusi.tex（每次全量重生成，不要手改该文件）
"""
import os, glob, re

ROOT = r'<本地路径>'
NOTES = os.path.join(ROOT, 'work', 'notes')
OUT = os.path.join(ROOT, 'src', 'chapters', 'appendix_zhusi.tex')

ACCESS = '2026-11-14'


MATH_SPLIT = re.compile(r'(\$[^$]*\$)')

# 表格里的裸 Unicode 数学符号 → 行内公式（Latin 字体不含这些字形）
SYMBOLS = [('\u2297', r'$\otimes$'), ('\u2208', r'$\in$'), ('\u27e8', r'$\langle$'),
           ('\u27e9', r'$\rangle$'), ('\u2218', r'$\circ$'), ('\u2207', r'$\nabla$'),
           ('\u2228', r'$\vee$'), ('\u2245', r'$\cong$'), ('\u2282', r'$\subset$'),
           ('\u2032', r"$'$"), ('\u00d7', r'$\times$'), ('\u2264', r'$\le$'),
           ('\u2265', r'$\ge$'), ('\u2192', r'$\to$'), ('\u2260', r'$\ne$'),
           ('\u223c', r'$\sim$'), ('\u00b1', r'$\pm$'), ('\u221e', r'$\infty$'),
           ('\u22c5', r'$\cdot$'), ('\u2212', r'$-$'), ('\u221a', r'$\sqrt{\ }$'),
           ('\u2113', r'$\ell$'), ('\u2102', r'$\mathbb{C}$'), ('\u211d', r'$\mathbb{R}$'),
           ('\u2124', r'$\mathbb{Z}$'), ('\u211a', r'$\mathbb{Q}$'), ('\u2229', r'$\cap$'),
           ('\u222a', r'$\cup$'), ('\u2200', r'$\forall$'), ('\u2203', r'$\exists$')]


def _sym(s):
    for a, b in SYMBOLS:
        s = s.replace(a, b)
    return s


def esc_loose(s):
    """概念/说明列：$…$ 内原样保留，段外把 _ ^ # & % 转义；去掉误留的反斜杠命令。"""
    s = s.strip().replace('\\znoteplain', '可见译注').replace('\\znote', '译注')
    out = []
    for part in MATH_SPLIT.split(s):
        if len(part) > 2 and part.startswith('$') and part.endswith('$'):
            out.append(part)
            continue
        part = part.replace('\\', '')
        part = _sym(part)
        part = part.replace('_', r'\_').replace('#', r'\#').replace('&', r'\&')
        part = part.replace('%', r'\%').replace('^', r'\^{}')
        out.append(part)
    return ''.join(out)


def esc_src(s):
    """来源列：$…$ 原样；段外转义 _ ^ # & %，但保留下划线已转义者与已有命令。"""
    s = s.strip().replace('\\znoteplain', '可见译注').replace('\\znote', '译注')
    out = []
    for part in MATH_SPLIT.split(s):
        if len(part) > 2 and part.startswith('$') and part.endswith('$'):
            out.append(part)
            continue
        part = _sym(part)
        part = re.sub(r'(?<!\\)([_#&%])', r'\\\1', part)
        part = re.sub(r'(?<!\\)\^', r'\\^{}', part)
        out.append(part)
    return ''.join(out)


def esc_plain(s):
    """单元格通用转义：无 $ 且无反斜杠时转义 LaTeX 特殊字符。"""
    s = s.strip()
    if '$' in s or '\\' in s:
        return s
    for a, b in (('&', r'\&'), ('%', r'\%'), ('#', r'\#'), ('_', r'\_')):
        s = s.replace(a, b)
    return s


URL_RE = re.compile(r'(https?://[A-Za-z0-9\-._~:/?#\[\]@!$&\'()*+,;=%]+)')


def fmt_source(src):
    """来源列：URL 单独进 \\url{}，其后的中文补充说明留作正文（否则中文会落进等宽字体）。"""
    src = src.strip()
    m = URL_RE.match(src)
    if m:
        url = m.group(1).rstrip('，。）),；;')
        rest = src[len(url):].strip()
        if rest:
            return r'\url{%s}%s' % (url, esc_src(rest))
        return r'\url{%s}' % url
    return esc_src(src)


def shortpos(pos):
    """lecture01.tex:22 -> L01:22"""
    m = re.match(r'lecture(\d+)\.tex:(\d+)', pos.strip())
    if m:
        return 'L%s:%s' % (m.group(1), m.group(2))
    return pos


def load():
    rows = []
    for p in sorted(glob.glob(os.path.join(NOTES, 'notes_*.tsv'))):
        for ln in open(p, encoding='utf-8').read().splitlines():
            if not ln.strip() or ln.startswith('#'):
                continue
            c = ln.split('\t')
            if len(c) < 7:
                print('WARN 列数不足(%d): %s :: %s' % (len(c), os.path.basename(p), ln[:80]))
                continue
            rows.append([x.strip() for x in c[:7]])
    return rows


def main():
    rows = load()
    notes, tutors = [], []
    for r in rows:
        if r[6] == 'skip':
            continue
        if r[6] == 'tutor-note':
            tutors.append(r)
        else:
            notes.append(r)
    def _lecnum(s):
        d = re.sub(r'\D', '', s)
        return int(d) if d else 0

    notes.sort(key=lambda r: (_lecnum(r[0]), _lecnum(r[2].split(':')[-1])))

    L = []
    L.append(r'\renewcommand{\xchaptertitle}{附录\thechapter}')
    L.append(r'\chapter{译注来源总表}')
    L.append(r'\begingroup\small\setstretch{1.02}')
    L.append(r'本表汇总全书 \textbf{%d} 条学生向译注的来源与等级，按讲排列。'
             r'每条译注在正文中以其概念首次出现处的脚注形式出现。'
             r'「位置」一栏指该译注在源文件中的位置，记作 L\,$n$\,:\,$m$，即第 $n$ 讲源文件第 $m$ 行。' % len(notes))
    L.append(r'')
    L.append(r'来源等级：\textbf{A} 为原书或作者文献、经典教材（带版次与章号）；'
             r'\textbf{B} 为 nLab、Stacks Project、MathWorld、DLMF、EMS 等正式参考源；'
             r'\textbf{I} 为本库既往译注与术语表；等级标作「译者按」者表示无外部依据、仅据上下文推断。'
             r'所有网页来源的访问日期为 %s。' % ACCESS)
    L.append(r'')
    L.append(r'\begin{longtable}{@{}p{1.0cm}p{3.3cm}p{1.5cm}p{1.3cm}p{7.9cm}@{}}')
    L.append(r'\toprule')
    L.append(r'\textbf{讲} & \textbf{概念} & \textbf{位置} & \textbf{等级} & \textbf{来源} \\')
    L.append(r'\midrule')
    L.append(r'\endfirsthead')
    L.append(r'\toprule')
    L.append(r'\textbf{讲} & \textbf{概念} & \textbf{位置} & \textbf{等级} & \textbf{来源} \\')
    L.append(r'\midrule')
    L.append(r'\endhead')
    L.append(r'\bottomrule')
    L.append(r'\endfoot')
    last = None
    for (lec, concept, pos, level, src, rev, status) in notes:
        if last is not None and lec != last:
            L.append(r'\midrule')
        last = lec
        lecname = int(re.sub(r'\D', '', lec) or 0)
        lev = level.split('/')[0].strip()
        if src.startswith('http'):
            source = fmt_source(src)
        else:
            source = esc_src(src)
        L.append(r'%d & %s & \texttt{%s} & %s & %s \\' % (
            lecname, esc_loose(concept), esc_plain(shortpos(pos)), esc_plain(lev), source))
    L.append(r'\end{longtable}')
    L.append(r'\endgroup')
    L.append(r'')

    L.append(r'\chapter{原书笔误与存疑登记}')
    L.append(r'\begingroup\small\setstretch{1.02}')
    L.append((r'下表登记在翻译与校订过程中发现的\textbf{英文原稿笔误}，以及已按正确写法处理的说明。'
              r'按本工程纪律，原稿笔误一律不悄悄改动正文而不留痕：凡译文已按正确写法处理的，'
              r'在对应 TeX 源码中以行注释（Tutor Note）就地登记。'
              r'附表为其汇总，供读者与后续校订者核对，共 ' + str(len(tutors)) + r' 条。'))
    L.append(r'')
    L.append(r'\begin{longtable}{@{}p{1.0cm}p{2.2cm}p{10.6cm}@{}}')
    L.append(r'\toprule')
    L.append(r'\textbf{讲} & \textbf{位置} & \textbf{说明} \\')
    L.append(r'\midrule')
    L.append(r'\endfirsthead')
    L.append(r'\toprule')
    L.append(r'\textbf{讲} & \textbf{位置} & \textbf{说明} \\')
    L.append(r'\midrule')
    L.append(r'\endhead')
    L.append(r'\bottomrule')
    L.append(r'\endfoot')
    for (lec, concept, pos, level, src, rev, status) in tutors:
        lecname = int(re.sub(r'\D', '', lec) or 0)
        L.append(r'%d & \texttt{%s} & %s \\' % (lecname, esc_plain(shortpos(pos)), esc_loose(concept)))
    L.append(r'\end{longtable}')
    L.append(r'\endgroup')
    L.append(r'')

    open(OUT, 'w', encoding='utf-8', newline='\n').write('\n'.join(L))
    print('wrote', OUT)
    print('notes: %d, tutor-notes: %d' % (len(notes), len(tutors)))


if __name__ == '__main__':
    main()
