---
id: csw/concept/fusion-rules
type: concept
track: E
---

# 融合规则与 Verlinde 公式

> 融合规则 $R_i\otimes R_j=\bigoplus_kN_{ij}^kR_k$ 的系数由 $S$ 矩阵给出：$N_{ij}^k=\sum_l\frac{S_{il}S_{jl}S_{kl}}{S_{0l}}$。

**问题**：融合系数为什么可以用 $S$ 矩阵“对角化”？这个公式的物理意义是什么？

## 定义

对可积表示 $R_i$，融合规则 $R_i\otimes R_j=\bigoplus_kN_{ij}^kR_k$ 定义非负整数 $N_{ij}^k$。Verlinde 公式：$N_{ij}^k=\sum_l\frac{S_{il}S_{jl}S_{kl}}{S_{0l}}$，其中 $S$ 是模 S 矩阵（$S^2=(ST)^3=C$）。等价地，Verlinde 代数 $v_iv_j=\sum_kN_{ij}^kv_k$ 在基 $w_i=S_{0i}\sum_mS_i^mv_m$ 下对角化。

*记号*：$S_{ij}$ 是模 S 矩阵；$N_{ij}^k$ 是融合系数；下标 $0$ 是真空。

## 要点

- 融合系数是 S² 上三点函数的维数：$N_{ij}^k=\dim\mathcal{H}(S^2;R_i,R_j,R_k)$。
- Verlinde 公式把“融合”（代数）与“模变换”（几何）联系起来。
- 它给出 CS 中 $S^3$ 配分函数与手术公式的闭合形式，是“可计算性”的核心。
- 公式在 WZW 里是定理（TUY、Faltings），在 CS 里是“物理推导 + 数学证明”。
- 截断（可积性）让求和有限，否则公式发散。

## 关键公式

- $R_i\otimes R_j=\bigoplus_kN_{ij}^kR_k$
- $N_{ij}^k=\sum_l\frac{S_{il}S_{jl}S_{kl}}{S_{0l}}$
- $v_iv_j=\sum_kN_{ij}^kv_k$

## Verlinde 公式

对可积表示，融合系数由 $N_{ij}^k=\sum_lS_{il}S_{jl}S_{kl}/S_{0l}$ 给出；等价地，Verlinde 代数在对角基下是幂等的。

**证明要点**（sketch）：

1. 在 $S^2\times S^1$ 上做手术，把 $\Sigma$ 换成 $S^3$，用两种方式算配分函数。 *（这是 Witten §4.5 的路线。）*
2. 手术关系给出 $\sum_kS_i{}^kN_{kl}{}^m=S_{il}S_i{}^m/S_{0i}$，即 $S$ 对角化融合矩阵。 *（两种算法相等给出该关系。）*
3. 把该关系写成特征值形式即 Verlinde 公式。 *（$S$ 的行是融合矩阵的共同特征向量。）*

> **缺口**：Witten 的推导是物理的（依赖手术与量子化自洽性）；严格数学证明由 TUY/Faltings 给出。

## 陷阱

- 不要把 $S$ 与融合矩阵 $N$ 混淆：$S$ 是模变换矩阵，$N$ 是融合系数张量。
- 公式里的求和必须只对可积表示；否则不收敛。
- 归一化：$S_{0l}$ 的分母与 $S$ 的归一化绑定，换约定要整体改。

## 相关卡片

- [s-matrix](../concepts/s-matrix.md)
- [verlinde-formula](../concepts/verlinde-formula.md)
- [conformal-blocks](../concepts/conformal-blocks.md)
- [su2-k2-s-matrix](../examples/su2-k2-s-matrix.md)

## 来源

- 威腾 1989，Commun. Math. Phys. 121 (1989) 351–399，§3.4（(3.6)）与 §4.5（(4.51)），印刷页 [374, 393] / PDF 页 [24, 43]（witten1989/sections/s05-hilbert.tex（§3.4）与 s08-calculability-c.tex（§4.5））

---
*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*
