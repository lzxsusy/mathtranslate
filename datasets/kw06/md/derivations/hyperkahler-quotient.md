# 超凯勒商与三个复结构 I, J, K

> `kw/deriv/hyperkahler-quotient` · 轨道 C · 舞台：曲线与模空间 · 状态 dev · 5 步

> **要回答的问题**：$M_H$ 为什么是超凯勒商，而它在 $I$、$J$、$K$ 三个复结构下分别「看」到什么？

## 一句话

从场空间 $W$ 的平坦超凯勒度规出发，写出复结构 $I,J,K$ 与矩映射 $\mu_I,\mu_J,\mu_K$；$\mu_I=\mu_J=\mu_K=0$ 模去规范群即 $M_H=W///G$，而 $I$、$J$ 中的全纯条件分别给出 Hitchin 对与平坦 $G_{\mathbb C}$ 联络。

## 目标

构造 $M_H=W///G$，并在三个复结构下识别其全纯对象。

## 前提

- $W$ 是 $(A,\varphi)$ 的仿射空间，其平度量 eq (4.2) 见 `B p.41`。
- 矩映射 eq (4.11) 与 Hitchin 方程 eq (4.1) 见 `B p.39–46`。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | $W$ 上取平度量 eq (4.2)，它使 $W$ 成为平坦超凯勒流形，带三个平移不变复结构 $I,J,K$；线性组合给出 $\mathbb{CP}^1$ 族 eq (4.6)。 | 不先把 $W$ 认成超凯勒流形，就没有三个矩映射可写，也谈不上超凯勒商。 | `B p.41` | A·原文明确写了 |
| 2 | $I_w$ 的全纯坐标为 $A_z-w\varphi_z$ 与 $A_{\bar z}+w^{-1}\varphi_{\bar z}$；$w=-i$ 给 $J$、$w=1$ 给 $K$，$I_0=I$、$I_\infty=-I$，故 $\mathbb{CP}^1$ 族覆盖三个标准复结构。 | 这一步决定后面「在哪个复结构里看什么」；不把 $I,J,K$ 与 $w$ 对应起来，$I$-全纯与 $J$-全纯会混淆。 | `B p.43 eq (4.6)` | A·原文明确写了 |
| 3 | 三个矩映射 eq (4.11)：$\mu_I=-\frac{1}{2\pi}\int_C\mathrm{Tr}\,\epsilon(F-\varphi\wedge\varphi)$，$\mu_J,\mu_K$ 由 $D\varphi$ 的对称与反对称组合给出；$\mu_I=\mu_J=\mu_K=0$ 模去规范群 $G$ 即 $M_H=W///G$。 | $\mu_I=0$ 就是 $F-\varphi\wedge\varphi=0$，$\mu_J=\mu_K=0$ 就是 $D\varphi=D^*\varphi=0$；三个零点合起来才等于 Hitchin 方程。 | `B p.46 eq (4.11)` | A·原文明确写了 |
| 4 | 在 $I$ 中全纯条件是 $\nu_I=\mu_J+i\mu_K=0$，等价于 $\bar\partial\varphi=0$，即 $\varphi\in H^0(C,K_C\otimes\mathrm{ad}E)$，$(E,\varphi)$ 称 Hitchin 对。 | $I$ 中的全纯对象正是 Hitchin 对；这一步把模空间与 Higgs 丛的语言接起来，是 §4.2 稳定性讨论的入口。 | `B p.49 eq (4.20)` | A·原文明确写了 |
| 5 | 在 $J$ 中全纯条件是 $\nu_J=\mu_K+i\mu_I=0$，等价于 $F(A+i\varphi)=0$，即 $A+i\varphi$ 是平坦 $G_{\mathbb C}$ 联络。 | $J$ 中的全纯对象是平坦 $G_{\mathbb C}$ 联络；这正是 §4 后半与 §11 中 B-模型所用到的结构。 | `B p.51 eq (4.21)` | A·原文明确写了 |

## 结论

$M_H=W///G$ 是超凯勒商，因此在 $I$、$J$、$K$ 下分别是 Hitchin 对、平坦 $G_{\mathbb C}$ 联络与另一组全纯数据；同一流形在不同复结构下「看」到不同对象，正是几何 Langlands 与镜像对称的几何基础。物理上它是二维 $(4,4)$ 规范理论低能 sigma 模型的靶空间。

## 缺口

- 稳定性（删除不稳定轨道）在原文 §4.2 只是概括，超凯勒商的奇点与复几何细节未展开。

## 最容易讲错的地方

- 把三个矩映射当成一个复方程：$\mu_I,\mu_J,\mu_K$ 是三组实方程，须同时为零。
- 混淆 $I$ 与 $J$ 的全纯对象：$I$ 中是 Hitchin 对，$J$ 中是平坦 $G_{\mathbb C}$ 联络。

## 相关卡

[超凯勒商](../concepts/hyperkahler-quotient.md) · [矩映射](../concepts/moment-map.md) · [Hitchin 模空间](../concepts/hitchin-moduli.md) · [M_H 上的 sigma 模型数据与维数公式](../derivations/mh-sigma-data.md)

## 出处（印刷页）

- B p.41–51（B p.46 eq (4.11)）

> 说明：A5：平超凯勒度规、$I_w$ 族、三个矩映射与 $I$/$J$ 全纯条件均在 `B p.41–51` 明写；最没把握处是 eq (4.11) 中 $\mu_J,\mu_K$ 的显式组合被本文压缩成一句。
