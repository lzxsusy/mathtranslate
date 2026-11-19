# 无分歧 Galois 表示与 lisse 层

> `gaits04/concept/unramified-lisse` · 轨 B 尖点与 Langlands 对应 · 状态 reviewed · 核验 source-only

**问题：** 为什么「处处无分歧」可以被翻译成「来自 $\pi_1(X)$ 的表示」？

**一句话：** 处处无分歧的 $n$ 维 $\overline{\mathbb Q}_\ell$-表示等同于 $X$ 上的 $n$ 维 lisse $\ell$-进层；每个闭点 $x$ 给出 Frobenius 共轭类 $\mathrm{Fr}_x$ 与半单部分 $\sigma_x$。

**别名：** `unramified Galois representation`、`lisse sheaf`、`Frobenius conjugacy class`

## 定义

设 $\sigma$ 是 $K$ 的 Galois 群的 $n$ 维不可约 $\overline{\mathbb Q}_\ell$-表示。假定 $\sigma$ 处处无分歧，即它可以看作平展基本群 $\pi_1(X)\to\mathrm{GL}_n(\overline{\mathbb Q}_\ell)$ 的表示。按定义，这样的表示等同于 $X$ 上的 lisse $\ell$-进层（又称局部系统），记为 $E_\sigma$。对每个点 $x\in|X|$，有确定的共轭类 $\mathrm{Fr}_x$（对应 $\pi_1(X)$ 的 Frobenius 元）。记 $\sigma_x\in\mathrm{GL}_n(\overline{\mathbb Q}_\ell)^{ss}/\mathrm{Conj}$ 为 $\sigma(\mathrm{Fr}_x)$ 的半单部分。（已知：若 $\sigma$ 不可约，则族 $(\sigma_x,x\in|X|)$ 唯一决定 $\sigma$。）就局部系统 $E_\sigma$ 而言，$\sigma_x$ 对应 $\mathrm{Gal}(\overline k_x/k_x)$ 中 Frobenius 元在 $E_\sigma$ 于 $x$ 处纤维上的作用。

**记号：** $\pi_1(X)$：平展基本群；$\mathrm{Fr}_x$：$x$ 处 Frobenius 共轭类；$\sigma_x$：$\sigma(\mathrm{Fr}_x)$ 的半单部分；$E_\sigma$：相应的 lisse 层。

## 要点

- 无分歧 = 在 $x$ 处惯性群作用平凡，故表示穿过 $\pi_1(X)$；这是「处处」的局部条件，不是单个位的条件。
- 取半单部分是因为 $\mathrm{Fr}_x$ 只定义到共轭、且 $\sigma(\mathrm{Fr}_x)$ 的幂幺部分依赖 $x$ 的选取；只有半单部分是共轭类不变量。
- 不可约 $\sigma$ 由 $(\sigma_x)$ 唯一决定（Chebotarev），故 §1.9 的对应可以逐点陈述。

## 公式

$$
\sigma:\pi_1(X)\to\mathrm{GL}_n(\overline{\mathbb Q}_\ell)
$$

$$
\sigma_x=\sigma(\mathrm{Fr}_x)^{ss}\in\mathrm{GL}_n(\overline{\mathbb Q}_\ell)^{ss}/\mathrm{Conj}
$$

## 易错点

- 把 $\sigma_x$ 写成 $\sigma(\mathrm{Fr}_x)$ 本身：$\mathrm{Fr}_x$ 只定义到共轭，且 $\sigma$ 在惯性群上未必平凡，取半单部分才是 $x$ 的函数。

## 批注

**〔背景直觉〕层是「带 Frobenius 的向量空间族」**　lisse 层在几何上就是局部常值的向量空间族；在每个闭点取纤维，Frobenius 在纤维上作用，其特征值就是 Satake 参数。层与表示的等价不是类比，是同一个函子。

## 相关

[[cuspidal]]、[[langlands-lafforgue]]

## 来源

- D. Gaitsgory《几何朗兰兹的非正式导论》，Bernstein–Gelbart 编《朗兰兹纲领导论》第 12 章，Birkhäuser 2004，pp. 269–281，§1.9，原书 pp. 273（PDF pp. 275）
  - 锚点：`08_source_code/SY02-13_Gaitsgory_几何朗兰兹非正式导论_中文译注/源码/chapters/ch12_sec1.tex:137-160（§1.9）`
