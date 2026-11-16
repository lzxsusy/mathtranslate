# 高斯积分 $\int_C e^{\mathrm{i}\lambda z^2}\mathrm{d}z$ 的最速下降围道

> `pi/example/steepest-descent-gaussian` · 轨道 C · 渐近方法与半经典 · 状态 draft

> **这张卡练什么**：为什么 $e^{\mathrm{i}\lambda z^2}$ 的最速下降围道是直线 $y=x$，而不是 $y=-x$？

## 一句话

对 $\int_C e^{\mathrm{i}\lambda z^2}\mathrm{d}z$ 取 $f=-\mathrm{i}z^2$，由 $\operatorname{Im}f$ 为常数定出直线 $y=x$，把振荡积分化为高斯积分。

## 设定

计算 $I(\lambda)=\int_C e^{\mathrm{i}\lambda z^2}\mathrm{d}z$（$\lambda>0$），$C$ 待定。先把被积函数写成 $e^{-\lambda f}$，找 $f'=0$ 的非退化鞍点，再定出经过它的最速下降围道并求首阶值。

## 计算

**第 1 步**：取 $f(z)=-\mathrm{i}z^2$，则 $e^{-\lambda f}=e^{\mathrm{i}\lambda z^2}$；$f'(z)=-2\mathrm{i}z$，唯一临界点 $z_0=0$，$f''(0)=-2\mathrm{i}\ne0$。

> 为什么：最速下降法从找非退化鞍点开始。

**第 2 步**：写 $z=x+\mathrm{i}y$：$f=-\mathrm{i}(x^2-y^2+2\mathrm{i}xy)=2xy-\mathrm{i}(x^2-y^2)$，故 $\operatorname{Re}f=2xy$、$\operatorname{Im}f=y^2-x^2$。

> 为什么：实部控制模 $e^{-\lambda\operatorname{Re}f}$，虚部在围道上须为常数。

**第 3 步**：围道过 $z_0=0$，故 $\operatorname{Im}f=0$，即 $y=\pm x$；衰减要求两端 $\operatorname{Re}f\to+\infty$。在 $y=x$ 上 $\operatorname{Re}f=2x^2\to+\infty$，在 $y=-x$ 上 $\operatorname{Re}f=-2x^2\to-\infty$。

> 为什么：$e^{-\lambda f}=e^{-\lambda\operatorname{Re}f}e^{-\mathrm{i}\lambda\operatorname{Im}f}$，只有 $\operatorname{Re}f\to+\infty$ 时模才衰减。

**第 4 步**：故取 $y=x$，方向角 $\psi=-\frac{1}{2}\operatorname{Arg}f''(0)=-\frac{1}{2}(-\frac{\pi}{2})=\frac{\pi}{4}$；等价地，由 $\frac{1}{2}f''(0)w^2>0$ 解出 $\psi=\pi/4$。

> 为什么：两个判据一致：$f''(0)$ 的辐角决定旋转角，符号由衰减条件固定。

**第 5 步**：沿 $C$ 令 $z=e^{\mathrm{i}\pi/4}u$（$u\in\mathbb{R}$）：$z^2=\mathrm{i}u^2$，$\mathrm{i}\lambda z^2=-\lambda u^2$，$\mathrm{d}z=e^{\mathrm{i}\pi/4}\mathrm{d}u$。

> 为什么：参数化把指数变成实的高斯型。

**第 6 步**：于是 $I(\lambda)=e^{\mathrm{i}\pi/4}\int_{\mathbb{R}}e^{-\lambda u^2}\mathrm{d}u=e^{\mathrm{i}\pi/4}\sqrt{\pi/\lambda}$，与公式 $\sqrt{2\pi/(\lambda f''(0))}=\sqrt{\pi/(-\mathrm{i}\lambda)}$ 一致。

> 为什么：标准高斯积分；复平方根的分支正好给出 $e^{\mathrm{i}\pi/4}$。

## 结果

$I(\lambda)=e^{\mathrm{i}\pi/4}\sqrt{\pi/\lambda}=\sqrt{\pi/(-\mathrm{i}\lambda)}$；$C$ 是直线 $y=x$，定向从 $-\infty e^{\mathrm{i}\pi/4}$ 到 $+\infty e^{\mathrm{i}\pi/4}$。

## 复核

取 $\lambda=1$ 得 $e^{\mathrm{i}\pi/4}\sqrt{\pi}$，与例 2.5.2 中 $C_{\pi/4}$ 上的结果一致；也可数值验证 $|I|^2=\pi$，或把 $z=e^{\mathrm{i}\pi/4}u$ 代回原积分确认指数为 $-\lambda u^2$。

## 易错点

- 选错分支：$y=-x$ 上 $\operatorname{Re}f=-2x^2\to-\infty$，$e^{-\lambda\operatorname{Re}f}$ 指数增长，积分发散——那是上升支。
- $f''$ 的符号：这里 $f''=-2\mathrm{i}$，$\sqrt{2\pi/(\lambda f'')}=\sqrt{\pi/(-\mathrm{i}\lambda)}=e^{\mathrm{i}\pi/4}\sqrt{\pi/\lambda}$；若把 $f''$ 写成 $2\mathrm{i}$ 会差一个 $\mathrm{i}$。
- 切角公式要按约定用：对 $\int e^{-\lambda f}$ 是 $\psi=-\frac{1}{2}\operatorname{Arg}f''$，对 $\int e^{+\lambda f}$ 才是 $\frac{\pi}{2}-\frac{1}{2}\operatorname{Arg}f''$。
- 围道定向：反向取 $C$ 得 $-e^{\mathrm{i}\pi/4}\sqrt{\pi/\lambda}$，写结果时要交代定向。

## 用到哪些概念

- [最速下降法](../concepts/steepest-descent.md)
- [莫尔斯流与最速下降曲线](../concepts/morse-flow.md)

## 相关卡

- [$\int_C e^{\mathrm{i}z^2}\,\mathrm{d}z$ 的围道计算](../examples/fresnel-integral.md)

## 出处

- §2.5.2 最速下降法（例 2.5.3），p.100（PDF p.101），源码 `ch02a.tex:1120-1135`
