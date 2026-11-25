# -*- coding: utf-8 -*-
"""把 harvmac 三处原始 \\halign 表格替换成 booktabs tabular。
    只改 skel/ 下的脚手架；译者在表内文字（如 Model 列）上按术语表翻译。"""
import io, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TABLE1 = r'''\begin{table}[htbp]
\centering
\begin{tabular}{ll}
\toprule
$G$ & ${}^L G$ \\
\midrule
$U(N)$ & $U(N)$ \\
$SU(N)$ & $PSU(N)=SU(N)/\Bbb{Z}_N$ \\
$Spin(2n)$ & $SO(2n)/\Bbb{Z}_2$ \\
$Sp(n)$ & $SO(2n+1)$ \\
$Spin(2n+1)$ & $Sp(n)/\Bbb{Z}_2$ \\
$G_2$ & $G_2$ \\
$E_8$ & $E_8$ \\
\bottomrule
\end{tabular}
\caption{Examples of the correspondence between a Lie group $G$ and its Langlands or GNO dual ${}^L\negthinspace G$.（原文 Table~1）}
\label{tab:gno-dual}
\end{table}'''

TABLE2 = r'''\begin{table}[htbp]
\centering
\begin{tabular}{ll}
\toprule
Model & $S$-Dual \\
\midrule
${I_B}$ & ${I_B}$ \\
${I_A}$ & ${I_A}$ \\
${J_B}$ & ${K_A}$ \\
${J_A}$ & ${K_B}$ \\
${K_B}$ & ${J_A}$ \\
${K_A}$ & ${J_B}$ \\
\bottomrule
\end{tabular}
\caption{A model and its $S$-dual. ${I_B}$, for example, represents the $B$-model in complex structure $I$, which is its own $S$-dual.（原文 Table~2）}
\label{tab:sdual-models}
\end{table}'''

TABLE3 = r'''\begin{table}[htbp]
\centering
\begin{tabular}{ll}
\toprule
Group & Center \\
\midrule
$SU(N)$ & $\Bbb{Z}_N$ \\
$Spin(2n+1)$ & $\Bbb{Z}_2$ \\
$Spin(4n+2)$ & $\Bbb{Z}_4$ \\
$Spin(4n)$ & $\Bbb{Z}_2\times\Bbb{Z}_2$ \\
$Sp(n)$ & $\Bbb{Z}_2$ \\
$E_6$ & $\Bbb{Z}_3$ \\
$E_7$ & $\Bbb{Z}_2$ \\
\bottomrule
\end{tabular}
\caption{Simple and simply-connected Lie groups with non-trivial centers. $F_4$, $G_2$, and $E_8$, which are omitted, have trivial center.（原文 Table~3；原文此处误作 $F_2$、$G_4$）}
\label{tab:centers}
\end{table}'''

TARGETS = [
    ('01-s01.tex', 'dual $^L\\negthinspace G$', TABLE1),
    ('13-s05.tex', 'Table 2.', TABLE2),
    ('19-s07.tex', 'non-trivial centers', TABLE3),
]


def replace_halign(text, tbl):
    """把包含 \\halign 的一整段 raw TeX 换掉：从最近的 \\centerline{ 到该表 caption 的
    \\vbox{...}} 结束处（以 '}}\\par\\medskip' 或 '}}' 收尾）。"""
    out, i = [], 0
    while True:
        j = text.find('\\halign{', i)
        if j < 0:
            out.append(text[i:])
            break
        start = text.rfind('\\centerline{', i, j)
        if start < 0:
            start = j
        # 找此表 caption 结束：\halign 之后第一个 '}}' 后接 \par\medskip 或空行
        k = text.find('\\nobreak', j)
        m = text.find('\\noindent Table', j)
        ends = []
        pat = re.compile(r'\}\}\s*\\par\\medskip|\}\}\s*\n\s*\n|\}\}\s*\\nobreak|\}\}\s*(?=\\n?\\s*$)', re.M)
        mm = None
        for mm in pat.finditer(text, j):
            ends.append(mm)
            break
        if mm is None:
            ends = list(pat.finditer(text, j))
            if not ends:
                out.append(text[i:])
                break
            mm = ends[0]
        out.append(text[i:start])
        out.append(tbl)
        i = mm.end()
    return ''.join(out)


def main():
    for fname, needle, tbl in TARGETS:
        p = os.path.join(ROOT, 'skel', fname)
        s = io.open(p, encoding='utf-8').read()
        if '\\halign' not in s:
            print('skip(no halign):', fname)
            continue
        if needle not in s:
            print('!! needle missing:', fname, needle)
            continue
        new = replace_halign(s, tbl)
        io.open(p, 'w', encoding='utf-8').write(new)
        print('ok', fname, 'halign left:', new.count('\\halign'))


if __name__ == '__main__':
    main()
