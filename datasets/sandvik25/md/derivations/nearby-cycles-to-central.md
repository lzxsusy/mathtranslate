# 从附近循环造出中心函子，并证明它 $t$-正合

> `sandvik25/deriv/nearby-cycles-to-central` · 轨道 A · 中心层与 Wakimoto 层 · 状态 dev · 4 步

> **要回答的问题**：中心函子的 $t$-正合性，究竟由哪条性质、在哪一步用上？

## 一句话

把 $Z(\mathcal F)=\Psi_f(\mathcal F\boxtimes k_{\mathbb C^\times}[1])$ 拆成「张量一个常层」与「附近循环」两步：前者显然 $t$-正合，后者由命题 2.2.2(2) 提供 $t$-正合性。

## 目标

从 $\Psi_f$ 的定义与五条性质，推出 $Z$ 是反常 $t$-正合的幺半函子。

## 前提

- $\mathrm{Gr}^{\mathrm{cen}}_G$ 带正则映射 $f$，一般纤维 $\mathrm{Gr}_G\times\mathbb C^\times$、特殊纤维 $\mathrm{Fl}_G$（§2.3）。
- $\Psi_f\colon\mathcal D^b_c(X^\times)\to\mathcal D^b_c(X^0)$，$\mathcal F\mapsto(i^*j_*\exp_{X*}\exp_X^*\mathcal F)[-1]$（定义 2.2.1）。
- 命题 2.2.2：(1) 保可构造；(2) perverse $t$-正合；(3) 光滑基变换；(4) 紧合基变换；(5) 投影的常层特殊化为原层。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 先看 $\mathcal F\mapsto\mathcal F\boxtimes k_{\mathbb C^\times}[1]$：它在 $\mathrm{Gr}_G\times\mathbb C^\times$ 上把反常层映到「反常层张量常层的一次平移」，是 $t$-正合的。 | 常层 $k_{\mathbb C^\times}[1]$ 是 perverse 的（$\mathbb C^\times$ 是 $1$ 维光滑，$[1]$ 恰把它摆到反常次数 $0$），与它作外积不改变反常 $t$-结构。 | `A p.3` | A·原文明确写了 |
| 2 | 再取 $\Psi_f$：由命题 2.2.2(2)，$\Psi_f$ 本身 perverse $t$-正合，故两步复合仍 $t$-正合，得 $Z$ 的 (2)。 | 这是唯一需要「非平凡输入」的一步：$\Psi_f$ 的 $t$-正合性不是自动的，正因为 $\exp_X$ 不是代数映射（脚注 4），才要单独立命题。 | `A p.3–4` | A·原文明确写了 |
| 3 | 幺半性：对 $\mathcal F,\mathcal G$ 用定义与 $\Psi_f$ 的乘法性质，把 $Z(\mathcal F)\star_I Z(\mathcal G)$ 与 $Z(\mathcal F\star\mathcal G)$ 都化成对 $\mathcal F\boxtimes\mathcal G$ 的一次附近循环，再用卷积的紧合基变换对齐。 | 原文把 (1) 归给「与 (5) 同法」，核心工具是命题 2.2.2(3)(4) 的两种基变换。 | `A p.4` | A·原文明确写了 |
| 4 | 结论：$Z$ 是 $t$-正合幺半函子；「像落在中心」(3) 另需一句「卷积可交换」的直接验证，原文未展开。 | (1)(2) 到这里就证完了；(3)(4) 是额外结构，本推导不覆盖。 | `A p.4` | A·原文明确写了 |

## 结论

$Z$ 的 $t$-正合性 = 「张量常层」的显然 $t$-正合性 $\circ$ 命题 2.2.2(2)；幺半性 = 两次基变换。

## 缺口

- (3) 落在中心、(4) 两次卷积仍反常，原文均只作断言；本推导只覆盖 (1)(2) 的链条。

## 最容易讲错的地方

- 把 $[1]$ 平移漏掉：$k_{\mathbb C^\times}$ 不经 $[1]$ 不是 perverse 的，第一步就不再 $t$-正合。
- $\Psi_f$ 的 $t$-正合性方向是「反常 → 反常」，不是「通常 $t$-结构 → 通常 $t$-结构」；两者不可混用。

## 相关卡

[附近循环函子 $\Psi_f$](../concepts/nearby-cycles.md) · [Gaitsgory 中心函子 $Z$](../concepts/gaitsgory-central-functor.md) · [Wakimoto 滤链的重数如何变成 $\dim V_\lambda$](../derivations/wakimoto-multiplicity.md)

## 出处（印刷页）

- A p.2–4（A p.4）

> 说明：$\Psi_f$ 的性质在 p.2–3，$Z$ 的定义与定理 2.4.1 在 p.3–4；本推导把定理证明中分散的依据串成一条链。
