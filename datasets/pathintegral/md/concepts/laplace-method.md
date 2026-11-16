# 拉普拉斯方法

> `pi/concept/laplace-method` · 轨道 C · 渐近方法与半经典 · 状态 draft

> **先自测**：为什么 $\lambda\to+\infty$ 时 $\int_a^b g\,e^{-\lambda f}\mathrm{d}x$ 只由 $f$ 的极小点邻域决定？

## 一句话

实积分 $\int g\,e^{-\lambda f}\mathrm{d}x$ 在 $\lambda\to+\infty$ 时由 $f$ 的唯一极小点邻域主导；二阶展开给出高斯首阶，$n$ 维推广只把 $f''$ 换成黑塞行列式。

## 定义

设 $f\in C^2[a,b]$ 在开区间 $(a,b)$ 内有唯一极小点 $x_0$，且 $f''(x_0)>0$；振幅 $g$ 在 $x_0$ 连续、$g(x_0)\ne0$。当 $\lambda\to+\infty$ 时，$g\,e^{-\lambda f}$ 在 $x_0$ 以外的部分被 $e^{-\lambda\delta}$ 压得可以忽略，积分与 $g(x_0)e^{-\lambda f(x_0)}\sqrt{2\pi/(\lambda f''(x_0))}$ 之比趋于 $1$。$n$ 维情形把 $f''$ 换成在极小点正定的黑塞矩阵 $H_f$，并出现因子 $(\det H_f)^{-1/2}$。

**记号约定**：$x\in\mathbb{R}$；$n$ 维时 $\mathbf{x}\in\mathbb{R}^n$；$\lambda>0$ 为大参数；$H_f=(\partial_i\partial_j f)$ 为黑塞矩阵；$g$ 是指数前的振幅。

## 要点

- 指数权重使 $x_0$ 邻域外的贡献按 $e^{-\lambda\delta}$ 衰减，故首阶只看极小点附近。
- 缩放 $x=x_0+y/\sqrt{\lambda}$ 把邻域放大到 $O(1)$ 尺度，二次项变成与 $\lambda$ 无关的标准高斯。
- 首阶有三个因子：$g(x_0)$、$e^{-\lambda f(x_0)}$、以及高斯积分 $\sqrt{2\pi/(\lambda f''(x_0))}$。
- $n$ 维时每个方向贡献一个 $1/\sqrt{\lambda}$，合起来是 $(2\pi/\lambda)^{n/2}/\sqrt{\det H_f(\mathbf{x}_0)}$。
- 若有多个极小点，要先比较 $e^{-\lambda f}$ 的指数大小；指数相同的简并情形必须把各点贡献相加，不能任取一个。

## 关键公式

$$
\int_a^b e^{-\lambda f(x)}\,\mathrm{d}x\sim e^{-\lambda f(x_0)}\sqrt{\dfrac{2\pi}{\lambda f''(x_0)}},\qquad \lambda\to+\infty
$$

$$
\int_a^b g(x)e^{-\lambda f(x)}\,\mathrm{d}x\sim g(x_0)e^{-\lambda f(x_0)}\sqrt{\dfrac{2\pi}{\lambda f''(x_0)}},\qquad \lambda\to+\infty
$$

$$
\int_{\mathbb{R}^n}g(\mathbf{x})e^{-\lambda f(\mathbf{x})}\,\mathrm{d}^n\mathbf{x}\sim\left(\dfrac{2\pi}{\lambda}\right)^{n/2}\dfrac{g(\mathbf{x}_0)}{\sqrt{\det H_f(\mathbf{x}_0)}}e^{-\lambda f(\mathbf{x}_0)}
$$

$$
\Gamma(s)\sim\sqrt{\dfrac{2\pi}{s}}\left(\dfrac{s}{e}\right)^s,\qquad s\to+\infty
$$

## 定理与证明

### 一维拉普拉斯首阶公式

设 $f\in C^2[a,b]$ 在 $(a,b)$ 内取唯一极小 $x_0$、$f''(x_0)>0$，$g$ 在 $x_0$ 连续且 $g(x_0)\ne0$。则当 $\lambda\to+\infty$ 时 $\int_a^b g\,e^{-\lambda f}\mathrm{d}x\sim g(x_0)e^{-\lambda f(x_0)}\sqrt{2\pi/(\lambda f''(x_0))}$。

**完整证明**

1. 取 $\epsilon>0$ 使 $[x_0-\epsilon,x_0+\epsilon]\subset(a,b)$ 且 $f''>0$ 于其上，把积分拆成邻域内、邻域外两部分。
   - *为什么*：邻域外 $f-f(x_0)\ge\delta>0$，那部分不超过 $Ce^{-\lambda(f(x_0)+\delta)}$，相对邻域内可忽略。
2. 在邻域内令 $x=x_0+y/\sqrt{\lambda}$，用 $f'(x_0)=0$ 展开 $f=f(x_0)+\frac{1}{2}f''(x_0)y^2/\lambda+O(y^3\lambda^{-3/2})$。
   - *为什么*：缩放后二次项与 $y$ 同量级，三次项在 $\lambda\to\infty$ 下消失。
3. 被积函数化为 $e^{-\lambda f(x_0)}\lambda^{-1/2}\int e^{-f''(x_0)y^2/2}\,[g(x_0)+o(1)]\,\mathrm{d}y$，积分限趋于 $\pm\infty$。
   - *为什么*：被积函数被 $e^{-cy^2}$ 控制，可用控制收敛定理把积分限取到全直线。
4. 用 $\int_{\mathbb{R}}e^{-ay^2/2}\mathrm{d}y=\sqrt{2\pi/a}$ 得 $\sqrt{2\pi/(\lambda f''(x_0))}\,g(x_0)e^{-\lambda f(x_0)}$。
   - *为什么*：这正是首阶；剩余误差为 $O(e^{-\lambda\delta})+O(\lambda^{-1/2})$，故比值趋于 $1$。

来源：ch02a.tex:889-950（原书 p.96–97）

### 多维拉普拉斯公式

设 $f$ 在区域内部有唯一极小 $\mathbf{x}_0$，$H_f(\mathbf{x}_0)$ 正定，则 $\int g(\mathbf{x})e^{-\lambda f(\mathbf{x})}\mathrm{d}^n\mathbf{x}\sim(2\pi/\lambda)^{n/2}g(\mathbf{x}_0)(\det H_f(\mathbf{x}_0))^{-1/2}e^{-\lambda f(\mathbf{x}_0)}$。

**完整证明**

1. 在极小点附近展开 $f(\mathbf{x})=f(\mathbf{x}_0)+\frac{1}{2}(\mathbf{x}-\mathbf{x}_0)^{\mathrm{t}}H_f(\mathbf{x}_0)(\mathbf{x}-\mathbf{x}_0)+O(|\mathbf{x}-\mathbf{x}_0|^3)$。
   - *为什么*：梯度在极小点为零，首个非零项由黑塞矩阵给出。
2. 作正交变换 $\mathbf{x}=\mathbf{x}_0+\lambda^{-1/2}Q\mathbf{y}$，使 $Q^{\mathrm{t}}H_fQ=\operatorname{diag}(h_1,\dots,h_n)$，则 $\mathrm{d}^n\mathbf{x}=\lambda^{-n/2}\mathrm{d}^n\mathbf{y}$。
   - *为什么*：正定性保证 $h_i>0$；正交变换不改变体积元。
3. 对每个 $y_i$ 作高斯积分，总因子 $\prod_i\sqrt{2\pi/h_i}=(2\pi)^{n/2}/\sqrt{\det H_f}$。
   - *为什么*：行列式等于特征值之积，故对角化后即得。

来源：ch02a.tex:995-1019（原书 p.98）

## 易错点

- 符号别写反：这里是 $e^{-\lambda f}$ 且 $f$ 取极小；若按极大展开会得到发散的 $e^{+\lambda f}$。
- 极小点必须唯一：两个指数相同的极小点要相加，否则漏掉一半贡献。
- 端点要分两种：若 $f'(a)\neq0$，边界层给 $g(a)e^{-\lambda f(a)}/(\lambda|f'(a)|)$（阶 $\lambda^{-1}$），不是高斯；只有驻点恰在端点（$f'(a)=0$）才取半条高斯、乘 $1/2$。
- $f''(x_0)=0$ 时公式失效：此时 $f-f(x_0)\sim c|x-x_0|^m$，首阶按 $\lambda^{-1/m}$ 定标。
- $g$ 在 $x_0$ 必须连续且不为零；$g(x_0)=0$ 会把首阶整体压低一阶。

## 相关卡

- [最速下降法](../concepts/steepest-descent.md)
- [Gamma 函数的拉普拉斯渐近](../examples/gamma-asymptotics.md)
- [有限维高斯积分](../concepts/gaussian-integral.md)

## 出处

- §2.5.1 拉普拉斯方法，p.96–98（PDF p.97–99），源码 `ch02a.tex:887-1020`
