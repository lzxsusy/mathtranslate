# 积分变换与核 $D^r_X$

> `cdm14/concept/integral-transform` · 轨道 E · 与 D-模的关系 · 状态 dev

> **先自测**：为什么 $\oblv^r\circ\ind^r$ 这个自函子可以用一个几何对象（核）完全描述？

## 一句话

$\IndCoh$ 自对偶把连续函子写成 $X\times Y$ 上的核；$\oblv^r\circ\ind^r$ 的核是 $D^r_X=(\widehat\Delta_X)_*\omega_{X\times_{X_{\mathrm{dR}}}X}$。

## 定义

对 $X,Y\in\DGIndSch_{\mathrm{laft}}$，$\mathrm{Funct}_{\mathrm{cont}}(\IndCoh(X),\IndCoh(Y))\simeq\IndCoh(X\times Y)$。对 $Q\in\IndCoh(X\times Y)$，$F_Q(\mathcal F)=(p_2)_*^{\IndCoh}\circ(\Delta_X\times\mathrm{id}_Y)^!(\mathcal F\boxtimes Q)$。

**记号**：$\widehat\Delta_X:X\times_{X_{\mathrm{dR}}}X\to X\times X$；$D^r_X$ 为 $\oblv^r_X\circ\ind^r_X$ 的核。

## 要点（为什么需要它）

1. 命题 5.1.3：$D^r_X\simeq(\widehat\Delta_X)_*^{\IndCoh}(\omega_{X\times_{X_{\mathrm{dR}}}X})$——群胚上的对偶化层沿 $\widehat\Delta_X$ 推出。
2. 推论 5.1.6：$\sigma(D^r_X)\simeq D^r_X$，其中 $\sigma$ 交换两个因子——核是对称的。
3. $D^r_X$ 是全化等变层的「单位」：$\oblv^r\circ\ind^r$ 就是与 $D^r_X$ 作积分变换。
4. 在光滑经典 $X$ 上，$D^l_X$（左版本核）落在 $t$-结构心中（命题 5.3.6），并与 $\mathrm{Diff}_X$ 同构（引理 5.4.3）。

## 核心公式

$$F_Q(\mathcal F)=(p_2)_*^{\IndCoh}\circ(\Delta_X\times\mathrm{id}_Y)^!(\mathcal F\boxtimes Q),\qquad D^r_X\simeq(\widehat\Delta_X)_*^{\IndCoh}\omega_{X\times_{X_{\mathrm{dR}}}X}$$

## 定理与证明（或缺口）

### 核的几何描述（命题 5.1.3）

$D^r_X\simeq(\widehat\Delta_X)_*^{\IndCoh}(\omega_{X\times_{X_{\mathrm{dR}}}X})$。

> 证明状态：**sketch**。第 2 步把「全化上的积分变换」写成对应，原文用 [GR1, 命题 2.9.2] 的基变换，细节未展开。

出处：`A p.42`

## 常见误解

- $F_Q$ 的公式里 $(\Delta_X\times\mathrm{id}_Y)^!$ 是 $!$-拉回，不是 $*$。
- 核 $D^r_X$ 不是 $\omega_X$：它住在群胚 $X\times_{X_{\mathrm{dR}}}X$ 上。
- $\sigma(D^r_X)\simeq D^r_X$ 只是同构，不是恒等。

## 相关卡

[右晶体的归纳函子 $\ind^r_X$](../concepts/induction-right.md) · [核 $D^l_X$ 与微分算子层 $\mathrm{Diff}_X$](../concepts/diff-operators.md) · [晶体与 D-模：经典等价](../concepts/crystals-vs-dmodules.md)

## 出处（印刷页）

- A p.41–43（A p.41）

> 说明：A=§5.1 的 (5.1)、命题 5.1.3、推论 5.1.6 与命题 5.3.6；最没把握处：第 2 步对应的构造。
