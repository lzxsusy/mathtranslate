# 增强三角范畴

> `siebert/concept/enhanced-triangulated-category` ｜ track F ｜ draft

**一句话**：把三角范畴的 Hom 群提升为复形、好三角提升为映射锥的数据；原书用它把 $\operatorname{Tw}^\Pi\mathcal F(X)$ 与 $D^b(Y)$ 放到同一层比较。

**自测**：为什么同调镜像对称不能直接陈述为「两个三角范畴等价」，而要先取 dg 或 $A_\infty$ 增强？

## 定义

设 $T$ 为三角范畴。$T$ 的一个增强是一个 dg（或 $A_\infty$）范畴 $\mathcal A$ 连同一个三角等价 $\mathrm{ho}(\mathcal A)\xrightarrow{\sim}T$，即把 $T$ 的态射集提升为复形、把好三角提升为映射锥。原书的具体用法是 $D^b\mathcal F(X)=H^0(\operatorname{Tw}^\Pi\mathcal F(X))$，其中 $\operatorname{Tw}^\Pi$ 是扭曲 Fukaya 范畴的分裂闭包（p.99–100）。

记号：$\operatorname{Tw}\mathcal A$ 记扭曲范畴（对象为满足 Maurer–Cartan 方程的扭曲复形），$\operatorname{Tw}^\Pi$ 记再加幂等元完备化（分裂闭包），$H^0$ 记取零次上同调。

## 要点

- 三角范畴的公理只约束 Hom 群与好三角，不记得复合的结合子与高阶运算；增强补上的正是这些高阶数据（Bondal–Kapranov 的 pretriangulated dg 范畴）。
- Kontsevich 的 $\operatorname{Tw}$：把 $\mathcal F(X)$ 的扭曲对象人为加入，即取 $\delta=(\delta_{ij})$、$\delta_{ij}\in\Hom^1(L_j,L_i)$ 严格下三角并满足 Maurer–Cartan 方程 (6.17)，得到「三角 $A_\infty$ 范畴」。
- $\operatorname{Tw}^\Pi$ 再加幂等元的像作完备化，称分裂闭包；于是 $H^0(\operatorname{Tw}^\Pi\mathcal F(X))$ 才是三角范畴，原书记作 $D^b\mathcal F(X)$。
- 猜想 1（HMS）：$\psi:D^b\mathcal F(X)=H^0(\operatorname{Tw}^\Pi\mathcal F(X))\xrightarrow{\sim}D^b(Y)$；两边都是「增强后的范畴取上同调」，等式才有意义。
- 增强不唯一但可比：dg 增强之间用拟等价比较；幂等完备的 pretriangulated dg 范畴与稳定 $k$-线性 $(\infty,1)$-范畴等价（nLab 引 Cohn）。

## 公式

$$\psi:D^b\mathcal F(X)=H^0\bigl(\operatorname{Tw}^\Pi\mathcal F(X)\bigr)\xrightarrow{\ \sim\ }D^b(Y)\qquad(6.18)$$
$$\delta_{ij}=0\ (j\ge i),\qquad \delta_{ij}\in\Hom^1(L_j,L_i)$$
$$\sum_{r\ge1}\sum_{i_0<\cdots<i_r}m_r(\delta_{i_r,i_{r-1}},\ldots,\delta_{i_1,i_0})=0\qquad(6.17)$$

## 定理与证明

### 猜想 1（同调镜像对称）

对紧 Calabi–Yau 流形 $(X,\omega)$ 及其镜像族 $Y/S$（$S=\Spec K$，$K=\Lambda_{\mathrm{nov},\CC}$），存在典范的 $A_\infty$ 范畴等价 $\psi:D^b\mathcal F(X)\xrightarrow{\sim}D^b(Y)$。

（none；来源：原书 p.99–100）


缺口：讲义只陈述猜想，未给证明；这是 Kontsevich HMS 猜想在亏格零、$c_1(X)=0$ 情形下的精确形式，属公开问题。

## 易错点

- $\operatorname{Tw}^\Pi$ 里的 $\Pi$ 是「幂等完备化」，与 §2.2 同调扰动引理里的投影算子 $\Pi$ 只是同名，含义完全不同。
- $\operatorname{Tw}$ 不是「取复形范畴」：扭曲对象必须满足 Maurer–Cartan 方程 (6.17)，否则 $m_1$ 不闭合。
- 「$D^b(X)$ 是三角范畴」不等于给了 dg 增强：增强是额外数据，不同增强只在拟等价意义下等同。
- $H^0$ 只取零次上同调，不能写成 $H^*$；后者给出的是分次范畴，不是三角范畴。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 6 章 §1.5 同调镜像对称，p.99–100（原书 p.99–100）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 6 章 §2 导出范畴的微分分次增强与同调扰动引理，p.100–100（原书 p.100）

关联：`siebert/concept/dg-category`、`siebert/concept/homological-mirror-symmetry`、`siebert/concept/fukaya-category`

来源说明：原书 p.99–100 §1.5（猜想 1、$\operatorname{Tw}^\Pi$ 分裂闭包）。nLab「enhanced triangulated category」（last revised 2026-01-27）核对 Bondal–Kapranov 的 pretriangulated dg 范畴、Lunts–Orlov 唯一性与 Cohn 的稳定 $\infty$-范畴对应；nLab「dg-category」（2024-05-14）核对同调范畴。
