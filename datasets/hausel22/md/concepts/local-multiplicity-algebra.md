# 局部重数代数 $Q_\calE$

> `hausel22/concept/local-multiplicity-algebra` · 轨道 D · 幂零锥上的等变重数 · 状态 dev

> **先自测**：为什么把 $Q_\calE$ 叫作「重数」代数？

## 一句话

$Q_\calE$ 是上行流与幂零锥概形论交的坐标环，分次、有限维、Gorenstein 且满足 Poincaré 对偶。

## 定义

对 $\calE\in\M^{s\T}$ 定义局部重数代数 $Q_\calE:=\C[W^+_\calE]/(h_1,\dots,h_N)=\C[W^+_\calE]/(h_\calE^{-1}(\mathfrak m_0))$，其中 $h_1,\dots,h_N$ 是 Hitchin 映射的分量、$\mathfrak m_0$ 是 $0\in\calA$ 的极大理想。它是 $W^+_\calE\cap h^{-1}(0)$ 的坐标环，带 $\T$-分次。定理 3.9：$Q_\calE$ 有限维、分次、Gorenstein、满足 Poincaré 对偶，且其 Poincaré 多项式等于 $m_\calE(t)$。

**记号**：$Q_\calE$；$h_1,\dots,h_N$；$\mathfrak m_0$；socle $J_{h_\calE}$；Poincaré 多项式。

## 要点（为什么需要它）

1. 它是「$W^+_\calE$ 与幂零锥的概形论交」的环：不只是集合交，还带重数结构（这正是名字的来源）。
2. Gorenstein 性给出 socle $Q^m_\calE\cong\C J_{h_\calE}$，从而有 Poincaré 对偶 $Q^k\times Q^{m-k}\to\C$——这是「Artin 代数」里的强条件。
3. Poincaré 多项式等于 $m_\calE(t)$，这就是定理 3.5 与定理 3.9 的接口：代数的不变量等于几何的多项式。
4. 定理 3.10：当 $\delta_1+\cdots+\delta_{n-1}$ 既约时，$Q_\delta\cong\prod_{i=1}^{n-1}H^*(\Gr(i,n);\C)^{m_i}$，把重数代数算成了 Grassmann 上同调环的乘积。

## 核心公式

$$
$$Q_\calE:=\C[W^+_\calE]/(h_1,\dots,h_N)=\C[W^+_\calE]/(h_\calE^{-1}(\mathfrak m_0))$$$$\sum_k\dim(Q^k_\calE)\,t^k=m_\calE(t),\qquad Q^m_\calE\cong\C J_{h_\calE}$$
$$

$$
$$\sum_k\dim(Q^k_\calE)\,t^k=m_\calE(t),\qquad Q^m_\calE\cong\C J_{h_\calE}$$
$$

## 定理与证明（或缺口）

### 重数代数的五条性质（定理 3.9）

$Q_\calE$ 满足：(1) 有限维；(2) 分次且 $Q^0\cong\C$；(3) Gorenstein，socle $Q^m_\calE\cong\C J_{h_\calE}$；(4) Poincaré 对偶 $Q^k\times Q^{m-k}\to\C$；(5) Poincaré 多项式 $\sum\dim(Q^k)t^k=m_\calE(t)$。

> 证明状态：**sketch**。原文只引 Arnold 学派与 [HH1]，未给逐条证明。

出处：`A p.2239`

### Hecke 情形下的乘积公式（定理 3.10）

若 $\delta_1+\cdots+\delta_{n-1}$ 既约，则 $Q_\delta\cong\prod_{i=1}^{n-1}H^*(\Gr(i,n);\C)^{m_i}$。

> 证明状态：**sketch**。原文引用 [HH, Thm 4.16/(5.18)]，未给证明。

出处：`A p.2240`

## 常见误解

- $Q_\calE$ 是「概形论交」的环，不是集合交的函数环；丢了重数结构就丢了 $m_\calE(t)$ 的信息。
- Gorenstein 不是「正则」：它允许奇点，只要求 socle 一维。
- Poincaré 对偶的配对是 $Q^k\times Q^{m-k}\to\C$，$m$ 是 socle 所在次数；写成 $Q^k\times Q^k$ 是错的。
- 定理 3.10 要求 $\delta_1+\cdots+\delta_{n-1}$ 既约；对一般 $\delta$ 该乘积公式不成立。

## 相关卡

[等变重数 $m_\calE(t)$](../concepts/equivariant-multiplicity.md) · [非常稳定 Higgs 丛](../concepts/very-stable-higgs-bundle.md) · [$Q_\calE$ 的 Gorenstein 性与 Poincaré 对偶](../derivations/gorenstein-multiplicity-algebra.md) · [定理 3.10：$Q_\delta$ 是 Grassmann 上同调环之积](../derivations/q-delta-grassmann.md)

## 出处（印刷页）

- A p.2238（A p.2238）
- A p.2239（A p.2239）
- A p.2240（A p.2240）

> 说明：A=原文 §3.2 的定义、定理 3.9 与定理 3.10；B=把「有限维 → 完备交 → Gorenstein」的链条补出来；C=「概形论交 vs 集合交」的区分是我们加的提醒。最没把握处：socle 的记号 $J_{h_\calE}$ 原文未定义细节，按 Arnold 学派的 Jacobi 理想理解。
