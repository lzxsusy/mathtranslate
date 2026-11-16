# $\alpha z^2/2$ 的鞍点流线与最速下降围道

> `pi/example/stokes-rays-linear` · 轨道 C · 渐近方法与半经典 · 状态 draft

> **这张卡练什么**：为什么二次鞍点的两条流线合起来是一条直线，它的方向又由 $\operatorname{Arg}\alpha$ 决定？

## 一句话

对 $\int_C e^{\lambda\alpha z^2/2}\mathrm{d}z$ 解流方程，得两支 $\pm e^{Au}e^{\mathrm{i}(\pi-\theta)/2}$，合成过原点的直线围道，积分为 $\mathrm{i}\sqrt{2\pi/(\lambda\alpha)}$。

## 设定

设 $f(z)=\alpha z^2/2$，$\alpha=Ae^{\mathrm{i}\theta}\in\mathbb{C}^*$、$A>0$，$\lambda>0$，计算 $I=\int_C e^{\lambda f(z)}\mathrm{d}z$。要求用流方程定出经过唯一鞍点 $z=0$ 的最速下降围道 $C$，再算出积分值。

## 计算

**第 1 步**：鞍点：$f'(z)=\alpha z$，故 $z_0=0$，$f''(0)=\alpha\ne0$，$f(0)=0$。

> 为什么：非退化临界点是最速下降曲线的起点。

**第 2 步**：流方程 $\mathrm{d}z/\mathrm{d}u=-\overline{f'(z)}=-\bar\alpha\bar z$，初条件 $\lim_{u\to-\infty}z(u)=0$；设 $z=re^{\mathrm{i}\psi}$，则 $\mathrm{d}z/\mathrm{d}u=\dot r e^{\mathrm{i}\psi}+\mathrm{i}r\dot\psi e^{\mathrm{i}\psi}$。

> 为什么：极坐标把复方程拆成径向与角向两部分。

**第 3 步**：比较实虚部得 $\dot\psi=A\sin(\theta+2\psi)$、$\dot r=-Ar\cos(\theta+2\psi)$；取 $\theta+2\psi=\pi$（下降支）即 $\psi=\frac{\pi}{2}-\frac{\theta}{2}$，此时 $\dot\psi=0$、$\dot r=Ar$。

> 为什么：直线解要求 $\sin(\theta+2\psi)=0$；下降支对应 $\cos=-1$，径向指数增长。

**第 4 步**：积分得两支 $z(u)=\pm e^{Au}e^{\frac{\mathrm{i}}{2}(\pi-\theta)}$；$u\to-\infty$ 时两支都趋于 $0$，$u$ 增大时沿同一直线反向流出。

> 为什么：两支相差一个符号，合起来是整条过原点的直线。

**第 5 步**：在这条线上 $f(z)=\frac{A}{2}r^2e^{\mathrm{i}(\theta+\pi-\theta)}=-\frac{A}{2}r^2$ 为负实数，故 $e^{\lambda f}=e^{-\lambda Ar^2/2}$，两端衰减。

> 为什么：这正是 $\operatorname{Im}f=0$、$\operatorname{Re}f\to-\infty$ 的下降条件。

**第 6 步**：取 $z=e^{\mathrm{i}\psi}s$（$s\in\mathbb{R}$，定向从 $-\infty$ 到 $+\infty$）积分：$I=e^{\mathrm{i}\psi}\int_{\mathbb{R}}e^{-\lambda As^2/2}\mathrm{d}s=e^{\mathrm{i}\psi}\sqrt{2\pi/(\lambda A)}=\mathrm{i}\sqrt{2\pi/(\lambda\alpha)}$。

> 为什么：高斯积分给出 $\sqrt{2\pi/(\lambda A)}$；$e^{\mathrm{i}\psi}=\mathrm{i}e^{-\mathrm{i}\theta/2}=\mathrm{i}\sqrt{A/\alpha}$，合并即得。

## 结果

$I=\mathrm{i}\sqrt{\dfrac{2\pi}{\lambda\alpha}}$；$C$ 是过原点、方向角 $\psi=\frac{\pi}{2}-\frac{1}{2}\operatorname{Arg}\alpha$ 的直线（反向则整体变号）。

## 复核

取 $\alpha=2\mathrm{i}$、$\lambda=1$：$\psi=\pi/4$，$I=\mathrm{i}\sqrt{\pi/\mathrm{i}}=e^{\mathrm{i}\pi/4}\sqrt{\pi}$，与例 2.5.2 的 $C_{\pi/4}$ 结果一致；取 $\alpha=2$：$C$ 为虚轴，$I=\mathrm{i}\sqrt{\pi/\lambda}$，与直接算 $\int_{\mathrm{i}\mathbb{R}}e^{\lambda z^2}\mathrm{d}z=\mathrm{i}\int_{\mathbb{R}}e^{-\lambda y^2}\mathrm{d}y$ 相符。

## 易错点

- 流方程里 $f'$ 要先取共轭再取负；写成 $-\alpha z$ 会得到 $\operatorname{Im}f$ 不守恒的错误轨道。
- 两支 $\pm$ 是同一围道的两半，不能只取一支；只取一支只是从鞍点出发的半条射线，积分不完整。
- 本书此处把积分写成 $\int e^{\lambda f}$（不是 $\int e^{-\lambda f}$），所以要求 $\operatorname{Re}f\to-\infty$；若沿用 §2.5.2 的约定，围道要转 $90^\circ$。
- 符号与定向：$C$ 反向时 $I$ 变号；$\sqrt{1/\alpha}$ 的分支由 $\psi$ 固定，不能随手取主值。

## 用到哪些概念

- [莫尔斯流与最速下降曲线](../concepts/morse-flow.md)
- [最速下降法](../concepts/steepest-descent.md)

## 相关卡

- [$\int_C e^{\mathrm{i}z^2}\,\mathrm{d}z$ 的围道计算](../examples/fresnel-integral.md)

## 出处

- §2.5.3 莫尔斯流（例 2.5.4），p.100–101（PDF p.101–102），源码 `ch02a.tex:1152-1188`
- §2.5.3 最速下降曲线在鞍点处的切角，p.102（PDF p.103），源码 `ch02a.tex:1196-1204`
