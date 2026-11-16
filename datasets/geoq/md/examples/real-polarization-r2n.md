# $\mathbb{R}^{2n}$ 的实极化与位置波函数

> `geoq/example/real-polarization-r2n` · 轨道 D · 几何量子化机器 · 状态 draft

> **这张卡练什么**：预量子化空间本来是流形上所有平方可积函数，极化条件怎样把它削减成位置波函数？

## 一句话

取动量方向的实拉格朗日极化后，协变常值截面恰为只依赖位置的函数，预量子化空间由此化为位置波函数。

## 设定

取 $M=\mathbb{R}^{2n}$，坐标 $(x^1,\dots,x^n,p_1,\dots,p_n)$，辛形式 $\omega=\sum_i dp_i\wedge dx^i$，刘维尔形式 $\theta=\sum_i p_i\,dx^i$。平凡线丛 $L=M\times\mathbb{C}$ 上取联络 $\nabla=d-\frac{i}{\hbar}\theta$，内积 $\langle f,g\rangle=\bar fg$。考虑常值分布 $P=\operatorname{Span}\{\partial_{p_1},\dots,\partial_{p_n}\}$。

## 计算

**第 1 步**：验证 $P$ 是实拉格朗日极化：它由常向量场张成，秩恒为 $n$，故对合；又 $\omega(\partial_{p_i},\partial_{p_j})=0$，因为 $\omega=\sum_i dp_i\wedge dx^i$ 的每一项都含一个 $dx$，对两个动量方向缩并为零。

> 为什么：极化要求 $P$ 极大迷向且对合；$\dim P=n=\frac12\dim M$ 加上迷向即极大。

**第 2 步**：写出极化条件 $\nabla_vf=0$（$v\in P$）。由于 $\theta(\partial_{p_i})=\sum_j p_j\,dx^j(\partial_{p_i})=0$，有 $\nabla_{\partial_{p_i}}f=\partial_{p_i}f$，条件就是 $\partial_{p_i}f=0$。

> 为什么：$\nabla_vf=v(f)-\frac{i}{\hbar}\theta(v)f$，而 $\theta$ 只含 $dx$ 分量，吃掉动量方向。

**第 3 步**：解方程：每个 $\partial_{p_i}f$ 为零，故 $f$ 与动量无关，$f=f(x^1,\dots,x^n)$。这正是位置表象的波函数。

> 为什么：沿每个动量方向的偏导为零，说明函数在纤维上是常值。

**第 4 步**：换成横向极化 $P'=\operatorname{Span}\{\partial_{x^1},\dots,\partial_{x^n}\}$。此时 $\theta(\partial_{x^i})=p_i$，条件变为 $\partial_{x^i}f=\frac{i}{\hbar}p_if$，解得 $f=e^{\frac{i}{\hbar}\sum_i x^ip_i}\,g(p)$。

> 为什么：逐个坐标积分，动量作为常数时指数因子给出平面波。

## 结果

动量方向的实极化给出位置波函数 $f=f(\mathbf{x})$；位置方向的实极化给出 $f=e^{\frac{i}{\hbar}\mathbf{x}\cdot\mathbf{p}}g(\mathbf{p})$。两者是同一预量子化线丛的两种表象。

## 复核

(i) 代回：$f(\mathbf{x})=e^{-\mathbf{x}^2}$ 满足 $\partial_{p_i}f=0$，确是 $P$-极化截面。(ii) 特例 $n=1$：$f=e^{\frac{i}{\hbar}xp}g(p)$ 满足 $\partial_xf=\frac{i}{\hbar}pf$ ✓。(iii) 结构核对：$P\cap P'=\{0\}$ 且两者维数相加为 $2n$，切空间分解为直和，这正是位置表象与动量表象互为傅里叶变换的几何来源。

## 易错点

- 朴素公式 $Q(f)=i\hbar\nabla_{X_f}+f$ 并非对每个 $f$ 都保持极化：$f=p_i$ 可以，因为 $V_{p_i}=-\partial_{x^i}$ 与 $P$ 交换；但 $f=p_i^2$ 不行——$V_{p_i^2}=-2p_i\partial_{x^i}$，它与 $\partial_{p_k}$ 的括号为 $-2\delta_{ik}\partial_{x^i}$，已经跑出 $P$。所以 $C^\infty_P$ 含全部 $p$ 的一次项，却不含 $p$ 的二次项。
- 范数 $\int|f|^2\,dx\,dp$ 沿动量方向发散：极化截面与 $p$ 无关，被积函数在纤维上为常值。真正的希尔伯特空间需要半形式修正（取 $\omega^n$ 的一半），这是后续的内容。
- 极化不是子流形：它定义为切丛的拉格朗日子丛，$P$ 的积分流形才是子流形；把两者混为一谈会错误地以为「极化截面 = 子流形上的函数」。

## 用到哪些概念

- [极化：实极化与凯勒极化](../concepts/polarization.md)
- [预量子化线丛](../concepts/prequantization.md)

## 相关卡

- [$\mathbb{C}^n$ 的凯勒极化与全纯截面](../examples/kahler-polarization-cn.md)
- [余切丛的典范辛结构与刘维尔形式](../concepts/cotangent-bundle.md)

## 出处

- §5.4.4 例 5.4.8，p.289（PDF p.290），源码 `ch05b.tex:1077-1124`
