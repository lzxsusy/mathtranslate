# 模形式、Hecke 算子与本征形式

> `lbook04/concept/ch5-hecke-eigenform` · 轨 L L 函数 · 状态 reviewed · 核验 source-only

**问题：** Hecke 算子为什么两两交换，从而使模形式空间有一组同时的本征形式基？

**一句话：** $S_2(\Gamma_0(N))$ 上的 Hecke 算子 $T_p$ 两两交换，故可同时对角化；本征形式 $f=\sum a_n q^n$ 的 $a_p$ 同时是 $T_p$ 的特征值，其 $L$ 函数有与椭圆曲线同形的 Euler 乘积。

**别名：** `Hecke 代数`、`本征形式`、`eigenform`

## 定义

Hecke 代数 $\mathbb T=\mathbb Z[\dots,T_p,\dots]$ 由双陪集 $\Gamma_0(N)\bigl(\begin{smallmatrix}1&0\\0&p\end{smallmatrix}\bigr)\Gamma_0(N)$ 作用在 $S_k(\Gamma_0(N))$ 上；等价地由对应 $X_0(N)\leftarrow X_0(pN)\to X_0(N)$ 的「拉回再推前」定义。$\mathbb T$ 交换（§4.3 的对应演算；$N$ 为素数时半单），故 $S_k$ 有本征形式基。本征形式满足 $f\mid T_p=a_p f$，$f=\sum_{n\ge1}a_n q^n$，$a_1=1$；其 $L$ 函数在好位为 $\prod_p(1-a_p p^{-s}+p^{1-2s})^{-1}$。

**记号：** $\Gamma_0(N)$：同余子群；$S_k(\Gamma_0(N))$：权 $k$ 尖点形式；$T_p,U_p$：Hecke 算子；$\mathbb T$：Hecke 代数；$q=e^{2\pi i\tau}$。

## 要点

- $T_p$ 由双陪集作用定义；$p\nmid N$ 时对应 $p+1$ 个 $p$ 阶循环子群，作用在 $J_0(N)$ 上。
- Hecke 代数交换（$(4.9)$–$(4.10)$ 的对应演算），$N$ 素数时半单，从而同时对角化。
- 本征形式 $f$ 的系数 $a_p$ 是 $T_p$ 的特征值；Petersson 内积下不同本征形式正交。
- $L(f,s)=\sum a_n n^{-s}=\prod_p(1-a_p p^{-s}+p^{1-2s})^{-1}$（好位），与椭圆曲线 $L$ 同形。

## 公式

$$
f\mid T_p=a_p f,\qquad f=\sum_{n\ge1}a_n q^n,\quad a_1=1
$$

$$
L(f,s)=\sum_{n\ge1}a_n n^{-s}=\prod_{p\nmid N}\bigl(1-a_p p^{-s}+p^{1-2s}\bigr)^{-1}
$$

$$
\mathbb T=\mathbb Z[\dots,T_p,\dots]\subset\operatorname{End}(J_0(N))\otimes\mathbb Q
$$

## 易错点

- $p\mid N$ 时要用 $U_p$，本征值不再满足 $|a_p|\le 2\sqrt p$；不能把好位公式逐字搬到坏位。
- 本征形式不等于新形式：本征形式可以是旧形式的提升，新形式要求水平恰为 $N$ 且不属于更低水平的像。

## 批注

**〔含糊点拨〕两种 $T_p$**　§4.3 的 $T_p$ 是 $\operatorname{Jac}(X)\to\operatorname{Jac}(X)$ 的对应映射，§5 的 $\widetilde T_p$ 是 Tate 模上的 $F+V$；二者在 $J_0(N)$ 的 $\ell$ 进实现上相容，但作用空间与符号不同，读定理 5.1 时不要混用。

**〔背景直觉〕交换性为什么关键**　交换性把「找所有模形式」化成「解一组交换算子」，本征值 $(a_p)$ 于是成为模形式的坐标；§6 再用 $e_f$ 从 $J_0(N)$ 切出椭圆曲线 $E_f$，其 $L$ 函数就是 $L(f,s)$。

## 相关

[[ch5-elliptic-l]]、[[ch5-eichler-shimura]]、[[ch5-bsd]]

## 来源

- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§4.1–4.3，原书 pp. 101–103（PDF pp. 106–108）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch05.tex:414-486`
- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§5.2，原书 pp. 105（PDF pp. 110）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch05.tex:533-562`
