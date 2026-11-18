# 非幺 $A_\infty$-代数

`kshms/concept/dfn-03-nonunital-a-inf-algebra` · track B（$A_\infty$ 形式框架） · 原文 定义 3

**问题**　为什么把非幺 $A_\infty$-代数定义成「余自由张量余代数上的余微分」，而不是直接罗列一列运算 $m_n$？

**摘要**　域 $k$ 上的分次模 $A$ 连同余自由张量余代数 $T_+(A[1])$ 上一个 $+1$ 次、平方为零的余微分 $d$；等价于给出一列满足 $A_\infty$ 关系的运算 $m_n$。

**别名**　non-unital $A_\infty$-algebra；非幺 $A_\infty$-代数；余自由张量余代数上的余微分（codifferential）

## 陈述

设 $A=\bigoplus_{i\in\mathbb{Z}}A^i$ 是域 $k$ 上的 $\mathbb{Z}$-分次模。$A$ 上的非幺 $A_\infty$-代数（non-unital $A_\infty$-algebra）结构，是指在余自由张量余代数（cofree tensor coalgebra）$T_+(A[1])=\bigoplus_{n\ge1}(A[1])^{\otimes n}$ 上给定一个 $+1$ 次的余微分（codifferential）$d$。

## 记号

$k$：基域（可换成 $\mathbb{Z}$-分次交换结合代数，并假定 $k$-模投射）；$A[1]$：满足 $(A[1])^i=A^{i+1}$ 的分次平移；$T_+(A[1])$：余自由张量余代数；$d$：$+1$ 次余微分；$m_n$：$d$ 的 Taylor 系数。

## 要点

- 结构是一对数据 $(A,d)$，其中 $d$ 是 $T_+(A[1])$ 上的余导子且 $d^2=0$；按定义余微分自动是余导子。
- 把 $d$ 展开成 Taylor 系数 $m_n\colon A^{\otimes n}\to A[2-n]$（$n\ge1$），$d^2=0$ 就化为 $A_\infty$ 关系的一列二次方程；特别地 $m_1^2=0$。
- 「非幺」只表示不指定单位元：定义没有要求 $A$ 含 $1$，也没有对 $m_2$ 加单位条件；$m_1$ 一般非零。
- $A[1]$ 的平移使 $m_n$ 的次数为 $2-n$，方程中的 Koszul 符号正来自这一平移以及把 $m_j$ 移过前面元素的操作。

## 公式

$$T_+(A[1])=\bigoplus_{n\ge1}(A[1])^{\otimes n}$$

$$m_n\colon A^{\otimes n}\to A[2-n],\quad n\ge1$$

$$\sum_{i+j=n+1}\sum_{0\le l\le i}\epsilon(l,j)\,m_i(a_0,\dots,a_{l-1},m_j(a_l,\dots,a_{l+j-1}),a_{l+j},\dots,a_n)=0$$

$$\epsilon(l,j)=(-1)^{j\sum_{0\le s\le l-1}\deg(a_s)+l(j-1)+j(i-1)}$$

## 易错点

- $m_n$ 的次数是 $2-n$，不是 $1-n$；少算一次平移会让 $d^2=0$ 的符号整体错位。
- 「非幺」不等于「$m_1=0$」：非幺只表示没有指定单位元，微分 $m_1$ 一般非零。
- 余微分的 $+1$ 次是相对 $A$ 的分次说的；改用 $A[1]$ 记法时不要再平移一次。
- 定义没有要求 $m_n$ 对 $n\ge3$ 消失；截断到 $m_1,m_2$ 是额外假设（微分分次代数），不是本条的内容。

## 相关卡

- `kshms/concept/dfn-04-nonunital-a-inf-morphism`
- `kshms/concept/dfn-05-nonunital-a-inf-category`

## 出处

- Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25） §4.2（原文 p.23）；锚点 `源码/chunks/ch04.tex:40-44（定义 3）`

> 原文 p23 §4.2；译本 ch04.tex:40-44；紧接其后的 ch04.tex:46-56 把 $d$ 展开为 Taylor 系数并写出 $d^2=0$ 的方程，可与原文 p23 对照。
