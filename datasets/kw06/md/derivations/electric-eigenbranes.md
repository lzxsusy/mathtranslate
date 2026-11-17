# 电特征膜 = 平坦 ^LG_C 联络

> `kw/deriv/electric-eigenbranes` · 轨道 E · Langlands 与翻译器 · 状态 dev · 6 步

> **要回答的问题**：零膜为什么是电特征膜，其特征值是什么几何对象，精确处理时又需要作哪些修正？

## 一句话

用 universal Higgs bundle 拉回的联络 $A+\ii\varphi$ 构造电特征膜；关键等式 $U_x\otimes E_q(R)=U_x\otimes E_q(R)|_x$ 说明零膜是电特征膜，其特征值是 $C$ 上的平坦 ${}^LG_\mathbb C$ 丛在 $x$ 的纤维。

## 目标

由 universal Higgs bundle 构造电特征膜，证明零膜是其特征情形，并给出磁侧与精确处理。

## 前提

- B p.119 eq (8.7)：$A+\ii\varphi=\Phi_p^*(\hat A)$ 是 universal Higgs bundle 联络的拉回。
- B p.121 eq (8.10)：$U_x\otimes E_q(R)=U_x\otimes E_q(R)|_x$。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 取 universal Higgs bundle 上的联络 $\hat A$，沿 $\Phi_p:C\to M_H\times C$ 拉回得 $A+\ii\varphi$；沿 $C$ 的平行移动给出 $C$ 上的丛 $E_p(R)$。 | 这条构造把 $M_H$ 上的万有对象变成膜的世界 volume 上的规范场，是电特征膜的定义性输入。 | `B p.119 eq (8.7)` | A·原文明确写了 |
| 2 | Wilson 线算子族作用于膜时，$U\mapsto U\otimes E_p(R)$；若取膜为点状零膜 $U_x$，作用后仍是 $U_x$ 与某个平坦丛的张量积。 | 这正是「特征」的含义：算子只给膜乘上一个固定对象，而膜的支撑不变。 | `B p.121` | A·原文明确写了 |
| 3 | 关键等式：任意丛在一点处平凡，故 $U_x\otimes E_q(R)=U_x\otimes E_q(R)\|_x$——零膜与 $E_q(R)$ 的张量积只是一个纤维空间。 | 这说明零膜在 Wilson 算子族下不变，因此零膜是电特征膜，其特征值就是 $E_q(R)\|_x$。 | `B p.121 eq (8.10)` | A·原文明确写了 |
| 4 | $E_q(R)\|_x$ 是 $C$ 上的平坦丛：Hitchin 方程的解对应平坦 ${}^LG_\mathbb C$ 丛，沿 $C$ 的平坦性由 Hitchin 方程保证。 | 平坦性保证特征值不随 $C$ 上的点连续变化，故「特征值」是有意义的离散数据。 | `B p.122` | A·原文明确写了 |
| 5 | 精确处理：电特征膜应是所有 $e_0$ 上的 twisted 零膜之和，磁特征膜则要按不同 $m_0$ 分支分别取；只有在分支逐个处理时上述简单陈述才严格成立。 | twist 类 $e_0$ 与分支 $m_0$ 是上一节 flux 分解的两种数据，它们使「单个零膜」的图像需要修正。 | `B p.122` | A·原文明确写了 |
| 6 | $S$ 把零膜送到 $M_H(G)$ 中 Hitchin 纤维上的 type F 膜（带秩一平坦 Chan-Paton 丛），故磁特征膜就是零膜的 $S$-对偶像；原文措辞为 at least a glimmering。 | 这句话把电、磁特征膜放进同一幅 $S$-对偶图像，但原文自己承认只是初步理解。 | `B p.123` | C·我们的判断 |

## 结论

由 universal Higgs bundle 拉回的 $A+\ii\varphi$ 定义电特征膜。恒等式 $U_x\otimes E_q(R)=U_x\otimes E_q(R)|_x$ 表明零膜在 Wilson 族下不变，故零膜是电特征膜，其特征值是 $C$ 上平坦 ${}^LG_\mathbb C$ 丛 $E_q(R)$ 在 $x$ 的纤维。精确处理需按 $e_0$ 取 twisted 零膜之和，并按 $m_0$ 分支处理磁侧。

## 缺口

- 精确处理中「所有 $e_0$ 上的 twisted 零膜之和」只在分支逐个处理时成立（B p.122，原文语气为建议）。
- $S$-对偶把零膜送到 type F 膜的论证原文只写 at least a glimmering，不构成完整证明（B p.123）。

## 最容易讲错的地方

- 这里用的是 $A+\ii\varphi$（$t=\ii$ 的 Wilson 侧），不要与 't Hooft 侧的组合混用。
- $E_q(R)|_x$ 是 $C$ 上的平坦丛的纤维，不是 $M_H$ 或 $\Sigma$ 上的丛。

## 相关卡

[特征膜：XB ≅ B ⊗ V 与同时对角化](../derivations/eigenbranes.md) · [universal bundle 的障碍与 twisted 丛](../derivations/twisted-bundles.md) · [Wilson 算子](../concepts/wilson-operator.md) · [希格斯丛](../concepts/higgs-bundle.md)

## 出处（印刷页）

- B p.119–123（B p.121 eq (8.10)）

> 说明：steps 的 provenance 分布：A×5、C×1（共 6 步）；gaps 2 条、pitfalls 2 条。
