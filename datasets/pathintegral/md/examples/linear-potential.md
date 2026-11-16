# 线性势的半经典格林函数

> `pi/example/linear-potential` · 轨道 D · 格林函数与 WKB · 状态 draft

> **这张卡练什么**：$V=-\lambda x$ 的半经典格林函数为什么随 $x',x''$ 位置改变项数，半条围道为何只给 $1/2$ 的权重？

## 一句话

线性势的经典轨道、精确核、四个鞍点与分情形的围道取舍，是连接公式的原型。

## 设定

势场 $V(x)=-\lambda x$（$\lambda>0$），运动方程 $m\ddot x=\lambda$。先求固定 $T$ 的经典轨道、$S_{cl}$ 与精确核，再令 $E=0$ 解鞍点方程，按 $x',x''$ 的位置分三种情形讨论 $G$ 的半经典贡献。

## 计算

**第 1 步**：积分 $m\ddot x=\lambda$ 两次，用 $x(0)=x'$、$x(T)=x''$ 定常数：$x_{cl}(t)=x'+\frac{x''-x'}{T}t-\frac{\lambda T}{2m}t+\frac{\lambda}{2m}t^2$。

> 为什么：匀加速运动，两个端点条件正好定两个积分常数。

**第 2 步**：把 $x_{cl}$ 代入 $L=\frac{m}{2}\dot x^2+\lambda x$ 逐项积分，得 $S_{cl}=\frac{m}{2T}(x''-x')^2+\frac{\lambda T}{2}(x''+x')-\frac{\lambda^2T^3}{24m}$。

> 为什么：$\dot x^2$ 给前两项、$\lambda x$ 里的 $\lambda t^2$ 项给出三阶修正；这是精确的经典作用量，没有近似。

**第 3 步**：算出 $\frac{\partial^2S_{cl}}{\partial x''\partial x'}=-\frac{m}{T}$，故半经典核为 $\left(\frac{i}{2\pi\hbar}\cdot\left(-\frac{m}{T}\right)\right)^{1/2}e^{iS_{cl}/\hbar}=\left(\frac{m}{2\pi i\hbar T}\right)^{1/2}e^{iS_{cl}/\hbar}$，与自由粒子核同形。

> 为什么：$i\cdot(-m/T)=-im/T$，而 $(-im/T)^{1/2}=(m/iT)^{1/2}$；高斯型路径积分对二次作用量精确，所以这个核不含 $\hbar$ 的高阶修正。

**第 4 步**：取 $E=0$（能量平移等价于 $x$ 平移，转折点移到 $x=0$），鞍点方程 $E=-\partial_TS_{cl}$ 化为 $\frac{m(x''-x')^2}{2T^2}-\frac{\lambda(x''+x')}{2}+\frac{\lambda^2T^2}{8m}=0$。

> 为什么：对 $S_{cl}$ 求 $\partial_T$ 并令其等于 $-E=0$；$E=0$ 使方程只含 $T^2$、$T^0$ 与 $T^{-2}$ 三项，成为 $T^2$ 的二次方程。

**第 5 步**：解得 $T_s^{(\pm\pm)}=\sqrt{\frac{2m}{\lambda}}\left(\pm\sqrt{x'}\pm\sqrt{x''}\right)$，共四个鞍点；代回得 $S_{cl}(T_s^{(\pm\pm)})=\frac{2}{3}(2m\lambda)^{1/2}\left(\pm x'^{3/2}\pm x''^{3/2}\right)$，且 $\dot x(0)\dot x(T_s)=\frac{(x''-x')^2}{T_s^2}-\frac{\lambda^2T_s^2}{4m^2}=-\frac{2\lambda}{m}(\pm\sqrt{x'})(\pm\sqrt{x''})$。

> 为什么：第二式用鞍点方程消去 $(x''-x')^2/T_s^2$；$\dot x(0)$、$\dot x(T_s)$ 由 $x_{cl}$ 求导得到，符号组合必须与所取鞍点一致。

**第 6 步**：按位置关系挑出落在形变围道上的鞍点：$0<x'<x''$ 取 $T_s^{(-+)}$（直达）与 $T_s^{(++)}$（经 $x=0$ 反射）；$x'<0<x''$ 只取 $T_s^{(-+)}$，其 $T_s$ 带虚部（穿禁区）；$x'<x''<0$ 取 $T_s^{(-+)}$ 与半条 $T_s^{(--)}$，书写作 $T_s^{(-+)}+\frac{1}{2}T_s^{(--)}$。

> 为什么：最速下降围道从 $0$ 走到 $\infty$ 时扫过哪些鞍点，决定了求和项；半条曲线给出高斯积分的 $1/2$，这正是斯托克斯跳跃的具体形态。

## 结果

$G\simeq\frac{1}{\hbar}\sum'\left(\frac{m}{2\lambda(\pm\sqrt{x'})(\pm\sqrt{x''})}\right)^{1/2}e^{iS_{cl}/\hbar}$，求和只遍历被围道扫过的鞍点：$0<x'<x''$ 为 $\{T_s^{(-+)},T_s^{(++)}\}$，$x'<0<x''$ 为 $\{T_s^{(-+)}\}$，$x'<x''<0$ 为 $\{T_s^{(-+)},\tfrac12T_s^{(--)}\}$。三条分支的跳跃就是连接公式的来源。

## 复核

取 $x'=0$（从转折点出发）：$T_s=\sqrt{2m/\lambda}\sqrt{x''}$ 代回鞍点方程左边，三部分 $\frac{\lambda x''}{4}-\frac{\lambda x''}{2}+\frac{\lambda x''}{4}=0$；此时 $S_{cl}(T_s)=\frac{2}{3}(2m\lambda)^{1/2}x''^{3/2}$ 也等于 $\int_0^{x''}\sqrt{2m\lambda x}\,\mathrm{d}x$。另一复核：把 $S_{cl}'(T)=-\frac{\lambda^2}{8mT^2}\prod_i(T-T_s^{(i)})$ 展开，四根之和为零、三次项消失，$T^{-2}$ 项与常数项分别复现 $-\frac{m(x''-x')^2}{2T^2}$ 与 $\frac{\lambda(x''+x')}{2}$，说明四个鞍点没有遗漏。

## 易错点

- 线性势的半经典核对 $T$ 精确，但格林函数不精确：对 $T$ 的驻定相位只取首阶，且还要按围道取舍鞍点。
- 把四个鞍点全加起来：只有被形变围道扫过的那些有贡献，禁区情形其余鞍点给的是指数小的项。
- $T_s^{(-+)}+\frac12T_s^{(--)}$ 是两个鞍点贡献的线性组合，不是把两个时间相加；半条曲线给 $\frac12$，来自高斯积分在半轴上的取法。
- $E=0$ 的简化依赖“能量平移等价于 $x$ 平移”这一线性势特有性质，不能对一般势照搬。
- $x'<0$ 时 $\sqrt{x'}=i\sqrt{|x'|}$ 的分支要与 $T_s$ 的符号约定一致，取错会选到错误的鞍点。

## 用到哪些概念

- [半经典格林函数](../concepts/semiclassical-green-function.md)
- [连接公式再探](../concepts/connection-formula.md)

## 相关卡

- [自由粒子的半经典格林函数](../examples/free-semiclassical-green.md)

## 出处

- §2.7.2 例 2.7.6（线性势），p.124–131（PDF p.125–132），源码 `ch02b.tex:984-1248`
