# 扭化的 Picard 群胚：$\mathrm{Tw}(Y)\simeq\tau^{\le2}(H_{\mathrm{dR}}\times_H *)[2]$

> `cdm14/concept/twist-picard` · 轨道 F · 扭化 · 状态 dev

> **先自测**：为什么扭化只看见 $H^2$ 与 $H^1$，更高阶的信息去哪了？

## 一句话

$\mathrm{Tw}(Y)$ 是 $\tau^{\le2}(H_{\mathrm{dR}}(Y)\times_{H(Y)}*)[2]$；光滑经典 $X$ 上化为 $\tau^{\le2}\Gamma(X,\Omega^1\to\Omega^{2,\mathrm{cl}})[2]$。

## 定义

$H(Y):=\Gamma(Y,\mathcal O_Y)=\Maps_{\QCoh(Y)}(\mathcal O_Y,\mathcal O_Y)$，$H_{\mathrm{dR}}(Y):=H(Y_{\mathrm{dR}})$。推论 6.5.3：$\mathrm{Tw}(Y)\simeq\tau^{\le2}\big(H_{\mathrm{dR}}(Y)\times_{H(Y)}*\big)[2]$。

**记号**：$\tau^{\le2}$ 为连通截断；$[2]$ 为平移。

## 要点（为什么需要它）

1. 光滑经典 $X$ 上 $H_{\mathrm{dR}}(X)\simeq\Gamma(X,\Omega^\bullet_X)$，故 $\mathrm{Tw}(X)\simeq\tau^{\le2}\Gamma(X,\Omega^1\to\Omega^{2,\mathrm{cl}})[2]$。
2. 这与 [BB] 的 TDO（扭微分算子）一致：$\pi_0$ 是闭 2-形式的类，$\pi_1$ 是 1-形式。
3. $\mathbf{Ge}_{\mathbb G_a}(S)=B^2(\Gamma(S,\mathcal O_S))$，故 $\Maps(Y,B^2\mathbb G_a)\simeq\tau^{\le0}(H(Y)[2])$。
4. 推论 6.4.5：$\mathrm{Tw}$ 升级为 $(\PreStk)^{\mathrm{op}}\to\infty\text{-}\mathrm{PicGrpd}_k$。

## 核心公式

$$\mathrm{Tw}(Y)\simeq\tau^{\le2}\big(H_{\mathrm{dR}}(Y)\times_{H(Y)}*\big)[2],\qquad \mathrm{Tw}(X)\simeq\tau^{\le2}\Gamma(X,\Omega^1\to\Omega^{2,\mathrm{cl}})[2]$$

## 定理与证明（或缺口）

### 扭化的确定（推论 6.5.3）

对任意 $Y$，$\mathrm{Tw}(Y)\simeq\tau^{\le2}(H_{\mathrm{dR}}(Y)\times_{H(Y)}*)[2]$。

> 证明状态：**sketch**。第 2 步「纤维积的连通截断」是形式推导，原文未逐项验证。

出处：`A p.55`

## 常见误解

- $\tau^{\le2}$ 不能去掉：$\mathrm{Tw}$ 只在度数 $\le2$ 有信息。
- 光滑经典时 $H_{\mathrm{dR}}(X)$ 是 $\Omega^\bullet$ 的超上同调，不是 $\Omega^1$ 的上同调。
- $[2]$ 是平移，不是取两次。

## 相关卡

[扭化 $\mathrm{Tw}(Y)$](../concepts/twisting.md) · [$\mathbb G_m$-gerbe 与 $\mathbf{Ge}_{\mathbb G_m}$](../concepts/gm-gerbe.md) · [扭晶体：$\Crys^{T,l}$ 与 $\Crys^{T,r}$](../concepts/twisted-crystals.md)

## 出处（印刷页）

- A p.55–56（A p.55）

> 说明：A=§6.5 的推论 6.5.3 与 6.5.4；最没把握处：第 2 步纤维积截断的严格性。
