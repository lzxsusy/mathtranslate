# 极大退化当且仅当单值算子的幂零指数为 $n+1$

`kshms/concept/prp-01-maximal-degeneration-nilpotent` · track A（CFT 与几何退化） · 原文 命题 1

**问题**　体积积分里对数因子的最高幂次，能否用单值算子的幂零指数来判定？

**摘要**　极大退化可等价地刻画为单值算子 $T$ 满足 $(T-\operatorname{Id})^{n+1}=0$ 而 $(T-\operatorname{Id})^{n}\ne0$：体积增长中对数因子的最高幂次，正是 $T$ 的幂零指数。

**别名**　maximal degeneration and unipotent monodromy；极大退化的单值算子判据；幂零指数刻画极大退化

## 陈述

Calabi–Yau 流形 $\mathcal{X}_{mer}$ 有极大退化，当且仅当：对所有充分小的 $q$，存在向量 $v\in H^n(X_q,\mathbb{C})$，使得
$$(T-\operatorname{Id})^{n+1}v=0,\qquad (T-\operatorname{Id})^{n}v\ne0,$$
其中 $T$ 是单值算子。

## 记号

$T$：$H^n(X_q,\mathbb{C})$ 上的单值算子；$\operatorname{Id}$：恒等算子；$n=\dim\mathcal{X}_{mer}$；$v$ 是见证幂零指数的向量，允许随 $q$ 变化，命题不要求它是单值截面。

## 要点

- 命题把定义 1 中「$m=n$」的体积渐近条件翻译成线性代数条件：对数因子的幂次顶到 $n$，等价于 $T$ 的幂零指数恰为 $n+1$。
- 两个条件缺一不可：只有 $(T-\operatorname{Id})^{n+1}v=0$ 时幂零指数可能更小，必须再加上 $(T-\operatorname{Id})^{n}v\ne0$ 才把指数钉在 $n+1$。
- 存在性对每个充分小的 $q$ 单独陈述，$v$ 可以随 $q$ 变化；这与「存在单值的周期积分截面」是两回事。
- 这是与 Hodge 结构形变意义下的经典定义等价的判据（原文引 [Mo]），证明路线经由幂零轨道定理与体积的上同调计算。

## 公式

$$(T-\operatorname{Id})^{n+1}v=0,\qquad (T-\operatorname{Id})^{n}v\ne0$$

$$m=n\iff (T-\operatorname{Id})^{n+1}=0,\ (T-\operatorname{Id})^{n}\ne0$$

## 证明（complete）

1. 把体积写成上同调中的 Poincaré 配对 $\langle[vol_q],[\overline{vol_q}]\rangle$。

   *为什么*：由 de Rham 定理，中间维数上同调上的配对等于体积形式的积分，故体积可以在上同调里计算。

2. 过渡到 $q$ 的方根覆盖使 $T$ 幂幺，并用 $q^{-\log(T)/2\pi i}=\sum_{k=0}^{n}\bigl(\frac{\log q}{-2\pi i}\bigr)^{k}\frac{(\log T)^{k}}{k!}$ 平凡化丛 $H^n(X_q,\mathbb{C})$。

   *为什么*：幂幺时 $\log(T)^{n+1}=0$，故展开式在 $k=n$ 处截断，这是一个有限和。

3. 由幂零轨道定理，$q^{-\log(T)/2\pi i}[vol_q]$ 乘以 $q$ 的适当幂次后成为圆盘上的全纯截面 $a(q)$，且 $a(0)\ne0$。

   *为什么*：幂零轨道定理断言 Hodge 滤过延拓为平凡化丛在整个圆盘（含 $q=0$）上的全纯滤过，故该截面的极点可以整体消去。

4. 展开配对，只有 $k+l\le n$ 的项存活；$k+l=n$ 的项贡献 $\frac{(\log|q|)^{n}}{(\pi i)^{n}n!}\bigl\langle(\log T)^{n}a(q),\overline{a(q)}\bigr\rangle$。

   *为什么*：$\log(T)$ 是实算子且关于 Poincaré 配对斜对称，交叉项合并后只剩 $\log|q|$ 的幂；$\log(T)^{n+1}=0$ 使 $k+l>n$ 的项全部消失。

5. 由极化 Hodge 结构形变的标准性质（见 [De]），$\log(T)^{n}\ne0$ 推出 $\log(T)^{n}a(0)\ne0$ 且该配对非零，故体积的对数幂次为 $n$ 当且仅当幂零指数为 $n+1$。

   *为什么*：最高次项系数非零给出 $m=n$；反之若 $m=n$，该系数必须非零，于是 $\log(T)^{n}\ne0$，即 $(T-\operatorname{Id})^{n}\ne0$ 而 $(T-\operatorname{Id})^{n+1}=0$。

## 易错点

- 条件写的是 $(T-\operatorname{Id})^{n+1}=0$，即幂零指数至多 $n+1$；只验证这一条而不检查 $(T-\operatorname{Id})^{n}\ne0$，会把更小的幂零指数误判为极大退化。
- 原文在 p13 把 $(T-\operatorname{Id})$ 与 $(T-\operatorname{id})$ 的大小写混用，两者是同一个恒等算子，不是两个不同的算子。
- 「对所有充分小的 $q$」不可减弱为「存在一列 $q\to0$」：渐近式中的 $C$、$k$、$m$ 是对整个族取的常数。

## 相关卡

- `kshms/concept/dfn-01-maximal-degeneration`
- `kshms/concept/conj-01-collapse-gh-limit`
- `kshms/concept/prp-02-dual-monge-ampere-manifold`

## 出处

- Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25） §3.1（原文 p.13）；锚点 `源码/chunks/ch03.tex:40-87（命题 1）`

> 原文 p13 §3.1，证明续至 p14；译文见 ch03.tex:40-87。译注 11（极大退化的含义）已把 $m=n$ 与单值算子的幂零指数 $n+1$ 对应起来。
