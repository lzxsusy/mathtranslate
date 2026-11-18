# $\varepsilon\to0$ 时系数是渐近级数

`kshms/remark/rmk-22-asymptotic-coefficients` · track G（复情形附录） · 原文 注 22

**问题**　§9 里把 $\varepsilon$ 固定成正常数时，系数是光滑函数；若让 $\varepsilon\to0$，这些系数变成了什么？

**摘要**　当 $\varepsilon$ 不是固定常数而是趋于 $0$ 的参数时，Dolbeault 形式展开的系数不再是函数，而是形如 $\sum_{j\ge1}e^{-\lambda_j/\varepsilon}f_{j,i_1\dots i_n}$ 的渐近级数；展开式中出现的指数集合正对应非阿基米德情形的谱 $\mathrm{Sp}_y(\alpha)$。

**别名**　Remark 22；asymptotic series in $\varepsilon$；$f_{i_1\dots i_n}(y,\varepsilon)=\sum_j e^{-\lambda_j/\varepsilon}f_{j,i_1\dots i_n}$

## 陈述

当 $\varepsilon$ 不是固定的数，而是参数 $\varepsilon\to0$ 时，系数 $f_{i_1\dots i_n}(y)$ 是 $\varepsilon$ 的渐近级数，形如
$$f_{i_1\dots i_n}(y,\varepsilon)=\sum_{j\ge1}\exp(-\lambda_j/\varepsilon)f_{j,i_1\dots i_n},$$
其中 $\lambda_j\in\mathbb{R}$，$\lambda_1<\dots<\lambda_j<\dots$，且 $\lambda_j\to+\infty$。

## 这条注在全文中的作用

它把 §9（$\varepsilon$ 固定、复情形）与 §7–§8（$\varepsilon\to0$、非阿基米德/Laurent 级数情形）接上：指数 $\{\lambda_j\}$ 就是谱 $\mathrm{Sp}_y(\alpha)$ 的元素，而 $e^{-\lambda_j/\varepsilon}$ 在 $\varepsilon\to0$ 时按 $\lambda_j$ 从小到大逐层「显形」，这正是非阿基米德估值分层在复情形的影子。

## 易错点

- $\sum_j e^{-\lambda_j/\varepsilon}f_{j}$ 一般**不收敛**，只作渐近展开理解；形式地把它当收敛级数会得到错误结论。
- 指数 $\lambda_j$ 要求单调递增且趋于 $+\infty$，这个排序是「逐层截断」能定义的前提；少了它，渐近展开的次序无从谈起。
- 只有 $\varepsilon\to0$ 时系数才变成渐近级数；$\varepsilon$ 固定时（§9 正文的其余部分）系数仍是普通的光滑函数。

## 相关卡

- `kshms/concept/dfn-23-hom-dolb`
- `kshms/remark/rmk-20-spectrum-filtration`

## 出处

- Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25） §9.2（原文 p.62）；锚点 `源码/chunks/ch10.tex:84-90（注 22）`

> 原文 p62 §9.2；译本 p46。紧接其后的正文说明该指数集合对应非阿基米德情形的 $\mathrm{Sp}_y(\alpha)$。
