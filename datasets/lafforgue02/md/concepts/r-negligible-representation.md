# $r$-可忽略表示与本质上同调

> `lafforgue02/concept/r-negligible-representation` · 轨道 A · 镜像对称与几何 Langlands · 状态 dev

> **先自测**：「可忽略」是相对什么而言的，为什么恰好是维数 $<r$ 的那一类？

## 一句话

$r$-可忽略表示是 $q'^*\sigma_1\otimes q''^*\sigma_2$（$\dim\sigma_i<r$）的直和项；不是它的叫本质的。本质部分才承载 Langlands 对应的解。

## 定义

设 $q',q'':X\times X\rightrightarrows X$ 为两个投影。$G_{F^2}$ 的一个不可约 $\ell$-进表示称为 $r$-可忽略的，若它是某个 $q'^*\sigma_1\otimes q''^*\sigma_2$ 的直和项，其中 $\sigma_1,\sigma_2$ 是 $G_F$ 的不可约表示且维数 $<r$。不是 $r$-可忽略的表示称为本质的（essentielle）。$\ell$-进上同调按此二分为可忽略上同调与本质上同调。

**记号**：$H^*_{\mathrm{ess}}$（本质上同调）、$H^*_{\mathrm{neg}}$（可忽略上同调）；$\{\pi\}^N_r$ 为尖点表示中 $K_N$-不变的、中心特征相应于 $a$ 者。

## 要点（为什么需要它）

1. 「可忽略」是相对秩 $r$ 而言的：所取的两个因子表示的维数必须严格小于 $r$，所以同一个表示在秩 $r$ 可忽略、在秩 $r+1$ 可能变成本质的。
2. 几何来源：边界分层的上同调形如 $(q_0^*\sigma_1\otimes q_1^*\sigma'_1)\otimes\cdots$，两次投影后只剩 $\sigma_1\otimes\sigma'_k$，维数都 $<r$——这正是边界被「$r$-可忽略」吸收的原因。
3. 本质部分的判据不是「不可约」，而是「不能被两个低维表示的张量积解释」。
4. 第 II 章的核心结论：本质部分集中在中间次数 $2r-2$，且在开叠、紧化、带水平紧化三处的本质上同调相同。

## 核心公式

$$
$q'^*\sigma_1\otimes q''^*\sigma_2$，$\dim\sigma_1,\dim\sigma_2<r$$H^{2r-2}_c(\Cht^{r}_N/a^{\mathbb Z})_{\mathrm{ess}}\cong H^{2r-2}_c(\ol{\Cht}^{\,r,\ol p\le p}_N/a^{\mathbb Z})_{\mathrm{ess}}$$H^*_{\mathrm{ess}}\cong\bigoplus_{\pi\in\{\pi\}^N_r}\pi^{K_N}\otimes q'^*\sigma_\pi\otimes q''^*\tilde\sigma_\pi(1-r)$
$$

$$
$H^{2r-2}_c(\Cht^{r}_N/a^{\mathbb Z})_{\mathrm{ess}}\cong H^{2r-2}_c(\ol{\Cht}^{\,r,\ol p\le p}_N/a^{\mathbb Z})_{\mathrm{ess}}$
$$

$$
$H^*_{\mathrm{ess}}\cong\bigoplus_{\pi\in\{\pi\}^N_r}\pi^{K_N}\otimes q'^*\sigma_\pi\otimes q''^*\tilde\sigma_\pi(1-r)$
$$

## 定理与证明（或缺口）

### 本质部分的集中性

上同调的本质部分（即非 $r$-可忽略部分）集中在次数 $2r-2$；它在 $H^{2r-2}_c(\Cht^{r,\ol p\le p}_N/a^{\mathbb Z})$、$IH^{2r-2}_c(\ol{\Cht}^{\,r,\ol p\le p}_N/a^{\mathbb Z})$ 与 $H^{2r-2}_c(\ol{\Cht}^{\,r,\ol p\le p'}_N/a^{\mathbb Z})$ 中相同。

> 证明状态：**sketch**。讲义只给骨架（$L$-函数的收敛性估计引自 Jacquet–Shalika，纯性论证引自 [Lafforgue 1997]）；完整证明在作者长文中。

出处：`A p.11`

## 常见误解

- 「可忽略」不是「零」或「可删」：它在几何上是有内容的边界上同调，只是不承载对应。
- 判据里的 $r$ 是**当前**要证的秩，不是 $\sigma$ 的维数；把 $r$ 读成「表示维数」会立刻读错定义。
- 本质部分集中在 $2r-2$ 只是中间次数；上下其他次数里仍可有可忽略部分，讲义明说「本质部分集中在中间次数」，不是「只有中间次数非零」。

## 相关卡

[Hecke 对应与 Hecke 代数](../concepts/hecke-correspondence.md) · [为什么本质部分集中在中间次数 $2r-2$](../derivations/essential-part-in-middle-degree.md) · [配对 $L$-函数（fonction $L$ de paires）](../concepts/lfunction-pairs.md)

## 出处（印刷页）

- A p.11–16（A p.11）

> 说明：定义取讲义 p.11 原文；边界上同调的 $q_0,q_1$ 形式与两次投影的计算取 p.13。集中性定理取 p.16，证明只复述其两步骨架。
