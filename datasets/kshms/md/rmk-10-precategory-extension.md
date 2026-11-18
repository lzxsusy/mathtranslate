# 预范畴上部分定义的 $m_2$ 在 $H(\mathcal{C})$ 上唯一延拓

`kshms/remark/rmk-10-precategory-extension` · track B（$A_\infty$ 形式框架） · 原文 注 10

**问题**　预范畴的复合只在横截三元组上有定义，为什么取同调后就能得到真正的范畴？

**摘要**　对 $A_\infty$-预范畴，$m_2$ 只在横截序列上有定义；取 $m_1$ 上同调后它可唯一延拓，使 $H(\mathcal{C})$ 成为通常范畴，这一步依赖定义 10 的延拓性质。

**别名**　Remark 10；extension of partially defined composition；$A_\infty$-预范畴的同调范畴

## 陈述

设 $\mathcal{C}$ 是 $A_\infty$-预范畴。则在 $H(\mathcal{C})=(\mathcal{C},\operatorname{Hom}_{H(\mathcal{C})}(\cdot,\cdot))$ 上部分定义的复合 $m_2$ 可以唯一地延拓，从而在 $H(\mathcal{C})$ 上定义一个范畴结构。

## 这条注在全文中的作用

这条注补上注 9 在预范畴情形缺的一环：横截性只保证部分复合，定义 10 的延拓性质（可插入 $X_\pm$）使部分复合在 $H(\mathcal{C})$ 上无歧义。§5 的 Fukaya–Oh 范畴正以预范畴形式出现，此处是它能被当作范畴使用的前提。

## 易错点

- 「部分定义」指 $m_2$ 只对横截序列给出，不是多值或依赖选择；不同横截代表给出的复合在 $H(\mathcal{C})$ 中相等。
- 延拓发生在取同调之后；不要以为 $m_2$ 在原预范畴上已经全局定义。
- 对象与态射空间没变，只是复合被补全；$H(\mathcal{C})$ 仍是非幺范畴。

## 相关卡

- `kshms/concept/dfn-07-nonunital-a-inf-pre-category`
- `kshms/concept/dfn-10-extension-property`
- `kshms/remark/rmk-09-cohomology-category`

## 出处

- Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25） §4.3（原文 p.26）；锚点 `源码/chunks/ch04.tex:232-236（注 10）`

> 原文 p26 §4.3，紧接定义 10（延拓性质）之后；中译注本 ch04.tex:232-236。
