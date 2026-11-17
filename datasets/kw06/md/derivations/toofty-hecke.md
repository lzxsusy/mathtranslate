# 't Hooft 算子的 Hecke 修改：U(1) 到 U(N)

> `kw/deriv/toofty-hecke` · 轨道 E · Langlands 与翻译器 · 状态 dev · 6 步

> **要回答的问题**：'t Hooft 算子怎样作用在 Higgs 丛上，为什么其磁荷正好就是 Hecke 修改的权？

## 一句话

't Hooft 算子在 Higgs 丛上实现 Hecke 修改：$U(1)$ 时 $L_+\cong L_-\otimes O(p_0)^m$，$U(N)$ 时逐 $L_i\mapsto L_i\otimes O(p_0)^{m_i}$；磁荷数组 ${}^L\!w$ 同时是 Hecke 权与仿射 Grassmannian 中 Schubert 胞腔的标号。

## 目标

从 $U(1)$ 到 $U(N)$ 逐级算出 't Hooft 算子的 Hecke 作用，并把磁荷识别为 ${}^LG$ 的最高权。

## 前提

- B p.130 eq (9.10)：$U(1)$ 't Hooft 算子的奇点 $F\sim(\ii m/2)\star_3 d(1/|x-p|)$。
- B p.132 eq (9.12)：$U(N)$ 时 $F$ 取对角值 $\mathrm{diag}(m_1,\dots,m_N)$。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 把静态 't Hooft 算子插在 $y=y_0$、$z=p_0$，其奇点附近的曲率是单极子型 $F\sim(\ii m/2)\star_3 d(1/\|\vec x-p\|)$；包围它的球面 $S$ 上 $\int_S c_1(L)=m$。 | 这个积分把「磁荷」变成拓扑数，从而与全纯丛的度数直接对应。 | `B p.130 eq (9.10)` | A·原文明确写了 |
| 2 | $U(1)$ 情形：$L_+$ 与 $L_-$ 在 $p_0$ 外同构，故 $L_+\otimes L_-^{-1}=O(p_0)^q$；由 $C_+-C_--S$ 是边界得 $q_+=m+q_-$，于是 $L_+\cong L_-\otimes O(p_0)^m$。 | 用同调边界关系把球面上的磁荷与两个截面的度数差联系起来，是本节最直接的计算。 | `B p.131` | A·原文明确写了 |
| 3 | $U(N)$ 情形：'t Hooft 算子由 $\rho:U(1)\to U(N)$ 的共轭类给出，取 $\rho(e^{\ii\alpha})=\mathrm{diag}(e^{\ii m_1\alpha},\dots,e^{\ii m_N\alpha})$，在 Lie 代数层面对应 $\mathrm{diag}(m_1,\dots,m_N)$（(9.11)），曲率也取对角形（(9.12)）。 | 对角化后问题化归为 $N$ 个 $U(1)$ 分量，每个分量独立地作同样的 Hecke 修改。 | `B p.131 eq (9.11)` | A·原文明确写了 |
| 4 | $E_y$ 在 $p_0$ 附近分裂为 $\oplus_i L_i$，'t Hooft 算子的作用就是逐项 $L_i\mapsto L_i\otimes O(p_0)^{m_i}$；这与通常的 Hecke 算子定义一致。 | 这一步给出全文的核心链接：'t Hooft 算子的规范场奇点等价于丛的 Hecke 修改。 | `B p.132` | A·原文明确写了 |
| 5 | 群论翻译：${}^LG$ 的表示对应 't Hooft 算子，最高权 ${}^L\!w$ 即磁荷数组；基本表示给 ${}^L\!w^{(1)}=(1,0,\dots,0)$，$\wedge^kV$ 给 ${}^L\!w^{(k)}=(1,\dots,1,0,\dots,0)$。 | 这样磁荷不仅能排序，还能按 ${}^LG$ 的表示论分类，才能与 Langlands 对偶对上。 | `B p.132 eq (9.13)` | A·原文明确写了 |
| 6 | 固定点 $p_0$ 上 $T({}^L\!w;p_0)=T(1;p_0)$ 的幂，不同点的算子交换；换成 $SU(N)$ 或一般 $G$ 时还需 $\sum_i m_i=0$ 以保持行列式（拓扑）不变。 | 前者解释了为什么 $U(N)$ 侧给出交换代数；后者说明 $U(N)$ 与 $SU(N)$ 的差别只在整体 $U(1)$ 因子。 | `B p.131` | A·原文明确写了 |

## 结论

't Hooft 算子在 Higgs 丛上的作用就是 Hecke 修改：$U(1)$ 时 $L_+\cong L_-\otimes O(p_0)^m$，$U(N)$ 时按 $\rho$ 的对角化逐项 $L_i\mapsto L_i\otimes O(p_0)^{m_i}$。磁荷数组 ${}^L\!w$ 正是 ${}^LG$ 的最高权，因此 't Hooft 算子按 ${}^LG$ 的表示分类，这也是它与 Hecke 算子对应的根源。

## 缺口

- 非阿贝尔情形下 't Hooft 算子的拓扑分类本身并不简单，本文改用 Hecke 修改作定义，未独立分类（B p.130-132）。

## 最容易讲错的地方

- $U(1)$ 的 $m$ 与 $U(N)$ 的 $m_i$ 是同一套整数，但 $U(N)$ 顺序约定 $m_1\ge\dots\ge m_N$，$SU(N)$ 还要 $\sum m_i=0$。
- $L_+\cong L_-\otimes O(p_0)^m$ 只是 $U(1)$ 的结论；$U(N)$ 必须逐 $L_i$ 改写，不能整体乘一个 $O(p_0)$。

## 相关卡

[Hecke 修改空间、仿射 Grassmannian 与 Schubert 胞腔](../derivations/grassmann-schubert.md) · [特征膜：XB ≅ B ⊗ V 与同时对角化](../derivations/eigenbranes.md) · ['t Hooft 算子](../concepts/thooft-operator.md) · [Hecke 算子](../concepts/hecke-operator.md)

## 出处（印刷页）

- B p.128–134（B p.132）

> 说明：steps 的 provenance 分布：A×6（共 6 步）；gaps 1 条、pitfalls 2 条。
