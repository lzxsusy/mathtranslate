# 自由粒子的固定能量格林函数

> `pi/example/free-green-function` · 轨道 D · 格林函数与 WKB · 状态 draft

> **这张卡练什么**：自由粒子的固定能量格林函数为什么只依赖 $|x''-x'|$，$\Delta\gtrless0$ 时留数法分别围住哪个极点？

## 一句话

从自由粒子的动量积分出发，用留数算出固定能量格林函数，并写成 $e^{ik|x''-x'|}$ 的闭式。

## 设定

一维自由粒子 $V=0$，$E>0$，$k=\sqrt{2mE}/\hbar$，$\Delta=x''-x'$。用定义 $G_0(x'',x';E)=\frac{1}{i\hbar}\int_0^{\infty}\mathrm{d}T\,e^{i(E+i\epsilon)T/\hbar}K_0$ 先积掉时间，再对动量积分，求 $G_0$ 的闭式。

## 计算

**第 1 步**：写下自由核的动量表示：$K_0(x'',T;x',0)=\frac{1}{2\pi\hbar}\int_{\mathbb{R}}\mathrm{d}p\,e^{ip\Delta/\hbar}e^{-ip^2T/(2m\hbar)}$。

> 为什么：把动量本征态 $e^{ipx/\hbar}$ 展开代入，自由哈密顿量在动量表象是对角的，时间演化只给相位 $e^{-iE_pT/\hbar}$。

**第 2 步**：对 $T$ 积分：$\frac{1}{i\hbar}\int_0^{\infty}\mathrm{d}T\,e^{iT(E+i\epsilon)/\hbar}e^{-iTp^2/(2m\hbar)}=\frac{1}{E-p^2/2m+i\epsilon}$。

> 为什么：$\int_0^\infty e^{iaT}\mathrm{d}T=i/a$（$a$ 有正虚部），这里的 $a=(E+i\epsilon-p^2/2m)/\hbar$，所以结果是一个能量分母。

**第 3 步**：把分母配成二次式：$E-p^2/2m+i\epsilon=-\frac{1}{2m}(p-p_+)(p-p_-)$，$p_\pm=\pm\sqrt{2m(E+i\epsilon)}$。

> 为什么：$E+i\epsilon$ 使两个零点偏离实轴（$p_+$ 在上半平面、$p_-$ 在下半平面），这样才能用留数定理。

**第 4 步**：$\Delta>0$ 时在上半平面闭合，围道只围住 $p_+$；留数为 $-\frac{m}{p_+}e^{ip_+\Delta/\hbar}$，故 $G_0=-\frac{im}{\hbar p_+}e^{ip_+\Delta/\hbar}$。

> 为什么：$p_+$ 附近的分母是 $-\frac{p_+}{m}(p-p_+)$，留数为 $-\frac{m}{p_+}e^{ip_+\Delta/\hbar}$；半圆上的贡献由 $e^{-|p||\Delta|/\hbar}$ 压掉。

**第 5 步**：$\Delta<0$ 时在下半平面闭合，围住 $p_-=-p_+$；因 $p_-\Delta=p_+|\Delta|$，结果与 $\Delta>0$ 同形，只含 $|\Delta|$。

> 为什么：$p_-\Delta=(-p_+)(-|\Delta|)=p_+|\Delta|$，两支合并后把 $\Delta$ 换成 $|\Delta|$，这正是出射波边条件的体现。

**第 6 步**：代入 $E=\hbar^2k^2/2m$：$G_0=\frac{1}{i\hbar}\sqrt{\frac{m}{2E}}e^{i\sqrt{2mE}|\Delta|/\hbar}=\frac{m}{i\hbar^2k}e^{ik|x''-x'|}$。

> 为什么：用 $m/(\hbar^2k)=m/(\hbar\sqrt{2mE})=\sqrt{m/(2E)}/\hbar$ 把两种写法统一。

## 结果

$G_0(x'',x';E)=\frac{m}{i\hbar^2k}e^{ik|x''-x'|}$，$k=\sqrt{2mE}/\hbar$；这是出射波边界条件下的自由预解核。

## 复核

代回方程：$e^{ik|x''-x'|}$ 的分布二阶导为 $-k^2e^{ik|x''-x'|}+2ik\delta(x''-x')$，乘 $\frac{m}{i\hbar^2k}$ 后第一项与 $E$ 抵消（$E=\hbar^2k^2/2m$），第二项给 $\delta(x''-x')$。量纲复核：$m/(\hbar^2k)$ 的量纲为 $1/(\text{能量}\cdot\text{长度})$，与 $\delta(x)$ 相同。

## 易错点

- 在上半平面闭合却去围 $p_-$：$p_+$ 在上半平面、$p_-$ 在下半平面，围错得到的是入射波 $e^{-ik|x''-x'|}$。
- 把 $p_+$ 处的留数算成正号：该点附近分母为 $-\frac{p_+}{m}(p-p_+)$，留数是 $-\frac{m}{p_+}$。
- 只算 $\Delta>0$ 一支，闭式里留下未取绝对值的 $\Delta$，破坏了 $x'\leftrightarrow x''$ 的对称性。
- 忘记 $E=\hbar^2k^2/2m$，把 $\frac{1}{i\hbar}\sqrt{m/(2E)}$ 与 $\frac{m}{i\hbar^2k}$ 当成两个不同结果。

## 用到哪些概念

- [固定能量格林函数](../concepts/fixed-energy-green-function.md)

## 相关卡

- [散射态的渐近行为](../examples/scattering-asymptotics.md)
- [自由粒子的半经典格林函数](../examples/free-semiclassical-green.md)

## 出处

- §2.7.1 例 2.7.2（自由粒子），p.118–119（PDF p.119–120），源码 `ch02b.tex:630-681`
