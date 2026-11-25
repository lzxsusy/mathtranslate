# 墙与穿墙

> `grassmann/concept/wall-and-wall-crossing` · 轨道 3 · Reider 与 Thaddeus 再探 · 状态 draft

> **先自测**：穿墙时模空间究竟发生了什么，为什么可以用翻折或翻转来描述？

## 一句话

当 $(s,t)$ 穿过半圆内的临界曲线时，$\mu_{s+it}$-稳定对象集合发生突变，模空间通过翻折或翻转相互替换，这就是穿墙现象。

## 定义

在 Bridgeland 稳定性的参数平面 $(s,t)$（$t>0$）中，使某个对象的 $\mu_{s+it}$-稳定性发生改变的点集称为**墙**。曲面 Thaddeus 对的墙是 $t=\sqrt{\frac14-\frac{2d}{H^2}}$（当 $d<\frac{2H^2}{9}$ 时它大于 $\frac16$）；当 $t$ 穿过墙时，对应割线簇 $\operatorname{Sec}^{d-1}(S)-\operatorname{Sec}^{d-2}(S)$ 上的扩张对象从稳定变为不稳定。墙两侧的模空间互为**翻折**（flip）或**翻转**（flop），$K_S=0$ 时是 Mukai 翻转。

**记号约定**：$t$-稳定 Thaddeus 对的空间是 $\mathbb P(\Ext^1(L,\mathcal O_S[1]))$ 到不变量 $(0,H,H^2/2)$ 的 $\mu_{1/2+it}$-稳定对象模空间的严格变换。

## 要点（为什么需要它）

- 墙不是固定超平面，而是半圆边界 $t^2+(s-\frac12)^2=\frac14-\frac{2d}{H^2}$；位置同时依赖 $d$ 与 $H^2$。
- $t>\frac12$ 时稳定对象恰是 Simpson 稳定层；$t$ 降到 $\frac12$ 时 $\mathbb P(\operatorname H^0(S,L))$ 被 $\mathbb P(\operatorname H^0(S,K_S+L)^\vee)$ 替换。
- 继续降到 $t=\frac16$ 出现秩 $3$ 丛，穿墙形如把 $L\otimes\mathcal I_Z\to\cdot\to\mathcal I_W^\vee[1]$ 换成反向扩张。
- $K_S=0$ 时整体是 $\operatorname{Hilb}^d(S)\times\operatorname{Hilb}^d(S)$ 上射影丛换对偶丛，即 Mukai 翻转。

## 关键公式

$$
t=\sqrt{\frac14-\frac{2d}{H^2}}
$$

$$
\mathbb P(\operatorname H^0(S,L))\ \longleftrightarrow\ \mathbb P(\operatorname H^0(S,K_S+L)^\vee)
$$

$$
\mathbb P(\operatorname H^0(S,L\otimes\mathcal I_W\otimes\mathcal I_Z))\ \leftrightarrow\ \mathbb P(\operatorname H^0(S,L\otimes\mathcal I_W\otimes\mathcal I_Z)^\vee)
$$

## 定理与证明（或缺口）

### 命题 4.1（稳定性的秩判据）

给定正整数 $r_0$。若 $t>\frac1{2r_0}$，且对 $\mathcal A_{1/2}$ 中所有奇数秩 $r\le r_0$ 的子对象 $K\subset L$ 都有 $\mu_{1/2+it}(K)<0$，则 $E_\epsilon^\bullet$ 是 $\mu_{1/2+it}$-稳定的。

**证明状态：完整**

1. 反设 $K^\bullet\subset E_\epsilon^\bullet$ 去稳定化。由极小秩论证，$K^\bullet=K$ 是奇数秩 $r$ 的 $H$-稳定层，且 $c_1(K)=\frac{r+1}{2}H$。
   - *为什么*：$r_{1/2}$ 的格点性是 $\frac{H^2}{2}$ 的整数倍，非零极小值只能是 $\frac{H^2}{2}$。
2. 由 Bogomolov 不等式，$d_{(1/2,t)}(K)\le\frac{H^2}{2r}(\frac14-r^2t^2)$；去稳定化给 $d_{(1/2,t)}(K)>0$，故 $t<\frac1{2r}$。
   - *为什么*：把 $c_1(K)-\frac r2H=\frac H2$ 代入 $d_{(1/2,t)}$ 的公式。
3. 于是 $r\le r_0$ 且 $t<\frac1{2r}\le\frac1{2r_0}$，与假设 $t>\frac1{2r_0}$ 矛盾。
   - *为什么*：整数秩的大小关系。


出处：中译 p.68（§4 命题 4.1）

## 易错点

- 墙的位置依赖 $d$ 与 $H^2$，不能只记成 $t=\frac12$：后者只是 $d=0$ 时的第一道墙。
- $t=\frac12$ 处被替换的是射影空间 $\mathbb P(\operatorname H^0(S,L))$，不是整个 Simpson 模空间；把两者等同会误判穿墙前后的模空间。
- 只有 $K_S=0$ 时穿墙才是 Mukai 翻转（flop），一般情形只是翻折（flip），两者不能混用。

## 相关卡

- [Bridgeland 稳定性条件](../concepts/bridgeland-stability-condition.md)
- [中心荷与相位](../concepts/central-charge-and-phase.md)
- [α-稳定凝聚系](../concepts/alpha-stable-coherent-system.md)

## 出处

- ch3 §1 穿墙现象与 §4 墙；中译 p.56（英文 PDF p.61），源码 `chapters/ch03.tex:88`
