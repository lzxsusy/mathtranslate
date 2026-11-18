# 坍缩的 Gromov–Hausdorff 极限：整仿射 Monge–Ampère 流形

`kshms/concept/conj-01-collapse-gh-limit` · track A（CFT 与几何退化） · 原文 猜想 1

**问题**　极大退化的 Calabi–Yau 族在 $q\to0$ 时按直径标度后，度量空间极限长什么样？光滑部分还剩哪些几何结构？

**摘要**　若 $\mathcal{X}_{mer}$ 在 $q=0$ 处极大退化，则按直径重新标度的 $X_q^{new}$ 在 Gromov–Hausdorff 度量下收敛到紧度量空间 $\bar Y$，其光滑部分带整仿射结构、有势度量与常体积元，即一个实 Monge–Ampère 流形。

**别名**　Conjecture 1；collapse limit of a maximal degeneration；SYZ 型坍缩极限的度量刻画

## 陈述

若 $\mathcal{X}_{mer}$ 在 $q=0$ 处有极大退化，则 $X_q^{new}$ 在 Gromov–Hausdorff 度量下存在极限 $(\bar Y,g_{\bar Y})$，使得：

a) $(\bar Y,g_{\bar Y})$ 是紧度量空间，它包含一个 $n$ 维光滑定向黎曼流形 $(Y,g_Y)$ 作为稠开的度量子空间。$Y^{sing}=\bar Y\setminus Y$ 的 Hausdorff 维数不超过 $n-2$。

b) $Y$ 带有整仿射结构（integral affine structure）。这是指：$Y$ 上带有一个无挠平坦联络 $\nabla$，其和乐含于 $SL(n,\mathbb{Z})$ 之中。

c) 度量 $g_Y$ 有势。这是指：在仿射坐标下它局部由对称矩阵 $(g_{ij})=(\partial^2K/\partial x_i\partial x_j)$ 给出，其中 $K$ 是光滑函数（定义到相差一个仿射函数，即一个线性函数与一个常数之和）。

d) 在仿射坐标下度量的体积元为常数，$\det(g_{ij})=\det(\partial^2K/\partial x_i\partial x_j)=\mathrm{const}$（实 Monge–Ampère 方程）。

## 记号

$X_q^{new}=(X_q,g^{new}_{X_q})$，$g^{new}_{X_q}=g_{X_q}/\operatorname{diam}(X_q,g_{X_q})^2$：重新标度后直径为 $1$ 的族；$\rho_{GH}$：Gromov–Hausdorff 度量；$Y^{sing}=\bar Y\setminus Y$：极限空间的奇点集；$\nabla$：$Y$ 上的无挠平坦联络。

## 要点

- 这是猜想，不是定理：原文没有证明，只在 §3.1 末尾给出「基于微分几何的考虑」的不严格解释，并说明凯勒类（精确到标量）的固定禁止多重坍缩。
- a)–d) 四项合起来说的是：极限空间的光滑部分 $Y$ 是一个带整仿射结构的 Monge–Ampère 流形（定义 2 的实类比），度量由势 $K$ 的 Hessian 给出且满足实 Monge–Ampère 方程。
- 极限取在 Gromov–Hausdorff 意义下，且必须先按直径重新标度：不标度时 $q\to0$ 的体积发散，度量族根本没有收敛子列。
- $\dim_{\mathrm{Haus}}Y^{sing}\le n-2$ 是结论的一部分：奇点集至少余维 $2$，因此 $Y$ 上的仿射结构与度量在典型情形可以跨越 $Y^{sing}$ 讨论（注 4 进一步预期 $\bar Y$ 是同调球）。
- 满足 a)–c) 的三元组 $(Y,g_Y,\nabla)$ 是后文的构造输入：取 $\varepsilon$-环面丛 $X^\varepsilon\to Y$，得到非紧的 Ricci 平坦凯勒族；猜想 2 把 $X_q^{new}$ 与它作比较。

## 公式

$$g^{new}_{X_q}=g_{X_q}/\operatorname{diam}(X_q,g_{X_q})^2$$

$$X_q^{new}\xrightarrow{\ \rho_{GH}\ }(\bar Y,g_{\bar Y}),\qquad \dim_{\mathrm{Haus}}(\bar Y\setminus Y)\le n-2$$

$$(g_{ij})=(\partial^2K/\partial x_i\partial x_j),\qquad \det(g_{ij})=\mathrm{const}$$

## 易错点

- 这是猜想，不是定理：原文只有 §3.1 末尾的「直觉解释」（对数因子只应来自环面纤维、凯勒类的固定禁止多重坍缩），不能当作证明引用。
- 极限是度量空间的 Gromov–Hausdorff 极限，不是复流形或代数的极限：$(\bar Y,g_{\bar Y})$ 只是紧度量空间，光滑结构只存在于稠开的 $Y$ 上。
- 条件 d) 的 $\det(g_{ij})=\mathrm{const}$ 只在仿射坐标下有意义（换仿射坐标行列式只差常数倍）；它也不表示 $g_Y$ 平坦——平坦的是 $\nabla$，$g_Y$ 一般不与 $\nabla$ 平行。
- 余维条件 $\dim_{\mathrm{Haus}}Y^{sing}\le n-2$ 是猜想的结论而非假设，不要把它当成额外的「奇点很小」条件加进陈述。

## 相关卡

- `kshms/concept/dfn-01-maximal-degeneration`
- `kshms/concept/dfn-02-monge-ampere-manifold`
- `kshms/concept/conj-02-collapse-ma-model`
- `kshms/remark/rmk-04-convex-potential-legendre`

## 出处

- Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25） §3.1（原文 p.15）；锚点 `源码/chunks/ch03.tex:100-115（猜想 1）`

> 原文 p15 §3.1；译本 p15；紧随其后的注 4 补两点技术说明，§3.1 末尾给出猜想的非严格解释。
