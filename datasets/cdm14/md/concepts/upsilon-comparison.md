# $\Upsilon$：左晶体与右晶体的比较

> `cdm14/concept/upsilon-comparison` · 轨道 B · 左/右晶体、IndCoh 与 Kashiwara · 状态 dev

> **先自测**：左右晶体什么时候是同一个范畴？

## 一句话

$\Upsilon_S(F)=F\otimes\omega_S$ 把 $\QCoh$ 送到 $\IndCoh$，逐层拼起来给出 $\Crys^l(Y)\to\Crys^r(Y)$，并且是等价。

## 定义

对 $S\in\DGSch_{\mathrm{aff}}$，令 $\Upsilon_S:\QCoh(S)\to\IndCoh(S)$，$\mathcal F\mapsto\mathcal F\otimes\omega_S$。它与 $f^!$ 相容，升级为自然变换 $\Upsilon:\QCoh^*_{\PreStk}\to\IndCoh^!_{\PreStk}$，从而给出 $\Upsilon_{Y_{\mathrm{dR}}}:\Crys^l(Y)\to\Crys^r(Y)$。

**记号**：$\omega_S$ 为对偶化层；$\Upsilon$ 与两个 $\oblv$ 构成交换三角。

## 要点（为什么需要它）

1. $\Upsilon$ 与 $\oblv^l$、$\oblv^r$ 相容：$\oblv^r\circ\Upsilon_{Y_{\mathrm{dR}}}=\Upsilon_Y\circ\oblv^l$。
2. 命题 2.4.4：对任意 $Y\in\PreStk_{\mathrm{laft}}$，$\Upsilon_{Y_{\mathrm{dR}}}$ 是等价；因此 $\Crys(Y)$ 可以只写一个字母，带两个实现。
3. 有了它，$f^{\dagger}$ 同时与 $f^*$（左实现）和 $f^!$（右实现）相容，这正是「同一范畴、两套函子性」的含义。
4. 顺带得到 $\oblv^l$ 保守（引理 2.2.6）：由 $\oblv^r$ 保守与 $\Upsilon$ 等价推出。

## 核心公式

$$\Upsilon_S:\QCoh(S)\to\IndCoh(S),\quad \mathcal F\mapsto\mathcal F\otimes\omega_S;\qquad \Upsilon_{Y_{\mathrm{dR}}}:\Crys^l(Y)\xrightarrow{\sim}\Crys^r(Y)$$

## 定理与证明（或缺口）

### 左右晶体等价（命题 2.4.4）

对 $Y\in\PreStk_{\mathrm{laft}}$，$\Upsilon_{Y_{\mathrm{dR}}}:\Crys^l(Y)\to\Crys^r(Y)$ 是等价。

> 证明状态：**sketch**。第 2 步的「逐层等价」用的是 [GR1, Diagram (7.16)] 的短正合列，本文没有重述该引理的条件。

出处：`A p.22`

## 常见误解

- $\Upsilon$ 不是恒等：它把 $\mathcal F$ 换成 $\mathcal F\otimes\omega$，在光滑 $n$ 维情形把 $t$-结构平移 $n$（命题 4.4.2）。
- 等价只在 laft 情形陈述；非最终余连接的 DG 概形上左右晶体未必等价。
- $\Upsilon$ 与 $f^!$ 相容，但与 $f^*$ 不相容——这正是左右两套函子性不同的根源。

## 相关卡

[左晶体：$\Crys^l(Y)=\QCoh(Y_{\mathrm{dR}})$](../concepts/left-crystal.md) · [右晶体：$\Crys^r(X)=\IndCoh(X_{\mathrm{dR}})$](../concepts/right-crystal.md) · [命题 2.4.4 的证明：逐层 $\Upsilon$ 拼成全化上的等价](../derivations/upsilon-equiv.md) · [左 $t$-结构：把 $\QCoh$ 的 $t$-结构搬到 $\Crys^l$](../concepts/left-t-structure.md)

## 出处（印刷页）

- A p.21–23（A p.21）
- A p.22（A p.22）

> 说明：A=§2.4.1–2.4.7；最没把握处：把命题 2.4.4 的证明压成三步。
