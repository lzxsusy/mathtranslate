# 最速下降法

> `pi/concept/steepest-descent` · 轨道 C · 渐近方法与半经典 · 状态 draft

> **先自测**：为什么最速下降围道要取 $\operatorname{Im}f$ 为常数的曲线，鞍点又为何决定首阶？

## 一句话

把复围道连续形变到 $\operatorname{Im}f$ 为常数、经过鞍点的路径，使 $|e^{-\lambda f}|$ 沿路下降最快，再用高斯积分取首阶。

## 定义

设 $f,g$ 在含围道 $C$ 的区域上解析，$I(\lambda)=\int_C g(z)e^{-\lambda f(z)}\mathrm{d}z$。由柯西定理，只要端点不动、无穷远端贡献消失，$C$ 就可连续形变而 $I$ 不变。把 $C$ 变到曲线 $C'$：$\operatorname{Im}f$ 在 $C'$ 上为常数，且 $C'$ 经过非退化临界点 $z_0$（$f'(z_0)=0$、$f''(z_0)\ne0$）。沿 $C'$ 离开 $z_0$ 时 $\operatorname{Re}f$ 增大，故 $|e^{-\lambda f}|=e^{-\lambda\operatorname{Re}f}$ 下降最快；$I$ 于是化为可用拉普拉斯方法处理的实指数积分，首阶来自 $z_0$ 的二次邻域。

**记号约定**：$z=x+\mathrm{i}y$，$f=u+\mathrm{i}v$；$z_0$ 为鞍点；$C'$ 与 $C$ 同向；$\sqrt{\cdot}$ 的分支由 $C'$ 在 $z_0$ 处的切向确定。

## 要点

- 解析性把围道形变变成自由操作：只要形变中不跨过奇点、两端贡献消失，积分值不变。
- 柯西–黎曼方程给出 $\nabla u\cdot\nabla v=0$，所以 $u=\operatorname{Re}f$ 的梯度方向与 $v$ 的水平集相切，最速下降路径必落在某条 $\operatorname{Im}f$ 为常数的水平集上。
- 鞍点满足 $f'=0$；沿经过它的水平集，$\operatorname{Re}f$ 在鞍点取极小（对 $e^{-\lambda f}$ 的约定），两端 $\operatorname{Re}f\to+\infty$ 保证收敛。
- 局部展开 $f=f(z_0)+\frac{1}{2}f''(z_0)(z-z_0)^2$，高斯积分给出 $\sqrt{2\pi/(\lambda f''(z_0))}$，平方根分支由下降方向固定。
- 与驻定相位的关系：取 $f=-\mathrm{i}\phi$、$\lambda=1/\hbar$，则 $e^{-\lambda f}=e^{\mathrm{i}\phi/\hbar}$，驻定相位是沿原围道只取 $\phi'=0$ 各点的版本；两者首阶相同，$\pm\pi/4$ 的相位差来自 $\sqrt{1/f''}$。

## 关键公式

$$
I(\lambda)=\int_{C'}g(z)e^{-\lambda f(z)}\,\mathrm{d}z=e^{-\mathrm{i}\lambda\operatorname{Im}f}\int_{C'}g(z)e^{-\lambda\operatorname{Re}f(z)}\,\mathrm{d}z
$$

$$
\nabla u\cdot\nabla v=0,\qquad u=\operatorname{Re}f,\quad v=\operatorname{Im}f
$$

$$
\int_{C'}g(z)e^{\Phi(z)}\,\mathrm{d}z\sim g(z_0)e^{\Phi(z_0)}\sqrt{\dfrac{2\pi}{-\Phi''(z_0)}},\qquad \lambda\to+\infty
$$

$$
\int_{C'}g(z)e^{-\lambda f(z)}\,\mathrm{d}z\sim\sqrt{\dfrac{2\pi}{\lambda f''(z_0)}}\,g(z_0)e^{-\lambda f(z_0)}
$$

$$
$\psi=\dfrac{\pi}{2}-\dfrac{1}{2}\operatorname{Arg}f''(z_0)$（对 $\int g\,e^{\lambda f}\mathrm{d}z$）；$\psi=-\dfrac{1}{2}\operatorname{Arg}f''(z_0)$（对 $\int g\,e^{-\lambda f}\mathrm{d}z$）
$$

## 定理与证明

### 最速下降首阶公式

设 $f,g$ 解析，$C'$ 上 $\operatorname{Im}f$ 为常数、经过非退化鞍点 $z_0$，$z_0$ 是 $\operatorname{Re}f$ 在 $C'$ 上的极小，两端 $\operatorname{Re}f\to+\infty$。则 $\int_{C'}g\,e^{-\lambda f}\mathrm{d}z\sim\sqrt{2\pi/(\lambda f''(z_0))}\,g(z_0)e^{-\lambda f(z_0)}$。

**完整证明**

1. 沿 $C'$ 把常数相位提出：$I=e^{-\mathrm{i}\lambda\operatorname{Im}f}\int_{C'}g\,e^{-\lambda\operatorname{Re}f}\mathrm{d}z$。
   - *为什么*：$\operatorname{Im}f$ 在 $C'$ 上不变，相位不随 $z$ 变。
2. 以 $z=z_0+e^{\mathrm{i}\psi}s$ 参数化 $C'$，取 $\psi=-\frac{1}{2}\operatorname{Arg}f''(z_0)$（模 $\pi$），使 $\frac{1}{2}f''(z_0)e^{2\mathrm{i}\psi}=\frac{1}{2}|f''(z_0)|>0$。
   - *为什么*：这正是下降方向：二次项为正实数，$e^{-\lambda f}$ 沿 $s$ 最快衰减。
3. 展开 $f=f(z_0)+\frac{1}{2}|f''(z_0)|s^2+O(s^3)$，被积函数化为 $g(z_0)e^{-\lambda f(z_0)}e^{-\lambda|f''|s^2/2}e^{\mathrm{i}\psi}$。
   - *为什么*：$g$ 连续，取首项；$\mathrm{d}z=e^{\mathrm{i}\psi}\mathrm{d}s$ 带出切向因子。
4. 高斯积分给出 $e^{\mathrm{i}\psi}\sqrt{2\pi/(\lambda|f''(z_0)|)}\,g(z_0)e^{-\lambda f(z_0)}$，而 $e^{\mathrm{i}\psi}/\sqrt{|f''|}=\sqrt{1/f''}$，故得 $\sqrt{2\pi/(\lambda f''(z_0))}$。
   - *为什么*：复平方根把模与切向相位一并编码；误差为 $O(\lambda^{-1})$。

来源：ch02a.tex:1074-1118（原书 p.99–100）

### 驻定相位与最速下降的首阶等价

设 $\phi$ 为实函数、$\lambda=1/\hbar$、$f=-\mathrm{i}\phi$，则最速下降首阶化为驻定相位公式 $I\sim g(x_0)\sqrt{2\pi\hbar/|\phi''(x_0)|}\,e^{\mathrm{i}\phi(x_0)/\hbar+\mathrm{i}\frac{\pi}{4}\operatorname{sgn}\phi''(x_0)}$。

**完整证明**

1. 令 $f=-\mathrm{i}\phi$、$\lambda=1/\hbar$，则 $e^{-\lambda f}=e^{\mathrm{i}\phi/\hbar}$，鞍点条件 $f'=0$ 就是驻定相位条件 $\phi'=0$。
   - *为什么*：复指数在 $f'$ 为零处驻定，等价于实相位驻定。
2. 由 $f''=-\mathrm{i}\phi''$ 得 $1/f''=\mathrm{i}/\phi''$，取 $\sqrt{1/f''}=e^{\mathrm{i}\frac{\pi}{4}\operatorname{sgn}\phi''}/\sqrt{|\phi''|}$。
   - *为什么*：$\phi''>0$ 时 $\sqrt{\mathrm{i}}=e^{\mathrm{i}\pi/4}$，$\phi''<0$ 时 $\sqrt{-\mathrm{i}}=e^{-\mathrm{i}\pi/4}$，两种情形合并为符号函数。
3. 代回 $\sqrt{2\pi/(\lambda f'')}\,g\,e^{-\lambda f}$，得 $g\sqrt{2\pi\hbar/|\phi''|}\,e^{\mathrm{i}\phi/\hbar+\mathrm{i}\frac{\pi}{4}\operatorname{sgn}\phi''}$。
   - *为什么*：两式逐项相同，说明驻定相位正是最速下降在 $f$ 为纯虚时的特例。

来源：ch02a.tex:1106-1118（原书 p.100）

## 易错点

- $f$ 的符号约定要统一：对 $\int e^{-\lambda f}$，下降方向是 $\psi=-\frac{1}{2}\operatorname{Arg}f''$；对 $\int e^{+\lambda f}$ 则是 $\psi=\frac{\pi}{2}-\frac{1}{2}\operatorname{Arg}f''$。混用会选到上升分支。
- 一个鞍点不够：围道必须真的穿过它，且两端 $\operatorname{Re}f\to+\infty$；若原围道端点处 $\operatorname{Re}f$ 不增，要先形变或补上端点贡献。
- $\sqrt{2\pi/(\lambda f'')}$ 是复平方根，分支由下降方向固定；随手取主值会差一个 $e^{\pm\mathrm{i}\pi/2}$ 因子。
- 多个鞍点时各项贡献都要保留（艾里积分就是两项之和），在斯托克斯射线附近两项同阶，不能只留指数大的那项。
- 退化鞍点 $f''(z_0)=0$ 时高斯近似失效，需按 $f$ 的首个非零高阶项重新定标。

## 相关卡

- [拉普拉斯方法](../concepts/laplace-method.md)
- [莫尔斯流与最速下降曲线](../concepts/morse-flow.md)
- [$\int_C e^{\mathrm{i}z^2}\,\mathrm{d}z$ 的围道计算](../examples/fresnel-integral.md)
- [高斯积分 $\int_C e^{\mathrm{i}\lambda z^2}\mathrm{d}z$ 的最速下降围道](../examples/steepest-descent-gaussian.md)

## 出处

- §2.5.2 最速下降法，p.98–100（PDF p.99–101），源码 `ch02a.tex:1021-1136`
