# Hitchin 系统的完全可积性与 Lagrange 纤维

> `kw/deriv/hitchin-integrability` · 轨道 C · 舞台：曲线与模空间 · 状态 dev · 4 步

> **要回答的问题**：为什么 Hitchin 模空间在复结构 $I$ 中是完全可积系统，其纤维为什么是环面？

## 一句话

从 Hitchin 纤维化 $\pi:M_H\to B$ 出发，用 Casimir 多项式次数算出 $\dim B=\frac12\dim M_H$；再构造 $\frac12\dim M_H$ 个对 $\Omega_I$ Poisson 对易的 $I$-全纯哈密顿量 $H_a$，证明 $M_H$ 在 $I$ 中完全可积、纤维一般为复环面。

## 目标

由纤维化与 Poisson 对易的哈密顿量证明 $M_H$ 的完全可积性。

## 前提

- Hitchin 纤维化 $\pi:M_H\to B$ 与 Casimir 次数 $d_i$ 见 `B p.53`。
- $M_H$ 的复辛形式 $\Omega_I$ 与 Poisson 括号见 `B p.44 eq (4.9)`。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 在复结构 $I$ 中，$\varphi$ 的规范不变多项式给出 $\pi:M_H\to B$；$\mathrm{SU}(N)$ 用 $w_n=\mathrm{Tr}\,\varphi^n$（$n=2,\dots,N$），一般 $G$ 用独立 Casimir $P_i$，$B=\oplus_i H^0(C,K^{d_i})$，且 $\sum(2d_i-1)=\dim G$ eq (4.24)。 | 纤维化的底由 Casimir 多项式定；不先写对次数 $d_i$，后面的维数公式无从计算。 | `B p.53 eq (4.24)` | A·原文明确写了 |
| 2 | $\dim H^0(C,K^n)=(2n-1)(g-1)$，故 $\dim B=\sum(2d_i-1)(g-1)=(g-1)\dim G=\frac12\dim M_H$；$\pi$ 满射，纤维维数也是 $\frac12\dim M_H$，即 eq (4.25)。 | $\dim B=\frac12\dim M_H$ 是可积性所需守恒量个数的来源；没有这个等式，$H_a$ 的数目不够。 | `B p.54 eq (4.25)` | A·原文明确写了 |
| 3 | 取 $H^1(C,T_C)$ 的一组基 $\alpha_a$（与 $H^0(C,K^2)$ 对偶），定义 eq (4.26)：$H_a=\int_C\alpha_a\wedge\mathrm{Tr}\,\varphi^2$；对一般 $G$ 把 $\mathrm{Tr}\,\varphi^2$ 换成 $P_i$。 | 这一步给出具体的守恒量；只抽象地说「取 Casimir」而不写积分，无法验证对易性。 | `B p.55 eq (4.26)` | A·原文明确写了 |
| 4 | 在 $W$ 上 $\Omega_I$ 使 $\varphi_z$ 与 $A_z$ 共轭而 $\varphi_z$ 与自己交换，$H_a$ 只依赖 $\varphi_z$，故彼此 Poisson 对易；限制到 $\nu_I=0$ 并商 $G_{\mathbb C}$ 后仍对易，于是得到 $\frac12\dim M_H$ 个独立对合量，生成 $I$-全纯对易流，轨道一般为复环面。 | 对易性若不能从 $W$ 下降到 $M_H$，就只是形式上的守恒量，不构成可积系统；这一步是全部论证的关键。 | `B p.55` | A·原文明确写了 |

## 结论

$\dim B=\frac12\dim M_H$ 给出足够的守恒量数目，$H_a$ 的对易性在超凯勒商后保持，故 $M_H$ 在 $I$ 中是复完全可积系统；一般纤维是对易流的轨道，为复环面，其显式构造可用谱覆盖。这是 §11 把 $M_H$ 当作 Hitchin 系统并在纤维上做 $T$-对偶的几何依据。

## 缺口

- 纤维是复环面在原文只用「一般情形可期望」并归引谱覆盖文献，未在本文内证明；完全可积性的细节也归引 Hitchin 1990。

## 最容易讲错的地方

- 把可积性当成实维数 $\frac12\dim$ 的 Liouville 可积：这里是复结构 $I$ 中的复完全可积，守恒量是 $I$-全纯函数。
- 混淆底的维数与纤维的维数：两者都等于 $\frac12\dim M_H$，但一个是底、一个是纤维。

## 相关卡

[Hitchin 纤维化](../concepts/hitchin-fibration.md) · [可积系统](../concepts/integrable-system.md) · [Hitchin 模空间](../concepts/hitchin-moduli.md) · [M_H 上的 sigma 模型数据与维数公式](../derivations/mh-sigma-data.md)

## 出处（印刷页）

- B p.53–55（B p.55 eq (4.26)）

> 说明：A4：eq (4.24)、eq (4.25)、eq (4.26) 与 Poisson 对易论证均在 `B p.53–55` 明写；最没把握处是纤维「一般为复环面」原文只用谱覆盖一句带过，未在本文证明。
