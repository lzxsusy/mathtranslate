# 自由粒子的半经典核

> `pi/example/free-particle-semiclassical` · 轨道 C · 渐近方法与半经典 · 状态 draft

> **这张卡练什么**：为什么自由粒子的半经典核与精确费曼核完全相等？

## 一句话

对自由粒子做驻定相位：经典轨道是直线，作用量为 $m(x''-x')^2/(2T)$，前因子恰好复现精确传播子。

## 设定

取 $S[x]=\int_{t'}^{t''}\frac{m}{2}\dot x^2\,dt$，端点固定为 $x(t')=x'$、$x(t'')=x''$，记 $T=t''-t'$。要求 $\hbar\to0$ 时 $K=\int\mathcal{D}x\,e^{\frac{i}{\hbar}S[x]}$ 的首阶，并与精确核比较。

## 计算

**第 1 步**：变分 $\delta S=-m\int\ddot x\,\delta x\,dt=0$ 给出 $\ddot x=0$，故唯一经典轨道是匀速直线 $x_{cl}(t)=x'+\frac{x''-x'}{T}(t-t')$。

> 为什么：自由情形运动方程最简单，端点条件直接定出两个积分常数。

**第 2 步**：代入得 $S_{cl}=\frac{m}{2}\left(\frac{x''-x'}{T}\right)^2T=\frac{m(x''-x')^2}{2T}$。

> 为什么：速度恒定，动能沿轨道为常数，积分只乘上时间长度。

**第 3 步**：二阶变分算子为 $A=-\frac{d^2}{dt^2}$，其基本解 $\varphi_0=t-t'$，故 $\varphi_0(t'')=T$、$\det A=2T$。

> 为什么：势能为零，雅可比方程退化为 $\ddot J=0$，初值给出 $J=t-t'$。

**第 4 步**：由 $\partial^2S_{cl}/\partial x'\partial x''=-m/T$，Van Vleck 公式给 $K_{sc}=\left(\frac{i}{2\pi\hbar}\cdot\frac{-m}{T}\right)^{1/2}e^{\frac{i}{\hbar}S_{cl}}=\left(\frac{m}{2\pi i\hbar T}\right)^{1/2}e^{\frac{im(x''-x')^2}{2\hbar T}}$。

> 为什么：$i\cdot(-m/T)=-im/T$，负号并入 $i$ 后正是标准自由核的前因子。

**第 5 步**：作用量对 $x$ 是二次的，展开到二阶后没有更高阶项，驻定相位不再有修正，故 $K_{sc}$ 就是精确的 $K$。

> 为什么：高斯积分对二次作用量精确，这是自由情形与一般势的关键差别。

## 结果

$K_{sc}(x'',t'';x',t')=\left(\frac{m}{2\pi i\hbar T}\right)^{1/2}\exp\left[\frac{im(x''-x')^2}{2\hbar T}\right]$，与精确自由传播子逐项相同。

## 复核

取 $T\to0$，前因子发散而指数迅速振荡，按分布意义趋于 $\delta(x''-x')$，与初值条件相符；量纲上前因子为 $1/\text{长度}$。也可与 §2.2.1 由路径积分直接算出的自由核对照，两者完全一致。

## 易错点

- $\partial^2S_{cl}/\partial x'\partial x''$ 是负的，负号必须与 $i$ 一起化简，否则会得到 $\sqrt{-1}$ 的错误分支。
- 不要把 $\det A=2T$ 直接当前因子；Van Vleck 公式用的是作用量二阶导，两者差一个因子与符号。
- 只有作用量为二次时半经典结果才精确；对一般势能，$K_{sc}$ 仅是首阶。
- 自由情形只有一条经典轨道，不存在多轨干涉，也没有共轭点。

## 用到哪些概念

- [半经典费曼核](../concepts/semiclassical-kernel.md)
- [雅可比场与 Van Vleck 行列式](../concepts/jacobi-field-van-vleck.md)

## 相关卡

- [自由粒子的精确核 $K_0$](../concepts/free-particle-kernel.md)

## 出处

- 例 2.6.2 自由粒子，p.114（PDF p.115），源码 `ch02b.tex:400-422`
