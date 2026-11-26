# 从截断读到 Langlands 对应：迹公式如何给出 $\sigma_\pi$

> `lafforgue02/deriv/trace-from-truncation` · 轨道 A · 镜像对称与几何 Langlands · 状态 dev · 4 步

> **要回答的问题**：迹公式只给出迹的相等，怎样从迹的相等得到「每个 $\pi$ 恰好对应一个 $\sigma$」？

## 一句话

把迹公式右端的 $\mathrm{Tr}_\pi(f)$ 与左端的几何迹比对，逐个 $\pi$ 得到 $H_\pi$；再由 $H_\pi\cong q'^*\sigma\otimes q''^*\check\sigma$ 认出 $\sigma_\pi$，最后用 Chebotarev 得整体双射。

## 目标

复原第 II 章末段：从迹公式到 (ii)$_r$ 的唯一性，再到 (i)$_r$ 的双射。

## 前提

- 迹公式：$\Tr_{H_{N,\mathrm{cusp}}}(f\times\Frob_x^{-s/\deg x})=q^{(r-1)s}\sum_\pi\Tr_\pi(f)(\cdots)$。
- 已知 $r-1$ 时的对应 $\pi'\mapsto\sigma_{\pi'}$（归纳假设）。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 对每个 $\pi\in\{\pi\}^N_r$，由迹公式的存在性得到 $W_{(X-N)\times(X-N)}\rtimes\mathbb Z$ 的表示 $H_\pi$，纯权 $0$，其迹由两个局部和给出。 | 把右端按 $\pi$ 分解，每个 $\pi$ 贡献一个不可约分量；纯性由前一条推导保证。 | `A p.18` | A·原文明确写了 |
| 2 | 认出 $H_\pi$：由 $r-1$ 的已知对应与局部因子匹配，得 $H_\pi\cong q'^*\sigma\otimes q''^*\check\sigma$，其中 $\sigma$ 是某个 $r$ 维 Weil 表示。 | 两个局部和分别是 $\infty$ 与 $0$ 处的特征值，恰是 $\sigma$ 在两个位点的局部因子的形状。 | `A p.19` | A·原文明确写了 |
| 3 | 故每个 $\pi$ 给出 $\sigma_\pi$；反向由 Galois 侧构造给出（归纳假设下），得双射 (i)$_r$。 | 反向构造用的是同一套 chtouca 上同调在 Galois 表示侧的版本。 | `A p.19` | A·原文明确写了 |
| 4 | Chebotarev 密度定理把「迹函数相等」升级为「表示同构」，从而 (ii)$_r$ 的逐位点匹配成立。 | 两个半单表示若在所有 Frobenius 上的迹相同则同构；密度定理保证 Frobenius 足够多。 | `A p.4` | A·原文明确写了 |

## 结论

(i)$_r$ 与 (ii)$_r$ 同时得证：双射由 $\pi\mapsto H_\pi\cong q'^*\sigma_\pi\otimes q''^*\check\sigma_\pi$ 给出，局部匹配由局部因子的形状与 Chebotarev 给出。

## 缺口

- 本卡只复述讲义的证明路线；讲义对「反向构造」只给一句话，细节在 [Lafforgue 2002]。

## 最容易讲错的地方

- Chebotarev 用的是「所有 Frobenius 上的迹」，不是「一个 Frobenius 的迹」；只在一个 $x$ 上比对不足以定出表示。
- $H_\pi$ 是 $W_{(X-N)\times(X-N)}\rtimes\mathbb Z$ 的表示，不是 $W_F$ 的；把 $\sigma_\pi$ 直接读成 $H_\pi$ 会丢一层。

## 相关卡

[本质同调上的迹公式](../concepts/trace-formula-essential-cohomology.md) · [函数域上的 Langlands 对应（$\mathrm{GL}_r$）](../concepts/langlands-correspondence-function-field.md) · [为什么本质部分集中在中间次数 $2r-2$](../derivations/essential-part-in-middle-degree.md)

## 出处（印刷页）

- A p.18–19（A p.19）

> 说明：第 1–3 步取讲义 p.18–19（A 级）；第 4 步的 Chebotarev 用法见 p.4 与 p.8。
