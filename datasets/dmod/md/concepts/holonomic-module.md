---
id: dmod/concept/holonomic-module
type: concept
track: B
---

# 完整模（holonomic 模）

> 完整模是特征簇维数取最小值 $n$ 的有限生成 $D(n)$-模；它们有有限长度，且对子模、商模、扩张封闭。

**问题**：为什么把「特征簇维数等于 $n$」的模单独命名为完整模，这个类对哪些操作封闭？

## 定义

设 $M$ 是非零有限生成 $D(n)$-模。由定理 7.13，$\dim\operatorname{Ch}(M)\ge n$。若 $\dim\operatorname{Ch}(M)\le n$，则称 $M$ 是\emph{完整（holonomic）}的。因此 $M$ 完整当且仅当 $M=0$ 或 $\dim\operatorname{Ch}(M)=n$。\par 在光滑簇 $X$ 上：凝聚 $\mathcal D_X$-模 $\mathcal V$ 称为完整的，若对任意 $x\in\operatorname{supp}(\mathcal V)$ 有 $$\dim_{p_X^{-1}(x)}\operatorname{Ch}(\mathcal V)=\dim_xX,$$ 其中 $p_X:T^*(X)\to X$ 是余切丛投影；这推广了上述定义。

*记号*：$\operatorname{Ch}(M)$ 是特征簇；$\operatorname{Hol}(D(n))$ 记 $\mathcal M_{fg}(D(n))$ 中由完整模构成的全子范畴；$\operatorname{Hol}(\mathcal D_X)$ 是 $\mathcal M_{coh}(\mathcal D_X)$ 的相应全子范畴；$\dim_{p_X^{-1}(x)}$ 指在纤维 $p_X^{-1}(x)$ 中的维数。

## 要点

- 完整等价于 $\dim\operatorname{Ch}(M)=n$（非零时），也等价于 $d(M)=n$：由定理 7.7，特征簇维数就是 Bernstein 维数。
- 定理 8.1：完整模有有限长度；完整模的子模、商模、扩张都完整，故 $\operatorname{Hol}(D(n))$ 在取子模、商模、扩张下封闭。
- $\operatorname{Hol}(D(n))\subset\mathcal M_{fl}(D(n))$；讲义指出当 $n>1$ 时这是真子范畴（未给证明）。
- 转置函子与 Fourier 函子都把完整模映为完整模。
- 基本例子：$\mathcal O_n$（$\operatorname{Ch}=k^n\times\{0\}$）、$\Delta_n$（$\operatorname{Ch}=\{0\}\times k^n$）、$M_\alpha=D(1)/D(1)(z\partial-\alpha)$、以及完整模的局部化 $M_P$（命题 8.6、推论 8.7）都完整。
- 光滑簇版本（第 V 章 5.1.1）：$\operatorname{Hol}(\mathcal D_X)$ 是 Abel 子范畴且是厚的。

## 关键公式

- $M\ \text{完整}\iff M=0\ \text{或}\ \dim\operatorname{Ch}(M)=n$
- $\dim\operatorname{Ch}(M)=d(M)$
- $\dim_{p_X^{-1}(x)}\operatorname{Ch}(\mathcal V)=\dim_xX\quad(x\in\operatorname{supp}\mathcal V)$
- $\operatorname{Ch}(\mathcal O_n)=k^n\times\{0\},\qquad \operatorname{Ch}(\Delta_n)=\{0\}\times k^n$

## 定理与证明

### 定理 8.1（完整模的基本性质）（完整）

(i) 完整模具有有限长度；(ii) 完整模的子模、商模和扩张都是完整的。

1. 先证 (ii)。由命题 7.4，对短正合列 $0\to M'\to M\to M''\to0$ 有 $\operatorname{Ch}(M)=\operatorname{Ch}(M')\cup\operatorname{Ch}(M'')$，故 $\dim\operatorname{Ch}(M)=\max\bigl(\dim\operatorname{Ch}(M'),\dim\operatorname{Ch}(M'')\bigr)$。  
   *为什么*：并集的维数是各成员维数的最大值。
2. 由定理 7.13，非零模的特征簇维数 $\ge n$；于是三个模中任意两个完整（维数 $=n$）都推出第三个完整（维数 $=\max\{n,n\}=n$），零模按约定完整。  
   *为什么*：上一步的 max 公式把「$\le n$」逐项传递。
3. 证 (i)。设 $M\neq0$ 完整，则 $\dim\operatorname{Ch}(M)=n$，由定理 7.7 得 $d(M)=n$。  
   *为什么*：完整性与 Bernstein 维数通过 7.7 相连。
4. $D(n)$ 诺特且 $M$ 有限生成，故存在极大真子模 $M'\subsetneq M$；商 $M/M'$ 不可约。由 (ii)，$M'$ 与 $M/M'$ 都完整；若 $M'\neq0$，由 §3 的重数性质得 $e(M')<e(M)$。  
   *为什么*：极大真子模的存在用诺特性；重数在真子模上严格下降，因为 $d(M')=d(M)=n$ 且 $M'\neq M$。
5. 对重数 $e(M)$ 归纳：$M'$ 有有限长度，$M/M'$ 不可约故长度为 $1$，由长度的可加性 $\ell(M)=\ell(M')+1<\infty$。  
   *为什么*：归纳假设给出 $\ell(M')<\infty$；不可约模的长度为 $1$。

*出处*：定理 8.1 / 原书 p.32

### 定理 5.1.3（光滑簇上完整模的有限长度）（完整）

设 $X$ 是光滑簇，则每个完整 $\mathcal D_X$-模都是有限长度的。

1. 完整模在开集上的限制仍完整；由 III.2.8，有限长度是局部性质，故可设 $X$ 是仿射空间 $k^n$ 的光滑闭子簇，$i:X\hookrightarrow k^n$。  
   *为什么*：两条性质都可逐开集检验，取仿射覆盖后归约。
2. 由引理 5.1.2 与 Kashiwara 定理，$\mathcal V$ 完整当且仅当 $i_+(\mathcal V)$ 完整；由定理 8.1(i)，$i_+(\mathcal V)$ 作为 $D(k^n)$-模有有限长度。  
   *为什么*：沿闭浸入的直像保持完整性（5.1.2），而仿射空间情形已由 8.1 解决。
3. $i_+(\mathcal V)$ 的子模与商模的支集都在 $X$ 中，故它作为 $\mathcal M_X(\mathcal D_{k^n})$ 中对象的长度等于作为全体 $D(k^n)$-模对象的长度；由 Kashiwara 定理（12.6）这个长度就是 $\mathcal V$ 的长度。  
   *为什么*：支集在 $X$ 中的模构成的全子范畴与 $\mathcal D_X$-模范畴在 Kashiwara 等价下对应。

*出处*：定理 5.1.3 / 原书 p.134


## 易错点

- 不要把「完整」与「有限长度」等同：$n>1$ 时 $\operatorname{Hol}(D(n))$ 严格小于有限长度模范畴（讲义指出可证，未展开）。
- 完整是对**有限生成**模说的；一般模要先验证有限生成，否则 $\operatorname{Ch}$ 与 $d$ 都没有定义。
- 零模按约定完整，但 $\operatorname{Ch}(0)=\varnothing$ 没有维数；陈述时要按「$M=0$ 或 $\dim=n$」的写法。
- 「$\dim\operatorname{Ch}(M)\le n$」对非零有限生成模自动是等号（定理 7.13），不要以为存在维数严格小于 $n$ 的非零模。

## 出处

- Miličić《Lectures on the Algebraic Theory of D-Modules》（中译校订批注本，150 页），§8 完整模，p.32-33-34-35-36（PDF p.38-39-40-41-42），`源码/chapters/chap1.tex:1160-1310（定理 8.1、例 8.2–8.5、命题 8.6）`
- Miličić《Lectures on the Algebraic Theory of D-Modules》（中译校订批注本，150 页），V §1 完整 D-模，p.133-134（PDF p.139-140），`源码/chapters/chap5.tex:3-58（定理 5.1.1–5.1.3）`

## 核验

状态：`external-confirmed`（2026-11-19）
- nLab：https://ncatlab.org/nlab/show/holonomic+D-module — 条目断言完整模当且仅当特征簇的维数等于 $n$，且此时特征簇是余切丛中的锥并是 Lagrangian 子簇；这与卡中的定义（$\dim\operatorname{Ch}(M)=n$ 即完整）及引理 7.3 的锥性一致。

## 关联

- `dmod/concept/characteristic-variety`
- `dmod/concept/bernstein-dimension`
- `dmod/concept/finite-length-of-holonomic`
- `dmod/concept/holonomicity-under-tensor`
- `dmod/concept/kashiwara-theorem-statement`
- `dmod/concept/preservation-of-holonomicity`
