---
id: csw/concept/verlinde-formula
type: concept
track: G
---

# Verlinde 公式

> $N_{ijk}=\sum_l\frac{S_{il}S_{jl}S_{kl}}{S_{0l}}$：融合系数 = 三点共形块维数 = $S$ 矩阵的组合。

**问题**：为什么三点函数的维数能用 $S$ 矩阵算出来？这个公式在 CS 里怎么“物理推导”？

## 定义

对可积表示 $i,j,k$，融合系数 $N_{ijk}$（三点共形块维数）由 Verlinde 公式给出：$N_{ijk}=\sum_l\frac{S_{il}S_{jl}S_{kl}}{S_{0l}}$。等价地，Verlinde 代数 $v_iv_j=\sum_kN_{ij}^kv_k$ 在基 $w_i=S_{0i}\sum_mS_i^mv_m$ 下变成 $w_iw_j=\delta_{ij}w_j$（幂等元）。

*记号*：$S$ 是模 S 矩阵；$N_{ijk}=\dim\mathcal{H}(S^2;R_i,R_j,R_k)$。

## 要点

- 这是“融合 = 模变换”的定量形式：$S$ 的行是融合矩阵的共同特征向量。
- 在 CS 里它由手术一致性推出（$S^2\times S^1$ 的两种算法）。
- 在 WZW 里它是定理（TUY 1989、Faltings 1994）；在 CS 里 Witten 给物理推导。
- $N_{ijk}$ 是非负整数，公式给的是整数（非平凡事实）。
- 它是“可计算性”的核心：$S^3$ 配分函数、手术不变量都归结为 $S$。

## 关键公式

- $N_{ijk}=\sum_l\frac{S_{il}S_{jl}S_{kl}}{S_{0l}}$
- $v_iv_j=\sum_kN_{ij}^kv_k$
- $w_i=S_{0i}\sum_mS_i^mv_m,\ w_iw_j=\delta_{ij}w_j$

## Verlinde 公式（CS 版本）

在 CS 中，$S^2$ 上三点函数的维数 $N_{ijk}$ 由 $S$ 矩阵给出：$N_{ijk}=\sum_lS_{il}S_{jl}S_{kl}/S_{0l}$；等价地，融合代数被 $S$ 对角化。

**证明要点**（sketch）：

1. 在 $S^2\times S^1$ 上沿一个 $S^1$ 做手术，得到 $S^3$ 上的链环。 *（$S^2\times S^1$ 的边界环面被手术。）*
2. 两种算法（先手术 vs 先在 $S^2\times S^1$ 上算）给出等式 $\sum_kS_i{}^kN_{kl}{}^m=S_{il}S_i{}^m/S_{0i}$。 *（这是 Witten (4.51) 的推导。）*
3. 该等式即 $S$ 对角化融合矩阵，写成特征值形式即 Verlinde 公式。 *（线性代数改写。）*

> **缺口**：Witten 的推导依赖手术与量子化的自洽性；严格证明见 TUY 1989 与 Faltings 1994。

## 陷阱

- 求和只对可积表示；否则发散。
- $N_{ijk}$ 对称但公式里的 $S$ 不是对称指标：$S$ 对称矩阵，但 $N$ 是三重对称张量。
- 归一化：$S_{0l}$ 与 $S$ 的整体归一化绑定，换书要重算。

## 相关卡片

- [fusion-rules](../concepts/fusion-rules.md)
- [s-matrix](../concepts/s-matrix.md)
- [surgery-formula](../concepts/surgery-formula.md)
- [conformal-blocks](../concepts/conformal-blocks.md)

## 来源

- 威腾 1989，Commun. Math. Phys. 121 (1989) 351–399，§3.4（(3.6)）与 §4.5（(4.51)），印刷页 [374, 393] / PDF 页 [24, 43]（witten1989/sections/s08-calculability-c.tex（§4.5））

---
*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*
