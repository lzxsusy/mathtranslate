# 「平坦局部」应为「平展局部」

> `siebert/correction/etale-vs-flat-local` ｜ 原书 p.33 ｜ draft

**一句话**：初版把 étale locally 译成「平坦局部」，丢掉「非分歧」这一半，等于把平展拓扑换成平坦拓扑；本章的层条件与下降全是按平展拓扑写的。

**自测**：为什么命题 2.3 的证明里只能写「平展局部」，写成「平坦局部」在数学上错在哪里？

## 初版

```
可以在使主丛平凡的平坦局部计算
```

## 改后

```
可以在使主丛平凡的平展局部计算
```

## 为什么改

讲义原文（原书 p.33，命题 2.3 的证明）作「It is enough to check étale locally on B」。étale 与 flat 是两个不同的条件：étale = 局部有限型 + 平坦 + 非分歧（nLab「étale morphism」，last revised 2025-01-30；讲义定义 2.6 的形式刻画是提升「存在且唯一」——非分歧给「至多唯一」，光滑性给「存在」）。丢掉「非分歧」就等于把局部化换成更粗的平坦拓扑，要检验的范围随之变大。在这本讲义里这一步是承重的：叠的定义（定义 2.5(1)）只要求 $\operatorname{Iso}_B(X,X')$ 是平展拓扑下的层，而注 2.6 明说 $\operatorname{Iso}_B$ 虽然有限、非分歧，却一般并不平坦——也就是说它未必满足平坦（fpqc）下降。命题 2.3 的证明先在一个平展局部把 $G$-主丛平凡化，算出 $\operatorname{Iso}_B(f,f')\cong B\times_{X\times_SX}(G\times_SX)$（式 (2.46)），再用平展下降拼回叠的层；若把局部化换成平坦覆盖，就先默认了 $\operatorname{Iso}_B$ 满足 fpqc 下降，而这一点恰好没有依据。

## 补注

同页附近的另一处同组术语改动是「没有分歧」→「非分歧」（ch02.tex:232，属 p.32）。「平展」是 étale 的通行译名，保留；本卡只改「平坦局部」这一处，不要把全书所有「平坦」都换成「平展」——$G$ 平坦、$\omega_{C/S}$ 平坦这些是另一回事。

## 易错点

- 不要因为命题 2.3 的假设里有「$G$ 是平坦群概形」，就把局部化也写成「平坦局部」：假设讲的是 $G$，局部化讲的是拓扑，两者层次不同。
- étale locally 也不能改译成「Zariski 局部」：$G$-主丛在 Zariski 局部一般不能平凡化，结点曲线在 Zariski 局部也看不出 $V(zw)$ 的形状。
- 反过来也不能把所有「平坦」都改成「平展」：平坦性本身在本章反复作为假设出现（例如「$\operatorname{Iso}_B$ 一般并不平坦」这条提醒），改错方向会毁掉另一个条件。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，校订，p.33–33（原书 p.33）

关联：`siebert/concept/etale-local`、`siebert/concept/representable-morphism`、`siebert/deriv/dm-stack-from-groupoid`

来源说明：据第 2 章校订记录（ch02.tex:272，已 applied）与讲义原 PDF p.33 命题 2.3 证明的英文原句「It is enough to check étale locally on B」核对；étale = 局部有限型 + 平坦 + 非分歧 按 nLab「étale morphism」（last revised 2025-01-30）与「étale topology」（2020-04-06）；层与下降的条件按讲义定义 2.5 与 Stacks Project tag 026F（定义 8.4.1）。
