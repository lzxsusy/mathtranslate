# 命题 3.3.2 的证明：全化 + Barr–Beck–Lurie

> `cdm14/deriv/right-induction` · 轨道 C · 下降性质与归纳函子 · 状态 dev · 4 步

> **要回答的问题**：$\oblv^r$ 的左伴随为什么恰好是「沿群胚传递再推回」？

## 一句话

先用命题 3.1.3 把 $\Crys^r(X)$ 写成全化，再用 [Lu2] 的单子性判据与 [GR1] 的基变换把伴随对认出来。

## 目标

证明 (a) $\oblv^r_X$ 有左伴随 $\ind^r_X$；(b) $\oblv^r_X\circ\ind^r_X\simeq(p_t)_*^{\IndCoh}\circ p_s^!$；(c) 该伴随对单子。

## 前提

- 命题 3.1.3：$\Crys^r(X)\simeq\mathrm{Tot}(\IndCoh(X_\bullet/X_{\mathrm{dR}}))$。
- $p_s,p_t$ ind-固有，故 $p_i^!$ 有左伴随 $(p_i)_*^{\IndCoh}$（[GR1, 推论 2.8.3]）。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 把 $\oblv^r_X$ 写成全化的第 0 项投影，其左伴随是沿群胚的「归纳」。 | 全化是极限，左伴随逐项给出。 | `A p.28` | A·原文明确写了 |
| 2 | 计算复合：归纳后遗忘等于 $p_s^!$ 再 $p_t$-推前。 | Čech 神经的馀面/面映射给出这两个箭头。 | `A p.28` | A·原文明确写了 |
| 3 | 用 [Lu2, 定理 6.2.4.2]：连续、保守、余完备 ⇒ 单子性。 | Barr–Beck–Lurie 判据。 | `A p.28` | B·原文暗示、我们补的中间步 |
| 4 | 验证 Beck–Chevalley：余面映射有左伴随，且与 $!$-拉回交换。 | [GR1, 命题 2.9.2] 的 ind-固有基变换。 | `A p.28` | B·原文暗示、我们补的中间步 |

## 结论

$(\ind^r_X,\oblv^r_X)$ 是单子伴随，且 $\Crys^r(X)$ 是其模范畴。

## 缺口

- 第 4 步的 Beck–Chevalley 在原文中只是一句「验证」，具体的方形交换图与符号未写出。

## 最容易讲错的地方

- [Lu2, 6.2.4.2] 要求函子连续，$\oblv^r$ 的连续性来自全化是极限。
- 保守性用的是引理 2.3.12，不是 $\oblv^l$ 的保守性。

## 相关卡

[右晶体的归纳函子 $\ind^r_X$](../concepts/induction-right.md) · [无穷小群胚 $X\times_{X_{\mathrm{dR}}}X\rightrightarrows X$](../concepts/infinitesimal-groupoid.md) · [右晶体：$\Crys^r(X)=\IndCoh(X_{\mathrm{dR}})$](../concepts/right-crystal.md)

## 出处（印刷页）

- A p.28（A p.28）

> 说明：A=命题 3.3.2 的证明；B=[Lu2] 与 [GR1]；最没把握处：第 2 步的复合公式与原文 (3.3) 的对应。
