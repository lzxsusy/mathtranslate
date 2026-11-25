# 用 V_M 表示的相交配对

> `grassmann/concept/intersection-pairing-via-vm` · 轨道 4 · 奇异模空间的相交配对 · 状态 draft

> **先自测**：相交上同调一般没有环结构，凭什么说它的配对「由等变上同调的杯积给出」？

## 一句话

平衡作用时存在截面 V_M 与 IH 同构，互补次数的两个 V_M 类之积等于最高次类乘配对值，于是相交数化成等变上同调的杯积。

## 定义

设连通约化群 $G$ 作用在 $M$ 上，$M^{ss}$ 为半稳定点集，$\kappa_M:H_G^*(M)\to IH^*(M//G)$ 为 Kirwan 映射。若作用平衡，存在向量子空间 $V_M\subset H_G^*(M^{ss})$ 使 $\kappa_M^{ss}:V_M\to IH^*(M//G)$ 是双射（定理 5.4）。设 $\sigma_1,\sigma_2\in V_M$ 具有**互补次数**，即 $\deg\sigma_1+\deg\sigma_2=\dim_{\mathbb{R}}(M//G)$，则 $\sigma_1\cup\sigma_2\in V_M$，且存在 $V_M$ 中的最高次类 $\tau$ 使
$$\sigma_1\cup\sigma_2=\tau\,\langle\sigma_1,\sigma_2\rangle,$$
其中 $\langle\cdot,\cdot\rangle$ 是相交上同调中的 Poincaré 配对（定理 5.5）。

**记号约定**：$H_G^*$ 取复系数等变上同调；$\tau$ 是 $V_M$ 的最高次类（$M//G$ 的基本类在 $V_M$ 中的代表）；$\langle\cdot,\cdot\rangle$ 是 $IH$ 的 Poincaré 配对；$\kappa^{ss}_M=\kappa_M|_{M^{ss}}$。

## 要点（为什么需要它）

- 相交同调只有 Poincaré 配对、一般没有环结构（§4），所以「两个 IH 类相乘」本身无定义；$V_M$ 是让杯积封闭的那个截面。
- 定理 5.5 把抽象配对换成可算的量：$\langle\kappa(\alpha),\kappa(\beta)\rangle=\int_{M(n,d)^s}\eta$，其中 $\eta$ 是紧支在稳定部分、表示 $\alpha\beta$ 的最高次形式。
- 互补次数的假设不能省：次数不互补时 $\sigma_1\cup\sigma_2$ 可能跑出 $V_M$，$\kappa^{ss}$ 就不再对应 IH 类。
- $M(n,d)$ 情形 $V_M$ 有显式刻画：对每个稳定子单位分支 $H$，$\Phi_H(\xi)\in H^*_{N_0^H/H}(Y_H)\otimes H_H^{<n_H}(\mathrm{pt})$，$n_H=\tfrac12\dim(W_p//H)$。
- 定理 5.4 的双射与定理 5.5 的乘积公式合起来，才是「IH 的配对可由等变杯积计算」的完整合法性来源。

## 关键公式

$$
\kappa_M^{ss}:V_M\xrightarrow{\ \sim\ }IH^*(M//G)
$$

$$
\sigma_1\cup\sigma_2=\tau\,\langle\sigma_1,\sigma_2\rangle\qquad(\deg\sigma_1+\deg\sigma_2=\dim_{\mathbb{R}}M//G)
$$

$$
V_M=\{\xi\in H_G^*(M^{ss}):\Phi_H(\xi)\in H^*_{N_0^H/H}(Y_H)\otimes H_H^{<n_H}(\mathrm{pt})\ \ \forall H\}
$$

## 定理与证明（或缺口）

### $V_M$ 中的杯积给出相交配对（定理 5.5）

若 $\sigma_1,\sigma_2\in V_M$ 且次数互补，则 $\sigma_1\cup\sigma_2=\tau\langle\sigma_1,\sigma_2\rangle$，其中 $\tau$ 是 $V_M$ 中的最高次类，$\langle\cdot,\cdot\rangle$ 是相交上同调中的配对。等价地，$\kappa_M$ 把等变上同调的杯积送到 IH 的配对。

**证明状态：只引出处，原书不重证**


出处：中译 p.77（§5 定理 5.5，引 Jeffrey–Kiem–Kirwan–Woolf, Transform. Groups 8 (2003) Thm 14）

## 易错点

- 以为 $\kappa$ 是环同态：$\kappa(\sigma_1\cup\sigma_2)$ 一般不等于 $\kappa(\sigma_1)\cup\kappa(\sigma_2)$（右边根本没定义）；只有限制在 $V_M$ 且次数互补时才有定理 5.5 的等式。
- 把 $\tau$ 当成 $H_G^*(\mathrm{pt})$ 的生成元：$\tau$ 是 $V_M$ 的最高次类，次数等于 $\dim_{\mathbb{R}}(M//G)$，与 $M$ 的维数无关。
- 验证 $\sigma_1\cup\sigma_2\in V_M$ 时只查一个稳定子层：注 1 的封闭性要对所有 $H$ 同时成立，漏层时乘积会掉出 $V_M$。

## 相关卡

- [平衡作用](../concepts/balanced-action.md)
- [配对的留数公式](../concepts/residue-formula-for-pairings.md)
- [整体奇异格拉斯曼流形](../concepts/global-singular-grassmannian.md)

## 出处

- ch4 §5 定理 5.5 与注 1；中译 p.78（英文 PDF p.84），源码 `chapters/ch04.tex:198`
