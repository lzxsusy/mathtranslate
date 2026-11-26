# 用赋值判据把紧合性化归为构造一个 $\varphi$-格

> `lafforgue02/deriv/properness-by-valuative-criterion` · 轨道 B · 拓扑镜像对称与 Hodge 数 · 状态 dev · 4 步

> **要回答的问题**：一条几何的紧合性，怎样被一步步换成一个「在 $V$ 中找一个格」的代数问题？

## 一句话

紧合性 $\rightsquigarrow$ 赋值判据 $\rightsquigarrow$ 一般纤维上的 $\varphi$-空间 $\rightsquigarrow$ 造一个满足 $p$ 的迭代 $\varphi$-格；第 V 章给路线，第 VI 章给构造。

## 目标

说明第 V、VI 章如何用赋值判据把主定理的紧合性归约到迭代 $\varphi$-格的构造。

## 前提

- $A$ 为离散赋值环，$K_A=\mathrm{Frac}(A)$，$\kappa_A$ 剩余域，$\pi_A$ 一致化子。
- 正则曲面 $X\otimes A$，特殊纤维 $X\otimes\kappa_A$，一般纤维 $X\otimes K_A$。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 紧合性 $\ol{\Cht}^{\,r,d,\ol p\le p}\to X\times X$ 由赋值判据检验：每个 $K_A$-点都延拓为 $A$-点。 | $X\times X$ 上的紧合态射可用赋值判据刻画，这是 Grothendieck 的标准判据。 | `A p.34` | A·原文明确写了 |
| 2 | $K_A$-点即一般纤维上的 chtouca；延拓即求其特殊化，等价于在该 chtouca 的 $\varphi$-空间 $V$ 中找一个迭代 $\varphi$-格 $M$，使 $\varphi(M)\subset M$ 且 $[M:\varphi(M)]$ 受 $p$ 控制。 | chtouca 在一般纤维处的结构由 $\varphi$-格刻画，特殊化就是格的选取。 | `A p.35` | A·原文明确写了 |
| 3 | 第 V 章：迭代 $\varphi$-格有无穷多个，其中恰有一个满足 $p$ 的条件；用初等变换在它们之间移动，并追踪退化子族避开 $N$。 | 「恰有一个」保证延拓唯一，从而判据成立。 | `A p.36` | A·原文明确写了 |
| 4 | 第 VI 章：用初等变换的序列显式构造出这个格，补全存在性，并修正 [Lafforgue 1998] 末页由 Varshavsky 指出的小错。 | 第 V 章只给路线，构造要靠序列；这也是本讲义比长文更精确的地方。 | `A p.45` | A·原文明确写了 |

## 结论

主定理（$\ol{\Cht}^{\,r,\ol p\le p}_N/a^{\mathbb Z}$ 的紧合性与光滑性）由赋值判据归约，最终落在「迭代 $\varphi$-格的存在唯一」这一代数命题上；该命题由初等变换序列构造。

## 缺口

- 第 V 章的存在唯一只给路线，第 VI 章的构造细节仍依赖 [Lafforgue 1998]；本讲义自称「比前面几章精确得多」，但对全部引理的证明仍是概要。

## 最容易讲错的地方

- 赋值判据的「$A$」是任意的离散赋值环，不是 $X$ 的局部环；只在 $X$ 的局部环上验证是特例，不足。
- 「恰有一个格」是判据成立的关键：若只是「存在」，延拓不唯一，紧合性仍不成立。

## 相关卡

[紧合性的赋值判据](../concepts/valuative-criterion-properness.md) · [迭代 $\varphi$-格](../concepts/iterated-phi-lattice.md) · [退化子（dégénérateur）](../concepts/degenerator.md)

## 出处（印刷页）

- A p.34–45（A p.34）

> 说明：归约链取第 V 章 p.34–35；存在唯一与初等变换取 p.36–41；第 VI 章的构造与「修正」取 p.42–45。本卡把两章压缩成一条链，未新增数学内容。
