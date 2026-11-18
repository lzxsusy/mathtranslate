# Fukaya 范畴的对象（三元组）

`kshms/concept/dfn-16-fukaya-objects` · track C（Fukaya 与退化） · 原文 定义 16

**问题**　Fukaya 范畴的对象要携带哪些数据，自旋结构与辐角提升为什么缺一不可？

**摘要**　Fukaya 范畴的对象是三元组：带自旋结构的紧定向拉格朗日子流形、其上的局部系、以及辐角函数的连续提升；并要求辛形式在相对球面类上的配对为零。

**别名**　objects of the Fukaya category；Fukaya 范畴的对象；带自旋结构与辐角提升的拉格朗日对象

## 陈述

Fukaya 范畴 $\mathcal{F}(V,\omega,J,\Omega)$ 的对象是三元组 $(L,\rho,\widetilde{Arg}_L)$，其中 $L$ 是 $V$ 中带自旋结构的紧定向拉格朗日子流形（称为对象的支撑），$\rho$ 是 $L$ 上的局部系（即带平坦联络的复向量丛），而 $\widetilde{Arg}_L:L\to\mathbb{R}$ 是 $\mathrm{Arg}_L$ 的连续提升。

我们要求：对任意元素 $\beta\in\pi_2^{\mathrm{free}}(V,L):=\pi_0(\mathrm{Maps}((D^2,\partial D^2),(V,L)))$，配对 $([\omega],\beta)$ 等于零。

## 记号

$V$ 是 $2n$ 维紧辛流形且 $c_1(TV)=0$；$\mathrm{Arg}_L$ 由关于 $J$ 的 $(n,0)$-形式 $\Omega$ 与 $L$ 的定向基给出，取值于 $\mathbb{R}/2\pi\mathbb{Z}$；$\mathcal{F}(V,\omega,J,\Omega)$ 常简记为 $\mathcal{F}(V,\omega)$ 或 $\mathcal{F}(V)$，对象常简记为 $(L,\rho)$。

## 要点

- 对象由三项数据组成：支撑 $L$ 承载几何、$\rho$ 承载系数、$\widetilde{Arg}_L$ 只用于 $\mathbb{Z}$-分级，三者各自独立。
- 自旋结构不是装饰：它给 Fredholm 算子的行列式以定向，从而确定 $m_k$ 各项的符号。
- 条件 $([\omega],\beta)=0$ 对所有相对球面类 $\beta\in\pi_2^{\mathrm{free}}(V,L)$ 提出，用于避开 $m_0$ 带来的复合问题；环面与拉格朗日子环面的主要应用满足此条件。
- $L$ 必须紧且定向；$\widetilde{Arg}_L$ 是 $\mathrm{Arg}_L$ 的连续提升，不是 $\mathrm{Arg}_L$ 本身。

## 公式

$$\mathcal{F}(V,\omega,J,\Omega)\ \text{的对象}=(L,\rho,\widetilde{Arg}_L)$$

$$([\omega],\beta)=0,\qquad \beta\in\pi_2^{\mathrm{free}}(V,L)$$

## 易错点

- $([\omega],\beta)=0$ 是对所有相对球面类的整体要求，不能只对某一个 $\beta$ 检验；原文的注 11 明说这一条件是「为了方便」而加的。
- 自旋结构与 $\widetilde{Arg}_L$ 的提升是两项独立数据：前者定符号，后者定分级；把二者混为一谈会误判对象之间的等价关系。
- $\rho$ 是局部系，即带平坦联络的复向量丛，不要求酉；这与通常 Floer 理论中取 $U(1)$ 系数的做法不同。

## 相关卡

- `kshms/concept/dfn-17-fukaya-morphism-spaces`
- `kshms/concept/dfn-18-t-transversal`

## 出处

- Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25） §5.1（原文 p.29）；锚点 `源码/chunks/ch05.tex:18-22（定义 16）`

> 原文 p29 §5.1；紧接定义 16 的译注「Fukaya 范畴的对象」说明自旋结构定符号、$\widetilde{Arg}_L$ 定分级。
