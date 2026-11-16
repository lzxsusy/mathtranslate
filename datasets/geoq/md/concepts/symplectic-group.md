# 辛群 $\operatorname{Sp}(V)$

> `geoq/concept/symplectic-group` · 轨道 A · 相空间的辛几何 · 状态 draft

> **先自测**：辛群、正交群与「与 $J$ 交换的线性群」三者之间为什么只两两交出酉群？辛群又为什么比正交群大？

## 一句话

保持辛配对的可逆线性变换组成辛群；在标准基下即满足分块矩阵方程的矩阵，维数 $n(2n+1)$，并与正交群、复线性群两两相交于酉群。

## 定义

固定辛向量空间 $(V,\omega)$。所有保持 $\omega$ 的可逆线性变换 $\phi:V\to V$（即 $\omega(\phi u,\phi v)=\omega(u,v)$ 恒成立）组成辛群 $\operatorname{Sp}(V,\omega)$，简写 $\operatorname{Sp}(V)$。在标准空间 $(\mathbb R^{2n},\omega_n)$ 上记作 $\operatorname{Sp}(2n)$；按辛基把 $\phi$ 写成 $n\times n$ 分块 $\phi=\begin{pmatrix}A&B\\mathbb{C}&D\end{pmatrix}$，条件 $\phi^T\omega_n\phi=\omega_n$ 等价于 $A^TC=C^TA$、$B^TD=D^TB$、$A^TD-C^TB=I_n$ 三式。

**记号约定**：分块次序与辛基 $(e_1,\dots,e_n,f_1,\dots,f_n)$ 一致：前 $n$ 个坐标沿 $e$ 方向，后 $n$ 个沿 $f$ 方向。$\operatorname{GL}(V,J)$ 指与 $J$ 交换的可逆变换（即 $V$ 的复线性自同构），$\operatorname{O}(V)$ 与 $\operatorname{U}(V)$ 分别关于 $g_J$ 与厄米形式 $\langle-,-\rangle=g_J+i\omega$ 定义。

## 要点

- $\operatorname{Sp}(V)$ 是 $\operatorname{GL}(V)$ 的闭子群，故为 Lie 群；其维数是 $n(2n+1)$，比 $\dim\operatorname{O}(2n)=n(2n-1)$ 大了 $2n$，所以辛条件比正交条件弱。
- 三个矩阵方程只对应 $\omega_n$ 的三个独立分块：左上、右下各一个对称性方程，右上给 $I_n$，左下是右上的转置。
- 由 $\phi^T\omega_n\phi=\omega_n$ 取行列式只得 $(\det\phi)^2=1$；$\det\phi=1$ 还要补一步（辛群连通，或用普法夫量 $\operatorname{Pf}(\phi^T\omega_n\phi)=\det\phi\,\operatorname{Pf}(\omega_n)$）。
- 命题 5.1.7：$\operatorname{Sp}(V)$、$\operatorname{GL}(V,J)$、$\operatorname{O}(V)$ 三群中任意两个的交都等于 $\operatorname{U}(V)$，因为 $g_J=\omega(-,J-)$ 把三者绑在一起。
- $\operatorname{Sp}(V)$ 在拉格朗日格拉斯曼流形 $\mathcal{L}(V)$ 上可迁；辛群正是「保持辛结构」这一侧的对称性全体，量子化时它作用在预量子化线丛上。

## 关键公式

$$
$\phi\in\operatorname{Sp}(V)\iff\omega(\phi u,\phi v)=\omega(u,v)\ \forall u,v\iff\phi^T\omega_n\phi=\omega_n$
$$

$$
$A^TC=C^TA,\qquad B^TD=D^TB,\qquad A^TD-C^TB=I_n$
$$

$$
$\operatorname{Sp}(V)\cap\operatorname{GL}(V,J)=\operatorname{Sp}(V)\cap\operatorname{O}(V)=\operatorname{GL}(V,J)\cap\operatorname{O}(V)=\operatorname{U}(V)$
$$

$$
$\dim\operatorname{Sp}(2n)=n(2n+1),\qquad \operatorname{Sp}(2)=\operatorname{SL}(2)$
$$

$$
$g_J(u,v)=\omega(u,Jv),\qquad \langle u,v\rangle=g_J(u,v)+i\,\omega(u,v)$
$$

## 定理与证明

### 命题 5.1.7（三个群的交都是酉群）

设 $(V,\omega)$ 是辛向量空间，$J$ 是 $\omega$-相容复结构，$g_J=\omega(-,J-)$，$\langle-,-\rangle=g_J+i\omega$。则 $\operatorname{Sp}(V)\cap\operatorname{GL}(V,J)=\operatorname{Sp}(V)\cap\operatorname{O}(V)=\operatorname{GL}(V,J)\cap\operatorname{O}(V)=\operatorname{U}(V)$：$\phi$ 只要保持 $\omega,J,g_J$ 中的任意两个，就自动保持第三个与整个厄米结构。

**完整证明**

1. 若 $\phi$ 同时保 $\omega$ 与 $J$，则 $g_J(\phi u,\phi v)=\omega(\phi u,J\phi v)=\omega(\phi u,\phi Jv)=\omega(u,Jv)=g_J(u,v)$，故 $\phi\in\operatorname{O}(V)$。
   - *为什么*：关键是把 $J\phi v$ 换成 $\phi Jv$，这正是「$\phi$ 与 $J$ 交换」；于是 $\operatorname{Sp}\cap\operatorname{GL}(V,J)\subset\operatorname{O}(V)$。
2. 若 $\phi$ 同时保 $\omega$ 与 $g_J$，则对一切 $u,v$ 有 $g_J(\phi u,J\phi v)=\omega(\phi u,-\phi v)=-\omega(\phi u,\phi v)=-\omega(u,v)=g_J(u,Jv)=g_J(\phi u,\phi Jv)$。$\phi$ 可逆、$g_J$ 非退化，故 $J\phi v=\phi Jv$，即 $\phi\in\operatorname{GL}(V,J)$。
   - *为什么*：非退化性允许从「对所有 $\phi u$ 成立」回到向量本身的相等，这一步是唯一用到正定性的地方。
3. 若 $\phi$ 同时保 $J$ 与 $g_J$，由 $\omega(u,v)=-g_J(u,Jv)$ 得 $\omega(\phi u,\phi v)=-g_J(\phi u,J\phi v)=-g_J(\phi u,\phi Jv)=-g_J(u,Jv)=\omega(u,v)$。
   - *为什么*：$\omega$ 完全由 $g_J$ 与 $J$ 决定（$\omega=g_J(\cdot,J\cdot)$ 的变体），保后两者自然保 $\omega$；负号来自 $J^2=-1$。
4. 三步合起来说明三个两两交相等。又 $\langle-,-\rangle=g_J+i\omega$ 的实部与虚部分别是 $g_J$ 与 $\omega$，故 $\phi$ 保厄米形式当且仅当它同时保 $g_J$ 与 $\omega$，即 $\operatorname{U}(V)=\operatorname{Sp}(V)\cap\operatorname{O}(V)$。四个群（三个交）全部相等。
   - *为什么*：复内积的实部、虚部是两个实双线性形式，保持复内积等价于分别保持它们，这是把 $\operatorname{U}$ 接进来的最后一块。

来源：ch05a.tex:186-207（原书 p.253）

### 分块条件与辛群的维数

$\phi^T\omega_n\phi=\omega_n$ 等价于三个矩阵方程 $A^TC=C^TA$、$B^TD=D^TB$、$A^TD-C^TB=I_n$；并且 $\dim\operatorname{Sp}(2n)=n(2n+1)$。

**完整证明**

1. 做分块乘法：$\phi^T\omega_n\phi$ 的四个块依次是 $A^TC-C^TA$、$A^TD-C^TB$、$B^TC-D^TA$、$B^TD-D^TB$，令其等于 $\omega_n$ 的四个块即得三个方程（左下块是右上块的转置的相反数，不独立）。
   - *为什么*：$\omega_n$ 的左上、右下块为零，右上为 $I_n$，左下为 $-I_n$，逐块比较即可。
2. 数维数改用切空间：把 $\phi=I+tX$ 代入并取 $t$ 的一阶项，得 $X^T\omega_n+\omega_nX=0$，即 $\omega_nX$ 对称。
   - *为什么*：群的条件是非线性的，但它在单位元处的切空间由线性方程刻画，而群与切空间同维数。
3. $X\mapsto\omega_nX$ 是 $2n\times2n$ 矩阵空间到自身的线性同构，故满足条件的 $X$ 与所有对称矩阵一一对应；对称矩阵空间维数 $\frac{2n(2n+1)}{2}=n(2n+1)$，于是 $\dim\operatorname{Sp}(2n)=n(2n+1)$。
   - *为什么*：把「受约束的对象」线性同构到「标准的对象」上，维数就直接可数，不需要解非线性方程。
4. 核对低维：$n=1$ 时得 $3$，与 $\dim\operatorname{SL}(2)=3$ 一致，符合 $\operatorname{Sp}(2)=\operatorname{SL}(2)$。
   - *为什么*：$n=1$ 是唯一能与特殊线性群对照的情形，可当作公式的独立检验。

来源：ch05a.tex:67-93（原书 p.251；维数结论为本文补充的推论）

## 易错点

- 第三个方程是 $A^TD-C^TB=I_n$，不是 $A^TD-B^TC$：$B$ 与 $C$ 的位置对应分块的右上、左下，写反等于把 $\omega_n$ 的符号搞错。
- $(\det\phi)^2=1$ 推不出 $\det\phi=1$。$n=1$ 时可以由 $\operatorname{Sp}(2)=\operatorname{SL}(2)$ 直接读出，$n\ge2$ 时必须补连通性论证（或用普法夫量），不要两步并作一步。
- 不要把 $\operatorname{Sp}(2n)$ 与 $\operatorname{SO}(2n)$、$\operatorname{SL}(2n)$ 混为一谈：$\operatorname{Sp}\cap\operatorname{O}=\operatorname{U}(n)$ 是「交」；$n\ge2$ 时 $\dim\operatorname{Sp}=n(2n+1)$ 既不等于 $n(2n-1)$ 也不等于 $4n^2-1$。

## 相关卡

- [辛向量空间与辛基](../concepts/symplectic-vector-space.md)
- [相容复结构与可缩性](../concepts/compatible-complex-structure.md)
- [拉格朗日子空间与格拉斯曼流形](../concepts/lagrangian-grassmannian.md)
- [$n=1$ 时 $\operatorname{Sp}(2)=\operatorname{SL}(2)$](../examples/sp2-equals-sl2.md)
- [$\operatorname{Sp}(2n)\cap\operatorname{O}(2n)=\operatorname{U}(n)$ 的显式实现](../examples/unitary-symplectic-intersection.md)
- [极化：实极化与凯勒极化](../concepts/polarization.md)

## 出处

- §5.1.1 定义 5.1.3 与分块方程，p.251（PDF p.252），源码 `ch05a.tex:59-93`
- §5.1.1 命题 5.1.7，p.253（PDF p.254），源码 `ch05a.tex:198-207`
