# 仿射 Grassmannian

> `kw/concept/affine-grassmannian` · 轨道 E · Langlands 与翻译器 · 状态 dev

> **先自测**：仿射 Grassmannian 为什么参数化 Hecke 修改，Schubert 胞腔又对应什么？

## 一句话

把丛在一点外固定平凡化后，Hecke 修改的空间就是仿射 Grassmannian $\mathrm{Gr}_G=G_{\mathbb C}((z))/G_{\mathbb C}[[z]]$；权 $^Lw$ 标号其 Schubert 胞腔。

## 定义

仿射 Grassmannian 是形式圆盘上 $G_{\mathbb C}$-丛平凡化的空间：$\mathrm{Gr}_G=G_{\mathbb C}((z))/G_{\mathbb C}[[z]]$，本文也写成 $G_{\mathbb C}(X)/G_{\mathbb C}(\mathcal O)$，其中 $X$ 是 $C$ 上的有理函数域、$\mathcal O$ 是 $p_0$ 处的局部环。它参数化在一点外有固定平凡化的丛，即 Hecke 修改。

**记号**：$X$：$C$ 上有理函数域；$\mathcal O$：$p_0$ 处局部环；$^Lw$：$^L G$ 的权。

## 要点（为什么需要它）

1. 它把 Hecke 修改参数化：权 $^Lw$ 的修改对应点 $g_{ji}=z^{-m_j}\delta_{ji}$ 在 $G_{\mathbb C}(\mathcal O)$ 下的轨道。
2. 它无穷维，Schubert 胞腔按 $^L G$ 的权分叶，闭包一般奇异——这解释了 §10 的轨道闭包与 IC 层。
3. 维数 $\Delta_{^Lw}=\sum_{i<j}(a_i-a_j)$ 是修改的自由度，也等于 Bogomolny 解的指标。
4. 它是 §9 与 §10 的共同舞台：一边是丛的修改，一边是单极子解的空间。

## 核心公式

$$
$\mathrm{Gr}_G=G_{\mathbb C}((z))/G_{\mathbb C}[[z]]=G_{\mathbb C}(X)/G_{\mathbb C}(\mathcal O)$$g_{ji}(z)=z^{-m_j}f_{ji}(z),\qquad \dim Y({}^Lw)=\Delta_{{}^Lw}=\sum_{i<j}(a_i-a_j)$
$$

$$
$g_{ji}(z)=z^{-m_j}f_{ji}(z),\qquad \dim Y({}^Lw)=\Delta_{{}^Lw}=\sum_{i<j}(a_i-a_j)$
$$

## 定理与证明（或缺口）

### 仿射 Grassmannian 参数化 Hecke 修改

$\mathbb{CP}^1$ 上 rank-$N$ 丛连同 $p_0$ 外的固定全纯平凡化由过渡函数 $g(z)$ 决定；模去 $p_0$ 邻域的平凡化（即 $G_{\mathbb C}(\mathcal O)$）后正是 $\mathrm{Gr}_G$，权 $^Lw=(m_1,\dots,m_N)$ 的修改对应 $g_{ji}=z^{-m_j}\delta_{ji}$ 的轨道。

> 证明状态：**sketch**。原文 p.146 只给同构陈述与过渡函数的直观说明，未证严格等价；一般 $G$ 的 (9.34) 也是陈述。

出处：`B p.146 eq (9.31)`

## 常见误解

- 把仿射 Grassmannian 当成有限维 Grassmannian $\mathrm{Gr}(k,N)$；它无穷维且非紧。
- 把 Schubert 胞腔与 Schubert 闭链混淆；胞腔光滑，闭包一般奇异。
- 弄错权所在群：$^Lw$ 是 $^L G$ 的权，却用来标号 $G$ 的修改。

## 相关卡

[Hecke 算子](../concepts/hecke-operator.md) · [Hecke 特征层](../concepts/hecke-eigensheaf.md) · [Hecke 修改空间、仿射 Grassmannian 与 Schubert 胞腔](../derivations/grassmann-schubert.md) · [Langlands 对偶群](../concepts/langlands-dual-group.md)

## 出处（印刷页）

- B p.146（B p.146 eq (9.29)）
- B p.148（B p.148 eq (9.34)）

> 说明：A=原文 p.146 的同构与 (9.29)–(9.31)、p.148 的 (9.34)；B=把过渡函数读成 $\mathrm{Gr}_G$ 的点；C=维数公式与 Schubert 闭包奇异的评注。
