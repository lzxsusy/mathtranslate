# 半经典格林函数

> `pi/concept/semiclassical-green-function` · 轨道 D · 格林函数与 WKB · 状态 draft

> **先自测**：半经典格林函数为什么是 $\frac{1}{\hbar}\sum(-\dot x_{cl}(0)\dot x_{cl}(T_s))^{-1/2}e^{iW_{cl}/\hbar}$，求和为什么只取一部分经典轨道？

## 一句话

对时间积分用最速下降法：鞍点同时要求经典轨道与能量固定，每个鞍点贡献端点速度的平方根与相位 $\int p\,\mathrm{d}x$；围道形变决定哪些鞍点入选。

## 定义

把 $G$ 的 $T$ 积分与费曼核的路径积分合并，被积相位为 $ET+S[x]$。令 $\hbar\to0$，对路径与对 $T$ 同时作最速下降：路径方向的驻定条件 $\delta S/\delta x=0$ 就是经典运动方程，时间方向的驻定条件把轨道的能量锁定为外部给定的 $E$。因此每个鞍点 $(x_{cl},T_s)$ 是一条能量为 $E$、从 $x'$ 出发、经 $T_s$ 到达 $x''$ 的经典轨道。把二阶涨落积掉，得到首阶渐近 $$G(x'',x';E)\simeq\frac{1}{\hbar}\sum_{(x_{cl},T_s)}\left(-\dot x_{cl}(0)\dot x_{cl}(T_s)\right)^{-1/2}e^{\frac{i}{\hbar}W_{cl}},\qquad W_{cl}=ET_s+S_{cl}=\int_{x'}^{x''}p\,\mathrm{d}x.$$ 求和只遍历落在形变后围道上的鞍点。

**记号约定**：$p=\sqrt{2m(E-V(x))}$ 为经典动量；$\dot x_{cl}(0)$、$\dot x_{cl}(T_s)$ 为轨道两端速度；$W_{cl}$ 为约化作用量；$T_s$ 为经典旅行时间；$J(t)$ 为雅可比场。

## 要点

- 两个鞍点条件分别来自对路径与对 $T$ 的变分：前者是经典方程，后者把能量固定为 $E$。
- $T_s$ 是沿能量 $E$ 的轨道从 $x'$ 走到 $x''$ 所花的时间；两端都在允许区时它为实数。
- 端点落在禁区（$E<V$）时 $T_s$ 带虚部，因为 $\int\mathrm{d}x/\sqrt{2(E-V)/m}$ 在 $E<V$ 段被积函数为虚。
- 振幅 $(-\dot x_{cl}(0)\dot x_{cl}(T_s))^{-1/2}$ 来自对 $T$ 的高斯积分与 $\partial^2S_{cl}/\partial x''\partial x'=-m/J$ 的合并。
- 不是所有经典轨道都进入渐近式：必须把积分围道形变到最速下降曲线，只有被扫过的鞍点有贡献，扫过与否的跳变即斯托克斯现象（注 2.7.4）。

## 关键公式

$$
\left.\dfrac{\delta}{\delta x}\left(ET+S\right)\right|_{x=x_{cl},T=T_s}=0,\qquad\left.\dfrac{\partial}{\partial T}\left(ET+S\right)\right|_{x=x_{cl},T=T_s}=0
$$

$$
E=-\dfrac{\partial S_{cl}}{\partial T}=E_{cl}
$$

$$
G(x'',x';E)\simeq\dfrac{1}{\hbar}\sum_{(x_{cl},T_s)}\left(-\dot x_{cl}(0)\dot x_{cl}(T_s)\right)^{-\frac12}e^{\frac{i}{\hbar}W_{cl}}
$$

$$
W_{cl}=ET_s+S_{cl}=\displaystyle\int_{x'}^{x''}p\,\mathrm{d}x
$$

$$
\dfrac{\partial^2S_{cl}}{\partial x''\partial x'}=-\dfrac{m}{J(T)}
$$

## 定理与证明

### 鞍点条件就是经典轨道条件

相位 $\Phi=ET+S[x]$ 的驻点 $(x_{cl},T_s)$ 等价于：$x_{cl}$ 满足 $m\ddot x=-V'(x)$ 且 $\frac{m}{2}\dot x_{cl}^2+V(x_{cl})=E$，而 $T_s$ 是该轨道由 $x'$ 到 $x''$ 的耗时。

**完整证明**

1. 对 $x(t)$ 变分：$\delta\Phi=\delta S=\int_0^T\left(\frac{\partial L}{\partial x}-\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial L}{\partial\dot x}\right)\delta x\,\mathrm{d}t+\left[\frac{\partial L}{\partial\dot x}\delta x\right]_0^T$，端点固定使边界项为零。
   - *为什么*：路径积分固定两端点，变分只动内部点，所以边界项不参与驻定条件。
2. $\delta S=0$ 对任意 $\delta x$ 成立给出欧拉–拉格朗日方程 $m\ddot x=-V'(x)$，即经典轨道。
   - *为什么*：这正是作用量驻定的定义，也是路径积分首阶近似的出发点。
3. 对 $T$ 求导时端点固定而总时长变，用 $\mathrm{d}S_{cl}/\mathrm{d}T=\partial S/\partial T=-E_{cl}$（哈密顿–雅可比）得 $E=E_{cl}$。
   - *为什么*：作用量沿经典轨道对末时刻的偏导是负能量，故 $E+\partial_TS_{cl}=0$ 等价于轨道能量等于给定值。
4. 两条合起来：轨道能量为 $E$，$T_s$ 为其飞行时间，鞍点与经典轨道一一对应。
   - *为什么*：能量守恒把 $E$ 与轨道锁在一起，剩下的自由度只有耗时。

来源：ch02b.tex:826-843（原书 p.121–122）

### 半经典格林函数的首阶公式

在 $\hbar\to0$ 首阶，每个落在围道上的鞍点 $(x_{cl},T_s)$ 对 $G$ 的贡献为 $\frac{1}{\hbar}(-\dot x_{cl}(0)\dot x_{cl}(T_s))^{-1/2}e^{iW_{cl}/\hbar}$，其中 $W_{cl}=\int_{x'}^{x''}p\,\mathrm{d}x$。

**完整证明**

1. 把半经典核 $K_{sc}=\left(\frac{i}{2\pi\hbar}\frac{\partial^2S_{cl}}{\partial x''\partial x'}\right)^{1/2}e^{iS_{cl}/\hbar}$ 代入 $G$ 的 $T$ 积分，被积函数成为振幅乘 $e^{i(ET+S_{cl})/\hbar}$。
   - *为什么*：先固定 $T$ 作路径积分、再对 $T$ 作驻定相位，两步近似针对不同的积分变量，可以依次进行。
2. 在 $T_s$ 附近展开 $ET+S_{cl}=ET_s+S_{cl}(T_s)+\frac12\partial_T^2S_{cl}(T-T_s)^2+\cdots$。
   - *为什么*：一阶项由鞍点方程 $\partial_T(ET+S_{cl})=0$ 消失，首阶只剩二阶项。
3. 对 $T$ 作复高斯积分，得 $\left(\frac{2\pi\hbar i}{\partial_T^2S_{cl}}\right)^{1/2}$。
   - *为什么*：用 $\int e^{iau^2/2}\mathrm{d}u=\sqrt{2\pi i/a}$，此处 $a=\partial_T^2S_{cl}/\hbar$。
4. 合并三个前因子：$\frac{1}{i\hbar}\left(\frac{i}{2\pi\hbar}\right)^{1/2}\left(2\pi\hbar i\right)^{1/2}=\frac{1}{\hbar}$。
   - *为什么*：括号内相乘为 $i\cdot i=-1$，其平方根取 $i$，再乘 $1/i$ 得 $1$；常数因子必须逐项算清，否则结果的 $i$ 会错。
5. 剩余比值 $\left(\frac{\partial^2S_{cl}/\partial x''\partial x'}{\partial_T^2S_{cl}}\right)^{1/2}$ 用 $\partial^2S_{cl}/\partial x''\partial x'=-m/J(T)$ 与 $\partial_T^2S_{cl}=-\partial E_{cl}/\partial T$ 改写，代入 $J(T)=v_{cl}(0)v_{cl}(T)\int_0^T\mathrm{d}t/v_{cl}^2$ 得 $(-\dot x_{cl}(0)\dot x_{cl}(T_s))^{-1/2}$；相位写成 $W_{cl}=\int p\,\mathrm{d}x$。
   - *为什么*：两组表达式中都含 $\int\mathrm{d}t/v_{cl}^2$，正好相消，只剩两个端点速度。

来源：ch02b.tex:845-945（原书 p.122–123）

### 约化作用量等于动量沿轨道的积分

对能量为 $E$ 的经典轨道，$W_{cl}=ET_s+S_{cl}=\int_{x'}^{x''}p\,\mathrm{d}x$。

**完整证明**

1. 按定义展开作用量：$W_{cl}=ET_s+\int_0^{T_s}\left(\frac{m}{2}\dot x_{cl}^2-V(x_{cl})\right)\mathrm{d}t$。
   - *为什么*：$W_{cl}$ 的定义就是 $ET_s+S_{cl}$，只需把 $S_{cl}$ 写成拉格朗日量的积分。
2. 用 $E=\frac{m}{2}\dot x_{cl}^2+V(x_{cl})$ 把 $-V$ 换掉，得 $W_{cl}=ET_s+\int_0^{T_s}\left(m\dot x_{cl}^2-E\right)\mathrm{d}t=\int_0^{T_s}m\dot x_{cl}^2\,\mathrm{d}t$。
   - *为什么*：$ET_s$ 与 $-\int E\,\mathrm{d}t$ 相消，能量项不再出现。
3. 换元 $\mathrm{d}x=\dot x_{cl}\,\mathrm{d}t$，得 $\int_0^{T_s}m\dot x_{cl}^2\,\mathrm{d}t=\int_{x'}^{x''}p\,\mathrm{d}x$。
   - *为什么*：$p=m\dot x$ 正是经典动量，于是约化作用量就是动量沿轨道的积分。

来源：ch02b.tex:925-933（原书 p.123）

## 易错点

- 把所有经典轨道都加起来：只有形变围道扫过的鞍点才有贡献，其余要么被指数压低，要么根本不在围道上（注 2.7.4）。
- 把 $(-\dot x_{cl}(0)\dot x_{cl}(T_s))^{-1/2}$ 当正实数开方；负号给出的 $-i$ 属于马斯洛夫相位，取错分支会差一个 $i$。
- 在焦散点 $J(T_s)=0$（共轭点）处振幅发散，首阶公式失效，需要一致渐近展开。
- 把禁区里 $T_s$ 的虚部当成计算错误；它是 $\int\mathrm{d}x/\sqrt{2(E-V)/m}$ 在 $E<V$ 段的真实取值。
- 书中个别地方把 $G(x'',x';E)$ 写成 $G(x',x'';E)$（如 p.123 与例 2.7.5 开头）；对实势二者相等，但推导时端点对应关系不能跟着换。

## 相关卡

- [固定能量格林函数](../concepts/fixed-energy-green-function.md)
- [半经典费曼核](../concepts/semiclassical-kernel.md)
- [雅可比场与 Van Vleck 行列式](../concepts/jacobi-field-van-vleck.md)
- [自由粒子的半经典格林函数](../examples/free-semiclassical-green.md)

## 出处

- §2.7.2 半经典分析，p.121–131（PDF p.122–132），源码 `ch02b.tex:809-1249`
