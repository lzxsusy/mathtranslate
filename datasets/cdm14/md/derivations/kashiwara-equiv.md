# 命题 2.5.6 的证明：把 $\Crys^r(Z)_X$ 算成形完备化

> `cdm14/deriv/kashiwara-equiv` · 轨道 B · 左/右晶体、IndCoh 与 Kashiwara · 状态 dev · 4 步

> **要回答的问题**：「在开补上为零」为什么恰好等于「沿 $X$ 的形式完备化」？

## 一句话

把 $\Crys^r(X)$ 写成 $\IndCoh(S^\wedge)$ 的极限，把 $\Crys^r(Z)_X$ 写成 $\ker(j_S^!)$ 的极限，再用形式完备化的 $\IndCoh$ 描述把两者对上。

## 目标

证明 $i'^{\dagger,r}:\Crys^r(Z)_X\to\Crys^r(X)$ 是等价。

## 前提

- $\Crys^r(X)=\lim_{S\in(\DGSch_{\mathrm{aff,ft}})_{/Z_{\mathrm{dR}}}}\IndCoh(S\times_{Z_{\mathrm{dR}}}X_{\mathrm{dR}})$。
- $\Crys^r(Z)_X=\lim_S\ker\big(j_S^!:\IndCoh(S)\to\IndCoh(S\times_{Z_{\mathrm{dR}}}Z^\circ_{\mathrm{dR}})\big)$。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 把两个范畴都写成沿 $S\in(\DGSch_{\mathrm{aff,ft}})_{/Z_{\mathrm{dR}}}$ 的极限。 | $\Crys^r$ 按定义就是这种极限，$\Crys^r(Z)_X$ 是逐项取核。 | `A p.25` | A·原文明确写了 |
| 2 | 识别 $S^\wedge=S\times_{Z_{\mathrm{dR}}}X_{\mathrm{dR}}$ 为 $S$ 沿 ${}^{\mathrm{cl,red}}S\times_{{}^{\mathrm{cl,red}}Z}{}^{\mathrm{cl,red}}X$ 的形式完备化。 | $\mathrm{dR}$ 把测试环先约化，故纤维积只看见既约经典部分。 | `A p.25` | A·原文明确写了 |
| 3 | 用 [GR1, 命题 7.4.5]：$\ker(j_S^!)\simeq\IndCoh(S^\wedge)$。 | 形式完备化的 $\IndCoh$ 正是「在开补上为零」的 $\IndCoh$。 | `A p.25` | B·原文暗示、我们补的中间步 |
| 4 | 逐项等价取极限，得 $\Crys^r(Z)_X\simeq\lim\IndCoh(S^\wedge)=\Crys^r(X)$。 | 极限保持等价。 | `A p.25` | A·原文明确写了 |

## 结论

$i'^{\dagger,r}$ 是等价；闭浸入上的右晶体与 $X$ 上的右晶体是同一件事。

## 缺口

- 第 3 步引用 [GR1, 命题 7.4.5]，本文未证明；该命题要求 $S$ 最终余连接且 $S^\wedge$ 是形式完备化。

## 最容易讲错的地方

- $j_S^!$ 的核与 $j_S^*$ 的核不同：$\IndCoh$ 只有 $!$-拉回。
- 第 2 步里外层 $S$ 是 DG 概形、内层是经典约化，两个层次不能混。

## 相关卡

[Kashiwara 引理：闭浸入上的晶体即开补上为零的晶体](../concepts/kashiwara.md) · [右晶体：$\Crys^r(X)=\IndCoh(X_{\mathrm{dR}})$](../concepts/right-crystal.md) · [$\Upsilon$：左晶体与右晶体的比较](../concepts/upsilon-comparison.md)

## 出处（印刷页）

- A p.25（A p.25）

> 说明：A=命题 2.5.6 的证明；B=[GR1, 7.4.5]；最没把握处：$\ker(j_S^!)$ 与 $\IndCoh(S^\wedge)$ 的等价是否需额外有限性。
