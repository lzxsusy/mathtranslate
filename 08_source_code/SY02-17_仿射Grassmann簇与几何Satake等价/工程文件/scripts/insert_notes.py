# -*- coding: utf-8 -*-
"""在指定行末追加 \\zy{...} 译注（改写前校验该行行尾片段，防止错位）。

每条记录：(文件名, 行号(1-based), 行尾必须包含的片段, 追加的 TeX 文本)
运行后在 stdout 输出每条的状态；任何一条校验失败则整体不写。
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CH = os.path.join(ROOT, "源码", "chunks")

NOTES = [
    ("ch00.tex", 127, "后一概念在本讲义中不会出现。",
     r"\zy{这里区分的是「严格」归纳概形与概形范畴中一般的归纳对象：nLab 词条 ind-scheme"
     r"（\url{https://ncatlab.org/nlab/show/ind-scheme}，2023-11-11 修订）把 ind-scheme 定义为概形范畴的"
     r"ind-对象，不要求过渡映射为闭浸入，并指出形式概形只对应其中一部分对象。本讲义只用到严格版，"
     r"故正文未再区分。[来源：nLab ind-scheme，2023-11-11；与原文 \S0.3.2 此处附注互校。]}"),

    ("ch01.tex", 22, "构成的集合。",
     r"\zy{nLab 词条 affine Grassmannian（\url{https://ncatlab.org/nlab/show/affine+Grassmannian}，"
     r"2023-08-15 修订）的定义逐条标注为「Definition 1.1.1 of [Zhu2016]」「Definition 1.1.2 of [Zhu2016]」，"
     r"即直接采用本文 \S1.1 的定义；一般群 $G$ 的情形则标注「Section 1.2 of [Zhu2016]」。"
     r"[来源：nLab affine Grassmannian，2023-08-15。]}"),

    ("ch02.tex", 23, r"把 $L(X\otimes_k F)$ 记作 $LX$。",
     r"\zy{这里 $L$ 与 $L^+$ 是函子式的（群）归纳概形；nLab 词条 loop group"
     r"（\url{https://ncatlab.org/nlab/show/loop+group}，2026-03-21 修订）讨论的则是拓扑环路群，"
     r"并记同胚兼半直积分解 $\mathcal{L}G\simeq G\times\Omega G$。两套对象要到 \S\ref{top loop group} 才真正接上。"
     r"[来源：nLab loop group，2026-03-21；与原文 \S1.3、\S1.6 互校。]}"),

    ("ch03.tex", 28, r"（见 \cite{BL2}）。",
     r"\zy{Beauville--Laszlo 下降定理即下文定理 \ref{descent lemma}：把 $D^*$ 上的平凡化与 $D$ 上的数据粘成"
     r"曲线上的丛。它是定理 \ref{glob aff} 的技术核心。nLab 无对应词条，本条只据原文所引 \cite{BL2}。"
     r"[来源：A 级，\cite{BL2}。]}"),

    ("ch03.tex", 75, "我们更愿意给出一个更典范的构造。",
     r"\zy{下文用 Tate 空间与格给出 $\mL_{\det}$ 的典范构造；$\GL_n$ 情形下它对应相对行列式 $\det(\La_1|\La_2)$，"
     r"其 $L^+G$-等变性正是 \S2.5 中中心扩张 \eqref{central extension} 的来源，并在 \S3.4 用于 "
     r"$\Gr_{\Ran}$ 上的刚性化线丛。[来源：原文 \S1.5、\S2.5、\S3.4 自身。]}"),

    ("ch07.tex", 106, r"细节见 \cite[\S~7]{Kac}。",
     r"\zy{关于 nLab：其词条 central extension（\url{https://ncatlab.org/nlab/show/central+extension}，"
     r"2025-02-16 修订）目前只有导引性内容、未给可引用的定义，故本条不以该词条为依据，而依 "
     r"\cite[Chap.~4, \S~7]{Kac}：$\widehat{L\frakg}=\frakg(F)\oplus k\mathbf{1}$ 的括号由留数给出，"
     r"这与 $\widehat{LG}$ 的中心扩张 \eqref{central extension} 在无穷小层面相对应。"
     r"[来源：A 级 \cite{Kac}；nLab central extension 仅记其现状。]}"),

    ("ch08.tex", 31, "记结构映射。",
     r"\zy{$\Gr_{\underline G,X^I}$ 是「把抛物结构放在 $I$ 个点上」的族；\S\ref{Ran space} 用 Ran 空间"
     r"把这些族按点集之并粘成 $\Gr_{\Ran}$，分解性质即在该对象上表述。nLab 词条 Ran space 与 "
     r"factorization algebra 记的正是这一框架。[来源：nLab Ran space（2020-07-27）、"
     r"factorization algebra（2026-08-16）。]}"),

    ("ch09.tex", 80, r"它连 \'etale 拓扑下的层都不是。",
     r"\zy{nLab 词条 Ran space（\url{https://ncatlab.org/nlab/show/Ran+space}，2020-07-27 修订）的定义正是 "
     r"$\mathrm{Ran}_X:=\varinjlim_I X^I$，$I$ 跑非空有限集、态射为满射，与正文一致；该词条注明此概念得名于 "
     r"Ziv Ran，系统使用见 Beilinson--Drinfeld, \emph{Chiral algebras}。"
     r"[来源：nLab Ran space，2020-07-27；A 级 \cite{BD}。]}"),

    ("ch10.tex", 46, r"可把 \eqref{one pt uni map} 看作单值化映射。",
     r"\zy{这正是 nLab 词条 Weil uniformization theorem"
     r"（\url{https://ncatlab.org/nlab/show/Weil+uniformization+theorem}，2023-04-04 修订）所述的双商 "
     r"$\Bun_{\underline G}\simeq[\underline G^{X^*}\backslash\Gr_{\underline G,x}]$；该词条并把函数域情形与"
     r"数域侧的 $G(F)\backslash G(\mathbb{A})/G(\mO)$ 并列。[来源：nLab Weil uniformization theorem，"
     r"2023-04-04；A 级 \cite{BL}、\cite{He}。]}"),

    ("ch12.tex", 16, r"的不可约对象恰为这些 $\on{IC}_\mu$。",
     r"\zy{反常层之名有误导：nLab 词条 perverse sheaf（\url{https://ncatlab.org/nlab/show/perverse+sheaf}，"
     r"2026-10-16 修订）开篇即指出这类对象「既非 perverse 也非 sheaf」，而 $\on{P}(X)$ 是 $D^b_c(X)$ 的"
     r"全 Abel 子范畴。$\IC_\mu$ 与相交上同调的关系见 nLab 词条 intersection cohomology（2023-05-07 修订）。"
     r"[来源：nLab perverse sheaf、intersection cohomology。]}"),

    ("ch12.tex", 80, "真正的证明将基于后面对卷积积作为融合积的解释。",
     r"\zy{这里用的是 Tannaka 对偶的「纤维函子」形式：由张量函子 $F:\mC\to\on{Vect}$ 的张量自同构群重建"
     r"群概形，一般形式见 nLab 词条 Tannaka duality（\url{https://ncatlab.org/nlab/show/Tannaka+duality}，"
     r"2025-07-28 修订）；本文把它用于 $\mC=\Sat_G$。[来源：nLab Tannaka duality，2025-07-28。]}"),

    ("ch13.tex", 20, r"通常称为 $G$ 的 \textbf{Langlands 对偶群}。",
     r"\zy{nLab 词条 Langlands dual group（\url{https://ncatlab.org/nlab/show/Langlands+dual+group}，"
     r"2014-09-07 修订）目前只列参考文献、未给定义，故不引为定义依据；本条依原文所引综述 \cite{Sp}（A 级）。"
     r"[来源：A 级 \cite{Sp}；nLab 词条现状如上。]}"),

    ("ch14.tex", 99, r"它们来自 $X^I$ 的对称性。",
     r"\zy{「交换约束是附加数据」值得强调：nLab 词条 geometric Satake equivalence"
     r"（\url{https://ncatlab.org/nlab/show/geometric+Satake+equivalence}，2024-07-22 修订）即警告，该等价左侧"
     r"「正确的交换约束的构造是微妙的——它是附加的数据，而不只是幺半结构的性质」。"
     r"本文引入融合积正是为构造这一约束。[来源：nLab geometric Satake equivalence，2024-07-22；原文 \S5.4 自身。]}"),

    ("ch17.tex", 18, "存在良好的 Grothendieck 六函子形式体系。",
     r"\zy{该六函子形式体系的一般框架见 nLab 词条 six operations"
     r"（\url{https://ncatlab.org/nlab/show/six+operations}，2026-09-30 修订）。"
     r"[来源：nLab six operations，2026-09-30。]}"),

    ("ch04.tex", 26, "(2) 由 (1) 直接推出。",
     r"\zy{这里与拓扑环路群正式接上：nLab 词条 loop group"
     r"（\url{https://ncatlab.org/nlab/show/loop+group}，2026-03-21 修订）记拓扑环路群的同胚分解 "
     r"$\mathcal{L}G\simeq G\times\Omega G$；本文所得是更强的陈述 $\Gr\cong\Omega K$（A 级：\cite[\S 8.3]{PS}）。"
     r"[来源：nLab loop group，2026-03-21；A 级 \cite{PS}。]}"),
]

# 额外：给 §3.3 Ran 空间小节加 label，供热注引用
LABELS = [("ch09.tex", 70, r"\subsection{Ran 空间}", r"\subsection{Ran 空间}\label{Ran space}")]


def main():
    cache = {}
    ok = True
    plan = {}
    for fname, lineno, tail, note in NOTES:
        path = os.path.join(CH, fname)
        if fname not in cache:
            with io.open(path, encoding="utf-8") as f:
                cache[fname] = f.read().split("\n")
        lines = cache[fname]
        line = lines[lineno - 1]
        if tail not in line:
            print("FAIL  %s:%d 行尾未找到片段 %r" % (fname, lineno, tail))
            ok = False
            continue
        if r"\zy{" in line and line.rstrip().endswith("}"):
            pass
        plan.setdefault(fname, {}).setdefault(lineno, []).append(note)
        print("OK    %s:%d  -> 追加译注" % (fname, lineno))

    for fname, lineno, old, new in LABELS:
        path = os.path.join(CH, fname)
        if fname not in cache:
            with io.open(path, encoding="utf-8") as f:
                cache[fname] = f.read().split("\n")
        lines = cache[fname]
        if lines[lineno - 1].strip() != old:
            print("FAIL  %s:%d 行内容不是 %r" % (fname, lineno, old))
            ok = False
            continue
        lines[lineno - 1] = new
        print("OK    %s:%d  加 label" % (fname, lineno))

    if not ok:
        print("有校验失败，未写入任何文件。")
        return 1

    for fname, edits in plan.items():
        lines = cache[fname]
        for lineno, notes in edits.items():
            lines[lineno - 1] = lines[lineno - 1].rstrip() + "".join(notes)
        path = os.path.join(CH, fname)
        with io.open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(lines))
        print("WROTE %s (%d 处)" % (fname, len(edits)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
