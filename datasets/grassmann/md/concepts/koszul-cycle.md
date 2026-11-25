# Koszul 闭链与退化轨迹

> `grassmann/concept/koszul-cycle` · 轨道 2 · Koszul 上同调 · 状态 draft

> **先自测**：为什么必须先让 $\mathrm{rank}\mathcal{A}=\mathrm{rank}\mathcal{B}$，退化轨迹才是一个除子而不是空集或更高余维的簇？

## 一句话

把「$K_{p,2}\neq0$」写成两个向量丛之间限制映射的退化轨迹，再用秩相等条件保证它是除子，于是可以用虚类算出 $\overline{\mathcal{M}}_g$ 上的新除子。

## 定义

记 $\widetilde{\mathfrak{G}}^r_d$ 为 $\mathfrak{G}^r_d$ 的部分紧化，在其上取向量丛 $\mathcal{A}(C,L)=H^0(\mathbb{P}^r,\wedge^pM_{\mathbb{P}^r}\otimes\mathcal{O}(2))$ 与 $\mathcal{B}(C,L)=H^0(C,\wedge^pM_L\otimes L^{\otimes2})$，以及限制映射 $\phi\colon mathcal{A}\to\mathcal{B}$。**Koszul 闭链**是 $\mathcal{U}_{g,p}:=\{(C,L)\in\mathfrak{G}^r_d:K_{p,2}(C,L)\neq0\}$，定理 3.5 断言它就是 $\phi$ 的退化轨迹；当 $r=2s+sp+p$、$g=rs+s$、$d=rs+r$ 时 $\mathcal{Z}_{g,p}:=\sigma_*(\mathcal{U}_{g,p})$ 是 $\mathcal{M}_g$ 上的虚除子。

**记号约定**：$\sigma\colon mathfrak{G}^r_d\to\mathcal{M}_g$ 为遗忘线性系的态射；$\mathcal{Z}_{g,p}$ 是推前得到的闭链。

## 要点（为什么需要它）

- $\mathcal{U}_{g,p}$ 是 $\phi$ 退化（不单射）的轨迹，于是「$K_{p,2}\neq0$」这个上同调条件变成「线性映射不是单射」这个线性代数条件，可以在族上逐纤维验证。
- 秩公式：$\mathrm{rank}\mathcal{A}=(p+1)\binom{r+2}{p+2}$，$\mathrm{rank}\mathcal{B}=\binom{r}{p}\left(-\frac{pd}{r}+2d+1-g\right)$；两者在 $r=2s+sp+p$、$g=rs+s$、$d=rs+r$ 时相等，此时退化轨迹的预期余维为 $1$。
- $s=1$ 时 $g=2p+3$、$r=2p+2$、$d=4p+4$；又 $\rho=0$ 且 $d=2g-2$ 迫使 $L=K_C$，故 $\mathfrak{G}^r_d\cong\mathcal{M}_g$，这正是 Green 猜想的临界情形。
- 定理 3.6 把 $\phi$ 延拓到 $\widetilde{\mathfrak{G}}^r_d$ 上并算 $c_1(\mathcal{B}-\mathcal{A})$，得 $[\overline{\mathcal{Z}}_{2p+3,p}]^{virt}=c_1(\mathcal{B}-\mathcal{A})$，其斜率恰为 $6+\frac{12}{g+1}$，即 Brill–Noether 除子的斜率。

## 关键公式

$$
\mathcal{U}_{g,p}=\{(C,L)\in\mathfrak{G}^r_d\colon mathrm{rank}\,\phi|_{(C,L)}<\mathrm{rank}\mathcal{B}\}
$$

$$
\mathrm{rank}\mathcal{A}=(p+1)\binom{r+2}{p+2},\qquad \mathrm{rank}\mathcal{B}=\binom{r}{p}\left(-\frac{pd}{r}+2d+1-g\right)
$$

$$
[\overline{\mathcal{Z}}_{2p+3,p}]^{virt}=\frac{1}{p+2}\binom{2p}{p}\left(6(p+3)\lambda-(p+2)\delta_0-6(p+1)\delta_1-\cdots\right)
$$

## 定理与证明（或缺口）

### 定理 3.5（Koszul 闭链 = 退化轨迹）

记号如上。则 $\mathcal{U}_{g,p}=\{(C,L)\in\mathfrak{G}^r_d:K_{p,2}(C,L)\neq0\}$ 是限制映射 $\phi\colon mathcal{A}\to\mathcal{B}$ 的退化轨迹；在秩相等条件 $r=2s+sp+p$、$g=rs+s$、$d=rs+r$（等价于 $g=s(2s+sp+p+1)$）下，$\mathcal{Z}_{g,p}=\sigma_*(\mathcal{U}_{g,p})$ 是 $\mathcal{M}_g$ 上的虚除子。

**证明状态：提纲（有缺口）**


> **缺口**：原文给出的是「$K_{p,2}=0\iff\phi$ 单射」这一观察加上秩计算，真正的困难在两边界的延拓：$\phi$ 要延拓到 $\widetilde{\mathfrak{G}}^r_d$ 的边界（可约曲线上的极限线性系、容许覆盖、半稳定等价），这部分是定理 3.6 与第 9 篇的内容，正文没有展开。


出处：中译 p.41（定理 3.5）

### 定理 3.6（类公式）

把 $\phi$ 延拓到 $\widetilde{\mathfrak{G}}^r_d$ 后，$c_1(\mathcal{B}-\mathcal{A})\equiv a\lambda-b_0\delta_0-b_1\delta_1-\cdots$ 满足 $b_1=12b_0-a$，斜率 $a/b_0=\frac{6f(s,p)}{(p+2)s\,h(s,p)}$；当 $s\ge2$ 时 $6<a/b_0<6+\frac{12}{g+1}$。

**证明状态：只引出处，原书不重证**


出处：中译 p.42（定理 3.6，引 Farkas–Popa）

## 易错点

- $\mathcal{U}_{g,p}$ 是 $\mathfrak{G}^r_d$ 上的子簇，$\mathcal{Z}_{g,p}$ 才是它在 $\mathcal{M}_g$ 的像；前者是退化轨迹，后者才是除子，别把两者混同。
- 秩相等的三个等式要联立：只验 $r=2s+sp+p$ 不够，还要 $g=rs+s$、$d=rs+r$；数值自检 $p=1,s=1$ 给 $g=5,d=8,r=4$，$\mathrm{rank}\mathcal{A}=2\binom{6}{3}=40=\mathrm{rank}\mathcal{B}=4(-2+16+1-5)$。
- 秩不等时退化轨迹可能是空集或更高余维，$\mathcal{Z}$ 不是除子；§5.1 里 $\rho=0$ 的虚除子 $\mathcal{Z}_{g,0}$ 正是这种临界情形。
- 式 (5) 中 $\delta_1$ 的系数是 $-6(p+1)$，漏掉因子 $6$ 会把斜率算成 $6+2/(g+1)$。

## 相关卡

- [核丛](../concepts/kernel-bundle.md)
- [有效除子的斜率](../concepts/slope-of-effective-divisor.md)
- [极大秩猜想](../concepts/maximal-rank-conjecture.md)
- [极小合冲猜想](../concepts/minimal-syzygy-conjecture.md)

## 出处

- ch2 §3.2 Koszul 闭链；中译 p.41（英文 PDF p.45），源码 `chapters/ch02.tex:487`
- ch2 §3.3 定理 3.6 与式 (5)；中译 p.42（英文 PDF p.46），源码 `chapters/ch02.tex:544`
