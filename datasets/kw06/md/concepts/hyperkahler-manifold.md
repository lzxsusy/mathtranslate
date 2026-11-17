# 超凯勒流形

> `kw/concept/hyperkahler-manifold` · 轨道 C · 舞台：曲线与模空间 · 状态 dev

> **先自测**：超凯勒流形的定义是什么，它为什么是构造一族二维拓扑场论的关键？

## 一句话

带三个复结构 $I,J,K$（满足四元数关系）与相容度量、且三个辛形式都闭的流形；超凯勒性使同一流形上有一整族复结构，是二维 A/B 模型可以互换的几何前提。

## 定义

超凯勒流形是带相容度量 $g$ 与三个两两正交复结构 $I,J,K$ 的流形：$IJ=-JI=K$ 并循环成立，且 $g$ 对 $I,J,K$ 都是 Kähler 度量。等价地，每个复结构下都有闭的全纯辛形式（如 $\Omega_I=\omega_J+\mathrm{i}\omega_K$，$d\Omega_I=0$），和乐群含于 $\mathrm{Sp}(k)$。其实维数为 $4k$。

**记号**：$(X,g,I,J,K)$；$\omega_I=g(I\cdot,\cdot)$；$\Omega_I=\omega_J+\mathrm{i}\omega_K$；$\dim_{\mathbb C}X=2k$，实维 $4k$。

## 要点（为什么需要它）

1. 复结构不唯一：任意单位向量 $(a,b,c)$ 给复结构 $aI+bJ+cK$，构成 $\mathbb{CP}^1$ 一族，物理上正是选扭化参数的自由度。
2. 二维 $(4,4)$ 超对称要求靶空间超凯勒：左右手可以各选一个复结构，这是 A/B 模型与 T-对偶的几何根源。
3. $M_H$ 与 $\mathcal W$ 都是超凯勒流形（$\mathcal W$ 还是平坦的），所以 $M_H$ 上能定义三个辛形式与三个矩映射。
4. 在 $M_H$ 情形，$\omega_J$ 依赖 $C$ 的复结构，而 $\omega_I$、$\omega_K$ 不依赖，这决定了 §4.3 用哪个复结构讲纤维化。

## 核心公式

$$
$IJ=-JI=K,\qquad JK=-KJ=I,\qquad KI=-IK=J$$\Omega_I:=\omega_J+\mathrm{i}\omega_K,\qquad d\Omega_I=0,\qquad \mathrm{Hol}(g)\subseteq\mathrm{Sp}(k)$
$$

$$
$\Omega_I:=\omega_J+\mathrm{i}\omega_K,\qquad d\Omega_I=0,\qquad \mathrm{Hol}(g)\subseteq\mathrm{Sp}(k)$
$$

## 定理与证明（或缺口）

### $\mathcal W$ 上的平坦超凯勒结构

在 $C$ 上所有 $(A,\varphi)$ 构成的仿射空间 $\mathcal W$ 上，(4.2) 的平度量连同 (4.3)–(4.5) 定义的常系数线性复结构 $I,J,K$ 使其成为平坦超凯勒流形。

> 证明状态：**sketch**。原文 p.42–43 只写出四元数关系与「可 readily verified」，未展开 $(1,1)$ 型的计算。

出处：`B p.43`

### 三个辛形式的复结构依赖

在 $M_H$ 上，$\omega_J$ 依赖 $C$ 的复结构，而 $\omega_I$ 与 $\omega_K$ 不依赖；等价地 $\Omega_I$、$\Omega_K$ 依赖 $C$ 的复结构，$\Omega_J$ 不依赖。

> 证明状态：**sketch**。原文 p.44 只陈述这一依赖关系，未给逐项验证。

出处：`B p.44`

## 常见误解

- 把三个复结构误当成三个流形（或三个靶空间）：它们是同一个实流形上的三个结构，度量是同一个。
- 以为给了三个复结构就是超凯勒：还必须存在与三者都相容的 Kähler 度量，等价地三个辛形式都闭。
- 把 twistor 球的参数 $w$ 当成物理参数 $\Psi$：$w$ 是几何复结构的标签，$\Psi$ 是理论参数。
- 以为 $\mathcal W$ 平坦就推出 $M_H$ 平坦：$M_H$ 只是商，一般并不平坦。

## 相关卡

[复结构](../concepts/complex-structure.md) · [超凯勒商](../concepts/hyperkahler-quotient.md) · [Hitchin 模空间](../concepts/hitchin-moduli.md) · [广义复几何：A/B 与 B-场的统一语言](../derivations/generalized-complex.md)

## 出处（印刷页）

- B p.41–42（B p.42）
- B p.43（B p.43 eq (4.6)）
- B p.44（B p.44）

> 说明：A=原文（$\mathcal W$ 的平度量、四元数关系与 $I_w$ 族、$\Omega_I$ 是 $(2,0)$ 型、$\omega_J$ 的复结构依赖、仿射空间上可积性自动）；B=由原文重建（三条辛形式的逐项依赖判断、$(1,1)$ 型验证的展开）；C=标准背景（$\mathrm{Hol}\subseteq\mathrm{Sp}(k)$ 的等价刻画）。
