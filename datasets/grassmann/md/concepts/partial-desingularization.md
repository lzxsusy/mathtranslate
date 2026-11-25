# 部分消奇异

> `grassmann/concept/partial-desingularization` · 轨道 4 · 奇异模空间的相交配对 · 状态 draft

> **先自测**：为什么必须反复爆破到所有稳定子群有限，只爆破一次得到的商有什么问题？

## 一句话

按稳定子群维数逆向归纳地沿最高维稳定子层爆破，把奇异辛商换成轨形，使普通上同调仍带 Kirwan 映射、并能看见相交上同调。

## 定义

设紧 Lie 群 $K$（极大环面 $T$）Hamilton 作用于辛流形 $M$，矩映射 $\mu$，辛商 $\mu^{-1}(0)/K$ 奇异。**部分消奇异**是按稳定子群维数作逆向归纳的爆破：先沿稳定子群维数最高的点构成的子簇爆破，使该层稳定子维数下降；对结果重复同一操作，直到所有稳定子群均为有限群，得到 $\widetilde M$。它具有以下性质：$K$ 的作用与矩映射 $\tilde\mu: \widetilde M\to\mathfrak{k}^*$ 一起延拓到 $\widetilde M$ 上；$\widetilde M$ 的稠密开集光滑且带辛结构；辛商 $\tilde\mu^{-1}(0)/K$ 是**轨形**（orbifold，每点稳定子有限）。

**记号约定**：$\widetilde M$ 记部分消奇异，$\widetilde{M^{\mathrm{ext}}}$ 是扩张模空间的部分消奇异；$\Delta$ 记稳定子群为整个 $K$ 的点集；$\widetilde\mu$ 是延拓后的矩映射；「轨形」指商在每点局部同构于 $\mathbb{R}^{2m}/\Gamma$，$\Gamma$ 有限。

## 要点（为什么需要它）

- 爆破对象是「稳定子群维数最高的点构成的子簇」（loci），不是某个群作用的轨道；中译 p.72 作「轨迹」是误译，会让人去找一个群作用。
- 归纳是逆向的：每一轮只降一维稳定子，$M(2,0)$ 第一轮沿 $\Delta=(S^1)^{2g}$（稳定子整个 $SU(2)$ 的点集，$\cong\mathrm{Jac}$）爆破，第二轮沿 $G\widehat\Gamma$ 爆破。
- 消奇异之后 $H^*(\widetilde M//K)$ 仍带 Kirwan 映射并且满射，而 $IH^*(M//K)$ 是它的直和项——这是能用 $\widetilde M$ 的上同调算 IH 配对的原因。
- $H_K^*(M^{\mathrm{ext}})$ 中的类可拉回到 $H_K^*(\widetilde{M^{\mathrm{ext}}})$，所以配对可以「先消奇异再算」。

## 关键公式

$$
\tilde\mu: \widetilde M\to\mathfrak{k}^*,\qquad \tilde\mu^{-1}(0)/K\ \text{是轨形}
$$

$$
IH^*(M//G)\ \hookrightarrow\ H^*(\widetilde M//G)\qquad(\text{直和项})
$$

$$
\Delta=(S^1)^{2g}\cong\mathrm{Jac}\subset M^{\mathrm{ext}}
$$

## 定理与证明（或缺口）

### 部分消奇异的存在性与轨形性（Kirwan）

对紧 Lie 群 $K$ 在辛流形 $M$ 上的 Hamilton 作用，存在由「沿最高维稳定子层爆破并迭代」得到的 $\widetilde M$，使 $K$ 的作用与矩映射延拓到 $\widetilde M$，且辛商 $\tilde\mu^{-1}(0)/K$ 是轨形；从而 $H_K^*(\widetilde M)\to H^*(\tilde\mu^{-1}(0)/K)$ 是满射。

**证明状态：只引出处，原书不重证**


出处：中译 p.73（§2，引 Kirwan, Ann. Math. 122 (1985)）

## 易错点

- 把部分消奇异当成一次爆破：只爆破最高维那一层后仍有非平凡稳定子，商还不是轨形，$H^*(\widetilde M//K)$ 也还不足以看见 $IH$。
- 把 $\Delta=(S^1)^{2g}$ 读成「$2g$ 维的环面」：它是极大环面 $S^1$ 的 $2g$ 次幂，维数 $2g$，同构于 $\mathrm{Jac}$，正是 $(S^1)^{2g}$ 这个记号里容易读错的地方。
- 以为消奇异后 $M(n,d)$ 的相交数可以直接在 $\widetilde M$ 上算：$\widetilde M\to M$ 是双有理而非同构，必须经 $V_M$ 与 $\kappa$ 才能把类搬回 $IH$。

## 相关卡

- [扩张模空间](../concepts/extended-moduli-space.md)
- [平衡作用](../concepts/balanced-action.md)
- [部分 Grothendieck 解消与幂零切片](../concepts/partial-grothendieck-resolution-and-nilpotent-slice.md)

## 出处

- ch4 §2 部分消奇异；中译 p.73（英文 PDF p.79），源码 `chapters/ch04.tex:45`
