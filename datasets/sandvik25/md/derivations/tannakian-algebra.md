# Tannakian 重构里的代数 $A$ 与 $\mathcal O(\widehat{\mathcal N}_X)\to A$

> `sandvik25/deriv/tannakian-algebra` · 轨道 B · Springer 侧与三造函子 · 状态 dev · 5 步

> **要回答的问题**：两个分量映射各自的数学来源是什么，为什么它们的合成会「唯一分解」出 $\mathcal O(\widehat{\mathcal N}_X)$ 上的映射？

## 一句话

先在对称幺半的非全子范畴 $\mathcal C\subset\mathcal P_I^{\mathrm{Wak}}$ 上取端环 $A$，得到 $H\colon\mathcal C\cong A\text{-}\mathrm{mod}_{\mathrm{free}}$；再把 $\mathcal O(\mathfrak g^\vee)\to A$（单值的对数）与 $\mathcal O(X)\to A$（Wakimoto 滤链）拼成 $\mathcal O(\widehat{\mathcal N}_X)\to A$。

## 目标

说明 $F_1$ 的扩张为什么等价于造一个等变代数映射 $\mathcal O(\widehat{\mathcal N}_X)\to A$，以及这个映射怎么造。

## 前提

- 脚注 10：$\mathrm{Coh}^{G^\vee\times T^\vee}_{\mathrm{free}}(\widehat{\mathcal N}_X)$ 对称幺半，而 $\mathcal P_I^{\mathrm{Wak}}$ 不是；故需先换成对称幺半的非全子范畴 $\mathcal C$。
- Tannakian 形式：存在 $H\colon\mathcal C\xrightarrow{\sim}A\text{-}\mathrm{mod}^{G^\vee\times T^\vee}_{\mathrm{free}}$，使 $F'_1$ 成为 $V\mapsto V\otimes A$。
- $\mathcal O(\widehat{\mathcal N}_X)$ 是 $\mathcal O(\mathfrak g^\vee)\otimes\mathcal O(X)$ 的商（因为 $\widehat{\mathcal N}_X\subset\mathfrak g^\vee\times X$ 是闭子概形）。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 取 $\mathcal C$ 的端环 $A=\mathrm{End}_{\mathcal C}(\mathbf 1)$ 型对象，用 Tannakian 形式把 $\mathcal C$ 等同于自由 $A$-模范畴。 | 这是「张量范畴 ↔ 交换代数上的模范畴」的标准双向；$A$ 带 $G^\vee\times T^\vee$ 作用来自 $\mathcal C$ 的等变性。 | `A p.7` | A·原文明确写了 |
| 2 | 造 $\mathcal O(\mathfrak g^\vee)\to A$：把它解释为附近循环的单值自同构的对数。 | 单值算子 $T$ 可写 $\exp(N)$，$N$ 给出 $\mathfrak g^\vee$ 的作用；$Z$ 的构造本身就依赖 $\Psi_f$，故这条映射在 $A$ 中有天然来源。 | `A p.8` | A·原文明确写了 |
| 3 | 造 $\mathcal O(X)\to A$：由定理 2.5.3 的 Wakimoto 滤链给出——滤链的各级商 $\mathbb W_\lambda$ 在 $A$ 中给出坐标函数。 | $X=\mathrm{Spec}\,\mathcal O(G^\vee/U^\vee)$ 的函数环由权坐标生成，而 Wakimoto 滤链恰按 $\lambda$ 分层。 | `A p.8` | A·原文明确写了 |
| 4 | 把两者张量得 $\mathcal O(\mathfrak g^\vee)\otimes\mathcal O(X)\to A$，再用「$\mathcal O(\widehat{\mathcal N}_X)$ 是该张量积的商」得唯一的分解 $\mathcal O(\widehat{\mathcal N}_X)\to A$。 | 商上的映射由原环上「在关系上取零」的映射唯一决定；这正是原文「factors uniquely」的含义。 | `A p.8` | A·原文明确写了 |
| 5 | 于是 $F_2(M)=M\otimes_{\mathcal O(\widehat{\mathcal N}_X)}A$，即沿环映射的换基。 | 换基函子自动是右正合、幺半的，故 $F_2$ 的幺半性不需要另证。 | `A p.8` | A·原文明确写了 |

## 结论

$F_2$ = 沿 $\mathcal O(\widehat{\mathcal N}_X)\to A$ 的换基；$A$ 由 $\mathcal C$ 的 Tannakian 端环给出。

## 缺口

- Tannakian 形式在此是黑箱：$\mathcal C$ 具体取哪个子范畴、$A$ 的具体计算，原文都未给。
- 「$\mathcal O(\mathfrak g^\vee)\to A$ 是单值的对数」「$\mathcal O(X)\to A$ 由 Wakimoto 滤链定」两句都只有一句解释，没有构造细节。

## 最容易讲错的地方

- 把 $A$ 与 $\mathcal O(\widehat{\mathcal N}_X)$ 混同：前者是范畴的端环，后者是几何环，映射方向是几何 → 范畴。
- 忽略「对称幺半」这个前提：$\mathcal P_I^{\mathrm{Wak}}$ 不对称，故必须先换到 $\mathcal C$，否则 Tannakian 形式不适用。

## 相关卡

[函子 II：经 Tannakian 重构把 $F_1$ 扩到 $\mathrm{Coh}_{\mathrm{free}}(\widehat{\mathcal N}_X)$](../concepts/functor-f2.md) · [无穷小稳定化子 $\widehat{\mathcal N}$ 与 $\widehat{\mathcal N}_X$](../concepts/hat-n-x.md) · [中心层的 Wakimoto 滤链（定理 2.5.3）](../concepts/wakimoto-filtration.md)

## 出处（印刷页）

- A p.7–8（A p.8）

> 说明：构造在 p.7，两条分量映射与「唯一分解」在 p.8，脚注 10 在 p.7。
