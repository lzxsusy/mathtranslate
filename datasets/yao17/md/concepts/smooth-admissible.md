# 光滑表示、容许表示与反变对偶

> `yao17/concept/smooth-admissible` · 轨道 自守侧 · 状态 dev

> **先自测**：为什么容许性要按「每个开子群 H 的 V^H 有限维」来定义，而不是按「V 有限维」？反变对偶在容许表示上为什么才行为良好？

## 一句话

光滑指每个向量的稳定子开；容许再要求每个开子群的固定向量空间有限维。反变对偶 V∨ 取「稳定子开」的线性泛函。

## 定义

设 $G$ 是 $K$ 上的连通约化群，$G=G(K)$，$V$ 是 $\mathbb C$-向量空间。(1) $\pi$ 光滑，若每个 $v\in V$ 的稳定子 $\operatorname{Stab}(v)$ 在 $G$ 中开；(2) $\pi$ 容许，若它光滑且对每个开子群 $H\subset G$，$V^H$ 有限维。记 $\Rep^\infty_G$、$\Rep^{\mathrm{adm}}_G$ 为对应范畴。反变对偶：$V^\vee=\{\psi\in V^\ast:\operatorname{Stab}(\psi)\ \text{开}\}$，即 $\pi^\vee$（亦称 $\tilde V$）。

**记号**：$\pi(g)(\psi)(v)=\psi(\pi(g)^{-1}v)$；$V^H$ 是 $H$-固定向量。

## 要点（为什么需要它）

1. 光滑性的等价说法：$V=\bigcup_K V^K$，$K$ 跑遍紧开子群；容许性再加「每个 $V^K$ 有限维」。这一步把无穷维表示拆成一族有限维 $K$-表示，是所有局部计算（$K$-型、迹、Hecke 模）的入口。
2. 对固定紧开子群 $C$，$V|_C$ 半单（每个向量落在有限维不可约 $C$-表示里），故 $V=\bigoplus_{\sigma\in E(C)}V_\sigma$；容许性等价于每个同型分量 $V_\sigma$ 有限维，此时 $V|_C=\bigoplus\Sigma^{m_\sigma}$ 且重数 $m_\sigma$ 有限。
3. 反变对偶在一般光滑表示上 $V\to V^{\vee\vee}$ 不是同构；底本 Remark 明确指出容许性正是为此而设：$\pi$ 容许 $\iff$ $\pi^\vee$ 容许 $\iff$ $V\xrightarrow{\sim}V^{\vee\vee}$。
4. Gelfand–Kazhdan：$G=\GL_n(K)$、$\pi$ 不可约光滑时，$\pi^\vee\cong(g\mapsto\pi({}^tg^{-1}))$——这就是「反变」（contragradient）这个名字的来源。

## 核心公式

$$
$\pi\ \text{光滑}\iff V=\bigcup_{K}V^K\quad(K\ \text{紧开})$$\pi\ \text{容许}\iff V=\bigoplus_{\sigma\in E(C)}V_\sigma,\quad \dim V_\sigma<\infty\ \forall\sigma$$V^\vee=\{\psi\in V^\ast:\operatorname{Stab}(\psi)\ \text{开}\},\qquad V\xrightarrow{\ \sim\ }V^{\vee\vee}\iff \pi\ \text{容许}$
$$

$$
$\pi\ \text{容许}\iff V=\bigoplus_{\sigma\in E(C)}V_\sigma,\quad \dim V_\sigma<\infty\ \forall\sigma$
$$

$$
$V^\vee=\{\psi\in V^\ast:\operatorname{Stab}(\psi)\ \text{开}\},\qquad V\xrightarrow{\ \sim\ }V^{\vee\vee}\iff \pi\ \text{容许}$
$$

## 常见误解

- 「容许」不是「有限维」：容许表示一般无穷维（如非分歧主序列），有限维只在不可约且光滑时由引理 2.6 逼出「一维」这一极端情形。
- $\pi^\vee$ 的不可约性需要另证（底本 Remark 称「$\pi$ 不可约 $\iff$ $\pi^\vee$ 不可约」），不能从容许性自动得到。

## 相关卡

[Hecke 代数 H(G)、双陪集子代数与 「光滑表示 ≃ 非退化 Hecke 模」](../concepts/hecke-modules.md) · [球面 Hecke 代数与 Satake 同构、非分歧表示](../concepts/satake.md) · [抛物诱导、Jacquet 函子与模特征标 δ 的正规化](../concepts/parabolic-induction.md) · [定理 2.5（光滑不可约 ⇒ 容许）、引理 2.6 与 Harish-Chandra 特征标](../concepts/harish-chandra-character.md)

## 出处（印刷页）

- A p.10（A p.10）

> 说明：光滑/容许/反变对偶的定义与四条 Remark 取自 p.10 的 2.1.1；「容许性把表示拆成有限维 K-表示族」的解读是我们的判断。
