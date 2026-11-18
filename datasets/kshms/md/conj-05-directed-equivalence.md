# 有向 $A_\infty$-预范畴与可数 $A_\infty$-范畴：等价类一一对应

`kshms/concept/conj-05-directed-equivalence` · track B（$A_\infty$ 形式框架） · 原文 猜想 5

**问题**　在对象类可数的情形，有向 $A_\infty$-预范畴能否把带严格单位态射的 $A_\infty$-范畴的等价类完整编码？

**摘要**　有向 $A_\infty$-预范畴（对象类 $\simeq\mathbb{Z}$、横截序列递增）的等价类，猜想与带严格单位态射、对象类可数的 $A_\infty$-范畴的等价类一一对应。

**别名**　Conjecture 5；directed A-infinity pre-categories；对象类可数情形下的等价对应

## 陈述

有向 $A_\infty$-预范畴的等价类，与带严格单位态射且对象类可数的 $A_\infty$-范畴的等价类一一对应。

## 记号

有向 $A_\infty$-预范畴（定义 15）：对象类与整数集双射 $\mathcal{C}\simeq\mathbb{Z}$，对象记 $X_i$，横截序列取 $(X_{i_1},\dots,X_{i_n})$，$i_1<i_2<\dots<i_n$；$A_\infty$-范畴一侧带定义 14 的严格单位态射，且对象类可数。

## 要点

- 这是猜想，不是定理：原文说「于是可以陈述前述猜想的如下版本」，即猜想 4 在对象类可数情形下的特化，仍然没有证明。
- 有向性给出编码手段（定义 15 之后那段）：取可数 $A_\infty$-范畴 $\mathcal{C}$，构造无穷序列 $(X_i)_{i\in\mathbb{Z}}$ 使每个对象在正负指标处各出现无穷多次，再令 $\operatorname{Hom}_{\mathcal{C}'}(X_i,X_j)=\operatorname{Hom}_{\mathcal{C}}(X_i,X_j)$（$i<j$），其余 $\operatorname{Hom}$ 不定义。
- 扩张性质此时等价于：每个 $X_i$ 都有 $j<i$ 与 $m>i$ 的对象与之拟同构——正是上面反复插入同一对象所保证的。
- 与猜想 4 的差别只在「可数」这一条件：它保证序列 $(X_i)$ 可数、双向编码可行。

## 公式

$$\mathcal{C}\simeq\mathbb{Z},\quad(\mathrm{对象}\ X_i),\qquad (X_{i_1},\dots,X_{i_n}),\ i_1<\dots<i_n$$

$$\operatorname{Hom}_{\mathcal{C}'}(X_i,X_j)=\operatorname{Hom}_{\mathcal{C}}(X_i,X_j)\quad(i<j)$$

## 易错点

- 这是猜想，不是定理：原文只把它列为猜想 4 的「版本」，没有给证明。
- 有向预范畴不是普通范畴：$\operatorname{Hom}$ 只在 $i<j$ 时有定义，其余不定义，因此不能直接套用通常范畴的等价定义。
- 「对象类可数」是相对猜想 4 额外加的条件，去掉它陈述未必成立——别把猜想 5 当成猜想 4 的等价改写。

## 相关卡

- `kshms/concept/conj-04-strict-unit-equivalence`
- `kshms/concept/dfn-15-directed-a-inf-precategory`
- `kshms/concept/dfn-13-a-inf-precategory-equivalence`

## 出处

- Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25） §4.4（原文 p.28）；锚点 `源码/chunks/ch04.tex:309-312（猜想 5）`

> 原文 p28 §4.4（例：有向 A∞-预范畴）；译本 p28；其前的定义 15 给出有向性，其后的段落给出「反复插入同一对象」的构造。
