---
id: dmod/concept/holonomicity-under-tensor
type: concept
track: B
---

# 外张量积下的完整性

> 外张量积使 Bernstein 维数相加，因此两个完整模的外张量积仍完整；特征簇是两特征簇在重排坐标下的像。

**问题**：两个完整模的外张量积为什么仍完整，特征簇与维数在 $\boxtimes$ 下如何变化？

## 定义

设 $X=k^n$，$Y=k^m$，$D_X$、$D_Y$ 为相应的多项式系数微分算子代数。外张量积 $D_X\boxtimes D_Y$ 作为 $k$-向量空间等于 $D_X\otimes_kD_Y$，乘法为 $(T\otimes S)(T'\otimes S')=TT'\otimes SS'$，且 $D_X\boxtimes D_Y=D_{X\times Y}$（引理 9.1）。对 $D_X$-模 $M$ 与 $D_Y$-模 $N$，\emph{外张量积} $M\boxtimes N$ 作为 $k$-向量空间等于 $M\otimes_kN$，$D_{X\times Y}$ 的作用由 $(T\boxtimes S)(m\otimes n)=Tm\otimes Sn$ 给出；$M$、$N$ 有限生成时 $M\boxtimes N$ 是有限生成 $D_{X\times Y}$-模（引理 9.2）。

*记号*：$\boxtimes$ 是外张量积（张量在 $k$ 上、作用在 $X\times Y$ 上），不要与 $X$ 上的 $\mathcal O_X$-张量积混淆；$q:k^{2n}\times k^{2m}\to k^{2(n+m)}$ 把 $(x,\xi,y,\eta)$ 重排为 $(x,y,\xi,\eta)$；$P(M,t)$ 是 $\operatorname{Gr}M$ 的 Poincaré 级数。

## 要点

- 定理 9.3：$d(M\boxtimes N)=d(M)+d(N)$——维数在 $\boxtimes$ 下相加。
- 推论 9.4：若 $M$、$N$ 分别完整，则 $M\boxtimes N$ 是完整 $D_{X\times Y}$-模。
- 定理 9.7：$\operatorname{Ch}(M\boxtimes N)=q\bigl(\operatorname{Ch}(M)\times\operatorname{Ch}(N)\bigr)$。
- 命题 9.8：$\operatorname{supp}(M\boxtimes N)=\operatorname{supp}(M)\times\operatorname{supp}(N)$。
- 证明之一：乘积滤过是好滤过，且 $\operatorname{Gr}_j(M\boxtimes N)\cong\bigoplus_{p+q=j}\operatorname{Gr}_pM\otimes_k\operatorname{Gr}_qN$，故 Poincaré 级数相乘、在 $t=1$ 处极点阶相加。
- 证明之二：由 $\operatorname{Ch}$ 的乘积公式取维数，再用定理 7.7 得 9.3。

## 关键公式

- $d(M\boxtimes N)=d(M)+d(N)$
- $\operatorname{Ch}(M\boxtimes N)=q\bigl(\operatorname{Ch}(M)\times\operatorname{Ch}(N)\bigr)$
- $\operatorname{supp}(M\boxtimes N)=\operatorname{supp}(M)\times\operatorname{supp}(N)$
- $P(M\boxtimes N,t)=P(M,t)\,P(N,t)$
- $\operatorname{Gr}_j(M\boxtimes N)\cong\bigoplus_{p+q=j}\operatorname{Gr}_pM\otimes_k\operatorname{Gr}_qN$

## 定理与证明

### 定理 9.3（外张量积的维数可加）（完整）

设 $M$ 是有限生成 $D_X$-模，$N$ 是有限生成 $D_Y$-模，则 $$d(M\boxtimes N)=d(M)+d(N).$$

1. 取 $M$、$N$ 的好滤过，在 $M\boxtimes N$ 上定义乘积滤过 $F_j(M\boxtimes N)=\sum_{p+q=j}F_pM\otimes_kF_qN$。由引理 9.5（张量映射的核公式）得 $\operatorname{Gr}_j(M\boxtimes N)\cong\bigoplus_{p+q=j}\operatorname{Gr}_pM\otimes_k\operatorname{Gr}_qN$。  
   *为什么*：分次化的核恰为 $F_{j-1}$，逐分片取商即得直和分解。
2. 该乘积滤过是好的：$\operatorname{Gr}(M\boxtimes N)$ 是有限生成 $\operatorname{Gr}D_{X\times Y}$-模。  
   *为什么*：$\operatorname{Gr}M$、$\operatorname{Gr}N$ 有限生成，张量积仍有限生成，而 $\operatorname{Gr}D_X\boxtimes\operatorname{Gr}D_Y=\operatorname{Gr}D_{X\times Y}$。
3. 于是 Poincaré 级数相乘：$P(M\boxtimes N,t)=P(M,t)P(N,t)$。  
   *为什么*：直和分片的维数是两两维数之积，求和即得级数乘积。
4. 由 §1 的引理 1.5，$P$ 在 $t=1$ 处极点的阶等于维数，故极点的阶相加，即 $d(M\boxtimes N)=d(M)+d(N)$。  
   *为什么*：乘积的极点阶是两因子极点阶之和。

*出处*：定理 9.3 / 原书 p.37

### 定理 9.7（外张量积的特征簇）（完整）

设 $M$、$N$ 分别是有限生成 $D_X$-、$D_Y$-模，则 $$\operatorname{Ch}(M\boxtimes N)=q\bigl(\operatorname{Ch}(M)\times\operatorname{Ch}(N)\bigr).$$

1. 设 $I$、$J$ 分别是 $\operatorname{Gr}M$、$\operatorname{Gr}N$ 的零化子。由引理 9.5，$\operatorname{Gr}(M\boxtimes N)$ 的零化子是 $I\otimes_k\operatorname{Gr}D_Y+\operatorname{Gr}D_X\otimes_kJ$。  
   *为什么*：张量积的零化子由两因子的零化子生成（核公式的另一面）。
2. 把 $\operatorname{Gr}D_X$、$\operatorname{Gr}D_Y$、$\operatorname{Gr}D_{X\times Y}$ 分别与 $k[x,\xi]$、$k[y,\eta]$、$k[x,y,\xi,\eta]$ 等同，则该理想由 $I$ 与 $J$ 的像生成，其零点集是 $\operatorname{Ch}(M)\times\operatorname{Ch}(N)$ 在重排映射 $q$ 下的像。  
   *为什么*：$q$ 只是把 $\xi$ 块与 $y$ 块交换，是线性同构；零点集按生成元取。
3. 取维数并用定理 7.7 得 $\dim\operatorname{Ch}(M\boxtimes N)=\dim\operatorname{Ch}(M)+\dim\operatorname{Ch}(N)$，这给出 9.3 的另一个证明。  
   *为什么*：线性同构保持维数，乘积簇的维数是两因子维数之和。

*出处*：定理 9.7 / 原书 p.39


## 易错点

- $q$ 不是恒等映射：它交换 $\xi$ 块与 $y$ 块，直接写 $\operatorname{Ch}(M\boxtimes N)=\operatorname{Ch}(M)\times\operatorname{Ch}(N)$ 在坐标次序上是错的。
- 这里是**外**张量积（对象在 $X\times Y$ 上），不是 $X$ 上的 $\mathcal O_X$-张量积；维数相加而不是取最大。
- 完整性在 $\boxtimes$ 下封闭要经过 $d$ 可加与定理 7.7，不能由 $\operatorname{Ch}$ 的积「直接看出」。
- $\boxtimes$ 只对左模—左模等同类情形定义；混用左右模要先转置，转置保持 $d$ 但不保持 $M$ 本身。

## 出处

- Miličić《Lectures on the Algebraic Theory of D-Modules》（中译校订批注本，150 页），§9 外张量积，p.36-37-38-39（PDF p.42-43-44-45），`源码/chapters/chap1.tex:1313-1437（定理 9.3、9.4、9.7、9.8）`

## 核验

状态：`source-only`（2026-11-19）

## 关联

- `dmod/concept/holonomic-module`
- `dmod/concept/characteristic-variety`
- `dmod/concept/bernstein-dimension`
- `dmod/concept/preservation-of-holonomicity`
