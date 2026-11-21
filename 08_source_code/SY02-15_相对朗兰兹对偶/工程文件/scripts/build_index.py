# -*- coding: utf-8 -*-
"""建立「编号对象 → 源码锚点 → 译本页码」索引。

输出：
  工程文件/work/section_index.json   机器读（供资料卡 03-条款索引 使用）
  工程文件/work/section_index.tsv    人读

约定（与 main.tex 的译者说明一致）：
  * 每节一个共享计数器，公式与定理类环境同号；
  * §13 前两条 display 在原文中不印编号但计数器进两位 → 本节第一个环境从 3 起；
  * §15 第一条 (15.1)，随后 rem 15.2，再 setcounter{2} 后 equation 为 15.3。
"""
import io, json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SRC = os.path.join(ROOT, '源码')
OUT = os.path.join(ROOT, '工程文件', 'work')
PDF = os.path.join(SRC, 'main.pdf')

KIND = {
    'equation': '公式', 'thm': '定理', 'lem': '引理', 'prop': '命题', 'cor': '推论',
    'conj': '猜想', 'defn': '定义', 'exmp': '例', 'exer': '练习', 'claim': '断言', 'rem': '注',
}
PAT = re.compile(r'\\begin\{(' + '|'.join(KIND) + r')\}')

# 起始计数器（1 表示下一个环境就是 x.1）
START = {}


def main():
    try:
        import pymupdf
    except ImportError:
        sys.exit('need pymupdf')

    doc = pymupdf.open(PDF)
    pages = [doc[i].get_text('text') for i in range(doc.page_count)]

    index = []
    for sec in range(1, 16):
        f = os.path.join(SRC, 'chunks', 'ch%02d.tex' % sec)
        text = io.open(f, encoding='utf-8').read()
        lines = text.split('\n')
        counter = START.get(sec, 1) - 1
        # 处理 §15 的 setcounter
        for i, line in enumerate(lines):
            if line.strip().startswith('%'):
                continue
            m = re.search(r'\\setcounter\{equation\}\{(\d+)\}', line)
            if m:
                counter = int(m.group(1))
            # 多行编号环境（align/gather/multline/eqnarray）：每个带 \label 的行算一个编号
            mb = re.search(r'\\begin\{(align|gather|multline|eqnarray)\}', line)
            if mb:
                env = mb.group(1)
                block = [line]
                j = i
                while ('\\end{%s}' % env) not in block[-1] and j + 1 < len(lines):
                    j += 1
                    block.append(lines[j])
                body = '\n'.join(block)
                rows = len(re.findall(r'\\label\{', body)) or (body.count('\\\\') + 1)
                for _ in range(rows):
                    counter += 1
                    num = '%d.%d' % (sec, counter)
                    page = None
                    pat = re.compile(r'^\s*\(' + re.escape(num) + r'\)', re.M)
                    for pi, t in enumerate(pages):
                        if pat.search(t):
                            page = pi + 1
                            break
                    index.append({
                        'sec': sec, 'num': counter, 'label': '(%s)' % num, 'kind': '公式',
                        'tex': '源码/chunks/ch%02d.tex' % sec, 'line': i + 1,
                        'pdf_page': page,
                    })
                i = j
                continue
            for mm in PAT.finditer(line):
                counter += 1
                kind = KIND[mm.group(1)]
                label = '(%d.%d)' % (sec, counter)
                # 找页码：公式看行首的 (s.n)，定理类看「<中文名> s.n.」
                num = '%d.%d' % (sec, counter)
                if mm.group(1) == 'equation':
                    pat = re.compile(r'^\s*\(' + re.escape(num) + r'\)', re.M)
                else:
                    pat = re.compile(r'^\s*' + KIND[mm.group(1)] + r'\s*' + re.escape(num), re.M)
                page = None
                for pi, t in enumerate(pages):
                    if pat.search(t):
                        page = pi + 1
                        break
                if page is None:                      # 兜底：位置散乱时退化为任意位置匹配
                    for pi, t in enumerate(pages):
                        if label in t:
                            page = pi + 1
                            break
                index.append({
                    'sec': sec, 'num': counter, 'label': label, 'kind': kind,
                    'tex': '源码/chunks/ch%02d.tex' % sec, 'line': i + 1,
                    'pdf_page': page,
                })

    with io.open(os.path.join(OUT, 'section_index.json'), 'w', encoding='utf-8') as fh:
        json.dump(index, fh, ensure_ascii=False, indent=1)

    with io.open(os.path.join(OUT, 'section_index.tsv'), 'w', encoding='utf-8') as fh:
        fh.write('节\t编号\t类型\t源码锚点\t源行\tPDF 页\t译本页\n')
        for e in index:
            fh.write('%d\t%s\t%s\t%s\t%d\t%s\t%s\n' % (
                e['sec'], e['label'], e['kind'], e['tex'], e['line'],
                e['pdf_page'] if e['pdf_page'] else '?',
                (e['pdf_page'] - 4) if e['pdf_page'] else '?'))

    miss = [e['label'] for e in index if not e['pdf_page']]
    print('items=%d  missing_page=%d %s' % (len(index), len(miss), miss[:12]))


if __name__ == '__main__':
    main()
