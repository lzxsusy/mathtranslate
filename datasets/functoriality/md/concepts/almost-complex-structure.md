# 殆复结构与相容性

> `functoriality/concept/almost-complex-structure` ｜ track A ｜ draft

**一句话**：殆复结构是切丛上满足 J²=-Id 的自同态；ω-相容性要求 ω(·,J·) 是黎曼度量，这类结构非空且空间可缩，用来定义条带方程。

**自测**：为什么 Floer 理论坚持用 ω-相容殆复结构，而不直接用复结构或任意黎曼度量？

## 定义

殆复结构是切丛的自同态 $J:TM\to TM$，满足 $J^2=-\Id$。给定辛形式 $\omega$，称 $J$ 与 $\omega$ 相容，若缩并 $\omega(\cdot,J\cdot)$ 在 $M$ 上定义一个黎曼度量（对称且正定）。所有 $\omega$-相容殆复结构构成空间 $\mathcal J(M,\omega)$；允许取时间依赖的族 $J_t$（$t\in[0,1]$），用于条带方程 $\partial_su+J_t(u)\partial_tu=0$。

记号：$\mathcal J(M,\omega)$ 可缩（McDuff–Salamon 命题 2.50(iii)）；$J_t$ 记时间依赖族，条带方向 $t\in[0,1]$、$s\in\R$。

## 要点

- 存在性：任何辛流形都带相容殆复结构（结构群可约化到 $U(n)$），故可把辛几何问题化为全纯曲线问题，无需 $M$ 是复流形。
- 可缩性使不变量与 $J$ 的选取无关：$\\mathcal J(M,\\omega)$ 可缩意味着沿参数取一条道路即可证明计数不随 $J$ 改变，这是 Floer 上同调良定义的关键一步。
- 相容性给出椭圆性与能量恒等式：$\\omega(\\cdot,J\\cdot)$ 是度量，配合 $J$-不变性可把能量写成辛面积，从而用能量控制模空间。
- 时间依赖 $J_t$ 不可省：条带在 $[0,1]$ 方向连接两个不同的拉格朗日边界条件，需要逐 $t$ 选取 $J_t$ 才能保证横截性。

## 公式

$J^2=-\Id$
$\omega(\cdot,J\cdot)$
$$\begin{gathered} \mathcal M(p_-,p_+;[v])\coloneqq\{u:\R\times[0,1]\to M\mid(*)\}/\R,\\ (*)\quad\coloneqq\quad u(s,0)\in L,\quad u(s,1)\in K,\quad\lim_{s\to\pm\infty}u(s,t)=p_{\mp},\\ \partial_su+J_t(u)\partial_tu=0,\quad[u]=[v], \end{gathered}$$

## 定理与证明

### 相容殆复结构空间可缩（McDuff–Salamon）

对任意辛流形 (M,ω)，ω-相容殆复结构之集非空且可缩。

（none；来源：原书 p.4–5 §2.1）


缺口：原文只引 McDuff–Salamon 命题 2.50(iii)（MS98），未给证明。

### Gromov 紧性

只要目标空间是辛的，从黎曼曲面到它的全纯映射模空间就具有自然的紧化。

（none；来源：原书 p.3 §1.1）


缺口：原文只引 [Gro85] 的结论，未展开紧化构造；紧化含球面与圆盘冒泡，是后续所有计数的基础。

## 易错点

- 把殆复当成复：$J$ 未必可积（Nijenhuis 张量可以非零），但 Gromov 理论只需要殆复结构与相容性。
- 以为相容性是冗余条件：$\\omega(\\cdot,J\\cdot)$ 必须正定；若只要求 $J^2=-\\Id$ 而不要求相容，能量恒等式失效，紧性论证无法进行。
- 忽略时间依赖：只取单个 $J$ 时，条带的横截性一般不能同时满足，模空间维数公式与计数都会出错。

## 参考与关联

- Abouzaid & Bottman, Functoriality in categorical symplectic geometry (arXiv:2210.11159v1)，§2.1，p.5–6（原书 p.5–6 §2.1）

关联：`functoriality/concept/symplectic-manifold`、`functoriality/concept/pseudoholomorphic-curve`、`functoriality/deriv/floer-d-squared`

来源说明：原书 p.4–6 §2.1（ω-相容殆复结构的定义、空间可缩性、条带方程 eq:12）；公式 $J^2=\Id$ 与 $\omega(\cdot,J\cdot)$ 取自 chapter2.tex 的定义条款。
