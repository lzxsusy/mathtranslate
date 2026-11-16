# $n=1$ 时 $\operatorname{Sp}(2)=\operatorname{SL}(2)$

> `geoq/example/sp2-equals-sl2` · 轨道 A · 相空间的辛几何 · 状态 draft

> **这张卡练什么**：为什么 $2\times2$ 的辛矩阵只有「行列式为 1」一个条件？这个巧合能推广到 $n\ge2$ 吗？

## 一句话

在 $\mathbb{R}^2$ 的标准辛形式下，保持 $\omega$ 的矩阵恰好是行列式为 1 的矩阵，于是辛群退化为特殊线性群。

## 设定

取 $V=\mathbb{R}^2$，$\omega=\omega_1$ 由 $\omega(e_1,e_2)=1$ 定义，矩阵写法为 $\begin{pmatrix}0&1\\-1&0\end{pmatrix}$。设 $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\operatorname{GL}(2,\mathbb{R})$，要判断 $A\in\operatorname{Sp}(2)$，即 $\omega(Au,Av)=\omega(u,v)$ 对一切 $u,v$ 成立。

## 计算

**第 1 步**：把条件写成矩阵方程。$\omega(u,v)=u^T J v$，其中 $J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$。于是「$A$ 保持 $\omega$」等价于 $A^TJA=J$。

> 为什么：辛形式是双线性的，只需验证它在基向量上的取值；矩阵写法把「对所有 $u,v$ 成立」压缩成一个方程。

**第 2 步**：展开 $A^TJA$。$A^TJA=\begin{pmatrix}a&c\\b&d\end{pmatrix}\begin{pmatrix}0&1\\-1&0\end{pmatrix}\begin{pmatrix}a&b\\c&d\end{pmatrix}=\begin{pmatrix}0&ad-bc\\-(ad-bc)&0\end{pmatrix}=(ad-bc)J$。

> 为什么：直接做两次矩阵乘法；关键是所有项都归并到 $ad-bc$ 这一个行列式上。

**第 3 步**：比较 $(ad-bc)J=J$。因为 $J\ne0$，这等价于 $ad-bc=1$，即 $\det A=1$。

> 为什么：标量只能通过行列式整体缩放 $J$，所以辛条件恰好是一个标量方程。

**第 4 步**：反过来，任何 $\det A=1$ 的 $2\times2$ 矩阵都满足 $A^TJA=J$，因此 $\operatorname{Sp}(2)=\operatorname{SL}(2)$。

> 为什么：步骤 2 是恒等式，$\det A=1$ 时它自动成立，两个方向的包含都得到。

## 结果

$\operatorname{Sp}(2)=\left\{A\in\operatorname{GL}(2,\mathbb{R})\mid\det A=1\right\}=\operatorname{SL}(2)$。特别地 $\dim\operatorname{Sp}(2)=3$，与 $\dim\operatorname{SL}(2)=3$ 一致。

## 复核

用 Lie 代数复核：$\mathfrak{sp}(2)=\{X\mid X^TJ+JX=0\}$，写 $X=\begin{pmatrix}\alpha&\beta\\\gamma&-\alpha\end{pmatrix}$，恰有 3 个自由参数，与 $\mathfrak{sl}(2)$（迹为零）同维数。再取一个具体矩阵 $A=\begin{pmatrix}1&1\\0&1\end{pmatrix}$，直接算 $A^TJA=J$ 验证。

## 易错点

- 这是 $n=1$ 的偶然等同。$n\ge2$ 时 $\dim\operatorname{Sp}(2n)=n(2n+1)$，而 $\dim\operatorname{SL}(2n)=4n^2-1$，两者一般不相等，$\operatorname{Sp}(2n)\not\cong\operatorname{SL}(2n)$。
- 辛矩阵的行列式恒为 1，但「行列式为 1」只是 $n=1$ 时的充分条件；不要把 $\operatorname{Sp}\subset\operatorname{SL}$ 误记成等号。

## 用到哪些概念

- [辛群 $\operatorname{Sp}(V)$](../concepts/symplectic-group.md)
- [辛向量空间与辛基](../concepts/symplectic-vector-space.md)

## 相关卡

- [标准辛基下的相容复结构](../examples/standard-compatible-complex-structure.md)

## 出处

- §5.1.1 例 5.1.4，p.251（PDF p.252），源码 `ch05a.tex:94-105`
