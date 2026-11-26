# 平均函子为什么 $t$-正合：式 (5)(6) 的用法

> `sandvik25/deriv/iw-averaging-t-exact` · 轨道 C · Iwahori–Whittaker 侧 · 状态 dev · 5 步

> **要回答的问题**：为什么「标准层到标准层」加上「一部分单层为零」就足以推出 $t$-正合，而不是只推出有界性？

## 一句话

$\mathrm{Av}^{\mathrm{IW}}=\Delta^{\mathrm{IW}}_0\star_I(-)$ 把标准层送到标准层、余标准层送到余标准层（式 (6)），并把非极小胞腔的单层打成零（式 (5)）；由反常 $t$-结构的「标准–余标准判别法」即得 $t$-正合性。

## 目标

由式 (5)(6) 推出定理 4.4.1(1) 的 $t$-正合性与 (2) 的「穿过反球商」。

## 前提

- 反常 $t$-结构由标准层/余标准层刻画：一个复形属于 $\mathcal D^{\le0}$ 当且仅当其反常上同调层都满足某些「标准层判别」条件。
- 式 (5)：$\mathrm{Av}^{\mathrm{IW}}(\mathrm{IC}_w)=0$ 除非 $w\in\widetilde W_{\mathrm{ext}}$。
- 式 (6)：$\mathrm{Av}^{\mathrm{IW}}(\Delta_w)\cong\Delta^{\mathrm{IW}}_\lambda$、$\mathrm{Av}^{\mathrm{IW}}(\nabla_w)\cong\nabla^{\mathrm{IW}}_\lambda$（$\lambda$ 由 $W\cdot w=W\cdot w_\lambda$ 定）。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 注意 $\mathrm{Av}^{\mathrm{IW}}=\Delta^{\mathrm{IW}}_0\star_I(-)$ 是右卷积，故它是正合（triangulated）函子；问题只在于它把反常 $t$-结构送到哪里。 | 卷积本身是三角函子，所以只需在反常层生成元上检验 $t$-级别的行为。 | `A p.10` | A·原文明确写了 |
| 2 | 在标准层上：$\Delta_w\mapsto\Delta^{\mathrm{IW}}_\lambda$，仍是反常层（次数 $0$）；在余标准层上同理仍是反常层。 | 这是式 (6)；它保证「反常层的像仍在反常层」，即 $\mathrm{Av}^{\mathrm{IW}}$ 把 $\mathcal D^{\le0}$ 送到 $\mathcal D^{\le0}$、$\mathcal D^{\ge0}$ 送到 $\mathcal D^{\ge0}$。 | `A p.10` | A·原文明确写了 |
| 3 | 在单层上：$\mathrm{IC}_w\mapsto0$（$w\notin\widetilde W_{\mathrm{ext}}$）或非零（$w\in\widetilde W_{\mathrm{ext}}$），两种情形都不产生负/正次数污染。 | 式 (5) 处理了「单层被打成零」这一唯一可能破坏 $t$-正合的情形。 | `A p.10` | A·原文明确写了 |
| 4 | 由「标准–余标准判别法」及反常层的生成性，上述三条合起来即 $\mathrm{Av}^{\mathrm{IW}}$ 反常 $t$-正合。 | 这正是原文「basic homological algebra allows one to deduce from 5 and 6」的具体含义。 | `A p.10` | A·原文明确写了 |
| 5 | 再由式 (5)：被 $\mathrm{Av}^{\mathrm{IW}}$ 打成零的单层恰是 $w\notin\widetilde W_{\mathrm{ext}}$ 那些，正是反球商 $\mathcal P_I\to\mathcal P_I^{\mathrm{asph}}$ 所商的 Serre 子范畴的生成元，故 $\mathrm{Av}^{\mathrm{IW}}$ 穿过反球商。 | 这是 (2) 的一半；另一半（全忠实）靠造截面，不在本推导范围内。 | `A p.10` | A·原文明确写了 |

## 结论

$t$-正合性 = 式 (6) 保证「像仍是反常层」+ 式 (5) 保证「少数单层为零不破坏判别」；穿过反球商 = 式 (5) 杀掉的那批恰是商掉的 Serre 子范畴。

## 缺口

- 「标准–余标准判别法」原文未写出具体表述，只称「基础同调代数」。
- 全忠实性（(2) 的另一半）另需构造截面，原文只给直观描述，本推导不覆盖。

## 最容易讲错的地方

- 式 (5) 只在 $w\notin\widetilde W_{\mathrm{ext}}$ 时给零；$\widetilde W_{\mathrm{ext}}$ 上的单层像一般非零且非单层，不能推出「单层到单层」。
- 把 $t$-正合性理解成「逐点正合」：这里的 $t$ 是反常 $t$-结构，不是通常的 $\mathrm{Coh}$ 或 $\mathbb Q_\ell$-层 $t$-结构。

## 相关卡

[IW 平均函子 $\mathrm{Av}^{\mathrm{IW}}$（定理 4.4.1）](../concepts/iw-averaging.md) · [反球商 $\mathcal P_I^{\mathrm{asph}}$](../concepts/antispherical-quotient.md) · [IW 反常层的最高权结构（命题 4.3.1）](../concepts/iw-highest-weight.md)

## 出处（印刷页）

- A p.10（A p.10）

> 说明：式 (5)(6) 与证明梗概全在 p.10；本推导把「basic homological algebra」一句展开成五步。
