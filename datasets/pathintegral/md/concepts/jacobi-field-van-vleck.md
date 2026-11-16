# 雅可比场与 Van Vleck 行列式

> `pi/concept/jacobi-field-van-vleck` · 轨道 C · 渐近方法与半经典 · 状态 draft

> **先自测**：半经典核的前因子为什么能写成经典作用量的二阶导数，焦散处又发生了什么？

## 一句话

经典轨迹族对初速度的变分给出雅可比场；它与基本解 $\varphi_0$ 相同，使 $\det A=2\varphi_0$，并把前因子写成作用量二阶导的平方根。共轭点处前因子发散。

## 定义

固定起点 $(x',t')$，用初速度 $v'$ 标记一族经典轨迹 $x_{cl}(t;v')$。变分 $J(t;v')=\partial x_{cl}(t;v')/\partial v'$ 称为雅可比场（Jacobi field），满足雅可比方程 $m\ddot J+V''(x_{cl})J=0$ 与初值 $J(t')=0,\ \dot J(t')=1$。§2.6.1 中的 $\varphi_0$ 正是 $J$。若 $J(t'';v')=0$，则 $t''$ 称为共轭点（conjugate point）：整族轨迹从同一点出发又在同一点汇聚，对应的焦散（caustic）使半经典前因子发散。

**记号约定**：$x_{cl}(t;v')$ 为以 $v'$ 标记的经典轨迹；$J$ 为沿轨迹的变分场；$S_{cl}(x'',t'';x',t')$ 为端点间的经典作用量；$A=-\frac{d^2}{dt^2}-\frac1m V''(x_{cl})$。

## 要点

- 雅可比场描述邻近经典轨道的一阶偏离，是把 $x_{cl}$ 对初速度求导得到的。
- 对运动方程求导即得雅可比方程；初值由 $x_{cl}(t')=x'$、$\dot x_{cl}(t')=v'$ 给出。
- 雅可比场与涨落算子的基本解满足同一个初值问题，故 $\varphi_0=J$。
- 由哈密顿–雅可比关系可证 $\partial^2S_{cl}/\partial x'\partial x''=-m/J(t'')$，前因子因此只含作用量的二阶导。
- 共轭点 $J(t'')=0$ 对应焦散：一族轨迹汇聚，前因子发散，需要 Maslov 相位或一致渐近。

## 关键公式

$$
J(t;v')=\frac{\partial x_{cl}(t;v')}{\partial v'}
$$

$$
m\ddot J+V''(x_{cl})J=0,\qquad J(t')=0,\quad \dot J(t')=1
$$

$$
\frac{\partial^2 S_{cl}}{\partial x'\partial x''}=-\frac{m}{J(t'')}
$$

$$
K_{sc}=\sum_{x_{cl}}\left(\frac{i}{2\pi\hbar}\frac{\partial^2 S_{cl}}{\partial x'\partial x''}\right)^{1/2}e^{\frac{i}{\hbar}S_{cl}}
$$

$$
\det A=2\varphi_0(t'')=2J(t'')
$$

## 定理与证明

### 雅可比场就是涨落算子的基本解

设 $x_{cl}(t;v')$ 满足 $m\ddot x_{cl}+V'(x_{cl})=0$、$x_{cl}(t')=x'$、$\dot x_{cl}(t')=v'$，并令 $J=\partial x_{cl}/\partial v'$。则 $J$ 满足 $m\ddot J+V''(x_{cl})J=0$、$J(t')=0$、$\dot J(t')=1$，从而 $J=\varphi_0$。

**完整证明**

1. 把 $m\ddot x_{cl}+V'(x_{cl})=0$ 对 $v'$ 求导，得 $m\ddot J+V''(x_{cl})J=0$。
   - *为什么*：链式法则；$x_{cl}$ 对 $v'$ 的导数正是 $J$。
2. 对初值 $x_{cl}(t';v')=x'$ 求导得 $J(t')=0$；对 $\dot x_{cl}(t';v')=v'$ 求导得 $\dot J(t')=1$。
   - *为什么*：起点 $x'$ 固定，不随 $v'$ 改变。
3. 二阶线性常微分方程初值问题的解唯一，而 $\varphi_0$ 满足同一方程与初值，故 $J=\varphi_0$。
   - *为什么*：解的唯一性把两个满足相同初值的解等同起来。

来源：ch02b.tex:298-349（原书 p.112–113）

### Van Vleck–Pauli–Morette 公式

设 $S_{cl}(x'',t'';x',t')$ 为经典作用量，$J(t'')=\partial x_{cl}(t'')/\partial v'$。则 $\partial^2S_{cl}/\partial x'\partial x''=-m/J(t'')$，从而 $K_{sc}=\sum_{x_{cl}}\left(\frac{i}{2\pi\hbar}\frac{\partial^2S_{cl}}{\partial x'\partial x''}\right)^{1/2}e^{\frac{i}{\hbar}S_{cl}}$。

**完整证明**

1. 由哈密顿–雅可比关系，$\partial S_{cl}/\partial x''=p(t'')$，$\partial S_{cl}/\partial x'=-p(t')=-mv'$。
   - *为什么*：作用量对端点位置的偏导等于端点动量，这是经典力学的标准结果。
2. 于是 $\partial^2S_{cl}/\partial x'\partial x''=-\partial p(t')/\partial x''=-m\,\partial v'/\partial x''$。
   - *为什么*：先对 $x'$ 求导再对 $x''$ 求导，偏导可交换次序。
3. 端点条件 $x_{cl}(t'';v')=x''$ 给出 $\partial x''/\partial v'=J(t'')$，故 $\partial v'/\partial x''=1/J(t'')$。
   - *为什么*：反函数定理；要求 $J(t'')\ne0$，否则正处共轭点。
4. 代入前因子得 $\left(\frac{m}{2\pi i\hbar\varphi_0}\right)^{1/2}=\left(\frac{i}{2\pi\hbar}\frac{\partial^2S_{cl}}{\partial x'\partial x''}\right)^{1/2}$。
   - *为什么*：用 $\varphi_0=J$ 与 $1/J=-(1/m)\partial^2S_{cl}/\partial x'\partial x''$ 消去 $J$。
5. 对连接同一对端点的所有经典轨道求和，即得 Van Vleck–Pauli–Morette 公式。
   - *为什么*：每条轨道的贡献来自各自的驻点，线性叠加即得总首阶。

来源：ch02b.tex:361-398（原书 p.114）

### Coleman 的行列式公式

记 $\Theta=V''(x_{cl})/m$，$A=-\frac{d^2}{dt^2}-\Theta(t)$。则 $\det A=2\varphi_0(t'')$，其中 $\varphi_0$ 满足 $A\varphi_0=0$、$\varphi_0(t')=0$、$\varphi_0'(t')=1$。

**证明提纲**

1. 对每个 $\lambda$，初值问题 $A\varphi_\lambda=\lambda\varphi_\lambda$、$\varphi_\lambda(t')=0$、$\varphi_\lambda'(t')=1$ 有唯一解；$\varphi_\lambda(t'')=0$ 当且仅当 $\lambda$ 是 $A$ 的狄利克雷本征值。
   - *为什么*：把边值问题写成初值问题的解在右端点取零的条件。
2. 取辅助算子 $\tilde A=-\frac{d^2}{dt^2}-\tilde\Theta$，则 $f(\lambda)=\det(A-\lambda)/\det(\tilde A-\lambda)$ 与 $g(\lambda)=\varphi_\lambda(t'')/\tilde\varphi_\lambda(t'')$ 的零点、极点相同，故 $f/g$ 为整函数。
   - *为什么*：两边都在 $A$ 的本征值处为零、在 $\tilde A$ 的本征值处为极点；书中说明这些零点与极点均为单重。
3. 当 $\lambda\to\infty$ 且 $\lambda\notin\mathbb{R}_+$ 时，$\Theta$ 相对 $-\frac{d^2}{dt^2}-\lambda$ 是小扰动，$f\to1$；格林算子估计给出修正 $u=O(\Theta/\sqrt\lambda)\varphi^{(0)}$，故 $g\to1$。
   - *为什么*：大 $|\lambda|$ 时势项可忽略，两个行列式之比与两个解之比都趋于自由情形的 1。
4. 整函数 $f/g$ 在无穷远趋于 1，故 $f/g\equiv1$，即 $\det(A-\lambda)/\varphi_\lambda(t'')=\det(\tilde A-\lambda)/\tilde\varphi_\lambda(t'')$。
   - *为什么*：有界整函数为常数，而无穷远处的极限把这个常数定为 1。
5. 令 $\lambda=0$：$\det A/\varphi_0(t'')=\det\tilde A/\tilde\varphi_0(t'')$；自由情形 $\det\tilde A=2T$、$\tilde\varphi_0=T$，故 $\det A=2\varphi_0(t'')$。
   - *为什么*：常数与势无关，可用自由情形定出因子 2。

> **缺口**：书中自称这是「直观计算」：零点与极点的单重性、谱行列式的解析性，以及 $f\to1$、$g\to1$ 的一致渐近都只作定性说明，未给严格证明。


来源：ch02b.tex:89-296（原书 p.109–112）

## 易错点

- 雅可比场是对初速度的变分，不是路径涨落 $\gamma$；两者满足同一方程，但边界条件不同（$J$ 的左端导数为 1，$\gamma$ 两端为零）。
- $\det A=2\varphi_0$ 中的因子 2 来自自由情形 $\det(-d^2/dt^2)=2T$；换归一化就会变，不能漏。
- 共轭点处 $J=0$ 只让前因子发散，核本身未必发散；焦散附近要用一致渐近。
- 多轨迹求和时每条有自己的 $J$ 与 Maslov 指标，不能共用一个前因子。
- 书中 Coleman 计算是直观推导，零点极点的单重性是断言；引用时要说明这一点。

## 相关卡

- [半经典费曼核](../concepts/semiclassical-kernel.md)
- [时间切片方法的行列式极限](../concepts/time-slicing-determinant.md)
- [谐振子传播子（Mehler 核）](../concepts/harmonic-oscillator-propagator.md)
- [谐振子的半经典核](../examples/harmonic-oscillator-semiclassical.md)

## 出处

- §2.6.1 半经典的费曼核、§2.6.2 雅可比场，p.109–115（PDF p.110–116），源码 `ch02b.tex:89-465`
