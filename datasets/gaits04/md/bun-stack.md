# $\mathfrak{B}\mathrm{un}_n$ 是模叠而非簇

> `gaits04/concept/bun-stack` · 轨 D 层化与猜想 · 状态 reviewed · 核验 source-only

**问题：** 为什么必须从集合升级到叠？

**一句话：** $\mathfrak{B}\mathrm{un}_n$ 是模叠：$\operatorname{Hom}(S,\mathfrak{B}\mathrm{un}_n)$ 是 $X\times S$ 上秩 $n$ 向量丛的范畴，而非集合；$D^b(\mathfrak{B}\mathrm{un}_n)$ 仍有意义。

**别名：** `moduli stack`、`Bun_n stack`、`Yoneda`

## 定义

下一步，把 $\mathrm{Bun}_n$ 不只看成集合，而看成定义在 $\mathbb{F}_q$ 上代数簇的有理点集，并考虑其上的 $\ell$-进层。一个小麻烦是：$\mathrm{Bun}_n$ 背后的几何对象不是簇，而是代数叠，记为 $\mathfrak{B}\mathrm{un}_n$。叠与概形的主要差别如下。按 Yoneda，范畴的对象（此处即概形 $\mathcal Y$）由函子 $\mathrm{Schemes}\Rightarrow\mathrm{Sets}$，$S\mapsto\operatorname{Hom}(S,\mathcal Y)$ 完全决定。在 $\mathfrak{B}\mathrm{un}_n$ 的情形，上述 $\operatorname{Hom}$ 确实有定义，但不再是集合，而是范畴——考虑 $X$ 上向量丛的范畴，比考虑向量丛同构类的集合自然得多。一般地，对概形 $S$，定义 $\operatorname{Hom}(S,\mathfrak{B}\mathrm{un}_n)$ 为范畴，其对象是 $X\times S$ 上秩 $n$ 的丛，态射是向量丛之间的同构。这样定义的 $\mathfrak{B}\mathrm{un}_n$ 确实是代数叠。

**记号：** $\mathfrak{B}\mathrm{un}_n$：模叠；$\operatorname{Hom}(S,\mathfrak{B}\mathrm{un}_n)$：范畴（对象为 $X\times S$ 上的丛）；$D^b(\mathfrak{B}\mathrm{un}_n)$：导出范畴。

## 要点

- 升级的动机是自同构：向量丛有自同构群，集合层面把它们全丢掉了，而层论需要它们。
- Yoneda 在此处的形式：叠由「$S$-点构成的范畴」决定，故 $\operatorname{Hom}$ 取值在范畴而非集合。
- 叠上仍能定义 $D^b$：$\ell$-进层只看见叠的局部信息，光滑覆盖上的下降使之可行。

## 公式

$$
\operatorname{Hom}(S,\mathfrak{B}\mathrm{un}_n)=\{\text{$X\times S$ 上秩 $n$ 向量丛的范畴}\}
$$

## 易错点

- 以为叠是「带自同构的簇」：叠是函子 $\mathrm{Schemes}^{op}\to\mathrm{Groupoids}$，不是拓扑空间；说「$\mathfrak{B}\mathrm{un}_n$ 的点」时要小心是群胚。

## 批注

**〔背景直觉〕为什么 $D^b$ 还有意义**　$\ell$-进层只看见叠的「局部」信息：叠有光滑覆盖，层的拉回沿光滑覆盖下降，于是可像在簇上一样定义可构造层及其导出范畴。代价是 $D^b$ 中对象不再有「逐点取值」，只有沿 $\mathbb{F}_q$-点取纤维求迹才得到函数。

## 相关

[[bun-bijection]]、[[hecke-functor]]

## 来源

- D. Gaitsgory《几何朗兰兹的非正式导论》，Bernstein–Gelbart 编《朗兰兹纲领导论》第 12 章，Birkhäuser 2004，pp. 269–281，§3.1，原书 pp. 276–277（PDF pp. 278–279）
  - 锚点：`08_source_code/SY02-13_Gaitsgory_几何朗兰兹非正式导论_中文译注/源码/chapters/ch12_sec3.tex:3-21（§3.1）`
