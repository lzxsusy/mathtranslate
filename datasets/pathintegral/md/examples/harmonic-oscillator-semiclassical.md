# 谐振子的半经典核

> `pi/example/harmonic-oscillator-semiclassical` · 轨道 C · 渐近方法与半经典 · 状态 draft

> **这张卡练什么**：谐振子的半经典核为什么与精确传播子一致，共轭点处又为何失效？

## 一句话

求出谐振子的经典轨道与作用量，用作用量二阶导得半经典核，与精确 Mehler 核相同；$\sin\omega T=0$ 处出现焦散。

## 设定

取 $S[x]=\int_{t'}^{t''}\left(\frac{m}{2}\dot x^2-\frac{m\omega^2}{2}x^2\right)dt$，端点 $x(t')=x'$、$x(t'')=x''$，$T=t''-t'$，并假定 $\omega T\notin\pi\mathbb{Z}$。求 $K_{sc}$ 并与精确核比较。

## 计算

**第 1 步**：运动方程 $\ddot x+\omega^2x=0$ 的通解为 $x=A\sin\omega t+B\cos\omega t$；代入两端点条件解得 $x_{cl}(\tau)=\dfrac{\sin\omega(T-\tau)\,x'+\sin\omega\tau\,x''}{\sin\omega T}$，其中 $\tau=t-t'$。

> 为什么：二阶线性方程的通解含两个常数，端点条件正好确定它们；分母 $\sin\omega T$ 非零的假定保证解唯一。

**第 2 步**：把 $x_{cl}$ 代入作用量并分部积分，利用运动方程化简，得 $S_{cl}=\dfrac{m\omega}{2\sin\omega T}\left[(x'^2+x''^2)\cos\omega T-2x'x''\right]$。

> 为什么：分部积分把 $\dot x^2$ 换成 $-x\ddot x$，再用 $\ddot x=-\omega^2x$ 合并，边界项给出端点组合。

**第 3 步**：对端点求混合偏导：$\dfrac{\partial^2S_{cl}}{\partial x'\partial x''}=-\dfrac{m\omega}{\sin\omega T}$。

> 为什么：作用量对 $x'$、$x''$ 分别是二次型，交叉项系数就是混合偏导。

**第 4 步**：代入 Van Vleck 公式：$K_{sc}=\left(\dfrac{i}{2\pi\hbar}\cdot\dfrac{-m\omega}{\sin\omega T}\right)^{1/2}e^{\frac{i}{\hbar}S_{cl}}=\left(\dfrac{m\omega}{2\pi i\hbar\sin\omega T}\right)^{1/2}e^{\frac{i}{\hbar}S_{cl}}$。

> 为什么：$i\cdot(-m\omega/\sin\omega T)=-im\omega/\sin\omega T$，与自由情形同一化简。

**第 5 步**：作用量是端点的二次型，二阶展开后无高阶项，故驻定相位精确；所得 $K_{sc}$ 与 Mehler 公式给出的精确核相同。

> 为什么：高斯型路径积分对二次作用量精确，谐振子因此成为可解模型。

**第 6 步**：当 $\sin\omega T=0$，即 $T=n\pi/\omega$ 时前因子发散，所有经典轨道汇聚到同一端点，这正是共轭点与焦散，需要 Maslov 相位或一致渐近处理。

> 为什么：雅可比场 $J=\sin\omega\tau/\omega$ 在该时刻为零，Van Vleck 分母消失。

## 结果

$K_{sc}=\left(\dfrac{m\omega}{2\pi i\hbar\sin\omega T}\right)^{1/2}\exp\left\{\dfrac{im\omega}{2\hbar\sin\omega T}\left[(x'^2+x''^2)\cos\omega T-2x'x''\right]\right\}$，在 $\omega T\notin\pi\mathbb{Z}$ 时与精确核一致。

## 复核

令 $\omega\to0$：$\sin\omega T\approx\omega T$、$\cos\omega T\approx1$，作用量化为 $m(x''-x')^2/(2T)$，前因子化为 $\left(m/(2\pi i\hbar T)\right)^{1/2}$，退回自由核。再取 $x''=x'$ 且 $T\to0$，应趋于 $\delta(x''-x')$；而 $T\to\pi/\omega$ 时前因子发散，与共轭点预言一致。

## 易错点

- 作用量中 $\cos\omega T$ 只乘 $(x'^2+x''^2)$，交叉项系数是 $-2x'x''$，漏掉因子 2 会使混合偏导错倍。
- $\sin\omega T$ 可正可负，平方根分支随其变号而跳变，这就是 Maslov 相位的来源。
- 条件 $\omega T\notin\pi\mathbb{Z}$ 不能省；$T=n\pi/\omega$ 是焦散，公式发散而非核发散。
- 半经典结果精确仅因作用量为二次；对非谐势只剩首阶。
- 前因子的 $i$ 与 $1/\sqrt{\sin\omega T}$ 同属相位信息，不能只取绝对值。

## 用到哪些概念

- [半经典费曼核](../concepts/semiclassical-kernel.md)
- [雅可比场与 Van Vleck 行列式](../concepts/jacobi-field-van-vleck.md)

## 相关卡

- [谐振子传播子（Mehler 核）](../concepts/harmonic-oscillator-propagator.md)

## 出处

- 例 2.6.3 谐振子，p.115（PDF p.116），源码 `ch02b.tex:425-464`
