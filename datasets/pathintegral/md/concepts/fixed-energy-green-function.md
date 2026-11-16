# 固定能量格林函数

> `pi/concept/fixed-energy-green-function` · 轨道 D · 格林函数与 WKB · 状态 draft

> **先自测**：固定能量格林函数为什么等于预解算子 $(E-\hat H+i\epsilon)^{-1}$ 的核，$+i\epsilon$ 在其中起什么作用？

## 一句话

把只向未来传播的费曼核对时间差作傅里叶变换，得到预解算子 $(E-\hat H+i\epsilon)^{-1}$ 的核；其极点给出束缚态能级，$+i\epsilon$ 既保证收敛又给出推迟性。

## 定义

设 $\hat H$ 不显含时间，$K$ 为费曼核，$\theta$ 为赫维赛德阶跃函数。把只在 $T\ge0$ 有支撑的核 $\theta(T)K(x'',T;x',0)$ 对时间差 $T$ 作傅里叶变换（变换变量取能量 $E$），所得函数记作 $G$：$$G(x'',x';E)=\frac{1}{i\hbar}\int_{-\infty}^{+\infty}\mathrm{d}T\,e^{i(E+i\epsilon)T/\hbar}\,\theta(T)K(x'',T;x',0).$$ 由于 $\theta$ 把积分截到 $T\ge0$，再把 $K$ 写成 $\langle x''|e^{-i\hat HT/\hbar}|x'\rangle$，指数上就只剩 $E+i\epsilon-\hat H$，于是 $G(x'',x';E)=\langle x''|(E-\hat H+i\epsilon)^{-1}|x'\rangle$。所以 $G$ 是算子 $E-\hat H$ 之逆在位置表象的积分核，即预解核；$\epsilon$ 是正的小量，最后取 $\epsilon\to0^+$。

**记号约定**：$x',x''\in\mathbb{R}$（一维；$\mathbb{R}^n$ 逐分量推广）；$T=t''-t'$ 为时间差；$\epsilon>0$ 且最终 $\epsilon\to0^+$；$\hat H$ 与时间无关；$\hbar$ 为约化普朗克常数。

## 要点

- $G$ 是预解算子 $(E-\hat H+i\epsilon)^{-1}$ 的积分核，因而满足 $(E-\hat H_{x''})G(x'',x';E)=\delta(x''-x')$。
- $\epsilon>0$ 有两个作用：让 $T$ 积分在上限收敛，并把极点推离实轴；$\epsilon\to0^+$ 选出推迟（因果）解。
- $G$ 在 $\operatorname{Im}E>0$ 内解析；离散谱在实轴上给出单极点，连续谱给出支割线。
- 对 $G$ 作逆傅里叶变换可以还原 $K$，所以固定能量与固定时间两种描述携带同样的信息。
- $\epsilon\to0^+$ 的极限用分布恒等式 $1/(x\pm i\epsilon)=\mp i\pi\delta(x)+\mathrm{P.V.}(1/x)$ 处理（注 2.7.1）。

## 关键公式

$$
G(x'',x';E)=\dfrac{1}{i\hbar}\displaystyle\int_0^{\infty}\mathrm{d}T\,e^{i(E+i\epsilon)T/\hbar}K(x'',T;x',0)
$$

$$
G(x'',x';E)=\langle x''|(E-\hat H+i\epsilon)^{-1}|x'\rangle
$$

$$
(E-\hat H_{x''})G(x'',x';E)=\delta(x''-x')
$$

$$
G(x'',x';E)=\sum_k\dfrac{\psi_k(x'')\psi_k^*(x')}{E-E_k}
$$

$$
K(x'',T;x',0)=\dfrac{i}{2\pi}\displaystyle\int_{\mathbb{R}}\mathrm{d}E\,e^{-iET/\hbar}G(x'',x';E)
$$

## 定理与证明

### 预解核满足的方程

设 $\epsilon>0$，$G$ 由定义给出，则 $(E-\hat H_{x''})G(x'',x';E)=\delta(x''-x')$；取 $\epsilon\to0^+$ 后作为分布仍成立。

**完整证明**

1. 把 $G$ 写成 $\frac{1}{i\hbar}\int_0^\infty\mathrm{d}T\,e^{i(E+i\epsilon)T/\hbar}e^{-i\hat HT/\hbar}$ 的矩阵元；$\epsilon>0$ 保证上限收敛，算子可移进积分号。
   - *为什么*：$e^{-\epsilon T/\hbar}$ 提供指数衰减，使交换极限合法。
2. 由 $\partial_T[e^{i(E+i\epsilon)T/\hbar}e^{-i\hat HT/\hbar}]=\frac{i}{\hbar}(E+i\epsilon-\hat H)e^{i(E+i\epsilon)T/\hbar}e^{-i\hat HT/\hbar}$，得 $(E+i\epsilon-\hat H)e^{\cdots}=\frac{\hbar}{i}\partial_T e^{\cdots}$。
   - *为什么*：对 $T$ 求导时 $E+i\epsilon-\hat H$ 是常算子，恒等式对每个矩阵元成立。
3. 代回得 $(E+i\epsilon-\hat H)G=\frac{1}{i\hbar}\frac{\hbar}{i}\int_0^\infty\partial_T e^{\cdots}\mathrm{d}T=-\left[e^{\cdots}\right]_0^\infty=1$。先得 $(E-\hat H+i\epsilon)G=1$，再取 $\epsilon\to0^+$，在分布意义下得 $(E-\hat H)G=1$，位置矩阵元即 $\delta(x''-x')$。
   - *为什么*：上限由 $e^{-\epsilon T/\hbar}\to0$ 消失，下限给 $-1$；$\epsilon\to0^+$ 的极限给出推迟格林函数。

来源：ch02b.tex:576-618（原书 p.117–118）

### 离散谱的谱表示

若 $\hat H$ 的谱是离散集 $\{E_k\}$、本征态 $\{\psi_k\}$ 正交归一，则 $G(x'',x';E)=\sum_k\psi_k(x'')\psi_k^*(x')/(E-E_k)$；连续谱时求和换成 $\int\mathrm{d}p/(2\pi\hbar)$ 的积分。

**完整证明**

1. 在 $\langle x''|(E-\hat H+i\epsilon)^{-1}|x'\rangle$ 中插入完备性 $\sum_k|\psi_k\rangle\langle\psi_k|=1$。
   - *为什么*：本征态张成整个希尔伯特空间，插入单位算符不改变矩阵元。
2. 由 $\hat H|\psi_k\rangle=E_k|\psi_k\rangle$ 得 $(E-\hat H+i\epsilon)^{-1}|\psi_k\rangle=(E-E_k+i\epsilon)^{-1}|\psi_k\rangle$，再取 $\epsilon\to0^+$ 即得求和式。
   - *为什么*：本征态上算子只剩数乘，分母的极点位置直接读出能级；这一点是后面用极点找谱的依据。

来源：ch02b.tex:619-628（原书 p.118）

## 易错点

- $+i\epsilon$ 与 $-i\epsilon$ 给出不同的边条件：前者是推迟核，后者是超前核，不能随意互换。
- 把 $1/(E-E_k)$ 在 $E=E_k$ 处当普通数值代入；那里是极点，必须按分布（或保留 $i\epsilon$）理解。
- 只看极点会漏掉连续谱：散射态不产生极点而产生支割线。
- 逆变换里漏掉 $i/(2\pi)$ 因子或把 $e^{-iET/\hbar}$ 的符号写反，会让 $K$ 与 $G$ 不再互为傅里叶对。
- 忘记 $\theta(T)$：没有它，全实轴上的变换对应的是另一种边条件，不再是推迟核。

## 相关卡

- [费曼核与传播子](../concepts/feynman-kernel.md)
- [半经典格林函数](../concepts/semiclassical-green-function.md)
- [自由粒子的固定能量格林函数](../examples/free-green-function.md)

## 出处

- §2.7.1 固定能量下的格林函数，p.117–121（PDF p.118–122），源码 `ch02b.tex:569-808`
