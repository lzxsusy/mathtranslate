# Fukaya 范畴的等价类只依赖连通分支

`kshms/concept/thm-01-fukaya-category-equivalence-class` · track C（Fukaya 与退化） · 原文 定理 1

**问题**　Fukaya 范畴依赖殆复结构 $J$ 与全纯体积形式 $\Omega$ 的选取，换一组 $(J,\Omega)$ 会得到不等价的范畴吗？

**摘要**　在相容殆复结构空间的某个第二纲集 $\Sigma$ 上，只要 $(J_1,\Omega_1)$ 与 $(J_2,\Omega_2)$ 同伦，两个 Fukaya 范畴就等价；故等价类只依赖这对数据所在空间的连通分支。

**别名**　Theorem 1 (equivalence class of the Fukaya category)；Fukaya 范畴的第二纲集定理；Fukaya 范畴的同伦不变性

## 陈述

存在与 $\omega$ 相容的殆复结构空间中的一个第二纲集（Baire 意义下）$\Sigma$，使得只要 $J_1,J_2\in\Sigma$ 且 $(J_1,\Omega_1)$ 与 $(J_2,\Omega_2)$ 同伦，Fukaya 范畴 $\mathcal{F}(V,\omega,J_1,\Omega_1)$ 与 $\mathcal{F}(V,\omega,J_2,\Omega_2)$ 就等价。因此，Fukaya 范畴的等价类只依赖于这对数据所在空间的连通分支。

## 记号

$\mathcal{F}(V,\omega,J,\Omega)$：$(V,\omega)$ 上由 $J$ 与 $\Omega$ 定义的 Fukaya 范畴，对象是带局部系的紧定向拉格朗日子流形 $(L,\rho)$，高阶复合由 $J$-全纯曲线的模空间计数；$\Sigma$：与 $\omega$ 相容的殆复结构空间中的第二纲集；$(J,\Omega)$ 构成的空间赋以自然拓扑，其连通分支之集是格 $H^1(V,\mathbb{Z})$ 上的主齐性空间，$f:V\to U(1)$ 以 $(J,\Omega)\mapsto(J,f\Omega)$ 作用。

## 要点

- 第二纲集是 Baire 意义下的「一般位置」：它不能表为可数个无处稠密集之并，与 $\omega$ 相容的殆复结构空间是 Baire 空间，故这样的 $\Sigma$ 存在且稠密。
- 等价性的前提有两条，缺一不可：$J_1,J_2\in\Sigma$，且 $(J_1,\Omega_1)$ 与 $(J_2,\Omega_2)$ 在 $(J,\Omega)$ 空间中同伦。
- 结论落到「连通分支」：$(J,\Omega)$ 空间的分支之集是 $H^1(V,\mathbb{Z})$ 上的主齐性空间，相位作用 $(J,\Omega)\mapsto(J,f\Omega)$ 正给出这个主齐性结构。
- 定理由 Fukaya 的 $A_\infty$-范畴与 Floer 同调结果（[Fu2]）推出，本文不复述其证明。

## 公式

$$\mathcal{F}(V,\omega,J_1,\Omega_1)\simeq\mathcal{F}(V,\omega,J_2,\Omega_2),\quad J_1,J_2\in\Sigma,\ (J_1,\Omega_1)\sim(J_2,\Omega_2)$$

## 证明（sketch）

1. 原文指出：定理可由 Fukaya [Fu2] 关于 $A_\infty$-范畴与 Floer 同调的结果推出。

   *为什么*：这是定理在文中给出的唯一依据；本文只在前一段交代 $(J,\Omega)$ 空间连通分支的主齐性结构，不重复 [Fu2] 的论证。

2. 在 $\Sigma$ 上取 $J$，使各模空间 $\mathcal{M}(L_{i_0},\dots,L_{i_m};\beta)$ 为光滑流形、其边界与定向行为受控，则计数所得的 $m_k$ 只随 $(J,\Omega)$ 的同伦类变化。

   *为什么*：第二纲集保证这样的 $J$ 存在（Baire 纲定理），而同伦不变性使等价类只依赖 $(J,\Omega)$ 所在的连通分支。

> 缺口：缺口：原文只写「下面的定理可由 [Fu2] 推出」，既未构造 $\Sigma$，也未证明同伦不变性；完整论证见 K. Fukaya, A∞-category and Floer homologies（GARC Workshop on Geometry and Topology '93, Seoul, p.1–102），本文 p32 仅作引用。

## 易错点

- 第二纲集不等于开稠密集：结论只对「一般位置」的 $J$ 成立，个别 $J$ 可以落在补集里，此时范畴可能退化。
- 不能读成「任意两组 $(J,\Omega)$ 都给出等价范畴」：必须同在 $\Sigma$ 内，且两个二元组同伦。
- $(J,\Omega)\mapsto(J,f\Omega)$ 改变的是 $(J,\Omega)$ 所在的连通分支，不要把它误当成 $J$ 的形变；$\Omega$ 的相位与 $J$ 的选取是两件事。

## 相关卡

- `kshms/concept/dfn-16-fukaya-objects`
- `kshms/concept/dfn-13-a-inf-precategory-equivalence`
- `kshms/concept/thm-04-abelian-hms`

## 出处

- Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25） §5.1（原文 p.32）；锚点 `源码/chunks/ch05.tex:104-108（定理 1）`

> 原文 p32（§5.1）；译注「第二纲集」（ch05.tex:110-112）说明 Baire 纲的含义，定理前一段给出 $(J,\Omega)$ 空间连通分支的主齐性结构。
