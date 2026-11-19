# 二维 $\sigma$-模型与靶空间 $\MH$

> `gtgl15/concept/sigma-model-mh` · 轨道 C · 膜、线算符与本征膜 · 状态 dev

> **先自测**：为什么四维规范理论会退化成一个二维非线性 $\sigma$-模型，而靶空间恰好是 Hitchin 模空间？

## 一句话

4d $\mathcal N=4$ 规范理论紧致化在 $\Sigma\times C$ 上（$\Sigma$ 很大）给出 2d $\sigma$-模型，靶空间是 $C$ 上希格斯丛的超凯勒模空间 $\MH$；这解释了“2+2=4”。

## 定义

把 4d $\mathcal N=4$ 超杨–米尔斯放在 $\Sigma\times C$ 上并令 $\Sigma$ 的尺度远大于 $C$。低能自由度是 $C$ 方向上的零模，即 $C$ 上的超对称真空：希格斯丛 $(E,\varphi)$，其模空间为 $\MH$。于是得到 2d $\sigma$-模型，靶空间 $\MH$。“$d$ 维 QFT 给出 $(d-2)$ 维流形范畴”的口诀在 $d=4$ 时是“2+2=4”：4d 理论的边界条件范畴 = 2d 理论的点范畴，即 $\MH$ 上的膜范畴。$\sigma$-模型只在 $\MH$ 的一般点有效；奇点处有额外规范对称恢复。完整描述是 $C$ 上联络的无穷维空间 $\mathcal Y$ 及其余切丛 $\mathcal W$，代数量化用 stack（Atiyah–Bott）。

**记号**：$\Sigma$（大）、$C$（小）；$\MH$；$\mathcal Y$；$\mathcal W=T^*\mathcal Y$；膜范畴。

## 要点（为什么需要它）

1. “2+2=4”：$d$ 维 QFT 的边界条件范畴 $\sim$ $(d-2)$ 维流形的范畴；4d 理论给 2d $\sigma$-模型。
2. 靶空间不是普通的 Kähler 流形而是超凯勒流形 $\MH$：三个复结构给出 A/B 模型的多种 twist。
3. $\sigma$-模型是有效理论：在 $\MH$ 的奇异点（规范对称增强处）失效，需要回到 $\mathcal W$ 的描述。
4. 边界条件 = $\MH$ 上的膜（B-膜对应 coherent sheaf，A-膜对应 Lagrangian + 平坦线丛）。
5. 不同 4d 超荷给出不同的 2d twist：$A$-模型与 $B$-模型，以及 $(B,A,A)$ 型膜；这是全文对偶陈述的舞台。

## 核心公式

$$
$$4d\ \mathcal N=4\ \text{on}\ \Sigma\times C\ \xrightarrow{\ \Sigma\ \text{大}\ }\ 2d\ \sigma\text{-模型，靶}=\MH$$$$\text{边界条件}\ \longleftrightarrow\ \MH\ \text{上的膜（B-膜 / A-膜）}$$
$$

$$
$$\text{边界条件}\ \longleftrightarrow\ \MH\ \text{上的膜（B-膜 / A-膜）}$$
$$

## 定理与证明（或缺口）

### 从 4d 到 2d 的有效描述

$\Sigma$ 尺度远大于 $C$ 时，4d $\mathcal N=4$ 理论的低能动力学由靶为 $\MH$ 的 2d $\sigma$-模型描述。

> 证明状态：**sketch**。原文 §1 只陈述结论并引用标准紧致化论证，未给逐阶有效作用量推导。

出处：`A p.2`

## 常见误解

- $\sigma$-模型只在 $\MH$ 的一般点有效；奇点处规范对称增强，必须回到 $\mathcal W$，不能只用 $\MH$ 上的膜描述。
- $C$ 与 $\Sigma$ 的大小关系不能反：要 $\Sigma\gg C$（或至少取 $\Sigma$ 为大尺度）。
- 靶空间 $\MH$ 是超凯勒的，但 $\sigma$-模型本身不自动超对称：需要选合适的 twist。
- “2+2=4”是范畴维数的口号，不是紧致化维数计算：$4-2=2$ 给的是 2d 理论的点范畴。

## 相关卡

[四维 $\mathcal N=4$ 超杨–米尔斯与部分拓扑场论](../concepts/n4-sym-partial-tqft.md) · [膜、$A$-膜与 $B$-膜](../concepts/branes-ab.md) · [希钦模空间 $\MH$](../concepts/hitchin-moduli.md) · [超凯勒商与复结构 I、J、K](../concepts/hyperkahler-quotient.md) · [从 4d $\mathcal N=4$ 到 2d $\sigma$-模型](../derivations/compactify-to-sigma.md)

## 出处（印刷页）

- A p.1–3（A p.2）
- A p.2–4（A p.3）
- A p.6（A p.6 eq (2.3)）

> 说明：A=原文 §1 的紧致化图像与 $\S2.1$–$\S2.2$ 的模空间度规；B=把“2+2=4”与有效作用量拆成三步；C=$\sigma$-模型在奇点失效的表述按原文脚注与 $\S2.1$ 整理。最没把握处：$\Sigma\gg C$ 的精确条件原文未量化。
