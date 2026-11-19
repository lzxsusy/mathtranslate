# 希钦模空间 $\MH$

> `gtgl15/concept/hitchin-moduli` · 轨道 A · Hitchin 几何与谱曲线 · 状态 dev

> **先自测**：$\MH$ 作为流形有多大，为什么它的复维数恰是 Hitchin 纤维化底空间维数的一半？

## 一句话

$\MH$ 是 $C$ 上稳定希格斯丛的模空间，也是希钦方程解模去规范群的结果；它是复维 $2(g-1)\dim G$ 的非紧完备超凯勒流形。

## 定义

固定紧黎曼面 $C$（亏格 $g$）与复约化群 $G$，$\MH=\MH(G,C)$ 是 $C$ 上稳定 $G_\mathbb{C}$-希格斯丛的模空间，等价地是希钦方程解的模空间。$\dim_\mathbb{C}\MH=2(g-1)\dim G$，即 Hitchin 底空间维数 $(g-1)\dim G$ 的两倍。对 $PSU(N)$ 等带中心商的群，$\MH$ 按离散拓扑荷 $\xi$ 分成若干连通分量。

**记号**：$\MH$；$g$；$\dim G$；$\xi\in H^2(C,\pi_1(G))$。

## 要点（为什么需要它）

1. $\MH$ 非紧但完备：无穷远处对应希格斯场的谱曲线退化，正是单极子与拓扑荷出现的区域。
2. 复结构 $I$ 下 $\MH$ 是希格斯丛模空间；复结构 $J$ 下是平坦联络模空间（非阿贝尔 Hodge 对应）。
3. $\dim_\mathbb{C}\MH=2\dim_\mathbb{C}\mathcal V$，其中 $\mathcal V$ 是 Hitchin 纤维化的底；这是完全可积性的维数前提（$\S2.4$）。
4. 对 $SU(N)$：$\dim_\mathbb{C}\MH=2(N^2-1)(g-1)$；对 $U(N)$：$\dim_\mathbb{C}\MH=2N^2(g-1)+2$（$U(N)$ 的底空间含 $\operatorname{Tr}\varphi$，维数是 $(g-1)N^2+1$，见 §2.6.5）。
5. $\MH$ 的奇点（增强规范对称处）是低能 σ-模型描述失效的地方，也是本文讨论 Hecke 作用的边界。

## 核心公式

$$
$$\dim_\mathbb{C}\MH=2(g-1)\dim G,\qquad \dim_\mathbb{R}\MH=4(g-1)\dim G$$$$\MH=\bigsqcup_{\xi}\MH^{(\xi)}$$
$$

$$
$$\MH=\bigsqcup_{\xi}\MH^{(\xi)}$$
$$

## 定理与证明（或缺口）

### 维数公式

$\dim_\mathbb{C}\MH=2(g-1)\dim G$，且 $\dim F=\dim\mathcal V=(g-1)\dim G=\frac12\dim_\mathbb{C}\MH$，其中 $F$ 是一般 Hitchin 纤维。

> 证明状态：**sketch**。原文 §2.4 直接陈述 $\dim F=\frac12\dim\MH$（eq (2.6)），纤维的 Lagrangian 性在 §2.5 末作为完全可积的推论给出；“纤维维数恰为一半”的独立形变理论证明原文未展开。

出处：`A p.8 eq (2.6)`

## 常见误解

- $\MH$ 非紧，别把它当紧 Kähler 流形用 Hodge 理论。
- $\dim_\mathbb{C}\MH=2(g-1)\dim G$：漏掉因子 2、或把 Hitchin 底空间的维数 $(g-1)\dim G$ 当成 $\MH$ 的维数，都是最常见的错。
- $g=0$ 时 $SU(N)$ 的 $\MH$ 退化为点；$g=1$ 时纤维化结构退化，不能套用 $g>1$ 的图像。
- $PSU(N)$ 的 $\MH$ 不连通，分量标签 $\xi$ 是离散磁荷，不能忽略。

## 相关卡

[希格斯丛与希钦对](../concepts/higgs-bundle.md) · [超凯勒商与复结构 I、J、K](../concepts/hyperkahler-quotient.md) · [希钦纤维化](../concepts/hitchin-fibration.md) · [稳定丛模空间与余切丛](../concepts/stable-locus.md) · [维数计数：$\sum(2d_i-1)=\dim G$](../derivations/dimension-count.md)

## 出处（印刷页）

- A p.4–6（A p.4 eq (2.1)）
- A p.7–8（A p.8 eq (2.6)）

> 说明：A=原文 §2.2（$\MH$ 定义）与 §2.4（维数计算 eq (2.5)(2.6)）；B=把 eq (2.6) 的断言整理成“底空间维数 → 纤维 Lagrangian → 一半维数”的三步推理；C=拓扑荷分量的陈述按 §2.6.6 的 $PSU(N)$ 情形推广。最没把握处：$g=0,1$ 的退化行为原文只在 §7.1.2 顺带提到。
