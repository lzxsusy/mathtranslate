---
id: glc/concept/cleanness-theorem
type: concept
track: D
---

# 洁净性定理

> 在 C_k 的三条条件下，F_k 跨非单射轨迹的延拓洁净：j_{k,!}F_k≃j_{k,*}F_k。

**问题**：洁净性定理的证明按什么分层归纳，最后还欠哪一步？

## 定义

固定满足 §6.1 三条条件的开子叠 $C_k\subset\operatorname{Coh}_k$，$j_k:C'_k\hookrightarrow\overline{C}'_k$ 为开嵌入，$F_k$ 为归纳定义的层。

*记号*：洁净性即 $j_{k,!}F_k\to j_{k,*}F_k$ 为同构；$\overline{C}'_k$ 允许截面非单射，$C'_k$ 是其开子叠。

## 要点

- 洁净性即 $j_{k,!}F_k\simeq j_{k,*}F_k$，等价于 $j_{k,!}=j_{k,!*}=j_{k,*}$。
- 按挠长 $\ell$ 分层归纳：$\ell=0$ 是无挠层，$\ell>0$ 用基变换与收缩原理。
- 基础情形与满射情形都归结为 $\operatorname{Av}^d_E=0$（定理 5.7.2）。
- 非满射情形归结为第 7 章的因子化恒等式。

## 关键公式

- $j_{k,!}F_k\simeq j_{k,*}F_k$
- $q_!j_{k,!}F_k\simeq\operatorname{Av}^d_E(W_k)|_{C_k^{\mathrm{tor}=0}}$
- $(s,q)_!m^*\mathcal{L}_E\simeq\mathcal{L}_E\boxtimes\mathcal{L}_E$

## 定理与证明

### 洁净性定理（要点（有缺口））

对 $1\le k<n$，$F_k$ 跨越非单射轨迹的延拓是洁净的，即在 $\overline{C}'_k$ 上有
\[
j_{k,!}F_k\simeq j_{k,*}F_k.
\]
因此，Fourier 归纳在所选开子叠上保持所需的不可约反常层。

1. 按挠部分的长度过滤：置 $\operatorname{Coh}_k^{\mathrm{tor},\le\ell}:=\{M_k\in\operatorname{Coh}_k\mid\operatorname{length}(\operatorname{Tor}(M_k))\le\ell\}$，并对 $\ell$ 归纳证明 $\overline{C}'_k{}^{\mathrm{tor},\le\ell}$ 上的洁净性。  
   *为什么*：$\operatorname{Coh}_k^{\mathrm{tor}=0}=\operatorname{Bun}_k$ 且 $C_k=\bigcup_{\ell\ge0}C_k^{\mathrm{tor},\le\ell}$，故可按层分层归纳。
2. $\ell=0$ 的基础情形：补集是零截面，由收缩原理与 Verdier 对偶，只需证 $q_!j_{k,!}F_k=0$；用 Whittaker 公式把它写成 $\operatorname{Av}^d_E(W_k)|_{C_k^{\mathrm{tor}=0}}$，条件 （2） 给出 $d>nk(2g-2)$，由定理 5.7.2 得零。  
   *为什么*：无挠时线丛到向量丛的映射要么为零、要么为单射，边界就是零截面。
3. 归纳步：把新的边界层 $Z$ 通过基变换换成带分裂表现的 $\widetilde{Y}$，固定点轨迹为 $\widetilde{Z}$，用 $\mathbb{G}_m$ 收缩原理把归纳步骤归约为 $\widetilde{f}_!\widetilde{j}_!(F_k|_{\widetilde{U}})=0$。  
   *为什么*：挠长 $\ell>0$ 时不存在到挠长 $\ell$ 轨迹的典范投影，必须把表现作为数据加入。
4. 在纤维上计算：若 $M_k\to\mathcal{T}$ 满射，纤维等价于普通修改叠，所需的 $!$-推前是 $\operatorname{Av}^d_E$ 的一个茎，且 $d=\mathring{\deg}\mathring{M}-\mathring{\deg}\mathring{M}_k>nk(2g-2)+\ell$，故由消失定理为零。  
   *为什么*：条件 （2） 给出 $\mathring{\deg}\mathring{M}>nk(2g-2)$，而在归一化次数下 $\mathring{\deg}\mathring{M}_k=-\ell$。
5. 若 $M_k\to\mathcal{T}$ 非满射，令 $\mathcal{T}'$ 为像，把数据分解到 $\mathcal{T}'$ 上；经仿射纤维化与基变换后，剩余项化为沿 $\mathrm{pr}$ 的推前，并由因子化恒等式 $(s,q)_!m^*\mathcal{L}_E\simeq\mathcal{L}_E\boxtimes\mathcal{L}_E$ 归约到满射情形。  
   *为什么*：该恒等式把挠商拆成 $M'/M_k$ 与 $\mathcal{T}/\mathcal{T}'$ 两部分，从而把非满射情形化回满射情形。

> 缺口：证明在 §6.3–§6.6 给出，但最后一步依赖因子化恒等式 $(s,q)_!m^*\mathcal{L}_E\simeq\mathcal{L}_E\boxtimes\mathcal{L}_E$，讲义明言它在第 7 章才证明；基础情形还调用定理 5.7.2，而后者只引用 [Gai04]、[Gai16b] 未证明。

*出处*：定理 6.2.1 / 原书 p.37


## 易错点

- 不能把 $\overline{C}'_k$ 与 $C'_k$ 混为一谈：定理断言的是跨过补集 $Z$（截面非单射的轨迹）的延拓为洁净。
- 「因此 Fourier 归纳保持不可约反常层」是洁净性的推论，不是额外假设。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§6.2 洁净性定理，p.37（PDF p.37），`源码/chapters/ch06.tex:39-49（定理 6.2.1）`

## 核验

状态：`source-only`（2026-11-18）
- nLab：https://ncatlab.org/nlab/show/six+operations — 页面给出 f_! ⊣ f^!（Verdier 对偶）、『There is a natural transformation f_! → f_* which is a natural equivalence when f is a proper map』以及 Beck–Chevalley 基变换 g^*∘f_! ≃ (p_2)_!∘(p_1)^*；这是洁净性证明所用六函子机制的框架，但页面没有 clean/cleanness 概念，也未陈述 j_{k,!}F_k ≃ j_{k,*}F_k（j_k 是开嵌入，非 proper），更没有定理 6.2.1。
- arXiv：https://arxiv.org/abs/math/0204081 — 摘要『In this paper we establish the required vanishing result』确认 Av_E^d 的消失定理由 [Gai04] 建立，即 gap_note 所称『定理 5.7.2 只引 [Gai04]、[Gai16b]』的出处属实；摘要不涉及洁净性本身。

## 关联

- `glc/concept/cleanness-expected`
- `glc/concept/fourier-tower`
- `glc/concept/non-surjective-reduction`
- `glc/concept/base-case-torsion-free`
