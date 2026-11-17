# 希格斯丛

> `kw/concept/higgs-bundle` · 轨道 C · 舞台：曲线与模空间 · 状态 dev

> **先自测**：希格斯丛与 Hitchin 方程、稳定性之间是什么关系？

## 一句话

曲线 $C$ 上的对 $(E,\varphi)$：$E$ 是 $G$-丛，希格斯场 $\varphi\in H^0(C,K_C\otimes\mathrm{ad}E)$；稳定对构成 $M_H$ 在复结构 $I$ 下的模型。

## 定义

希格斯丛（Hitchin 对）是 $C$ 上的对 $(E,\varphi)$：$E$ 为光滑 $G$-丛（配上联络后自动成为全纯丛），$\varphi\in H^0(C,K_C\otimes\mathrm{ad}E)$ 称为希格斯场。$G=SU(2)$ 时 $E$ 是秩 2 全纯向量丛，$\varphi$ 是 $E\to E\otimes K_C$ 的截面。稳定希格斯丛的模空间就是 $M_H$ 在复结构 $I$ 下的样子。

**记号**：$(E,\varphi)$；$E$：$G$-丛；$\mathrm{ad}E$：伴随丛；$\varphi\in H^0(C,K_C\otimes\mathrm{ad}E)$；$M$：稳定 $G$-丛的模空间。

## 要点（为什么需要它）

1. 它是 $M_H$ 在复结构 $I$ 下的具体对象：$\varphi=0$ 给出稳定丛的嵌入 $M\hookrightarrow M_H$，非零 $\varphi$ 沿余切方向离开 $M$。
2. 稳定性（$\varphi$-不变子丛的斜率条件）是模空间良定义的关键；不稳定对必须剔除，否则得到的商不是分离的模空间。
3. 两个复结构两种读法：$I$ 下是希格斯丛，$J$ 下是稳定平坦 $G_{\mathbb C}$ 丛，对应 Hitchin 定理与 Corlette–Donaldson 定理。
4. 它是「$M_H$ 包含 $T^*M$」的具体实现：Serre 对偶把 $\varphi$ 认成 $M$ 的余切向量。

## 核心公式

$$
$\varphi\in H^0(C,K_C\otimes\mathrm{ad}E),\qquad T^*_E M=H^0(C,K_C\otimes\mathrm{ad}E)$$M_H\supset T^*M,\qquad T_E M=H^1(C,\mathrm{ad}E)$
$$

$$
$M_H\supset T^*M,\qquad T_E M=H^1(C,\mathrm{ad}E)$
$$

## 定理与证明（或缺口）

### Hitchin 定理（复结构 $I$ 下的描述）

在复结构 $I$ 下，$M_H$ 等于稳定 Hitchin 对 $(E,\varphi)$ 的模空间。

> 证明状态：**sketch**。原文 p.50 引用 Hitchin [20] 的结果，未复述证明；稳定性只以 $G=SU(2)$ 与一般 $G$ 的判据形式陈述。

出处：`B p.50`

## 常见误解

- 把 $\varphi$ 当成标量：它取值于 $K_C\otimes\mathrm{ad}E$，带 $C$ 上 $(1,0)$-形式指标，才能与联络相加。
- 把 $T^*M$ 当成整个 $M_H$：$M_H$ 一般是非紧超凯勒流形，$T^*M$ 只是开稠密子集，差一个高余维坏集。
- 忘记区分商 $G$ 与商 $G_{\mathbb C}$：复结构 $I$ 的希格斯丛描述来自 $G_{\mathbb C}$-商，实矩映射约束来自 $G$-商。

## 相关卡

[希格斯场](../concepts/higgs-field.md) · [Hitchin 模空间](../concepts/hitchin-moduli.md) · [Riemann 面](../concepts/riemann-surface.md) · [M_H 上的 sigma 模型数据与维数公式](../derivations/mh-sigma-data.md)

## 出处（印刷页）

- B p.49–50（B p.49）
- B p.50–51（B p.50）
- B p.52（B p.52）

> 说明：A=原文（Hitchin 对与希格斯场的命名、$\varphi\in H^0(C,K_C\otimes\mathrm{ad}E)$、稳定性、Hitchin 定理、$T^*M\subset M_H$ 的 Serre 对偶论证）；B=由原文重建（两种复结构的分工、$M_H$ 与 $T^*M$ 的关系式）；C=标准背景（$G=SU(2)$ 时写成秩 2 向量丛的语言）。
