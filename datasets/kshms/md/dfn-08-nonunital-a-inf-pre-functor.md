# 非幺 $A_\infty$-预范畴之间的函子

`kshms/concept/dfn-08-nonunital-a-inf-pre-functor` · track B（$A_\infty$ 形式框架） · 原文 定义 8

**问题**　非幺 $A_\infty$-预范畴之间的函子为什么只对递增指标对 $i<j$ 求和，而定义 6 的函子对全部 $(i,j)$ 求和？

**摘要**　对象映射 $\phi$ 须把横截序列送到横截序列，$f_n$ 只在横截序列上定义，并要求递增指标直和之间的映射是 $A_\infty$-态射。

**别名**　functor between non-unital $A_\infty$-pre-categories；非幺 $A_\infty$-预范畴函子；保持横截性的 $A_\infty$-函子

## 陈述

非幺 $A_\infty$-预范畴之间的函子 $F\colon\mathcal{C}\to\mathcal{D}$ 由以下数据给出：
1) 对象类的映射 $\phi\colon\mathcal{C}\to\mathcal{D}$，满足 $\phi^n(\mathcal{C}^{\mathrm{tr}}_n)\subset\mathcal{D}^{\mathrm{tr}}_n$。
2) 对 $\mathcal{C}$ 中任意横截对象序列 $(X_0,\dots,X_n)$（$n\ge1$），一个分次 $k$-模态射
$$f_n\colon\bigotimes_{0\le i\le n-1}\operatorname{Hom}_{\mathcal{C}}(X_i,X_{i+1})\longrightarrow\operatorname{Hom}_{\mathcal{D}}(\phi(X_0),\phi(X_n))[1-n].$$
这些数据满足以下性质：序列 $f_n$（$n\ge1$）定义一个 $A_\infty$-态射 $\bigoplus_{i<j}\operatorname{Hom}_{\mathcal{C}}(X_i,X_j)\to\bigoplus_{i<j}\operatorname{Hom}_{\mathcal{D}}(\phi(X_i),\phi(X_j))$。

## 记号

$\mathcal{C},\mathcal{D}$：非幺 $A_\infty$-预范畴；$\phi$：对象映射，须保持横截性；$f_n$：只在 $\mathcal{C}$ 的横截序列上定义，次数 $1-n$；$i<j$：递增指标对。

## 要点

- 数据 = 保持横截性的对象映射 $\phi$（$\phi^n(\mathcal{C}^{\mathrm{tr}}_n)\subset\mathcal{D}^{\mathrm{tr}}_n$）+ 只在横截序列上定义的 $f_n$（$n\ge1$）。
- 条件是 $\bigoplus_{i<j}\operatorname{Hom}_{\mathcal{C}}(X_i,X_j)\to\bigoplus_{i<j}\operatorname{Hom}_{\mathcal{D}}(\phi(X_i),\phi(X_j))$ 为 $A_\infty$-态射。
- 只取 $i<j$ 是因为横截性不必对称：$\operatorname{Hom}(X_j,X_i)$ 可能没有定义，不能对全部 $(i,j)$ 求和。
- 当所有 $\operatorname{Hom}$ 都有定义（$\mathcal{C}^{\mathrm{tr}}_n=\mathcal{C}^n$）时，本条与定义 6 一致（原文紧接其后的说明）。

## 公式

$$\phi^n(\mathcal{C}^{\mathrm{tr}}_n)\subset\mathcal{D}^{\mathrm{tr}}_n$$

$$f_n\colon\bigotimes_{0\le i\le n-1}\operatorname{Hom}_{\mathcal{C}}(X_i,X_{i+1})\to\operatorname{Hom}_{\mathcal{D}}(\phi(X_0),\phi(X_n))[1-n]$$

$$\bigoplus_{i<j}\operatorname{Hom}_{\mathcal{C}}(X_i,X_j)\to\bigoplus_{i<j}\operatorname{Hom}_{\mathcal{D}}(\phi(X_i),\phi(X_j))$$

## 易错点

- 不要照定义 6 给这里补 $f_0$：定义 8 的数据只要求 $n\ge1$，且 $\operatorname{Hom}(\phi(X_0),\phi(X_0))$ 未必有定义。
- 对象映射的横截性条件 $\phi^n(\mathcal{C}^{\mathrm{tr}}_n)\subset\mathcal{D}^{\mathrm{tr}}_n$ 是定义的一部分；只检查 $f_n$ 的公式不够。
- 把 $\bigoplus_{i<j}$ 写成 $\bigoplus_{i,j}$ 是实质性错误，不只是记号差异。

## 相关卡

- `kshms/concept/dfn-06-nonunital-a-inf-functor`
- `kshms/concept/dfn-07-nonunital-a-inf-pre-category`
- `kshms/concept/dfn-05-nonunital-a-inf-category`

## 出处

- Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25） §4.3（原文 p.25）；锚点 `源码/chunks/ch04.tex:178-193（定义 8）`

> 原文 p25 §4.3；译本 ch04.tex:178-193；原文同页紧接着说明为何只对 $i<j$ 求和，并指出 $\mathcal{C}^{\mathrm{tr}}_n=\mathcal{C}^n$ 时与定义 6 一致。
