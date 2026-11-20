# 超 Kähler 商

- **id**：`gw06/concept/hyperkahler-quotient`
- **类型**：concept
- **位置**：§3.1
- **问题**：希格斯丛模空间为什么能写成 μ^{-1}(0)/G，三重矩映射的三个分量各自对应哪条希钦方程？

> 把无限维平坦超 Kähler 空间按三重矩映射的零点集对规范群作商，所得恰是希格斯丛模空间，这是研究 M_H 的起点。

## 定义

取黎曼面 $C$ 上的光滑 $G$-丛 $E$，令 $\mathcal W$ 为所有数对 $(A,\phi)$ 构成的空间，其中 $A$ 是 $E$ 上的联络、$\phi\in\Omega^1(C,\mathrm{ad}(E))$；$\mathcal W$ 是平坦的超 Kähler 流形，规范变换群 $\mathcal G$ 保超 Kähler 结构地作用其上，并带有三重矩映射 $\vec\mu=(\mu_I,\mu_J,\mu_K)$，每个分量对 $\epsilon\in\Omega^0(C,\mathrm{ad}(E))$ 线性。超 Kähler 商定义为 $\mathcal W/\! /\! /\mathcal G:=\vec\mu^{-1}(0)/\mathcal G$，它是有限维超 Kähler 流形；而在本情形中方程 $\vec\mu=0$ 恰好就是希钦方程，于是该商就是希格斯丛模空间 $\mathcal M_H(G,C)$。物理上这是四维 $\mathcal N=4$ 超杨–米尔斯理论紧化到二维后所出现的σ模型的目标空间。

**记号**：$\mathcal W$：$(A,\phi)$ 的空间、$\mathcal G$：$E$ 的规范变换群、$\vec\mu=(\mu_I,\mu_J,\mu_K)$：三重矩映射、$\mathcal W/\! /\! /\mathcal G$：超 Kähler 商、$\mathcal M_H(G,C)$：希格斯丛模空间

## 关键点

- 三重矩映射的每个分量形如 $\mu_\bullet=-{c\over2\pi}\int_C\Tr\epsilon(\cdots)$，对 $\epsilon$ 线性，取值于规范群李代数的对偶。
- $\mu_I=0$ 给出 $F=\phi\wedge\phi$；$\nu_I=\mu_J+i\mu_K=0$ 给出 $D_{\bar z}\phi_z=0$，其共轭给出 $D_z\phi_{\bar z}=0$，两条合起来才是 $d_A\phi=d_A\star\phi=0$。
- $\mu_K$ 前的因子 $i$ 不是规范选择：去掉它 $\nu_I$ 就不再全纯，第 3.2 节的 GIT 商构造随之失效。
- 商是几何不变量意义下的商而非集合商：$\mathcal G$ 的作用一般有非平凡稳定子，故 $\mathcal M_H$ 可能出现轨形奇点。
- 同一构造逐字搬到带奇点的情形，只须把 $\mathcal G$ 换成在 $p$ 处取值于环面 $\mathbb T$ 的子群 $\mathcal G_p$。

## 公式

```latex
\mu_I=-{1\over 2\pi}\int_C\Tr\epsilon(F-\phi\wedge\phi)
```
```latex
\mu_J=-{1\over 2\pi}\int_C|d^2z|\Tr\epsilon\left(D_z\phi_{\bar z}+D_{\bar z}\phi_z\right)
```
```latex
\mu_K=-{i\over 2\pi}\int_C|d^2z|\Tr\epsilon\left(D_z\phi_{\bar z}-D_{\bar z}\phi_z\right)
```
```latex
\mathcal W/\! /\! /\mathcal G=\vec\mu^{-1}(0)/\mathcal G
```

## 定理

**矩映射零点集与希钦方程等价**：对任意 $\epsilon\in\Omega^0(C,\mathrm{ad}(E))$，$\vec\mu=0$ 当且仅当 $(A,\phi)$ 满足希钦方程 $F=\phi\wedge\phi$、$d_A\phi=0$、$d_A\star\phi=0$。

证明：sketch（§3.1，式 (3.1) 及紧随其后的讨论）

1. $\mu_I=0$ 给出 $F-\phi\wedge\phi=0$。 —— 被积函数对任意 $\epsilon$ 为零，逐点得 $F-\phi\wedge\phi=0$。
2. $\nu_I=\mu_J+i\mu_K=0$ 给出 $D_{\bar z}\phi_z=0$。 —— 把式 (3.1) 的 $\mu_J,\mu_K$ 组合，$D_z\phi_{\bar z}$ 项系数为 $1-1=0$，只剩 $D_{\bar z}\phi_z$。
3. 取共轭得 $D_z\phi_{\bar z}=0$，与上一步合起来即 $d_A\phi=d_A\star\phi=0$。 —— $\phi$ 取值于实李代数，$D_z\phi_{\bar z}=0$ 的共轭就是 $D_{\bar z}\phi_z=0$ 的另一半。

## 常见错误

- 以为 $\mu_I,\mu_J,\mu_K$ 各自「就是」希钦方程的一条，从而把三条实方程数成三条独立复条件，$\mathcal M_H$ 的维数会算错一倍。
- 把商读成集合商，忽略稳定子，导致以为 $\mathcal M_H$ 处处光滑、跨墙现象无从出现。
- 抄式 (3.1) 时丢掉 $\mu_K$ 的 $i$，此时「三个分量」不再是同一个超 Kähler 结构下的矩映射，后续 GIT 描述整体作废。

## 批注

### 易错预警：三重矩映射，不是三条方程

超 Kähler 商的存在性依赖 $\vec\mu$ 的三重结构：三个分量分别对三个 Kähler 形式 $\omega_I,\omega_J,\omega_K$ 取矩。若只记住「商掉规范群」而忘了矩映射是三重，就会在第 3.2 节把 $\nu_I=\mu_J+i\mu_K$ 误当成人为拼凑的复组合，看不出它恰是复结构 $I$ 下的全纯矩映射。

### 含糊点拨：「平坦超 Kähler」是无穷维的陈述

「$\mathcal W$ 是平坦的超 Kähler 流形」是无穷维的陈述：$\mathcal W$ 作为仿射空间带平坦度量，超 Kähler 结构由 $C$ 上的复结构诱导。断言商之后仍是超 Kähler 流形，用的是 Hitchin–Karlhede–Lindström–Roček 的有限维定理，其无穷维版本需要先作规范固定（slice）才能严格化。

### 背景直觉：μ=0 就是 D-项与 F-项平坦

物理上 $\vec\mu=0$ 就是 D-项与 F-项平坦条件：$\mu_I=0$ 是「$F$ 被希格斯场吃掉」的 BPS 条件，$\nu_I=0$ 是全纯性条件。超 Kähler 商正是超对称σ模型的目标空间由超对称场论定义的几何版本。

## 出处

- Gukov–Witten 2006（hep-th/0612073v2）中译校订本 §3.1；印刷页 [31] / PDF 页 [32]；锚点 `08_source_code/SY02-06_规范理论、分歧与几何朗兰兹纲领/源码/sections/s03a-quotient.tex:29-60`
- 式 (3.1) 与超 Kähler 商定义见 PDF 第 32 页（印刷第 31 页）。

---

权利：`rewritten`；核验：`source-only`（2026-11-20）。
