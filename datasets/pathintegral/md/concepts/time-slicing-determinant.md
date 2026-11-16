# 时间切片方法的行列式极限

> `pi/concept/time-slicing-determinant` · 轨道 C · 渐近方法与半经典 · 状态 draft

> **先自测**：离散高斯积分的行列式如何在连续极限下重现半经典核的前因子？

## 一句话

把涨落积分切成 N 段，离散行列式满足三项递推；步长趋零时递推化为雅可比方程，$\varepsilon\det A_N$ 趋于 $\varphi_0$，独立验证半经典前因子。

## 定义

把时间区间 $[t',t'']$ 分成 $N$ 段，步长 $\varepsilon=(t''-t')/N$，在每段上把涨落作用量写成 $\frac{m}{2\varepsilon}(x_{j+1}-x_j)^2-\frac{m}{2}\varepsilon\omega_j^2x_j^2$。对 $x_1,\dots,x_{N-1}$ 作高斯积分，得离散前因子 $\left(m/(2\pi i\hbar\varepsilon\det A_N)\right)^{1/2}$，其中 $A_N$ 为三对角矩阵。定义 $u_j=\varepsilon\det A_j$ 后，$u_j$ 满足三项递推，$\varepsilon\to0$ 时化为 $u$ 的雅可比方程，初值 $u(t')=0$、$u'(t')=1$，故 $\varepsilon\det A_N\to\varphi_0(t'')$。

**记号约定**：$\varepsilon=(t''-t')/N$；$\omega_j^2=V''(x_{cl}(t_j))/m$；$A_N$ 为 $(N-1)\times(N-1)$ 三对角矩阵；$u_j=\varepsilon\det A_j$。

## 要点

- 时间切片把路径积分化为 $N-1$ 重高斯积分，离散化只保留到 $V''(x_{cl})$ 的二阶项。
- 离散矩阵 $A_N$ 是三对角的：对角元 $2-\varepsilon^2\omega_j^2$，非对角元 $-1$。
- $u_j=\varepsilon\det A_j$ 的三项递推在 $\varepsilon\to0$ 时成为 $\ddot u+\omega^2u=0$。
- 初值 $u_0=\varepsilon$、$(u_1-u_0)/\varepsilon=1-\varepsilon^2\omega_1^2$ 化为 $u(t')=0$、$u'(t')=1$。
- 极限给出 $\varepsilon\det A_N\to\varphi_0(t'')$，与 §2.6.1 的 $\det A=2\varphi_0$ 及前因子一致，构成独立验证。

## 关键公式

$$
A_N=\operatorname{tridiag}\left(-1,\ 2-\varepsilon^2\omega_j^2,\ -1\right)
$$

$$
\frac{u_{j+1}-2u_j+u_{j-1}}{\varepsilon^2}+\omega_{j+1}^2u_j=0
$$

$$
\ddot u+\omega^2(t)u=0,\qquad u(t')=0,\quad u'(t')=1
$$

$$
\lim_{\varepsilon\to0}\varepsilon\det A_N=u(t'')=\varphi_0(t'')
$$

$$
K_{sc}=\lim_{\varepsilon\to0}\left(\frac{m}{2\pi i\hbar\,\varepsilon\det A_N}\right)^{1/2}e^{\frac{i}{\hbar}S_{cl}}
$$

## 定理与证明

### 离散行列式的连续极限

记 $A_j$ 为取前 $j$ 个格点的三对角行列式，$u_j=\varepsilon\det A_j$。则 $u_j$ 满足三项递推，$\varepsilon\to0$ 时 $u$ 满足 $\ddot u+\omega^2(t)u=0$、$u(t')=0$、$u'(t')=1$；因此 $\lim_{\varepsilon\to0}\varepsilon\det A_N=\varphi_0(t'')$。

**完整证明**

1. 把 $N$ 段时间切片上的涨落积分写成 $\left(\frac{m}{2\pi i\hbar\varepsilon}\right)^{N/2}\int\prod_{j=1}^{N-1}dx_j\,e^{\frac{im}{2\hbar\varepsilon}\mathbf{x}^tA_N\mathbf{x}}$。
   - *为什么*：每段的动能项给出相邻差，势能项给出 $\varepsilon^2\omega_j^2$ 的对角修正。
2. 完成 $N-1$ 重高斯积分，得 $\left(\frac{m}{2\pi i\hbar\varepsilon\det A_N}\right)^{1/2}$。
   - *为什么*：高斯积分产生 $(2\pi i\hbar\varepsilon/m)^{(N-1)/2}(\det A_N)^{-1/2}$，与前面的归一化相乘正好剩一个 $\varepsilon$。
3. 把 $\det A_j$ 按最后一行展开，得 $D_j=(2-\varepsilon^2\omega_j^2)D_{j-1}-D_{j-2}$，即 $u_j=(2-\varepsilon^2\omega_j^2)u_{j-1}-u_{j-2}$。
   - *为什么*：三对角行列式的标准展开；乘以 $\varepsilon$ 后递推式两边量纲一致。
4. 整理为 $\frac{u_{j+1}-2u_j+u_{j-1}}{\varepsilon^2}+\omega_{j+1}^2u_j=0$，令 $\varepsilon\to0$ 得 $\ddot u+\omega^2(t)u=0$。
   - *为什么*：二阶中心差商在步长趋零时趋于二阶导数。
5. 初值 $u_0=\varepsilon$、$(u_1-u_0)/\varepsilon=1-\varepsilon^2\omega_1^2$ 在极限下给出 $u(t')=0$、$u'(t')=1$；与 $\varphi_0$ 的初值问题相同，故 $u=\varphi_0$，$\varepsilon\det A_N\to\varphi_0(t'')$。
   - *为什么*：二阶线性常微分方程初值问题的解唯一。

来源：ch02b.tex:489-563（原书 p.116–117）

### 与半经典前因子的一致性

时间切片极限给出 $K_{sc}=\left(\frac{m}{2\pi i\hbar\varphi_0(t'')}\right)^{1/2}e^{\frac{i}{\hbar}S_{cl}}$，与 §2.6.1 由 $\det A=2\varphi_0$ 得到的前因子相同。

**完整证明**

1. 离散高斯积分的结果是 $\left(\frac{m}{2\pi i\hbar\varepsilon\det A_N}\right)^{1/2}e^{\frac{i}{\hbar}S_{cl}}$。
   - *为什么*：涨落只进入前因子，经典作用量作为整体相位提出。
2. 取 $\varepsilon\to0$，用 $\varepsilon\det A_N\to\varphi_0(t'')$ 得 $\left(\frac{m}{2\pi i\hbar\varphi_0(t'')}\right)^{1/2}e^{\frac{i}{\hbar}S_{cl}}$。
   - *为什么*：极限与平方根连续，$\varphi_0\ne0$ 时可直接代入。
3. §2.6.1 的 $\det A=2\varphi_0(t'')$ 把 $\left(\frac{m}{\pi i\hbar\det A}\right)^{1/2}$ 化为同一个式子，两种算法一致。
   - *为什么*：$\det A=2\varphi_0$ 使分母的 $\pi i\hbar\det A$ 变为 $2\pi i\hbar\varphi_0$。

来源：ch02b.tex:466-566（原书 p.115–117）

## 易错点

- $\varepsilon\det A_N$ 的极限是 $\varphi_0$，不是 $\det A$；连续行列式还要乘 2（$\det A=2\varphi_0$），指数里的 2 不能丢。
- $A_N$ 的对角元含 $\varepsilon^2\omega^2$；在取极限前不能先把这一项丢掉，否则递推退化为自由情形。
- 高斯归一化 $\left(m/(2\pi i\hbar\varepsilon)\right)^{N/2}$ 与 $N-1$ 个积分给出 $\varepsilon$ 的幂次，数错会差一个 $\sqrt\varepsilon$。
- 时间切片只对二次（高斯）涨落精确；高阶项在 $\varepsilon\to0$ 时不影响首阶，但有限步长时有修正。

## 相关卡

- [半经典费曼核](../concepts/semiclassical-kernel.md)
- [雅可比场与 Van Vleck 行列式](../concepts/jacobi-field-van-vleck.md)
- [zeta 函数正则化与泛函行列式](../concepts/zeta-regularization.md)
- [有限维高斯积分](../concepts/gaussian-integral.md)

## 出处

- §2.6.3 时间切片方法，p.115–117（PDF p.116–118），源码 `ch02b.tex:466-566`
