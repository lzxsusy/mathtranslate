# Hitchin 模空间

> `kw/concept/hitchin-moduli` · 轨道 C · 舞台：曲线与模空间 · 状态 dev

> **先自测**：Hitchin 模空间 $M_H$ 有哪些结构，它为什么是整条论证链的中央舞台？

## 一句话

Hitchin 方程 $F-\varphi\wedge\varphi=0,\ D\star\varphi=0$ 的解模规范群得到的空间 $M_H(G,C)$：复维 $(2g-2)\dim G$ 的超凯勒流形，是紧化后二维 sigma 模型的靶空间。

## 定义

给定紧 Riemann 面 $C$（$g>1$）与紧半单群 $G$，$M_H(G,C)$ 是 Hitchin 方程 $F-\varphi\wedge\varphi=0,\ D\star\varphi=0$ 的解空间模去规范群作用得到的模空间。$g>1$ 时它的复维是 $(2g-2)\dim G$，并带超凯勒结构；它一般非紧、带奇点，奇点对应可约解。

**记号**：$M_H=M_H(G,C)$；$\mathcal W$：所有 $(A,\varphi)$ 构成的仿射空间；$M_H=\mathcal W/\!/\!/G$；$\dim_{\mathbb C}M_H=(2g-2)\dim G$。

## 要点（为什么需要它）

1. 中央舞台：扭化参数用来选 $M_H$ 上的复结构，膜范畴与谱链都住在它上面。
2. 三种复结构两种读法：$I$ 下 $M_H$ 是稳定希格斯丛的模空间，$J$ 下是稳定平坦 $G_{\mathbb C}$ 丛的模空间，$K$ 与 $J$ 在物理上分别对应 A-模型与 B-模型。
3. 超凯勒性不是额外假设：$\mathcal W$ 是平坦超凯勒仿射空间，$M_H$ 是它关于规范群的超凯勒商。
4. 它是完全可积系统：Hitchin 纤维化把 $M_H$ 摊成「半维底 + 半维环面纤维」。
5. 非紧且带奇点：奇点来自可约解，本文一律在一般点附近工作，紧的只是 Hitchin 纤维。

## 核心公式

$$
$\dim_{\mathbb C}M_H=(2g-2)\dim G,\qquad \dim_{\mathbb R}M_H=4(g-1)\dim G$$M_H=\mathcal W/\!/\!/G=\{\mu_I=\mu_J=\mu_K=0\}/G$
$$

$$
$M_H=\mathcal W/\!/\!/G=\{\mu_I=\mu_J=\mu_K=0\}/G$
$$

## 定理与证明（或缺口）

### Corlette–Donaldson 定理（复结构 $J$ 下的描述）

$M_H$ 在复结构 $J$ 下同构于稳定同态 $\vartheta:\pi_1(C)\to G_{\mathbb C}$ 的模空间，即稳定平坦 $G_{\mathbb C}$ 丛的模空间。

> 证明状态：**gap**。原文 p.51 引用 [58] 与 [20] 附录的结果，只陈述结论，未复述证明。

出处：`B p.51`

### Hitchin 定理（复结构 $I$ 下的描述）

$M_H$ 在复结构 $I$ 下等于稳定 Hitchin 对 $(E,\varphi)$ 的模空间。

> 证明状态：**sketch**。原文 p.50 引用 Hitchin [20] 的结果，未复述证明；稳定性只以 $G=SU(2)$ 与一般 $G$ 的判据形式陈述。

出处：`B p.50`

## 常见误解

- 把三个复结构当成三个不同流形：$I,J,K$ 是同一个实流形上的三个结构，$\omega_I,\omega_J,\omega_K$ 也来自同一个度量。
- 把 $M_H$ 当成 $T^*M$ 的平凡商：$T^*M$ 只是开稠密子集，$\varphi=0$ 之外还差一个高余维坏集。
- 把 $M_H$ 当成紧流形或 Calabi–Yau 流形：它一般非紧、带奇点，复维随 $g$ 与 $\dim G$ 增长。
- 记错维数：复维是 $(2g-2)\dim G$，实维要乘 4 而不是乘 2。

## 相关卡

[Hitchin 纤维化](../concepts/hitchin-fibration.md) · [超凯勒商](../concepts/hyperkahler-quotient.md) · [希格斯丛](../concepts/higgs-bundle.md) · [超凯勒商与三个复结构 I, J, K](../derivations/hyperkahler-quotient.md) · [M_H 上的 sigma 模型数据与维数公式](../derivations/mh-sigma-data.md)

## 出处（印刷页）

- B p.38–40（B p.39）
- B p.50–51（B p.50）
- B p.53–56（B p.54）

> 说明：A=原文（Hitchin 方程 (4.1)、复维 $(2g-2)\dim G$、两个模空间描述、超凯勒商、可积系统）；B=由原文重建（「中央舞台」的角色归纳、实维换算）；C=标准背景（非紧性与奇点的关系，原文只提到避开奇点）。
