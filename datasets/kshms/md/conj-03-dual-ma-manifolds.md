# 几何镜像对称：对偶族的坍缩极限互为对偶 Monge–Ampère 流形

`kshms/concept/conj-03-dual-ma-manifolds` · track A（CFT 与几何退化） · 原文 猜想 3

**问题**　镜像对称在「环面纤维化之对偶」这一几何层面应该陈述成什么？

**摘要**　几何镜像对称的猜想形式：一对对偶 Calabi–Yau 族在极大退化处，坍缩极限的光滑部分互为对偶的 Monge–Ampère 流形，其整仿射结构也互为对偶。

**别名**　Conjecture 3；geometric counterpart of mirror symmetry；duality of torus fibrations as duality of Monge–Ampère manifolds

## 陈述

对偶的 Calabi–Yau 流形族的极大退化的光滑部分，是带对偶整仿射结构的对偶 Monge–Ampère 流形。

## 记号

$(Y^{\vee},g^{\vee}_Y,\nabla^{\vee}_Y)$：命题 2 给出的对偶 Monge–Ampère 流形（与 $(Y,g_Y)$ 黎曼等同，只换平坦联络）；对偶协变格为 $(T^{\mathbb{Z}}_Y)^{\vee}$（推论 1）。

## 要点

- 这是猜想，不是定理：原文只用一句话陈述，本节没有任何论证；正文只在复阿贝尔簇情形（§8 定理 4）把它变成定理。
- 陈述把两个族配对：一个族的极大退化光滑部分 $Y$ 与对偶族的对应物 $Y^{\vee}$ 互为对偶 Monge–Ampère 流形，整仿射结构也随之对偶——这就是「环面纤维化之间的对偶」。
- 对偶只改平坦联络、不改底流形与度量（译注「『对偶』改变的是什么」）：$(Y^{\vee},g^{\vee}_Y)$ 与 $(Y,g_Y)$ 作为黎曼流形等同，所以猜想的实质落在整仿射结构上。
- 用「光滑部分」而非整个 $\bar Y$，与猜想 1 的 a) 一致：$Y^{sing}$ 不进陈述；作为实类比，带整仿射结构的 Monge–Ampère 流形对应 Calabi–Yau 流形。

## 公式

$$(\bar Y,g_{\bar Y})^{\vee}=((\bar Y)^{\vee},g^{\vee}_{\bar Y})$$

$$(T^{\mathbb{Z}}_Y)^{\vee}\subset T_{Y^{\vee}},\qquad \operatorname{Hol}(\nabla^{\vee}_Y)\subset GL(n,\mathbb{Z})$$

## 易错点

- 这是猜想，不是定理：原文一句话带过，本节其余内容是命题 2、推论 1 这类「对偶流形存在」的定理，不能用来推出本条。
- 「对偶」是两层复合：流形层面对偶 Monge–Ampère 流形（命题 2）与格层面对偶协变格（推论 1）；只说「对偶流形」会漏掉整结构。
- 本条不声称存在把 $Y$ 送到 $Y^{\vee}$ 的全局对合映射；它只说两边的（带结构的）光滑部分是彼此的对偶。

## 相关卡

- `kshms/concept/conj-01-collapse-gh-limit`
- `kshms/concept/dfn-02-monge-ampere-manifold`
- `kshms/concept/prp-02-dual-monge-ampere-manifold`
- `kshms/remark/rmk-06-legendre-idea`

## 出处

- Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25） §3.2（原文 p.19）；锚点 `源码/chunks/ch03.tex:287-290（猜想 3）`

> 原文 p19 §3.2；译本 p19；前有命题 2（对偶 Monge–Ampère 流形存在）与推论 1（整结构对偶），译注「『对偶』改变的是什么」说明对偶只换联络。
