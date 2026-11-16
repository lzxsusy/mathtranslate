# 谐振子配分函数

> `pi/concept/harmonic-oscillator-partition` · 轨道 B · 高斯路径积分与谐振子 · 状态 draft

> **先自测**：怎样不经过能谱、只靠路径积分得到谐振子的配分函数？

## 一句话

对谐振子传播子取迹并延拓到虚时间，算出 $\operatorname{Tr}e^{-\beta\hat H}=1/(2\sinh(\beta\hbar\omega/2))$，与能谱直接求和一致，从而独立检验了 zeta 正则化与归一化常数。

## 定义

配分函数 $Z(\beta)=\operatorname{Tr}e^{-\beta\hat H}$ 汇总了全部能级。除了按 $E_n$ 求和，还可以取传播子的对角元并对位置积分：$Z=\int\mathrm{d}x\,K(x,-i\beta\hbar;x,0)$，也就是在虚时间 $\beta\hbar$ 上走一条闭合路径。谐振子的 $K$ 在虚时间下变成实指数高斯，积分给出 $1/(2\sinh(\beta\hbar\omega/2))$。

**记号约定**：$\beta=1/(k_BT)$ 为逆温度；$\omega$ 为角频率；$\tau$ 为虚时间；$K_E$ 为欧氏核。

## 要点

- 取迹即在位置表象取对角元再积分，等价于让路径在虚时间里闭合。
- 替换 $T=-i\beta\hbar$ 把 $\sin\omega T$ 变为 $-i\sinh(\beta\hbar\omega)$，振荡的核变成衰减的高斯。
- 指数系数 $\frac{2\sinh^2(\theta/2)}{\sinh\theta}$（$\theta=\beta\hbar\omega$）可化简为 $\tanh(\theta/2)$。
- 高斯积分后预因子与指数系数相消，只剩 $1/(2\sinh(\theta/2))$。
- 两条算法给出同一结果，说明 zeta 正则化的 $\det A$ 与归一化常数 $N$ 都取对了。

## 关键公式

$$
\operatorname{Tr}e^{-\beta\hat H}=\sum_{n=0}^{\infty}e^{-\beta E_n}=\frac{e^{-\frac12\beta\hbar\omega}}{1-e^{-\beta\hbar\omega}}=\frac{1}{2\sinh(\beta\hbar\omega/2)}
$$

$$
K_E(x'',\tau;x',0)=K(x'',-i\tau;x',0)=\langle x''|e^{-\hat H\tau/\hbar}|x'\rangle
$$

$$
\operatorname{Tr}e^{-\beta\hat H}=\int_{\mathbb{R}}\mathrm{d}x\,K(x,-i\beta\hbar;x,0)
$$

$$
K(x,-i\beta\hbar;x,0)=\left(\frac{m\omega}{2\pi\hbar\sinh(\beta\hbar\omega)}\right)^{1/2}\exp\left\{-\frac{m\omega}{\hbar}\tanh\left(\frac{\beta\hbar\omega}{2}\right)x^2\right\}
$$

$$
\operatorname{Tr}e^{-\beta\hat H}=\left(\frac{m\omega}{2\pi\hbar\sinh(\beta\hbar\omega)}\cdot\frac{\pi\hbar\sinh(\beta\hbar\omega)}{2m\omega\sinh^2(\beta\hbar\omega/2)}\right)^{1/2}=\frac{1}{2\sinh(\beta\hbar\omega/2)}
$$

## 定理与证明

### 配分函数的两种算法一致

$\operatorname{Tr}e^{-\beta\hat H}=\frac{1}{2\sinh(\beta\hbar\omega/2)}$ 既可由能谱求和得到，也可由虚时间核的对角积分得到。

**完整证明**

1. 用能谱 $E_n=\left(n+\frac12\right)\hbar\omega$ 求和：$\sum_ne^{-\beta E_n}=\frac{e^{-\beta\hbar\omega/2}}{1-e^{-\beta\hbar\omega}}$。
   - *为什么*：能级等间距，级数是公比 $e^{-\beta\hbar\omega}<1$ 的等比级数。
2. 把迹写成 $\int\mathrm{d}x\,\langle x|e^{-\beta\hat H}|x\rangle=\int\mathrm{d}x\,K_E(x,\beta\hbar;x,0)$。
   - *为什么*：位置本征态构成完备基，迹等于对角矩阵元对连续指标积分。
3. 作虚时间延拓 $T=-i\beta\hbar$，用 $\sin(-i\theta)=-i\sinh\theta$、$\cot(-i\theta)=i\coth\theta$ 化简 Mehler 核。
   - *为什么*：解析延拓把振荡因子变成双曲函数，指数由纯虚变为负实，积分才收敛。
4. 指数化为 $-\frac{m\omega}{\hbar}\tanh\left(\frac{\beta\hbar\omega}{2}\right)x^2$，对 $x$ 作高斯积分。
   - *为什么*：系数为正，高斯积分 $\int e^{-ax^2}\mathrm{d}x=\sqrt{\pi/a}$ 收敛，且与预因子的 $m\omega$ 部分相消。
5. 比较两式，结果同为 $1/(2\sinh(\beta\hbar\omega/2))$。
   - *为什么*：两条推导互不依赖（一条只用能谱，一条只用路径积分），一致即说明正则化方案与归一化自洽。

来源：ch02a.tex:837-878（原书 p.95）

### 欧氏核与热核的等价

对 $\tau>0$，$K_E(x'',\tau;x',0)=K(x'',-i\tau;x',0)=\langle x''|e^{-\hat H\tau/\hbar}|x'\rangle$。

**证明提纲**

1. 把 $T=-i\tau$ 代入 $K(x'',T;x',0)=\langle x''|e^{-i\hat HT/\hbar}|x'\rangle$。
   - *为什么*：实时传播子对复 $T$ 按解析延拓理解，指数中 $i\cdot(-i\tau)=\tau$ 变为实数。
2. 得 $\langle x''|e^{-\hat H\tau/\hbar}|x'\rangle$，取 $\tau=\beta\hbar$ 即玻尔兹曼因子在位置表象的矩阵元。
   - *为什么*：$\hat H$ 有下界时 $e^{-\hat H\tau/\hbar}$ 对 $\tau>0$ 是迹类算子，矩阵元有定义。

> **缺口**：书中直接把该等式当定义写出，没有证明实时路径积分在 $T=-i\tau$ 处的解析延拓确实等于 $\langle x''|e^{-\hat H\tau/\hbar}|x'\rangle$（需要 $\operatorname{Re}\tau>0$ 与谱条件保证收敛），这一块未展开。


来源：ch02a.tex:851-866（原书 p.95）

## 易错点

- 迹是对角元对 $x$ 的一重积分，不是对 $x'$、$x''$ 的二重积分。
- 虚时间延拓时 $\sin(-i\theta)=-i\sinh\theta$、$\cot(-i\theta)=i\coth\theta$，$i$ 因子与符号都要跟。
- 谱求和不能漏零点能 $\frac12\hbar\omega$，否则结果差一个 $e^{\beta\hbar\omega/2}$ 的因子。
- $\beta\hbar\omega$ 无量纲；漏写 $\hbar$ 会让 $\sinh$ 的自变量带量纲。
- 指数里的 $\frac{2\sinh^2(\theta/2)}{\sinh\theta}$ 应先化简为 $\tanh(\theta/2)$ 再积分，否则容易把预因子算错。

## 相关卡

- [谐振子传播子（Mehler 核）](../concepts/harmonic-oscillator-propagator.md)
- [虚时间与欧氏路径积分](../concepts/imaginary-time.md)
- [zeta 函数正则化与泛函行列式](../concepts/zeta-regularization.md)

## 出处

- §2.4.2 配分函数，p.95（PDF p.96），源码 `ch02a.tex:835-881`
