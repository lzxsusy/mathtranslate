# Wilson 与 't Hooft 线算子及其分类

> `kw/deriv/line-operators` · 轨道 D · 二维、膜与算子 · 状态 dev · 8 步

> **要回答的问题**：Wilson 与 't Hooft 线算子为什么都保半超对称，它们按什么数据分类，作用在膜上又会产生什么？

## 一句话

把 Wilson 与 't Hooft 线算子统一为保半超对称的算子：Wilson 由表示 $R$ 标号、't Hooft 由 $\rho:U(1)\to G$ 即 ${}^L\!R$ 标号；它们把边界 $B$ 变成 $XB$，OPE 分别生成 $\mathrm{Rep}(G)$ 与（预期）$\mathrm{Rep}({}^LG)$。

## 目标

由超对称变分定出半 BPS 线算子，用表示论分类，并说明它们把边界条件变为新膜。

## 前提

- B p.79 eq (6.1)：Wilson 圈 $W_0(R,S)=\mathrm{Tr}_R P\exp(-\oint_S A)$。
- B p.80 eq (6.2)：超对称变换 $\delta_T A=\ii u\psi+\ii v\tilde\psi$。
- B p.80 eq (6.3)：$\delta_T\varphi=\ii v\psi-\ii u\tilde\psi$。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 单独的 $W_0$ 在超对称变换下不保持：$\delta_T A$ 给出 $\ii u\psi+\ii v\tilde\psi$，而 $\varphi$ 的变分是 $\ii v\psi-\ii u\tilde\psi$。取 $t=v/u=\ii$ 时组合 $A+\ii\varphi$ 的变分抵消，得到半 BPS Wilson 算子 $W(R,S)=\mathrm{Tr}_R P\exp(-\oint_S(A+\ii\varphi))$。 | 两个变分要线性组合成零，唯一可能是 $t=\pm\ii$；非零的 $t$ 实数给不出闭算子。 | `B p.80 eq (6.4)` | A·原文明确写了 |
| 2 | Wilson 线可以是不闭合的：端点在 $p\to q$ 时它给平行移动矩阵，作用在边界上就是边界局部算子。 | 这解释了为什么线算子能「贴近边界」并改变边界条件，而不只是一个环上的示性数。 | `B p.81` | A·原文明确写了 |
| 3 | 't Hooft 算子由单极子奇点定义：$U(1)$ 情形 $F\sim(\ii m/2)\star_3 d(1/\|x\|)$、$\varphi\sim(\ii/2\|x\|)ds$；一般群由同态 $\rho:U(1)\to G$ 的共轭类给出，等价于 ${}^LG$ 的最高权即不可约表示 ${}^L\!R$。 | GNO 对偶把「磁荷」翻译为对偶群的表示，这正是分类数据的来源。 | `B p.84` | A·原文明确写了 |
| 4 | 两类算子都是 order/disorder 对偶的两端：Wilson 由 $G$ 的表示 $R$ 标号，'t Hooft 由 ${}^LG$ 的表示 ${}^L\!R$ 标号；在 $U(N)$ 自对偶情形两者标号可以比较。 | 把两类算子放进同一个表示论框架，才能在后面讨论它们生成的代数。 | `B p.84` | A·原文明确写了 |
| 5 | 从拓扑看，算子可支撑在 $C$ 中的三类曲线上：点 $p\times S'$ 给局部算子，$S''\times q$ 给线算子，一般曲线上的算子可分解为线算子与局部算子的乘积。 | 这给出算子的一般定义：任意曲线上的算子都由线算子加上插入的局部算子构成。 | `B p.89` | A·原文明确写了 |
| 6 | 线算子 $X$ 贴近边界时把边界条件 $B$ 变成新膜 $XB$；由于算子来自四维理论，不同点的算子自动交换（$C$ 至少二维），因此可以同时作用。 | 交换性是把线算子视为「可同时对角化的可观测量」的前提，也是特征膜概念的起点。 | `B p.94` | A·原文明确写了 |
| 7 | Wilson 与 't Hooft 线的 OPE 给出算子代数：Wilson 侧精确地生成 $\mathrm{Rep}(G)$（(6.27)），'t Hooft 侧预期生成 $\mathrm{Rep}({}^LG)$（(6.29)）。 | 两个代数分别是 $G$ 与 ${}^LG$ 的表示环，这为几何 Langlands 的「特征层↔表示」对应提供算子侧输入。 | `B p.98 eq (6.27)` | A·原文明确写了 |
| 8 | $U(N)$ 情形可检验 't Hooft 算子的 OPE 与 $\mathrm{Rep}({}^LG)$ 一致，但一般群的这一陈述原文只写「we expect」，是几何 Langlands 的预言而非本文的证明。 | 把精确与预期分开，才能说清本文证明的边界在哪里。 | `B p.99 eq (6.29)` | C·我们的判断 |

## 结论

Wilson 与 't Hooft 线算子都是保半超对称的算子，分别在 $t=\pm\ii$ 与 $t=1$ 附近定义。Wilson 由 $G$ 的表示 $R$ 标号，'t Hooft 由 $\rho:U(1)\to G$ 即 ${}^LG$ 的最高权 ${}^L\!R$ 标号。它们把边界 $B$ 变成 $XB$，且 OPE 分别生成 $\mathrm{Rep}(G)$ 与（预期的）$\mathrm{Rep}({}^LG)$。

## 缺口

- 't Hooft OPE 等于 $\mathrm{Rep}({}^LG)$ 在一般群上原文只写「we expect」，缺少证明（B p.99）。
- 弱消失定理只对 $(B,A,A)$ 型膜有效，讨论其他膜型时不能直接引用（B p.126）。

## 最容易讲错的地方

- Wilson 只在 $t=\pm\ii$ 时保超对称，且必须用组合 $A+\ii\varphi$；单独的 $W_0$ 不保超对称。
- 两类算子的标号属于不同的群：Wilson 用 $G$ 的表示，'t Hooft 用 ${}^LG$ 的表示，不要混用。

## 相关卡

[折叠：线算子变成边界条件](../derivations/folding.md) · [特征膜：XB ≅ B ⊗ V 与同时对角化](../derivations/eigenbranes.md) · [Wilson 算子](../concepts/wilson-operator.md) · ['t Hooft 算子](../concepts/thooft-operator.md)

## 出处（印刷页）

- B p.79–99（B p.80 eq (6.4)）

> 说明：steps 的 provenance 分布：A×7、C×1（共 8 步）；gaps 2 条、pitfalls 2 条。
