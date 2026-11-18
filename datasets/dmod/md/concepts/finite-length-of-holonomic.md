---
id: dmod/concept/finite-length-of-holonomic
type: concept
track: B
---

# 完整模的有限长度

> 完整模必为有限长度：证明对 Bernstein 重数归纳，用极大真子模把长度问题化到不可约商模。

**问题**：为什么特征簇维数最小的模一定具有有限合成列，归纳该对哪个量做？

## 定义

称 $D(n)$-模 $M$ 具有\emph{有限长度}，若它有一列有限长的子模链 $$0=M_0\subsetneq M_1\subsetneq\cdots\subsetneq M_\ell=M$$ 使每个商 $M_i/M_{i-1}$ 不可约；此时 $\ell$ 与链的选取无关，记为 $\ell(M)$，称为 $M$ 的长度。定理 8.1(i) 断言：完整 $D(n)$-模都具有有限长度。

*记号*：$\mathcal M_{fl}(D(n))$ 记 $\mathcal M_{fg}(D(n))$ 中由有限长度模构成的全子范畴；$e(M)$ 是 Bernstein 重数，$d(M)$ 是 Bernstein 维数；长度对短正合列可加。

## 要点

- 非零完整模满足 $\dim\operatorname{Ch}(M)=n$，故 $d(M)=n$（定理 7.7）；归纳不能在维数上做，因为维数恒为 $n$。
- 归纳变量是 Bernstein 重数 $e(M)$：对极大真子模 $M'$ 有 $e(M')<e(M)$。
- 极大真子模的存在用 $D(n)$ 诺特 + $M$ 有限生成；商 $M/M'$ 不可约，故长度为 $1$。
- 长度可加给出 $\ell(M)=\ell(M')+1$，由归纳得 $\ell(M)<\infty$。
- $\operatorname{Hol}(D(n))\subset\mathcal M_{fl}(D(n))$；$n>1$ 时包含严格（讲义指出可证，未给证明）。
- 光滑簇版本（定理 5.1.3）：每个完整 $\mathcal D_X$-模都有限长度，证明归约到仿射空间并用 Kashiwara 定理。

## 关键公式

- $\ell(M)=\ell(M')+1$
- $e(M')<e(M)\quad(M'\subsetneq M,\ d(M')=d(M))$
- $d(M)=n\quad(0\neq M\ \text{完整})$
- $0\to M'\to M\to M/M'\to0$

## 定理与证明

### 定理 8.1(i)（完整模具有有限长度）（完整）

设 $M$ 是完整 $D(n)$-模，则 $M$ 具有有限长度。

1. 设 $M\neq0$ 完整。由定义 $\dim\operatorname{Ch}(M)=n$，由定理 7.7 得 $d(M)=n$。  
   *为什么*：完整性的定义就是特征簇维数取最小值 $n$，而 7.7 把它换成 Bernstein 维数。
2. $D(n)$ 是诺特环且 $M$ 有限生成，故存在极大真子模 $M'\subsetneq M$，得正合列 $0\to M'\to M\to M/M'\to0$，其中 $M/M'$ 不可约。  
   *为什么*：诺特性保证非零有限生成模的极大真子模存在（对子模的递增链取并）。
3. 由定理 8.1(ii)，$M'$ 与 $M/M'$ 都完整；若 $M'\neq0$，由 §3 的重数性质得 $e(M')<e(M)$。  
   *为什么*：子模与商模完整是 8.1(ii) 的内容；维数相同而模更小时重数严格下降。
4. 对 $e(M)$ 作归纳：$M'$ 有有限长度，$M/M'$ 不可约故长度为 $1$，于是 $\ell(M)=\ell(M')+1<\infty$。  
   *为什么*：长度对短正合列可加；归纳从 $e(M)$ 的最小值（不可约情形）起步。
5. $M=0$ 时长度为 $0$，结论平凡。  
   *为什么*：零模按约定完整，其合成列为空。

*出处*：定理 8.1(i) / 原书 p.32

### 定理 5.1.3（光滑簇上的版本）（完整）

设 $X$ 是光滑簇，则每个完整 $\mathcal D_X$-模都是有限长度的。

1. 完整模在开集上的限制仍完整，且有限长度是局部性质（III.2.8），故可设 $X$ 是 $k^n$ 的光滑闭子簇，$i:X\hookrightarrow k^n$。  
   *为什么*：两条性质都可逐仿射开集检验。
2. 由引理 5.1.2 与 Kashiwara 定理，$i_+(\mathcal V)$ 完整；由仿射空间情形（定理 8.1(i)），$i_+(\mathcal V)$ 有有限长度。  
   *为什么*：沿闭浸入的直像保持完整性，而定理 8.1 已处理 $D(k^n)$-模。
3. $i_+(\mathcal V)$ 的子商支集都在 $X$ 中，故其长度在 $\mathcal M_X(\mathcal D_{k^n})$ 中计算与在全体模中相同；由 Kashiwara 定理这等于 $\ell(\mathcal V)$。  
   *为什么*：Kashiwara 等价（定理 12.6）把支集含于 $X$ 的模与 $\mathcal D_X$-模一一对应并保持长度。

*出处*：定理 5.1.3 / 原书 p.134


## 易错点

- 归纳变量是重数 $e(M)$，不是维数（维数恒为 $n$）也不是长度（正是要证的量）；搞错归纳变量会循环论证。
- 极大真子模的存在依赖 $D(n)$ 诺特与 $M$ 有限生成；对非有限生成模这一步失效。
- $M/M'$ 不可约 ⇒ 长度为 $1$ 这一步不能省，否则 $\ell(M)=\ell(M')+1$ 缺依据。
- 有限长度不蕴含完整：$n>1$ 时完整模构成有限长度模的真子范畴。

## 出处

- Miličić《Lectures on the Algebraic Theory of D-Modules》（中译校订批注本，150 页），§8 完整模，p.32（PDF p.38），`源码/chapters/chap1.tex:1160-1185（定理 8.1）`
- Miličić《Lectures on the Algebraic Theory of D-Modules》（中译校订批注本，150 页），V §1 完整 D-模，p.133-134（PDF p.139-140），`源码/chapters/chap5.tex:52-58（定理 5.1.3）`

## 核验

状态：`source-only`（2026-11-19）

## 关联

- `dmod/concept/holonomic-module`
- `dmod/concept/bernstein-dimension`
- `dmod/concept/characteristic-variety`
- `dmod/concept/kashiwara-theorem-statement`
