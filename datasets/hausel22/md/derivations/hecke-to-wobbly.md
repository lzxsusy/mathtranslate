# Hecke 修改把仿射 Grassmannian 嵌入上行流

> `hausel22/deriv/hecke-to-wobbly` · 轨道 E · 仿射 Grassmannian 与重数代数 · 状态 dev · 5 步

> **要回答的问题**：为什么 Hecke 修改能给出 $W^+_{\delta^\mu_c}$ 与 $\calH^\mu$ 之间的同构？

## 一句话

在 $\Gr^\mu$ 中取点并作 Hecke 修改，得到 Hitchin 截面里的新点；合法修改的条件把 $\calH^\mu$ 变成 $W^+_{\delta^\mu_c}$ 上的同构。

## 目标

沿式 (3.1)、(3.5)–(3.8) 走一遍构造，说明定理 3.12(1) 的 $\calH^\mu\xrightarrow{\cong}W^+_{\delta^\mu_c}$ 从何而来。

## 前提

- $\Gr=\GL_n((z))/\GL_n[[z]]$ 是仿射 Grassmannian，$\oGr^\mu$ 是按支配权分层后的闭包。
- $\calE_0$ 是标准均匀化 Higgs 丛，$W^+_0$ 是 Hitchin 截面的点（在 $\calE_0$ 处的上行流）。
- $\calH^\mu=\{(\calE_a,V)\in W^+_0\times\Gr^\mu\mid \Phi_a|_{\Delta_c}(V)\subset V\}$（式 (3.5)）。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 取 $(\calE_a,V)\in\calH^\mu$，其中 $\calE_a$ 是 $W^+_0$ 上的点、$V\in\Gr^\mu$ 是 $c$ 处的一个子空间。 | 这是式 (3.5) 的定义；条件 $\Phi_a\|_{\Delta_c}(V)\subset V$ 保证子空间对 Higgs 场不变。 | `A p.2241 eq (3.5)` | A·原文明确写了 |
| 2 | 在 $c$ 处沿 $V$ 作反向 Hecke 修改，得到新的 Higgs 丛 $\calE_{(a,V)}$，它落在 $W^+_{\delta^\mu_c}$ 中。 | 修改后 $\calE$ 的 Harder–Narasimhan 型由 $\delta$ 记录；$\delta^\mu_c$ 的分量 $\alpha_ic$（式 (3.7)）正是每步修改落在 $c$ 处的次数。 | `A p.2241 eq (3.7)` | A·原文明确写了 |
| 3 | 修改合法的判据是 $\gamma_a g^{-1}\in\gl_n[[z]]$（式 (3.6)）：$\gamma_a$ 是 $\calE_0$ 在该点的局部矩阵、$g$ 代表 $V$。 | 只有过渡函数仍为形式幂级数矩阵，修改后才还是向量丛；这条方程定义了 $\calH^\mu$ 中 $V$ 的可行集。 | `A p.2241 eq (3.6)` | A·原文明确写了 |
| 4 | $(a,V)\mapsto\calE_{(a,V)}$ 与投影 $\calH^\mu\to W^+_0$ 构成交换图 (3.8)：$\calH^\mu\to W^+_{\delta^\mu_c}$ 与 $h$ 相容。 | Hecke 修改不改变 Higgs 场的特征多项式，故 Hitchin 映射两边一致；交换图把「修改」翻译成「上行流中的位置」。 | `A p.2241 eq (3.8)` | A·原文明确写了 |
| 5 | 当 $\calE_{\delta^\mu_c}$ 稳定时，此映射是同构：$\calH^\mu\cong W^+_{\delta^\mu_c}$。 | 两边维数相同、映射在一般点上一一对应，且 $W^+$ 是仿射空间（BB 定理 3.1：$W^+\cong T^+$），有限双有理即同构。 | `A p.2243 eq (3.8)` | A·原文明确写了 |

## 结论

Hecke 修改给出 $\calH^\mu\xrightarrow{\cong}W^+_{\delta^\mu_c}$（定理 3.12(1)），从而把重数代数的计算搬到 $\Gr^\mu$ 上的线性代数问题。

## 缺口

- 第 5 步「有限双有理即同构」的细节（为何是有限、为何是双有理）原文未写。
- 第 2 步 Hecke 修改的具体构造（局部矩阵如何拼接）原文只给局部条件 (3.6)，未给整体构造。

## 最容易讲错的地方

- $\calH^\mu$ 是 $W^+_0$ 与 $\Gr^\mu$ 的纤维积式的子簇，不是整个 $\Gr^\mu$。
- $\delta^\mu_c$ 的下标 $c$ 是曲线上的点，$\mu$ 是权；$\delta^\mu_c=(\alpha_nc,\dots,\alpha_1c)$ 的次序是反的（$\alpha_n$ 在最前）。
- Hecke 修改是「反向」的：从 $\calE_0$ 出发改出 $\calE_{\delta^\mu_c}$，方向反了会得到下行流。
- 同构只在 $\calE_{\delta^\mu_c}\in\M^{s\T}$（稳定）时成立，这是定理 3.12 的前提。

## 相关卡

[仿射 Grassmannian $\Gr$](../concepts/affine-grassmannian.md) · [非常稳定 Higgs 丛](../concepts/very-stable-higgs-bundle.md) · [局部重数代数 $Q_\calE$](../concepts/local-multiplicity-algebra.md)

## 出处（印刷页）

- A p.2241（A p.2241 eq (3.8)）

> 说明：A=原文式 (3.1)、(3.5)–(3.8) 与定理 3.12(1)；B=第 5 步的同构论证是我们按 BB 定理补的；C=对 Hecke 修改方向的说明是我们的整理。最没把握处：Hecke 修改的整体构造原文完全省略。
