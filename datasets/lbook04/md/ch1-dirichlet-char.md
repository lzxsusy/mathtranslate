# Dirichlet 特征与 Dirichlet L 函数

> `lbook04/concept/ch1-dirichlet-char` · 轨 L L 函数 · 状态 reviewed · 核验 source-only

**问题：** 为什么 Dirichlet 定理（算术级数中的素数）等价于非主特征满足 $L(\chi,1)\ne0$？

**一句话：** 模 $q$ 的特征把 $(\mathbb Z/q\mathbb Z)^\times$ 的群同态延拓到 $\mathbb Z$ 上；$L(\chi,s)$ 的解析性质由本原特征与导子决定，非主特征在 $s=1$ 不为零即得 Dirichlet 定理。

**别名：** `Dirichlet character`、`Dirichlet L-function`、`导子与本原特征`

## 定义

设 $\tilde\chi:(\mathbb Z/q\mathbb Z)^\times\to\mathbb C^\times$ 为群同态，令 $\chi(n)=\tilde\chi(n \bmod q)$（若 $(n,q)=1$）而 $(n,q)\ne1$ 时 $\chi(n)=0$。$\chi$ 完全乘性，故 $L(\chi,s)=\sum\chi(n)n^{-s}=\prod_p(1-\chi(p)p^{-s})^{-1}$。用 $(\mathbb Z/q\mathbb Z)^\times$ 上的正交关系，可把「$p\equiv a$」的指示函数写成 $\frac{1}{\varphi(q)}\sum_\chi\overline\chi(a)\chi(p)$；再对 $\log L(\chi,s)$ 在 $s=1$ 附近展开，主项为 $\frac{1}{\varphi(q)}\log\frac{1}{s-1}$，非主特征的贡献若有 $1/\varphi(q)$ 量级的负项就会抵消主项——故 Dirichlet 定理归结为 $L(\chi,1)\ne0$（$\chi_4$ 给出 $\pi/4$ 的经典例子）。函数方程只对本原特征干净：任一 $\chi$ 由唯一本原 $\tilde\chi$ 诱导，$L(\chi,s)$ 与 $L(\tilde\chi,s)$ 差有限个 Euler 因子 (3.1)。

**记号：** $q$：模（导子的倍数）；$\tilde q$：导子（本原特征的模）；$\varphi$：Euler 函数；$\tau(\chi)$：Gauss 和；$\varepsilon(\chi)$：根数；$\Lambda(\chi,s)$：完备化 L 函数。

## 要点

- $\chi$ 在 $(x,q)\ne1$ 处取 $0$ 不是疏忽：这让 $p\mid q$ 处的 Euler 因子退化为 $1$，从而 $L(\chi,s)$ 与 $\zeta(s)$ 只差有限个因子。
- 本原特征才满足干净的函数方程；非本原 $\chi$ 由唯一本原 $\tilde\chi$ 诱导，二者相差有限乘积 (3.1)。
- Dirichlet 定理的解析核心是「$L(\chi,1)\ne0$」：$\log L$ 展开中主项由 $p\equiv1$ 的素数的 $1/p$ 给出，其余类由正交关系合成。

## 公式

$$
L(\chi,s)=\sum_{n\ge1}\chi(n)n^{-s}=\prod_{p}\bigl(1-\chi(p)p^{-s}\bigr)^{-1}
$$

$$
\Lambda(\chi,s)=\varepsilon(\chi)\,q^{1/2-s}\,\Lambda(\overline{\chi},1-s),\qquad \varepsilon(\chi)=\begin{cases}\tau(\chi)/\sqrt{q}, & \chi(-1)=1,\\ -i\,\tau(\chi)/\sqrt{q}, & \chi(-1)=-1.\end{cases}
$$

$$
L(\chi,s)=L(\tilde\chi,s)\prod_{p\mid q/\tilde q}\bigl(1-\chi(p)p^{-s}\bigr)
$$

## 定理与证明

**定理 3.1（算术级数中的素数）**　设 $(a,q)=1$，则有无穷多素数 $p\equiv a\pmod q$，且 $\sum_{p\le X,\,p\equiv a}\frac{1}{p}=\frac{1}{\varphi(q)}\log\log X+O(1)$。

1. 用正交关系把 $1_{p\equiv a}$ 写成 $\frac{1}{\varphi(q)}\sum_\chi\overline\chi(a)\chi(p)$。
1. 对每个 $\chi$ 展开 $\log L(\chi,s)$，$s\to1^+$；主特征给 $\log\frac{1}{s-1}$ 的主项。
1. $\chi\ne\chi_0$ 时 $L(\chi,1)\ne0$，故其对数在 $s=1$ 有界，不抵消主项。

> 跳步说明：书中只陈述定理；$L(\chi,1)\ne0$ 的证明（尤其实特征情形）要到本章后段与第 2 章才补，那里用的是类数公式与零点排斥。

*出处：ch01.tex:112-150（§3，定理 3.1）*

## 易错点

- $\varepsilon(\chi)$ 的两个分支由 $\chi(-1)=\pm1$ 决定；统一写法是 $\varepsilon(\chi)=\tau(\chi)/(i^a\sqrt q)$，$a\in\{0,1\}$ 由 $\chi(-1)=(-1)^a$ 定。$\sqrt q$ 与 $|\tau(\chi)|=\sqrt q$ 只对本原特征成立，非本原时要换成导子 $\tilde q$。
- (3.1) 的乘积下标是 $p\mid q/\tilde q$，不是 $p\mid q$：被剔除的正是「多余」的那些素因子。

## 批注

**〔易错预警〕模还是导子**　$\chi$ 的模 $q$ 不唯一（可乘素因子的幂提升），本原的 $\tilde q$ 才唯一；函数方程里出现的是 $\tilde q$ 而不是任意一个模。书中 §3 正是用这一点说明「先验未知的导子会以这种方式出现」。

**〔背景直觉〕Gauss 和是伽马因子的有限域类比**　$\tau(\chi)=\sum_{x\bmod q}\chi(x)e(x/q)$ 是加法特征与乘法特征的配对；书里把它称作 $\Gamma$ 因子的某种有限域类比，根数 $\varepsilon$ 因此是「阿基米德因子之外」的整体不变量。

## 相关

[[ch1-zeta-euler]]、[[ch1-gamma-factor]]、[[ch4-artin-hecke]]

## 来源

- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§3，原书 pp. 4–5（PDF pp. 12–13）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch01.tex:112-150`
- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§3，原书 pp. 5–7（PDF pp. 13–15）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch01.tex:155-201`
