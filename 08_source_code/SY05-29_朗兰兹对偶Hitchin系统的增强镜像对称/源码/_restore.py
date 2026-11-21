# -*- coding: utf-8 -*-
import io, sys

P1 = "1987 年，Hitchin \\cite{hitchin} 考察 4 维 Yang--Mills 方程在二维上的约化，引入并研究了黎曼曲面上某一类自对偶方程的解所构成的模空间。结果发现，这个模空间具有“极其丰富的几何结构”。"
P2 = "对我们来说，镜像对称有三个相关的方面：拓扑镜像对称、同调镜像对称，以及 Strominger--Yau--Zaslow 镜像对称。"
P3 = "为表述 \\cite{hausel-thaddeus} 的这个镜像对称版本，我们需要把模空间说得更精确些。对 $\\SL_n$，取 $\\M:=\\M_\\Dol$ 为 $C$ 上秩 $n$、$E$ 固定、行列式线丛固定且次数为 $1$、Higgs 场无迹（$\\Phi\\in H^0(C;\\End_0(E)\\otimes K)$）的稳定 Hitchin 对的模空间。对 $\\PGL_n$，考虑 $\\Gamma:=\\Jac_C[n]$——即 $C$ 上 $n$ 阶线丛构成的群——在 $\\SL_n$ 的模空间 $\\M$ 上的作用，并令 $\\M^\\vee:=\\M/\\Gamma$。于是 $\\M$ 是光滑的拟射影簇，而 $\\M^\\vee$ 是拟射影的轨形。在我们的讨论中，还需要模空间上的额外扭结构，其形式是一个 gerbe"
P4 = "2007 年，Kapustin--Witten \\cite{kapustin-witten} 提出了一整套细致的思想，其要旨是从物理上把几何 Langlands 对应推导为一种增强镜像对称。他们论证：某个四维 $N=4$ 超对称 Yang--Mills 理论中研究得很充分的 $S$ 对偶（又称电磁对偶，或 Montonen--Olive 对偶 \\cite{montonen-olive}），约化到二维之后给出一种增强镜像对称，而后者又反过来蕴含了 \\cite{beilinson-drinfeld} 所表述的几何 Langlands 对应。"
P5 = "下面这些考察的原初动机，是要找到一种办法来检验 \\cite{baraglia-schaposnik,garcia-prada-etal,hitchin-characteristic} 所提出的 $(B,A,A)$ 型与 $(B,B,B)$ 型膜的猜想镜像对。迄今为止唯一的检验——常常就在这些文献中完成——是检查所提议的镜像对相对于 Hitchin 映射是否确实互为 Fourier--Mukai 对偶。而这种检验只能在 Hitchin 底上的\\emph{一般}点处进行。我们希望看到更多整体性的检验，特别是那些能在 Hitchin 映射的 $0$-纤维，即整体幂零锥上验证镜像对称提议的检验。"
P6 = "设复数乘法群 $\\T:=\\C^\\times$ 作用在一个簇（即 $\\C$ 上有限型的既约分离概形，可以可约）上。称此作用是\\textbf{半射影的} \\cite[\\S 1]{hausel-large}，如果下面三条成立："
P7 = "主要想法是：对 $\\calE\\in \\M^{s\\T}$，在 Arnold 学派 \\cite{arnold-etal} 的框架中研究受限 Hitchin 映射"
P8 = "这里我们说明，如何用仿射 Grassmannian \\cite{gortz,zhu} 把上述技术推广，以理解 wobbly 的——即不非常稳定的——上行流的重数代数。\\footnote{译注：“wobbly”是原文自造的说法，指不非常稳定的上行流；原文在此没有给出更细的定义，其含义只能由定理 \\ref{mainema} 与定理 \\ref{conjecturewobbly} 的对照看出：非常稳定的上行流是有限（proper）映射，wobbly 的则不是，但仍可以是支配的、重数非零的。[译者按（无外部依据）]}"
P9 = "最后，我们来表述一些猜想，它们正是前面许多想法的原初动机。特别地，这些猜想暗示了 $\\GL_n(\\C)$ 的不可约表示的一种新构造，并更一般地暗示了任意复约化群 $\\G$ 的不可约表示的新构造。"

def patch(fn, pairs):
    s = io.open(fn, encoding="utf-8").read()
    for old, new in pairs:
        if old not in s:
            print("MISS in", fn, ":", repr(old[:40]))
            continue
        s = s.replace(old, new, 1)
    io.open(fn, "w", encoding="utf-8", newline="\n").write(s)

patch("ch1_intro.tex", [
    ("\\section{引言}\n\n\n", "\\section{引言}\n\n" + P1 + "\n\n"),
])

patch("ch2_background.tex", [
    ("\\subsection{镜像对称}\n\n\n", "\\subsection{镜像对称}\n\n" + P2 + "\n\n"),
    ("\n\\[\n\\alpha\\in H^2(\\M^\\vee", "\n" + P3 + "\n\\[\n\\alpha\\in H^2(\\M^\\vee"),
    ("\\label{gls}\n\n\n", "\\label{gls}\n\n" + P4 + "\n\n"),
])

patch("ch3_enhanced.tex", [
    ("\\label{enhanced}\n\n\n", "\\label{enhanced}\n\n" + P5 + "\n\n"),
    ("的 Białynicki--Birula 分解}\n\n\n", "的 Białynicki--Birula 分解}\n\n" + P6 + "\n\n"),
    ("\\subsubsection{Higgs 丛的 Białynicki--Birula 分解}\n\n", "\\subsubsection{Higgs 丛的 Białynicki--Birula 分解}\n\n"),
    ("\\subsection{重数代数与拉格朗日子流形上的显式 Hitchin 系统}\n\n\n",
     "\\subsection{重数代数与拉格朗日子流形上的显式 Hitchin 系统}\n\n" + P7 + "\n"),
    ("\\subsection{wobbly 拉格朗日子流形上的显式 Hitchin 系统}\n\n\n",
     "\\subsection{wobbly 拉格朗日子流形上的显式 Hitchin 系统}\n\n" + P8 + "\n\n"),
    ("\\label{geosat}\n\n\n", "\\label{geosat}\n\n" + P9 + "\n\n"),
])
print("done")
