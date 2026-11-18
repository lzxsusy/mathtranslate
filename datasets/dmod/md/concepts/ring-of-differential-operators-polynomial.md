---
id: dmod/concept/ring-of-differential-operators-polynomial
type: concept
track: A
---

# 微分算子环 $\operatorname{Diff}_k(A)$

> 对交换 $k$-代数 $A$，用嵌套换位子定义阶数 $\le n$ 的微分算子，其全体构成子代数 $\operatorname{Diff}_k(A)$，阶数给出滤过。

**问题**：不依赖坐标，怎样在一个交换 $k$-代数上定义“微分算子”及其阶数？这样得到的集合为什么对乘法封闭？

## 定义

设 $k$ 是特征 $0$ 的域，$A$ 是交换 $k$-代数，$\operatorname{End}_k(A)$ 配换位子 $[S,T]=ST-TS$。称 $T\in\operatorname{End}_k(A)$ 是 $A$ 上阶数 $\le n$ 的 $k$-线性微分算子，若对任意 $a_0,a_1,\dots,a_n\in A$ 有 $$[\cdots[[T,a_0],a_1],\dots,a_n]=0,$$ 其中 $a\in A$ 通过左乘作用。记 $\operatorname{Diff}_k(A)$ 为所有这些算子的并，并置 $$F_n\operatorname{Diff}_k(A)=\{T\in\operatorname{Diff}_k(A)\mid\operatorname{order}(T)\le n\}\quad(n\ge0),$$ $n<0$ 时取 $0$。

*记号*：$\operatorname{order}(T)$：使嵌套换位子全为零的最小 $n$；$\operatorname{Der}_k(A)$：$k$-导子空间，即满足 $T(ab)=T(a)b+aT(b)$ 的 $T$；$\operatorname{End}_A(A)$：$A$-线性自同态，与 $A$ 等同（引理 5.1）。

## 要点

- 引理 5.1：$a\mapsto(b\mapsto ab)$ 是 $A$ 到 $\operatorname{End}_A(A)$ 的代数同构，故 $A$-线性自同态就是乘子。
- 引理 5.2：若 $T,S$ 阶数分别 $\le n,\le m$，则 $T\circ S$ 阶数 $\le n+m$；因此 $\operatorname{Diff}_k(A)$ 是 $\operatorname{End}_k(A)$ 的子代数，阶数给出与环结构相容的滤过。
- 引理 5.3：$F_0\operatorname{Diff}_k(A)=A$，$F_1\operatorname{Diff}_k(A)=\operatorname{Der}_k(A)\oplus A$，且 $[F_n,F_m]\subset F_{n+m-1}$。
- 由 $[F_n,F_m]\subset F_{n+m-1}$ 知 $\operatorname{Gr}\operatorname{Diff}_k(A)$ 是交换 $A$-代数，$\operatorname{Diff}_k(A)$ 满足 §3 的 (i)–(v)。
- 引理 5.5：当 $A=k[X_1,\dots,X_n]$ 时，$(\partial_1,\dots,\partial_n)$ 是自由 $A$-模 $\operatorname{Der}_k(A)$ 的一组基；此时 $\operatorname{Diff}_k(A)=D(n)$。

## 关键公式

- $[\cdots[[T,a_0],a_1],\dots,a_n]=0\quad(\forall a_0,\dots,a_n\in A)$
- $F_n\operatorname{Diff}_k(A)=\{T\mid\operatorname{order}(T)\le n\},\qquad F_n\circ F_m\subset F_{n+m}$
- $F_0\operatorname{Diff}_k(A)=A,\qquad F_1\operatorname{Diff}_k(A)=\operatorname{Der}_k(A)\oplus A$
- $[F_n\operatorname{Diff}_k(A),F_m\operatorname{Diff}_k(A)]\subset F_{n+m-1}\operatorname{Diff}_k(A)$
- $\operatorname{Der}_k(k[X_1,\dots,X_n])=\bigoplus_{i=1}^n k[X_1,\dots,X_n]\,\partial_i$

## 定理与证明

### 引理 5.2（阶数对复合次加）（完整）

设 $T,S\in\operatorname{End}_k(A)$ 的阶数分别 $\le n$、$\le m$。则 $T\circ S$ 是阶数 $\le n+m$ 的微分算子。

1. 对 $n+m$ 归纳。$n=m=0$ 时 $T,S\in\operatorname{End}_A(A)$，由 5.1 它们是乘子，故 $TS$ 也是乘子，阶数 $0$。  
   *为什么*：阶数 $0$ 的算子恰为 $A$-线性自同态，即乘子；乘子的复合仍是乘子。
2. 一般情形用恒等式 $[TS,a]=T[S,a]+[T,a]S$（对 $a\in A$）。  
   *为什么*：$TSa-aTS=TSa-TaS+TaS-aTS=T(Sa-aS)+(Ta-aT)S$，逐项重排即得。
3. $[S,a]$ 阶数 $\le m-1$、$[T,a]$ 阶数 $\le n-1$；由归纳假设，$T[S,a]$ 阶数 $\le n+m-1$，$[T,a]S$ 阶数 $\le n+m-1$。  
   *为什么*：归纳假设适用于阶数之和更小的算子对；两项的阶数上界相加分别为 $n+(m-1)$ 与 $(n-1)+m$。
4. 故 $[TS,a]$ 阶数 $\le n+m-1$ 对一切 $a\in A$ 成立，即 $TS$ 阶数 $\le n+m$。  
   *为什么*：阶数 $\le N$ 的定义是：对一切 $a$，$[\cdot,a]$ 的阶数 $\le N-1$；逐次降阶即得。

*出处*：引理 5.2 / 原书 p.18

### 引理 5.3（低阶算子的结构）（完整）

(i) $F_0\operatorname{Diff}_k(A)=A$；(ii) $F_1\operatorname{Diff}_k(A)=\operatorname{Der}_k(A)\oplus A$；(iii) $[F_n,F_m]\subset F_{n+m-1}$。

1. (ii) 先证 $\operatorname{Der}_k(A)\subset F_1$：若 $T$ 是导子，则 $[T,a]=T(a)\in A$ 是乘子，故 $[[T,a],b]=0$。  
   *为什么*：导子定义给出 $[T,a](b)=T(ab)-aT(b)=T(a)b$，即 $[T,a]$ 等于乘 $T(a)$。
2. 对导子 $T$ 有 $T(1)=T(1\cdot1)=T(1)+T(1)$，故 $T(1)=0$；于是 $\operatorname{Der}_k(A)\cap A=0$（常数乘子 $c$ 满足 $c=T(1)=0$ 时才可能是导子）。  
   *为什么*：$k$ 是域故 $2T(1)=T(1)$ 推出 $T(1)=0$；乘子 $c$ 作为导子需 $c=T(1)=0$。
3. 设 $S\in F_1$，令 $T=S-S(1)$（减去乘子），则 $T(1)=0$。对 $a,b\in A$，$T(ab)=[T,ab](1)=([T,a]b)(1)+(a[T,b])(1)=T(a)b+aT(b)$。  
   *为什么*：$[T,ab]=[T,a]b+a[T,b]$；$[T,a],a\in A$ 而 $T(1)=0$，故 $([T,a]b)(1)=b(1)T(a)$ 型计算给出 Leibniz 法则。
4. 故 $T\in\operatorname{Der}_k(A)$，即 $F_1=\operatorname{Der}_k(A)+A$；由第 2 步的零交与 $A\subset F_1$ 得直和。(iii) 对 $n+m$ 归纳：由 Jacobi 恒等式 $[[T,S],a]=[[T,a],S]+[T,[S,a]]$，右端阶数 $\le n+m-2$，故 $[T,S]$ 阶数 $\le n+m-1$。  
   *为什么*：Jacobi 恒等式把三重换位子拆成两个已知阶数的项；归纳假设给出界。

*出处*：引理 5.3 / 原书 p.19


## 易错点

- 阶数的定义是对一切 $a_0,\dots,a_n$ 的嵌套换位子为零，而不是“写成 $\sum P_I\partial^I$ 后最高的 $|I|$”；对一般的 $A$ 后者没有意义，两者一致需要 5.10 那样的基定理。
- $F_n$ 是“阶数 $\le n$”的递增滤过，$F_0=A$ 而不是 $k$；把 $F_0$ 当成常数会漏掉所有乘子。
- $\operatorname{Der}_k(A)\cap A=0$ 的论证依赖 $k$ 是域且 $A$ 含 $1$：由 $T(1)=2T(1)$ 得 $T(1)=0$，故非零常数乘子不是导子。
- $[T,S]$ 比 $TS$ 低一阶（5.3(iii)），这是 $\operatorname{Gr}\operatorname{Diff}_k(A)$ 交换的唯一来源；忘记这一条会把分次环误当作非交换。

## 出处

- Miličić《Lectures on the Algebraic Theory of D-Modules》（中译本，校订批注本），§5 多项式系数微分算子环，p.18-19-20（PDF p.24-25-26），`源码/chapters/chap1.tex:660-764（引理 5.2、5.3、5.5）`

## 核验

状态：`source-only`（2026-11-19）

## 关联

- `dmod/concept/weyl-algebra`
- `dmod/concept/order-filtration-of-dn`
- `dmod/concept/symbol-and-principal-symbol`
- `dmod/concept/associated-graded-ring`
