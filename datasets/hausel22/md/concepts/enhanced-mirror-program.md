# 总览：幂零锥尖端的增强镜像对称纲领

> `hausel22/concept/enhanced-mirror-program` · 轨道 总览 · 状态 dev

> **先自测**：整篇文章到底证明了什么，又猜了什么？

## 一句话

本文第一部分综述 Langlands 对偶 Hitchin 系统之间的镜像对称，第二部分在幂零锥上引入重数代数并猜想其镜像对应物。

## 定义

论文分两部分。第一部分（§1–§2）综述 Langlands 对偶群 $\G,\G^\vee$ 的 Hitchin 系统之间的镜像对称现象：拓扑镜像对称（Hodge 数，猜想 2.1）、同调镜像对称（式 (2.4)）、SYZ 镜像对称（式 (2.1)–(2.3)），以及 Kapustin–Witten 的增强镜像对称（HMS + 膜匹配 + Wilson–Hecke 交换）。第二部分（§3）在 Hitchin 映射的 $0$-纤维即整体幂零锥上作整体检验：引入非常稳定 Higgs 丛、等变重数 $m_\calE(t)$ 与局部重数代数 $Q_\calE$，证明它们的分次、Gorenstein、Poincaré 对偶性质（定理 3.9），在 Hecke 情形算出 $Q_\delta\cong\prod H^*(\Gr(i,n))^{m_i}$（定理 3.10），并对 wobbly 情形提出猜想 3.12、以拉格朗日闭包（定理 3.18）与几何 Satake 猜想 3.19 收尾。

**记号**：$\M_\Dol,\M_\DR$；$\calA$；$\T$；$m_\calE(t)$；$Q_\calE$；$\Gr$。

## 要点（为什么需要它）

1. 已证的：定理 3.1–3.6、3.9、3.10、3.18（多数引自 [HH] 与 [HH1]）；猜想的：猜想 2.1（拓扑镜像对称，综述）、猜想 3.12 的一般 $\mu$ 版本（注 3.13）、猜想 3.19（几何 Satake）。
2. 纲领的检验策略是「在幂零锥上验证」：一般点处的 Fourier–Mukai 检验太弱，只有 $0$-纤维才给出整体约束。
3. 工具是 $\T$-等变 Euler 型 $\chi_\T$：它把无穷维的 Ext 群压成 $\C((t))$ 里的元素，从而可以比较。
4. 三条主线互相咬合：非常稳定 ⇒ 重数多项式（3.5）；重数多项式 = Poincaré 多项式（3.9）；Poincaré 多项式 = Grassmann 上同调（3.10）。

## 核心公式

$$
$$\chi_\T(\mathscr{S}(\calF),\mathscr{S}(\calG))=\chi_\T(\calF,\calG)$$$$Q_\delta\cong\prod_{i=1}^{n-1}H^*(\Gr(i,n);\C)^{m_i}\qquad(\delta_1+\cdots+\delta_{n-1}\ \text{既约})$$
$$

$$
$$Q_\delta\cong\prod_{i=1}^{n-1}H^*(\Gr(i,n);\C)^{m_i}\qquad(\delta_1+\cdots+\delta_{n-1}\ \text{既约})$$
$$

## 定理与证明（或缺口）

### 文章的结构（已证 vs 猜想）

已证：定理 3.1（BB 性质）、3.2/3.3（非常稳定的等价刻画）、3.5（重数多项式）、3.6（$t$-二项式系数积）、3.9（重数代数的性质）、3.10（Grassmann 乘积）、3.18（闭包）；猜想：2.1（拓扑镜像对称）、3.12 的一般 $\mu$ 版本（注 3.13）、3.19（几何 Satake）。

> 证明状态：**sketch**。「已证/猜想」的划分是我们按原文的定理环境与猜想环境整理的，原文没有这样一张表。

出处：`A p.2228`

## 常见误解

- 把猜想 2.1 说成本文证明的定理：它只是综述，证明在 [HT]/[GWZ]/[Maulik–Shen]。
- 把定理 3.12 当成无条件定理：它带假设 $\calE_{\delta^\mu_c}\in\M^{s\T}$，且其一般 $\mu$ 版本仍是猜想（注 3.13）。
- 把第二部分当成「应用」：它是新的数学（非常稳定、重数代数、拉格朗日闭包），不是第一部分的应用。
- 把 $\chi_\T$ 当成普通 Euler 特征：它取值在 $\C((t))$，带 $\T$-权的分次信息。

## 相关卡

[镜像对称（三个方面）](../concepts/mirror-symmetry.md) · [增强镜像对称](../concepts/enhanced-mirror-symmetry.md) · [局部重数代数 $Q_\calE$](../concepts/local-multiplicity-algebra.md) · [拉格朗日闭包 $\overline{\overline{W^+_\calE}}$](../concepts/lagrangian-closure.md)

## 出处（印刷页）

- A p.2228（A p.2228）
- A p.2235（A p.2235）

> 说明：A=摘要的两部分划分与 §3 首段的纲领；B=「已证 vs 猜想」的清单是我们按定理/猜想环境整理的；C=「三条主线互相咬合」的归纳是我们的。最没把握处：定理 3.6 与 3.12 的归属（哪些在 [HH] 已证、哪些在 [HH1]），原文只给引用不给页码。
