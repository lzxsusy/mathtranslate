# $\mathbb G_m$-gerbe 与 $\mathbf{Ge}_{\mathbb G_m}$

> `cdm14/concept/gm-gerbe` · 轨道 F · 扭化 · 状态 dev

> **先自测**：为什么同一个 gerbe 要分三个版本？

## 一句话

$\mathbb G_m$-gerbe 是 $\mathbf{pt}/\mathbb G_m$ 的 torsor 预层；三种「局部平凡」版本分别由 $B^{\mathrm{et}}$、$B^{\mathrm{Zar}}$、$B^{\mathrm{naive}}$ 表示。

## 定义

$\mathbf{pt}/\mathbb G_m$ 是分类栈 $S\mapsto$（$S$ 上线丛的 $\infty$-群胚）。$\mathbb G_m$-gerbe 是满足下列之一非空条件的 torsor 预层：(i) 平展局部非空；(ii) Zariski 局部非空；(iii) 整体非空。对应表示对象 $B^{\mathrm{et}}$、$B^{\mathrm{Zar}}$、$B^{\mathrm{naive}}$。

**记号**：$\mathbf{Ge}_{\mathbb G_m}(Y):=\lim_{S\in(\DGSch_{\mathrm{aff}}/Y)^{\mathrm{op}}}\mathbf{Ge}_{\mathbb G_m}(S)$。

## 要点（为什么需要它）

1. 三个版本不必等价（注 6.1.2），但它们在 §6.4 被证明给出同一个 $\mathrm{Tw}$（命题 6.4.2、推论 6.4.4）。
2. $\mathbb G_m$ 的交换群结构（张量积）使它升级为 $(\DGSch_{\mathrm{aff}})^{\mathrm{op}}\to\infty\text{-}\mathrm{PicGrpd}$ 的群对象。
3. $\mathbf{Ge}_{\mathbb G_m}(Y)$ 是「$Y$ 上的 gerbe」的 $\infty$-群胚，按 $Y$ 反变。
4. 对 $\mathbb G_a$ 情形三个版本等价（$H^2_{\mathrm{Zar}}=H^2_{\mathrm{et}}=0$），且 $\mathbf{Ge}_{\mathbb G_a}(S)=B^2(\Gamma(S,\mathcal O_S))$。

## 核心公式

$$\mathbf{Ge}_{\mathbb G_m}(S)=\{\text{$S$ 上的 }\mathbb G_m\text{-gerbe}\},\qquad B^{\mathrm{et}},B^{\mathrm{Zar}},B^{\mathrm{naive}}$$

## 定理与证明（或缺口）

### 三种 gerbe 版本给出同一扭化（推论 6.4.4）

$\mathrm{Tw}$、$\mathrm{Tw}^{\mathrm{/red}}$、$\mathrm{Tw}_a$、$\mathrm{Tw}^{\mathrm{/red}}_a$ 四个函子两两等价。

> 证明状态：**sketch**。第 3 步「重合」的证明在原文中占 §6.4 整节，此处只记结论链。

出处：`A p.54`

## 常见误解

- gerbe 不是线丛：线丛只给出特殊的扭化 $T(L)$。
- 三个版本的「非空」条件不同，不能默认它们相等；等价性是定理不是定义。

## 相关卡

[扭化 $\mathrm{Tw}(Y)$](../concepts/twisting.md) · [扭化的 Picard 群胚：$\mathrm{Tw}(Y)\simeq\tau^{\le2}(H_{\mathrm{dR}}\times_H *)[2]$](../concepts/twist-picard.md)

## 出处（印刷页）

- A p.48–50（A p.48）
- A p.53–55（A p.54）

> 说明：A=§6.1 的定义与 §6.4 的等价链；最没把握处：三个版本的层化构造。
