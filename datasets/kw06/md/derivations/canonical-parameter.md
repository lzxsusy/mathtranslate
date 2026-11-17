# 典范参数 Ψ：定义、S 作用与消去 t

> `kw/deriv/canonical-parameter` · 轨道 B · 扭化与拓扑 · 状态 dev · 4 步

> **要回答的问题**：为什么一族 $(\tau,t)$ 的 TQFT 实际只依赖一个组合 $\Psi$，且 $S$-对偶在 $\Psi$ 上仍是 Möbius 变换？

## 一句话

从拓扑项系数 eq (3.49) 出发，把 $t$ 与 $\tau$ 的组合定义为 $\Psi$ eq (3.50)；作用量写成 $I=\delta_tV+(i\Psi/4\pi)\int\mathrm{Tr}F\wedge F$，再用 $\delta'_t=\delta_t/\sqrt{1+t^2}$ 证明物理只依赖 $\Psi$，$S,T$ 在 $\Psi$ 上是 Möbius 变换。

## 目标

定义 $\Psi$，证明物理只依赖 $\Psi$，并给出 $S$ 与 $T$ 在 $\Psi$ 上的作用。

## 前提

- 扭化参数 $t$、耦合 $\tau$ 与拓扑项 $I_2$ eq (3.49) 见 `B p.35`。
- $S$ 在 $\tau$ 与 $t$ 上的作用 eq (3.13) 见 `B p.22`。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 把 $I_2$ 的系数 $-((t-t^{-1})/(e^2(t+t^{-1}))-i\theta/8\pi^2)$ 写成 $-\Psi/4\pi i$，即定义 eq (3.50)：$\Psi=(\tau+\bar\tau)/2+((\tau-\bar\tau)/2)(t-t^{-1})/(t+t^{-1})$。等价地 $\Psi=(\tau t^2+\bar\tau)/(1+t^2)$。 | 不引入 $\Psi$，$(\tau,t)$ 是两个独立参数，后面无法说清 S-对偶到底作用在什么上。 | `B p.35 eq (3.50)` | A·原文明确写了 |
| 2 | 作用量可写成 eq (3.51)：$I=\delta_tV+(i\Psi/4\pi)\int_M\mathrm{Tr}F\wedge F$。$\delta_tV$ 项在 $Q$-上同调中可去，故可观测量的相关函数只依赖 $\Psi$。 | 这一步给出「只依赖 $\Psi$」的第一层理由；但 $\delta_t$ 本身还带 $t$，必须再处理。 | `B p.36 eq (3.51)` | A·原文明确写了 |
| 3 | 重标定 $\delta'_t=\delta_t/\sqrt{1+t^2}$，使 $(\delta'_t)^2=-i\mathcal L_\sigma$ 与 $t$ 无关；各多重态化为 $\delta'_tU=V$、$\delta'_tV=-i\mathcal L_\sigma U$（Cartan 模型），于是 $t$ 只通过 $\Psi$ 进入。 | 不重标定，就还有 $\delta_t$ 定义里的 $t$-依赖，$t$ 与 $\Psi$ 无法解耦；这是整个论证最容易被跳过的一步。 | `B p.36` | A·原文明确写了 |
| 4 | 由 eq (3.50) 与 eq (3.52) 可得 $\Psi\to-1/(n_g\Psi)$（eq (3.54)）；$T$ 给 $\Psi\to\Psi+1$。故一般 $M=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ 作用为 eq (3.53)：$\Psi\to(a\Psi+b)/(c\Psi+d)$。 | 这一步说明 $S$-对偶在 $\Psi$ 上仍是 Möbius 变换，$\Psi$ 才是对偶群真正作用的坐标；$\tau$ 与 $t$ 只是它的分解。 | `B p.37 eq (3.53)` | A·原文明确写了 |

## 结论

$\Psi$ 把 $\tau$ 与 $t$ 合成一个复参数，作用量只含 $\Psi$ 与 $\delta_t$-恰当项，重标定后连 $\delta_t$ 的 $t$-依赖也被去掉，故 $(\tau,t)$ 族的物理由 $\Psi$ 完全决定。$S,T$ 仍按 Möbius 作用，且 $\Psi$ 取值于 $\mathbb{CP}^1$；这使后面的 S-对偶成为 $\Psi$ 上的一个变换，而不是两个参数的分别作用。

## 缺口

- 「只依赖 $\Psi$」是上同调层面的论证：原文未证明带算子的非拓扑关联函数也只依赖 $\Psi$。

## 最容易讲错的地方

- 把 $\Psi$ 与 $\tau$ 混为一谈：$\Psi$ 是 $\mathbb{CP}^1$ 上的复参数，可取 $\infty$，而 $\tau$ 始终在上半平面。
- 重标定 $\delta'_t$ 时忘记 $t=\pm i$ 处 $\sqrt{1+t^2}=0$：那里 $\Psi=\infty$，须改用齐次坐标单独处理。

## 相关卡

[一族拓扑场论：t ∈ CP¹ 与 Q² = 0](../derivations/one-parameter-family.md) · [Ψ 的特殊点与为什么必须是 GL 扭化](../derivations/psi-special-points.md) · [S-对偶](../concepts/s-duality.md) · [拓扑量子场论](../concepts/topological-qft.md)

## 出处（印刷页）

- B p.35–37（B p.35 eq (3.50)）

> 说明：A4：$\Psi$ 的定义、eq (3.51)、$\delta'_t$ 重标定与 Möbius 作用均在 `B p.35–37` 明写；最没把握处是「可观测量的相关函数只依赖 $\Psi$」被原文压缩成一句主张。
