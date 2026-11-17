---
id: csw/concept/borel-weil-bott
type: concept
track: D
---

# Borel–Weil–Bott 与表示的几何化

> 不可约表示 $R_\lambda$ 等于旗流形 $G/T$ 上全纯线丛的全纯截面空间（$\lambda$ 支配整）。

**问题**：$G/T$ 上的全纯截面为什么正好给出表示 $R_\lambda$？这里为什么 $\lambda$ 不加 $\rho$？

## 定义

设 $G$ 紧连通单群，$T$ 极大环面，$G/T$ 旗流形（复结构由正根决定）。对支配整权 $\lambda$，取 $G/T$ 上辛形式 $\omega_\lambda$（其 de Rham 类为 $\lambda$）与预量子化线丛 $\mathcal{L}_\lambda$。Borel–Weil–Bott 定理：$H^0(G/T,\mathcal{L}_\lambda)=R_\lambda$（最高权 $\lambda$ 的不可约表示），其它上同调为零。

*记号*：$\lambda$ 是最高权；$\rho$ 是 Weyl 向量（正根和的一半）；$\mathcal{L}_\lambda=G\times_T\mathbb{C}_\lambda$。

## 要点

- 表示论被翻译成复几何：$R_\lambda$ 是某个线丛的全纯截面空间。
- 指标是 $\lambda$ 而不是 $\lambda+\rho$：$\mathcal{L}_\lambda=G\times_T\mathbb{C}_\lambda$，权重直接是 $\lambda$。
- $\rho$ 出现在半形式修正里：$K_{G/T}^{1/2}=\mathcal{L}_{-\rho}$，所以“带半形式的量子化”给出 $\lambda+\rho$ 的指标。
- Witten 用它把 Wilson 线的表示“量子化”：把 $R_s$ 换成 $G/T$ 上一层几何量子化数据，从而把穿刺点约束变成经典可解的约束。
- 可积性（$2j\le k$ 等）不是 BWB 的推论，而来自仿射代数（见 integrable-representation 卡）。

## 关键公式

- $H^0(G/T,\mathcal{L}_\lambda)=R_\lambda$
- $K_{G/T}^{1/2}=\mathcal{L}_{-\rho}$
- $\dim R_\lambda=\prod_{\alpha>0}\frac{(\lambda+\rho,\alpha)}{(\rho,\alpha)}$

## Borel–Weil–Bott

对支配整权 $\lambda$，$H^0(G/T,\mathcal{L}_\lambda)\cong R_\lambda$，且 $H^q(G/T,\mathcal{L}_\lambda)=0$（$q>0$）；若 $\lambda+\rho$ 落在 Weyl 壁另一侧，则上同调只在某个 $q$ 次非零，给出相应的对偶表示。

**证明要点**（sketch）：

1. $G/T$ 上的全纯线丛由 $T$ 的特征 $\lambda$ 分类。 *（线丛的转移函数是 $T$-值上闭链。）*
2. 对支配整 $\lambda$，$H^0$ 的维数由 Weyl 维数公式给出，且 $G$ 作用不可约。 *（这是 BWB 的标准证明（用 Weyl 群与上同调消没）。）*
3. 一般 $\lambda$ 时，非零上同调出现在 $q=\ell(w)$（$w$ 使 $w(\lambda+\rho)$ 支配整）。 *（这就是“Bott”部分：上同调的跳变。）*

> **缺口**：本文只引用 BWB 的结论（$H^0=R_\lambda$），不证明；一般 $\lambda$ 的 Bott 部分本文不用。

## 陷阱

- 不要写 $\lambda+\rho$ 当指标：$\mathcal{L}_\lambda$ 的权重是 $\lambda$，$\rho$ 属于 $K^{1/2}$。
- BWB 给的是全纯截面，不是“所有截面”；全纯性由复结构决定。
- 可积性 $2j\le k$ 不来自 BWB，而来自仿射代数的表示论。

## 相关卡片

- [puncture-gauss-law](../concepts/puncture-gauss-law.md)
- [flag-orbit-symplectic](../concepts/flag-orbit-symplectic.md)
- [integrable-representation](../concepts/integrable-representation.md)

## 来源

- 威腾 1989，Commun. Math. Phys. 121 (1989) 351–399，§3.3（用 BWB 把表示量子化），印刷页 [371, 372] / PDF 页 [21, 22]（witten1989/sections/s05-hilbert.tex（§3.3））

---
*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*
