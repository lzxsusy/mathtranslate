# $K$ 凸故 Legendre 变换局部可用；$\bar Y$ 何时是同调球

`kshms/remark/rmk-04-convex-potential-legendre` · track A（CFT 与几何退化） · 原文 注 4

**问题**　猜想 1 的光滑部分要拿来做对偶，凭什么 $K$ 的 Legendre 变换有定义？极限空间 $\bar Y$ 又该是什么拓扑型？

**摘要**　两点技术说明：$(g_{ij})$ 正定使势 $K$ 凸、Legendre 变换局部可用（§3.2 对偶所需）；并预期 $X_q$ 单连通且中间 Hodge 数消失时 $\bar Y$ 是同调球，例子中同胚于 $S^n$。

**别名**　Remark 4；convexity of the potential；homology sphere limit

## 陈述

1) 由于度量 $g_Y$ 决定的矩阵 $(g_{ij})$ 是正定的，函数 $K$ 是凸的。特别地，$K$ 的 Legendre 变换局部有定义。这一事实将在后面讨论 Monge–Ampère 流形的对偶时用到。

2) 看起来可信的是：当所有 $X_q$ 都单连通、且 $h^{k,0}(X_q)=0$（$0<k<n$）时，度量空间 $\bar Y$ 是 $n$ 维同调球。在所有例子中它事实上同胚于 $S^n$。

## 这条注在全文中的作用

1) 是猜想 1 的 c) 项与 §3.2 的接口：$g_Y$ 正定推出势 $K$ 凸，于是引理 1 的 Legendre 变换 $\widehat K$ 局部有定义，命题 2 的对偶 Monge–Ampère 流形才造得出来。2) 给猜想 1 的 a) 补一个拓扑预期：单连通加中间 Hodge 数消失时 $\bar Y$ 应是同调球，例子中甚至是 $S^n$，这提示余维条件在实际情形下相当强。

## 易错点

- 1) 的凸性是 $(g_{ij})$ 正定的直接推论，不是额外假设；但 Legendre 变换只保证**局部**有定义（$\widehat K$ 只在 $dK(U)$ 上定义），不能当作全局对偶。
- 2) 是「看起来可信」的猜测，不在猜想 1 的陈述里；原文把它放在注中，引用时不要说成猜想 1 的一部分。
- 「同调球」比「同胚于 $S^n$」弱：原文说所有例子中事实上同胚于 $S^n$，不能把后者当作前者的推论。

## 相关卡

- `kshms/concept/conj-01-collapse-gh-limit`
- `kshms/concept/dfn-02-monge-ampere-manifold`
- `kshms/concept/conj-03-dual-ma-manifolds`

## 出处

- Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25） §3.1（原文 p.15）；锚点 `源码/chunks/ch03.tex:119-125（注 4）`

> 原文 p15 §3.1，紧随猜想 1；译本 p15；其中 1) 服务于 §3.2 的引理 1 与命题 2（对偶 Monge–Ampère 流形）。
