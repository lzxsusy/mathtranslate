# GL 扭化的构造：选哪个 Spin(4)

> `kw/deriv/twist-construction` · 轨道 B · 扭化与拓扑 · 状态 dev · 4 步

> **要回答的问题**：GL 扭化到底改了哪个对称群，为什么这个选择能给出 $Q^2=0$ 的标量超荷？

## 一句话

从弯曲四维流形上需要标量超荷出发，选同态 $\kappa$ 把 $\mathrm{Spin}(4)$ 嵌入 $\mathrm{Spin}(6)$，使 4 与 6 按 $(2,1)\oplus(1,2)$ 与 $(2,2)\oplus(1,1)$ 分解，得到不变旋量 $\varepsilon_\ell,\varepsilon_r$ 与标量超荷 $Q=uQ_\ell+vQ_r$。

## 目标

构造 GL 扭化：选出 $\kappa$，得到不变超荷与扭化后的场内容。

## 前提

- 在任意四维流形上构造 TQFT 需要一个标量超荷 $Q$ 且 $Q^2=0$，见 `B p.16`。
- $N=4$ 的对称群为 $\mathrm{Spin}(4)\times\mathrm{Spin}(6)$，六个标量构成 $6_v$，见 `B p.19`。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 扭化指用 $\mathrm{Spin}(4)\times\mathrm{Spin}(6)$ 中与 $\mathrm{Spin}(4)$ 同构的 $\mathrm{Spin}'(4)$ 替换 $\mathrm{Spin}(4)$：它在 $\mathbb R^4$ 上作用不变，但改变 $N=4$ 各场按新群的表示。这样原来的旋量超荷对新群可以变成标量。 | 不换群就无法把旋量型超荷变成标量，弯曲流形上的守恒超荷也就无从定义。 | `B p.17` | A·原文明确写了 |
| 2 | 取 $\kappa:\mathrm{Spin}(4)\to\mathrm{Spin}(6)$，令 $\mathrm{Spin}'(4)=(1\times\kappa)(\mathrm{Spin}(4))$；要求 $\kappa$ 使 4 按 $(2,1)\oplus(1,2)$ 变换，即分块对角嵌入 eq (3.2)。 | $\kappa$ 的选取决定哪些超荷存活；选错嵌入就没有不变旋量，扭化退化。 | `B p.18 eq (3.2)` | A·原文明确写了 |
| 3 | 该嵌入使 4 与 $\bar4$ 分别带 $K=\pm1$ 的 $U(1)$ 荷，且 $6_v=\wedge^2 4=(2,2)_0\oplus(1,1)_2\oplus(1,1)_{-2}$。于是六个标量分为 $4_v$ 的 $\varphi_\mu$ 与 $K=\pm2$ 的 $\sigma,\bar\sigma$。 | 这一步把「扭化后的场内容」定下来：$\sigma,\bar\sigma$ 的 $K$ 荷决定后面 $\delta_T\sigma=0$，不能跳过。 | `B p.19` | A·原文明确写了 |
| 4 | 不变旋量满足 $\Gamma_{0145}\varepsilon=\varepsilon$、$\Gamma_{2367}\varepsilon=\varepsilon$、$\Gamma_{89}\varepsilon=-i\varepsilon$ eq (3.11)，且 $\varepsilon_\ell,\varepsilon_r$ 的 $K$ 本征值相同；任意 $\varepsilon=u\varepsilon_\ell+v\varepsilon_r$ 给 $Q=uQ_\ell+vQ_r$，由 (2.15) 右端无 $\mathrm{Spin}'(4)$-不变算符得 $Q^2=0$。 | 若两个不变旋量的 $K$ 不同，它们的线性组合不再不变，$Q$ 也失去标量性；$K$ 相同是这一构造的关键。 | `B p.21 eq (3.11)` | A·原文明确写了 |

## 结论

取 $\kappa$ 后 4 与 6 的分解确定，得到两个 $K$ 荷相同的不变旋量，其线性组合给出标量超荷 $Q$ 且 $Q^2=0$。扭化后的玻色场为 $A,\varphi,\sigma,\bar\sigma$，其中 $\sigma$ 带 $K=\pm2$，为 §3.2 的一族方程与 §3.4 的作用量作准备。

## 缺口

- 扭化后的理论为何是 TQFT，原文明说要到 §3.4 用曲面上作用量的 $\delta_t$-恰当性才证明，这里先搁置。

## 最容易讲错的地方

- 把扭化理解成「改变 $N=4$ 理论」：作用量与场内容不变，变的是按哪个 $\mathrm{Spin}'(4)$ 解读。
- 把 $6_v$ 的分解错记成 $(2,2)\oplus(1,3)$：$K=\pm2$ 的是两个 $\mathrm{SO}(4)$ 标量，不是三重态。

## 相关卡

[拓扑扭化](../concepts/topological-twist.md) · [拓扑量子场论](../concepts/topological-qft.md) · [一族拓扑场论：t ∈ CP¹ 与 Q² = 0](../derivations/one-parameter-family.md) · [$\mathcal N=4$ 超对称杨–米尔斯理论](../concepts/n4-sym-theory.md)

## 出处（印刷页）

- B p.17–22（B p.21 eq (3.11)）

> 说明：A4：扭化定义、$\kappa$ 的选取、$6_v$ 分解与 eq (3.11) 均在 `B p.17–21` 明写；最没把握处是「$Q^2=0$ 由 (2.15) 右端无不变算符」这一句在 p.18 的语境与 eq (3.11) 的衔接。
