# 齐性扭微分算子层

> `mloc/concept/homogeneous-twisted-sheaf` · type=concept · track=B · status=draft · verification=source-only

**别名**：homogeneous twisted sheaf of differential operators、$(\mathcal D,\gamma,\alpha)$、$U^\circ=\mathcal O_X\otimes U(\mathfrak g)$

## 摘要

齐性扭层 $(\mathcal D,\gamma,\alpha)$：$G$-作用 $\gamma$ 与 $G$-等变 $\alpha:U(\mathfrak g)\to\Gamma(X,\mathcal D)$ 相容。

## 问题

齐性空间上的扭层要满足哪些与 $G$-作用相容的条件，为什么所有齐性扭层都来自 $U^\circ$ 的商？

## 定义

设 $G$ 是特征 $0$ 的代数闭域 $k$ 上的连通代数群，$X$ 是齐性 $G$-空间；对 $G$ 在 $\mathcal O_X$ 上作用的微分得到代数同态 $\tau:U(\mathfrak g)\to\Gamma(X,\mathcal D_X)$，它 $G$-等变。齐性扭微分算子层是三元组 $(\mathcal D,\gamma,\alpha)$：$\mathcal D$ 是 $X$ 上的扭层，$\gamma$ 是 $G$ 在 $\mathcal D$ 上的代数作用，$\alpha:U(\mathfrak g)\to\Gamma(X,\mathcal D)$ 是代数同态，满足 (i) $\mathcal D$ 的乘法是 $G$-等变的；(ii) $\gamma$ 的微分等于 $T\mapsto[\alpha(\xi),T]$（$\xi\in\mathfrak g$，$T\in\mathcal D$）；(iii) $\alpha$ 是 $G$-模的态射。

记号：$U^\circ=\mathcal O_X\otimes_k U(\mathfrak g)$；$\mathfrak g^\circ=\mathcal O_X\otimes\mathfrak g$；$\tau:U^\circ\to\mathcal D_X$；$\mathfrak b^\circ=\ker(\tau:\mathfrak g^\circ\to T_X)$；$J_0=\mathfrak b^\circ U^\circ$；$F_pU^\circ=\mathcal O_X\otimes F_pU(\mathfrak g)$。

## 要点

- 三条相容性缺一不可：乘法 $G$-等变；$\gamma$ 的微分是 $T\mapsto[\alpha(\xi),T]$；$\alpha$ 是 $G$-模态射。第二条把「$\alpha$ 是李代数作用」与「$\gamma$ 是群作用」接上。
- $U^\circ$ 的乘法 $(f\otimes\xi)(g\otimes\eta)=f\tau(\xi)g\otimes\eta+fg\otimes\xi\eta$ 由 $\tau$ 决定；它不是 $\mathcal O_X$-双线性的，所以 $\tau:U^\circ\to\mathcal D_X$ 是环层同态而不是 $\mathcal O_X$-代数同态。
- 滤过 $F_pU^\circ=\mathcal O_X\otimes F_pU(\mathfrak g)$ 满足 $F_0U^\circ=\mathcal O_X$、$F_1U^\circ=\mathcal O_X\oplus\mathfrak g^\circ$，且 $F_1U^\circ$ 作为代数层生成 $U^\circ$。
- 第 1 章引理 2.1：$\tau:\mathfrak g^\circ\to T_X$ 满，故 $T_X$ 是 $\mathfrak g^\circ$ 的商；第 1 章命题 2.2：$\tau:U^\circ\to\mathcal D_X$ 满且核恰为 $J_0=\mathfrak b^\circ U^\circ$，即 $\mathcal D_X\cong U^\circ/J_0$。
- $\mathfrak b^\circ$ 是 $\mathfrak g^\circ$ 的理想层，且 $\mathfrak b^\circ$ 上的换位子是 $\mathcal O_X$-线性的——正是这条使 $J_0$ 成为双边理想，商才是环层。

## 公式

$$(f\otimes\xi)(g\otimes\eta)=f\tau(\xi)g\otimes\eta+fg\otimes\xi\eta$$

$$[f\otimes\xi,g\otimes\eta]=f\tau(\xi)g\otimes\eta-g\tau(\eta)f\otimes\xi+fg\otimes[\xi,\eta]$$

$$F_pU^\circ=\mathcal O_X\otimes_k F_pU(\mathfrak g)$$

$$F_0U^\circ=\mathcal O_X,\qquad F_1U^\circ=\mathcal O_X\oplus\mathfrak g^\circ$$

$$\mathcal D_X\cong U^\circ/\mathfrak b^\circ U^\circ$$

## 相关定理

### 第 1 章引理 2.1（$\tau:\mathfrak g^\circ\to T_X$ 满）

态射 $\tau:\mathfrak g^\circ\to T_X$ 是满态射。

证明状态：`complete`

1. $\mathcal O_X$-模 $\mathfrak g^\circ$ 与 $T_X$ 都局部自由，故只需证 $\tau$ 在任意 $x\in X$ 的几何纤维上给出的线性映射 $T_x(\tau):\mathfrak g\to T_xX$ 是满射。
   - 为什么：局部自由层的态射若在每根纤维上满则本身满；纤维上的映射就是 $T_x(\tau)$。
2. $T_x(\tau)$ 是 $G$ 在 $X$ 上作用的微分；$G$ 在 $X$ 上可迁，故轨道映射 $G\to X$ 在单位元处的切映射 $\mathfrak g\to T_xX$ 满。
   - 为什么：可迁作用的轨道是开集，故切映射满；而 $T_x(\tau)$ 就是这条切映射与 $G\to X$ 的复合。
3. 于是每个纤维上 $\tau$ 满，故 $\tau$ 是满态射。
   - 为什么：第 1 步的归约。

### 第 1 章命题 2.2（$\mathcal D_X\cong U^\circ/J_0$）

(i) 态射 $\tau:U^\circ\to\mathcal D_X$ 是满态射。(ii) $\tau:U^\circ\to\mathcal D_X$ 的核是理想层 $J_0=\mathfrak b^\circ U^\circ$。

证明状态：`complete`

1. (i) $\mathcal D_X$ 作为 $k$-代数层由 $\mathcal O_X$ 与 $T_X$ 生成；由第 1 章引理 2.1，$\tau(\mathfrak g^\circ)=T_X$，而 $\tau(\mathcal O_X)=\mathcal O_X$，故 $\tau(U^\circ)=\mathcal D_X$。
   - 为什么：环层同态的像包含全部生成元即等于整个层；$\tau$ 在 $F_1U^\circ=\mathcal O_X\oplus\mathfrak g^\circ$ 上已满。
2. (ii) 先看包含 $J_0\subset\ker\tau$：$\mathfrak b^\circ$ 的元素被 $\tau$ 送到 $0$，故其生成的理想 $J_0$ 整个落入核。
   - 为什么：核是 $U^\circ$ 的双边理想，理想由生成元生成，生成元的像为 0 则整个理想在核中。
3. 反向：化到几何纤维。$T_x(U^\circ)=U(\mathfrak g)$，$T_x(\mathcal D_X)=U(\mathfrak g)/\mathfrak b_xU(\mathfrak g)$，而 $T_x(\tau)$ 的核正是 $\mathfrak b_xU(\mathfrak g)$——它就是 $T_x(J_0)$。
   - 为什么：$\mathfrak b_x$ 是 $\mathfrak g$ 中被 $\tau$ 在 $x$ 处杀死的部分，由 PBW，$U(\mathfrak g)$ 中由它生成的左理想正是这个核；这是讲义在第 1 章命题 2.2 的证明中直接使用的纤维描述。
4. $J_0$ 与 $\ker\tau$ 的几何纤维处处相等，两者都拟凝聚，故相等。
   - 为什么：拟凝聚 $\mathcal O_X$-模的态射由纤维上的核决定（$X$ 上拟凝聚层的局部化—纤维判据）。

## 易错点

- 条件 (iii)（$\alpha$ 是 $G$-模态射）不能省：没有它，$\alpha(\mathfrak b^\circ)\subset\mathcal O_X$ 的论证不成立，参数 $\lambda$ 也无从定义。
- $U^\circ$ 的乘法不是 $\mathcal O_X$-双线性的（含 $\tau(\xi)g$ 项），所以 $U^\circ$ 不是 $\mathcal O_X$-代数，而是带 $\mathcal O_X$-模结构的 $k$-代数层；不要把它当作 $\mathcal O_X\otimes U(\mathfrak g)$ 的 $\mathcal O_X$-代数。
- $\mathfrak b^\circ=\ker(\tau:\mathfrak g^\circ\to T_X)$ 是「向量场提升的核」，与 $\mathcal O_X$ 在 $U^\circ$ 中的像无关；不要与 $\ker(i:\mathcal O_X\to\mathcal D)$ 混淆。
- 第 1 章命题 2.2 的商是 $U^\circ/\mathfrak b^\circ U^\circ$，不是 $U^\circ/\mathfrak b^\circ$：只有理想 $J_0$ 的商才是环层。

## 相关卡

- `mloc/concept/d-lambda-sheaf`
- `mloc/concept/borel-and-nilpotent-radical-sheaves`
- `mloc/concept/twisted-sheaf-of-differential-operators`
- `dmod/concept/dz-structure-sheaf`

## 出处

- Miličić, Localization and Representation Theory of Reductive Lie Groups · 第 1 章 §2 齐性扭微分算子层 · p.[10, 11]（PDF [14, 15]） · `源码/chapters/ch01.tex:373-401（三元组的定义与 $U^\circ$ 的构造）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · 第 1 章 §2 齐性扭微分算子层 · p.[11, 12]（PDF [15, 16]） · `源码/chapters/ch01.tex:403-432（第 1 章引理 2.1、第 1 章命题 2.2）`
