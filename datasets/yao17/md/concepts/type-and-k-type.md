# 类型（type）、K-型与极小 K-型；Bushnell–Kutzko 型的区别

> `yao17/concept/type-and-k-type` · 轨道 惯性 Langlands 与类型 · 状态 dev

> **先自测**：类型与 K-型的差别只在一个「当且仅当」上，为什么这个差别是本质的？Bushnell–Kutzko 型又放宽了什么？

## 一句话

σ 是 (L,ς) 的类型，若「π|_K 含 σ ⇔ π∈R(L,ς)」；只要求单向的是 K-型，π 上维数最小者为极小 K-型。

## 定义

设 $\sigma$ 是 $K$ 的光滑不可约表示，$s=(L,\varsigma)\in\mathcal B(\GL_n)$。(1) $\sigma$ 是 $(L,\varsigma)$ 的类型（type），若对所有光滑不可约 $\pi$：$\pi|_K$ 含 $\sigma$ $\iff$ $\pi\in R(L,\varsigma)$；(2) $\sigma$ 是 $(L,\varsigma)$ 的 $K$-型，若对所有光滑不可约 $\pi$：$\pi|_K$ 含 $\sigma$ $\Rightarrow$ $\pi\in R(L,\varsigma)$；(3) 对 $\pi\in R(L,\varsigma)$，$\pi$ 的极小 $K$-型是出现在 $\pi|_K$ 中的、维数最小的 $K$-型。

**记号**：$K=\GL_n(\mathcal O_K)$；底本注：本文的 type 与 [9]（Paskunas）一致，而与 [4]（Bushnell–Kutzko）不同；后者称 Bushnell–Kutzko 型，是一对 $(J,\sigma)$，$J$ 为更一般的紧开子群。

## 要点（为什么需要它）

1. 「类型」是双向判据，等价于「分量 $R(L,\varsigma)$ 由单个不可约 $K$-表示 $\sigma$ 探测」；「$K$-型」只有单向，故一个分量可以有多个 $K$-型，但类型（若存在）唯一决定分量。
2. 两个概念都只依赖 $(L,\varsigma)\in\mathcal B$，与具体的 $\pi$ 无关；只有「极小 $K$-型」依赖 $\pi$ 本身——同一分量里不同的 $\pi$ 可以有不同维数的极小 $K$-型。
3. Bushnell–Kutzko 型把 $K=\GL_n(\mathcal O_K)$ 换成更一般的紧开子群 $J$，这才能覆盖「深度 $>0$」的分量；底本的 type 定义钉死在 $\GL_n(\mathcal O_K)$ 上，只能处理「$K$-型」层级。
4. 底本把类型理论放在 §4.3「最后简要讨论」，且只在 $K=\GL_n(\mathcal O_K)$ 上定义，这与 §4.2 的惯性对应形成对照：惯性类型（Galois 侧）由 $I_K$ 给出，类型（自守侧）由 $\GL_n(\mathcal O_K)$ 给出。

## 核心公式

$$
$\sigma\ \text{是}\ (L,\varsigma)\ \text{的类型}\iff \big[\pi|_K\ni\sigma\iff\pi\in R(L,\varsigma)\big]\ \forall\pi$$\sigma\ \text{是}\ (L,\varsigma)\ \text{的}\ K\text{-型}\iff \big[\pi|_K\ni\sigma\Rightarrow\pi\in R(L,\varsigma)\big]\ \forall\pi$$\sigma_{\min}\ \text{是}\ \pi\ \text{的极小}\ K\text{-型}\iff \dim\sigma_{\min}=\min\{\dim\sigma:\sigma\subset\pi|_K,\ \sigma\ \text{为}\ K\text{-型}\}$
$$

$$
$\sigma\ \text{是}\ (L,\varsigma)\ \text{的}\ K\text{-型}\iff \big[\pi|_K\ni\sigma\Rightarrow\pi\in R(L,\varsigma)\big]\ \forall\pi$
$$

$$
$\sigma_{\min}\ \text{是}\ \pi\ \text{的极小}\ K\text{-型}\iff \dim\sigma_{\min}=\min\{\dim\sigma:\sigma\subset\pi|_K,\ \sigma\ \text{为}\ K\text{-型}\}$
$$

## 常见误解

- 「$\pi|_K$ 含 $\sigma$」用的是 $K$ 上的表示包含，不是 $G$ 上的同态；$\sigma$ 可以完全不含 $G$-结构。
- 极小 $K$-型不是「所有 $K$-型里维数最小的」，而是「出现在这个具体 $\pi|_{K}$ 里的 $K$-型中维数最小的」；跨分量比较没有意义。

## 相关卡

[Bernstein 分量、惯性等价与定理 4.2 的直积分解](../concepts/bernstein-decomposition.md) · [惯性对应：Bernstein 中心 ↔ Weil–Deligne 惯性类型（引理 4.3–4.5）](../concepts/inertial-correspondence.md) · [球面 Hecke 代数与 Satake 同构、非分歧表示](../concepts/satake.md)

## 出处（印刷页）

- A p.35（A p.35）

> 说明：类型/Ｋ-型/极小 $K$-型三条定义与 Bushnell–Kutzko 的对照取自 p.35 的 4.3.1；「单向 vs 双向」的解释是我们的判断。
