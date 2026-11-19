# 希钦纤维化

> `gtgl15/concept/hitchin-fibration` · 轨道 A · Hitchin 几何与谱曲线 · 状态 dev

> **先自测**：为什么以特征多项式为底的纤维化能成为完全可积系统的结构映射？

## 一句话

希钦纤维化 $\pi:\MH\to\mathcal V$ 把希格斯丛映到其特征多项式，是 $\MH$ 上的完全可积系统；一般纤维是复环面，维数恰为 $\MH$ 的一半。

## 定义

对 $SU(N)$，$\pi$ 把 $(E,\varphi)$ 送到 $w_n=\operatorname{Tr}\varphi^n\in H^0(C,K^n)$（$n=2,\dots,N$），$\mathcal V=\bigoplus_{n=2}^{N}H^0(C,K^n)$ 是仿射空间。对一般 $G$ 用 Casimir 不变量 $P_i(\varphi)$，$\mathcal V=\bigoplus_i H^0(C,K^{d_i})$，$d_i$ 是 Casimir 的次数。$\pi$ 的纤维由相同的特征多项式（即相同的谱曲线）刻画。

**记号**：$\pi$；$\mathcal V$；$w_n=\operatorname{Tr}\varphi^n$；$d_i$；$F=\pi^{-1}(v)$。

## 要点（为什么需要它）

1. $\mathcal V$ 是向量空间（仿射空间），$\dim\mathcal V=(g-1)\dim G=\frac12\dim_\mathbb{C}\MH$，这是完全可积性的维数条件。
2. $\pi$ 满射（Hitchin）：对 $SU(2)$ 这是 $3g-3$ 个方程、$3g-3$ 个未知数的一般解计数（$\S2.4$）。
3. 一般纤维 $F$ 是复环面（阿贝尔簇或 torsor）；在判别式轨迹上纤维奇异。
4. 纤维对 $\Omega_I$ Lagrangian：因为 $\Omega_I$ 在纤维方向限制为零，且纤维维数是 $\MH$ 的一半。
5. 对 $SU(N)$，纤维 $\cong\mathrm{Prym}(D/C)$ 类对象；对 $PSU(N)$，纤维是被 $\mathrm{Jac}(C)$ 商掉的版本（$\S2.6.6$）。

## 核心公式

$$
$$\pi:\MH\to\mathcal V,\qquad \mathcal V=\bigoplus_{n=2}^{N}H^0(C,K^n)$$$$\dim\mathcal V=(g-1)\dim G=\frac12\dim_\mathbb{C}\MH=\dim F$$
$$

$$
$$\dim\mathcal V=(g-1)\dim G=\frac12\dim_\mathbb{C}\MH=\dim F$$
$$

## 定理与证明（或缺口）

### $\pi$ 满射

每个特征多项式 $w=(w_2,\dots,w_N)$ 都来自某个稳定希格斯丛，故 $\pi$ 满射。

> 证明状态：**sketch**。原文 $\S2.4$ 只对 $SU(2)$ 给出一般解计数，一般 $G$ 引用 [13][21]。

出处：`A p.8`

## 常见误解

- $\mathcal V$ 是仿射空间，不是射影空间；不要给它装 Hodge 结构。
- 纤维在判别式上奇异：一般纤维是环面，奇异纤维不是。
- $\dim\mathcal V=\frac12\dim_\mathbb{C}\MH$；若换成实维数则 $\dim_\mathbb{R}\MH=2\dim_\mathbb{R}\mathcal V$，两种“一半”不要混用。
- 对 $PSU(N)$ 纤维不是阿贝尔簇而是 torsor（差一个 $\mathrm{Jac}(C)$），这影响对偶的陈述。

## 相关卡

[希钦模空间 $\MH$](../concepts/hitchin-moduli.md) · [完全可积性与对易哈密顿量](../concepts/integrable-system.md) · [谱曲线](../concepts/spectral-curve.md) · [阿贝尔化与 Prym 簇](../concepts/abelianization-prym.md) · [维数计数：$\sum(2d_i-1)=\dim G$](../derivations/dimension-count.md)

## 出处（印刷页）

- A p.7–8（A p.8 eq (2.6)）
- A p.10–11（A p.10 eq (2.9)）

> 说明：A=原文 $\S2.4$ 的纤维化定义与 eq (2.5)(2.6)；B=把“满射”拆成谱曲线＋阿贝尔化两步来陈述；C=维数一半的 Lagrangian 结论按 $\S2.5$ 推论补全。最没把握处：一般 $G$ 的 $\mathcal V$ 表达式原文只在 $\S2.4$ 提 Casimir 次数。
