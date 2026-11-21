# $Q_\calE$ 的 Gorenstein 性与 Poincaré 对偶

> `hausel22/deriv/gorenstein-multiplicity-algebra` · 轨道 D · 幂零锥上的等变重数 · 状态 dev · 5 步

> **要回答的问题**：为什么一个坐标环会满足 Poincaré 对偶这种「拓扑」性质？

## 一句话

$h$ 是完备交，故 $Q_\calE$ 是 Artin 完全交，从而是 Gorenstein、有 socle 与 Poincaré 对偶，且 Poincaré 多项式等于 $m_\calE(t)$。

## 目标

由 $h_\calE$ 的有限性与 $h$ 的完备交结构，推出定理 3.9 的五条性质。

## 前提

- $Q_\calE=\C[W^+_\calE]/(h_1,\dots,h_N)$，$N=\dim\calA=\dim W^+_\calE$（在光滑点处）。
- $\calE$ 非常稳定，故 $h_\calE$ 有限（定理 3.3）。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | $W^+_\calE$ 光滑、维数等于 $N$，方程个数也是 $N$，故 $Q_\calE$ 是零维完全交。 | 完全交的维数 = 环境维数 − 方程个数 = 0；零维即有限维。 | `A p.2239` | A·原文明确写了 |
| 2 | $\T$ 分次来自 $W^+_\calE$ 与 $h_i$ 的齐次性：$\lambda:(E,\Phi)\mapsto(E,\lambda\Phi)$ 使 $h_i$ 齐次，故理想齐次，商环分次，且 $Q^0_\calE\cong\C$。 | 齐次理想之商自然分次；零次部分由常数给出。 | `A p.2239` | A·原文明确写了 |
| 3 | 零维完全交是 Gorenstein：socle 一维，$Q^m_\calE\cong\C J_{h_\calE}$，其中 $J_{h_\calE}$ 是 Jacobi 理想。 | 这是 Arnold 学派关于孤立奇点的标准结论：完全交的 socle 由 Jacobi 行列式生成。 | `A p.2239` | B·原文暗示、我们补的中间步 |
| 4 | Gorenstein + 分次 ⇒ Poincaré 对偶 $Q^k\times Q^{m-k}\to\C$。 | socle 一维给出非退化的配对，这是 Gorenstein 分次代数的定义性性质。 | `A p.2239` | B·原文暗示、我们补的中间步 |
| 5 | Poincaré 多项式等于 $m_\calE(t)$：两者都数 $\T$-权空间的维数。 | $Q_\calE$ 的分次维数就是 $W^+_\calE\cap h^{-1}(0)$ 的等变重数。 | `A p.2239` | A·原文明确写了 |

## 结论

$Q_\calE$ 有限维、分次、$Q^0\cong\C$、Gorenstein（socle $\cong\C J_{h_\calE}$）、满足 Poincaré 对偶，且 $\sum_k\dim(Q^k)t^k=m_\calE(t)$。

## 缺口

- 第 3 步的 Gorenstein 性是引用 Arnold 学派与 [HH1]，本文未证明；完备交 ⇒ Gorenstein 的推导细节未写。
- 第 5 步「分次维数 = $m_\calE(t)$」的等号原文视为显然，未给证明。

## 最容易讲错的地方

- Gorenstein 不等于正则：$Q_\calE$ 一般有奇点，只要求 socle 一维。
- 零维完全交的「完全交」是指方程个数等于环境维数，不是「理想由正则序列生成」的更强条件（两者在此等价，但说法不同）。
- Poincaré 对偶的配对是 $Q^k\times Q^{m-k}\to\C$，$m$ 是 socle 的次数，不是维数。
- 分次性依赖 $\T$-作用，去掉 $\T$ 就只有非分次的环，Poincaré 多项式无从谈起。

## 相关卡

[局部重数代数 $Q_\calE$](../concepts/local-multiplicity-algebra.md) · [等变重数 $m_\calE(t)$](../concepts/equivariant-multiplicity.md) · [非常稳定 $\Rightarrow$ 重数是多项式](../derivations/multiplicity-polynomial.md)

## 出处（印刷页）

- A p.2239（A p.2239）

> 说明：A=原文定理 3.9 的五条与 $Q_\calE$ 的定义；B=第 3、4 步的标准代数论证（完备交 ⇒ Gorenstein ⇒ Poincaré 对偶）是我们补的；C=「分次维数 = 重数」的解释是我们的。最没把握处：socle 记号 $J_{h_\calE}$ 的确切定义（Jacobi 理想）原文未写。
