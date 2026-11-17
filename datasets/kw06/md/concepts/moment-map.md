# 矩映射

> `kw/concept/moment-map` · 轨道 C · 舞台：曲线与模空间 · 状态 dev

> **先自测**：矩映射的定义是什么，它怎样把 Hitchin 方程写成三个零点条件？

## 一句话

群作用在辛流形上给出的守恒量映射 $\mu:X\to\mathfrak h^*$，由 $\iota_{V(\epsilon)}\omega=\delta\mu_\epsilon$ 定义；Hitchin 方程正是三个矩映射同时为零。

## 定义

设李群 $H$ 以保持辛形式的方式作用在辛流形 $(X,\omega)$ 上，$V(\epsilon)$ 是 $\epsilon\in\mathfrak h$ 生成的基本向量场。若光滑映射 $\mu:X\to\mathfrak h^*$ 满足 $\iota_{V(\epsilon)}\omega=\delta\langle\mu,\epsilon\rangle$ 对所有 $\epsilon$ 成立，就称 $\mu$ 为矩映射。在规范理论里 $X=\mathcal W$、$H$ 为规范群，矩映射由把曲率与 $\varphi$ 在 $C$ 上积分给出。

**记号**：$\mu:X\to\mathfrak h^*$；$\iota_{V(\epsilon)}\omega=\delta\mu_\epsilon$；$\mu_I,\mu_J,\mu_K$：三个辛形式对应的矩映射；$\nu_I=\mu_J+\mathrm{i}\mu_K$。

## 要点（为什么需要它）

1. 统一语言：Hitchin 方程、超凯勒商、Bogomolny 方程都写成矩映射零点，于是辛约化的整套工具可以直接使用。
2. 三个矩映射对应三个辛形式，一起取零才给 Hitchin 方程；单个零点只给一部分方程。
3. 全纯矩映射 $\nu_I$ 的零点给 $\varphi$ 的全纯性（Hitchin 对），实矩映射 $\mu_I$ 的零点给 $F-\varphi\wedge\varphi=0$。
4. 归一化 $1/2\pi$ 不是任意的：它使 $\omega_I/2\pi$ 落在整上同调，从而 $\theta$ 角与二维、四维的瞬子数对齐。

## 核心公式

$$
$\iota_{V(\epsilon)}\omega=\delta\mu_\epsilon$$\mu_I=-\frac{1}{2\pi}\int_C\mathrm{Tr}\,\epsilon\,(F-\varphi\wedge\varphi)$$\nu_I:=\mu_J+\mathrm{i}\mu_K,\qquad \nu_I=0\iff\bar\partial_A\varphi=0$
$$

$$
$\mu_I=-\frac{1}{2\pi}\int_C\mathrm{Tr}\,\epsilon\,(F-\varphi\wedge\varphi)$
$$

$$
$\nu_I:=\mu_J+\mathrm{i}\mu_K,\qquad \nu_I=0\iff\bar\partial_A\varphi=0$
$$

## 定理与证明（或缺口）

### $\omega_J,\omega_K$ 的正合性与矩映射

存在规范不变的泛函 $\lambda_J,\lambda_K$ 使 $\omega_J=\delta\lambda_J$、$\omega_K=\delta\lambda_K$；而 $\omega_I=\omega_I'+\delta\lambda_I$，其中 $\omega_I'=-(1/4\pi)\int_C\mathrm{Tr}\,\delta A\wedge\delta A$ 的上同调类是 determinant line bundle 的曲率。

> 证明状态：**sketch**。原文 p.45 给出 $\lambda$ 的显式式并称可直接验证，未逐项写出变分计算；$\omega_I'$ 的上同调陈述只给结论。

出处：`B p.45`

## 常见误解

- 把矩映射当标量函数：它取值于 $\mathfrak h^*$，每个 $\epsilon\in\mathfrak h$ 给一个分量，定义式必须对偶地写。
- 忽略符号与归一化：原文的 $-\frac{1}{2\pi}$ 决定了 $\omega_I/2\pi$ 的整性，符号错会颠倒稳定性条件的方向。
- 把 $\nu_I$ 当成独立的第四个矩映射：它只是 $\mu_J+\mathrm{i}\mu_K$ 的复组合，真正的矩映射是三个实映射。
- 以为矩映射零点已经给出模空间：还要模去规范群，否则得到的只是解空间而不是模空间。

## 相关卡

[超凯勒商](../concepts/hyperkahler-quotient.md) · [超凯勒流形](../concepts/hyperkahler-manifold.md) · [Bogomolny 方程](../concepts/bogomolny-equation.md) · [超凯勒商与三个复结构 I, J, K](../derivations/hyperkahler-quotient.md)

## 出处（印刷页）

- B p.45（B p.45）
- B p.46（B p.46 eq (4.11)）
- B p.49（B p.49 eq (4.20)）

> 说明：A=原文（矩映射定义 $\iota_{V(\epsilon)}\omega=\delta\mu$、三个矩映射的显式式、$\omega_J,\omega_K$ 正合、$\nu_I$ 的零点与全纯性）；B=由原文重建（三条正合性论证的分步整理、归一化与整上同调的关系）；C=标准背景（辛约化的一般语言）。
