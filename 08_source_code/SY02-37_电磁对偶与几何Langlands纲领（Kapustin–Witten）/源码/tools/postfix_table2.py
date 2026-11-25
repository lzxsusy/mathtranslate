# -*- coding: utf-8 -*-
"""补救：13-s05.tex 里 Table 2（harvmac \halign）残块 → booktabs tabular。
   harvmac2tex.py 之后跑；幂等（找不到就跳过）。"""
import io, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, 'skel', '13-s05.tex')

START = '\\centerline{\n\\vbox{\\hsize=2truein\\offinterlineskip\\halign'
END = 'which is its own $S$-dual.}}\n'

TABLE = r'''\begin{table}[htbp]
\centering
\begin{tabular}{ll}
\toprule
Model & $S$-Dual \\
\midrule
$I_B$ & $I_B$ \\
$I_A$ & $I_A$ \\
$J_B$ & $K_A$ \\
$J_A$ & $K_B$ \\
$K_B$ & $J_A$ \\
$K_A$ & $J_B$ \\
\bottomrule
\end{tabular}
\caption{A model and its $S$-dual.  $I_B$, for example, represents the $B$-model in complex structure $I$, which is its own $S$-dual.（原文 Table~2）}
\label{tab:sdual-models}
\end{table}
'''


def main():
    s = io.open(P, encoding='utf-8').read()
    if '\\halign' not in s:
        print('skip: no halign left in 13-s05.tex')
        return
    i = s.find(START)
    if i < 0:
        print('!! start marker missing')
        sys.exit(1)
    j = s.find(END, i)
    if j < 0:
        print('!! end marker missing')
        sys.exit(1)
    j += len(END)
    s = s[:i] + TABLE + s[j:]
    io.open(P, 'w', encoding='utf-8').write(s)
    print('ok 13-s05.tex halign left:', s.count('\\halign'))


if __name__ == '__main__':
    main()
