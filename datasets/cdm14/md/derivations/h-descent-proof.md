# h-下降的证明：双单纯对象与两次全化

> `cdm14/deriv/h-descent-proof` · 轨道 C · 下降性质与归纳函子 · 状态 dev · 4 步

> **要回答的问题**：固有满覆盖的下降为什么不能直接用 $\IndCoh$ 的下降？

## 一句话

把固有满覆盖 $S'\to S$ 与其 de Rham 版本拼成双单纯对象，两个方向各用一次命题 3.1.3，再比较全化。

## 目标

证明 $\Crys^r(S)\to\mathrm{Tot}(\Crys^r(S'^\bullet/S))$ 对 h-覆盖是等价。

## 前提

- 命题 3.1.3：$\Crys^r(X)\simeq\mathrm{Tot}(\IndCoh(X_\bullet/X_{\mathrm{dR}}))$。
- $\IndCoh$ 满足 fppf 下降（[IndCoh, 推论 10.4.5]）。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 先处理平展（含 Zariski）覆盖：$\Crys^r$ 逐项是 $\IndCoh$ 的极限，故继承 fppf 下降。 | 极限的下降性质逐项继承。 | `A p.26` | A·原文明确写了 |
| 2 | 对固有满 $S'\to S$，构造双单纯对象 $(S'^\bullet/S)\star(S'^\bullet_{\mathrm{dR}}/S_{\mathrm{dR}})$。 | 一行记录覆盖，一列记录 de Rham 方向，交错后每行都是群胚。 | `A p.26` | A·原文明确写了 |
| 3 | 沿一个方向用命题 3.1.3 把 $\Crys^r$ 换成全化，沿另一个方向用固有满映射的 $\IndCoh$ 下降。 | 两次下降给出同一个全化。 | `A p.27` | B·原文暗示、我们补的中间步 |
| 4 | 比较两个全化，得到 $\Crys^r(S)\simeq\mathrm{Tot}(\Crys^r(S'^\bullet/S))$。 | 双单纯对象全化的交换性。 | `A p.27` | A·原文明确写了 |

## 结论

$\Crys^r$ 满足 h-下降，从而满足 fppf 下降。

## 缺口

- 第 3 步「固有满映射的 $\IndCoh$ 下降」在原文中是 [GR1] 的结果，本文只写「用同样的论证」。

## 最容易讲错的地方

- 双单纯对象的两个方向不能交换顺序，否则会用到尚未证明的下降。
- 固有满覆盖不是平展覆盖，不能把第 1 步直接套到第 2 步。

## 相关卡

[晶体满足 h-下降](../concepts/h-descent.md) · [无穷小群胚 $X\times_{X_{\mathrm{dR}}}X\rightrightarrows X$](../concepts/infinitesimal-groupoid.md)

## 出处（印刷页）

- A p.26–27（A p.26）

> 说明：A=命题 3.2.2 的证明；B=[GR1] 的固有满下降；最没把握处：双单纯对象两方向的先后。
