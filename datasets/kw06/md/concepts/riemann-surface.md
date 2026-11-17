# Riemann 面

> `kw/concept/riemann-surface` · 轨道 C · 舞台：曲线与模空间 · 状态 dev

> **先自测**：Riemann 面在紧化与 Hitchin 构造中起什么作用？

## 一句话

紧致的一维复流形（复代数曲线）；本文取亏格 $g>1$，使半单群 $G$ 的平坦联络一般不可约，它是 Hitchin 方程与几何 Langlands 的共同舞台。

## 定义

紧致连通的一维复流形，即复代数曲线 $C$；全纯 1-形式空间 $H^0(C,K_C)$ 的维数称为亏格 $g$。本文的紧化取 $M=\Sigma\times C$，并要求 $g>1$，以保证半单群 $G$ 的一般平坦联络不可约。

**记号**：$C$：紧 Riemann 面；$g=\mathrm{genus}(C)>1$；$K_C$：典范丛；$\pi_1(C)$：基本群。

## 要点（为什么需要它）

1. 整条论证链的几何舞台：$G$-丛、Hitchin 方程、Hecke 算子都定义在 $C$ 上，$M_H$ 随 $(G,C)$ 变化。
2. 取 $g>1$ 使半单群的一般平坦联络不可约，于是 $M_H$ 的一般点光滑，奇点（可约解）只占低维。
3. 复维为 1 是关键：$(0,2)$-形式空间为零，$\bar\partial^2=0$ 自动成立，所以任意联络都给出全纯丛结构。
4. 紧性往下传：$C$ 紧、$M=\Sigma\times C$ 紧，紧化与 Hitchin 纤维的紧性都依赖它。

## 核心公式

$$
$\dim_{\mathbb C}H^0(C,K_C^{\,n})=(2n-1)(g-1)\quad(n\ge 1)$$M=\Sigma\times C,\qquad g=\mathrm{genus}(C)>1$
$$

$$
$M=\Sigma\times C,\qquad g=\mathrm{genus}(C)>1$
$$

## 定理与证明（或缺口）

### Riemann 面上的联络自动给出全纯结构

设 $E\to C$ 是光滑 $G$-丛、$A$ 是其上任意联络。令 $\bar\partial_A$ 为 $A$ 的 $(0,1)$ 部分，则 $\bar\partial_A^2=0$，因此 $E$ 自动具有全纯 $G$-丛结构。

1. 取 $A$ 的 $(0,1)$ 部分定义 $\bar\partial_A$：局部坐标下 $\bar\partial_A=d\bar z\,D_{\bar z}$，它把 $E$ 的截面送到 $E\otimes\overline{K_C}$ 的截面。
   - *为什么*：这是把联络拆成 $(1,0)$ 与 $(0,1)$ 两半的标准做法，$(0,1)$ 部分正是全纯结构的候选。
2. 计算 $\bar\partial_A^2$：它是 $(0,2)$-型微分算子，而 $C$ 是复一维的，$(0,2)$-形式空间为零，故 $\bar\partial_A^2=0$ 自动成立。
   - *为什么*：全纯结构的唯一障碍是 $(0,2)$ 分量；复维 1 时该分量不存在，这正是整套构造只在曲线上成立的原因。

出处：`B p.49`

## 常见误解

- 把「$C$ 紧」误推成「$M_H$ 紧」：$M_H$ 一般非紧、还带奇点，紧的是 Hitchin 纤维。
- 把 $g>1$ 当成无关的技术条件：$g=0,1$ 时 $2g-2$ 与一般不可约性一起退化，整套维数公式失效。
- 把 $C$ 与 $M_H$ 混为同一层对象：$C$ 是紧化的小因子，$M_H$ 是由 $C$ 上的丛模空间构成的靶空间。

## 相关卡

[Hitchin 模空间](../concepts/hitchin-moduli.md) · [希格斯丛](../concepts/higgs-bundle.md) · [复结构](../concepts/complex-structure.md) · [紧化到 Hitchin 方程：M = Σ×C](../derivations/compactify-to-hitchin.md)

## 出处（印刷页）

- B p.38–40（B p.38）
- B p.49（B p.49）
- B p.54（B p.54）

> 说明：A=原文（紧 Riemann 面、$g>1$ 与不可约性、维数公式、联络给出全纯结构）；B=由原文重建（$(0,1)$ 形式化的表述、$g>1$ 与一般点光滑的关系）；C=标准背景（紧复曲线即复代数曲线，未写入正文）。
