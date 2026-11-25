# 例：$s=1/2$ 处的二分法

> `grassmann/example/s-half-dichotomy` · 轨道 3 · Reider 与 Thaddeus 再探 · 状态 draft

> **这张卡练什么**：为什么 $s=\frac12$ 这一条直线上，Bridgeland 稳定性恰好退化为秩 $2$ 层的半稳定性？

## 一句话

在 $s=\frac12$ 处，$L\otimes\mathcal I_Z\to\mathcal O_S[1]$ 的态射是否单射恰好对应秩 $2$ 层 $E$ 的半稳定性，Bridgeland 二分法因此复现 Reider 的经典二分。

## 背景定义

$s=\frac12$ 处的**二分法**指：$\mathcal A_{1/2}$ 中 $f:L\otimes\mathcal I_Z\to\mathcal O_S[1]$ 的单射性，与扩张 $0\to\mathcal O_S\to E\to L\otimes\mathcal I_Z\to0$ 所定义的秩 $2$ 层 $E$ 的 $H$-半稳定性互相等价。

## 设定

设 $S$ 是光滑射影曲面，$L$ 充裕，$H=c_1(L)$，$Z\subset S$ 是长度 $d$ 的零维子概形。取 $\epsilon\in\Ext^1(L\otimes\mathcal I_Z,\mathcal O_S)$，对应扩张 $0\to\mathcal O_S\to E\to L\otimes\mathcal I_Z\to0$；此时 $E$ 秩 $2$、$\mu_H(E)=\frac12$。把 $\epsilon$ 看成倾斜心 $\mathcal A_{1/2}$ 中的态射 $f:L\otimes\mathcal I_Z\to\mathcal O_S[1]$。

## 计算

推论 3.2 给出三种情形：(a) $f$ 单射，商为 $Q[1]$ 且 $\mu_H(Q)\le\frac12$；(b) $f$ 满射，核为 $K'$ 且 $\mu_H(K')>\frac12$；(c) $f$ 既非单射也非满射，此时 $E$ 是 $\mathcal O_S(D)\otimes\mathcal I_V$ 被 $L(-D)\otimes\mathcal I_W$ 的扩张，不是半稳定的。在 $s=\frac12$：(a) 中 $E=Q$ 半稳定；(b) 中 $E=K'$ 与 $\mu_H(K')>\frac12$ 矛盾；(c) 非半稳定。反之若 $E$ 半稳定，则 $E[1]\in\mathcal A_{1/2}$，而 (a) 的正合列正是该扩张的倾斜。

## 要点

- $E$ 的秩为 $2$、$\mu_H(E)=\frac12$ 是扩张决定的，不是额外假设。
- 原结论只说「几乎」得到第 2 节的二分法：这里固定在 $s=\frac12$ 一条直线上，其他 $s$ 的二分法不同。
- 单射性必须在 $\mathcal A_{1/2}$ 中判断；$\mathcal O_S[1]$ 是移位对象，回到凝聚层范畴看 $\Hom$ 会漏掉倾斜结构。
- 这条二分法与 Reider 定理的稳定/非稳定两支是同一件事的两种语言。

## 关键公式

$$
f:L\otimes\mathcal I_Z\to\mathcal O_S[1],\qquad f\in\Ext^1_{\mathcal O_S}(L\otimes\mathcal I_Z,\mathcal O_S)
$$

$$
\mu_H(E)=\frac12,\qquad f\ \text{单射}\iff E\ \text{半稳定}
$$

## 相关定理

- **例（$s=1/2$ 二分法）**：在 $s=\frac12$ 处，$f\in\Hom_{\mathcal A_{1/2}}(L\otimes\mathcal I_Z,\mathcal O_S[1])$ 在 $\mathcal A_{1/2}$ 中是单射，当且仅当 $E$ 是 $H$-半稳定的。

## 易错点

- $E$ 是秩 $2$ 层，$\mu_H(E)=\frac12$ 是定理内容的一部分；把它当成假设会漏掉「扩张决定 $E$」这一步。
- 原文说「几乎」：$s=\frac12$ 的二分法只在这一条直线上成立，不能外推到所有 $s$。
- $\mathcal O_S[1]$ 是移位对象，$f$ 的单射性在倾斜心里判断，不能用凝聚层范畴里的 $\Ext^1$ 直接读。

## 用到哪些概念

- [Bridgeland 稳定性条件](../concepts/bridgeland-stability-condition.md)
- [挠对与倾斜](../concepts/torsion-pair-and-tilt.md)

## 相关卡

- [Bridgeland 稳定性条件](../concepts/bridgeland-stability-condition.md)
- [挠对与倾斜](../concepts/torsion-pair-and-tilt.md)
- [Reider 定理](../concepts/reiders-theorem.md)
- [α-稳定凝聚系](../concepts/alpha-stable-coherent-system.md)

## 出处

- ch3 §3 例（$s=1/2$ 二分法）；中译 p.62（英文 PDF p.67），源码 `chapters/ch03.tex:364`
