# 扰动构造逐范畴成立；命题 4、5 应在 operad 代数上成立

`kshms/remark/rmk-17-perturbation-general` · track D（Morse 机器） · 原文 注 17

**问题**　同调扰动（投影算子加同伦）为什么能从 $A_\infty$-代数推广到任意非幺 $A_\infty$-范畴？

**摘要**　同调扰动可逐态射空间搬到任意非幺 $A_\infty$-范畴：给定 $\Pi_{X,Y},H_{X,Y}$ 后公式不变，所得范畴与原范畴等价；作者并预期命题 4、5 对 operad 上的代数也成立。

**别名**　Remark 17；perturbation for $A_\infty$-categories；operad 上的推广

## 陈述

a) 类似的构造对任意非幺 $A_\infty$-范畴都适用。此时需要对每个分次态射空间 $\operatorname{Hom}(X,Y)$ 给定投影算子 $\Pi_{X,Y}$ 与同伦 $H_{X,Y}$。所有公式都与 $A_\infty$-代数的情形相同。所得的 $A_\infty$-范畴，其态射空间由 $\Pi_{X,Y}(\operatorname{Hom}(X,Y))$ 给出，与原范畴等价。我们以后会用到这一事实。
b) 命题 4 与命题 5 应当在 operad 上的代数这一远为一般的情形下也成立（例如见 [M]）。

## 这条注在全文中的作用

a) 是 §6.5 把 Morse 侧的扰动构造用于一般 $A_\infty$-范畴的许可证：逐对象取 $(\Pi,H)$ 后所有 $m_k$ 公式仍有意义，且不改变等价类。b) 则把 §4 的命题 4、5 定位为 operad 代数一般理论的影子，提示原证明未用尽结构。

## 易错点

- 需要对每个分次态射空间分别给 $\Pi_{X,Y}$ 与 $H_{X,Y}$，不能只给一个全局的 $\Pi$。
- 所得范畴的态射空间是 $\Pi_{X,Y}(\operatorname{Hom}(X,Y))$，不是原空间；等价不等于同构。
- b) 是「应当成立」的预期并引 [M]，不是本文证明的定理。

## 相关卡

- `kshms/concept/dfn-05-nonunital-a-inf-category`
- `kshms/remark/rmk-18-alternative-canonical-element`

## 出处

- Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25） §6.4（原文 p.43,44）；锚点 `源码/chunks/ch07.tex:145-151（注 17）`

> 原文 p43 §6.4，注文续至 p44；中译注本 ch07.tex:145-151。
