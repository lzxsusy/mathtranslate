---
id: csw/concept/surgery-formula
type: concept
track: G
---

# 手术公式：沿环面切开-粘合

> 沿环面上的 $K$ 个 Wilson 线做手术，配分函数由 $S$ 矩阵与链环不变量给出：$Z_k(M)=S_{00}C^{\sigma(L)}\sum_\lambda S_{0\lambda}J$。

**问题**：为什么任意三维流形都能用手术从 $S^3$ 得到？手术公式为什么只依赖 $S$ 矩阵与链环？

## 定义

任一定向闭三维流形可由 $S^3$ 沿链环 $L$ 做 Dehn 手术得到（Lickorish–Wallace）。CS 的手术公式给出 $Z_k(M)$ 用 $S^3$ 上链环 $L$ 的 Wilson 线期望值表示：$Z_k(M)=\sum_\lambda S_{0\lambda}^{(1)}\cdots S_{0\lambda}^{(K)}\langle\prod_iW_{R_i}(K_i)\rangle_{S^3}$（带标架修正相位）。

*记号*：$K$ 是手术链环的分量数；$S_{0\lambda}$ 是真空到 $\lambda$ 的 S 矩阵元；$\sigma(L)$ 是标架修正相位。

## 要点

- 手术把“任意流形”化为“$S^3$ + 链环”，所以 CS 的计算归结为链环不变量。
- 公式的两种算法：先在 $S^3$ 算链环，再乘以 $S_{0\lambda}$ 求和；或先在挖空的流形上算，再粘合。
- 两种算法相等就是手术一致性；它给出 $S$ 矩阵的幺正性与 Verlinde 公式。
- 标架修正（扭转相位）来自 Wilson 线的标架与流形的标架。
- Verlinde 公式正是“$S^2\times S^1$ 手术到 $S^3$”的两算法对比。

## 关键公式

- $Z_k(M)=\sum_\lambda S_{0\lambda}\langle\prod W_{R_i}(K_i)\rangle_{S^3}$
- $Z_k(M)=\sum_\lambda S_{0\lambda}^{(1)}\cdots S_{0\lambda}^{(K)}\langle\cdots\rangle$

## 手术公式

沿链环 $L$ 做 Dehn 手术得到的流形 $M$ 的 CS 配分函数，等于 $S^3$ 上该链环的 Wilson 线期望值按 $S_{0\lambda}$ 加权求和（带标架相位），这与在挖空流形上量子化再粘合的结果一致。

**证明要点**（sketch）：

1. 在挖空的 $S^3$ 上，边界环面 $T^2$ 的态空间由 $S$ 矩阵基给出。 *（$\cH(T^2)$ 的基是 $|\lambda\rangle$，内积由 $S$ 给出。）*
2. 粘合映射 $\phi\in SL(2,\mathbb{Z})$ 作用在态空间上，给出 $\phi$ 的矩阵元。 *（$\operatorname{MCG}(T^2)=SL(2,\mathbb{Z})$。）*
3. 把链环的 Wilson 线插入并收缩，得 $\sum S_{0\lambda}\langle W\rangle$ 的形式。 *（收缩用了 $S$ 的幺正性。）*

> **缺口**：本文对一般手术的标架修正只给规则，未处理所有边界情形（p.391 留白）。

## 陷阱

- 不要漏掉标架相位：不同标架的链环期望值差一个 $e^{2\pi i\cdot(\text{标架})\cdot h_R}$ 因子。
- 手术链环的分量数与 $S$ 的指标要对齐，否则求和错位。
- Kirby 移动不改变流形，但改变链环表示；公式必须在 Kirby 移动下不变（这是 $S^2=(ST)^3$ 的来源）。

## 相关卡片

- [s-matrix](../concepts/s-matrix.md)
- [verlinde-formula](../concepts/verlinde-formula.md)
- [jones-from-cs](../concepts/jones-from-cs.md)
- [mapping-class-group](../concepts/mapping-class-group.md)

## 来源

- 威腾 1989，Commun. Math. Phys. 121 (1989) 351–399，§4.2–4.3（手术，原文 p.383–388），印刷页 [383, 388] / PDF 页 [33, 38]（witten1989/sections/s07-calculability-b.tex（§4.2））

---
*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*
