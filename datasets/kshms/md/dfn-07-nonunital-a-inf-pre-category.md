# 非幺 $A_\infty$-预范畴

`kshms/concept/dfn-07-nonunital-a-inf-pre-category` · track B（$A_\infty$ 形式框架） · 原文 定义 7

**问题**　为什么要在非幺 $A_\infty$-范畴之外再引入「横截序列类」，它对应 Fukaya 范畴的哪个困难？

**摘要**　在非幺 $A_\infty$-范畴上加一个横截序列类：$\operatorname{Hom}$ 与复合 $m_n$ 只对横截序列定义，横截性对子序列封闭，方程与定义 5 相同。

**别名**　non-unital $A_\infty$-pre-category；非幺 $A_\infty$-预范畴；带横截序列类的 $A_\infty$-范畴

## 陈述

设 $k$ 是如前所述的 $\mathbb{Z}$-分次交换结合环。$k$ 上的非幺 $A_\infty$-预范畴由以下数据定义：
a) 一个对象类 $\mathcal{C}$。
b) 对任意 $n\ge1$，一个子类 $\mathcal{C}^{\mathrm{tr}}_n\subset\mathcal{C}^n$，其中 $\mathcal{C}^{\mathrm{tr}}_1=\mathcal{C}$，称为横截序列类。
c) 对 $(X_1,X_2)\in\mathcal{C}^{\mathrm{tr}}_2$，一个 $\mathbb{Z}$-分次 $k$-模 $\operatorname{Hom}(X_1,X_2)$。
d) 对横截的对象序列 $(X_0,\dots,X_n)$（$n\ge0$），一个 $k$-模态射（复合映射）
$$m_n\colon\bigotimes_{0\le i\le n-1}\operatorname{Hom}(X_i,X_{i+1})\longrightarrow\operatorname{Hom}(X_0,X_n)[2-n].$$
要求：横截序列 $(X_1,\dots,X_n)$ 的任意子序列 $(X_{i_1},\dots,X_{i_l})$（$i_1<i_2<\cdots<i_l$）都是横截的，且复合映射满足与非幺 $A_\infty$-范畴相同的一组方程。具体写出即
$$\sum_{i+j=n+1}\sum_{0\le l\le i}\epsilon(l,j)\,m_i(a_0,\dots,a_{l-1},m_j(a_l,\dots,a_{l+j-1}),a_{l+j},\dots,a_n)=0,$$
其中 $a_m\in\operatorname{Hom}(X_m,X_{m+1})$，而 $\epsilon(l,j)=(-1)^{j\sum_{0\le s\le l-1}\deg(a_s)+l(j-1)+j(i-1)}$。

## 记号

$k$：$\mathbb{Z}$-分次交换结合环；$\mathcal{C}^{\mathrm{tr}}_n\subset\mathcal{C}^n$：横截 $n$ 元组类，约定 $\mathcal{C}^{\mathrm{tr}}_1=\mathcal{C}$；$\operatorname{Hom}(X_1,X_2)$：只对横截对定义；$m_n$：复合映射；$\epsilon(l,j)$：Koszul 符号。

## 要点

- 预范畴只对横截对 $(X_1,X_2)\in\mathcal{C}^{\mathrm{tr}}_2$ 定义 $\operatorname{Hom}$，只对横截序列定义 $m_n$；这是它与定义 5 的全部差别。
- 横截性对子序列封闭：$(X_1,\dots,X_n)$ 横截则任意递增子序列 $(X_{i_1},\dots,X_{i_l})$ 横截；$\mathcal{C}^{\mathrm{tr}}_1=\mathcal{C}$ 是约定。
- 横截性不必对称：可能 $\operatorname{Hom}(X_0,X_1)$ 存在而 $\operatorname{Hom}(X_1,X_0)$ 不存在（原文在定义 8 之后点明）。
- 复合满足与非幺 $A_\infty$-范畴相同的方程；当 $\mathcal{C}^{\mathrm{tr}}_n=\mathcal{C}^n$（对一切 $n$）时就是定义 5 的非幺 $A_\infty$-范畴。

## 公式

$$\mathcal{C}^{\mathrm{tr}}_n\subset\mathcal{C}^n,\qquad \mathcal{C}^{\mathrm{tr}}_1=\mathcal{C}$$

$$m_n\colon\bigotimes_{0\le i\le n-1}\operatorname{Hom}(X_i,X_{i+1})\to\operatorname{Hom}(X_0,X_n)[2-n]$$

$$\sum_{i+j=n+1}\sum_{0\le l\le i}\epsilon(l,j)\,m_i(a_0,\dots,a_{l-1},m_j(a_l,\dots,a_{l+j-1}),a_{l+j},\dots,a_n)=0$$

## 易错点

- 「横截」在本节纯属形式术语（原文脚注 5），不要按微分拓扑的横截性理解。
- $\mathcal{C}^{\mathrm{tr}}_n$ 是对象 $n$ 元组的类，不是态射的条件；判断 $\operatorname{Hom}(X,Y)$ 是否存在只看 $(X,Y)\in\mathcal{C}^{\mathrm{tr}}_2$。
- 原文在此把 $m_j$ 的末变量误写作 $a_{l+j}$、其后的变量写作 $a_{l+j+1}$，与 $m_j$ 只吃 $j$ 个变量不合；译本按数学意义改为 $a_{l+j-1}$ 与 $a_{l+j}$，引用原文时留意。
- 预范畴没有单位态射，也不是通常意义的范畴；不要用范畴复合的结合律去检验它。

## 相关卡

- `kshms/concept/dfn-05-nonunital-a-inf-category`
- `kshms/concept/dfn-06-nonunital-a-inf-functor`
- `kshms/concept/dfn-08-nonunital-a-inf-pre-functor`

## 出处

- Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25） §4.3（原文 p.25）；锚点 `源码/chunks/ch04.tex:147-170（定义 7）`

> 原文 p25 §4.3；译本 ch04.tex:147-170，其后 ch04.tex:172-176 的译注记录原文公式的下标笔误；与 p25 图核对一致。
