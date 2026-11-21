# -*- coding: utf-8 -*-
import io

P6 = "设复数乘法群 $\\T:=\\C^\\times$ 作用在一个簇（即 $\\C$ 上有限型的既约分离概形，可以可约）上。称此作用是\\textbf{半射影的} \\cite[\\S 1]{hausel-large}，如果下面三条成立："
P7 = "主要想法是：对 $\\calE\\in \\M^{s\\T}$，在 Arnold 学派 \\cite{arnold-etal} 的框架中研究受限 Hitchin 映射"
P8 = "这里我们说明，如何用仿射 Grassmannian \\cite{gortz,zhu} 把上述技术推广，以理解 wobbly 的——即不非常稳定的——上行流的重数代数。\\footnote{译注：“wobbly”是原文自造的说法，指不非常稳定的上行流；原文在此没有给出更细的定义，其含义只能由定理 \\ref{mainema} 与定理 \\ref{conjecturewobbly} 的对照看出：非常稳定的上行流是有限（proper）映射，wobbly 的则不是，但仍可以是支配的、重数非零的。[译者按（无外部依据）]}"
P9 = "最后，我们来表述一些猜想，它们正是前面许多想法的原初动机。特别地，这些猜想暗示了 $\\GL_n(\\C)$ 的不可约表示的一种新构造，并更一般地暗示了任意复约化群 $\\G$ 的不可约表示的新构造。"

fn = "ch3_enhanced.tex"
lines = io.open(fn, encoding="utf-8").read().split("\n")

sub_idx = [i for i, l in enumerate(lines) if l.startswith("\\subsection{")]
subsub_idx = [i for i, l in enumerate(lines) if l.startswith("\\subsubsection{")]
print("subsections:", len(sub_idx), "subsubsections:", len(subsub_idx))

targets = [
    (subsub_idx[0], P6, "P6"),
    (sub_idx[1], P7, "P7"),
    (sub_idx[2], P8, "P8"),
    (sub_idx[3], P9, "P9"),
]

# insert from bottom to top so indices stay valid
for idx, para, name in sorted(targets, key=lambda t: -t[0]):
    j = idx + 1
    while j < len(lines) and lines[j].strip() == "":
        j += 1
    lines[j:j] = [para, ""]
    print("inserted", name, "before line", j + 1)

io.open(fn, "w", encoding="utf-8", newline="\n").write("\n".join(lines))
print("ok")
