# 从 4d $\mathcal N=4$ 到 2d $\sigma$-模型

> `gtgl15/deriv/compactify-to-sigma` · 轨道 总览 · 状态 dev · 4 步

> **要回答的问题**：怎样从 4d $\mathcal N=4$ 的场论逐步得到靶空间为 $\MH$ 的二维 $\sigma$-模型，并说清这个大 $\Sigma$ 近似的适用范围？

## 一句话

在 $\Sigma\times C$（$\Sigma\gg C$）上紧致化：$C$ 方向零模是 Hitchin 方程解，$\Sigma$ 方向有效理论是靶为 $\MH$ 的 2d $\sigma$-模型。

## 目标

把 4d $\mathcal N=4$ 在 $\Sigma\times C$ 上的低能有效理论识别为 2d $\sigma$-模型，靶空间为 $C$ 上希格斯丛模空间 $\MH$。

## 前提

- 4d $\mathcal N=4$ 超杨–米尔斯：$A_\mu$ 与 6 个伴随标量 $\varphi_i$，16 超荷，耦合 $\tau$（§1、§2.1）。
- 时空取 $\Sigma\times C$，$C$ 是亏格 $g\ge2$ 的紧 Riemann 面，$\Sigma$ 的尺度远大于 $C$。
- $C$ 方向的超对称真空由 Hitchin 方程 eq (2.1) 刻画，解空间为 $\MH$。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 把 4d 场按 $C$ 上的形式分解：$A_\mu$ 给 $C$ 上的联络 $A$，6 个标量中两个组合成 $C$ 上取值于 $K$ 的 $(1,0)$-形式 $\varphi$（其余被 twist 吸收）。 | 这是拓扑扭曲后的场内容，也是 Hitchin 对 $(E,\varphi)$ 的来源。 | `A p.4 eq (2.1)` | A·原文明确写了 |
| 2 | 令 $\Sigma$ 方向动量/涨落为零，$C$ 方向要求超对称基态：$F_{z\bar z}-[\varphi_z,\varphi_{\bar z}]=0$、$D_{\bar z}\varphi_z=D_z\varphi_{\bar z}=0$。 | BPS 方程就是 Hitchin 方程，其解集即 $\MH$。 | `A p.4 eq (2.1)` | A·原文明确写了 |
| 3 | 零模空间 $\MH$ 上的 $L^2$ 度规作为 2d 非线性 $\sigma$-模型的作用量度规（eq (2.3)）。 | 模空间度规就是低能有效作用量的动能项。 | `A p.6 eq (2.3)` | A·原文明确写了 |
| 4 | $\Sigma$ 足够大时，$C$ 方向的高频模式质量 $\gtrsim1/\mathrm{vol}(C)$，只有零模在低能存活，故得到 2d $\sigma$-模型。 | 这是“$\Sigma\gg C$”的定量含义。 | `A p.2` | B·原文暗示、我们补的中间步 |

## 结论

低能有效理论是靶为 $\MH$ 的 2d $\sigma$-模型；$\sigma$-模型只在 $\MH$ 的一般点有效，在规范对称增强的奇点处失效。

## 缺口

- 第 4 步的尺度论证原文只给直觉（“$\Sigma$ 大”），没有逐阶匹配有效作用量的推导。
- $\mathcal N=4$ 的拓扑扭曲与部分拓扑场论的合法性原文脚注 `partial`（p.3）承认不完整。

## 最容易讲错的地方

- $\Sigma$ 与 $C$ 的角色不能反：$\Sigma$ 大、$C$ 小（亏格 $g\ge2$），否则低能谱不同。
- $\sigma$-模型是有效理论，不是精确描述：奇点处需回到 $C$ 上联络的无穷维空间 $\mathcal W$。
- Hitchin 方程是 BPS 方程（一阶），不是运动方程；不要把它和 4d 场方程混淆。

## 相关卡

[二维 $\sigma$-模型与靶空间 $\MH$](../concepts/sigma-model-mh.md) · [四维 $\mathcal N=4$ 超杨–米尔斯与部分拓扑场论](../concepts/n4-sym-partial-tqft.md) · [希钦方程](../concepts/hitchin-equations.md) · [希钦模空间 $\MH$](../concepts/hitchin-moduli.md) · [希钦方程 = 超凯勒矩映射商](../derivations/hitchin-as-moment-map.md)

## 出处（印刷页）

- A p.1–3（A p.2）
- A p.4–6（A p.4 eq (2.1)）

> 说明：A3：场分解、Hitchin 方程、模空间度规均在原文 §1–§2.2 明写；B1：$\Sigma\gg C$ 的定量版本是整理时补的。最没把握处：第 1 步“6 个标量中两个组合成 $\varphi$”是按 §2.1 的场内容的压缩表述。
