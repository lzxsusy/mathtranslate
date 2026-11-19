# Langlands 对应与 Lafforgue 定理

> `gaits04/concept/langlands-lafforgue` · 轨 B 尖点与 Langlands 对应 · 状态 reviewed · 核验 source-only

**问题：** 对应为什么写成逐点等式 $\sigma_x=\gamma_x$，而不是写成某个整体函子？

**一句话：** $n$ 维无分歧不可约 Galois 表示与 $\mathrm{GL}_n(\mathbb A)$ 的尖点球表示一一对应，对应规则是逐点 $\sigma_x=\gamma_x$。

**别名：** `Langlands correspondence`、`Lafforgue`、`global Langlands for GL_n`

## 定义

现在给出关键定义：$n$ 维无分歧不可约 Galois 表示 $\sigma$ 在 Langlands 意义下对应于 $\mathrm{GL}_n(\mathbb A)$ 的尖点自守表示 $\pi$，若对一切 $x\in|X|$ 有 $\sigma_x=\gamma_x$，其中 $\gamma_x\in\mathrm{GL}_n(\overline{\mathbb Q}_\ell)^{ss}/\mathrm{Conj}$ 是附着于 $\pi_x$ 的相应点，即 $\operatorname{Spec}(\overline{\mathbb Q}_\ell[T_x^1,\dots,T_x^{n-1},T_x^n,(T_x^n)^{-1}])$ 中的点。Langlands 猜想（现已是 Lafforgue 的定理）断言：由上述对应关系决定，$\sigma$ 的集合与 $\pi$ 的集合之间存在双射。

**记号：** $\gamma_x$：$\pi_x$ 的 Satake 参数；$\sigma_x$：Frobenius 半单部分；两者都取值在 $\mathrm{GL}_n(\overline{\mathbb Q}_\ell)^{ss}/\mathrm{Conj}$。

## 要点

- 对应是逐点的：$\sigma$ 一侧给出一族共轭类，$\pi$ 一侧由 Satake 也给出一族共轭类，双射就是这两族的逐点相等。
- 「尖点」与「不可约」是两边的限定词：去掉任一边，双射不成立（ Eisenstein 侧要另作处理）。
- 这是整体 Langlands 对应的函数域情形；数域情形仍开放。

## 公式

$$
\sigma_x=\gamma_x,\qquad \forall x\in|X|
$$

## 定理与证明

**定理（Lafforgue）**　由逐点条件 $\sigma_x=\gamma_x$ 决定的双射，给出 $n$ 维处处无分歧不可约 $\overline{\mathbb Q}_\ell$-Galois 表示与 $\mathrm{GL}_n(\mathbb A)$ 的尖点球自守表示之间的对应。

> 跳步说明：全章只陈述，不证明；证明属 Lafforgue 2002，本章未引其技术。

*出处：§1.9，原书 p.273*

## 易错点

- 把定理的方向记反：是「每个 $\sigma$ 存在唯一 $\pi$」，不是「每个 $\pi$ 来自某个 $\sigma$」——后者对非球表示要另行陈述。

## 批注

**〔易错预警〕这已是定理**　原书写「现已是 Lafforgue 的定理」（2002）。引用时不要说成猜想；对 $\mathrm{GL}_2$ 是 Drinfeld（1980 年代），一般 $n$ 是 Lafforgue。

## 相关

[[unramified-lisse]]、[[eigensheaf]]

## 来源

- D. Gaitsgory《几何朗兰兹的非正式导论》，Bernstein–Gelbart 编《朗兰兹纲领导论》第 12 章，Birkhäuser 2004，pp. 269–281，§1.9，原书 pp. 273（PDF pp. 275）
  - 锚点：`08_source_code/SY02-13_Gaitsgory_几何朗兰兹非正式导论_中文译注/源码/chapters/ch12_sec1.tex:137-160（§1.9）`
