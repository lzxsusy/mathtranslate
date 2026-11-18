# 非幺 $A_\infty$-范畴

`kshms/concept/dfn-05-nonunital-a-inf-category` · track B（$A_\infty$ 形式框架） · 原文 定义 5

**问题**　为什么非幺 $A_\infty$-范畴的一致性条件要打包成「任意对象序列的 $\operatorname{Hom}$ 直和构成非幺 $A_\infty$-代数」，而不逐条列出 $m_n$ 的方程？

**摘要**　对象类、每对对象的 $\operatorname{Hom}$ 分次模、以及对每个对象序列的复合 $m_n$；要求任意对象序列的 $\operatorname{Hom}$ 直和构成非幺 $A_\infty$-代数。

**别名**　non-unital $A_\infty$-category；非幺 $A_\infty$-范畴；$A_\infty$-范畴（非幺）

## 陈述

域 $k$ 上的非幺 $A_\infty$-范畴 $\mathcal{C}$ 由以下数据给出：
1) 一个对象类 $\operatorname{Ob}(\mathcal{C})$。
2) 对任意两个对象 $X_1$ 与 $X_2$，一个 $\mathbb{Z}$-分次 $k$-模 $\operatorname{Hom}(X_1,X_2)$。
3) 对任意对象序列 $X_0,\dots,X_n$（$n\ge1$），一个 $k$-模态射（称为复合映射）
$$m_n\colon\bigotimes_{0\le i\le n-1}\operatorname{Hom}(X_i,X_{i+1})\longrightarrow\operatorname{Hom}(X_0,X_n)[2-n].$$
要求：对任意对象序列 $X_0,\dots,X_N$（$N\ge0$），分次 $k$-模 $A=A(X_0,\dots,X_N):=\bigoplus_{i,j}\operatorname{Hom}(X_i,X_j)$ 配以复合 $m_n$（$n\ge1$）的直和，构成一个非幺 $A_\infty$-代数。

## 记号

$\mathcal{C}$：非幺 $A_\infty$-范畴，其对象类 $\operatorname{Ob}(\mathcal{C})$ 今后常简记为 $\mathcal{C}$；$\operatorname{Hom}(X_1,X_2)$：分次 $k$-模态射模（省略下标 $\mathcal{C}$）；$m_n$：复合映射；$A(X_0,\dots,X_N)$：对象序列的 $\operatorname{Hom}$ 直和。

## 要点

- 数据是「对象类 + 每对对象的 $\operatorname{Hom}$ + 每个对象序列的复合 $m_n$」，定义中没有单位态射。
- 一致性条件不逐条写，而是要求 $A(X_0,\dots,X_N)=\bigoplus_{i,j}\operatorname{Hom}(X_i,X_j)$ 配 $m_n$ 的直和是非幺 $A_\infty$-代数；这就等价于定义 3 的那组方程。
- 指标 $i,j$ 取遍所有对象对，不要求 $i<j$：本条没有横截性，所有 $\operatorname{Hom}$ 都有定义。
- 只有一个对象 $X$ 且 $\operatorname{Hom}(X,X)=A$ 时，回到非幺 $A_\infty$-代数（原文注 8）。

## 公式

$$m_n\colon\bigotimes_{0\le i\le n-1}\operatorname{Hom}(X_i,X_{i+1})\to\operatorname{Hom}(X_0,X_n)[2-n]$$

$$A(X_0,\dots,X_N)=\bigoplus_{i,j}\operatorname{Hom}(X_i,X_j)$$

## 易错点

- 非幺范畴仍要求 $m_1^2=0$：这是「构成非幺 $A_\infty$-代数」的一部分，不要以为非幺就连微分条件都没有。
- 对象类 $\operatorname{Ob}(\mathcal{C})$ 与范畴 $\mathcal{C}$ 在原文中常混用同一个字母，读 $\operatorname{Hom}(X_i,X_j)$ 时要记得它在哪一层。
- 定义 5 的 $m_n$ 对所有对象序列定义；定义 7 的预范畴只对横截序列定义，两者不可混用。

## 相关卡

- `kshms/concept/dfn-03-nonunital-a-inf-algebra`
- `kshms/concept/dfn-06-nonunital-a-inf-functor`
- `kshms/concept/dfn-07-nonunital-a-inf-pre-category`

## 出处

- Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25） §4.2（原文 p.23）；锚点 `源码/chunks/ch04.tex:90-104（定义 5）`

> 原文 p23–p24 §4.2：第 1) 项在 p23，2)–3) 与「要求」续于 p24；译本 ch04.tex:90-104；items.tsv 记原文页 23。
