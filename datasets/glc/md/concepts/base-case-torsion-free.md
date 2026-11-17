---
id: glc/concept/base-case-torsion-free
type: concept
track: D
---

# 基础情形：无挠层的洁净性

> ℓ=0（无挠）时补集是零截面，收缩原理把洁净性化为 q_!j_{k,!}F_k=0，再由消失定理得零。

**问题**：无挠基础情形中，收缩原理为什么能把 i^!j_{k,!} 换成 q_!j_{k,!}？

## 定义

设 $\ell=0$，即考虑 $C_k^{\mathrm{tor}=0}\subset\overline{C}'_k{}^{\mathrm{tor}=0}$。从线丛到向量丛的映射要么为零、要么为单射，因此 $C'_k{}^{\mathrm{tor}=0}$ 在 $\overline{C}'_k{}^{\mathrm{tor}=0}$ 中的补集是零截面
\[
i:C_k^{\mathrm{tor}=0}\hookrightarrow\overline{C}'_k{}^{\mathrm{tor}=0}.
\]
令 $q:\overline{C}'_k{}^{\mathrm{tor}=0}\to C_k^{\mathrm{tor}=0}$ 为向量丛投影。该层沿纤维上的伸缩作用的轨道局部常值（monodromic）。

*记号*：$\overline{C}'_k{}^{\mathrm{tor}=0}\to C_k^{\mathrm{tor}=0}$ 是向量丛，$i$ 是它的零截面。

## 要点

- 无挠时补集恰是零截面，故洁净性化为 $i^*j_{k,*}F_k=0$。
- 收缩原理把 $i^!j_{k,!}$ 换成 $q_!j_{k,!}$。
- 边界上紧化 Whittaker 叠退化为普通 Whittaker 叠 $\operatorname{Bun}_{N_k}\xrightarrow{\pi}\operatorname{Bun}'_k\xrightarrow{r}\operatorname{Bun}_k$。
- 条件 （2） 把支撑推到 $d>nk(2g-2)$ 的次数分支，再用消失定理。

## 关键公式

- $i^*j_{k,*}F_k=0$
- $i^!j_{k,!}F_k\simeq q_!j_{k,!}F_k$
- $q_!j_{k,!}F_k\simeq\operatorname{Av}^d_E(W_k)|_{C_k^{\mathrm{tor}=0}}$

## 定理与证明

### 基础情形：无挠层的洁净性（要点（有缺口））

在 $C_k^{\mathrm{tor}=0}$ 上，$j_{k,!}F_k\simeq j_{k,*}F_k$；等价地，边界消失 $i^*j_{k,*}F_k=0$ 成立。

1. 与 $\operatorname{GL}_2$ 情形一样，洁净性等价于边界消失 $i^*j_{k,*}F_k=0$；由 Verdier 对偶，只需对 $F_k$ 及其对偶证明紧支撑版本。  
   *为什么*：补集是零截面，$j_{k,!}\to j_{k,*}$ 的锥支撑在补集上。
2. 收缩原理给出 $i^!j_{k,!}F_k\simeq q_!j_{k,!}F_k$。  
   *为什么*：层沿纤维的 $\mathbb{G}_m$-伸缩轨道局部常值（monodromic），故收缩原理适用。
3. 使用 $F_k$ 的 Whittaker 公式，
\[
q_!j_{k,!}F_k\simeq(r\circ\pi)_!(p_1^*\mathcal{L}_E\otimes p_2^*\mathcal{L}_{\psi})[\text{移位}](\text{扭曲})|_{C_k^{\mathrm{tor}=0}},
\]
在无挠零截面边界上紧化 Whittaker 叠限制为普通 Whittaker 叠 $\operatorname{Bun}_{N_k}\xrightarrow{\pi}\operatorname{Bun}'_k\xrightarrow{r}\operatorname{Bun}_k$。  
   *为什么*：边界上挠商为零，紧化 Whittaker 叠退化为普通 Whittaker 叠。
4. 令 $W_k$ 为把 $\exp_{\psi}$ 从 $\operatorname{Bun}_{N_k}$ 直接像到 $\operatorname{Bun}_k$ 所得的层（相同的移位与扭转）；在归一化次数 $d$ 的分支上 $q_!j_{k,!}F_k\simeq\operatorname{Av}^d_E(W_k)|_{C_k^{\mathrm{tor}=0}}$。  
   *为什么*：这正是平均函子的定义形式。
5. 归一化次数约定使 $\operatorname{Bun}_{N_k}$ 位于 $\operatorname{Bun}_k$ 的次数零分支之上；条件 （2） 给出 $C_k^{\mathrm{tor}=0}\subset\bigcup_{d>nk(2g-2)}\operatorname{Bun}_k^d$。由于 $k<n$，定理 5.7.2 说明 $d>nk(2g-2)$ 时 $\operatorname{Av}^d_E=0$，故 $q_!j_{k,!}F_k=0$。  
   *为什么*：归纳层级满足 $k<n$，正落在消失定理的适用范围。

> 缺口：这是定理 6.2.1 的基础情形（讲义 §6.3）；论证在讲义中给出，但依赖定理 5.7.2，而该定理只引用 [Gai04]、[Gai16b] 未证明。

*出处*：§6.3 基础情形：无挠层（定理 6.2.1 证明的一部分，原文未单独编号）/ 原书 p.37–38


## 易错点

- 必须用 $i^!$ 而不是 $i^*$：$i$ 是零截面的闭嵌入，$i^!$ 才天然配对紧支撑推前；收缩原理给出的正是 $!$-版本。
- 收缩原理要求 $F_k$ 沿 $\mathbb{G}_m$-伸缩轨道局部常值（monodromic），否则不适用。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§6.3 基础情形：无挠层，p.37-38（PDF p.37-38），`源码/chapters/ch06.tex:50-74（§6.3 基础情形）`

## 核验

状态：`source-only`（2026-11-18）
- nLab：https://ncatlab.org/nlab/show/six+operations — 页面给出 Verdier 对偶 f_! ⊣ f^!（故 i 为闭嵌入时与之配对的是紧支撑推前）与『proper 时 f_! ≃ f_*』，支持卡里『必须用 i^! 而不是 i^*』及紧支撑版 Verdier 对偶的一般做法；但收缩原理 i^!j_{k,!} ≃ q_!j_{k,!}、monodromic 条件与 q_!j_{k,!}F_k ≃ Av_E^d(W_k) 页面均无。

## 关联

- `glc/concept/cleanness-theorem`
- `glc/concept/base-whittaker-sheaf`
- `glc/concept/vanishing-theorem`
