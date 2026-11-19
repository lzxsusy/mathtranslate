# 维数计数：$\sum(2d_i-1)=\dim G$

> `gtgl15/deriv/dimension-count` · 轨道 A · Hitchin 几何与谱曲线 · 状态 dev · 4 步

> **要回答的问题**：为什么 Hitchin 底空间 $\mathcal V$ 的维数恰好是 $\MH$ 复维数的一半，而这又恰好等于一般纤维的维数？

## 一句话

由 $\dim H^0(C,K^d)=(2d-1)(g-1)$ 与 Casimir 次数和 $\sum_i(2d_i-1)=\dim G$，得 $\dim\mathcal V=(g-1)\dim G=\frac12\dim_\mathbb{C}\MH=\dim F$。

## 目标

计算 $\dim\mathcal V$、$\dim_\mathbb{C}\MH$ 与一般纤维 $F$ 的维数，并验证三者的关系。

## 前提

- $\mathcal V=\bigoplus_i H^0(C,K^{d_i})$，$d_i$ 是 $G$ 的 Casimir 不变量次数（$SU(N)$ 时 $d_i=i$，$i=2,\dots,N$）。
- Riemann–Roch：$\dim H^0(C,K^d)=(2d-1)(g-1)$（$d\ge1$，$g\ge2$）。
- $\dim_\mathbb{C}\MH=2\dim\mathcal V$（超凯勒流形的复维数等于底空间维数的两倍，因为一般纤维是复环面且 $\dim F=\dim\mathcal V$）。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | $\dim H^0(C,K^{d_i})=(2d_i-1)(g-1)$，故 $\dim\mathcal V=(g-1)\sum_i(2d_i-1)$。 | $\mathcal V$ 是直和，逐项用 Riemann–Roch。 | `A p.8 eq (2.5)` | A·原文明确写了 |
| 2 | Casimir 不变量次数满足 $\sum_i(2d_i-1)=\dim G$（例如 $SU(N)$：$\sum_{i=2}^{N}(2i-1)=N^2-1$）。 | 这是半单李代数的标准恒等式。 | `A p.8` | A·原文明确写了 |
| 3 | 代入得 $\dim\mathcal V=(g-1)\dim G$。 | 合并前两步。 | `A p.8 eq (2.6)` | A·原文明确写了 |
| 4 | $\MH$ 的超凯勒结构给 $\dim_\mathbb{C}\MH=2\dim\mathcal V$；一般纤维 $F=\pi^{-1}(v)$ 的复维数也为 $\dim\mathcal V$，因为 $\pi$ 满射且 $\mathcal V$ 是仿射空间（$\dim F=\dim_\mathbb{C}\MH-\dim\mathcal V=\dim\mathcal V$）。 | 这解释了“完全可积”：纤维恰好是一半维数。 | `A p.8 eq (2.6)` | A·原文明确写了 |

## 结论

$\dim\mathcal V=(g-1)\dim G=\frac12\dim_\mathbb{C}\MH=\dim F$；$SU(N)$ 时是 $(N^2-1)(g-1)$。

## 缺口

- 第 4 步“纤维维数 = $\dim\mathcal V$”用到了 $\pi$ 满射，而满射的完整证明原文对一般 $G$ 引用 [13][21]。

## 最容易讲错的地方

- $\sum(2d_i-1)=\dim G$ 的 $d_i$ 是 Casimir 次数（$SU(N)$ 的 $d_i=i$），不是指数/对偶 Coxeter 数。
- $\dim H^0(C,K^d)=(2d-1)(g-1)$ 只对 $d\ge1$ 成立；$d=1$ 给 $g-1=\dim H^0(C,K)$。
- $\dim_\mathbb{C}\MH$ 是复维数；写成实维数要乘 2，别和 $\dim\mathcal V$ 混。

## 相关卡

[希钦纤维化](../concepts/hitchin-fibration.md) · [完全可积性与对易哈密顿量](../concepts/integrable-system.md) · [希钦模空间 $\MH$](../concepts/hitchin-moduli.md) · [谱曲线](../concepts/spectral-curve.md) · [谱曲线亏格与分歧点计数](../derivations/spectral-genus.md)

## 出处（印刷页）

- A p.8（A p.8 eq (2.5)）
- A p.8（A p.8 eq (2.6)）

> 说明：A4：eq (2.5)(2.6) 与 Casimir 次数和均在 §2.4 明写；B=第 4 步把满射与纤维维数连起来陈述。最没把握处：$\pi$ 满射的一般 $G$ 证明原文只有引用。
