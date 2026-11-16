# 半经典费曼核

> `pi/concept/semiclassical-kernel` · 轨道 C · 渐近方法与半经典 · 状态 draft

> **先自测**：为什么 $\hbar\to0$ 时费曼核的主贡献来自经典轨道，前因子又由什么决定？

## 一句话

在 $\hbar\to0$ 时对路径积分用驻定相位：经典轨道给出 $S_{cl}$ 相位，涨落的二阶变分给出前因子；平方根分支还藏着 Maslov 相位。

## 定义

对一维费曼核 $K=\int_{x(t')=x'}^{x(t'')=x''}\mathcal{D}x\,e^{\frac{i}{\hbar}S[x]}$，取经典极限 $\hbar\to0$。作用量的驻点满足欧拉–拉格朗日方程，记作 $x_{cl}$；把路径写成 $x=x_{cl}+\gamma$，其中 $\gamma(t')=\gamma(t'')=0$。将 $S$ 展开到 $\gamma$ 的二阶，涨落积分成为高斯型，由此得到的首阶近似称为半经典费曼核 $K_{sc}$。它的相位是 $S_{cl}/\hbar$，前因子由涨落算子 $A=-\frac{d^2}{dt^2}-\frac1m V''(x_{cl})$ 的行列式或基本解 $\varphi_0$ 决定。

**记号约定**：$S_{cl}=S[x_{cl}]$；$\gamma$ 为端点固定的涨落；$A$ 为狄利克雷型二阶算子；$\varphi_0$ 满足 $A\varphi_0=0$、$\varphi_0(t')=0$、$\varphi_0'(t')=1$。

## 要点

- $\delta S=0$ 给出经典运动方程，所以驻定相位的主贡献来自连接两端点的经典轨道。
- 二阶展开只保留 $V''(x_{cl})$；更高阶项在 $\hbar\to0$ 时进入次阶。
- 高斯涨落积分给出 $\left(m/(\pi i\hbar\det A)\right)^{1/2}$，前因子是普适的 $1/\sqrt{\hbar}$ 量级。
- 利用 $\det A=2\varphi_0(t'')$ 可把前因子写成 $\left(m/(2\pi i\hbar\varphi_0)\right)^{1/2}$。
- $\varphi_0$ 过零时平方根分支翻转，产生半整数相位；有多条经典轨道时还要对每条轨道求和。

## 关键公式

$$
K(x'',t'';x',t')=\int_{x(t')=x'}^{x(t'')=x''}\mathcal{D}x\,e^{\frac{i}{\hbar}S[x]}
$$

$$
S[x]=S_{cl}+\int_{t'}^{t''}\left(\frac{m}{2}\dot\gamma^2-\frac12V''(x_{cl})\gamma^2\right)dt+O(\gamma^3)
$$

$$
K_{sc}=\left(\frac{m}{\pi i\hbar\det A}\right)^{1/2}e^{\frac{i}{\hbar}S_{cl}}
$$

$$
K_{sc}=\left(\frac{m}{2\pi i\hbar\,\varphi_0(t'')}\right)^{1/2}e^{\frac{i}{\hbar}S_{cl}}
$$

$$
A=-\frac{d^2}{dt^2}-\frac1m V''(x_{cl}(t))
$$

## 定理与证明

### 半经典核的驻定相位公式

设 $x_{cl}$ 是连接 $(x',t')$ 与 $(x'',t'')$ 的经典轨迹，$A=-\frac{d^2}{dt^2}-\frac1m V''(x_{cl})$。在 $\hbar\to0$ 的首阶，$K\simeq K_{sc}=\left(\frac{m}{\pi i\hbar\det A}\right)^{1/2}e^{\frac{i}{\hbar}S_{cl}}$。

**完整证明**

1. 令 $x=x_{cl}+\gamma$，两端固定；由 $\delta S=0$，作用量展开中的线性项消失。
   - *为什么*：经典轨迹是作用量的驻点，这是驻定相位近似的出发点。
2. 展开得 $S=S_{cl}+\int\left(\frac{m}{2}\dot\gamma^2-\frac12V''(x_{cl})\gamma^2\right)dt+O(\gamma^3)$。
   - *为什么*：一阶项为零，二阶项分别来自动能的二次项与势能在 $x_{cl}$ 处的泰勒展开。
3. 把二阶部分写成 $\int\gamma A\gamma\,dt$ 的高斯泛函积分。
   - *为什么*：$A$ 正是二阶变分算子，高斯积分只依赖它的行列式。
4. 用 §2.3 的高斯路径积分公式得 $\left(\frac{m}{\pi i\hbar\det A}\right)^{1/2}e^{\frac{i}{\hbar}S_{cl}}$。
   - *为什么*：常数因子由自由情形的归一化固定，与势的具体形状无关。

来源：ch02b.tex:31-71（原书 p.108–109）

### 共轭点处的 Maslov 相位

当 $\varphi_0(t'')=0$（共轭点，也是焦散）时前因子发散，首阶驻定相位失效；越过该点后 $\varphi_0$ 变号，平方根取连续分支会多出 $i$ 因子。累计 $\mu$ 个共轭点给出相位 $e^{\pm i\pi\mu/2}$，即 Maslov 相位。

**证明提纲**

1. 在 $\varphi_0=0$ 处 $\left(m/(2\pi i\hbar\varphi_0)\right)^{1/2}$ 发散，说明焦散附近不能用非退化驻定相位。
   - *为什么*：平方根在零点无界，驻定相位的非退化条件失效。
2. 越过零点后 $\varphi_0$ 变号，$(1/\varphi_0)^{1/2}$ 取连续分支等价于乘 $i$。
   - *为什么*：绕枝点半圈，平方根改变一个 $i$ 因子。
3. 每过一次共轭点累乘一次，$\mu$ 次后为 $i^\mu=e^{i\pi\mu/2}$；整体符号可随约定取反。
   - *为什么*：Maslov 指标就是穿过焦散的累计次数。

> **缺口**：书中只给出带 $i$ 的平方根前因子，没有定义 Maslov 指标，也未证明焦散附近的一致渐近；这里从分支跳变读出相位，完整处理需 Airy 一致展开或 §5.2 的 Maslov 修正。


来源：ch02b.tex:73-88（原书 p.109）

## 易错点

- 首阶近似不是精确核；自由粒子与谐振子因作用量二次才例外。
- $\det A$ 是泛函行列式，需按 §2.3.2 正则化，不能当有限维行列式直接算。
- 有多条经典轨道时必须逐条求和，相位不同会发生干涉；只取一条会漏掉干涉项。
- $\varphi_0(t'')=0$ 时公式发散，不能硬套；要换一致渐近并加 Maslov 相位。
- 前因子中的 $i$ 与 $\pi/4$ 常数相位不能丢，它影响干涉的相长与相消。

## 相关卡

- [雅可比场与 Van Vleck 行列式](../concepts/jacobi-field-van-vleck.md)
- [时间切片方法的行列式极限](../concepts/time-slicing-determinant.md)
- [斯托克斯射线与渐近求和](../concepts/stokes-rays-asymptotic-summation.md)
- [谐振子传播子（Mehler 核）](../concepts/harmonic-oscillator-propagator.md)

## 出处

- §2.6.1 半经典的费曼核，p.108–109（PDF p.109–110），源码 `ch02b.tex:31-88`
