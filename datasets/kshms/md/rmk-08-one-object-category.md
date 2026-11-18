# 非幺 $A_\infty$-代数就是单对象的非幺 $A_\infty$-范畴

`kshms/remark/rmk-08-one-object-category` · track B（$A_\infty$ 形式框架） · 原文 注 8

**问题**　为什么可以把非幺 $A_\infty$-代数当作非幺 $A_\infty$-范畴的特例来处理？

**摘要**　非幺 $A_\infty$-代数可看成只有一个对象 $X$、自同态空间为 $A$ 的非幺 $A_\infty$-范畴；此后代数层面的构造都可逐字搬到范畴层面。

**别名**　Remark 8；one-object non-unital $A_\infty$-category；单对象范畴的退化情形

## 陈述

非幺 $A_\infty$-代数 $A$ 可以看成一个非幺 $A_\infty$-范畴，它只有一个对象 $X$，且 $\operatorname{Hom}(X,X)=A$。

## 这条注在全文中的作用

这条注给出「代数到范畴」的最小翻译：单对象范畴的高阶复合只剩 $A^{\otimes n}\to A$，定义 3 与定义 5 的公理于是逐条重合。它是 §4 后续构造在单对象情形下的落点，也让人可以把范畴命题反过来读成代数命题。

## 易错点

- 范畴只有一个对象，不表示它「平凡」：$\operatorname{Hom}(X,X)=A$ 仍可承载无穷多高阶运算。
- 非幺意味着不额外添加单位态射；不要为了得到 $\mathrm{id}_X$ 而给 $A$ 添一个单位元。
- 反向把范畴缩成代数只在对象集为单点时合法；多对象范畴对应的是直和 $A(X_0,\dots,X_n)=\bigoplus_{i,j}\operatorname{Hom}(X_i,X_j)$，不是单个 $A$。

## 相关卡

- `kshms/concept/dfn-03-nonunital-a-inf-algebra`
- `kshms/concept/dfn-05-nonunital-a-inf-category`
- `kshms/remark/rmk-09-cohomology-category`

## 出处

- Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25） §4.2（原文 p.24）；锚点 `源码/chunks/ch04.tex:108-111（注 8）`

> 原文 p24 §4.2，紧接定义 5（非幺 $A_\infty$-范畴）之后；中译注本 ch04.tex:108-111。
