# 中心 Z、离散 flux 与 S-对偶的作用

> `kw/deriv/center-and-flux` · 轨道 E · Langlands 与翻译器 · 状态 dev · 5 步

> **要回答的问题**：规范群的中心如何决定 't Hooft 算子的相位，紧流形上的离散 flux 又在 $S$-对偶下如何变换？

## 一句话

中心 $Z=\Lambda^\vee/\Lambda$ 通过完美配对 $\Upsilon$ 控制 't Hooft 算子的相位；紧流形上的离散 flux $(e,m)$ 与 $S$ 的作用 $(e,m)\mapsto(-m,e)$ 把理论分成电、磁两类分支。

## 目标

用中心上的完美配对定义 't Hooft 算子的相位，并把离散 flux 的 $S$ 变换算清楚。

## 前提

- B p.104 eq (7.1)：$\Upsilon:Z\times Z\to U(1)$ 是中心上的完美配对。
- B p.104 eq (7.2)：$\Upsilon(a,b)=\exp(2\pi\ii\langle a,b\rangle)$；单连时 $Z=\Lambda^\vee/\Lambda$。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 群的中心 $Z$ 带有完美配对 $\Upsilon(a,b)=\exp(2\pi\ii\langle a,b\rangle)$；单连情形 $Z=\Lambda^\vee/\Lambda$ 是权格模根格。 | 配对的非退化性保证「相位」把中心元素与对偶侧元素一一对应，这是后面所有离散数据的来源。 | `B p.104 eq (7.1)` | A·原文明确写了 |
| 2 | 't Hooft 算子绕紧流形一圈时，其相位由配对 $\Upsilon$ 给出；只有 $Z$ 中的元素才给出良好定义的相位，故算子在紧空间上按中心分类。 | 这解释了为什么规范群有中心时 't Hooft 算子才有离散的、拓扑的标签。 | `B p.104` | A·原文明确写了 |
| 3 | 在紧四维流形 $W$ 上，丛的拓扑由 $\xi(E)=a\oplus m$ 描述，其中 $a\in H^1(W,Z)$ 是离散电 flux、$m\in H^2(W,Z)$ 是离散磁 flux。 | 把连续场论约化后，剩下的拓扑数据正是这两个上同调类，它们不能连续形变。 | `B p.105 eq (7.6)` | A·原文明确写了 |
| 4 | $S$ 交换这两类 flux：$S:(e,m)\mapsto(-m,e)$，故 $\oplus_e H_{e,0}$ 与 $\oplus_m H_{0,m}$ 在 $S$ 下互换。 | 这正是电-磁对偶在离散扇区上的体现：$S$ 把纯电扇区送到纯磁扇区。 | `B p.106 eq (7.9)` | A·原文明确写了 |
| 5 | 把 $H_{e,m}$ 按电、磁指标分解可得 $\oplus_e H_{e,0}$ 与其对偶 $\oplus_m H_{0,m}$；一般 $(e,m)$ 给出混合扇区，只有 $(0,m)$ 与 $(e,0)$ 在 $S$ 下互变。 | 这给出紧流形上 Hilbert 空间的完整分解，并说明 $S$ 是其中的对偶变换。 | `B p.106 eq (7.10)` | A·原文明确写了 |

## 结论

中心 $Z$ 上的完美配对 $\Upsilon$ 给出 't Hooft 算子的离散相位，因此有中心的规范群才能定义相应算子。紧四维流形上丛的拓扑由离散 flux $(e,m)\in H^1(W,Z)\oplus H^2(W,Z)$ 描述，$S$ 作用为 $(e,m)\mapsto(-m,e)$，把纯电扇区与纯磁扇区互换。

## 缺口

- 流形有奇点时 universal bundle 的障碍可能还有局部贡献，原文只在脚注中提及（B p.107 脚注 32）。

## 最容易讲错的地方

- $Z=\Lambda^\vee/\Lambda$ 只在单连群时成立；一般群要用中心的定义而非这个商。
- $S$ 把 $(e,m)$ 换成 $(-m,e)$，不是 $(m,e)$；负号来自定向与 $S$ 的矩阵形式。

## 相关卡

[universal bundle 的障碍与 twisted 丛](../derivations/twisted-bundles.md) · [电特征膜 = 平坦 ^LG_C 联络](../derivations/electric-eigenbranes.md) · [S-对偶](../concepts/s-duality.md) · [拓扑量子场论](../concepts/topological-qft.md)

## 出处（印刷页）

- B p.103–106（B p.104 eq (7.1)）

> 说明：steps 的 provenance 分布：A×5（共 5 步）；gaps 1 条、pitfalls 2 条。
