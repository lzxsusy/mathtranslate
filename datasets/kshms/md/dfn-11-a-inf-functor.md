# $\mathcal{A}_\infty$-函子（预范畴之间）

`kshms/concept/dfn-11-a-inf-functor` · track B（$A_\infty$ 形式框架） · 原文 定义 11

**问题**　预范畴之间的函子要额外满足什么，才不会在同伦意义下丢掉信息？

**摘要**　两个 $A_\infty$-预范畴之间的 $A_\infty$-函子，就是相应的非幺预范畴函子中把拟同构映为拟同构的那些；它比定义 12 的等价函子少一条本质满条件。

**别名**　$A_\infty$-functor；$A_\infty$-函子；保持拟同构的预范畴函子

## 陈述

设 $\mathcal{C}$ 与 $\mathcal{D}$ 是 $k$ 上的 $A_\infty$-预范畴。$A_\infty$-函子 $F\colon\mathcal{C}\to\mathcal{D}$ 是指相应的非幺 $A_\infty$-预范畴之间的函子，且 $F$ 把 $\mathcal{C}$ 中的拟同构映为 $\mathcal{D}$ 中的拟同构。

## 记号

沿用定义 8：函子由对象映射 $\phi$ 与 $f_n\colon\bigotimes_{0\le i\le n-1}\operatorname{Hom}_{\mathcal{C}}(X_i,X_{i+1})\to\operatorname{Hom}_{\mathcal{D}}(\phi(X_0),\phi(X_n))[1-n]$（$n\ge1$，$(X_0,\dots,X_n)$ 横截）给出；「相应的非幺 $A_\infty$-预范畴」指先忘掉扩张性质。

## 要点

- 定义不引入新数据：$A_\infty$-函子首先是非幺 $A_\infty$-预范畴的函子，只额外加一条保持性。
- 保持性的内容：$\mathcal{C}$ 中的拟同构经 $F$ 之后仍是 $\mathcal{D}$ 中的拟同构。
- 这条要求有意义的前提是 $\phi$ 把横截序列送到横截序列，而这一点已写在定义 8 的数据里（$\phi^n(\mathcal{C}^{\mathrm{tr}}_n)\subset\mathcal{D}^{\mathrm{tr}}_n$）。
- 与定义 12 的分工：本条不要求 $\phi$ 在对象上本质满，也不逐序列要求同调同构，因此单个 $A_\infty$-函子本身不是等价。

## 公式

$$F=(\phi,(f_n)_{n\ge1})\colon\mathcal{C}\longrightarrow\mathcal{D}$$

$$f_n\colon\bigotimes_{0\le i\le n-1}\operatorname{Hom}_{\mathcal{C}}(X_i,X_{i+1})\longrightarrow\operatorname{Hom}_{\mathcal{D}}(\phi(X_0),\phi(X_n))[1-n]$$

$$\bigoplus_{i<j}\operatorname{Hom}_{\mathcal{C}}(X_i,X_j)\longrightarrow\bigoplus_{i<j}\operatorname{Hom}_{\mathcal{D}}(\phi(X_i),\phi(X_j))$$

## 易错点

- 「保持拟同构」与「诱导拟同构」不是同一条件：后者是定义 12 的 b) 项，要求所诱导的 $(f_n)$ 族本身在同调上同构。
- 本条不要求本质满，所以不能把「存在 $A_\infty$-函子」当成「两个预范畴等价」。
- 定义 8 的求和只对递增指标对 $i<j$：横截性不是对象间的对称关系，$\operatorname{Hom}(X_0,X_1)$ 存在不保证 $\operatorname{Hom}(X_1,X_0)$ 存在。
- 一个对象上的 $f_1$ 不必是拟同构，除非该对象到自身的对是横截的且 $f_1$ 对应一个拟同构。

## 相关卡

- `kshms/concept/dfn-08-nonunital-a-inf-pre-functor`
- `kshms/concept/dfn-09-quasi-isomorphism`
- `kshms/concept/dfn-12-a-inf-equivalence-functor`
- `kshms/concept/dfn-13-a-inf-precategory-equivalence`

## 出处

- Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25） §4.3（原文 p.26）；锚点 `源码/chunks/ch04.tex:238-242（定义 11）`

> 原文 p26 §4.3；译本 ch04.tex 238–242 行；图版 Definition 11 与译文一致。
