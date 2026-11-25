# 椭圆曲线上的指标计算

> `grassmann/example/elliptic-curve-regularity` · 轨道 8 · 阿贝尔簇上的正则性 · 状态 draft

> **这张卡练什么**：为什么椭圆曲线上 $m(n\Theta)=n-1$ 这条整齐公式，在高亏格阿贝尔簇上会变得完全误导？

## 一句话

在椭圆曲线上把每个 $V^i$ 直接手算出来：$L$ 是 $M$-正则的恰好当 $\deg L\ge1$，此时逐点的 $p(L)$ 与整体的 $m(L)$ 都等于 $d-1$，于是 $m(n\Theta)=n-1$；高亏格下这个线性行为会失效。

## 背景定义

本例要计算的量是定义 7.1 的指标：$m(L)=\max\{l\mid L\otimes\mathfrak m_{x_1}^{k_1}\otimes\cdots\otimes\mathfrak m_{x_p}^{k_p}$ 对一切互异 $x_i$ 与 $\sum k_i=l$ 都 $M$-正则$\}$。在 $g=1$ 时它化简为『$L$ 沿单点被扭的最大阶数』，因为总次数 $\sum k_i$ 完全决定 $\deg(L(-\sum k_ix_i))=d-\sum k_i$。

## 设定

取椭圆曲线 $E$（$g=1$），$\Theta$ 是主极化点，$\operatorname{Pic}^0(E)\cong E$。设 $L$ 是次数 $d=\deg L$ 的线丛，$x\in E$，$\mathfrak m_x$ 为其极大理想。因为 $i>0$ 只有 $i=1$，定义 2.7 的判据退化成一句：是否 $\dim V^1(L\otimes\mathfrak m_x^k)\le g-1-1=-1$，即 $V^1$ 是否为空。目标是算出 $m(L)$。

## 计算

对 $k\ge0$ 有 $\deg(L(-kx))=d-k$。若 $k\le d-1$，则 $\deg(L(-kx))>0$，由 Serre 对偶与负次数层无截面得 $h^1(L(-kx)\otimes\alpha)=h^0\bigl((L(-kx)\otimes\alpha)^{-1}\bigr)=0$ 对一切 $\alpha\in\operatorname{Pic}^0(E)$，故 $V^1=\varnothing$，$L\otimes\mathfrak m_x^k$ 是 $M$-正则的。若 $k=d$，则 $\deg(L(-kx))=0$，存在唯一 $\alpha_0$ 使 $L(-kx)\otimes\alpha_0\cong\mathcal O_E$，此时 $h^1=1$，$V^1=\{\alpha_0\}$ 是单点，$\dim V^1=0>-1$，故 $L\otimes\mathfrak m_x^d$ 不是 $M$-正则的。于是 $m(L)=p(L)=d-1$；取 $L=n\Theta$（$\deg=n$）得 $m(n\Theta)=n-1$，再由定理 7.4 得 $\varepsilon(n\Theta)\ge n-1$。

## 要点

- $g=1$ 时判据只查 $i=1$，而且退化成『$V^1$ 是否为空』，所以整条 $M$-正则性可以手算。
- 互异点不会让计算变复杂：只有总次数进入 $\deg(L(-\sum k_ix_i))=d-\sum k_i$，故 $m(L)=p(L)=d-1$。
- $k=d$ 时次数掉到 $0$，层变平凡化一次，$h^1$ 跳成 $1$，$V^1$ 是一个单点——这正是 $M$-正则性失败的机制。
- 取 $L=n\Theta$ 得 $m(n\Theta)=n-1$，配定理 7.4 得 Seshadri 常数的下界 $\varepsilon(n\Theta)\ge n-1$。
- 高亏格下这条线性公式完全失效：维数 $\ge2$ 的不可约主极化阿贝尔簇上 $m(2\Theta)\ge2$，比椭圆曲线的 $2-1=1$ 大一格。

## 关键公式

$$
\deg(L(-kx))=d-k,\qquad h^1(L(-kx)\otimes\alpha)=h^0\bigl((L(-kx)\otimes\alpha)^{-1}\bigr)
$$

$$
m(L)=d-1\quad(d=\deg L\ge1),\qquad m(n\Theta)=n-1
$$

$$
\dim V^1\bigl(\mathcal O(2\Theta)\otimes\mathfrak m_x\otimes\mathfrak m_y\bigr)=0,\qquad V^1\bigl(\mathcal O(2\Theta)\otimes\mathfrak m_x^2\bigr)=\varnothing
$$

## 相关定理

- **例 7.14（椭圆曲线上的 $M$-正则性与 $m(L)$）**：设 $E$ 是椭圆曲线，$L$ 是 $E$ 上的线丛。则 $L$ 是 $M$-正则的 $\iff\deg L\ge1$（等价于 $L$ 充裕）；且当 $d=\deg L\ge1$ 时有 $m(L)=d-1$，从而对一切 $n\ge1$ 有 $m(n\Theta)=n-1$。

## 易错点

- 空集的余维必须按 $+\infty$ 计（等价写法 $\dim V^i\le g-i-1$）：若按 $\operatorname{codim}\varnothing=g=1$ 算，$\operatorname{codim}V^1>1$ 在椭圆曲线上永不成立，例 7.14 会自相矛盾。
- 别把『互异点』当成额外条件：$\deg$ 只看到总次数，故椭圆曲线上 $m(L)=p(L)$；在高亏格上这一点才失效，$p$ 与 $m$ 才需要分开定义。
- 别把 $m(n\Theta)=n-1$ 外推到高亏格：维数 $\ge2$ 的不可约 PPAV 上 $m(2\Theta)\ge2$（Kummer 映射的性质：$|2\Theta|$ 给出到 $\mathbb P^{2^g-1}$ 的 $2:1$ 映射且微分单射），说明『$\deg-1$』规律只是 $g=1$ 的巧合。

## 用到哪些概念

- [$M$-正则层](../concepts/m-regular-sheaf.md)
- [$M$-正则性指标 $m(L)$](../concepts/m-regularity-index.md)
- [$m$-$\Theta$-正则性](../concepts/m-theta-regular.md)

## 相关卡

- [$M$-正则性指标 $m(L)$](../concepts/m-regularity-index.md)
- [$M$-正则层](../concepts/m-regular-sheaf.md)
- [$m$-$\Theta$-正则性](../concepts/m-theta-regular.md)
- [$GV$-层](../concepts/gv-sheaf.md)

## 出处

- ch8 §7.1 例 7.14（椭圆曲线上的指标计算）；中译 p.149（英文 PDF p.166），源码 `chapters/ch08.tex:604`
