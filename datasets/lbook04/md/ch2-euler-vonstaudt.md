# Euler 乘积与 von Staudt

> `lbook04/concept/ch2-euler-vonstaudt` · 轨 L L 函数 · 状态 reviewed · 核验 source-only

**问题：** 为什么说 L 函数在 $s=1$ 的极点「只能来自 zeta」，模 $p$ 的极点又为何仍由调和级数解释？

**一句话：** L 函数的极点总由 $\zeta$ 的极点解释；Serre 观察到 $\zeta(1-k)=-b_k/k$，而 von Staudt–Clausen 定理把 $b_k$ 分母的素数写成 $p-1\mid k$。

**别名：** `von Staudt–Clausen`、`Bernoulli 数`、`L 函数的极点`

## 定义

第 2 章 §5 讨论「零碎内容，包括极点」。酉归一化之后，$s=1$ 是 L 函数唯一可能的极点，而且总由 $\zeta$ 的单极点解释：书中举出 $L(f,s)=\zeta(s)^kL(f_1,s)$ 的三种来源——Dedekind zeta、Rankin–Selberg（对称平方）、Artin（Brauer 诱导），极点的阶数等于平凡表示的重数。这条原则的算术影子是 Serre 的观察：$\zeta(1-k)=-b_k/k$（(5.1)），于是负整数处的值与 Bernoulli 数挂钩；von Staudt–Clausen 定理给出 $b_k$ 分母的素数分解，从而「模 $p$ 的极点」仍由调和级数 $\sum1/n$ 解释。书中还提到 Tate 猜想与 Leopoldt 的 $p$ 进 zeta，把这条线索延伸到 $p$ 进世界。

**记号：** $b_k$：Bernoulli 数；$\zeta(1-k)$：负整数处的 zeta 值；$p-1\mid k$：von Staudt–Clausen 的整除条件；$L(f,s)=\zeta(s)^kL(f_1,s)$：极点分解。

## 要点

- 「极点来自 $\zeta$」是结构性的：只要 L 函数来自自守表示（或 Artin 表示），极点就由平凡表示的重数决定，而平凡表示的 L 就是 $\zeta$。
- von Staudt–Clausen 把 Bernoulli 数分母的算术（$p-1\mid k$）暴露出来，这正是模 $p$ 极点的来源：分母含 $p$ 当且仅当 $p-1\mid k$。
- 书中的 $p-1\mid2k$ 与随后同余式 $x^{k-1}\equiv x^{-1}\pmod p$ 不自洽；标准定理是 $p-1\mid k$（$k$ 偶），中译注本已出译注。

## 公式

$$
\zeta(1-k)=-\frac{b_k}{k}\qquad(k\ge1)
$$

$$
\operatorname{denom}(b_k)=\prod_{p-1\mid k}p\qquad(k\ \text{偶})
$$

$$
L(f,s)=\zeta(s)^{k}L(f_1,s)
$$

## 易错点

- 把「极点阶数 = 平凡表示重数」当成对所有 Dirichlet 级数成立：它要求 L 来自自守表示或 Artin 表示；一般的 Dirichlet 级数没有这个性质。
- 照抄书中的 $p-1\mid2k$：von Staudt–Clausen 的标准形式是 $p-1\mid k$（$k$ 偶数）；书中同余式只在 $p-1\mid k$ 时成立。

## 批注

**〔易错预警〕von Staudt 的整除条件**　中译注本在 §5 出注：原书「$p-1\mid2k$」与随后的同余不自洽，正确的充分必要条件是 $p-1\mid k$；译文照录并出译注给出标准形式。引用时务必用 $p-1\mid k$，否则 $p=5$、$k=2$ 之类的例子会立刻矛盾。

**〔背景直觉〕调和级数是唯一真正发散的级数**　书中这句话的意思是：正系数 Dirichlet 级数在收敛边界处若有极点，其发散必须由 $\sum1/n$ 提供；Landau 定理把「正系数 ⇒ 实轴上有奇点」严格化。所以「极点来自 $\zeta$」并不是巧合，而是正系数与 Euler 乘积共同强制的。

## 相关

[[ch2-nonvanishing]]、[[ch1-zeta-euler]]

## 来源

- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§5，原书 pp. 36–37（PDF pp. 44–45）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch02.tex:498-529`
