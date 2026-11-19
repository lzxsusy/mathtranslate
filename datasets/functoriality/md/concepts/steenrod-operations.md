# Steenrod 运算

> `functoriality/concept/steenrod-operations` ｜ track D ｜ draft

**一句话**：模 p 上同调上的 Steenrod 运算可看成相干同伦交换代数结构的产物；§5.4 猜想它们能从余切丛 Floer 理论与逐纤维相加几何提取（作者猜想，非定理）。

**自测**：Steenrod 运算为什么可能与余切丛的 Floer 理论发生联系，这个联系目前只是猜想还是已证定理？

## 定义

Steenrod 运算是模 $p$ 上同调上的自然运算。§5.4 的观察是：在特征 $0$，$\Ainf$-代数的交换性本质上不提供额外信息；而在有限特征下，「相干地同伦交换」的代数理论足够丰富，可以从中提取空间上同调上的 Steenrod 运算。作者据此提出猜想 5.6：闭流形上同调的 Steenrod 运算可从其余切丛的 Floer 理论与逐纤维相加的几何中提取出来。本卡必须强调：这是猜想，不是本文定理。

记号：$p$：素数（或有限特征）；$\Gamma^\otimes$：实现对称幺半结构的拉格朗日对应；「幺半单位」$L$ 满足 $\Gamma^\otimes\circ_{1,2}(L\times L)=L$。

## 要点

- Steenrod 运算定义在模 $p$ 上同调上；在特征 $0$，交换性本质上是 $\Ainf$-代数的内在性质，能提取的额外信息很少。
- 在有限特征，相干同伦交换的代数理论足够丰富，可提取 Steenrod 运算；这是猜想 5.6 的动机。
- 猜想 5.6（作者提出，非定理）：这些运算可从闭流形余切丛的 Floer 理论加逐纤维相加的几何得到。
- 与 §5.4 的对称幺半结构相关：幺半结构的单位是满足 $\Gamma^\otimes\circ_{1,2}(L\times L)=L$ 的拉格朗日 $L$；在特征 $0$ 其 Floer 上同调环的乘法交换，但信息很少。

## 公式

$\Gamma^\otimes\subset M\times M\times M^-$
$\Gamma^\otimes\circ_{1,2}(L\times L)=L$

## 定理与证明

### 猜想 5.6（作者提出，非定理）

闭流形的上同调上的 Steenrod 运算可以从其余切丛的 Floer 理论以及逐纤维相加的几何中提取出来。

（none；来源：原书 p.57 §5.4（作者猜想 5.6））


缺口：原文用 conjecture 环境，没有证明；这是作者提出的猜想，不能当作定理使用。

## 易错点

- 把猜想 5.6 当定理：原文明确是 conjecture 环境，本文没有证明。
- 以为特征 $0$ 也有同样丰富的 Steenrod 信息：交换性在特征 $0$ 本质上是 $\Ainf$-代数的性质，额外信息很少。
- 把「相干地同伦交换」与严格交换混淆：可提取 Steenrod 运算的正是相干同伦交换结构。

## 参考与关联

- Abouzaid & Bottman, Functoriality in categorical symplectic geometry (arXiv:2210.11159v1)，§5.4，p.57–57（原书 p.57 §5.4）

关联：`functoriality/concept/hms`、`functoriality/concept/formal-group`、`functoriality/concept/g-manifold`

来源说明：据中译本 §5.4（p.57）转述；Steenrod 猜想 5.6 为作者提出，非定理。
