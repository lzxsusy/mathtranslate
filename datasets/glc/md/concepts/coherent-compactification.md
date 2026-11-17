---
id: glc/concept/coherent-compactification
type: concept
track: C
---

# 凝聚层紧化与 Fourier–Deligne 函子

> 把 Q_1-一般位置约化写成非零有理向量，得到 Bun'_n 与紧化叠 Coh'_m；Serre 对偶把下一次 Fourier 变换放到对偶空间上，逐次降秩到秩一即得 Whittaker 层。

**问题**：紧化构造里 Serre 对偶把 Ext^1(M',Ω^{n-1}) 的对偶写成什么，逐次变换的终点为什么是 Whittaker 层？

## 定义

采用使 $Q_1$ 稳定所选向量的右作用约定，$G=\operatorname{GL}_n$ 的 $Q_1$-一般位置约化可以写成一个非零有理向量：$\operatorname{Bun}_G^{Q_1\text{-gen}}=\{(M,\Omega_X^{n-1}\dashrightarrow M),\quad\text{不恒为 }0\}$。其正则版本为 $\operatorname{Bun}'_n=\{(M,s:\Omega_X^{n-1}\to M)\mid s\text{ 在一般点非零},\ M\in\operatorname{Bun}_n\}$，并有遗忘映射 $\operatorname{Bun}'_n\to\operatorname{Bun}_n$。引入紧化叠 $\operatorname{Coh}'_m=\{(\mathcal F,\Omega_X^{m-1}\xrightarrow{s}\mathcal F)\mid\mathcal F\in\operatorname{Coh},\ \operatorname{rank}\mathcal F=m\}$，开子叠 ${}^{\ne0}\operatorname{Coh}'_m$ 由 $s$ 在一般点非零定义。对 $m=n,n-1,\ldots,2$，令 $\mathcal E_m\to\operatorname{Coh}_{m-1}$ 为相对向量叠，它在 $M'$ 上的纤维为 $\operatorname{Ext}^1(M',\Omega_X^{m-1})$。

*记号*：$\Omega_X$ 为 $X$ 上的典范线丛；$\dashrightarrow$ 表示有理映射；$\operatorname{Coh}$ 为凝聚层范畴/叠；$\mathcal E_m^\vee$ 为对偶相对向量叠。

## 要点

- 由于 $M$ 局部自由且 $X$ 为光滑曲线，在一般点非零的映射 $s$ 作为凝聚层的映射是单射，并给出 $0\to\Omega_X^{n-1}\to M\to M'\to0$；这里 $M'$ 是秩 $n-1$ 的凝聚层，因 $s$ 的像未必饱和而未必局部自由。
- 扩张类属于 $\operatorname{Ext}^1(M',\Omega_X^{n-1})$，Serre 对偶给出 $\operatorname{Ext}^1(M',\Omega_X^{n-1})^*\simeq\operatorname{Hom}(\Omega_X^{n-2},M')$；这恰好是下一次 Fourier 变换所在的对偶向量空间。
- Serre 对偶把对偶相对向量叠等同于 $\mathcal E_m^\vee\simeq\operatorname{Coh}'_{m-1}$（纤维 $\operatorname{Hom}(\Omega_X^{m-2},M')$）；映射 $\mathcal E_m\to\operatorname{Coh}'_m$ 记住带有典范截面的中间项，并置 ${}^{\ne0}\mathcal E_m:=\mathcal E_m\times_{\operatorname{Coh}'_m}{}^{\ne0}\operatorname{Coh}'_m$。
- 相继的 Fourier 变换为 ${}^{\ne0}\operatorname{Coh}'_m\xleftarrow{p_m}{}^{\ne0}\mathcal E_m\xrightarrow{\mathsf F}\mathcal E_m^\vee\simeq\operatorname{Coh}'_{m-1}$（$m=n,n-1,\ldots,2$）；第一次变换按 [KL85] 的归一化定义 $\mathsf F_n:D({}^{\ne0}\operatorname{Coh}'_n)\to D(\operatorname{Coh}'_{n-1})$，重复每次降秩一。
- 秩一的终点必定是 Whittaker 层；这是 Laumon 构造中所用 Whittaker 归一化的紧化形式。

## 关键公式

- $\operatorname{Bun}'_n=\{(M,s:\Omega_X^{n-1}\to M)\mid s\text{ 在一般点非零},\ M\in\operatorname{Bun}_n\}$
- $0\longrightarrow\Omega_X^{n-1}\longrightarrow M\longrightarrow M'\longrightarrow0$
- $\operatorname{Ext}^1(M',\Omega_X^{n-1})^*\simeq\operatorname{Hom}(\Omega_X^{n-2},M')$
- ${}^{\ne0}\operatorname{Coh}'_m\xleftarrow{p_m}{}^{\ne0}\mathcal E_m\xrightarrow{\mathsf F}\mathcal E_m^\vee\simeq\operatorname{Coh}'_{m-1},\qquad m=n,n-1,\ldots,2$
- $\mathsf F_n:D({}^{\ne0}\operatorname{Coh}'_n)\longrightarrow D(\operatorname{Coh}'_{n-1})$

## 易错点

- 对偶空间里出现的是 $\operatorname{Hom}(\Omega_X^{n-2},M')$，指数是 $n-2$ 而不是 $n-1$；不要按「同一个 $\Omega_X^{n-1}$」把它改写。
- $\mathcal E_m$ 是相对向量叠（纤维为 $\operatorname{Ext}^1$），不是概形；${}^{\ne0}\mathcal E_m$ 还要再与 ${}^{\ne0}\operatorname{Coh}'_m$ 作纤维积，即要求中间项带的一般点非零截面。
- $\operatorname{Bun}'_n$ 里的 $s$ 是单射（一般点非零、$M$ 局部自由），但 $M'$ 未必局部自由；把 $0\to\Omega_X^{n-1}\to M\to M'\to0$ 当作向量丛短正合列会丢掉这一点。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§3.10 使用凝聚层的紧化变体，p.25-26（PDF p.25-26），`源码/chapters/ch03.tex:196-216（§3.10）`

## 核验

状态：`source-only`（2026-11-18）
- Stacks Project：https://stacks.math.columbia.edu/tag/0BS2 — Ext^1(M',Ω_X^{n-1})^*≃Hom(Ω_X^{n-2},M')（Serre 对偶一步）
- nLab：https://ncatlab.org/nlab/show/affine+Grassmannian — Bun'_n、Coh'_m、E_m→Coh_{m-1}、E_m^∨≃Coh'_{m-1}、F_n:D(⁰Coh'_n)→D(Coh'_{n-1})

## 关联

- `glc/concept/iterated-fourier-transform`
- `glc/concept/local-whittaker-eigenfunction`
- `glc/concept/laumon-sheaf`
