# 扭晶体：$\Crys^{T,l}$ 与 $\Crys^{T,r}$

> `cdm14/concept/twisted-crystals` · 轨道 G · 扭晶体 · 状态 dev

> **先自测**：扭化到底改变了晶体的什么？

## 一句话

固定 $T\in\mathrm{Tw}(Y)$，把 $\QCoh/\IndCoh$ 换成 $T$-扭版本，得到 $\Crys^{T,l}(Y)$、$\Crys^{T,r}(Y)$，两者仍由 $\Upsilon$ 等价。

## 定义

$\QCoh$ 上 $\mathbf{pt}/\mathbb G_m$ 作用（线丛张量）给出扭版本 $\QCoh^G$。对 $T\in\mathrm{Tw}(Y)$，定义 $\Crys^{T,l}(Y):=\QCoh^T(Y_{\mathrm{dR}})=\lim_{S}\QCoh^T(S)$，$\Crys^{T,r}(Y):=\IndCoh^T(Y_{\mathrm{dR}})$。

**记号**：$\oblv^{T,l},\oblv^{T,r}$ 为到 $\QCoh^T/\IndCoh^T$ 的遗忘函子。

## 要点（为什么需要它）

1. 注 7.3.1：扭情形的结论不自动成立（无法同时把仿射 $X$ 嵌入光滑 $Z$ 并投到 $Y$），但对 Zariski/平展局部平凡的 $T$ 自动成立。
2. 命题 7.3.3：$\Upsilon:\Crys^{T,l}(Y)\to\Crys^{T,r}(Y)$ 仍是等价。
3. 引理 7.3.7：$\oblv^{T,r}\circ\ind^{T,r}$ 与 $\oblv^r\circ\ind^r$ 经平凡化非典范同构，核多出一个线丛 $L$。
4. 定理 7.5.1：光滑经典 $X$ 上 $\Crys^{T,l}(X)\simeq D\text{-}\mathrm{mod}^{T,l}(X)$，即扭 D-模。

## 核心公式

$$\Crys^{T,l}(Y):=\QCoh^T(Y_{\mathrm{dR}}),\qquad \Crys^{T,r}(Y):=\IndCoh^T(Y_{\mathrm{dR}})$$

## 定理与证明（或缺口）

### 扭情形的左右等价（命题 7.3.3）

$\Upsilon:\Crys^{T,l}(Y)\to\Crys^{T,r}(Y)$ 是等价。

> 证明状态：**sketch**。第 1 步「在 $Y$ 上平凡化」只在 $G$ 于既约经典部分平凡时可行，这正是注 7.3.1 的假设。

出处：`A p.60`

## 常见误解

- $T$ 不是线丛：$\Crys^{T,l}$ 依赖整个 gerbe，不只是 $\pi_0$。
- 扭晶体不是「带联络的层」；它没有平坦连接，只有 gerbe 的扭。
- 左右等价需要 $G$ 在既约经典层面平凡；一般 $T$ 未必满足。

## 相关卡

[扭化 $\mathrm{Tw}(Y)$](../concepts/twisting.md) · [扭化的 Picard 群胚：$\mathrm{Tw}(Y)\simeq\tau^{\le2}(H_{\mathrm{dR}}\times_H *)[2]$](../concepts/twist-picard.md) · [扭晶体上的两个 $t$-结构](../concepts/twisted-t-structure.md) · [晶体与 D-模：经典等价](../concepts/crystals-vs-dmodules.md)

## 出处（印刷页）

- A p.58–59（A p.58）
- A p.60–61（A p.60）

> 说明：A=§7.1–7.3 的定义与命题 7.3.3；最没把握处：第 1 步平凡化的范围。
