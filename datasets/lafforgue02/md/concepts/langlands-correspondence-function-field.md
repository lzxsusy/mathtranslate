# 函数域上的 Langlands 对应（$\mathrm{GL}_r$）

> `lafforgue02/concept/langlands-correspondence-function-field` · 轨道 A · 镜像对称与几何 Langlands · 状态 dev

> **先自测**：讲义要证的 Langlands 对应，其 (i)$_r$ 与 (ii)$_r$ 分别断言什么？

## 一句话

对函数域 $F=\mathbb F_q(X)$：$\mathrm{GL}_r$ 的尖点自守表示与 $r$ 维 $\ell$-进 Weil 表示一一对应，且逐位点匹配局部对应与 $L$、$\varepsilon$ 因子。

## 定义

记 $\{\pi\}_r$ 为 $\mathrm{GL}_r(\mathbb A_F)$ 的尖点自守表示的等价类，$\{\sigma\}_r$ 为 $W_F\to\mathrm{GL}_r(\overline{\mathbb Q}_\ell)$ 的不可约连续表示的等价类。(i)$_r$ 断言二者之间存在双射 $\pi\leftrightarrow\sigma_\pi$；(ii)$_r$ 断言该双射在每个位点与局部 Langlands 对应相容，并保持 $L$ 因子与 $\varepsilon$ 因子。

**记号**：$W_F$ 是 $F$ 的 Weil 群；$\sigma_\pi$ 也记 $\sigma$；$q'=q^{r}$ 相关归一化见原文。

## 要点（为什么需要它）

1. 对应是「整体双射 + 逐位点匹配」两部分：(i)$_r$ 管整体，(ii)$_r$ 管局部匹配，缺一不可。
2. 讲义对 $r$ 归纳证明：$r=1$ 是类域论；归纳步骤把 $r-1$ 的对应当作已知，用迹公式把 $r$ 维情形逼出来。
3. 证明的最终输出不是一个抽象双射，而是把想要的表示从 chtouca 的上同调里**分离**出来：本质部分同构于 $\bigoplus_\pi\pi\otimes q'^*\sigma_\pi\otimes q''^*\tilde\sigma_\pi(1-r)$。
4. 两件「已知」工具反复出现：Piatetski-Shapiro 的强重数一（(ii)$_r$ 的唯一性）与 Chebotarev 密度定理（从迹函数回到表示）。

## 核心公式

$$
$\{\pi\}_r\longleftrightarrow\{\sigma\}_r$，$\pi\mapsto\sigma_\pi$$H^{2r-2}_{\mathrm{ess}}\cong\bigoplus_{\pi\in\{\pi\}^N_r}\pi^{K_N}\otimes q'^*\sigma_\pi\otimes q''^*\tilde\sigma_\pi(1-r)$$\mathrm{Tr}(\sigma_\pi(\mathrm{Frob}_x))=q^{(r-1)\deg x}\,\mathrm{Tr}(\pi_x)$（未分歧处，$1-r$ 扭）
$$

$$
$H^{2r-2}_{\mathrm{ess}}\cong\bigoplus_{\pi\in\{\pi\}^N_r}\pi^{K_N}\otimes q'^*\sigma_\pi\otimes q''^*\tilde\sigma_\pi(1-r)$
$$

$$
$\mathrm{Tr}(\sigma_\pi(\mathrm{Frob}_x))=q^{(r-1)\deg x}\,\mathrm{Tr}(\pi_x)$（未分歧处，$1-r$ 扭）
$$

## 定理与证明（或缺口）

### Langlands 对应（函数域，$\mathrm{GL}_r$）

存在双射 $\{\pi\}_r\leftrightarrow\{\sigma\}_r$，$\pi\mapsto\sigma_\pi$，使得对每个位点 $v$ 有 $\pi_v\leftrightarrow\sigma_{\pi,v}$，且 $L(\pi,s)=L(\sigma_\pi,s)$、$\varepsilon(\pi,s)=\varepsilon(\sigma_\pi,s)$。

> 证明状态：**sketch**。本卡只复述讲义 §I 的陈述与路线；完整证明在 [Lafforgue 2002]，讲义本身不证。

出处：`A p.3`

## 常见误解

- 尖点性不能省：去掉「尖点」后双射不成立，讲义在本章开头就把 $\{\pi\}_r$ 限定为尖点表示。
- $\sigma_\pi$ 是 $\ell$-进表示、取在 $\overline{\mathbb Q}_\ell$ 上；$\ell\ne p$ 的选取在讲义中固定，不可随 $\pi$ 变。

## 相关卡

[Drinfeld chtouca（带水平结构）](../concepts/drinfeld-chtouca.md) · [从截断读到 Langlands 对应：迹公式如何给出 $\sigma_\pi$](../derivations/trace-from-truncation.md) · [配对 $L$-函数（fonction $L$ de paires）](../concepts/lfunction-pairs.md)

## 出处（印刷页）

- A p.3–4（A p.3）

> 说明：(i)$_r$/(ii)$_r$ 的陈述取讲义 p.3–4。最后一条 formula 的 $1-r$ 扭归一化按讲义 p.9 的分解式写法；局部因子公式的精确归一化讲义未逐条写出，属上下文推断（B 级）。
