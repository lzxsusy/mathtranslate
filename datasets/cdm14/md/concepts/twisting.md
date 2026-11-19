# 扭化 $\mathrm{Tw}(Y)$

> `cdm14/concept/twisting` · 轨道 F · 扭化 · 状态 dev

> **先自测**：为什么扭化要定义成「gerbe + 平凡化」的核？

## 一句话

$\mathrm{Tw}(Y)$ 是「在 $Y_{\mathrm{dR}}$ 上的 gerbe，加上在 $Y$ 上的平凡化」；线丛 $L$ 给出例子 $T(L)$。

## 定义

$\mathrm{Tw}(Y):=\ker\big(p^*_{\mathrm{dR},Y}:\mathbf{Ge}_{\mathbb G_m}(Y_{\mathrm{dR}})\to\mathbf{Ge}_{\mathbb G_m}(Y)\big)$，即 $Y_{\mathrm{dR}}$ 上的 gerbe 连同在 $Y$ 上的平凡化。

**记号**：$p_{\mathrm{dR},Y}:Y\to Y_{\mathrm{dR}}$。

## 要点（为什么需要它）

1. 线丛 $L$ 给出 $T(L)$：在每点取平凡 gerbe，平凡化由 $L$ 给出（§6.2.3）。
2. $\mathrm{Tw}$ 反变，并把余极限送到极限；它是 $\mathrm{Tw}|_{\mathcal C}$ 沿 $\mathcal C^{\mathrm{op}}\hookrightarrow\PreStk^{\mathrm{op}}$ 的右 Kan 延拓（引理 6.2.6）。
3. 光滑经典 $X$ 上 $\mathrm{Tw}(X)$ 的 $\pi_0$ 是 $H^2(X,\Omega^1\to\Omega^{2,\mathrm{cl}})$，同构空间是 $H^1$（§6.5）。
4. 扭化是 §7 扭晶体的输入：$T\in\mathrm{Tw}(Y)$ 决定 $\Crys^{T,l}$ 与 $\Crys^{T,r}$。

## 核心公式

$$\mathrm{Tw}(Y):=\ker\big(p^*_{\mathrm{dR},Y}:\mathbf{Ge}_{\mathbb G_m}(Y_{\mathrm{dR}})\to\mathbf{Ge}_{\mathbb G_m}(Y)\big)$$

## 定理与证明（或缺口）

### $\mathrm{Tw}$ 的右 Kan 延拓（引理 6.2.6）

对 $\mathcal C\in\{\DGSch_{\mathrm{aff}},\DGSch_{\mathrm{qs-qc}},\DGSch\}$，$\mathrm{Tw}$ 是 $\mathrm{Tw}|_{\mathcal C}$ 沿 $\mathcal C^{\mathrm{op}}\hookrightarrow\PreStk^{\mathrm{op}}$ 的右 Kan 延拓。

> 证明状态：**sketch**。「右 Kan 延拓」与「由仿射值决定」的等价在原文中只用一句「显然」。

出处：`A p.50`

## 常见误解

- $\mathrm{Tw}(Y)$ 的对象不是线丛：它比 Pic 大，含非平凡 gerbe。
- 平凡化只在 $Y$ 上给，不是在 $Y_{\mathrm{dR}}$ 上给；这是「扭」的来源。

## 相关卡

[$\mathbb G_m$-gerbe 与 $\mathbf{Ge}_{\mathbb G_m}$](../concepts/gm-gerbe.md) · [扭化的 Picard 群胚：$\mathrm{Tw}(Y)\simeq\tau^{\le2}(H_{\mathrm{dR}}\times_H *)[2]$](../concepts/twist-picard.md) · [扭晶体：$\Crys^{T,l}$ 与 $\Crys^{T,r}$](../concepts/twisted-crystals.md)

## 出处（印刷页）

- A p.50–51（A p.50）

> 说明：A=§6.2 的定义与引理 6.2.6；最没把握处：右 Kan 延拓的等价表述。
