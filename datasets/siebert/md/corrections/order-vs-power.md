# 「阶为 $a$」应为「满足 $\varphi^a=\mathrm{id}$」

> `siebert/correction/order-vs-power` ｜ 原书 p.26 ｜ draft

**一句话**：初版把「满足 $\varphi^a=\mathrm{id}$ 的自同构」译成「阶为 $a$ 的自同构」，把「$a$ 是某个周期」加强成「$a$ 是最小正周期」，例 2.3 可用的 $a$ 因此被无谓砍掉。

**自测**：「$\varphi^a=\mathrm{id}$」与「$\varphi$ 的阶为 $a$」差在哪里，为什么这个差别会影响例 2.3 的构造？

## 初版

```
取一个阶为 $a$ 的自同构 $\varphi$，即 $\varphi^a=\mathrm{id}$
```

## 改后

```
取一个满足 $\varphi^a=\mathrm{id}$ 的自同构 $\varphi$
```

## 为什么改

讲义原文（原书 p.26 例 2.3）作「Take φ to be any automorphism such that φ^a = id」，条件只是「$a$ 是 $\varphi$ 的一个周期」。记 $\operatorname{ord}(\varphi)=d$（最小正周期），则 $\varphi^a=\mathrm{id}\iff d\mid a$；写成「阶为 $a$」等于断言 $d=a$，于是 $a=2d,3d,\dots$ 这些同样合法的取法被排除。这不是措辞问题而是条件变了：例 2.3 只用两件事——$\mathbb{Z}/a$ 经 $(\varphi,\zeta)$ 作用在 $C_0\times\mathbb{G}_m$ 上，以及 $\zeta$ 是本原 $a$ 次单位根（这要求 $a\ge2$）。当 $\operatorname{Aut}(C_0)=(\mathbb{Z}/2)^2$ 时，按「阶为 $a$」只剩 $a=1,2$ 可选，而 $a=1$ 又因 $\zeta$ 须本原而被排除，最后只剩 $a=2$；按原文条件则 $a$ 可取任意偶数，构造的自由度大得多。依据：讲义原句 + 群论中「元素的阶 = 最小正周期」这一通行定义（本条的校订记录记为 ch02.tex:59）。

## 补注

同类措辞在别处要逐处核对：只有原文明确写「of order $a$」时才可译「阶为 $a$」。本卡只覆盖例 2.3 这一处，不要推广到别处。

## 易错点

- 不要把它当润色：$\varphi^a=\mathrm{id}$ 是弱条件，「阶为 $a$」是强条件，后者把 $a$ 为阶的倍数时全部排除。
- 改后必须保留公式 $\varphi^a=\mathrm{id}$：只写「满足条件的自同构」会让 $a$ 无处定义，后文的 $\zeta$ 与 $\mathbb{Z}/a$ 作用就接不上。
- 中文「阶为 $a$」默认指最小正周期，与原文的「any automorphism such that」明确不合；若想保留「阶」字，只能写成「$a$ 是 $\varphi$ 的周期的倍数」。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，校订，p.26–26（原书 p.26）

关联：`siebert/concept/moduli-space`、`siebert/deriv/dm-stack-from-groupoid`、`siebert/concept/stable-curve`

来源说明：据第 2 章校订记录（ch02.tex:59，已 applied）与讲义原 PDF p.26 例 2.3 的英文原句逐字核对；「阶 = 最小正周期」按群论通行定义，未另取外部条目。
