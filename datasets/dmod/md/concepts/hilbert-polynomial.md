---
id: dmod/concept/hilbert-polynomial
type: concept
track: O
---

# Hilbert 多项式与 Poincaré 级数

> 分次诺特环上有限生成模的 Poincaré 级数是有理函数；生成元次数全为 $1$ 时，各次分量的可加函数最终等于一条多项式，其次数与首项系数给出维数和重数。

**问题**：为什么分次模各次分量的长度最终由一条多项式给出，这条多项式的次数与首项系数又编码了什么？

## 定义

设 $A=\bigoplus_{n\in\mathbb{Z}}A^n$ 是分次诺特交换环，$1\in A^0$，且 $n<0$ 时 $A^n=0$。设 $\lambda$ 是有限生成 $A^0$-模上的可加函数，即对任意短正合列 $0\to M'\to M\to M''\to 0$ 有 $\lambda(M)=\lambda(M')+\lambda(M'')$。对有限生成分次 $A$-模 $M=\bigoplus_{n\in\mathbb{Z}}M^n$ 定义其 Poincaré 级数 $$P(M,t)=\sum_{n\in\mathbb{Z}}\lambda(M^n)\,t^n\in\mathbb{Z}((t)).$$ 设 $x_1,\dots,x_s$ 是 $A_+=\bigoplus_{n\ge1}A^n$ 的齐次生成元，$d_i=\deg x_i$。当所有 $d_i=1$ 时，$\lambda(M^n)$ 对充分大的 $n$ 等于一条有理系数多项式，称为 $M$ 关于 $\lambda$ 的 Hilbert 多项式。

*记号*：$\lambda$：有限生成 $A^0$-模上的可加函数，常用 $\lambda=\dim_k$（$A^0=k$ 为域）或 $\lambda=\operatorname{length}$；$d_\lambda(M)$：$P(M,t)$ 在 $t=1$ 处极点的阶数，等于 Hilbert 多项式的次数加 $1$；$g(t)$：$f(t)=(1-t)^p g(t)$ 中满足 $g(1)\neq0$ 的因子。

## 要点

- 引理 1.1：$A^0$ 是诺特环，且 $A$ 是有限生成 $A^0$-代数；其逆命题由 Hilbert 基定理给出。
- 引理 1.2：有限生成分次 $A$-模的每个 $M^n$ 都是有限生成 $A^0$-模，故 $\lambda(M^n)$ 有定义且当 $n$ 充分负时为零。
- 定理 1.4（Hilbert–Serre）：$P(M,t)$ 是有理函数，分母可取 $\prod_{i=1}^s(1-t^{d_i})$，分子在 $\mathbb{Z}[t,t^{-1}]$ 中。
- 推论 1.5：若所有 $d_i=1$，则 $\lambda(M^n)$ 对充分大的 $n$ 是次数为 $d_\lambda(M)-1$ 的多项式，首项系数为 $g(1)/(d_\lambda(M)-1)!$。
- 对 $A=k[X_1,\dots,X_s]$（全次数分次）有 $P(A,t)=(1-t)^{-s}$，因此 $d_{\dim_k}(A)=s$，Hilbert 多项式次数为 $s-1$。

## 关键公式

- $P(M,t)=\sum_{n\in\mathbb{Z}}\lambda(M^n)\,t^n$
- $P(M,t)=\frac{f(t)}{\prod_{i=1}^s(1-t^{d_i})},\qquad f(t)\in\mathbb{Z}[t,t^{-1}]$
- $(1-t^{d_s})P(M,t)=P(L,t)-t^{d_s}P(K,t)$
- $\lambda(M^n)=\sum_{k=-N}^{N}a_k\binom{d+n-k-1}{d-1}\quad(n\gg0)$
- $P(k[X_1,\dots,X_s],t)=\frac{1}{(1-t)^s},\qquad \dim_k A^n=\binom{n+s-1}{s-1}$

## 定理与证明

### 定理 1.4（Hilbert–Serre）（完整）

对任意有限生成分次 $A$-模 $M$，存在 $f(t)\in\mathbb{Z}[t,t^{-1}]$ 使得 $$P(M,t)=\frac{f(t)}{\prod_{i=1}^s(1-t^{d_i})}.$$

1. 对生成元个数 $s$ 归纳。$s=0$ 时 $A=A^0$，$M$ 是有限生成 $A^0$-模，故 $n$ 充分大时 $M^n=0$，于是 $P(M,t)\in\mathbb{Z}[t,t^{-1}]$，取分母为空积即可。  
   *为什么*：$A_+=0$ 时无正次数部分；有限生成模在 $A^0$ 上只有有限多个非零齐次分量。
2. 设 $s>0$。乘以 $x_s$ 给出保次 $d_s$ 的 $A$-模自同态 $f:M\to M$，置 $K=\ker f$、$L=\operatorname{coker}f$，得正合列 $0\to K\to M\xrightarrow{f}M\to L\to0$。  
   *为什么*：核与余核都是分次 $A$-模，且 $f$ 保分次，故正合列逐次成立。
3. 取 $n$ 次齐次部分得 $A^0$-模正合列 $0\to K^n\to M^n\xrightarrow{x_s}M^{n+d_s}\to L^{n+d_s}\to0$，由 $\lambda$ 可加性得 $\lambda(K^n)-\lambda(M^n)+\lambda(M^{n+d_s})-\lambda(L^{n+d_s})=0$。  
   *为什么*：正合列中交错和为 $0$ 是 $\lambda$ 可加性的直接推论（引理 1.3）。
4. 乘以 $t^n$ 并对 $n$ 求和，左端化为 $(1-t^{d_s})P(M,t)$，右端化为 $P(L,t)-t^{d_s}P(K,t)$。  
   *为什么*：两个求和分别是 $P(M,t)$ 与 $t^{d_s}P(M,t)$ 的移项，以及 $P(L,t)$ 与 $t^{d_s}P(K,t)$ 的移项。
5. $x_s$ 在 $K$ 与 $L$ 上的作用为零，故二者可看作 $A/(x_s)$-模；$A/(x_s)$ 由 $s-1$ 个生成元生成，用归纳假设即得结论。  
   *为什么*：$K$ 上 $x_s$ 按定义为零；$L$ 上 $x_s$ 是商映射后的零映射。归纳假设给出分母 $\prod_{i<s}(1-t^{d_i})$。

*出处*：定理 1.4 / 原书 p.2

### 推论 1.5（Hilbert 多项式的次数与首项）（完整）

若 $d_i=1$（$1\le i\le s$），则 $n\mapsto\lambda(M^n)$ 对充分大的 $n\in\mathbb{Z}$ 等于一条有理系数多项式，其次数为 $d_\lambda(M)-1$，首项系数为 $g(1)/(d_\lambda(M)-1)!$。

1. 写 $f(t)=(1-t)^p g(t)$，$g(1)\neq0$，并令 $d=d_\lambda(M)=s-p$，则 $P(M,t)=g(t)/(1-t)^d$。  
   *为什么*：$p$ 是 $f$ 在 $1$ 处零点的阶数，而 $P$ 在 $1$ 处的极点阶数正是 $s-p$。
2. 用 $(1-t)^{-d}=\sum_{k\ge0}\binom{d+k-1}{d-1}t^k$ 与 $g(t)=\sum_{k=-N}^{N}a_k t^k$ 作卷积，得 $\lambda(M^n)=\sum_{k=-N}^{N}a_k\binom{d+n-k-1}{d-1}$（$n\ge N$）。  
   *为什么*：形式幂级数乘法逐项相加；$g$ 只有有限多项，故 $n$ 充分大时每一项都有定义。
3. 把二项式系数写成 $(n-k+1)\cdots(n-k+d-1)/(d-1)!$，即得 $n$ 的多项式，次数 $d-1$，首项系数 $g(1)/(d-1)!\neq0$。  
   *为什么*：每个因子是 $n$ 的一次多项式，$d-1$ 个因子相乘给出首项 $n^{d-1}/(d-1)!$，系数求和为 $g(1)$。

*出处*：推论 1.5 / 原书 p.3


## 易错点

- $d_\lambda(M)$ 是 $P(M,t)$ 在 $t=1$ 处极点的阶数，Hilbert 多项式的次数是 $d_\lambda(M)-1$；把两者混同会把 $k[X_1,\dots,X_s]$ 的维数算成 $s$ 而非 $s-1$。
- Poincaré 级数只是形式幂级数：多项式只在 $n$ 充分大时等于 $\lambda(M^n)$，不能反过来用它计算小的 $n$。
- 可加函数 $\lambda$ 必须取值于 $\mathbb{Z}$ 且对短正合列可加；$\lambda=\dim_k$ 仅在 $A^0$ 为域时可用，一般 $A^0$ 上应取 $\operatorname{length}$。
- 定理只保证分子 $f\in\mathbb{Z}[t,t^{-1}]$ 存在，不保证其系数非负；首项系数 $g(1)/(d-1)!$ 一般是有理数而非整数。

## 出处

- Miličić《Lectures on the Algebraic Theory of D-Modules》（中译本，校订批注本），§1 Hilbert 多项式，p.1-2-3-4-5（PDF p.7-8-9-10-11），`源码/chapters/chap1.tex:3-175（定理 1.4、推论 1.5）`

## 核验

状态：`source-only`（2026-11-19）

## 关联

- `dmod/concept/krull-dimension-and-multiplicity`
- `dmod/concept/associated-graded-ring`
- `dmod/concept/dimension-theory-of-filtered-modules`
