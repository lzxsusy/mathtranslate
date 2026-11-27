# 代数簇的 $\zeta$ 函数与 Deligne 的四个结论

> `goresky04/concept/zeta-function-of-variety` · 轨道 A · 域与 Galois 侧 · 状态 dev

> **先自测**：$\zeta(Y,s)$ 是怎么由上同调定义的，Deligne 的四个结论各说了什么？

## 一句话

$\zeta(Y,s)$ 把每个素数处 Frobenius 在 $H^i_{\et}$ 上的特征值打包成一个欧拉乘积；Deligne 证明它有理性、函数方程，且零点满足 Riemann 假设。

## 定义

设 $Y$ 定义在 $\bbF_q$ 上。把 $\Fr_p$ 在 $H^i_{\et}(Y,\Ql)$ 上的特征值记为 $\alpha_{ij}$，则 $\zeta(Y,s)$ 定义为这些特征值的欧拉乘积；等价地，$\zeta(Y,s)$ 是 $\#Y(\bbF_{q^m})$ 的增长函数。Deligne 证明：(1) 有理性；(2) 函数方程；(3) 零点与极点的位置（Riemann 假设的类比）；(4) 与拓扑 Betti 数的关系。

**记号**：$\zeta(Y,s)=\prod_p\zeta_p(Y,p^{-s})$；$t=q^{-s}$ 时常写作 $Z(Y,t)$；$\alpha_{ij}$ 是 $\Fr$ 在 $H^i_{\et}(Y,\Ql)$ 上的特征值。

## 要点（为什么需要它）

1. 把 $\zeta$ 与上同调挂钩，是 Weil 猜想的实质：$\zeta$ 的解析性质被翻译成 $\Fr$ 在有限维空间上的线性代数。
2. 「Riemann 假设」在这里不是比喻：它断言 $\alpha_{ij}$ 的复绝对值为 $q^{i/2}$，这正是 $\Re s=i/2$ 的类比。
3. 函数方程来自 Poincaré 对偶：$H^i$ 与 $H^{2d-i}$ 配对，特征值取倒数。

## 核心公式

$$
$\zeta(Y,s)=\prod_{i=0}^{2d}\prod_j\bigl(1-\alpha_{ij}q^{-s}\bigr)^{(-1)^{i+1}}$$\zeta(Y,s)\mapsto\pm q^{d(1-s)}\zeta(Y,1-s)$（函数方程）
$$

$$
$\zeta(Y,s)\mapsto\pm q^{d(1-s)}\zeta(Y,1-s)$（函数方程）
$$

## 定理与证明（或缺口）

### Deligne 的四个结论（Weil 猜想）

(1) $\zeta(Y,s)$ 是有理函数；(2) 满足函数方程 $\zeta(Y,s)=\pm q^{d(1-s)}\zeta(Y,1-s)$；(3) 每个 $\alpha_{ij}$ 的复绝对值为 $q^{i/2}$；(4) 当 $Y$ 光滑投射时，$\zeta$ 的「次数」与 Betti 数一致。

> 证明状态：**gap**。原文只列结论并注明是 Deligne 的定理（[Del]），没有证明；这是 20 世纪代数几何最深的结果之一。

出处：`A p.6`

## 常见误解

- 不要把它与 Dedekind $\zeta$ 或 Riemann $\zeta$ 混为一谈：这里是**代数簇**的 $\zeta$，即使 $Y=\mathrm{Spec}\,\bbZ$ 也只是形式上的类比。
- 函数方程里的 $\pm$ 号与 $d=\dim Y$ 有关，原文没展开符号，读者不必在此纠缠。
- 「Riemann 假设」部分（结论 3）只对光滑投射簇叙述，奇异簇要用相交上同调修正（见注 28）。

## 相关卡

[平展上同调与 Galois 作用](../concepts/etale-cohomology.md) · [从 Frobenius 特征值造出局部因子与欧拉乘积](../derivations/local-zeta-factor.md) · [Frobenius 元素与局部因子](../concepts/frobenius-element.md)

## 出处（印刷页）

- A p.6（A p.6）

> 说明：对应原文 §4.2 的四个结论与 $\zeta$ 函数定义；「Riemann 假设的类比」一段是把原文一句「与 $\Re s=1/2$ 类比」讲开。
