# Hecke 修改空间、仿射 Grassmannian 与 Schubert 胞腔

> `kw/deriv/grassmann-schubert` · 轨道 E · Langlands 与翻译器 · 状态 dev · 6 步

> **要回答的问题**：Hecke 修改空间是什么几何对象，其维数与紧化如何由权 ${}^L\!w$ 决定？

## 一句话

Hecke 修改空间是仿射 Grassmannian $Gr_N=GL(N,\mathbb C((z)))/GL(N,\mathbb C[[z]])$ 中对应的 Schubert 胞腔，维数 $\Delta_{{}^Lw}=\sum_{i<j}(a_i-a_j)$；紧化需加入关联表示，minuscule 权给光滑紧空间。

## 目标

把 Hecke 修改实现为仿射 Grassmannian 的 Schubert 胞腔，算出维数并说明紧化与 minuscule 情形。

## 前提

- B p.146：$Gr_N\cong GL(N,\mathbb C((z)))/GL(N,\mathbb C[[z]])$ 是仿射 Grassmannian。
- B p.146 eq (9.30)：$g_{ji}(z)=z^{-m_j}f_{ji}(z)$ 给出权 $m_i$ 的 Hecke 修改。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | Hecke 修改是带同构 $\sigma:E\cong E_-$（在 $p_0$ 外）的丛 $E$；等价类由 $p_0$ 附近的局部平凡化之差 $g(z)$ 决定，$g$ 是 $C^*$ 上取值的 $GL(N,\mathbb C)$ 函数。 | 取局部平凡化之差就把「丛+同构」的数据压缩成一个矩阵值函数，从而可以用环路群的语言描述。 | `B p.145` | A·原文明确写了 |
| 2 | 最简单选择 $f_{ji}(z)=\delta_{ji}$ 给出 $g_{ji}(z)=z^{-m_j}\delta_{ji}$；一般 $f_{ji}$ 给出 $g_{ji}=z^{-m_j}f_{ji}$，其全体构成 $GL(N,X)/GL(N,O)\cong Gr_N$。 | 这说明所有 Hecke 修改都落在同一个商空间里，$m_i$ 只标出其中一族点。 | `B p.146 eq (9.30)` | A·原文明确写了 |
| 3 | 固定权 ${}^L\!w$ 的修改给出 $GL(N,O)$ 在 $Gr_N$ 中的一条轨道 $Y({}^L\!w)$，称为 Schubert 胞腔；所有轨道都由此得到。 | 轨道分解是 $Gr_N$ 的胞腔分解，Hecke 修改空间就是其中一个胞腔。 | `B p.147` | A·原文明确写了 |
| 4 | 维数由权差给出：$\Delta_{{}^Lw}=\sum_{i<j}(a_i-a_j)$，其中 ${}^L\!w=(a_1\ge\dots\ge a_N)$。 | 每一对 $(i,j)$ 贡献一个可以独立调节的自由度，求和即为总维数；这与 10.1 的指标计算一致。 | `B p.144 eq (9.25)` | A·原文明确写了 |
| 5 | 紧化：当 $m_i\ge m_j+2$ 时自然紧化必须加入 $(m_i-1,m_j+1)$ 等关联权，即 $SU(2)$ 子群退化产生的 Hecke 修改；minuscule 权没有关联表示，故其空间光滑紧。 | 胞腔的闭包包含更低维胞腔，这正是 't Hooft 算子「混合」的几何来源。 | `B p.143` | A·原文明确写了 |
| 6 | 一般群：$Gr_G=G_\mathbb C(X)/G_\mathbb C(O)$，$\rho_\mathbb C:\mathbb C^*\to G_\mathbb C$ 的轨道 $Y(\rho)$ 就是 Hecke 修改空间。 | 这是 $GL(N)$ 构造在任意约化群上的推广，使结论可用于几何 Langlands 的一般 $G$。 | `B p.148 eq (9.34)` | A·原文明确写了 |

## 结论

Hecke 修改空间是仿射 Grassmannian $Gr_N$ 中的 Schubert 胞腔 $Y({}^L\!w)$，由局部平凡化之差 $g_{ji}(z)=z^{-m_j}f_{ji}(z)$ 描述。其维数为 $\Delta_{{}^Lw}=\sum_{i<j}(a_i-a_j)$，与 Bogomolny 指标一致。紧化必须加入关联权；minuscule 权（如 $\wedge^kV$）无关联表示，故 Hecke 修改空间光滑紧。

## 缺口

- 本文声明不使用仿射 Grassmannian 框架，维数公式另由第 10 节的指标论证（B p.145、p.155），两条路线未在正文中逐项对照。

## 最容易讲错的地方

- $\Delta_{{}^L\!w}=\sum_{i<j}(a_i-a_j)$ 中 $a_i$ 按降序排列；顺序弄反会得到负的「维数」。
- 紧化是取胞腔的闭包，单个胞腔本身并不紧；minuscule 情形例外地光滑紧。

## 相关卡

['t Hooft 算子的 Hecke 修改：U(1) 到 U(N)](../derivations/toofty-hecke.md) · [单极子冒泡、辛商与 OPE 代数](../derivations/bubbling-ope.md) · [仿射 Grassmannian](../concepts/affine-grassmannian.md) · [Hitchin 模空间](../concepts/hitchin-moduli.md)

## 出处（印刷页）

- B p.143–148（B p.144 eq (9.25)）

> 说明：steps 的 provenance 分布：A×6（共 6 步）；gaps 1 条、pitfalls 2 条。
