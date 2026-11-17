---
id: csw/concept/s-matrix
type: concept
track: G
---

# 模 S 矩阵与 T 矩阵

> $S$ 与 $T$ 是 $SL(2,\mathbb{Z})$ 在共形块空间上的表示；$T$ 对角，$S$ 由正弦公式给出（$SU(2)$）。

**问题**：$S$ 矩阵为什么是模变换？它的矩阵元为什么正好是正弦函数？

## 定义

环面 $T^2$ 的模群 $SL(2,\mathbb{Z})$ 由 $S:\tau\mapsto-1/\tau$ 与 $T:\tau\mapsto\tau+1$ 生成，作用在环面共形块空间 $\mathcal{H}(T^2)$ 上。$T$ 对角（相位 $e^{2\pi i(h_j-c/24)}$），$S$ 是“傅里叶变换”。对 $SU(2)_k$，$S_{jl}=\sqrt{\frac{2}{k+2}}\sin\frac{\pi(2j+1)(2l+1)}{k+2}$，$j,l=0,\frac12,\dots,\frac k2$。

*记号*：$j,l$ 标可积表示；$c=k\dim G/(k+h^\vee)$；$S^2=(ST)^3=C$。

## 要点

- $S$ 是模变换 $\tau\to-1/\tau$ 的表示矩阵；它是幺正且对称的。
- 模关系 $S^2=(ST)^3=C$（$C$ 是电荷共轭）是 $SL(2,\mathbb{Z})$ 的呈现。
- $T$ 的相位含 $-c/24$：这是标架反常的模块化形式。
- $S$ 的矩阵元给出融合系数（Verlinde）与 $S^3$ 配分函数（$Z(S^3)=S_{00}$）。
- 正弦形式来自 $SU(2)$ 的特征标（Weyl 特征标公式在 $A_1$ 的情形）。

## 关键公式

- $S_{jl}=\sqrt{\frac{2}{k+2}}\sin\frac{\pi(2j+1)(2l+1)}{k+2}$
- $T_{jj}=e^{2\pi i(h_j-c/24)}$
- $S^2=(ST)^3=C$

## SU(2) 的 S 矩阵

对 $SU(2)_k$，$S_{jl}=\sqrt{\frac{2}{k+2}}\sin\frac{\pi(2j+1)(2l+1)}{k+2}$ 满足 $S^2=(ST)^3=C$，其中 $T=\mathrm{diag}(e^{2\pi i(h_j-c/24)})$。

**证明**：

1. $SU(2)_k$ 的特征标在 $S$ 变换下由 Weyl 特征标公式给出。 *（$\chi_j(-1/\tau)=\sum_lS_{jl}\chi_l(\tau)$。）*
2. $A_1$ 的 Weyl 特征标是正弦之比，化简得正弦公式。 *（$\chi_j(\tau)=\frac{\sin(\pi(2j+1)z/\ldots)}{\sin(\pi z/\ldots)}$，在 $z$ 的特殊值取极限。）*
3. 直接验证 $S^2=(ST)^3=C$ 与 $C_{jl}=\delta_{j,\bar l}$。 *（有限矩阵，可逐项验算。）*

## 陷阱

- 归一化：$\sqrt{2/(k+2)}$ 与 $\sqrt{2/(k+h^\vee)}$ 在 $SU(2)$ 是同一个，但一般群要换成 $k+h^\vee$。
- $T$ 的相位约定（是否含 $-c/24$）影响 $S^2=(ST)^3$ 的验证：取拓扑自旋 $T=\mathrm{diag}(e^{2\pi ih_j})$ 时 $(ST)^3=e^{2\pi ic/8}$。
- $S$ 的指标是可积表示（$j\le k/2$），不是所有 $j$。

## 相关卡片

- [verlinde-formula](../concepts/verlinde-formula.md)
- [surgery-formula](../concepts/surgery-formula.md)
- [mapping-class-group](../concepts/mapping-class-group.md)
- [su2-k2-s-matrix](../examples/su2-k2-s-matrix.md)

## 来源

- 威腾 1989，Commun. Math. Phys. 121 (1989) 351–399，§3.4（(3.6)）与 §4（(4.21)），印刷页 [374, 382] / PDF 页 [24, 32]（witten1989/sections/s04-canonical.tex（§3.4））

---
*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*
