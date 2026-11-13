# 讲义体例与符号约定（STYLE v1.0）

> 本文件是写作的**硬约束**。任何一章不合体例，Integration 会退回重写。
> 目标：一本 80–100 页、数学上可自洽检验、学生能自学的研读讲义，而不是论文缩写。

## 0. 读者与目标

- 读者：学过量子力学、一学期场论或微分几何的研究生；**没有**学过共形场论、不熟悉指标定理与模空间。
- 读完应能：独立复述本文论证链；自己算 (1.4)(3.1)(3.2)(4.28)(4.51)；判断"这是定理还是纲领"；知道每一处细节在哪本书的哪一页补。
- 判断标准：一个没读过本文的研究生，只靠本讲义 + 原文页图，能把 §3–§4 的主链推一遍。

## 1. 每章固定结构（缺一不可）

```
\chapter{...}
\section{这一章要解决什么}     1 段，问题导向，不写"本章介绍..."
\section{原文说了什么}         带锚点的短陈述；只写原文真有的
\section{原文没说的细节}       逐条列出（编号 G-x），说明缺什么、为什么重要
\section{补出的推导}           编号 D-x；每步可检验；不能写"容易看出"
\section{与其他来源的对照}     表格：本文 / 河野 / 上野 / Moore / Schottenloher / 李思
\section{陷阱与约定}           符号冲突、因子 2、正负号、归一化
\section{练习}                 4–8 题，分「复算型 / 推导型 / 判断题」，答案提示进 appC
\section{本章边界}             哪些已证、哪些我们补、哪些仍是猜想
```

## 2. 出处标注（四档，必须用对）

- `\src{N}` → 本文印刷页 N（CMP 121 (1989) 351–399）。
- `\src[N]{x.y}` → 本文公式 (x.y)。公式编号一律用原文编号。
- `[河野 p.N]`、`[上野 §x.y]`、`[Moore p.N]`、`[Schottenloher p.N]`、`[李思 p.N]` → 教材页码（Moore 用**页脚页**；河野 PDF=书页+14；Schottenloher PDF=书页+12；李思 PDF=书页+12）。
- `[我们]` → 我们自己补的推导/判断；不得冒充原文或教材。
- 引原文原话必须给英文原句 + 页码；引译文标 `[译注]`。

## 3. 数学写作规则

1. 每个公式先给**出发点**（哪条定义/哪个已知结论），再给结果；中间步骤不许跳超过两步。
2. 出现"可以证明"时，必须给：谁证的、在哪、证明思路一句话；给不出就改成"我们未找到证明"。
3. 因子 2、符号、归一化：凡与常见约定不同的地方，用 `\begin{keypoint}` 框单独说明。
4. 不用"显然""容易看出""众所周知"（除非真的是定义级结论）。
5. 所有符号首次出现必须定义；与附录 A 冲突时以附录 A 为准。
6. 图：能用 TikZ 画的（模空间、穿刺点、手术、辫群）就画；不许贴第三方图片。
7. 中文为主，术语首次出现给英文；关键术语统一译名（见附录 A.2）。

## 4. 全局符号（与附录 A 一致；不得私改）

- $M$：定向闭三维流形；$\Sigma$：切开的黎曼面，亏格 $g$，$n$ 个标记点。
- $G$：紧单连通单 Lie 群，$d=\dim G$，$h^\vee$ 对偶 Coxeter 数；$\mathfrak{g}=\mathrm{Lie}\,G$。
- 归一化：$\mathrm{Tr}$ 取定义表示（$SU(N)$ 的 $N$ 维）的迹；一般单群取长根平方 $=2$。**本文 $L$ 与河野的 $\mathrm{CS}$ 差 $2\pi k$**（见 appA）。
- $A=A_idx^i$ 为 $\mathfrak{g}$-值 1-形式联络；$F=dA+A\wedge A$；$D_i=\partial_i+[A_i,\cdot]$（注意 Witten 的 $A_i\to A_i-D_i\varepsilon$）。
- CS 作用量：$L=\dfrac{k}{4\pi}\int_M\mathrm{Tr}\big(A\wedge dA+\tfrac23A^3\big)$，定向闭流形上 $k\in\mathbb Z$。
- 相空间：$\mathcal A$ = $\Sigma$ 上联络空间；$\mathcal M=\mathrm{Hom}(\pi_1\Sigma,G)/G$；辛形式 $\omega=\dfrac{k}{4\pi}\int_\Sigma\mathrm{Tr}(\delta A\wedge\delta A)$。
- 预量子化线丛 $\mathcal L$（行列式线丛），Quillen 度规；量子 Hilbert 空间 $\mathcal H_\Sigma^{(J)}=H^0(\mathcal M_J,\mathcal L^{\otimes k})$。
- 最高权 $\lambda$，$\rho=\tfrac12\sum_{\alpha>0}\alpha$；仿射 level $k$；共形权 $h_\lambda=\dfrac{(\lambda,\lambda+2\rho)}{2(k+h^\vee)}$。
- $SU(N)$：$q=e^{2\pi i/(N+k)}$（原文 (4.21)）；一般 $G$：$q=e^{2\pi i/(k+h^\vee)}$。
- $SU(2)$：$S_{jl}=\sqrt{\tfrac{2}{k+2}}\sin\dfrac{\pi(2j+1)(2l+1)}{k+2}$。
- 记号 $\mathcal M$ 与 $\mathcal M_J$ 不混用：$\mathcal M$ 实模空间，$\mathcal M_J$ 复结构 $J$ 下的 Kähler 模空间。

## 5. 每章体量

- 正文 6–10 页（LaTeX 编译后），推导占一半以上篇幅。
- 每章至少 1 个 `derivation` 框（多步推导），至少 1 个 `keypoint` 框（约定陷阱）。
- 全讲义目标 80–100 页；超过 110 页先删，不足 75 页补推导。

## 6. 引用与文献

- 本文公式用原文编号，不重编号。
- 教材用 `[河野 p.N]` 形式；**不得**用"某书说过"。
- 后世结果（Khovanov、Witten 2011、Kapustin–Witten）必须标年份，并与 1989 年的陈述分开。

## 7. 交付与文件

- 每章一个文件：`chapters/chNN_name.tex`，只写自己的文件。
- 不改 `preamble.tex`、`main.tex`、其他章（需要新宏先找 Lead）。
- 写完自检：`python deliverables/engineering/scripts/check_anchors.py ...` 与两次 xelatex 无错。
- 完成后三行汇报：文件、页数、未解决项。
