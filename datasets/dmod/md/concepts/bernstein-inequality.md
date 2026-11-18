---
id: dmod/concept/bernstein-inequality
type: concept
track: E
---

# Bernstein 不等式

> 凝聚 $\mathcal D_X$-模的特征簇在支集每一点的纤维维数不低于底空间维数，等价于完整亏格非负，这是 D-模理论的根本估计。

**问题**：为什么非零凝聚 $\mathcal D_X$-模的特征簇不会比底空间「更小」？

## 定义

设 $X$ 是光滑簇，$p_X:T^*X\to X$ 是余切丛投影。对凝聚 $\mathcal D_X$-模 $\mathcal V$ 与点 $x\in\operatorname{supp}(\mathcal V)$，Bernstein 不等式断言 $$\dim_{p_X^{-1}(x)}\operatorname{Ch}(\mathcal V)\ge\dim_xX.$$ 用完整亏格写就是 $\operatorname{holdef}_x(\mathcal V)\ge0$。

*记号*：$p_X^{-1}(x)=T_x^*X$：$x$ 处的余切纤维；$\dim_{p_X^{-1}(x)}\operatorname{Ch}(\mathcal V)$：$\operatorname{Ch}(\mathcal V)\cap T_x^*X$ 在 $x$ 处的局部维数；$\operatorname{holdef}_x$：完整亏格 $\dim_{p_X^{-1}(x)}\operatorname{Ch}(\mathcal V)-\dim_xX$。

## 要点

- 断言只针对支集内的点：$x\notin\operatorname{supp}(\mathcal V)$ 时 $\operatorname{holdef}_x(\mathcal V)=-\dim_xX$，不等式不成立。
- 等价形式是 $\operatorname{holdef}_x(\mathcal V)\ge0$；在支集上处处取等号正是完整模的定义（第 V 章）。
- 证明分三步：局部化到仿射邻域、闭嵌入到 $k^n$、再用完整亏格在闭浸入直像下的不变性把待证不等式化成 $\dim\operatorname{Ch}(i_+(\mathcal V|_U))\ge n$。
- 它是 $\mathcal D_X$ 上 Bernstein 维数下界 $d(M)\ge n$ 的几何对应物；讲义称其为对 D-模理论具有根本重要性的结果（§7 开篇）。

## 关键公式

- $\dim_{p_X^{-1}(x)}\operatorname{Ch}(\mathcal V)\ge\dim_xX$
- $\operatorname{holdef}_x(\mathcal V)=\dim_{p_X^{-1}(x)}\operatorname{Ch}(\mathcal V)-\dim_xX\ge0$
- $\dim\operatorname{Ch}(i_+(\mathcal V|_U))-n=\operatorname{holdef}_x(\mathcal V|_U)$

## 定理与证明

### 定理 4.7.1（Bernstein 不等式）（完整）

设 $\mathcal V$ 是凝聚 $\mathcal D_X$-模。则对任意 $x\in\operatorname{supp}(\mathcal V)$ 有 $$\dim_{p_X^{-1}(x)}\operatorname{Ch}(\mathcal V)\ge\dim_xX.$$

1. 取 $x\in\operatorname{supp}(\mathcal V)$ 与 $x$ 的连通开仿射邻域 $U$，使 $p_X^{-1}(U)$ 只与 $\operatorname{Ch}(\mathcal V)$ 中同 $p_X^{-1}(x)$ 相交的不可约分支相交。  
   *为什么*：这样 $\dim U=\dim_xX$，且 $\dim\operatorname{Ch}(\mathcal V|_U)=\dim_{p_X^{-1}(x)}\operatorname{Ch}(\mathcal V)$，问题可整体搬到 $U$ 上而两个维数都不变，故只需对 $\mathcal V|_U$ 证明。
2. 把仿射光滑簇 $U$ 写成某个 $k^n$（$n\in\mathbb Z_+$）的闭光滑子簇，取相应的闭浸入 $i:U\to k^n$。  
   *为什么*：仿射光滑簇可闭嵌入仿射空间，从而把问题化到余切丛结构已知的 $k^n$ 上。
3. 对齐两个差：$\dim_{p_X^{-1}(x)}\operatorname{Ch}(\mathcal V)-\dim_xX=\dim_{p_U^{-1}(x)}\operatorname{Ch}(\mathcal V|_U)-\dim_xU=\operatorname{holdef}_x(\mathcal V|_U)$。  
   *为什么*：「纤维维数减底维数」之差在第一步的局部化下不变，故待证不等式等价于 $\operatorname{holdef}_x(\mathcal V|_U)\ge0$。
4. 用闭浸入直像的完整亏格不变性：$\operatorname{holdef}_x(\mathcal V|_U)=\operatorname{holdef}_x(i_+(\mathcal V|_U))=\dim\operatorname{Ch}(i_+(\mathcal V|_U))-n$。  
   *为什么*：由推论 4.6.9 与定理 4.6.8 的纤维维数公式，$\operatorname{codim}$ 项在两边相消（即 $\operatorname{Ch}(i_+(\mathcal V|_U))=\operatorname{Ch}(\mathcal V|_U)\times k^{n-\dim U}$ 的纤维形式），问题化为 $T^*k^n$ 中的一个整体维数估计。
5. 由前述结果得 $\dim\operatorname{Ch}(i_+(\mathcal V|_U))\ge n$，于是 $\dim_{p_X^{-1}(x)}\operatorname{Ch}(\mathcal V)\ge\dim_xX$。  
   *为什么*：这一步讲义只写「由前述可知」，未逐字展开（原书此处把 $\dim$ 漏写成 $\operatorname{Ch}(i_+(\mathcal V|_U))\ge n$，量纲不严，校订批注已指出）；本卡按量纲正确的形式抄录，不补证。

*出处*：定理 4.7.1 / 原书 §7, p.119–120


## 易错点

- 只对 $x\in\operatorname{supp}(\mathcal V)$ 成立；在支集外 $\operatorname{holdef}_x=-\dim_xX$ 可以任意负，把不等式写成「对一切 $x$ 成立」是错的。
- 原文末步写作 $\operatorname{Ch}(i_+(\mathcal V|_U))\ge n$，漏掉 $\dim$；引用时要补成 $\dim\operatorname{Ch}(i_+(\mathcal V|_U))\ge n$，否则量纲不成立。
- 不等式只是维数下界，不能推出 $\operatorname{Ch}(\mathcal V)$ 含零截面；使特征簇恰为 $n$ 维的是完整模。
- 这里的 $n$ 是闭嵌入后仿射空间的维数，不是 $X$ 的维数；两步归约中符号容易混。

## 出处

- Miličić《Lectures on the Algebraic Theory of D-Modules》（中译本，校订批注本），§7 Bernstein 不等式，p.119–120（PDF p.125–126），`源码/chapters/chap4.tex:991-1014（定理 4.7.1）`

## 核验

状态：`source-only`（2026-11-19）

## 关联

- `dmod/concept/holonomic-defect`
- `dmod/concept/bernstein-dimension-bound`
- `dmod/concept/kashiwara-theorem`
