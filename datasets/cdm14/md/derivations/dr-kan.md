# dR 与极限交换、左 Kan 延拓表述

> `cdm14/deriv/dr-kan` · 轨道 A · de Rham 预栈与晶体定义 · 状态 dev · 3 步

> **要回答的问题**：为什么 $\mathrm{dR}$ 可以「不需要知道」DG 概形而直接由公式定义？

## 一句话

从逐对象定义直接读出 dR 保极限，再把左 Kan 延拓写成逐对象余极限。

## 目标

证明 $\mathrm{dR}$ 保极限/余极限，且 $\mathrm{dR}|_{\DGSch_{\mathrm{aff}}}$ 沿 $\DGSch_{\mathrm{aff}}\hookrightarrow\PreStk$ 是左 Kan 延拓。

## 前提

- $\PreStk$ 是函子范畴，极限与余极限逐对象计算。
- $\mathrm{dR}$ 逐对象定义为 $Y\mapsto (S\mapsto Y({}^{\mathrm{cl,red}}S))$。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 把 $\mathrm{dR}$ 写成复合 $\mathrm{ev}\circ(\mathrm{cl,red})^*$：先沿 ${}^{\mathrm{cl,red}}$ 拉回，再取值。 | 定义逐对象进行，复合结构决定函子性。 | `A p.12` | A·原文明确写了 |
| 2 | 拉回与取值都逐对象、保所有极限与余极限，故 $\mathrm{dR}$ 保极限与余极限。 | 函子范畴中的 (co)limit 逐对象计算。 | `A p.12` | A·原文明确写了 |
| 3 | 左 Kan 延拓在逐对象层面就是把 $\mathrm{dR}$ 在 $\DGSch_{\mathrm{aff}}$ 上的值沿余极限延拓，得到的正是同一公式。 | 左 Kan 延拓 = 逐对象余极限（[Lu0] 的普遍事实）。 | `A p.12` | B·原文暗示、我们补的中间步 |

## 结论

$\mathrm{dR}$ 与极限、余极限交换；$\mathrm{dR}|_{\DGSch_{\mathrm{aff}}}$ 沿包含是左 Kan 延拓，故 $\mathrm{dR}$ 由其在仿射 DG 概形上的值唯一决定。

## 缺口

- 第 3 步引用 [Lu0] 中「左 Kan 延拓 = 逐对象余极限」的一般事实，原文只说「这是对的」。

## 最容易讲错的地方

- 保余极限不等于保极限：这里两者都保，是因为 $\mathrm{dR}$ 逐对象复合。
- 左 Kan 延拓沿的是 $\DGSch_{\mathrm{aff}}\hookrightarrow\PreStk$，不是沿 $\mathrm{redSch}_{\mathrm{aff}}\hookrightarrow\DGSch_{\mathrm{aff}}$（后者是引理 1.1.7）。

## 相关卡

[de Rham 预栈 $X_{\mathrm{dR}}$](../concepts/dr-prestack.md) · [局部几乎有限型（laft）与 $Y_{\mathrm{dR}}$ 的正性](../concepts/laft-and-dr.md)

## 出处（印刷页）

- A p.12（A p.12）

> 说明：A=引理 1.1.4 与推论 1.1.5 的原文；B=左 Kan 延拓的普遍事实；最没把握处：第 1 步的复合写法是我为讲清结构补的。
