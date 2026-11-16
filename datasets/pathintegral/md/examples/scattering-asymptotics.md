# 散射态的渐近行为

> `pi/example/scattering-asymptotics` · 轨道 D · 格林函数与 WKB · 状态 draft

> **这张卡练什么**：怎样从满足出射边条件的格林函数里读出透射振幅，为什么朗斯基行列式在两端算出同一个值？

## 一句话

用朗斯基行列式拼出散射态格林函数，由 $x\to\pm\infty$ 的边条件读出透射振幅 $A$。

## 设定

势场满足 $V(x)\to0$（$|x|\to\infty$），$E>0$，$k=\sqrt{2mE}/\hbar$。$\psi_1,\psi_2$ 为 $(E-\hat H)\psi=0$ 的两个线性无关解，$W=\psi_1'\psi_2-\psi_2'\psi_1$。要构造 $G$，并读出 $x'\to-\infty$、$x''\to+\infty$ 时的透射振幅。

## 计算

**第 1 步**：因 $\psi_1,\psi_2$ 满足同一方程，$W'=\psi_1''\psi_2-\psi_2''\psi_1=0$，$W$ 与 $x$ 无关。

> 为什么：代入 $\psi_i''=\frac{2m}{\hbar^2}(V-E)\psi_i$ 后，含 $V-E$ 的两项相消；$W$ 为常数是后面用同一个 $W$ 归一两端的前提。

**第 2 步**：造 $\xi(x)=\frac{2m}{\hbar^2W}\left[\theta(x-x')\psi_1(x)\psi_2(x')+\theta(x'-x)\psi_1(x')\psi_2(x)\right]$。一阶导里 $\delta$ 乘的括号 $\psi_1(x)\psi_2(x')-\psi_1(x')\psi_2(x)$ 在 $x=x'$ 为零，二阶导才多出 $\frac{2m}{\hbar^2W}\delta(x-x')W$。

> 为什么：必须是二阶导才出 $\delta$，且 $\theta$ 项满足齐次方程、整体抵消，所以 $\delta$ 的系数只由 $W$ 决定。

**第 3 步**：于是 $\left(\frac{\hbar^2}{2m}\partial_x^2-V(x)+E\right)\xi=\delta(x-x')$：$\delta$ 前的系数 $\frac{\hbar^2}{2m}\cdot\frac{2m}{\hbar^2}=1$。

> 为什么：前因子 $\frac{2m}{\hbar^2W}$ 正是为抵消 $\frac{\hbar^2}{2m}$ 而设，这是格林函数的标准归一化。

**第 4 步**：自由情形 $\psi_1=e^{ikx}$、$\psi_2=e^{-ikx}$，$W=2ik$，$\xi=\frac{m}{i\hbar^2k}e^{ik|x-x'|}$，回到例 2.7.2。

> 为什么：两个 $\theta$ 分支合成 $\theta(x-x')e^{ik(x-x')}+\theta(x'-x)e^{ik(x'-x)}=e^{ik|x-x'|}$，验证了构造。

**第 5 步**：散射情形取 $\psi_1=e^{ikx}+B(k)e^{-ikx}$（$x\to-\infty$）、$A(k)e^{ikx}$（$x\to+\infty$）；$\psi_2=A(k)e^{-ikx}$（$x\to-\infty$）、$e^{-ikx}+C(k)e^{ikx}$（$x\to+\infty$）。两端算 $W$ 都得 $2ikA$。

> 为什么：$\psi_1$ 是左入射定态（透射 $A$、反射 $B$），$\psi_2$ 是右入射定态（同一透射 $A$、反射 $C$）；$W$ 为常数，两端必须相等，这是自洽性检验。

**第 6 步**：取 $x'\to-\infty$、$x''\to+\infty$：$\psi_1(x'')\to Ae^{ikx''}$、$\psi_2(x')\to Ae^{-ikx'}$，乘积 $A^2e^{ik(x''-x')}$ 与前面的 $1/A$ 相消，得 $G=\frac{mA}{i\hbar^2k}e^{ik(x''-x')}$。

> 为什么：两个渐近式各带一个 $A$，相乘为 $A^2$；除以 $W$ 里的 $A$ 后只剩一个 $A$，故 $G$ 正比于透射振幅。

## 结果

$G(x'',x';E)=\frac{mA(k)}{i\hbar^2k}e^{ik(x''-x')}$（$x'\to-\infty$，$x''\to+\infty$）；与 $G=\frac{m}{i\hbar^2k}Ae^{ik(x''-x')}$ 对照即读出透射振幅 $A(k)$，$|A|^2$ 为透射概率。

## 复核

两端各算一次 $W$：$x\to-\infty$ 端 $\psi_1'\psi_2-\psi_2'\psi_1=2ikA$，$x\to+\infty$ 端同样得 $2ikA$，相等是构造自洽的必要条件；再取无势极限 $A=1$、$B=C=0$，结果退化为自由预解核。另外由概率守恒（实势）有 $|A|^2+|B|^2=1$，可作独立校核。

## 易错点

- 书中把 $\psi_1(x'')\psi_2(x')$ 的渐近值直接写成 $Ae^{ik(x''-x')}$，跳过了 $A^2$ 这一步；最终 $\frac{m}{i\hbar^2k}Ae^{ik(x''-x')}$ 是对的，但中间少写了一个 $A$，自己推时不要照抄。
- 只在一端算 $W$ 就下结论：只有两解满足同一方程时 $W$ 才是常数，否则两端不等。
- 漏掉 $\frac{2m}{\hbar^2W}$ 的前因子，$\delta$ 的系数会差 $2m/\hbar^2$ 倍。
- $\theta(x''-x')$ 与 $\theta(x'-x'')$ 写反，会把两条拼接的入射、出射角色互换。

## 用到哪些概念

- [固定能量格林函数](../concepts/fixed-energy-green-function.md)
- [经由路径积分的 WKB](../concepts/wkb-path-integral.md)

## 相关卡

- [自由粒子的固定能量格林函数](../examples/free-green-function.md)

## 出处

- §2.7.1 例 2.7.3（散射态），p.119–121（PDF p.120–122），源码 `ch02b.tex:702-807`
