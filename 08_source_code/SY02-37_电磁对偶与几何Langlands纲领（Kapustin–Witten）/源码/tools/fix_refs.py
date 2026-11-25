# -*- coding: utf-8 -*-
"""修正 refs.tex 里 harvmac 老式字体开关（流水线：harvmac2tex.py 之后跑，幂等）。

背景：harvmac 源里的文献条目用 plain TeX 写法 `{\\bf 170}`、`{\\it ...}`。
而 macros.tex 从源文件导言区抽到了 `\\def\\bf#1{\\mathbf{#1}}`，
于是 {\bf 170} 变成 \\mathbf{170}，在文本模式下报
`LaTeX Error: \\mathbf allowed only in math mode.`（106 处，全在 refs.tex）。

修法：refs.tex 是纯文本著录，直接改成 LaTeX2e 的 \\textbf{} / \\emph{}。
（skel 里的 `{\\bf 4}` 等在数学模式下工作正常，不动。）
"""
import io, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, 'refs.tex')


def main():
    with io.open(P, encoding='utf-8') as f:
        s = f.read()
    n_bf = s.count(r'{\bf ')
    n_it = s.count(r'{\it ')
    s = s.replace(r'{\bf ', r'\textbf{')
    s = s.replace(r'{\it ', r'\emph{')
    # 形如 {\bf{0506}}（比上一类推文多一层花括号）：整体换成 \textbf{0506}
    s = re.sub(r'\{\\bf\s*\{([^{}]*)\}\}', r'\\textbf{\1}', s)
    s = re.sub(r'\{\\it\s*\{([^{}]*)\}\}', r'\\emph{\1}', s)
    with io.open(P, 'w', encoding='utf-8', newline='\n') as f:
        f.write(s)
    print('refs.tex: \\bf -> \\textbf %d 处, \\it -> \\emph %d 处' % (n_bf, n_it))


if __name__ == '__main__':
    main()
