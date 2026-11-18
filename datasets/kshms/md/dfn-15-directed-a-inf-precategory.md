# 有向 $\mathcal{A}_\infty$-预范畴

`kshms/concept/dfn-15-directed-a-inf-precategory` · track B（$A_\infty$ 形式框架） · 原文 定义 15

**问题**　把横截性完全交给指标顺序之后，$A_\infty$-预范畴会简化成什么样子？

**摘要**　对象类与 $\mathbb{Z}$ 双射、横截序列恰为指标严格递增序列的 $A_\infty$-预范畴；此时扩张性质化为「每个对象在两侧都有与之拟同构的对象」。

**别名**　directed $A_\infty$-pre-category；有向 $A_\infty$-预范畴；对象类为 $\mathbb{Z}$ 的预范畴

## 陈述

有向 $A_\infty$-预范畴（directed $A_\infty$-pre-category）是指满足以下条件的 $A_\infty$-预范畴：\n\na) 对象类与整数集之间存在双射：$\mathcal{C}\simeq\mathbb{Z}$。用 $X_i$ 记对应于 $i\in\mathbb{Z}$ 的对象。\n\nb) 横截序列是 $(X_{i_1},\dots,X_{i_n})$，其中 $i_1<i_2<\cdots<i_n$。

## 记号

$X_i$：对应于 $i\in\mathbb{Z}$ 的对象；$\mathcal{C}^{\mathrm{tr}}_n$：横截序列类；$\simeq_{\mathrm{qi}}$：本卡书写记号，表示拟同构。

## 要点

- 两条数据：对象类与 $\mathbb{Z}$ 双射；横截序列类被指标顺序完全决定。
- 于是 $\operatorname{Hom}(X_i,X_j)$ 只在 $i<j$ 时有定义，$i\ge j$ 时没有定义——这就是「有向」。
- 扩张性质在此等价于：对每个 $X_i$ 存在 $j<i$ 与 $m>i$，使 $X_j$ 与 $X_m$ 都拟同构于 $X_i$（原文在定义后随即指出）。
- 原文引 [Se] 说明类似概念由 Seidel 独立提出，并据此陈述猜想 5：有向预范畴的等价类与带严格单位、对象类可数的 $A_\infty$-范畴的等价类一一对应。

## 公式

$$\mathcal{C}\simeq\mathbb{Z},\qquad X_i\longleftrightarrow i$$

$$(X_{i_1},\dots,X_{i_n})\in\mathcal{C}^{\mathrm{tr}}_n\iff i_1<i_2<\cdots<i_n$$

$$\forall\,i\ \ \exists\,j<i,\ m>i:\quad X_j\simeq_{\mathrm{qi}}X_i\simeq_{\mathrm{qi}}X_m$$

## 易错点

- 「有向」不是关于 $\operatorname{Hom}$ 的代数结构，只是说横截性由指标顺序决定。
- $i\ge j$ 时 $\operatorname{Hom}(X_i,X_j)$ 不定义，不能写成「$\operatorname{Hom}$ 为零模」；零模是数据，不定义是数据的缺失。
- b) 原文只说「横截序列是 $(X_{i_1},\dots,X_{i_n})$，$i_1<\cdots<i_n$」，未写「当且仅当」；按上下文应读作刻画，否则扩张性质中的 $X_\pm$ 无从选取。
- 「对象类可数」这一条只出现在猜想 5 中，不属于定义 15；定义 15 的对象类就是 $\mathbb{Z}$。

## 相关卡

- `kshms/concept/dfn-10-extension-property`
- `kshms/concept/dfn-13-a-inf-precategory-equivalence`
- `kshms/concept/dfn-09-quasi-isomorphism`

## 出处

- Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25） §4.4（原文 p.28）；锚点 `源码/chunks/ch04.tex:296-304（定义 15）`

> 原文 p28 §4.4（例：有向 $A_\infty$-预范畴）；译本 ch04.tex 296–304 行；§4.4 止于 p28，其后为 §5。
