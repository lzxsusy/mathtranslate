# Novikov 域

> `functoriality/concept/novikov-field` ｜ track A ｜ draft

**一句话**：Novikov 域是以实数为指数、指数趋于无穷的形式幂级数域；Floer 与 Fukaya 理论用它编码辛面积，使无穷条带计数可以收敛地相加。

**自测**：为什么 Floer 微分必须取值在 Novikov 域里，而不能只用普通域上的有限和？

## 定义

Novikov 域定义为 $\Lambda\coloneqq\left\{\sum_{k=0}^{\infty}a_kT^{\lambda_k}\ \middle|\ a_k\in\mathbf k,\ \lambda_k\in\R,\ \lim_{k\to\infty}\lambda_k=+\infty\right\}$（式(11)），其中 $\mathbf k$ 是系数域（本文多取 $\Z/2\Z$），加法与乘法按形式幂级数进行，$T$ 是指标为实数的形式变量。几何上 $T^{\lambda}$ 记录辛面积 $\lambda=\omega(v)$：每条伪全纯条带对 $T$ 的指数就是它的辛面积。

记号：单调/正合情形可用多项式版本 $\Lambda_{\mathrm{poly}}$（只允许有限个非零 $T$ 幂）；有间隙指能量谱落在离散子集 $\Gamma\subset[0,\infty)$。

## 要点

- 收敛性：微分是无穷和，指数条件 $\lim\lambda_k=+\infty$ 保证对每个能量层只有有限多项贡献，这是 Floer 理论能代数化的技术基础。
- 能量分层：$T$ 的指数保持辛面积的信息，使「按能量截断」成为滤过结构，A∞ 方程才能逐阶比较。
- 系数域的选择影响结论：$\Z/2\Z$ 系数可回避定向问题；特征 0 域（如 $\Q$）能讨论更细的分次与符号。
- 简化情形：单调或正合时可把系数域下到 $\mathbf k$；单调情形还可在 $\Lambda_{\mathrm{poly}}$ 上定义 Fukaya 范畴（需平衡性），并与 $\Lambda$ 系数版本比较（式(20)）。

## 公式

$$\Lambda\coloneqq\left\{\sum_{k=0}^{\infty}a_kT^{\lambda_k}\ \middle|\ a_k\in\mathbf k,\ \lambda_k\in\R,\ \lim_{k\to\infty}\lambda_k=+\infty\right\}.$$
$\Lambda_{\mathrm{poly}}$

## 定理与证明

### 有间隙性与逐阶收敛

Novikov 系数下每条条带对 T 的指数等于其辛面积；只有当能量谱离散（有间隙）时，无穷多面积递增的贡献才能被收进系数，μ_k 的幂级数表达才有意义。

（none；来源：原书 p.9–10 §2.2）


缺口：原文在注 thm:2.10 与译注中说明这一点，未给形式证明；这是构造性约定而非定理。

### 单调/正合情形的系数下降

单调或正合情形可把系数域取为 k；单调情形还可在多项式版 Λ_poly 上定义 Fukaya 范畴，并且需要「平衡性」条件，由此得到与 Λ 系数版本的比较函子。

（none；来源：原书 p.9 §2.2）


缺口：原文只陈述结论（注 thm:2.10），引 [She15]、[Sei08] 等，未给证明。

## 易错点

- 把 $\\Lambda$ 当成普通的 Laurent 级数域：指数是实数且必须趋于 $+\\infty$，否则无穷和一般发散，Floer 微分不收敛。
- 以为换系数域不影响结论：$\\Z/2\\Z$ 与特征 0 域给出不同的定向与分次结论，$\\Lambda$ 与 $\\Lambda_{\\mathrm{poly}}$ 也不同（后者要求有限个 $T$ 幂）。
- 混淆「系数域」与「环」：$\\Lambda$ 是域，$\\Lambda_{\\mathrm{poly}}$ 只是一族有限和构成的子环，讨论模范畴时要区分二者。

## 参考与关联

- Abouzaid & Bottman, Functoriality in categorical symplectic geometry (arXiv:2210.11159v1)，§2.2，p.9–10（原书 p.9–10 §2.2）

关联：`functoriality/concept/floer-cohomology`、`functoriality/concept/fukaya-category`、`functoriality/concept/filtered-a-infinity`

来源说明：原书 p.9–10 §2.2（Novikov 域式(11)、注 thm:2.10 关于系数与 Λ_poly 的讨论）；定义在 §2.1 首次出现，按清单归入 §2.2 页区间。
