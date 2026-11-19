# §5.5 的证明：晶体 = D-模的六步

> `cdm14/deriv/cdm-equiv` · 轨道 E · 与 D-模的关系 · 状态 dev · 6 步

> **要回答的问题**：为什么等价要在「心」的层面证，而不能直接比较导出范畴？

## 一句话

Zariski 下降 → Kashiwara 到光滑仿射 → 左右化 → 心上的范畴 → 单子比较，最后用 $D^l_X\simeq\mathrm{Diff}_X$ 收口。

## 目标

证明 $\Crys^r(X)\simeq D\text{-}\mathrm{mod}^r(X)$（$X$ 经典有限型）。

## 前提

- 命题 4.7.3：$D(\Crys^r(X)^\heartsuit)\simeq\Crys^r(X)$（仿射）。
- 引理 5.4.3：$D^l_X\simeq\mathrm{Diff}_X$。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 两边都满足 Zariski 下降，化到 $X$ 仿射。 | 注 5.5.1。 | `A p.47` | A·原文明确写了 |
| 2 | 经典 Kashiwara 把 $X$ 换成光滑仿射。 | 命题 2.5.6 的经典版本。 | `A p.47` | A·原文明确写了 |
| 3 | 用命题 2.4.4 把右晶体换成左晶体，右 D-模换成左 D-模。 | $\Upsilon$ 与 $\omega$ 平移。 | `A p.47` | A·原文明确写了 |
| 4 | 命题 4.7.3 与 4.4.2 把两边写成心上的导出范畴，垂直箭头 $t$-正合。 | 只需心上的等价（图 (5.3)）。 | `A p.48` | A·原文明确写了 |
| 5 | 两边都是 $\QCoh(X)^\heartsuit$ 上单子的模：$\mathrm{Diff}_X$ 与 $\oblv^l\circ\ind^l$。 | §5.5.5 的单子描述。 | `A p.48` | A·原文明确写了 |
| 6 | 引理 5.4.3 给出两个单子同构，故模范畴等价。 | 单子同构 ⇒ 模范畴等价。 | `A p.48` | A·原文明确写了 |

## 结论

$\Crys^r(X)\simeq D\text{-}\mathrm{mod}^r(X)$，且等价与遗忘函子相容。

## 缺口

- 第 4 步「垂直箭头 t-正合」同时用到命题 4.7.3、2.4.4、4.4.2，原文用一张图带过。

## 最容易讲错的地方

- 第 3 步换到左之后，$\omega$ 的平移不能忘，否则 $t$-结构对不上。
- 第 5 步的单子是 $\oblv^l\circ\ind^l$，不是 $\oblv^r\circ\ind^r$。

## 相关卡

[晶体与 D-模：经典等价](../concepts/crystals-vs-dmodules.md) · [核 $D^l_X$ 与微分算子层 $\mathrm{Diff}_X$](../concepts/diff-operators.md) · [$\Crys^r(X)$ 是其心上的导出范畴](../concepts/abelian-heart.md)

## 出处（印刷页）

- A p.47–48（A p.47）

> 说明：A=§5.5.2–5.5.5 的证明结构；最没把握处：第 4 步三条命题的配合方式。
