# 紧化到 Hitchin 方程：M = Σ×C

> `kw/deriv/compactify-to-hitchin` · 轨道 C · 舞台：曲线与模空间 · 状态 dev · 4 步

> **要回答的问题**：为什么四维扭化理论在 $\Sigma\times C$ 上约化后，低能物理只由 $C$ 上的 Hitchin 方程决定？

## 一句话

从 $M=\Sigma\times C$ 与尺度分层出发，用 §3.4 的平方和论证说明极小解在 $C$ 上满足 Hitchin 方程 $F-\varphi\wedge\varphi=0$、$D\varphi=D^*\varphi=0$；由此低能有效理论是以 $M_H$ 为靶的二维 sigma 模型。

## 目标

从紧化与平方和论证推出 Hitchin 方程与 $M_H$ 靶空间。

## 前提

- $M=\Sigma\times C$，$C$ 紧致且 $g>1$，$\Sigma$ 的尺度远大于 $C$，见 `B p.38`。
- 极小解同时使作用量取极小，这由 §3.4 的平方和论证给出，见 `B p.38`。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 把 $M$ 取成 $\Sigma\times C$：$C$ 是几何 Langlands 的紧 Riemann 面（$g>1$，一般平坦联络不可约），$\Sigma$ 可以是 $\mathbb R^2$ 或更大的紧曲面。沿 $\Sigma$ 方向的低能激发只有零模，且因 $\Sigma\gg C$ 零模沿 $\Sigma$ 缓变。 | 没有尺度分层，四维解与二维有效理论之间没有小参数；这是整个 §4 的物理前提。 | `B p.38` | B·原文暗示、我们补的中间步 |
| 2 | 由 §3.4，扭化作用量的玻色部分是平方和，极小当且仅当拓扑方程成立；取 $\sigma=0$、$A$ 与 $\varphi$ 由 $C$ 拉回，是一类极小解。 | 这一步把「解四维方程」换成「解 $C$ 上的方程」；若不知道极小等价于平方和为零，就找不到这个约化。 | `B p.39` | A·原文明确写了 |
| 3 | 此时极小条件化为 $C$ 上的 Hitchin 方程 eq (4.1)：$F-\varphi\wedge\varphi=0$、$D\varphi=D^*\varphi=0$。模去规范变换得 $M_H(G,C)$，复维 $(2g-2)\dim G$，奇点对应可约解。 | eq (4.1) 是后面所有几何的出发方程；把它错写成 $F=0$ 会漏掉 $\varphi$ 的贡献，模空间也就不对。 | `B p.39 eq (4.1)` | A·原文明确写了 |
| 4 | 一般极小解给出映射 $\Phi:\Sigma\to M_H$；零能量是常映射，近零能量是缓变映射，长距离有效理论即靶为 $M_H$ 的超对称 sigma 模型。 | 这一步把「模空间」变成「靶空间」，从而 §4 剩余部分可以用 $M_H$ 的复几何语言讨论对偶。 | `B p.39` | A·原文明确写了 |

## 结论

平方和论证把四维极小解压到 $C$ 上的 Hitchin 方程，$M_H$ 因而成为低能靶空间；映射 $\Sigma\to M_H$ 是 §11 中 A-膜与 B-膜讨论的舞台。尺度条件 $\Sigma\gg C$ 保证缓变映射存在且作用量小，反过来 $C\gg\Sigma$ 则得到对偶的 Hitchin 系统。

## 缺口

- 「零模沿 $\Sigma$ 缓变」依赖 $\Sigma\gg C$ 的物理近似，原文未给误差估计；非紧 $\Sigma$ 的边界条件也只是概括。

## 最容易讲错的地方

- 把 Hitchin 方程写成 $F=0$：eq (4.1) 是 $F-\varphi\wedge\varphi=0$ 与 $D\varphi=D^*\varphi=0$，缺一不可。
- 弄反尺度：必须是 $\Sigma$ 远大于 $C$；若 $C$ 远大于 $\Sigma$，得到的是相反方向的 Hitchin 系统。

## 相关卡

[Q-不变方程与消失定理](../derivations/vanishing-theorem.md) · [Hitchin 模空间](../concepts/hitchin-moduli.md) · [Hitchin 纤维化](../concepts/hitchin-fibration.md) · [$\mathcal N=4$ 超对称杨–米尔斯理论](../concepts/n4-sym-theory.md)

## 出处（印刷页）

- B p.38–39（B p.39 eq (4.1)）

> 说明：A3/B1：$\Sigma\times C$ 设定、平方和极小、eq (4.1) 与 $\Sigma\to M_H$ 映射均在 `B p.38–39` 明写；第 1 步的零模—缓变图像是原文暗示下补的中间步（B），最没把握处即此步。
