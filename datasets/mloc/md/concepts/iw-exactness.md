# 交织函子的正合性与上同调消没范围

> `mloc/concept/iw-exactness` · type=concept · track=E · status=draft · verification=source-only

**别名**：$I_w$ 的正合性、$I_w$ 的消没范围、左上同调维数、intertwining functor exactness

## 摘要

$LI_w=J_w$；$I_w$ 只在 $0$ 到 $\ell(w)$ 次有同调，界可收紧到 $\operatorname{Card}(\Sigma^+_w\cap\Sigma_\lambda)$，且最佳。

## 问题

$I_w$ 在什么条件下正合，$H^i(J_w(D(V)))$ 一般落在什么范围里、界能否再改进？

## 定义

因 $I_w=H^0\circ J_w$，$I_w$ 只右正合。对 $V\in\mathcal{M}_{qc}(D_\lambda)$，底本 ch03c.tex:72 陈述 $H^i(J_w(D(V)))=0$ 当 $i<-\ell(w)$ 与 $i>0$（译本校注存疑，见 pitfalls）。在导出范畴上 $LI_w=J_w$（定理 3.14(i)），且 $I_w$ 的左上同调维数 $\le\ell(w)$（定理 3.14(ii)）；更精细地，它 $\le\operatorname{Card}(\Sigma^+_w\cap\Sigma_\lambda)$（定理 3.21）。当 $\Sigma^+_w\cap\Sigma_\lambda=\varnothing$ 时 $I_w$ 正合，并且是范畴等价、逆为 $I_{w^{-1}}$（推论 3.22）。命题 3.24 说明 3.21 的界不可改进。

记号：$\Sigma^+_w=\{\alpha\in\Sigma^+\mid w\alpha\in-\Sigma^+\}=\Sigma^+\cap(-w^{-1}\Sigma^+)$（§3.3，ch03d.tex:54）；$\Sigma_\lambda=\{\alpha\in\Sigma\mid\check{\alpha}(\lambda)\in\mathbb{Z}\}$，$\Pi_\lambda=\Sigma_\lambda\cap\Pi$（§2.2）；$\ell(w)$ 为 $w$ 在 $W$ 中的长度。$J_w=Rp_{1+}(T_w\otimes p_2^+(-))$ 见 §3.3（ch03c.tex:67-70），$T_w=p_1^*(\mathcal{O}(\rho-w\rho))$；$D_\lambda=D_{X,\lambda+\rho}$ 按 §2.1 约定。

## 要点

- $I_w$ 只右正合；它的左导出 $LI_w$ 与 $J_w$ 在 $D^b$ 上重合（定理 3.14(i)），一切消没陈述都是这一等式的推论。
- 同调维数是「单侧」的：定理 3.14(ii) 只断言左侧 $L^iI_w=0\ (i<-\ell(w))$，并不给出 $H^i$ 的双侧有界性；不要把「左上同调维数 $\le\ell(w)$」读成 $I_w$ 有有限的双侧同调维数。
- $\ell(w)$ 不是最终的界：定理 3.21 把它收紧为 $\operatorname{Card}(\Sigma^+_w\cap\Sigma_\lambda)$。$\lambda$ 正则时 $\Sigma_\lambda=\varnothing$，于是 $I_w$ 正合、$LI_w\cong I_w$。
- 命题 3.24 说明 3.21 的界最佳：取 $V=\mathcal{O}(\lambda+\rho)$，则 $I_w$ 只在 $i=-\ell(w)$ 处非零。
- 正合性与可逆性是同一件事：推论 3.22 给出 $\Sigma^+_w\cap\Sigma_\lambda=\varnothing\Rightarrow I_w$ 是等价、逆为 $I_{w^{-1}}$；这刻画了 $\lambda$ 与 $w$ 的「一般位置」关系。
- 单反射已有干净的消没：引理 3.9 断言 $H^i(J_{s_\alpha}(D(D_\lambda)))=0$ 对 $i\ne0$，这是 §3.8 显式公式（只有 $U^{-1},U^0,U^1$）的起点。

## 公式

$$$LI_w=J_w\quad\text{on}\ D^b(D_\lambda)$$$

$$$L^iI_w=0\qquad(i<-\ell(w))$$$

$$$L^iI_w=0\qquad\bigl(i<-\operatorname{Card}(\Sigma^+_w\cap\Sigma_\lambda)\bigr)$$$

$$$L^{-\ell(w)}I_w\bigl(\mathcal{O}(\lambda+\rho)\bigr)=\mathcal{O}(w\lambda+\rho),\qquad L^iI_w\bigl(\mathcal{O}(\lambda+\rho)\bigr)=0\ (i\ne-\ell(w))$$$

$$$\Sigma^+_w\cap\Sigma_\lambda=\varnothing\ \Longrightarrow\ I_w:\mathcal{M}_{qc}(D_\lambda)\xrightarrow{\ \sim\ }\mathcal{M}_{qc}(D_{w\lambda}),\quad (I_w)^{-1}=I_{w^{-1}}$$$

## 相关定理

### 定理 3.21：$I_w$ 左上同调维数的精细界

对任意 $w\in W$ 与 $\lambda\in\mathfrak{h}^*$，$I_w$ 的左上同调维数不超过 $\operatorname{Card}(\Sigma^+_w\cap\Sigma_\lambda)$。

证明状态：`sketch`

1. 用几何平移（引理 3.5）与乘积公式（定理 3.18）把问题归约到 $w=s_\alpha$ 是单反射、$\lambda$ 落在 $\check{\alpha}(\lambda)\in\mathbb{Z}$ 的情形。
   - 为什么：只需处理 $\Sigma^+_w\cap\Sigma_\lambda\ne\varnothing$ 的单根；若为空则由推论 3.22 同调维数为 $0$。
2. 单反射时用引理 3.9 与 §3.8 的显式三项复形（定理 8.3）读出 $L^{-1}I_{s_\alpha}$ 与 $L^{0},L^{1}$ 的消没，得维数 $\le\operatorname{Card}(\Sigma^+_{s_\alpha}\cap\Sigma_\lambda)\le1$。
   - 为什么：$\Sigma^+_{s_\alpha}=\{\alpha\}$，故该基数只能是 $0$ 或 $1$，与显式复形只有 $U^{-1},U^{0},U^{1}$ 相符。
3. 对一般 $w$ 用既约分解逐次相加基数（引理 3.12(ii) 的 $\Sigma^+_{w'w}=w^{-1}\Sigma^+_{w'}\cup\Sigma^+_w$）并归纳。
   - 为什么：长度可加时两族的基数相加，正给出界的加性。

> 缺口：第 2 步把 §3.8 的显式公式（定理 8.3）用在单反射上，其证明依赖 $Y_\alpha$ 上的特异三角与基变换（ch03f.tex:187-206），本卡未逐行复核；第 3 步的归纳细节从略。

### 命题 3.24：界的不可改进性

设 $\lambda\in P(\Sigma)$。则 $L^iI_w(\mathcal{O}(\lambda+\rho))=0$ 对 $i\ne-\ell(w)$，且 $L^{-\ell(w)}I_w(\mathcal{O}(\lambda+\rho))=\mathcal{O}(w\lambda+\rho)$。

证明状态：`sketch`

1. 用几何平移把 $\lambda$ 搬到反支配正则位置（$\lambda\in P(\Sigma)$ 时可行），此时 $\mathcal{O}(\lambda+\rho)=\Delta_\lambda(\mathbb{C}_\lambda)$。
   - 为什么：线丛 $\mathcal{O}(\lambda+\rho)$ 正是由一维 $U_\theta$-模 $\mathbb{C}_\lambda$ 局部化而来。
2. 对 $\ell(w)$ 归纳，用定理 3.16（$LI_w\circ L\Delta_\lambda\cong L\Delta_{w\lambda}$）把 $LI_w$ 作用在 $\Delta_\lambda$ 上，再用 §1 的 1.22 计算 $L\Delta$ 的平移部分。
   - 为什么：$\Delta$ 与 $\Gamma$ 的交换性是唯一需要外部输入的地方，其余是权计算。
3. 逐项比较得只有 $i=-\ell(w)$ 一项存活，其余为形式验算。
   - 为什么：归纳中每一步只有一个 $L^{-1}$ 贡献，故总次数恰为 $-\ell(w)$。

> 缺口：证明用到 §1 的 1.22（本卡未复核）与定理 3.16 的归纳实施（ch03d.tex:219-223 原文从略）。

### 推论 3.22：无交条件下的范畴等价

若 $\Sigma^+_w\cap\Sigma_\lambda=\varnothing$，则 $I_w$ 是 $\mathcal{M}_{qc}(D_\lambda)$ 与 $\mathcal{M}_{qc}(D_{w\lambda})$ 的范畴等价，其逆为 $I_{w^{-1}}$。

证明状态：`complete`

1. 由定理 3.21，$I_w$ 的左上同调维数 $\le\operatorname{Card}(\Sigma^+_w\cap\Sigma_\lambda)=0$，故 $I_w$ 正合。
   - 为什么：左上同调维数为 $0$ 等价于 $L^iI_w=0$（$i<0$），即 $I_w$ 与左导出重合。
2. $I_{w^{-1}}$ 同理正合；由推论 3.8 及 $w^{-1}w=1$ 得两向复合均为恒等。
   - 为什么：两方向的复合分别等于 $I_1$，而 $Z_1$ 是对角、$I_1=\mathrm{id}$。

## 易错点

- 译本 ch03c.tex:73-75（底本 p.49）的校注怀疑底本 ch03c.tex:72 的消没区间上下界印反：若按仿射直像读应为 $i<0$ 与 $i>\ell(w)$。这是**存疑**而非定论；本卡按底本原文陈述（$i<-\ell(w)$ 与 $i>0$），引用前请自行核对原书。
- 「同调维数 $\le\ell(w)$」讲的是左下方向（$L^i$，$i$ 为负），不是 $H^i$ 的双侧消没；不要写成「$I_w$ 的同调维数为 $\ell(w)$」。
- $\lambda$ 正则并不自动使 $I_w$ 正合：还要 $\Sigma_\lambda$ 与 $\Sigma^+_w$ 无交。$\lambda$ 正则时 $\Sigma_\lambda=\varnothing$，故一切 $w$ 都正合；但 $\lambda$ 只是「一般」而 $\Sigma^+_w$ 取反方向时，两者仍可能相交。
- 命题 3.24 的 $\lambda$ 要求 $\lambda\in P(\Sigma)$（整权），此时 $\mathcal{O}(\lambda+\rho)$ 才是 $D_\lambda$-模；对非整权的 $\lambda$ 该陈述没有意义。

## 相关卡

- `mloc/concept/intertwining-functor-i-w`
- `mloc/concept/single-reflection-intertwining`
- `mloc/concept/weyl-group-action-on-d-lambda-modules`
- `mloc/concept/intertwining-and-holonomic`

## 出处

- Miličić, Localization and Representation Theory of Reductive Lie Groups · §3.3 单反射的消没（引理 3.9） · p.[51]（PDF [55]） · `源码/chapters/ch03c.tex:174-177（$Z=Z_{s_\alpha}$、引理 3.9）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · §3.3 $LI_w=J_w$ 与 $\ell(w)$ 界 · p.[54, 55]（PDF [58, 59]） · `源码/chapters/ch03d.tex:68-87（引理 3.13、定理 3.14 及其证明）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · §3.3 精细界与范畴等价 · p.[57, 58]（PDF [61, 62]） · `源码/chapters/ch03d.tex:175-190（定理 3.21、推论 3.22）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · §3.3 界的最佳性 · p.[58]（PDF [62]） · `源码/chapters/ch03d.tex:219-223（命题 3.24）`
