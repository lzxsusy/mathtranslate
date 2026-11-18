---
id: dmod/concept/d-module-on-affine-line
type: concept
track: H
---

# 仿射直线上的 $\mathcal D$-模

> $\mathbb A^1$ 上的 $\mathcal D$-模即 $k[z,\partial]$ 上的模；完整模有限长，$M_\alpha=\mathcal D/\mathcal D(z\partial-\alpha)$ 给出完整模型。

**问题**：$\mathbb A^1$ 上的 $\mathcal D$-模如何用 Weyl 代数 $\mathcal D(1)$ 描述，完整模的结构与例子 $M_\alpha$ 说明了什么？

## 定义

取 $X=\mathbb A^1=\operatorname{Spec}k[z]$。$X$ 上微分算子层的整体截面是 Weyl 代数 $\mathcal D(1)=k[z,\partial]$，$\partial=\mathrm d/\mathrm dz$，$[\partial,z]=1$；$\mathbb A^1$ 上的 $\mathcal D$-模就是左 $\mathcal D(1)$-模。有限生成 $\mathcal D(1)$-模的完整性与特征簇按 I §8 判定：$\operatorname{Ch}(M)$ 是 $k^2$（坐标 $(z,\xi)$，$\xi$ 是 $\partial$ 的主符号）中的锥，$M\neq0$ 时 $\dim\operatorname{Ch}(M)\ge1$，且 $M$ 完整当且仅当 $\dim\operatorname{Ch}(M)=1$。曲线情形下完整模是 $X$ 上有限秩平坦联络的推广（§4 批注），其不可约对象由定理 5.4.4 用「光滑子簇 + 其上的不可约联络」分类。

*记号*：$z$：$\mathbb A^1$ 的坐标；$\partial=\mathrm d/\mathrm dz$；$\xi$：$\partial$ 的主符号，$(z,\xi)$ 是 $T^*\mathbb A^1$ 的坐标；$\mathcal D(1)=k[z,\partial]$；$M_\alpha=\mathcal D(1)/\mathcal D(1)(z\partial-\alpha)$。

## 要点

- $\mathcal D(1)=k[z,\partial]$、$[\partial,z]=1$；$\mathbb A^1$ 上的 $\mathcal D$-模就是左 $\mathcal D(1)$-模，而 $\{z^pE^q,\ \partial^pE^q\}$（$E=z\partial$，$p,q\in\mathbb Z_+$）是 $\mathcal D(1)$ 的 $k$-基。
- 完整 $\mathcal D(1)$-模有限长（定理 5.1.3 的一维情形），故其分类归结为不可约完整模的分类（定理 5.4.4）。
- 曲线上的完整模是 $X$ 上有限秩平坦联络的推广（§4 批注）；正则奇点情形下 Deligne 定理给出完整分类。
- $M_\alpha=\mathcal D(1)/\mathcal D(1)(z\partial-\alpha)$ 的谱是 $\{\alpha+n;n\in\mathbb Z\}$（重数 1）；$\alpha\notin\mathbb Z$ 时不可约，$\alpha\in\mathbb Z$ 时可约。
- 所有 $M_\alpha$ 的特征簇都是 $\{z=0\}\cup\{\xi=0\}$，但 $\alpha$ 的整平移类不同则模不同构：特征簇不能决定模。

## 关键公式

- $\mathcal D(1)=k[z,\partial],\qquad[\partial,z]=1$
- $M_\alpha=\mathcal D(1)/\mathcal D(1)(z\partial-\alpha)$
- $\operatorname{Ch}(M_\alpha)=\{z=0\}\cup\{\xi=0\}\subset k^2$

## 定理与证明

### 定理 5.1.3（完整模有限长度）（完整）

设 $X$ 是光滑簇。则每个完整 $\mathcal D_X$-模都是有限长度的；特别地，$\mathbb A^1$ 上每个完整 $\mathcal D(1)$-模有限长。

1. 完整性在开集上的限制仍完整，且有限长度是局部性质（III.2.8），故可设 $X$ 光滑仿射，再设 $X$ 是 $k^n$ 的光滑闭子簇，$i:X\to k^n$。  
   *为什么*：两个性质都逐开集验证，仿射局部化不改变结论。
2. 由引理 5.1.2，$\mathcal V$ 完整蕴含 $i_+(\mathcal V)$ 完整；由 I.8.1，$k^n$ 上的完整模 $i_+(\mathcal V)$ 有限长。  
   *为什么*：引理 5.1.2 说闭浸入的直像保持并反射完整性；I.8.1 是 $k^n$ 上的有限长度定理。
3. $i_+(\mathcal V)$ 的子模与商模支集都含于 $X$，故它在全模范畴中的长度等于它在「支集含于 $X$ 的模」子范畴中的长度；由 Kashiwara 定理（$i_+$ 是该子范畴与 $\mathcal M(\mathcal D_X)$ 的等价），$\mathcal V$ 有限长。  
   *为什么*：长度由合成列定义，而子模/商模的支集含于原模的支集，故合成因子都留在子范畴内。

*出处*：定理 5.1.3 / 原书 V §1, p.134


## 易错点

- $\mathcal D(1)$ 不是有限 $k[z]$-模：它是 $k[z]$ 上的无限秩自由模；把 $\mathcal D$-模当成 $k[z]$-模来算会漏掉 $\partial$ 的作用。
- $M_\alpha$ 只在整平移下同构（$M_\alpha\cong M_{\alpha+p}$，$p\in\mathbb Z$）；$\alpha'-\alpha\notin\mathbb Z$ 时谱不同，模不同构。
- $\alpha\notin\mathbb Z$ 时基向量 $z^{\alpha+n}$ 不是 $k[z]$ 中的多项式，不能按多项式基展开；它们是形式幂。
- $\alpha\in\mathbb Z$ 时 $M_\alpha$ 可约，$0\to\mathcal O_1\to M_{-n}\to\Delta_1\to0$ 不分裂；不要因为 $M_\alpha$ 由一个生成元给出就以为它不可约。

## 出处

- Miličić《Lectures on the Algebraic Theory of D-Modules》中译本（校订批注本），I §8 完整模，p.33（PDF p.39），`源码/chapters/chap1.tex:1160-1183（完整性的定义与有限长度定理）`
- Miličić《Lectures on the Algebraic Theory of D-Modules》中译本（校订批注本），V §4 不可约完整模的分类，批注，p.140（PDF p.146），`源码/chapters/chap5.tex:274-276（批注：一维情形与 Deligne）`

## 核验

状态：`source-only`（2026-11-19）

## 关联

- `dmod/concept/irreducible-holonomic-classification`
- `dmod/concept/flat-connection`
- `dmod/concept/deligne-regular-singular`
- `dmod/example/example-euler-operator-on-a1`
