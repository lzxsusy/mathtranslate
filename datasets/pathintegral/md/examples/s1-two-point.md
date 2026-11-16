# $S^1$ 上的两点关联

> `pi/example/s1-two-point` · 轨道 E · 微扰与代数结构 · 状态 draft

> **这张卡练什么**：两点关联展开后为什么只留下偶数阶项，$\hbar^2$ 修正的系数又为什么是 $\frac16$ 而不是 Moyal 乘积的 $\frac12$？

## 一句话

$m=1$ 的圆上关联：权函数换成 $g(\theta)=\theta-\frac12$ 后只剩 $D$ 的偶次幂，得 $\langle x\otimes p\rangle=xp$、$\langle x^2\otimes p^2\rangle=x^2p^2-\frac{\hbar^2}{6}$。

## 设定

取 $A=\mathbb{R}[x,p]$，$f_0,f_1\in A$。按定义 2.8.12（$m=1$）写圆上两点关联：$\langle f_0\otimes f_1\rangle_{S^1}=\int_{\mathrm{Cyc}_2(S^1)}\mathrm{d}\theta_0\mathrm{d}\theta_1\,f_0\,e^{\mathrm{i}\hbar g(\theta_1-\theta_0)D}f_1$，其中 $D=\overleftarrow{\partial}_x\overrightarrow{\partial}_p-\overleftarrow{\partial}_p\overrightarrow{\partial}_x$ 只作用在两个因子上。要用它算 $\langle x\otimes p\rangle_{S^1}$ 与 $\langle x^2\otimes p^2\rangle_{S^1}$。

## 计算

**第 1 步**：把定义里出现的两个格林函数合并：$G(\theta_0,\theta_1)=g(\theta_1-\theta_0)$、$G(\theta_1,\theta_0)=g(\theta_0-\theta_1)=-g(\theta_1-\theta_0)$（$g$ 是奇函数），故指数只剩 $\mathrm{i}\hbar g(\theta_1-\theta_0)D$；再令 $\theta=\theta_1-\theta_0$，$\mathrm{Cyc}_2$ 上的积分化为 $\int_0^1\mathrm{d}\theta$。

> 为什么：两点情形只有一对非零 $G$；用 $g$ 的奇性把它并成一个算符，是后面所有计算的出发点。

**第 2 步**：用命题 2.8.11：$0<\theta<1$ 时 $g(\theta)=\theta-\frac12$，换元 $u=\theta-\frac12$ 后 $\langle f_0\otimes f_1\rangle_{S^1}=\int_{-1/2}^{1/2}\mathrm{d}u\,f_0\,e^{\mathrm{i}\hbar uD}f_1$。

> 为什么：换元把权函数变成奇函数 $u$，这是「奇数阶项自动消失」的根源，也是结果里不出现 $\hbar$ 一次项的原因。

**第 3 步**：展开指数 $e^{\mathrm{i}\hbar uD}=\sum_k\frac{(\mathrm{i}\hbar u)^k}{k!}D^k$，并算 $\int_{-1/2}^{1/2}u^{2k}\mathrm{d}u=\frac{1}{(2k+1)2^{2k}}$；奇数 $k$ 因 $u$ 的奇性积分为零。

> 为什么：只要偶次项，才能把无穷级数压成 $D$ 的偶次幂级数，并且知道系数 $\frac{(\mathrm{i}\hbar)^{2k}}{(2k+1)2^{2k}(2k)!}$ 是怎么来的。

**第 4 步**：对 $f_0=x^2$、$f_1=p^2$ 算：$D(x^2\otimes p^2)=(\partial_x x^2)(\partial_p p^2)=4xp$，$D^2=4$，$D^3=0$；代入只留 $k=0,1$ 两项。

> 为什么：多项式次数有限，$D$ 每作用一次就提高一次导数阶，超过 $2$ 阶即消失，所以这个例子是有限的、可手工核对的。

**第 5 步**：求积：$x^2p^2+(\mathrm{i}\hbar)^2\frac{4}{2!}\int u^2\mathrm{d}u=x^2p^2-\frac{\hbar^2}{6}$（用 $\int u^2=\frac1{12}$）；对 $f_0=x$、$f_1=p$，$D(x\otimes p)=1$，更高阶为零，得 $xp$。

> 为什么：$(\mathrm{i}\hbar)^2=-\hbar^2$ 提供负号，$\frac{4}{2}\cdot\frac1{12}=\frac16$ 提供系数；逐项算可避免把 $\hbar^2$ 算重。

## 结果

$\langle x\otimes p\rangle_{S^1}=xp$，$\langle x^2\otimes p^2\rangle_{S^1}=x^2p^2-\frac{\hbar^2}{6}$；一般地 $\langle f_0\otimes f_1\rangle_{S^1}=\sum_{k\ge0}\frac{(\mathrm{i}\hbar)^{2k}}{(2k+1)2^{2k}(2k)!}f_0D^{2k}f_1$。

## 复核

① $\hbar\to0$ 时两式回到 $xp$、$x^2p^2$，与定义 2.8.12 的经典极限一致。② 只出现 $\hbar$ 的偶次幂，与权函数 $u$ 的奇性、$\theta\mapsto-\theta$ 的对称性相符。③ 与 Moyal 乘积对比：$x^2*p^2=x^2p^2+2\mathrm{i}\hbar xp-\frac{\hbar^2}{2}$，修正系数与 $\frac16$ 不同，说明圆上关联不是 Moyal 乘积的伪装，两者是不同的量子化。

## 易错点

- 换元后积区间是 $[-1/2,1/2]$，权函数是 $u$ 而不是 $\theta-\frac12$；忘记换元会以为奇次项有贡献。
- $(\mathrm{i}\hbar)^2$ 的负号来自 $i^2$，$\hbar^2/6$ 的负号就由这里产生；只写 $\hbar^2$ 会丢符号。
- 不能把 $\langle x^2\otimes p^2\rangle$ 当成 Moyal 乘积 $x^2*p^2$：系数 $\frac16\ne\frac12$，两者相差一个「循环序 vs 全对称」的效应。

## 用到哪些概念

- [$S^1$ 上的传播子与关联函数](../concepts/s1-correlators.md)

## 相关卡

- [$S^1$ 上的三点关联](../examples/s1-three-point.md)

## 出处

- §2.8.4 例 2.8.13（两点关联），p.155（PDF p.156），源码 `ch02c.tex:992-1023`
