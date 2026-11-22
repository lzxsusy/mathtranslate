# Gross–Zagier 公式与 Heegner 点

> `lbook04/concept/ch5-gross-zagier` · 轨 L L 函数 · 状态 reviewed · 核验 source-only

**问题：** Heegner 点的高度为什么能计算 $L$ 函数在中心的导数，而不是 $L$ 值本身？

**一句话：** 用虚二次域 $K$ 的 Heegner 点在 $X_0(N)$ 上造出 $E(K)$ 中的点 $P_K$；Gross–Zagier 公式把 $L'(E/K,1)$ 与 $P_K$ 的 Neron–Tate 高度成正比，于是解析秩 $1$ 推出代数秩 $1$。

**别名：** `Heegner 点`、`Gross–Zagier 公式`、`Euler 系统`

## 定义

设 $E/\mathbb Q$ 导子 $N$，$K=\mathbb Q(\sqrt{-D})$ 虚二次，满足 Heegner 条件（每个 $p\mid N$ 在 $K$ 中分裂或 ramified）。取 $K$ 的理想类 $\mathfrak a$ 与对应 Heegner 点 $x_{\mathfrak a}\in X_0(N)(K)$，令 $P_K$ 为 $\sum(x_{\mathfrak a}-\infty)$ 经模参数化 $X_0(N)\to E$ 的像。Gross–Zagier（1986）：$L'(E/K,1)=c\cdot\widehat h(P_K)$，$c>0$ 显式（含 $\sqrt{|D|}$、$\Omega_E$ 与 $\int|f|^2$）。配合 Kolyvagin 的 Euler 系统：若 $L'(E/K,1)\ne0$，则 $E(K)$ 的秩为 $1$。

**记号：** $K$：虚二次域；$D$：判别式；$X_0(N)$：模曲线；$x_{\mathfrak a}$：Heegner 点；$P_K\in E(K)$；$\widehat h$：Neron–Tate 高度；$L(E/K,s)$。

## 要点

- Heegner 条件保证 $x_{\mathfrak a}$ 定义在 $K$ 上（复乘的模解释）；否则只能得到定义在更大域上的点。
- Gross–Zagier 用 Eisenstein 级数的 Fourier 系数与 Heegner 除子的交数（Gross 的局部高度）证明，核心是 $L'(E/K,1)$ 的展开。
- 结论是「解析秩 $1\Rightarrow$ 代数秩 $\ge1$」；配合 Kolyvagin 得等号，故 BSD 的秩 $1$ 情形成立。
- Gross–Kohnen–Zagier 给出权 $3/2$ 模形式与 Heegner 除子的关系，用于保证 Heegner 点非平凡（Kolyvagin 的 Euler 系统论证所需）。

## 公式

$$
L'(E/K,1)=c\cdot\widehat h(P_K),\qquad c>0
$$

$$
\operatorname{rank}E(K)\ge1\iff L'(E/K,1)\ne0\quad(\text{Gross–Zagier}+\text{Kolyvagin})
$$

## 易错点

- 本章正文（§3.3、§6.2）并未展开 Gross–Zagier：ch05.tex 全文 grep 不到 Gross/Heegner。本卡按导读补足，引用时须标明出处，不能当作原文陈述。
- Heegner 条件不能漏：$p\mid N$ 在 $K$ 中 inert 时相应的点不定义在 $K$ 上，Gross–Zagier 的公式要换成其它 Heegner 除子。

## 批注

**〔易错预警〕本章没有这一节**　ch05.tex 全文不含 Gross、Heegner 字样；BSD 只在 §3.3 的注与 §6.2 的 STW 语境被提及。本卡内容属于导读补足，sources 只锚到相邻段落，正式引用应另补 Gross–Zagier 1986 原文。

**〔背景直觉〕为什么是导数**　Heegner 点的高度是「算术」量，$L'(E/K,1)$ 是「解析」量；Gross–Zagier 把两者相等，于是「导数非零」直接给出「点非有限」，这正是 Euler 系统证明 BSD 秩 $1$ 的入口。

## 相关

[[ch5-bsd]]、[[ch5-eichler-shimura]]、[[ch5-elliptic-l]]

## 来源

- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§3.3，原书 pp. 99–100（PDF pp. 104–105）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch05.tex:346-370`
- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§6.2，原书 pp. 107（PDF pp. 112）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch05.tex:579-605`
