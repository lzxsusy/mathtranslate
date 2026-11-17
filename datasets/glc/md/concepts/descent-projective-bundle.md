---
id: glc/concept/descent-projective-bundle
type: concept
track: E
---

# 沿射影丛纤维下降局部系统

> 把 $\operatorname{Aut}'_E$ 认成局部系统后，因纤维 $\mathbb P^m$ 且 $\pi_1(\mathbb P^m_{\bar k})=1$，它沿 $p_V$ 唯一下降；关键是证 IC 延拓是局部系统。

**问题**：为什么把一个 IC 层认成局部系统之后，沿射影丛型映射的下降就变成唯一且自动的？

## 定义

在光滑开图 $V\subset C_n^\circ\cap\operatorname{Bun}_n^d$ 上工作。必要时缩小 $V$ 后，截面 $\Omega_X^{n-1}\to M$ 的空间是 $V$ 上的向量丛；再对截面上的标量作用取商，得到射影丛型映射 $p_V:V'\to V$。下降的图景是：先将 $\operatorname{Aut}'_E|_{V'}$ 写成 $V'$ 的某个稠密开部分上局部系统的 IC 延拓，再证明这个 IC 延拓实际上是整个 $V'$ 上的局部系统。使用两个条件：(i) 对每个几何点 $m\in V$，良好开部分与纤维的交是稠密的，即 $V'\cap p_V^{-1}(m)\subset p_V^{-1}(m)$ 是开且稠密的（可纳入良好开部分的定义）；(ii) $\operatorname{Aut}'_E|_{V'}$ 必须是局部系统，而不只是 IC 层。知道 (ii) 后，局部系统沿 $p_V$ 唯一下降，因为几何纤维是射影空间，且 $\pi_1(\mathbb P^m_{\bar k})=1$；等价地，从 $V$ 上局部系统到 $V'$ 上局部系统的拉回函子是等价。

*记号*：$V\subset C_n^\circ\cap\operatorname{Bun}_n^d$ 是光滑开图；$V'$ 是『丛 $M$ 带上非零截面』的模空间对截面标量取商后的叠；$p_V$ 是射影丛型映射；$m\in V$ 是几何点，$p_V^{-1}(m)$ 是纤维。

## 要点

- 条件 (i) 保证 IC 延拓所依赖的『稠密开部分』在每个纤维里确实稠密，从而延拓的边界不会吃掉整个纤维。
- 条件 (ii) 是真正的分水岭：只有 IC 时无法下降，必须是局部系统；而 §8.3 的 Euler 示性数判据正是用来把 IC 升级成局部系统的。
- 下降的唯一性来自 $\pi_1(\mathbb P^m_{\bar k})=1$：射影空间单连通，纤维方向没有单值群可容纳，故局部系统沿纤维不变当且仅当它来自底空间。
- 等价说法：拉回函子 $\{\text{$V$ 上局部系统}\}\to\{\text{$V'$ 上沿纤维不变的局部系统}\}$ 是范畴等价。
- 这一步给出从 $C_n^{\prime,\circ}$ 到 $C_n^\circ$ 的整体下降：$V$ 上的结论由光滑开图的覆盖拼起来。

## 关键公式

- $p_V:V'\longrightarrow V$
- $V'\cap p_V^{-1}(m)\subset p_V^{-1}(m)\quad\text{开且稠密}$
- $\pi_1(\mathbb P^m_{\bar k})=1$

## 定理与证明

### 局部系统沿射影丛纤维的唯一性下降（完整）

设 $p_V:V'\to V$ 如上，几何纤维为射影空间 $\mathbb P^m_{\bar k}$，且 (i) 良好开部分与每个纤维的交开稠密、(ii) $\operatorname{Aut}'_E|_{V'}$ 是局部系统。则 $\operatorname{Aut}'_E|_{V'}$ 沿 $p_V$ 唯一地下沉为 $V$ 上的局部系统。

1. 由 (i)，$V'$ 的稠密开部分在每个纤维中稠密，故在那里取的 IC 延拓其边界不吞掉任何整个纤维；再由 (ii)，这个延拓其实是整个 $V'$ 上的局部系统。  
   *为什么*：IC 延拓只可能在边界上偏离原来的局部系统；纤维中稠密使边界不能整块出现，而 (ii) 又直接排除了偏离。
2. 于是问题化为：沿 $p_V$ 下降一个局部系统。$p_V$ 的几何纤维是 $\mathbb P^m_{\bar k}$，而 $\pi_1(\mathbb P^m_{\bar k})=1$。  
   *为什么*：射影空间单连通，沿纤维的局部系统必为常值，故局部系统在纤维上没有单值信息。
3. 因此从 $V$ 上局部系统到 $V'$ 上局部系统的拉回函子是等价，特别地是全忠实且本质满的：$\operatorname{Aut}'_E|_{V'}$ 有唯一的下降对象。  
   *为什么*：单连通纤维使『沿纤维不变』成为自动条件，拉回的逆就是取纤维上的常值部分，两者互逆。

*出处*：§8.2 / 原书 p.44–45


## 易错点

- 若 $p_V$ 是向量丛而非射影丛（即忘记对截面标量取商），纤维带 $\mathbb G_m$ 作用，$\pi_1$ 不再平凡，下降不唯一。
- $p_V$ 被称为『射影丛型』而不是射影丛：它只是纤维为射影空间，不必整体是射影丛。
- $\pi_1(\mathbb P^m_{\bar k})=1$ 只在 $\bar k$ 上成立；用 $k$-结构或实结构会引入额外的单值群。
- 条件 (ii) 不能由 (i) 或 IC 性质推出，必须另行证明（这正是 §8.3 的全部内容）。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§8.2 沿射影丛纤维下降，p.44-45（PDF p.44-45），`源码/chapters/ch08.tex:22-31（$p_V$、两个条件与 $\pi_1(\mathbb P^m_{\bar k})=1$）`

## 核验

状态：`source-only`（2026-11-18）
- 课程讲义（标准拓扑事实）：https://www.math.ucr.edu/~res/math246A-2012/projspaces1b.pdf — 「Theorem 1. For all $n\ge1$ the fundamental group of $\mathbb{CP}^n$ is trivial.」支持卡里核心事实 $\pi_1(\mathbb P^m_{\bar k})=1$（复拓扑；光滑射影空间的 étale 基本群同样平凡）；据此射影空间纤维上的局部系统必为常值，沿 $p_V$ 的下降唯一。
- nLab：https://ncatlab.org/nlab/show/local+system — 页面称局部系统「often this is presented or taken to be presented by a locally constant sheaf」，并指出「local systems on $X$ correspond to functors out of the fundamental groupoid of $X$」。支持卡里把「局部系统沿纤维常值 $\Rightarrow$ 沿 $p_V$ 下降」化为 $\pi_1$ 陈述；页面没有射影丛纤维化上的具体下降命题。

## 关联

- `glc/concept/aut-e-whittaker-laumon`
- `glc/concept/euler-characteristic-trace-test`
- `glc/concept/deligne-trace-constancy`
