# 扭曲结构层 $\mathcal{O}'_Y$：为什么 $Y^{an}$ 是「错的」

`kshms/remark/rmk-19-oy-tilde` · track E（刚性解析与凝聚层） · 原文 注 19

**问题**　既然 $Y^{an}$ 在奇异纤维情形不紧、也无法嵌入紧解析空间，那该用什么替换它？

**摘要**　带奇异纤维坍缩时，按 $\mathcal{O}_Y$ 造的刚性解析空间 $Y^{an}$ 不紧、也嵌入不了射影紧化；作者猜测应换成同构于 $\mathcal{O}_Y$ 的扭曲层 $\mathcal{O}'_Y$，其同构类由 $H^1(Y,\underline{\mathrm{Aut}}(\mathcal{O}_Y))$ 分类——这是非阿贝尔簇情形镜像对称所需的新要素。

**别名**　Remark 19；twisted structure sheaf $\mathcal{O}'_Y$；第一非阿贝尔上同调分类的层扭曲

## 陈述

对于带奇异纤维的坍缩，如上构造的刚性解析空间 $Y^{an}$ 似乎是「错误」的。首先，它不紧致，因为 $Y$ 不紧致。但还有一个更根本的问题：$Y^{an}$ 似乎不能嵌入到与射影代数簇相联系的紧解析空间中去。有若干迹象表明，存在另一个代数层 $\mathcal{O}'_Y$，它（在 $Y$ 上局部地）同构于 $\mathcal{O}_Y$，而与 $(Y,\mathcal{O}'_Y)$ 相联系的刚性解析空间 $(Y^{an})'$ 容许一个代数紧化。一般地，作为 $\mathcal{O}_Y$ 的扭曲版本的层 $\mathcal{O}'_Y$ 由第一非阿贝尔上同调 $H^1(Y,\underline{\mathrm{Aut}}(\mathcal{O}_Y))$ 分类，其中 $\underline{\mathrm{Aut}}(\mathcal{O}_Y)$ 是 $\mathcal{O}_Y$ 的自同构群层。因此，对于不是阿贝尔簇的 Calabi–Yau 流形的镜像对称，我们期待一个新的要素，即上同类 $[\mathcal{O}'_Y]$。

## 这条注在全文中的作用

这条注解释了 §7 为什么只在阿贝尔簇情形把 $Y^{an}$ 当真：一般情形需要额外的离散/连续参数 $[\mathcal{O}'_Y]$，它是作者留给后人的接口（后来成为 Gross–Siebert 型构造里「除子/影」的雏形），也是本文「只对阿贝尔簇证明」这一限制的技术根源之一。

## 易错点

- $\mathcal{O}'_Y$ 与 $\mathcal{O}_Y$ 局部同构，因此 $Y$ 上的解析/拓扑内容不变；变的只是层的粘接方式（由 $H^1$ 中的类决定），别把它当成换了底流形。
- 分类用的是第一**非阿贝尔**上同调（取值在自同构群层里），不是通常的 $H^1(Y,\mathcal{O}^{*})$：这里扭曲的是结构层本身，而不是线丛。
- 这是作者的猜测与期待（「有若干迹象表明」「我们期待」），不是定理；引用时不要说成已证明。

## 相关卡

- `kshms/concept/prp-09-mumford-construction`
- `kshms/concept/prp-10-analytic-hms`
- `kshms/concept/thm-04-abelian-hms`

## 出处

- Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25） §7.1（原文 p.50）；锚点 `源码/chunks/ch08.tex:90-99（注 19）`

> 原文 p50 §7.2；译本 p39；紧随其后的译注 36 说明「层扭曲由 $H^1$ 分类」的类比（线丛由 $H^1(\mathcal{O}^{*})$ 分类）。
