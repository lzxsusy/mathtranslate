# Riemann zeta 与 Euler 乘积

> `lbook04/concept/ch1-zeta-euler` · 轨 L L 函数 · 状态 reviewed · 核验 source-only

**问题：** Euler 乘积为什么比「$\zeta(s)$ 的级数定义」更强，它究竟把素数的什么信息编码进来了？

**一句话：** $\zeta(s)=\prod_p(1-p^{-s})^{-1}$ 把唯一分解写成局部因子；Riemann 把 $s$ 看成复变量，用完备化 $\Lambda$ 得到对称的函数方程。

**别名：** `Riemann zeta function`、`Euler product`、`ζ(s) 的 Euler 乘积`

## 定义

Euler 1737 年用调和级数发散重新证明了素数无穷多，并得到 $\sum_{p\le X}1/p=\log\log X+O(1)$。Riemann 1859 年的贡献不是乘积而是「把 $s$ 看成复变量」：他定义 $\Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)$，证明 $\Lambda(s)=\Lambda(1-s)$，算出 $\zeta(0)=-1/2$ 并指出平凡零点 $s=-2n$。Euler 乘积在 $\operatorname{Re}(s)>1$ 时绝对收敛，因此在该半平面给出 $\zeta(s)\ne0$；这正是后来素数定理证明的起点之一。书中 §2 还给出显式公式 (2.5)：素数幂上的 von Mangoldt 和等于极点主项、临界带零点求和与一条竖线上的阿基米德积分三项之和。

**记号：** $\zeta(s)$：Riemann zeta 函数；$p$：素数；$\Lambda(s)$：完备化 zeta；$\Gamma$：伽马函数；$\rho$：非平凡零点；$\Lambda(n)$：von Mangoldt 函数（第 2 章起用）。

## 要点

- Euler 乘积是唯一分解定理的解析形式：每个素数 $p$ 贡献因子 $(1-p^{-s})^{-1}$，乘开即得全部 $n^{-s}$。
- Riemann 的贡献在于「复变量 + 函数方程 + 零点」：他把一个收敛性问题变成了整函数/亚纯函数的对称性问题。
- $\operatorname{Re}(s)>1$ 时乘积绝对收敛，故 $\zeta(s)\ne0$；这是 Euler 乘积给出的定性信息，也是第 2 章无零点区域的出发点。

## 公式

$$
\zeta(s)=\prod_{p}\bigl(1-p^{-s}\bigr)^{-1}=\sum_{n\ge1}n^{-s},\qquad \operatorname{Re}(s)>1
$$

$$
\Lambda(s)=\pi^{-s/2}\Gamma\bigl(\tfrac{s}{2}\bigr)\zeta(s),\qquad \Lambda(s)=\Lambda(1-s)
$$

$$
\Lambda(n)=\begin{cases}\log p, & n=p^{k},\\ 0, & \text{其他}\end{cases}
$$

## 定理与证明

**命题 2.1（显式公式 (2.5)）**　设 $\varphi$ 为 $]0,+\infty[$ 上具紧支集的 $C^\infty$ 函数，$\hat\varphi(s)=\int_0^{+\infty}\varphi(x)x^{s-1}dx$，$\psi(x)=\varphi(x^{-1})/x$。则 $\sum_p\sum_{k\ge1}(\log p)(\varphi(p^k)+\psi(p^k))=\int_0^{+\infty}\varphi(x)dx-\sum_{\zeta(\rho)=0,\,0<\operatorname{Re}\rho<1}\hat\varphi(\rho)+\frac{1}{2\pi i}\int_{(-1/2)}\bigl(\tfrac12\frac{\Gamma'}{\Gamma}(\tfrac{s}{2})-\tfrac12\frac{\Gamma'}{\Gamma}(\tfrac{1-s}{2})\bigr)\hat\varphi(s)ds$。

1. 对 $\Lambda'/\Lambda$ 用 Mellin 反演，把 $\sum\Lambda(n)\varphi(n)$ 写成围道积分。
1. 把围道移到 $\operatorname{Re}(s)=-1/2$，途中拣出 $s=1$ 的极点（给 $\int\varphi$）与临界带内的零点（给 $-\sum\hat\varphi(\rho)$）。
1. 用 $\Lambda(s)=\Lambda(1-s)$ 把 $1-s$ 的部分化回 $s$，两个 $\Gamma'/\Gamma$ 各得系数 $1/2$。

> 跳步说明：书中只给公式与三项来源的说明，未逐行重排围道；第 2 章命题 3.5 才给出一般 Hecke 情形的证明梗概。

*出处：ch01.tex:74-100（§2，命题 2.1）*

## 易错点

- 把 $\Lambda(s)$ 当成整函数：$\Lambda$ 在 $s=0,1$ 各有一个单极点；整函数是 $\xi(s)=\tfrac12 s(s-1)\Lambda(s)$，且 $\xi(0)=\xi(1)=\tfrac12$。引用「Riemann 的函数方程」时要先声明用的是 $\Lambda$ 还是 $\xi$。
- 以为 Euler 乘积自动给出解析延拓：乘积只在 $\operatorname{Re}(s)>1$ 收敛，跨过这条线要靠 theta 函数与 Poisson 求和（第 2 章 §2）。

## 批注

**〔易错预警〕Λ 还是 ξ**　中译注本 §2 的批注特别指出：$\Lambda(s)$ 仍带两个极点，Riemann 1859 原文用的是 $\xi(s)=\tfrac12 s(s-1)\Lambda(s)$。若把「$\Lambda(s)=\Lambda(1-s)$」直接说成「$\zeta$ 的函数方程」，会漏掉极点与对称轴 $s=1/2$ 的平移。

**〔背景直觉〕Euler 因子是局部数据**　书中脚注提醒：在数域上，Euler 因子 $L_{\mathfrak p}(s)$ 这份数据比乘积 $\prod_{\mathfrak p}L_{\mathfrak p}(s)$ 更强——即使乘积定义了一个全纯函数（例如第 5 节的部分 zeta），单个因子的信息仍可能丢失。这就是「局部-整体原则」在 L 函数上的雏形。

## 相关

[[ch1-dirichlet-char]]、[[ch1-gamma-factor]]

## 来源

- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§2，原书 pp. 1–2（PDF pp. 9–10）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch01.tex:17-35`
- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§2，原书 pp. 3–4（PDF pp. 11–12）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch01.tex:43-70`
