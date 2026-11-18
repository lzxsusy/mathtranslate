# $A_\infty$-预范畴与带严格单位态射的 $A_\infty$-范畴：等价类一一对应

`kshms/concept/conj-04-strict-unit-equivalence` · track B（$A_\infty$ 形式框架） · 原文 猜想 4

**问题**　把带严格单位态射的 $A_\infty$-范畴都看成 $A_\infty$-预范畴，会不会把不等价的范畴并成一类？

**摘要**　仿照预范畴定义带严格单位态射的 $A_\infty$-范畴的等价后，猜想两边的等价类一一对应——即把 $A_\infty$-范畴嵌入预范畴框架不会丢失等价信息。

**别名**　Conjecture 4；A-infinity pre-categories versus A-infinity categories with strict identity morphisms；预范畴框架不丢失等价信息

## 陈述

我们类似 $A_\infty$-预范畴的情形（见上）来定义带严格单位态射的 $A_\infty$-范畴的等价。于是 $A_\infty$-预范畴的等价类与带严格单位态射的 $A_\infty$-范畴的等价类一一对应。

## 记号

「等价」按定义 13：存在有限序列 $(\mathcal{C}_0,\dots,\mathcal{C}_n)$，$\mathcal{C}_0=\mathcal{C}$、$\mathcal{C}_n=\mathcal{D}$，相邻两项间有 $A_\infty$-等价函子（定义 12）或反向；「严格单位」按定义 14：$1_X\in\operatorname{Hom}^0(X,X)$ 且 $m_2(1,f)=m_2(f,1)=f$、$m_n(\dots,1,\dots)=0$（$n\ne2$）。

## 要点

- 这是猜想，不是定理：原文说「下面的猜想为 $A_\infty$-范畴的这种推广提供了另一佐证」，把它当作支持预范畴框架的证据，而非已证结论。
- 猜想分两半：先**定义**带严格单位态射的 $A_\infty$-范畴之间的等价（照定义 13 的链式定义），再断言两边的等价类集合一一次对应。
- 动机是绕过「对应 operad 不自由、标准形变理论变复杂」的困难（定义 14 之后那段）：预范畴框架容纳带严格单位的 $A_\infty$-范畴（横截序列扩充为 $(X,S,X)$，取 $X_+=X_-=X$、$f_\pm=1_X$），猜想说这样做不丢失信息。
- 若成立，就可以在预范畴框架里做 $A_\infty$-范畴的形变理论（原文指向 \cite{KoS1} 的思路）；这是 §4 引入预范畴的主要理由之一。

## 公式

$$\mathcal{C}\sim\mathcal{D}\iff\exists\,(\mathcal{C}_0,\dots,\mathcal{C}_n),\ \mathcal{C}_0=\mathcal{C},\ \mathcal{C}_n=\mathcal{D}$$

$$m_2(1_X,f)=m_2(f,1_X)=f,\qquad m_n(f_1,\dots,1,\dots,f_n)=0\ (n\ne2)$$

## 易错点

- 这是猜想，不是定理：原文的措辞是「给出另一佐证」，没有证明，也没有说它是定理。
- 「等价」不是拟同构（那是定义 12 的 $A_\infty$-等价函子），而是定义 13 意义下的有限链；两者混用会让命题变成平凡陈述。
- 定义 14 的「严格单位」比「有单位」强：要求所有 $n\ne2$ 的高阶运算在代入 $1$ 时为 $0$；去掉这条，猜想的内容就变了。
- 原文的笔误：定义 13 中原文写作 $\mathcal{C}_0=\mathcal{D}$、$0\le i\le k-1$，译文按上下文改为 $\mathcal{C}_n=\mathcal{D}$、$0\le i\le n-1$（见该处译注）。

## 相关卡

- `kshms/concept/conj-05-directed-equivalence`
- `kshms/concept/dfn-14-strict-identity-a-inf-category`
- `kshms/concept/dfn-13-a-inf-precategory-equivalence`

## 出处

- Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25） §4.3（原文 p.27）；锚点 `源码/chunks/ch04.tex:287-290（猜想 4）`

> 原文 p27 §4.3（A∞-预范畴）之末；译本 p27；紧接其前的段落说明 operad 不自由的技术困难，本条被当作预范畴框架的「佐证」。
