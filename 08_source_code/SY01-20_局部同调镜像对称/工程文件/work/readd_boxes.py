# -*- coding: utf-8 -*-
import io

SRC = r"<本地路径>"

ch11 = r"""
\begin{conceptbox}{轨道范畴（回顾）}
前面 \S3c 已给出轨道范畴的精确定义：\textbf{对象与 $\mathcal{C}$ 相同}，态射取
$\hom_{\mathcal{C}/K}(X,Y)=\bigoplus_{\lambda\in\widehat{K}}\hom_{\mathcal{C}}(X(\lambda),Y)$，
其中 $X(\lambda)$ 表示把等变结构按特征标 $\lambda$ 扭一下。本节用它把「先限制到子群 $H$、再商掉 $H^{\perp}$」写成全忠实嵌入，这正是扭 Künneth 公式在代数侧的来源；详细讨论与例子见 \S3c 的概念框。
\par\smallskip\noindent{\footnotesize 参考：Keller, \emph{On triangulated orbit categories}, arXiv:math/0610212。}
\end{conceptbox}
"""

ch14 = r"""
\begin{conceptbox}{dg 范畴与 $A_\infty$ 范畴（回顾）}
dg 范畴的态射空间是上链复形、合成严格结合；$A_\infty$ 范畴只要求合成在链同伦意义下结合，高阶运算 $\mu^d$ 记录结合子偏离严格结合的程度。两者可通过「同伦转移」互相转换（Keller、Seidel），而附录 A 的 Eilenberg--Zilber 收缩正是构造这种转移的技术工具——这也解释了为什么扭 Künneth 公式的证明要在这里落脚。
\par\smallskip\noindent{\footnotesize 参考：Keller, arXiv:math/0601185；Seidel, \emph{Fukaya categories and Picard--Lefschetz theory}, 2008。}
\end{conceptbox}
"""

for name, block in (("ch11", ch11), ("ch14", ch14)):
    p = SRC + "\\" + name + ".tex"
    s = io.open(p, encoding="utf-8").read()
    io.open(p, "w", encoding="utf-8").write(s.rstrip() + "\n" + block)
    print("appended to", name)
