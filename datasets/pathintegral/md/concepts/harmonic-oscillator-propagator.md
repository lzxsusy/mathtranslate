# 谐振子传播子（Mehler 核）

> `pi/concept/harmonic-oscillator-propagator` · 轨道 B · 高斯路径积分与谐振子 · 状态 draft

> **先自测**：谐振子传播子为什么由 $\sin\omega T$ 控制，$\omega T$ 取 $\pi$ 的整数倍时公式出了什么问题？

## 一句话

把谐振子路径积分的涨落算子 $A=-\mathrm{d}^2/\mathrm{d}t^2-\omega^2$ 用 zeta 正则化算出 $\det A=2\sin\omega T/\omega$，配合经典作用量得 Mehler 核；$\omega T\in\pi\mathbb{Z}$ 处出现焦散奇点。

## 定义

哈密顿量 $H=\frac{1}{2m}p^2+\frac{m}{2}\omega^2x^2$ 的传播子是高斯型路径积分。令 $x=x_{cl}+\gamma$，其中 $x_{cl}$ 解经典边值问题、$\gamma$ 在两端为零；经典解的分母为 $\sin\omega T$。作用量分离成 $S_{cl}$ 与涨落二次型 $\frac{m}{2}\int\gamma A\gamma\,\mathrm{d}t$，$A=-\mathrm{d}^2/\mathrm{d}t^2-\omega^2$。zeta 正则化给出 $\det A=2\sin\omega T/\omega$，代回一般高斯公式即得传播子的 Mehler 形式。

**记号约定**：$x'=x(0)$、$x''=x(T)$；$\omega$ 为角频率；$T>0$ 为演化时间；$A$ 为 Dirichlet 边界下的涨落算子。

## 要点

- 经典边值问题 $\ddot x=-\omega^2x$ 的解在 $\omega T\notin\pi\mathbb{Z}$ 时唯一，分母正是 $\sin\omega T$。
- 作用量对 $\gamma$ 没有一次项；涨落算子比自由粒子多一个常数项 $-\omega^2$，本征值整体平移。
- $\det A$ 拆成自由粒子部分 $2T$ 与收敛乘积 $\sin\omega T/(\omega T)$ 之积，得 $2\sin\omega T/\omega$，$\omega\to0$ 时回到 $2T$。
- 经典作用量由 $\dot x^2-\omega^2x^2=\frac{\mathrm{d}}{\mathrm{d}t}(x\dot x)$ 化为端点项，只依赖 $x'$、$x''$。
- $\omega T\in\pi\mathbb{Z}$ 时 $\det A=0$，预因子发散、经典解不唯一，这是焦散（共轭点），须取极限或加 Maslov 相位。

## 关键公式

$$
x_{cl}(t)=\frac{\sin\omega(T-t)}{\sin\omega T}x'+\frac{\sin\omega t}{\sin\omega T}x''
$$

$$
A=-\frac{\mathrm{d}^2}{\mathrm{d}t^2}-\omega^2,\qquad \lambda_m=\left(\frac{\pi m}{T}\right)^2-\omega^2
$$

$$
\det A=2T\cdot\frac{\sin\omega T}{\omega T}=\frac{2\sin\omega T}{\omega}
$$

$$
S_{cl}=\frac{m\omega}{2\sin\omega T}\left[\left((x')^2+(x'')^2\right)\cos\omega T-2x'x''\right]
$$

$$
K(x'',T;x',0)=\left(\frac{m\omega}{2\pi i\hbar\sin\omega T}\right)^{1/2}\exp\left\{\frac{im\omega}{2\hbar}\left[\left((x')^2+(x'')^2\right)\cot\omega T-\frac{2x'x''}{\sin\omega T}\right]\right\}
$$

## 定理与证明

### 谐振子传播子的 Mehler 形式

当 $\omega T\notin\pi\mathbb{Z}$ 时，$K(x'',T;x',0)=\left(\frac{m\omega}{2\pi i\hbar\sin\omega T}\right)^{1/2}\exp\left\{\frac{im\omega}{2\hbar}\left[\left((x')^2+(x'')^2\right)\cot\omega T-\frac{2x'x''}{\sin\omega T}\right]\right\}$。

**完整证明**

1. 解经典边值问题 $\ddot x_{cl}=-\omega^2x_{cl}$，得 $x_{cl}(t)=\frac{\sin\omega(T-t)}{\sin\omega T}x'+\frac{\sin\omega t}{\sin\omega T}x''$。
   - *为什么*：两个积分常数由端点值定出；分母 $\sin\omega T$ 出现，说明 $\omega T=n\pi$ 时解不唯一或不存在。
2. 作分解 $x=x_{cl}+\gamma$，作用量化为 $S_{cl}+\frac{m}{2}\int_0^T\gamma A\gamma\,\mathrm{d}t$，$A=-\frac{\mathrm{d}^2}{\mathrm{d}t^2}-\omega^2$。
   - *为什么*：经典解满足欧拉-拉格朗日方程，故一次变分项为零；分部积分时 $\gamma(0)=\gamma(T)=0$ 消掉边界项。
3. 算本征值 $\lambda_m=(\pi m/T)^2-\omega^2$，把乘积拆成 $\prod_m(\pi m/T)^2\cdot\prod_m\left[1-\left(\frac{\omega T}{\pi m}\right)^2\right]$。
   - *为什么*：第一个乘积就是自由粒子的情形（$2T$），第二个乘积因 $\sum_m m^{-2}$ 收敛而绝对收敛，可以单独算。
4. 用 $\prod_{m\ge1}\left[1-\left(\frac{z}{\pi m}\right)^2\right]=\frac{\sin z}{z}$（$z=\omega T$）得 $\det A=2T\cdot\frac{\sin\omega T}{\omega T}=\frac{2\sin\omega T}{\omega}$。
   - *为什么*：这是正弦的无穷乘积，收敛性与 $\sin\omega T$ 的零点位置都吻合。
5. 把 $\det A$ 代回高斯路径积分，并用 $\dot x_{cl}^2-\omega^2x_{cl}^2=\frac{\mathrm{d}}{\mathrm{d}t}(x_{cl}\dot x_{cl})$ 把 $S_{cl}$ 化为端点项，整理即得结论。
   - *为什么*：运动方程使体积分只剩边界值，端点导数由经典解给出，最终只含 $x'$、$x''$ 与 $\cot\omega T$、$1/\sin\omega T$。

来源：ch02a.tex:715-832（原书 p.93–95）

### 焦散点 $\omega T\in\pi\mathbb{Z}$ 的行为

当 $\omega T=n\pi$ 时 $\det A=0$：预因子发散、经典边值解不唯一（$x''=(-1)^nx'$ 时有无穷多条，否则无解），Mehler 公式失效，只能取 $\omega T\to n\pi$ 的极限或引入 Maslov 相位修正。

**证明提纲**

1. 令 $\varepsilon=\omega T-n\pi$，则 $\cot\omega T\approx1/\varepsilon$、$1/\sin\omega T\approx(-1)^n/\varepsilon$，指数在 $\varepsilon\to0$ 时剧烈振荡。
   - *为什么*：除 $x''=(-1)^nx'$ 外相位随 $\varepsilon$ 发散，振荡相消，只有该点附近的贡献留存。
2. 把两个近似代进指数并配方：$\frac{im\omega}{2\hbar\varepsilon}\left((x')^2+(x'')^2-2(-1)^nx'x''\right)=\frac{im\omega}{2\hbar\varepsilon}\left(x'-(-1)^nx''\right)^2$。
   - *为什么*：平方完成说明相位只在一维子流形 $x''=(-1)^nx'$ 上不随 $\varepsilon$ 振荡，其余点的贡献被振荡相消压掉，这正是焦散的含义。

> **缺口**：书中 §2.4.1 没有讨论 $\sin\omega T=0$ 的情形；这里只指出 $\det A\to0$、经典解不唯一与预因子发散，未证明极限确实是支撑在 $x''=(-1)^nx'$ 上的 $\delta$ 型分布，也未给出 Maslov 相位的具体形式。


来源：ch02a.tex:804-811（原书 p.94）

## 易错点

- $\sin\omega T=0$ 时不能把公式当有限值用：预因子发散，经典边值问题或有无穷多解或没有解。
- $\omega T>\pi$ 后部分本征值 $(\pi m/T)^2-\omega^2$ 变负，$A$ 不再正定，高斯积分只能按解析延拓理解。
- 经典作用量的边界项符号易错：$\frac{\mathrm{d}}{\mathrm{d}t}(x\dot x)=\dot x^2+x\ddot x$，代入 $\ddot x=-\omega^2x$ 才得到 $\dot x^2-\omega^2x^2$。
- 无穷乘积 $\prod_m\left[1-\left(\frac{z}{\pi m}\right)^2\right]=\frac{\sin z}{z}$ 中取 $z=\omega T$，漏掉它会把 $\det A$ 误写成 $2T$。

## 相关卡

- [zeta 函数正则化与泛函行列式](../concepts/zeta-regularization.md)
- [有限维高斯积分](../concepts/gaussian-integral.md)
- [谐振子配分函数](../concepts/harmonic-oscillator-partition.md)
- [半经典费曼核](../concepts/semiclassical-kernel.md)

## 出处

- §2.4.1 积分核，p.93–95（PDF p.94–96），源码 `ch02a.tex:715-834`
