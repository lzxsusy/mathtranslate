# 把 LLC 从超尖点归纳到一般表示：rec_n = ⊕ Sp_{m_i} ∘ rec_{n_i}

> `yao17/deriv/induction-to-supercuspidal` · 轨道 分类与不变量 · 状态 dev · 4 步

> **要回答的问题**：定理 2.13 为什么只需在超尖点上验证？一般 π 的 rec_n(π) 是怎么由各段的超尖点数据拼出来的？

## 一句话

由 BZ 把 π 写成 Q(Δ₁,…,Δ_r)，再对每个段用 Sp_{m_i}(rec_{n_i}(π_i))，底层 ρ 是 rec_{n_i}(π_i)(j) 的直和。

## 目标

证明 §3.1.7：只需在 $\Asc_n\to\mathcal G_n^{\mathrm{irr}}$ 上构造 $\rec_n$，一般情形由 BZ 分类唯一确定。

## 前提

- $\pi=Q(\Delta_1,\dots,\Delta_r)$ 是 BZ 分类下的标准表示，$\Delta_i=\Delta_i(\pi_i,m_i)$ 是 Zelevinsky 段，$\pi_i$ 是 $\GL_{n_i}(K)$ 的超尖点表示，$n=\sum_i n_i m_i$。
- $\Sp_m$ 是 $\GL_m$ 的 Steinberg 表示在 LLC 下的像；$\rec_{n_i}(\pi_i)=\rho_i$。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 由定理 3.1（BZ 分类），每个 $\pi\in\mathcal G_n^{\mathrm{irr}}$ 唯一写成 $Q(\Delta_1,\dots,\Delta_r)$，其中 $\Delta_i=\Delta_i(\pi_i,m_i)$ 且 $\pi_i$ 超尖点、$n_i m_i=n$ 分配。 | 这一步把「一般表示」化归为「超尖点 + 段长」的有限数据，是归纳的出发点。 | `A p.26` | A·原文明确写了 |
| 2 | 定义 $\rec_n(\pi):=\bigoplus_i\Sp_{m_i}(\rec_{n_i}(\pi_i))$。右边只依赖超尖点的 $\rec_{n_i}(\pi_i)$ 与段长 $m_i$。 | 这是「把 $\Sp_m$ 看成 $W_K\times\SL_2$ 的表示」的直接用法：段长 $m$ 变成 $\Sp_m$ 的维数。 | `A p.26` | A·原文明确写了 |
| 3 | 写出底层 $W_K$ 表示：$\rho=\bigoplus_i\bigoplus_{j=0}^{m_i-1}\rec_{n_i}(\pi_i)(j)$，即每个 $\rec_{n_i}(\pi_i)$ 取 $j=0,\dots,m_i-1$ 的全部整数扭转。 | $\Sp_m$ 作为 $W_K\times\SL_2$ 表示在 $W_K$ 上正是 $\bigoplus_{j=0}^{m-1}$ 的扭转链，这一步把 $\rec_n(\pi)$ 从「$\SL_2$ 的表示」落回「一对 $(\rho,N)$」。 | `A p.26` | A·原文明确写了 |
| 4 | 验证与引理 2.11/2.12 相容：若各段两两不相连（$\Delta_i$ 与 $\Delta_j$ 不 linked），$Q(\Delta_1,\dots,\Delta_r)$ 不可约，$\rec_n$ 的直和分解与不可约性一致；若相连，则取唯一不可约商，对应取 $\Sp_{m}$ 的更大段。 | 这一步保证归纳定义与「诱导是否不可约」的判据不冲突——即 $\rec_n$ 在 $\pi$ 不可约时确实给出不可约的 $(\rho,N)$。 | `A p.26` | A·原文明确写了 |

## 结论

$\rec_n(\pi)=\bigoplus_i\Sp_{m_i}(\rec_{n_i}(\pi_i))$，底层 $\rho=\bigoplus_i\bigoplus_{j=0}^{m_i-1}\rec_{n_i}(\pi_i)(j)$。故定理 2.13 的构造只需在 $\Asc_n$（超尖点）上给出 $\rec_n$，一般情形由 BZ 分类唯一延拓。

## 缺口

- 第 4 步「相连时取更大段」底本只作一句带过，未给 $\Sp_m$ 与 Zelevinsky 段的逐项对应。
- 「唯一延拓」的相容性（与 BZ 分类的唯一性一致）底本未证，只说「由 BZ 分类唯一确定」。

## 最容易讲错的地方

- 底层 $\rho$ 的扭转取 $j=0,\dots,m_i-1$，而 p.25 的超尖点支撑排版只写到 $j=1,\dots,m_i-1$（漏了 $j=0$）；按定义应为 $j=0$ 起，译本已在译注中点明。
- $\Sp_{m_i}(\rec_{n_i}(\pi_i))$ 是 $W_K\times\SL_2$ 的表示，不是 $W_K$ 的；写成 $\rho$ 时必须把 $\SL_2$ 的权展开成扭转链，否则会少算因子。
- $n=\sum_i n_i m_i$ 是对全部段求和，不是对 $i$ 取 $n_i$ 之和；漏掉 $m_i$ 会让 $\dim\rho$ 与 $n$ 对不上。

## 相关卡

[定理 3.1：Bernstein–Zelevinsky 对 GL_n 容许表示的七条分类](../concepts/bz-classification.md) · [Zelevinsky 段 Δ(π,m)、linked/precedes 与 (∗) 条件](../concepts/zelevinsky-segment.md) · [局部 Langlands 对应：定理 2.13 的五条性质](../concepts/llc-statement.md) · [GL₂ 的四类表示如何对应到 Weil–Deligne 表示](../derivations/gl2-llc-cases.md)

## 出处（印刷页）

- A p.26（A p.26）

> 说明：公式与底层 $\rho$ 的扭转链取自 p.26 的 3.1.7；第 4 步的相容性是我们的整理。
