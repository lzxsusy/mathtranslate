# 例：斜率比较的半圆

> `grassmann/example/slope-comparison-semicircle` · 轨道 3 · Reider 与 Thaddeus 再探 · 状态 draft

> **这张卡练什么**：两条斜率不等式的比较为什么会产生一个半圆，而不是一条直线？

## 一句话

把 $\mathcal O_X[1]$ 与 $L\otimes\mathcal I_Z$ 的 Bridgeland 斜率相减，等价条件恰好是一个以 $(\frac12-\frac{d}{H^n},0)$ 为圆心的半圆内部。

## 背景定义

**半圆比较**指 $\mu_{s+it}(L\otimes\mathcal I_Z)>\mu_{s+it}(\mathcal O_X[1])$ 与点 $(s,t)$ 落在半圆 $t^2+(s-(\frac12-\frac{d}{H^n}))^2<(\frac12-\frac{d}{H^n})^2$（$t>0$）内部的等价性。

## 设定

设 $X$ 是 $n\ge2$ 维光滑射影簇，$L$ 充裕，$H=c_1(L)$，$Z\subset X$ 是长度 $d$ 的零维子概形，记 $e=\frac{d}{H^n}$。在倾斜心 $\mathcal A_s$ 中比较 $L\otimes\mathcal I_Z$ 与 $\mathcal O_X[1]$ 的 Bridgeland 斜率 $\mu_{s+it}$。

## 计算

两条斜率为 $\mu_{s+it}(\mathcal O_X[1])=\frac{t^2-s^2}{2st}$ 与 $\mu_{s+it}(L\otimes\mathcal I_Z)=\frac{(1-s)^2-t^2-2e}{2t(1-s)}$。要求后者大于前者，同乘 $2t(1-s)s>0$ 得 $s((1-s)^2-t^2-2e)>(1-s)(t^2-s^2)$；展开并消去 $s^3$ 与 $-st^2$ 项，得 $t^2<s(1-s-2e)$；配方 $s(1-s-2e)=(\frac12-e)^2-(s-(\frac12-e))^2$，即 $t^2+(s-(\frac12-e))^2<(\frac12-e)^2$，且 $t>0$。当 $H^n>2d$ 时右边为正，半圆非空。

## 要点

- 圆心是 $\frac12-\frac{d}{H^n}$，不是 $\frac12$；只有 $d=0$ 时圆心才回到 $\frac12$。
- 非空条件 $H^n>2d$ 不能省，否则半圆退化，两条斜率的次序在整个参数域内不变。
- 这里比较的是 $\mu_{s+it}$ 而不是 $\mu_H$：前者的分子分母都含 $s,t$，后者的分母是 $\operatorname{rk}E\,H^n$。
- 这个半圆正是命题 3.8 中 $C(d,H^2)$ 的来源，也是穿墙位置 $t=\sqrt{\frac14-\frac{2d}{H^n}}$ 的来源。

## 关键公式

$$
\mu_{s+it}(\mathcal O_X[1])=\frac{t^2-s^2}{2st}
$$

$$
\mu_{s+it}(L\otimes\mathcal I_Z)=\frac{(1-s)^2-t^2-\frac{2d}{H^n}}{2t(1-s)}
$$

$$
t^2+\left(s-\left(\frac12-\frac{d}{H^n}\right)\right)^2<\left(\frac12-\frac{d}{H^n}\right)^2
$$

## 相关定理

- **例（斜率比较的半圆）**：对 $n\ge2$，$\mu_{s+it}(L\otimes\mathcal I_Z)>\mu_{s+it}(\mathcal O_X[1])$ 当且仅当 $t>0$ 且 $t^2+(s-(\frac12-\frac{d}{H^n}))^2<(\frac12-\frac{d}{H^n})^2$。

## 易错点

- 圆心是 $\frac12-\frac{d}{H^n}$；写成 $\frac12$ 会把 $d>0$ 时的半圆整体平移错。
- 非空条件 $H^n>2d$ 不能省，否则不等式无解，「半圆」退化为空集。
- 两条 $\mu$ 公式的分母分别是 $2st$ 与 $2t(1-s)$，交叉相乘时必须确认都为正，否则不等号方向会反。

## 用到哪些概念

- [中心荷与相位](../concepts/central-charge-and-phase.md)
- [Bridgeland 稳定性条件](../concepts/bridgeland-stability-condition.md)

## 相关卡

- [中心荷与相位](../concepts/central-charge-and-phase.md)
- [墙与穿墙](../concepts/wall-and-wall-crossing.md)
- [有效除子的斜率](../concepts/slope-of-effective-divisor.md)

## 出处

- ch3 §3 例（半圆比较）；中译 p.64（英文 PDF p.69），源码 `chapters/ch03.tex:462`
