# 用 $\mathbb{R}$-滤过代替谱

`kshms/remark/rmk-20-spectrum-filtration` · track F（同调镜像猜想） · 原文 注 20

**问题**　§8.2 用谱 $\mathrm{Sp}_y(\alpha)$ 组织态射，能不能只用态射空间自身的滤过说同一件事？

**摘要**　不必用谱，也可以在态射空间上取 $\mathbb{R}$-滤过 $\mathrm{Hom}(E_1,E_2)^{\le s}$：它由态射层完备张量积的茎上的一族不等式定义，且 $\alpha$ 落在第 $s$ 层当且仅当对每个 $y$ 都有 $\mathrm{Sp}_y(\alpha)\subset(-\infty,s]$。

**别名**　Remark 20；$\mathbb{R}$-filtration on Hom spaces；谱 $\mathrm{Sp}_y$ 的等价刻画

## 陈述

可以不用谱，而在态射空间上使用一个 $\mathbb{R}$-滤过 $\mathrm{Hom}_{C(Y)}(E_1,E_2)^{\le s}$。它来自态射层 $\underline{\mathrm{Hom}}_{\mathcal{O}_Y}(E_1,E_2)\widehat{\otimes}\widehat{\Omega}^{*}_Y$（完备张量积）的茎上的滤过，后者由条件 $\{-\lambda_{j,i_1\dots i_n}+\sum_{1\le k\le n}i_ky_k+f_1(y)-f_2(y)\}\le s$ 定义。容易看出，$\alpha$ 属于 $\mathrm{Hom}_{C(Y)}(E_1,E_2)^{\le s}$ 当且仅当对所有 $y\in Y$ 都有 $\mathrm{Sp}_y(\alpha)\subset(-\infty,s]$。

## 这条注在全文中的作用

把「逐点的谱」换成「整体滤过」，是为了让 $\varphi^t$ 这类几何操作（沿 $\xi_\gamma$ 的 Lie 导数）在态射空间上有干净的作用域：滤过给出一个可作极限（$t\to+\infty$）的框架，而不必每次追到每个 $y$ 的指数集合。它是 §8.2 半群构造的技术前提。

## 易错点

- 滤过定义里的 $"\{\cdot\}\le s"$ 指的是花括号内那一串指数取值的上界，不要误读成模长或绝对值。
- 两个说法等价（滤过 ↔ 谱含于 $(-\infty,s]$）只在上述茎的完备张量积描述下成立；换一种态射层的表示，常数项要对齐。
- 这是作者顺手给出的等价表述，没有证明细节；用它时要回到 $\mathrm{Sp}_y$ 的定义核对。

## 相关卡

- `kshms/remark/rmk-22-asymptotic-coefficients`

## 出处

- Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25） §8.2（原文 p.54）；锚点 `源码/chunks/ch09.tex:104-112（注 20）`

> 原文 p54 §8.2；译本 p41。
