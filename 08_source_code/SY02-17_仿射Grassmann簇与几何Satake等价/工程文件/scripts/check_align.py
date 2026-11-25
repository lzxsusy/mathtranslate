# -*- coding: utf-8 -*-
"""SY02-17 对齐自检：显示公式集合、label 集合、术语残留、黑名单、字数。

用法：
  python check_align.py            # 全部检查
  python check_align.py eq         # 只跑公式
"""
import io
import os
import re
import sys
import collections

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(os.path.dirname(HERE))   # .../SY02-17_...
SRC = os.path.join(PROJ, '工程文件', 'work', '原文', 'main.tex')
CH = os.path.join(PROJ, '源码', 'chunks')


def read(p):
    with io.open(p, encoding='utf-8', errors='replace') as f:
        return f.read()


def body_src():
    t = read(SRC)
    i = t.index(r'\begin{document}')
    j = t.index(r'\end{document}')
    return t[i:j]


def math_blocks(t):
    """抽出所有显示公式（equation / \[ \] / align / gather / multline），去 label。"""
    out = []
    # \begin{equation} ... \end{equation}  与 align/gather 家族
    for m in re.finditer(r'\\begin\{(equation|align|gather|multline|eqnarray)\*?\}(.*?)\\end\{\1\*?\}',
                         t, re.S):
        body = m.group(2)
        body = re.sub(r'\\label\{[^}]*\}', '', body)
        out.append(body)
    # \[ ... \]
    for m in re.finditer(r'\\\[(.*?)\\\]', t, re.S):
        body = m.group(1)
        body = re.sub(r'\\label\{[^}]*\}', '', body)
        out.append(body)
    return out


def strip_text(s):
    """去掉 \\mbox{..} / \\text{..} / 中文与 \\begin{split}|array 的排版差异，只留数学。"""
    prev = None
    while prev != s:
        prev = s
        s = re.sub(r'\\(mbox|text|textrm|mathrm)\{[^{}]*\}', ' ', s)
    s = re.sub(r'\\begin\{(split|array|aligned|gathered)\}(\[[^\]]*\]|\{[^{}]*\})?', ' ', s)
    s = re.sub(r'\\end\{(split|array|aligned|gathered)\}', ' ', s)
    s = re.sub(r'[\u4e00-\u9fff]+', ' ', s)
    return s


def norm(s):
    s = re.sub(r'\\label\{[^}]*\}', '', s)
    s = strip_text(s)
    s = re.sub(r'\\(left|right|big|Big|bigg|Bigg)\.', '', s)
    s = re.sub(r'\\(left|right|big|Big|bigg|Bigg)(?=[\\\(\[\{a-zA-Z0-9])', '', s)
    s = re.sub(r'\\[,;:! ]', '', s)
    s = re.sub(r'\s+', '', s)
    s = s.replace('{', '').replace('}', '')
    s = s.replace('\\mO', 'O').replace('\\mF', 'F').replace('\\mE', 'E')
    s = s.replace('\\GL', 'GL').replace('\\Spec', 'Spec')
    s = s.replace('\\on', '').replace('\\Sat', 'Sat')
    s = s.replace('\\bZ', 'Z').replace('\\bC', 'C').replace('\\bG', 'G')
    return s


def tokens(s):
    """数学 token 签名：把 \\cmd 与字母数字串都当 token，忽略顺序中的连接符差异。"""
    s = re.sub(r'\\begin\{[^}]*\}|\\end\{[^}]*\}', ' ', s)
    s = re.sub(r'\\\\', ' ', s)
    s = re.sub(r'&', ' ', s)
    st = re.findall(r'\\[A-Za-z]+|[A-Za-z]+|\d+|[<>=+\-*/^_()\[\]|,.]', s)
    return st


def bag(seq):
    return collections.Counter(seq)


def diff_bag(a, b):
    """返回 a 有而 b 缺、(或计数更少) 的 token 及数量。"""
    ca, cb = bag(a), bag(b)
    miss = {}
    for k, v in ca.items():
        if cb.get(k, 0) < v:
            miss[k] = v - cb.get(k, 0)
    return miss


def all_chunks():
    names = sorted(f for f in os.listdir(CH) if f.endswith('.tex'))
    return {f: read(os.path.join(CH, f)) for f in names}


def check_eq(src, chunks, fh):
    def p(s=''):
        print(s)
        fh.write(s + '\n')
    sb = math_blocks(body_src())
    cb = []
    for f, t in chunks.items():
        cb += math_blocks(t)
    p('原文显示公式 %d 条，译文 %d 条' % (len(sb), len(cb)))
    cbtok = [bag(tokens(norm(x))) for x in cb]
    unused = set(range(len(cb)))
    exact = near = bad = 0
    for i, s in enumerate(sb):
        st = bag(tokens(norm(s)))
        best, bestscore = None, -1.0
        for j in unused:
            ct = cbtok[j]
            inter = sum(min(v, ct.get(k, 0)) for k, v in st.items())
            union = sum(max(v, ct.get(k, 0)) for k, v in st.items()) + \
                sum(v for k, v in ct.items() if k not in st)
            sc = inter / union if union else 1.0
            if sc > bestscore:
                best, bestscore = j, sc
        if bestscore > 0.999:
            exact += 1
            unused.discard(best)
        elif bestscore > 0.82:
            near += 1
            unused.discard(best)
            p('[近似 %.2f] 原 %d' % (bestscore, i + 1))
            p('  原: ' + ' '.join(s.split())[:260])
            p('  译: ' + ' '.join(cb[best].split())[:260])
            d = diff_bag(tokens(norm(s)), tokens(norm(cb[best])))
            if d:
                p('  差: ' + str(d))
        else:
            bad += 1
            p('[未匹配 %.2f] 原 %d' % (bestscore, i + 1))
            p('  原: ' + ' '.join(s.split())[:300])
    p('')
    p('== 汇总：完全一致 %d，近似 %d，未匹配 %d，译文多余公式 %d ==' %
      (exact, near, bad, len(unused)))
    for j in sorted(unused):
        p('[译文多出] ' + ' '.join(cb[j].split())[:300])
    return bad + near


def check_labels(src, chunks, fh):
    def p(s=''):
        print(s)
        fh.write(s + '\n')
    sl = set(re.findall(r'\\label\{([^}]*)\}', body_src()))
    cl = set()
    for t in chunks.values():
        cl |= set(re.findall(r'\\label\{([^}]*)\}', t))
    p('label：原文 %d，译文 %d' % (len(sl), len(cl)))
    p('  译文缺: ' + str(sorted(sl - cl)))
    p('  译文多: ' + str(sorted(cl - sl)))


BANNED = ['知乎', 'zhihu', '百度百科', 'baike', 'CSDN', '简书', 'jianshu', '公众号']


def check_terms(chunks, fh):
    def p(s=''):
        print(s)
        fh.write(s + '\n')
    joined = '\n'.join(chunks.values())
    p('=== 黑名单扫描 ===')
    hits = 0
    for w in BANNED:
        c = joined.count(w)
        if c:
            hits += c
            p('  命中 %s：%d' % (w, c))
    p('  合计 %d' % hits)
    p('=== 机械指标 ===')
    p('  汉字数 %d' % len(re.findall(r'[\u4e00-\u9fff]', joined)))
    for pat in [r'被.{1,12}所', r'进行.{1,12}的', r'对于.{1,12}而言']:
        c = len(re.findall(pat, joined))
        p('  %s：%d' % (pat, c))
    p('  译注 \\zy 条数：%d' % joined.count('\\zy{'))
    p('  未定义占位 TODO/FIXME：%d' % (joined.count('TODO') + joined.count('FIXME')))


def main():
    chunks = all_chunks()
    what = sys.argv[1] if len(sys.argv) > 1 else 'all'
    out = os.path.join(PROJ, '工程文件', 'work', 'align_report.txt')
    with io.open(out, 'w', encoding='utf-8') as fh:
        if what in ('all', 'eq'):
            fh.write('========= 显示公式对齐 =========\n')
            check_eq(None, chunks, fh)
        if what in ('all', 'labels'):
            fh.write('\n========= label 对齐 =========\n')
            check_labels(None, chunks, fh)
        if what in ('all', 'terms'):
            fh.write('\n========= 术语/卫生 =========\n')
            check_terms(chunks, fh)
    print('report -> ' + out)


if __name__ == '__main__':
    main()
