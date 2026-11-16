# 标准辛基给出的两张拉格朗日子空间

> `geoq/example/standard-lagrangian-subspaces` · 轨道 A · 相空间的辛几何 · 状态 draft

> **这张卡练什么**：为什么 $\operatorname{span}\{e_i\}$ 与 $\operatorname{span}\{f_i\}$ 都是拉格朗日子空间，它们彼此是什么关系？

## 一句话

辛基的 $e$ 半边与 $f$ 半边各自张成拉格朗日子空间，二者互为 $\omega$-正交补，并直和成整个空间。

## 设定

取 $(V,\omega)=(\mathbb R^{2n},\omega_n)$，辛基 $\{e_1,\dots,e_n,f_1,\dots,f_n\}$，令 $L_1=\operatorname{span}\{e_1,\dots,e_n\}$、$L_2=\operatorname{span}\{f_1,\dots,f_n\}$。

## 计算

**第 1 步**：维数：$\dim L_1=\dim L_2=n=\frac12\dim V$，因为辛基线性无关、各取一半基向量。

> 为什么：张成空间的维数等于所用基向量的个数。

**第 2 步**：迷向：$\omega(e_i,e_j)=0$ 对一切 $i,j$，故 $\omega$ 在 $L_1\times L_1$ 上为零；同理 $\omega(f_i,f_j)=0$ 给出 $L_2$ 迷向。

> 为什么：双线性形式在张成空间上恒为零，当且仅当它在生成元的每一对上为零。

**第 3 步**：求 $L_1^\perp$：写 $u=\sum_i x_ie_i+\sum_i y_if_i$，则 $\omega(u,e_j)=\sum_i y_i\omega(f_i,e_j)=-\sum_i y_i\delta_{ij}=-y_j$。故 $u\in L_1^\perp\iff y=0\iff u\in L_1$，即 $L_1^\perp=L_1$。

> 为什么：只有 $f$ 分量与 $e_j$ 配对，且 $\omega(f_i,e_j)=-\delta_{ij}$；$e$ 分量自身配对为零。

**第 4 步**：同理 $\omega(u,f_j)=\sum_i x_i\omega(e_i,f_j)=x_j$，故 $L_2^\perp=L_2$。

> 为什么：与步骤 3 对称，只是这次符号为正。

**第 5 步**：交与和：辛基线性无关给出 $L_1\cap L_2=0$，而 $\dim L_1+\dim L_2=2n=\dim V$，故 $V=L_1\oplus L_2$；并且 $\omega\bigl(\sum x_ie_i,\sum y_jf_j\bigr)=\sum_i x_iy_i$ 是非退化配对，故 $L_2\cong L_1^*$。

> 为什么：维数相加等于全空间且交为零就得到直和；配对矩阵是 $I_n$，可逆，故给出对偶。

**第 6 步**：两张都满足拉格朗日定义（迷向 + 维数一半），并且由步骤 3–4 各自等于自己的 $\omega$-正交补。

> 为什么：定义与等价刻画同时验证，避免只验一半。

## 结果

$L_1=\operatorname{span}\{e_i\}$、$L_2=\operatorname{span}\{f_i\}$ 都是拉格朗日子空间，$L_1^\perp=L_1$、$L_2^\perp=L_2$、$V=L_1\oplus L_2$，且 $L_2\cong L_1^*$。

## 复核

(i) 任取 $u=\sum x_ie_i\in L_1$，$\omega(u,u)=0$ 自动成立，与迷向一致；(ii) 维数 $n+n=2n$ 且交为零，直和成立；(iii) $n=1$ 时 $L_1=\mathbb Re_1$、$L_2=\mathbb Re_2$，$\omega(e_1,e_2)=1$，是 $\mathbb{RP}^1$ 中相差 $\pi/2$ 的两个点；(iv) $J_0L_1=L_2$，符合 $V=L\oplus J(L)$。

## 易错点

- $L_1$ 与 $L_2$ 互补是这张例子的特殊之处，不是拉格朗日子空间的普遍性质：$\mathbb R^4$ 中可以有两个拉格朗日子空间交于一条直线。
- $L_1^\perp=L_1$ 用的是 $\omega$-正交补；若换成 $g_{J_0}$-正交补则 $L_1^*=L_2$，两者恰好互换，别把 $L^\perp$ 与 $L^*$ 混同。
- 零向量属于任何迷向子空间，$\{0\}$ 也是迷向的；「迷向」只排除非零向量与自身配对，不排除退化情形。

## 用到哪些概念

- [拉格朗日子空间与格拉斯曼流形](../concepts/lagrangian-grassmannian.md)
- [辛向量空间与辛基](../concepts/symplectic-vector-space.md)

## 相关卡

- [$\mathcal L(\mathbb R^2)=\mathbb{RP}^1$ 上的马斯洛夫指标](../examples/maslov-index-rp1.md)
- [标准辛基下的相容复结构](../examples/standard-compatible-complex-structure.md)

## 出处

- §5.1.2 例 5.1.14，p.255（PDF p.256），源码 `ch05a.tex:335-345`
