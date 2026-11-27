# 几何朗兰兹：把猜想搬到曲线上

> `goresky04/concept/geometric-langlands` · 轨道 D · 几何侧与展望 · 状态 dev

> **先自测**：几何朗兰兹换掉的是哪几样东西，为什么这样换能绕开 $n\ge3$ 的障碍？

## 一句话

把 $\bbQ$ 换成曲线 $C$ 的函数域，把「Galois 表示」换成 $C$ 上的 $G$-丛与局部系统，把「自守表示」换成 $\Bun_G$ 上的层，得到几何版的对应。

## 定义

设 $C$ 为 $\bbF_q$ 上的光滑射影曲线，$G$ 为约化群。几何朗兰兹猜测：$C$ 上 $G^\vee$-局部系统与 $\Bun_G$（$G$-丛的模栈）上满足 Hecke 特征条件的 $\Ql$-层（Hecke 特征层）之间存在对应，使每个局部系统 $E$ 对应一个层 $\mathcal F_E$，且 $\mathcal F_E$ 是每个 Hecke 算子 $\mathbb H_V$ 的特征层，特征值为 $E$ 的相应数据。

**记号**：$\Bun_G$ 为 $G$-丛模栈；$G^\vee$ 为对偶群；$\mathbb H_V$ 为沿 $\mathrm{Gr}_{G,V}$ 的 Hecke 算子；$\mathcal F_E$ 为 Hecke 特征层。

## 要点（为什么需要它）

1. 换的三样：底域（$\bbQ$ → 曲线函数域）、左侧（Galois 表示 → 局部系统）、右侧（$\GL(n)$ 的自守表示 → $\Bun_G$ 上的层）。
2. 绕开障碍的机制：不再需要 Shimura 簇。$\Bun_G$ 对任意 $G$ 都存在，是无穷维栈，直接在它上面做层论。
3. $n=2$ 的经典对应是几何对应的「$\bbQ$ 影子」：模曲线上的 Hecke 特征层可以看成 $\Bun_{\GL(2)}$ 上的层在有限域上的痕迹。
4. 本文 §8.5 只有标题、正文为空；作者在引言里说「几个月后再来看空节有没有补上」，但这一节直到本文定稿仍是空的。

## 核心公式

$$
$\mathbb H_V\colon \mathcal D(\Bun_G)\to\mathcal D(\Bun_G\times C)$，$\mathcal F_E\mapsto E\boxtimes\mathcal F_E$$\mathcal F_E$ 是 Hecke 特征层：$\mathbb H_V(\mathcal F_E)\cong E_V\boxtimes\mathcal F_E$
$$

$$
$\mathcal F_E$ 是 Hecke 特征层：$\mathbb H_V(\mathcal F_E)\cong E_V\boxtimes\mathcal F_E$
$$

## 定理与证明（或缺口）

### 几何朗兰兹猜想（本文未陈述）

$C$ 上 $G^\vee$-局部系统与 $\Bun_G$ 上的 Hecke 特征层之间存在对应；在 $G=\GL(n)$ 且 $C$ 为椭圆曲线时，这与经典对应一致。

> 证明状态：**gap**。原文 §8.5 正文为空，只留标题；本卡的陈述按标题与 §8.1 的一般形式补出，属译者按（B 级），不是原文内容。

出处：`B p.15`

## 常见误解

- 几何朗兰兹不是「把朗兰兹翻译成几何语言」：它改变的是底域（数域 → 函数域），因此它是**另一个猜想**，不是同一个猜想的重述。
- 不要把它与「$p$ 进朗兰兹」「局部朗兰兹」混为一谈：那些仍在数域上，几何朗兰兹在曲线上。
- 本文没有给出几何朗兰兹的任何内容：§8.5 是空的。读到这里应当把它当成「作者指了一个方向」，而不是「作者讲了这个方向」。

## 相关卡

[$n\ge3$ 的障碍：Shimura 簇不存在](../concepts/obstruction-n-ge-3.md) · [对偶群与 $L$-群](../concepts/dual-group.md) · [函子性：换群的那条路](../concepts/functoriality.md)

## 出处（印刷页）

- A p.15–16（B p.15）
- A p.1（A p.1）

> 说明：原文 §8.5 只有标题。本卡的定义与陈述按标题、§8.1 的一般形式、以及库内已译的 SY02-40/SY02-38/SY99-04 补出，属 B 级译者按；不冒充原文。
