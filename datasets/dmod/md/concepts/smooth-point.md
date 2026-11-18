---
id: dmod/concept/smooth-point
type: concept
track: C
---

# 光滑点

> 点 $x\in X$ 光滑指 $\dim_kT_x(X)=\dim_xX$，等价于局部环 $\mathcal O_x$ 正则；光滑点集开稠密，且每个光滑点只落在一个不可约分支中。

**问题**：切空间维数在每点都不小于局部维数，为什么等号成立的点既构成开稠密集、又不能落在两个不可约分支的交上？

## 定义

设 $X$ 是特征零代数闭域 $k$ 上的代数簇，$T_x(X)$ 是 $x$ 处的 Zariski 切空间。称 $x$ 是光滑点，若 $\dim_kT_x(X)=\dim_xX$；等价地，局部环 $\mathcal O_x$ 是正则的。若 $X$ 的每点都光滑，称 $X$ 为光滑簇。$X$ 总可局部嵌入某个 $k^n$，此时 $T_x(X)$ 由定义 $X$ 的理想 $I$ 中多项式在 $x$ 处的一阶偏导刻画（引理 2.5）。

*记号*：$T_x(X)$：$x$ 处的 Zariski 切空间；$\dim_xX$：$x$ 处局部维数；$I$：$X\subset k^n$ 的消没理想；$T_x(j)$：包含 $j:X\to k^n$ 的切映射。

## 要点

- 恒有 $\dim_kT_x(X)\ge\dim_xX$（命题 2.2），故光滑就是等号成立。
- 嵌入 $k^n$ 时 $T_x(X)=\{\xi\in k^n:\sum_i\xi_i(\partial_iP)(x)=0,\ P\in I\}$，切空间由理想的一阶偏导线性方程给出（引理 2.5）。
- $x\mapsto\dim_kT_x(X)$ 上半连续（命题 2.6），这给出光滑点集的开性。
- 光滑点集在 $X$ 中开且稠密；光滑点含于 $X$ 的唯一不可约分支中（定理 2.7）。
- 光滑点处存在坐标系 $(f_1,\dots,f_n;D_1,\dots,D_n)$，满足 $D_i(f_j)=\delta_{ij}$（定理 2.9），这是第三章主符号计算的局部基础。

## 关键公式

- $\dim_kT_x(X)=\dim_xX$
- $T_x(X)=\Bigl\{\xi\in k^n\ \Big|\ \sum_{i=1}^n\xi_i(\partial_iP)(x)=0,\ P\in I\Bigr\}$
- $D_i(f_j)=\delta_{ij},\qquad [D_i,D_j]=0$

## 定理与证明

### 引理 2.5（切空间的方程刻画）（完整）

设 $X\subset k^n$ 是闭子簇，$I$ 是 $k[X_1,\dots,X_n]$ 中在 $X$ 上消失的多项式理想，$x\in X$。则 $T_x(X)=\{(\xi_1,\dots,\xi_n)\in k^n:\sum_i\xi_i(\partial_iP)(x)=0\ \text{对一切}\ P\in I\}$。

1. 由引理 2.4(ii)，把 $T_x(X)$ 经 $T_x(j)$ 等同于 $k^n$ 中 $T^*_x(j):k^n\to T^*_x(X)$ 的核的正交补。  
   *为什么*：切映射与余切映射互为对偶，切空间是余切映射核的正交补。
2. $\ker T^*_x(j)=\{\mathrm df(x)\mid f\in I_x\}$；$I_x$ 中元素是 $P/Q$（$P\in I$，$Q(x)\neq0$），故 $\mathrm df(x)=Q(x)^{-1}\mathrm dP(x)$，该核等于 $\{\mathrm dP(x)\mid P\in I\}$。  
   *为什么*：局部化的分母在 $x$ 处可逆，取一阶微分后只差一个非零常数，故张成的子空间不变。
3. 正交补条件即 $\sum_i\xi_i(\partial_iP)(x)=0$ 对一切 $P\in I$ 成立，因为 $\mathrm dP(x)=(\partial_1P(x),\dots,\partial_nP(x))$。  
   *为什么*：内积写出的正交关系正是这组线性方程，两者互相决定。

*出处*：引理 2.5 / chap2.tex:322-329

### 定理 2.7（光滑点的分布）（要点（有缺口））

设 $X$ 是 $k$ 上的代数簇。则 (i) $X$ 的所有光滑点之集在 $X$ 中开且稠密；(ii) 光滑点 $x\in X$ 含于 $X$ 的唯一不可约分支中。

1. 由命题 2.6 上半连续性与命题 2.2 的下界 $\dim_kT_x(X)\ge\dim_xX$，光滑点集是开集。  
   *为什么*：$\dim_kT_x(X)$ 在每点不小于局部维数，等号成立处是上半连续函数的「最低层」。
2. 稠密性与 (ii) 要在每个不可约分支上分别论证，分支内部的点才可能光滑。  
   *为什么*：不可约分支是闭的，光滑性在分支上定义为局部维数与切空间维数相等。

> 缺口：讲义在 chap2.tex:345-405 给出完整证明（含稠密性与唯一分支部分），本卡只记录陈述与两条可直接引用的中间事实（命题 2.2、2.6）。

*出处*：定理 2.7 / chap2.tex:345-405


## 易错点

- 光滑性是点上的性质而非 $X$ 整体的性质：先有上半连续性，才能谈「光滑点集开」。
- 公式里的 $\dim_xX$ 是 $x$ 处的局部维数，不是 $X$ 的整体维数；在分支相交处两者不同。
- 光滑点不能跨分支：定理 2.7(ii) 说光滑点只含于唯一不可约分支，故两个分支的交点必非光滑点。

## 出处

- Miličić《Lectures on the Algebraic Theory of D-Modules》中译本，第 II 章 §2 代数簇的光滑点，p.62（PDF p.68），`源码/chapters/chap2.tex:322-350（引理 2.5 与定理 2.7）`

## 核验

状态：`source-only`（2026-11-19）

## 关联

- `dmod/concept/graded-dz-on-smooth`
- `dmod/concept/dz-structure-sheaf`
