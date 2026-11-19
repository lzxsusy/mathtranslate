# 滤过 A∞-范畴与有间隙条件

> `functoriality/concept/filtered-a-infinity` ｜ track A ｜ draft

**一句话**：滤过 A∞-范畴的态射带能量滤过，μ_k 只降低滤过度；有间隙指能量谱离散，使无穷计数可按能量逐阶收敛，并与 Novikov 系数相容。

**自测**：为什么在 Novikov 系数之外还需要「滤过且有间隙」这一层结构，它解决什么收敛问题？

## 定义

设 $A$ 是 $\mathbf K$-线性 $\Ainf$-范畴，$\mathbf K$ 为 Novikov 域或系数域。称 $A$ 带滤过，若每个态射空间带下降滤过 $F^{\ge\lambda}\hom$（$\lambda\in\R$），且每个运算 $\mu_k$ 只降低滤过度：$\mu_k(F^{\ge\lambda_1}\otimes\cdots\otimes F^{\ge\lambda_k})\subset F^{\ge\lambda_1+\cdots+\lambda_k}$。称滤过有间隙，若存在离散子集 $\Gamma\subset[0,\infty)$，使 $\mu_k$ 的非零贡献只出现在 $\lambda\in\Gamma$。在 Novikov 系数下，滤过指标 $\lambda$ 就是 $T$ 的指数（即辛面积），有间隙由 Gromov 紧性保证。

记号：$\lambda$ 记能量/辛面积指标；$\Gamma$ 记能量谱；§2.4 的带曲率理论要求更强的「有间隙 + 滤过 + 范数」条件。

## 要点

- 滤过把「无穷多条带」整理成可按能量截断的逐阶信息：计算到能量 $\\le E$ 只需有限多项，A∞ 方程可以逐阶验证。
- 有间隙保证每个能量层内条带有限；没有它，能量谱可能稠密，逐阶论证与域结构都会失效。
- 滤过是 §2.4 带曲率理论的关键：带曲率时需在底层分次向量空间上加范数，要求 $\\mu_0$ 的贡献范数严格小于 1，从而 $\\mu_1$ 的最低阶项占主导。
- 与谱序列技术同源：先按滤过算分次部分，再处理高阶修正；这是把分析问题代数化的标准手段。

## 公式

$$\Lambda\coloneqq\left\{\sum_{k=0}^{\infty}a_kT^{\lambda_k}\ \middle|\ a_k\in\mathbf k,\ \lambda_k\in\R,\ \lim_{k\to\infty}\lambda_k=+\infty\right\}.$$
$$\mu^k=\sum T^\lambda\mu^k_\lambda.$$

## 定理与证明

### 滤过与范数条件（注 thm:2.23）

为使带曲率范畴有良好理论，须在底层分次向量空间上引入范数，要求每个 μ_k 写成范数递减各项之和，并让 μ₀ 的所有贡献范数严格小于 1；这样 μ₁ 的最低阶贡献占主导，得到与普通 A∞ 理论平行的结论。

（none；来源：原书 p.17 §2.4）


缺口：原文只作说明性论述（注 thm:2.23），未给形式定理；严格化属 FOOO 的技术框架。

### 有间隙保证 A∞ 方程逐阶可比

若能量谱落在离散子集 Γ 内，则 A∞ 方程中每个能量层的贡献是有限和，方程可以按 T 的指数逐阶比较。

（none；来源：原书 p.10 §2.2）


缺口：原文把它作为 Novikov 系数的构造性说明（注 thm:2.10 与译注），未单独列为定理。

## 易错点

- 把滤过当成 $\\Z$-分次：滤过是下降链 $F^{\\ge\\lambda}$（$\\lambda\\in\\R$），分次另由 Maslov 指标给出，两者不能混为一谈。
- 以为有间隙自动成立：一般情形下能量谱未必离散；有间隙是需要验证的假设，带曲率理论中它和范数条件一起使用。
- 忽略滤过与系数域的相容性：滤过指标与 $T$ 的指数必须一致，否则 $\\mu^k=\\sum T^{\\lambda}\\mu^k_\\lambda$ 的分解对不上。

## 参考与关联

- Abouzaid & Bottman, Functoriality in categorical symplectic geometry (arXiv:2210.11159v1)，§2.2，p.9–11（原书 p.9–11 §2.2）

关联：`functoriality/concept/novikov-field`、`functoriality/concept/a-infinity-category`、`functoriality/concept/curved-a-infinity`

来源说明：原书 p.9–11 §2.2（注 thm:2.10 的滤过/有间隙讨论）与 p.17 §2.4（注 thm:2.23 的范数条件）；公式取自 chapter2.tex 的 eq:11、eq:40。
