# -*- coding: utf-8 -*-
import io, os, re

SRC = r'<本地路径>'
b = io.open(SRC, encoding='utf-8').read()
orig = b

def rep(old, new, count=1):
    global b
    n = b.count(old)
    if n != count:
        raise SystemExit('COUNT %d (want %d): %r' % (n, count, old[:60]))
    b = b.replace(old, new)

# ---- 1. structural / factual fixes ----
rep(r'\section{\texorpdfstring{\(N\to\infty\)}{N\textbackslash to\textbackslash infty}}',
    r'\section{\texorpdfstring{\(N\to\infty\)}{N 趋于无穷}}')
rep("(E,F)+(E'F')", "(E,F)+(E',F')")
rep('整体世界体异常', '整体世界体反常')
rep('成核出', '成核产生')
rep('该群的加法律', '该群的加法')
rep('位形', '构型', 3)

# ---- 2. quotes / pandoc artifacts ----
for a, c in [('”K-理论”', '“K-理论”'), ('”上同调”', '“上同调”'), ('”结”', '“结”'),
             ('”磁荷”', '“磁荷”'), ('”旁观”', '“旁观”'), ('”规范丛”', '“规范丛”'),
             ('”Fredholm 算子”', '“Fredholm 算子”'), ('”Morita 等价”', '“Morita 等价”'),
             ('”只不过”', '“只不过”'), ('”补”', '“补”'), ('”唯一”', '“唯一”')]:
    if a in b:
        b = b.replace(a, c)
b = b.replace('------', '——')
b = b.replace('{[}文献{]}', '[文献]')
b = b.replace('W”', r'W^{\prime\prime}')

# ---- 3. reference placeholders ----
rep('也与理解 RR 场有关 [文献]。', '也与理解 RR 场有关 [6--8,3]。')
rep('整体异常 [文献]。', '整体异常 [9--13,7,8,3]。')
rep(r'\(E_8\) 规范丛 [文献]。', r'\(E_8\) 规范丛 [13,14,3]。')
rep(r'它最早是在 [文献] 中与 \(D\)-膜联系起来使用的', r'它最早是在 [20] 中与 \(D\)-膜联系起来使用的')

# ---- 4. numbered equations (match original numbering) ----
def eq(old, tag, label):
    global b
    n = b.count(old)
    if n != 1:
        raise SystemExit('EQ COUNT %d: %r' % (n, old[:50]))
    b = b.replace(old, '\\begin{equation}\\tag{%s}\\label{%s}\n%s\n\\end{equation}' % (tag, label, old.strip()[2:-2].strip()))

eq(r'\[f(g)=fg,\]', '1.1', 'eq:1.1')
eq(r'\[(E,F)\leftrightarrow(E\oplus G,F\oplus G).\]', '1.2', 'eq:1.2')
eq(r"\[(E,F)+(E',F')=(E\oplus E',F\oplus F').\]", '1.3', 'eq:1.3')
eq(r'\[\int_U\frac{G_p}{2\pi}=\,{\mathrm integer}.\]', '2.1', 'eq:2.1')
eq(r'\[V(T)={1\over g_{st}}\mathrm{Tr}\,F(T),\]', '3.1', 'eq:3.1')

# 3.2 first occurrence, 3.3 second
oldT = r'\[T=\frac{\vec\sigma\cdot\vec x}{|x|}f(|x|),\]'
assert b.count(oldT) == 2
i = b.find(oldT)
b = b[:i] + '\\begin{equation}\\tag{3.2}\\label{eq:3.2}\nT=\\frac{\\vec\\sigma\\cdot\\vec x}{|x|}f(|x|)\n\\end{equation}' + b[i+len(oldT):]
i = b.find(oldT)
b = b[:i] + '\\begin{equation}\\tag{3.3}\\label{eq:3.3}\nT=\\frac{\\vec\\sigma\\cdot\\vec x}{|x|}f(|x|)\n\\end{equation}' + b[i+len(oldT):]

eq(r'\[\left(\begin{matrix}1 & 0 \\ 0 & -1\\\end{matrix}\right)\]', '3.4', 'eq:3.4')
eq(r'\[{\mathcal A}_\alpha\otimes {\mathcal K}={\mathcal A}_\beta\otimes {\mathcal K}.\]', '3.5', 'eq:3.5')
eq(r'\[M_{\alpha\gamma}\leftrightarrow M_{\beta\gamma}.\]', '4.1', 'eq:4.1')
eq(r"\[E\otimes \overline W \leftrightarrow E\otimes \overline{W'}\]", '4.2', 'eq:4.2')

# references to numbered equations
rep('比（式）微妙得多。对（式）存在', '比\\eqref{eq:2.1}微妙得多。对\\eqref{eq:2.1}存在')
rep('其中 \\(U\\) 是（式）中矩阵', '其中 \\(U\\) 是\\eqref{eq:3.4}中矩阵')

# ---- 5. page anchors (p2-p18) ----
anchors = [
    (2, '包裹在时空子流形'),
    (3, '为了分类'),
    (5, '这一陈述意味着'),
    (10, '时一样，我们希望用满足通常那类等价关系'),
    (12, None, '\\subsection{弦论的推广？}'),
    (14, '投射模构成一个半群'),
    (16, '最显然的左'),
    (17, '所以投射右'),
]
for item in anchors:
    if len(item) == 3 and item[1] is None:
        n, _, key = item
        rep(key, '\\SourcePage{%d}%s' % (n, key))
    else:
        n, key = item
        rep(key, '\\SourcePage{%d}%s' % (n, key))

# inline anchors (page starts mid-paragraph)
inline = [
    (4, '事实上（尽管一些数学细节'),
    (6, '也在渐近 AdS'),
    (7, '其中当'),
    (8, '如果我们试图把横向方向紧致化'),
    (9, '同伦群都为零'),
    (11, '是平凡的秩一复丛'),
    (13, '这一猜想的证据相当有限'),
    (15, '在复共轭下彼此等价'),
]
for n, key in inline:
    rep(key, '\\SourcePage{%d}%s' % (n, key))

# ---- 6. translator notes ----
rep('对于理解某种整体世界体反常是必需的', '对于理解某种整体世界体反常\\TN{原文作 global worldvolume anomaly；旧译「整体世界体异常」，此处按物理学惯例改「反常」。}是必需的')
rep('在 \\(x=0\\) 附近存在一个拓扑性的“结”', '在 \\(x=0\\) 附近存在一个拓扑性的“结”\\TN{原文 topological knot，指快子场本征值在无穷远处的缠绕，非纽结理论中的「结」。}')
rep('（最后一个条件使 \\(T\\) 成为“Fredholm 算子”。）', '（最后一个条件使 \\(T\\) 成为“Fredholm 算子”。\\TN{原文 Fredholm operator；此处指有界自伴、谱离散且零非聚点的算子。}）')
rep('称为 Morita 等价。它最早是在', '称为 Morita 等价\\TN{Morita equivalence；旧译名不统一，本文一律作 Morita 等价。}。它最早是在')

# ---- 7. references ----
refs = r'''
\SourcePage{18}
\section*{参考文献}
\TN{参考文献保留原文英文条目，编号与原文一致；未逐条中译，以免二次转写失真。}
{\small
\begin{enumerate}[label={[\arabic*]},leftmargin=2.4em,itemsep=2pt,topsep=4pt]
\item A. Sen, ``Tachyon Condensation On The Brane-Antibrane System,'' JHEP 9808:012 (1998), hep-th/9805170.
\item E. Witten, ``D-Branes And K-Theory,'' JHEP 9812:019 (1998), hep-th/9810188.
\item E. Diaconescu, G. Moore, and E. Witten, ``E8 Gauge Theory, And A Derivation Of K-Theory From M-Theory,'' hep-th/0005091.
\item D. Freed and E. Witten, ``Anomalies In String Theory With D-Branes,'' hep-th/9907189.
\item A. Connes, M. Douglas, and A. Schwarz, ``Noncommutative Geometry And Matrix Theory: Compactification On Tori,'' JHEP 9802:003 (1998), hep-th/9711162.
\item D. S. Freed and M. J. Hopkins, ``On Ramond-Ramond Fields And K-Theory,'' JHEP 0005:044 (2000), hep-th/0002027.
\item E. Witten, ``Duality Relations Among Topological Effects In String Theory,'' JHEP 0005:031 (2000), hep-th/9912086.
\item G. Moore and E. Witten, ``Self-Duality, Ramond-Ramond Fields, And K-Theory,'' JHEP 0005:032 (2000), hep-th/9912279.
\item M. Bershadsky, C. Vafa, and V. Sadov, ``D-Branes And Topological Field Theories,'' Nucl. Phys. B463 (1996) 420.
\item M. B. Green, J. A. Harvey, and G. Moore, ``I-Brane Inflow And Anomalous Couplings On D-Branes,'' Class. Quant. Grav. 14 (1997) 47, hep-th/9605033.
\item E. Cheung and Z. Yin, ``Anomalies, Branes, and Currents,'' Nucl. Phys. B517 (1998) 69, hep-th/9710206.
\item G. Moore and R. Minasian, ``K-Theory And Ramond-Ramond Charge,'' JHEP 9711:002 (1997), hep-th/9710230.
\item E. Witten, ``On Flux Quantization In M-Theory And The Effective Action,'' J. Geom. Phys. 22 (1997) 1, hep-th/9609122.
\item M. Fabinger and P. Horava, ``Casimir Effect Between World-Branes In Heterotic M-Theory,'' Nucl. Phys. B580 (2000) 243, hep-th/0002073.
\item K. Hori, ``D-Branes, T-Duality, and Index Theory,'' hep-th/9902102.
\item P. Horava, ``Type IIA D-Branes, K Theory, and Matrix Theory,'' ATMP 2 (1999) 1373, hep-th/9812135.
\item A. Kapustin, ``D-Branes In A Topologically Nontrivial B-Field,'' hep-th/9909089.
\item P. Bouwknegt and V. Mathai, ``D-Branes, B Fields, And Twisted K Theory,'' JHEP 0003:007 (2000), hep-th/0002023.
\item M. F. Atiyah and G. B. Segal, unpublished.
\item A. Schwarz, ``Morita Equivalence And Duality,'' Nucl. Phys. B534 (1998) 720, hep-th/9805034; A. Schwarz and B. Pioline, ``Morita Equivalence And T Duality (Or B Versus Theta),'' JHEP 9908:021 (1999), hep-th/9908019.
\item N. Seiberg and E. Witten, ``String Theory And Noncommutative Geometry,'' JHEP 9909:032 (1999), hep-th/9908142.
\end{enumerate}
}
'''
b = b.rstrip() + '\n' + refs

io.open(SRC, 'w', encoding='utf-8').write(b)
print('OK chars', len(orig), '->', len(b), 'sections', b.count('\\section{'), 'anchors', b.count('\\SourcePage'))
