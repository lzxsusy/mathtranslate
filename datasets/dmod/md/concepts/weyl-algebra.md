---
id: dmod/concept/weyl-algebra
type: concept
track: A
---

# Weyl 代数 $D(n)$

> $D(n)=k[X]\langle\partial\rangle$ 由 $[\partial_i,X_j]=\delta_{ij}$ 及其余交换关系定义；$X^I\partial^J$ 是 $k$-基，中心为 $k$。

**问题**：多项式环上的微分算子构成什么代数？它由哪些生成元与关系刻画，唯一性（基）与对称性（自同构）从何而来？

## 定义

设 $k$ 是域，$A=k[X_1,\dots,X_n]$。$A$ 上 $k$-线性微分算子环 $D(n)=\operatorname{Diff}_k(A)$ 是由 $X_i$（乘子）与 $\partial_i=\partial/\partial X_i$ 生成的 $k$-代数：$X_i$ 是乘子，$\partial_i$ 是形式偏导，满足 $$[X_i,X_j]=0,\qquad[\partial_i,\partial_j]=0,\qquad[\partial_i,X_j]=\delta_{ij}.$$ 等价地，$D(n)$ 是以 $(X^I\partial^J;\ I,J\in\mathbb{Z}_+^n)$ 为 $k$-基、乘法由上述关系决定的结合代数。它是 $\mathcal D_{\mathbb{A}^n}$ 的整体截面，也是 §5 讨论的算子环的原型。

*记号*：$X^I=X_1^{I_1}\cdots X_n^{I_n}$，$\partial^J=\partial_1^{J_1}\cdots\partial_n^{J_n}$，$|I|=\sum I_i$；$Z(D(n))$：中心；$D(n)^\circ$：反代数；$\varphi$：主反自同构；$F$：Fourier 自同构。

## 要点

- 定理 5.10：$(X^I\partial^J;\ I,J\in\mathbb{Z}_+^n)$ 构成 $D(n)$ 作为 $k$-向量空间的一组基，故每个算子有唯一的规范形 $\sum_{I,J}a_{IJ}X^I\partial^J$（$\partial$ 全部在右）。
- 定理 5.11：$D(n)$ 就是由 $X_i,\partial_j$ 生成、满足上述三条关系的 $k$-代数；这是 $D(n)$ 的泛性质刻画。
- 命题 5.12：$D(n)$ 的中心等于 $k\cdot1$。
- 命题 5.13：主反自同构 $\varphi:D(n)^\circ\to D(n)$，$\varphi(X_i)=X_i$、$\varphi(\partial_i)=-\partial_i$，给出 $D(n)^\circ\cong D(n)$。
- Fourier 自同构 $F(X_i)=\partial_i$、$F(\partial_i)=-X_i$ 满足 $F^2=\iota$，其中 $\iota(X_i)=-X_i$、$\iota(\partial_i)=-\partial_i$，$\iota^2=1$。

## 关键公式

- $D(n)=k[X_1,\dots,X_n]\langle\partial_1,\dots,\partial_n\rangle$
- $[\partial_i,X_j]=\delta_{ij},\qquad[X_i,X_j]=[\partial_i,\partial_j]=0$
- $D(n)=\bigoplus_{I,J\in\mathbb{Z}_+^n}k\,X^I\partial^J$
- $Z(D(n))=k\cdot1$
- $\varphi(X_i)=X_i,\ \varphi(\partial_i)=-\partial_i;\qquad F(X_i)=\partial_i,\ F(\partial_i)=-X_i,\ F^2=\iota$

## 定理与证明

### 定理 5.10（规范形基）（完整）

$(X^I\partial^J;\ I,J\in\mathbb{Z}_+^n)$ 构成 $D(n)$ 作为 $k$-向量空间的一组基。

1. 这族元素张成 $D(n)$：$D(n)$ 由 $X_i,\partial_j$ 生成，而任何由它们构成的长积都可通过关系 $\partial_iX_j=X_j\partial_i+\delta_{ij}$ 与 $X_iX_j=X_jX_i$、$\partial_i\partial_j=\partial_j\partial_i$ 归约为 $X^I\partial^J$ 的 $k$-线性组合。  
   *为什么*：每次把 $\partial$ 向左交换到 $X$ 的右侧只产生低一次项，归纳即得规范形。
2. 设 $\sum_{I,J}a_{IJ}X^I\partial^J=0$ 是 $k$ 上的线性关系。按 $|J|=p$ 分组，取 $p$ 最大的非零组。  
   *为什么*：只有有限多个 $J$ 出现，故最大次数组有意义。
3. 对 $T=\sum_{|J|=p}a_{IJ}X^I\partial^J$ 取 $p$-主符号（5.6）：$\operatorname{Symb}_p(T)=\sum_{|J|=p}a_{IJ}X^I\xi^J$。由 $T=0$ 得 $\operatorname{Symb}_p(T)=0$。  
   *为什么*：主符号对 $k$-线性组合线性，且零算子的主符号为零。
4. $(X^I\xi^J;\ I,J\in\mathbb{Z}_+^n)$ 是 $k[X,\xi]$ 的 $k$-基，故该组系数 $a_{IJ}$ 全为零；对 $p$ 递降归纳即得所有系数为零。  
   *为什么*：多项式环的单式构成基；最大组消去后对剩余关系重复同一论证。

*出处*：定理 5.10 / 原书 p.22

### 定理 5.11（生成元与关系的刻画）（完整）

$k$-代数 $D(n)$ 是由 $X_1,\dots,X_n$ 与 $\partial_1,\dots,\partial_n$ 生成、满足 $[X_i,X_j]=0$、$[\partial_i,\partial_j]=0$、$[\partial_i,X_j]=\delta_{ij}$ 的 $k$-代数。

1. 设 $B$ 是由同样的生成元与关系给出的 $k$-代数。三条关系在 $D(n)$ 中成立，且 $D(n)$ 由这些元素生成，故存在唯一的 $k$-代数满射 $B\to D(n)$，把生成元映到相应生成元。  
   *为什么*：自由代数到 $D(n)$ 的映射由生成元的像决定，关系落在核中才诱导出 $B$ 上的映射；满射性因像含生成元。
2. $B$ 由 $X^I\partial^J$ 张成：关系允许把任意字归约为规范形，与第 1 步中 $D(n)$ 的情形相同。  
   *为什么*：$B$ 中同样的交换与 Leibniz 关系成立，故同一归约算法可用。
3. 由 5.10，$X^I\partial^J$ 在 $D(n)$ 中 $k$-线性无关，故第 1 步的满射是单射，从而是同构。  
   *为什么*：满射把 $B$ 的生成族送到 $D(n)$ 的基，基的线性无关性迫使核为零。

*出处*：定理 5.11 / 原书 p.22

### 命题 5.12（中心）（完整）

$Z(D(n))=k\cdot1$。

1. 设 $T\in Z(D(n))$。则 $[T,P]=0$ 对一切 $P\in k[X_1,\dots,X_n]$ 成立，特别地 $\sigma_p(T)=0$（$p=\operatorname{ord}T$），由 5.8 得 $\operatorname{ord}T\le0$，即 $T\in k[X_1,\dots,X_n]$。  
   *为什么*：$\sigma_p(T)(P,\dots,P)=[\cdots[T,P]\cdots,P]=0$；5.8 断言 $\operatorname{Symb}_p(T)=0$ 当且仅当阶数 $<p$。
2. 又 $0=[\partial_i,T]=\partial_i T- T\partial_i=\partial_i(T)$，即 $T$ 的所有一阶偏导为零。  
   *为什么*：$T$ 是多项式，$[\partial_i,T]$ 按 Leibniz 法则等于 $\partial_i(T)$ 作为乘子。
3. $k$ 是域，偏导为零的多项式必为常数，故 $T\in k$；反向包含显然。  
   *为什么*：特征零域上多元多项式的一阶偏导全为零蕴含它是常数（对每个变量单独积分）。

*出处*：命题 5.12 / 原书 p.22


## 易错点

- 关系的符号约定：$[\partial_i,X_j]=\delta_{ij}$ 即 $\partial_iX_j=X_j\partial_i+\delta_{ij}$；若写成 $[X_j,\partial_i]=\delta_{ij}$，则主反自同构与 Fourier 自同构的公式整体差一个符号。
- $X^I\partial^J$ 是基，但乘积的规范形需要把 $\partial$ 全部移到右侧，交换会产生低次项；直接令 $\partial^JX^I=X^I\partial^J$ 是常见错误。
- 中心为 $k\cdot1$ 的证明用到 $k$ 是域（特征零）这一默认假设；正特征时中心严格大于 $k$，命题 5.12 不能照搬。
- $D(n)$ 是有限生成 $k$-代数但不是有限维 $k$-代数；只有 Bernstein 层 $D_p(n)$ 才有限维，讨论 Hilbert 多项式时必须区分“阶”与“全次数”。

## 出处

- Miličić《Lectures on the Algebraic Theory of D-Modules》（中译本，校订批注本），§5 多项式系数微分算子环，p.22-23（PDF p.28-29），`源码/chapters/chap1.tex:819-855（定理 5.10、5.11、命题 5.12、5.13）`

## 核验

状态：`source-only`（2026-11-19）

## 关联

- `dmod/concept/ring-of-differential-operators-polynomial`
- `dmod/concept/order-filtration-of-dn`
- `dmod/concept/symbol-and-principal-symbol`
- `dmod/concept/noetherianity-of-dn`
