# 非幺 $A_\infty$-范畴之间的函子

`kshms/concept/dfn-06-nonunital-a-inf-functor` · track B（$A_\infty$ 形式框架） · 原文 定义 6

**问题**　非幺 $A_\infty$-范畴之间的函子与代数之间的态射（定义 4）相比多了什么，为什么这里的 $f_n$ 要从 $n=0$ 开始？

**摘要**　对象映射 $\phi$ 加一族 $f_n$（$n\ge0$），使每个对象序列的 $\operatorname{Hom}$ 直和之间的映射成为 $A_\infty$-态射（定义 4）。

**别名**　functor between non-unital $A_\infty$-categories；非幺 $A_\infty$-函子；$A_\infty$-函子（范畴情形）

## 陈述

非幺 $A_\infty$-范畴之间的函子 $F\colon\mathcal{C}_1\to\mathcal{C}_2$ 由以下数据给出：
1) 对象类之间的映射 $\phi\colon\mathcal{C}_1\to\mathcal{C}_2$。
2) 对任意有限对象序列 $X_0,\dots,X_n$（$n\ge0$），一个分次 $k$-模的态射
$$f_n\colon\bigotimes_{0\le i\le n-1}\operatorname{Hom}_{\mathcal{C}_1}(X_i,X_{i+1})\longrightarrow\operatorname{Hom}_{\mathcal{C}_2}(\phi(X_0),\phi(X_n))[1-n].$$
以下条件成立：对任意 $X_1,\dots,X_N\in\mathcal{C}_1$，序列 $f_n$（$n\ge1$）定义一个 $A_\infty$-态射
$$\bigoplus_{i,j}\operatorname{Hom}_{\mathcal{C}_1}(X_i,X_j)\longrightarrow\bigoplus_{i,j}\operatorname{Hom}_{\mathcal{C}_2}(\phi(X_i),\phi(X_j)).$$

## 记号

$\mathcal{C}_1,\mathcal{C}_2$：非幺 $A_\infty$-范畴；$\phi$：对象映射；$f_n$：函子的 Taylor 系数，次数 $1-n$；下标 $\mathcal{C}_1$、$\mathcal{C}_2$ 标明 $\operatorname{Hom}$ 取自哪个范畴。

## 要点

- 函子 = 对象映射 $\phi$ + 一族 $f_n$；$f_n$ 定义在 $\mathcal{C}_1$ 的任意有限对象序列上（$n\ge0$），取值到 $\mathcal{C}_2$ 的 $\operatorname{Hom}$，次数为 $1-n$。
- $n=0$ 时空张量积为 $k$，$f_0\colon k\to\operatorname{Hom}_{\mathcal{C}_2}(\phi(X_0),\phi(X_0))$；这是代数间态射（定义 4，$n\ge1$）所没有的项。
- 条件是把每个对象序列的 $\operatorname{Hom}$ 直和（对全部 $i,j$ 求和）映成 $A_\infty$-态射，即 $f_n$ 满足定义 4 的交换方程。
- 这里的直和取全部指标对 $(i,j)$；预范畴的函子（定义 8）只取 $i<j$，因为那里 $\operatorname{Hom}(X_j,X_i)$ 可能不存在。

## 公式

$$f_n\colon\bigotimes_{0\le i\le n-1}\operatorname{Hom}_{\mathcal{C}_1}(X_i,X_{i+1})\to\operatorname{Hom}_{\mathcal{C}_2}(\phi(X_0),\phi(X_n))[1-n]$$

$$\bigoplus_{i,j}\operatorname{Hom}_{\mathcal{C}_1}(X_i,X_j)\to\bigoplus_{i,j}\operatorname{Hom}_{\mathcal{C}_2}(\phi(X_i),\phi(X_j))$$

## 易错点

- 数据条款写 $n\ge0$，而条件里只用到 $n\ge1$；不要因此省掉 $f_0$——定义 8 才是从 $n\ge1$ 开始的。
- 对象映射 $\phi$ 与 $f_n$ 是两套独立数据，缺一不可；只给 $f_1$ 不构成函子。
- 把定义 6 直接搬到预范畴会出错：预范畴里 $\operatorname{Hom}(X_j,X_i)$ 可能没有定义，故定义 8 只对 $i<j$ 求和。

## 相关卡

- `kshms/concept/dfn-04-nonunital-a-inf-morphism`
- `kshms/concept/dfn-05-nonunital-a-inf-category`
- `kshms/concept/dfn-08-nonunital-a-inf-pre-functor`

## 出处

- Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25） §4.2（原文 p.24）；锚点 `源码/chunks/ch04.tex:113-129（定义 6）`

> 原文 p24 §4.2；译本 ch04.tex:113-129；原文同页的注 9（ch04.tex:131-138）给出 $H(\mathcal{C})$ 的非幺范畴结构。
