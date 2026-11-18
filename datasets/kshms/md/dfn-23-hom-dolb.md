# Dolbeault 态射空间 $\mathrm{Hom}_{\mathrm{Dolb}}$

`kshms/concept/dfn-23-hom-dolb` · track G（复情形附录） · 原文 定义 23

**问题**　复情形附录里，全纯向量丛之间的 Dolbeault 态射空间如何定义？

**摘要**　对 $X$ 上两个全纯向量丛，$\mathrm{Hom}_{\mathrm{Dolb}}$ 取取值于 $\mathrm{Hom}(E_1,E_2)$ 的 $(0,*)$-形式空间；配以 $\bar{\partial}$-微分后成为 dg-代数。

**别名**　Dolbeault Hom；$\mathrm{Hom}_{\mathrm{Dolb}}(E_1,E_2)$；Dolbeault 形式空间

## 陈述

对 $X$ 上任意两个全纯向量丛 $E_1$、$E_2$，定义
$$\mathrm{Hom}_{\mathrm{Dolb}}(E_1,E_2)=\Omega^{0,*}\bigl(X,\mathrm{Hom}(E_1,E_2)\bigr).$$

## 记号

$X$ 是复流形（附录中取 $X=X_\varepsilon$）；$\Omega^{0,*}$ 表示 $(0,q)$-形式的直和；$\mathrm{Hom}(E_1,E_2)$ 是 $X$ 上的全纯 Hom 丛。

## 要点

- 这是把全纯 Hom 丛的 $(0,*)$-形式截面取出来得到的分次向量空间，一般不是有限维的。
- 配以 $\bar{\partial}$-微分后成为 dg-代数，从而在 $X$ 上凝聚层的导出范畴上给出 $A_\infty$-范畴结构（实际上是 dg-范畴结构）。
- 原文指出，这一 $A_\infty$-结构与正文中（非阿基米德情形）提到的那个结构等价。
- $\mathrm{Hom}_{\mathrm{Dolb}}$ 是 §9.2 中扇区分解与层 $\underline{\mathrm{Hom}}_{\mathcal{A}(Y)}$ 的出发点。

## 公式

$$\mathrm{Hom}_{\mathrm{Dolb}}(E_1,E_2)=\Omega^{0,*}\bigl(X,\mathrm{Hom}(E_1,E_2)\bigr)$$

$$\bar{\partial}:\Omega^{0,q}\bigl(X,\mathrm{Hom}(E_1,E_2)\bigr)\longrightarrow\Omega^{0,q+1}\bigl(X,\mathrm{Hom}(E_1,E_2)\bigr)$$

## 易错点

- $\Omega^{0,*}$ 只是 $(0,q)$-形式的直和，不含 $(p,0)$ 部分；把它写成 $\Omega^{*}$ 会与 de Rham 复形混淆。
- $\mathrm{Hom}(E_1,E_2)$ 是 $X$ 上的向量丛，不是态射空间；不要把它与 $\mathrm{Hom}_{\mathrm{Dolb}}$ 本身混同。
- 这是复情形（$\varepsilon$ 固定）的构造；附录明言此时如何严格证明同调镜像猜想尚不清楚，相关级数的收敛性未证。

## 相关卡

- `kshms/concept/dfn-22-rigid-analytic-space`
- `kshms/concept/dfn-21-formal-laurent-series`

## 出处

- Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25） §9.1（原文 p.61）；锚点 `源码/chunks/ch10.tex:46-49（定义 23）`

> 原文 p61 §9.1 末；定义 23 紧接命题 10 的证明，其后说明 $\bar{\partial}$-微分使其成为 dg-代数。
