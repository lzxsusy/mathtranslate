# Weyl 群在 $D_\lambda$-模上的作用（由 $I_w$ 给出）

> `mloc/concept/weyl-group-action-on-d-lambda-modules` · type=concept · track=E · status=draft · verification=source-only

**别名**：Weyl 群作用、$W$-作用、交织函子的乘积公式、$LI_w$ 给出的作用

## 摘要

$LI_w$ 是 $D(D_\lambda)\simeq D(D_{w\lambda})$ 的等价，并满足乘积公式 $LI_{w'}LI_w\cong LI_{w'w}$。

## 问题

$W$ 是怎样通过交织函子作用在 $D_\lambda$-模上的，这个作用为什么只在 $W\lambda$ 轨道上才封闭？

## 定义

对 $w\in W$，$LI_w:D(D_\lambda)\to D(D_{w\lambda})$ 是范畴等价（定理 3.20）。当 $\ell(w'w)=\ell(w')+\ell(w)$ 时 $LI_{w'}\circ LI_w\cong LI_{w'w}$（定理 3.18）。于是对任意 $w$ 取既约分解 $w=s_{\alpha_1}\cdots s_{\alpha_k}$（$\alpha_i\in\Pi$），把 $LI_w$ 读作复合 $LI_{s_{\alpha_1}}\circ\cdots\circ LI_{s_{\alpha_k}}$：定理 3.18 保证每一步都满足 $\ell$ 可加，故该复合不依赖分解的写法（就自然同构而言）。单反射的 $LI_{s_\alpha}$ 因此是生成元，$W$ 在 $\bigcup_{\lambda\in\theta}D(D_\lambda)$ 上以弱作用（复合只到自然同构）的方式作用；固定 $\lambda$ 时，稳定化子 $W(\lambda)$ 给出 $D(D_\lambda)$ 的自等价。

记号：$D(D_\lambda)$ 为 $D_\lambda$-模的导出范畴；$\mathcal{M}_{qc}(D_\lambda)$ 上 $I_w$ 的定义见 §3.3（ch03c.tex:76-78），$I_w$ 只右正合，作用在导出范畴上由 $LI_w$ 实现。$s_\alpha$ 是单根 $\alpha\in\Pi$ 对应的单反射（§3.8，ch03f.tex:131-134）；$p_\alpha:X\to X_\alpha$ 是 $\alpha$ 型抛物子代数簇的投影（§3.3，ch03c.tex:182-185）。$\Sigma^+_w=\{\alpha\in\Sigma^+\mid w\alpha\in-\Sigma^+\}$（§3.3，ch03d.tex:54），$\Sigma_\lambda=\{\alpha\in\Sigma\mid\check{\alpha}(\lambda)\in\mathbb{Z}\}$（§2.2）。

## 要点

- $LI_w$ 是从 $D(D_\lambda)$ 到 $D(D_{w\lambda})$ 的等价，不是 $D(D_\lambda)$ 的自同态：$w\lambda\ne\lambda$ 时它把整个范畴搬到另一特征标上，所以「$W$ 作用」只在并集 $\bigcup_{\lambda\in\theta}D(D_\lambda)$ 上才是封闭的。
- 乘积公式（定理 3.18）只在 $\ell(w'w)=\ell(w')+\ell(w)$ 时断言；一般 $w$ 必须经既约分解理解为单反射函子的复合，$\ell$ 不增的乘法律不在定理之列。
- 单反射是生成元：$w=s_{\alpha_1}\cdots s_{\alpha_k}$ 既约时 $LI_w\cong LI_{s_{\alpha_1}}\circ\cdots\circ LI_{s_{\alpha_k}}$，于是 $W$ 的作用完全由有限多个 $LI_{s_\alpha}$ 决定（这是定理 6.2 只对单反射证明的理由）。
- 作用与权扭变相容：$LI_w(V(\nu))=LI_w(V)(w\nu)$（引理 3.5），即 $W$ 同时置换特征标与权；缺了这一条，$W(\lambda)$ 的自等价就无法与几何平移对齐。
- 逆由对偶给出：$(LI_w)^{-1}\cong\mathbb{D}\circ LI_{w^{-1}}\circ\mathbb{D}$（定理 4.4）。正因为逆要绕道 $D_{-\lambda}$，这个作用是「弱」的——只在自然同构意义下成立，而不是严格的群作用。
- 只是弱作用还有一个具体表现：$LI_{s_\alpha}\circ LI_{s_\alpha}$ 一般不同构于恒等函子（$\check{\alpha}(\lambda)\in\mathbb{Z}$ 时它带着 $V(p\alpha)$ 的平移），所以不能把 $W$ 读成严格作用的群。

## 公式

$$$LI_w:\ D(D_\lambda)\xrightarrow{\ \sim\ }D(D_{w\lambda})$$$

$$$LI_{w'}\circ LI_w\cong LI_{w'w}\qquad\bigl(\ell(w'w)=\ell(w')+\ell(w)\bigr)$$$

$$$LI_w\bigl(V^\bullet(\nu)\bigr)=LI_w(V^\bullet)(w\nu)$$$

$$$(LI_w)^{-1}\cong\mathbb{D}\circ LI_{w^{-1}}\circ\mathbb{D}$$$

$$$w=s_{\alpha_1}\cdots s_{\alpha_k}\ \text{既约}\ \Longrightarrow\ LI_w\cong LI_{s_{\alpha_1}}\circ\cdots\circ LI_{s_{\alpha_k}}$$$

## 相关定理

### 定理 3.18：乘积公式（最终形式）

设 $w',w\in W$ 且 $\ell(w'w)=\ell(w')+\ell(w)$。则作为从 $D(D_\lambda)$ 到 $D(D_{w'w\lambda})$ 的函子有 $LI_{w'}\circ LI_w\cong LI_{w'w}$。

证明状态：`sketch`

1. 由引理 3.6，$\ell$ 可加时 $r:Z_{w'}\times_X Z_w\to Z_{w'w}$ 是同构，故 $J_{w'}\circ J_w=J_{w'w}$（引理 3.7）。
   - 为什么：两个相对位置复合的几何对应就是乘积 $w'w$ 的 $Z$，$\ell$ 可加保证纤维维数相加、不发生退化。
2. 在导出范畴上取左导出：$LI_{w'}\circ LI_w$ 是 $J_{w'}\circ J_w$ 的左导出，而 $J_{w'w}$ 与 $LI_{w'w}$ 在 $D^b$ 上一致（定理 3.14(i)）。
   - 为什么：左导出与复合相容，且 $J$ 的乘法性正是第 1 步的同构。
3. 剩下的相容性（结合约束、与 $T_{w''}$ 的计算）为形式验算。
   - 为什么：各步自然同构的协调性只涉及 $Z_w$ 上可逆层的拉回，属机械验证。

> 缺口：第 1 步依赖引理 3.6、3.7 的完整证明（ch03c.tex:129-169，底本 p.50-51）；本卡只复述其结论与用法，未逐行复核基变换计算。

### 定理 3.20：$LI_w$ 是导出范畴的等价

对任意 $w\in W$ 与 $\lambda\in\mathfrak{h}^*$：(i) $LI_w$ 是 $D(D_\lambda)$ 与 $D(D_{w\lambda})$ 的等价；(ii) 它诱导 $D^b\simeq D^b$；(iii) 它诱导 $D^b_{coh}\simeq D^b_{coh}$。

证明状态：`sketch`

1. 先设 $\lambda$ 反支配且正则。由定理 3.19(i)，$LI_w$ 是等价且同构于 $L\Delta_{w\lambda}\circ R\Gamma$。
   - 为什么：正则反支配时 $\Delta_\lambda$ 与 $\Gamma$ 互为逆（定理 1.12），交织函子只是把这一对搬到 $w\lambda$。
2. $\Gamma$ 与 $\Delta$ 的同调维数有限（定理 1.13、1.16），故 $L\Delta_{w\lambda}\circ R\Gamma$ 把有界复形送到有界复形、把凝聚复形送到凝聚复形。
   - 为什么：有界性与凝聚性在有限同调维数的函子下保持，这正是 (ii)(iii) 所需的。
3. 对一般 $\lambda$，用引理 3.5 的几何平移把 $\lambda$ 搬到反支配正则位置，再把结论搬回来。
   - 为什么：几何平移是范畴等价且只把权按 $w$ 搬运，不改变上述三条性质。

> 缺口：证明依赖 §1 的定理 1.12、1.13、1.16（$\Gamma$、$\Delta$ 的伴随性与有限同调维数），本卡未复核这些引理。

### 推论 3.22：无交条件下的范畴等价

若 $\Sigma^+_w\cap\Sigma_\lambda=\varnothing$，则 $I_w:\mathcal{M}_{qc}(D_\lambda)\to\mathcal{M}_{qc}(D_{w\lambda})$ 是范畴等价，其逆为 $I_{w^{-1}}$。

证明状态：`complete`

1. 由定理 3.21，$I_w$ 的左上同调维数不超过 $\operatorname{Card}(\Sigma^+_w\cap\Sigma_\lambda)=0$，故 $I_w$ 正合。
   - 为什么：左上同调维数为 $0$ 意味着 $L^iI_w=0$ 对一切 $i<0$，即 $I_w$ 与左导出重合、从而正合。
2. 同理 $I_{w^{-1}}$ 也正合；由推论 3.8 的乘法公式（此时 $\ell$ 可加）得 $I_{w^{-1}}\circ I_w=I_1=\mathrm{id}$ 与 $I_w\circ I_{w^{-1}}=\mathrm{id}$。
   - 为什么：两方向的复合都归结为 $Z_1$（对角）上的恒等函子，而 $w^{-1}w=1$。

## 易错点

- 把 $LI_w$ 当成 $D(D_\lambda)$ 上的自等价是错的：$w\lambda$ 一般不等于 $\lambda$；只有在稳定化子 $W(\lambda)$ 内、且复合满足 $\ell$ 可加时，才是自等价。
- 定理 3.18 的 $\ell$ 可加条件不能省：$\ell(w'w)<\ell(w')+\ell(w)$ 时 $LI_{w'}\circ LI_w$ 不再同构于 $LI_{w'w}$，中间会多出 $Z_{w'}\times_X Z_w\to Z_{w'w}$ 的退化纤维。
- $W$ 的作用不跨越轨道：不同 $\theta=W\lambda$ 之间的两个范畴没有 $I_w$ 相连，只有 $\Delta_\lambda$ 与 $\Gamma$ 这类「竖直」函子相连；把 $W$-作用写成整个 $D$-模范畴上的作用会出错。
- 「弱作用」不是修辞：$LI_{s_\alpha}^2\ncong\mathrm{id}$ 一般成立（当 $\check{\alpha}(\lambda)\in\mathbb{Z}$ 时它伴随 $V(p\alpha)$ 的平移，见 §3.8 与定理 5.6），所以 $W$ 不是以严格群作用的方式作用。

## 相关卡

- `mloc/concept/intertwining-functor-i-w`
- `mloc/concept/inverse-intertwining-functor`
- `mloc/concept/single-reflection-intertwining`
- `mloc/concept/iw-exactness`

## 出处

- Miličić, Localization and Representation Theory of Reductive Lie Groups · §3.3 单反射的复合（推论 3.8） · p.[51]（PDF [55]） · `源码/chapters/ch03c.tex:170-171（推论 3.8）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · §3.3 乘积公式与导出范畴的等价 · p.[56, 57]（PDF [60, 61]） · `源码/chapters/ch03d.tex:127-128, 158-164（定理 3.18、定理 3.20）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · §3.3 精细同调维数界与逆（定理 3.21、推论 3.22） · p.[57, 58]（PDF [61, 62]） · `源码/chapters/ch03d.tex:175-190（定理 3.21、推论 3.22）`
