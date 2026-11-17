---
id: glc/concept/betti-characteristic-variety
type: concept
track: F
---

# 解层的奇异支撑与特征簇

> 正则完整 $D$ 模的解层，其微局部奇异支撑恰是原模的特征簇；这把 Betti 层与 de Rham 侧的特征簇对应起来。

**问题**：为什么说 Betti 层的微局部支撑是完整 $D$ 模特征簇的对应物？

## 定义

设 $M$ 为正则完整 $D$ 模，$\operatorname{Sol}(M)$ 是它的解层。则
$$\operatorname{SS}(\operatorname{Sol}(M))=\operatorname{Char}(M).$$
因此，Betti 层的微局部支撑是完整 $D$ 模特征簇的 Betti 对应物。

*记号*：$\operatorname{Sol}(M)=\underline{\operatorname{Hom}}_{D}(M,\mathcal O)$ 为 $M$ 的解层；$\operatorname{Char}(M)\subset T^*X$ 为 $M$ 的特征簇；$\operatorname{SS}$ 为 §11.4 定义的微局部奇异支撑。

## 要点

- 等式 $\operatorname{SS}(\operatorname{Sol}(M))=\operatorname{Char}(M)$ 要求 $M$ 为正则完整 $D$ 模。
- 它把 Betti 侧的微局部奇异支撑等同于 de Rham 侧的特征簇，从而是两侧比较的桥梁。
- $\operatorname{Char}(M)$ 与 $\operatorname{SS}(\operatorname{Sol}(M))$ 都住在同一个余切丛 $T^*X$ 中，因此可以直接比较。

## 关键公式

- $$\operatorname{SS}(\operatorname{Sol}(M))=\operatorname{Char}(M)$$

## 定理与证明

### 解层奇异支撑等于特征簇（要点（有缺口））

若 $M$ 为正则完整 $D$ 模、$\operatorname{Sol}(M)$ 为其解层，则 $\operatorname{SS}(\operatorname{Sol}(M))=\operatorname{Char}(M)$。

1. 把 $M$ 的特征簇理解为奇异性在余切丛中的传播集合。  
   *为什么*：特征簇按定义刻画 $D$ 模解的各阶奇异性。
2. Riemann–Hilbert 对应把正则完整 $D$ 模送到其解层，并保持微局部奇异支撑。  
   *为什么*：该对应在奇异支撑层面是精确的。

> 缺口：讲义只陈述该等式，未给证明；它是微局部分析中的标准结果，讲义此处未注明出处，本章亦未展开。

*出处*：命题（§11.4，讲义无编号） / 原书 p.58–59


## 易错点

- 等式只对正则完整 $D$ 模陈述：讲义正是在这一情形给出 $\operatorname{SS}(\operatorname{Sol}(M))=\operatorname{Char}(M)$，不要把它推广到任意 $D$ 模上使用。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§11.4 层的微局部奇异支撑，p.58-59（PDF p.58-59），`源码/chapters/ch11.tex:86-89（SS(Sol)=Char，§11.4，跨 p.58–59）`

## 核验

状态：`source-only`（2026-11-18）
- nLab：https://ncatlab.org/nlab/show/holonomic+D-module — 『A D-module M on a smooth complex analytic variety X of dimension n is holonomic if its characteristic variety is of dimension n. It follows that the characteristic variety of a holonomic D-module is conic and lagrangian』——只给特征簇的定义与锥-Lagrange 性，没有 SS(Sol(M))=Char(M)。
- nLab：https://ncatlab.org/nlab/show/Riemann-Hilbert+correspondence — 『D^b_{rh}(X,D_X)≃D^b_c(X^an,C)』（Mebkhout/Kashiwara/Beilinson–Bernstein）——只给 RH 等价本身，全页未提解层的微局部支撑与特征簇相等。

## 关联

- `glc/concept/microlocal-singular-support`
- `glc/concept/quasi-lisse-sheaves`
