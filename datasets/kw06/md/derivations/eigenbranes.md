# 特征膜：XB ≅ B ⊗ V 与同时对角化

> `kw/deriv/eigenbranes` · 轨道 D · 二维、膜与算子 · 状态 dev · 8 步

> **要回答的问题**：线算子作用在膜上时为何能把膜变成自身的张量积，这种特征膜与算子代数如何对应？

## 一句话

线算子 $X$ 贴近边界把 $B$ 变成 $XB$；若 $XB\cong B\otimes V$ 就称 $B$ 为特征膜。不同点的算子自动交换，故可同时对角化；Wilson 与 't Hooft 侧的 OPE 分别生成 $\mathrm{Rep}(G)$ 与预期的 $\mathrm{Rep}({}^LG)$。

## 目标

由 $XB\cong B\otimes V$ 定义特征膜，说明交换性、同时对角化与两侧 OPE 代数。

## 前提

- B p.94：线算子 $X$ 贴近边界，把边界条件 $B$ 变成新膜 $XB$。
- B p.95 eq (6.22)：特征膜的定义是 $XB\cong B\otimes V$。
- B p.95：张量积满足 $H_{\tilde B,B\otimes V}=H_{\tilde B,B}\otimes V$。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 线算子沿 $\Sigma$ 方向贴近边界时，相当于在边界上插入一个算子；它把原来的边界条件 $B$ 改变为新的膜 $XB$，这是「线作用于膜」的基本图像。 | 只有把线算子看成边界条件的变换，才能把算子代数翻译为膜的几何。 | `B p.94` | A·原文明确写了 |
| 2 | 若存在向量空间 $V$ 使 $XB\cong B\otimes V$，则称 $B$ 为特征膜：线算子的作用只是给开弦空间乘上 $V$。 | 这正是「本征值」的范畴化：算子作用等价于张量积一个固定对象。 | `B p.95 eq (6.22)` | A·原文明确写了 |
| 3 | 张量积规则 $H_{\tilde B,B\otimes V}=H_{\tilde B,B}\otimes V$ 表明：与任何别的膜 $\tilde B$ 之间的态空间都统一地乘以 $V$，因此 $V$ 是膜本身的属性。 | 若没有这条规则，「特征」就只是单个空间上的偶然同构，无法在膜之间一致地定义。 | `B p.95` | A·原文明确写了 |
| 4 | 不同点的线算子可以互相穿过（图 9），因此在二维拓扑场论中它们天然交换；交换性保证存在同时对角化的基，即同时特征膜。 | 交换性是「算子可同时测量」的代数表达，也解释了特征膜为什么必须存在。 | `B p.96` | A·原文明确写了 |
| 5 | 把线算子缩到一点得到点状算子 $X_p$：$X_pB=B\otimes V_p$，其中 $V_p$ 是 $C$ 上的平坦丛，沿 $C$ 移动 $p$ 只作平行移动。 | 平坦性说明 $V_p$ 只依赖 $C$ 的基本群，这为电特征膜的构造（用平坦丛 $E_q(R)\|_x$）铺路。 | `B p.97 eq (6.25)` | A·原文明确写了 |
| 6 | 按算子来源分两类：Wilson 族给出电特征膜（electric eigenbrane），'t Hooft 族给出磁特征膜（magnetic eigenbrane）；它们分别是相应算子族的联合特征膜。 | 两类算子对应不同的几何构造，必须分开命名才不会混淆。 | `B p.98` | A·原文明确写了 |
| 7 | OPE 给出算子代数：Wilson 侧精确为 $\mathrm{Rep}(G)$（(6.27)），'t Hooft 侧预期为 $\mathrm{Rep}({}^LG)$（(6.29)，原文写 we expect）。 | 两个代数正是 $G$ 与 ${}^LG$ 的表示环，把「算子代数」与「表示论」对应起来是几何 Langlands 的入口。 | `B p.98 eq (6.27)` | A·原文明确写了 |
| 8 | 't Hooft 侧的 OPE 是否等于 $\mathrm{Rep}({}^LG)$ 在一般群上仍是预言：原文只写 we expect，属于几何 Langlands 待证的一端。 | 把已证与预期分开叙述，才能准确标出这一节结论的强弱。 | `B p.99 eq (6.29)` | C·我们的判断 |

## 结论

线算子 $X$ 贴近边界把 $B$ 变成 $XB$；当 $XB\cong B\otimes V$ 时称 $B$ 为特征膜，此时与任意膜 $\tilde B$ 的态空间都张量上 $V$。不同点算子交换，故特征膜可同时对角化；点状情形给 $X_pB=B\otimes V_p$，$V_p$ 是 $C$ 上平坦丛。电与磁特征膜分别来自 Wilson 与 't Hooft 族，其 OPE 代数分别为 $\mathrm{Rep}(G)$ 与（预期的）$\mathrm{Rep}({}^LG)$。

## 缺口

- 't Hooft OPE 等于 $\mathrm{Rep}({}^LG)$ 在一般群上只写 we expect，未证明（B p.99）。

## 最容易讲错的地方

- 特征膜的条件是 $XB\cong B\otimes V$，不是 $XB\cong B$；$V$ 还必须带平坦结构（点状情形）。
- Wilson 给 $\mathrm{Rep}(G)$、't Hooft 给 $\mathrm{Rep}({}^LG)$，两个群不要弄反。

## 相关卡

[Wilson 与 't Hooft 线算子及其分类](../derivations/line-operators.md) · [折叠：线算子变成边界条件](../derivations/folding.md) · [特征膜（eigenbrane）](../concepts/eigenbrane.md) · [Hecke 特征层](../concepts/hecke-eigensheaf.md)

## 出处（印刷页）

- B p.94–99（B p.95 eq (6.22)）

> 说明：steps 的 provenance 分布：A×7、C×1（共 8 步）；gaps 1 条、pitfalls 2 条。
