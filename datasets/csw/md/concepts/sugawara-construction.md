---
id: csw/concept/sugawara-construction
type: concept
track: E
---

# Sugawara 构造与中心荷

> $T(z)=\frac1{2(k+h^\vee)}\sum_a:J^aJ^a:$ 给出 Virasoro 代数，中心荷 $c=k\dim G/(k+h^\vee)$。

**问题**：为什么分母是 $k+h^\vee$ 而不是 $k$？$h^\vee$ 从哪里来？

## 定义

设 $J^a(z)$ 是 level $k$ 的仿射流。定义 $T(z)=\frac{1}{2(k+h^\vee)}\sum_a{:}J^a(z)J^a(z){:}$（正规序）。则 $T$ 满足 Virasoro 代数，中心荷 $c=k\dim G/(k+h^\vee)$，且 $J^a$ 是权 $1$ 的初级场。

*记号*：$h^\vee$ 是对偶 Coxeter 数（$SU(N)$ 为 $N$，$SU(2)$ 为 2）；$k+h^\vee$ 是有效 level。

## 要点

- 经典 Sugawara 是 $T\propto\sum J^aJ^a$；量子化时双收缩产生额外项，把 $k$ 修正为 $k+h^\vee$。
- $h^\vee$ 来自双收缩的一次收缩：$\sum_a f^{abc}f^{abd}=h^\vee\delta^{cd}$（适当归一化）。
- 中心荷 $c=k\dim G/(k+h^\vee)$ 在 $k\to\infty$ 时趋于 $\dim G$（半经典极限）。
- Virasoro 的中心荷与 CS 的标架反常是同一件事：$c$ 出现在标架相位 $e^{2\pi i(n-m)c/24}$ 里。
- 表示的最高权 $h_\lambda=(\lambda,\lambda+2\rho)/(2(k+h^\vee))$，$\lambda$ 是可积最高权。

## 关键公式

- $T(z)=\frac1{2(k+h^\vee)}\sum_a{:}J^aJ^a{:}$
- $c=\frac{k\dim G}{k+h^\vee}$
- $h_\lambda=\frac{(\lambda,\lambda+2\rho)}{2(k+h^\vee)}$

## Sugawara 公式

由 level $k$ 的仿射流按上式构造的 $T(z)$ 满足 Virasoro 代数，中心荷 $c=k\dim G/(k+h^\vee)$，且流的共形权为 1。

**证明要点**（sketch）：

1. 计算 $T(z)T(w)$ 的 OPE：四流项用 Wick 收缩，双收缩给出 $k$ 与 $h^\vee$ 的组合。 *（双收缩 $\sum_a:J^aJ^a:$ 的系数来自 $f^{abc}f^{abd}=h^\vee\delta^{cd}$。）*
2. 要求 $T$ 的 OPE 形状为标准 Virasoro，解出归一化 $1/(2(k+h^\vee))$。 *（归一化由 $T$ 的 $1/(z-w)^4$ 系数（即 $c/2$）确定。）*
3. 故 $c=k\dim G/(k+h^\vee)$。 *（把 $k$ 换成 $k+h^\vee$ 的修正来自双收缩。）*

> **缺口**：本文不推导 Sugawara，只在 §2 用 $c$ 的公式（(2.25)）；细节见教材。

## 陷阱

- 分母写成 $k$ 是错的：会丢掉 $h^\vee$，$k=1$ 时甚至给出 $c=\dim G$ 而不是 $\dim G/(1+h^\vee)$。
- $h_\lambda$ 公式里的 $\lambda+2\rho$ 常被误写成 $\lambda+\rho$；展开 $(\lambda,\lambda)+2(\lambda,\rho)$。
- 有效 level $k+h^\vee$ 与截断用的 $k$ 是两个不同的 $k$，别混。

## 相关卡片

- [affine-lie-algebra](../concepts/affine-lie-algebra.md)
- [conformal-blocks](../concepts/conformal-blocks.md)
- [half-form-correction](../concepts/half-form-correction.md)

## 来源

- 威腾 1989，Commun. Math. Phys. 121 (1989) 351–399，§2（(2.25) 的 c）与 §4 (4.21)，印刷页 [361, 382] / PDF 页 [11, 32]（witten1989/sections/s02-weak-coupling.tex（(2.25)））

---
*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*
