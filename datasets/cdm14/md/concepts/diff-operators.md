# 核 $D^l_X$ 与微分算子层 $\mathrm{Diff}_X$

> `cdm14/concept/diff-operators` · 轨道 E · 与 D-模的关系 · 状态 dev

> **先自测**：晶体的卷积为什么就是微分算子的复合？

## 一句话

光滑经典 $X$ 上，$D^l_X$ 是 $\mathrm{Diff}_X$ 的代数推广：卷积对应复合，$D^l_X\to\mathrm{Diff}_X$ 是代数同构。

## 定义

设 $X$ 光滑经典。对支撑在对角线上的 $Q\in\QCoh(X\times X)^\heartsuit$，有 $\Maps((p_2)_*(p_1^*\mathcal F_1\otimes Q),\mathcal F_2)\simeq\Maps(Q,\mathrm{Diff}_X(\mathcal F_1,\mathcal F_2))$，且与卷积相容。取 $Q=D^l_X$、$\mathcal F_1=\mathcal F_2=\mathcal O_X$ 得代数同态 $D^l_X\to\mathrm{Diff}_X$。

**记号**：$\mathrm{Diff}_X$ 为微分算子层；$D^l_X$ 为左版本核。

## 要点（为什么需要它）

1. 引理 5.4.3：$D^l_X\to\mathrm{Diff}_X$ 是代数同构——这是 §5.5 的核心计算。
2. 卷积的几何来源：$D^l_X$ 支撑在 $X\times_{X_{\mathrm{dR}}}X$ 上，沿群胚的乘法正是微分算子的复合。
3. 光滑 $n$ 维时 $D^l_X$ 在 $t$-结构心中（命题 5.3.6），故可在 Abel 层面谈同构。
4. 这个同构把「晶体范畴上的单子」与「微分算子环上的模」接起来。

## 核心公式

$$\Maps\big((p_2)_*(p_1^*\mathcal F_1\otimes Q),\mathcal F_2\big)\simeq\Maps\big(Q,\mathrm{Diff}_X(\mathcal F_1,\mathcal F_2)\big)$$

## 定理与证明（或缺口）

### $D^l_X\simeq\mathrm{Diff}_X$（引理 5.4.3）

$X$ 光滑经典时，$D^l_X\to\mathrm{Diff}_X$ 是代数同构。

> 证明状态：**sketch**。第 2 步「由 $\mathrm{Diff}(A)$ 生成」在原文中是标准事实，未证。

出处：`A p.47`

## 常见误解

- $D^l_X$ 是「左」核，右晶体对应 $D^r_X$；两者经 $\Upsilon$ 相差 $\omega$。
- 同构只在光滑 $X$ 上成立；奇异时 $\mathrm{Diff}_X$ 不再是好对象。

## 相关卡

[积分变换与核 $D^r_X$](../concepts/integral-transform.md) · [晶体与 D-模：经典等价](../concepts/crystals-vs-dmodules.md)

## 出处（印刷页）

- A p.46–47（A p.46）

> 说明：A=§5.4 的 (5.2) 与引理 5.4.3；最没把握处：仿射情形的双模生成论证。
