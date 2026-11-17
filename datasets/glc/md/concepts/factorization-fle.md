---
id: glc/concept/factorization-fle
type: concept
track: H
---

# 因子化 FLE 与谱 Poincaré 函子

> 定理 15.2.1 的 Ran 空间版本：临界 KL 范畴在 Ran 上等价于非分歧 oper 上的 IndCoh，与局部化相容。

**问题**：$\operatorname{Poinc}^{\mathrm{spec}}$ 比较的是什么？

## 定义

§15.2 中的点态等价有 Ran 空间上的因子化版本：
$$\operatorname{FLE}_{G,\mathrm{crit},\mathrm{Ran}}:\operatorname{KL}_{G,\mathrm{crit},\mathrm{Ran}}\xrightarrow{\sim}\operatorname{IndCoh}(\operatorname{Op}^{\mathrm{unr}}_{\check G})_{\mathrm{Ran}}.$$
对点 $x$，记 $\operatorname{Op}_{\check G}(X\setminus\{x\})^{\mathrm{unr}}:=\operatorname{Op}_{\check G}(X\setminus\{x\})\times_{\operatorname{LocSys}_{\check G}(X\setminus\{x\})}\operatorname{LocSys}_{\check G}(X)$。

*记号*：$\operatorname{Ran}(X)$ 为 $X$ 的 Ran 空间，下标 $\mathrm{Ran}$ 表示相应的因子化版本；$\mathbb L$ 表示整体 Langlands 函子；$\operatorname{coeff}$ 为 Whittaker 系数函子，$\Gamma^{\mathrm{spec}}$ 为谱整体截面。

## 要点

- 它与到 $\operatorname{Bun}_G$ 的局部化函子及全局谱函子相容。
- 基本图表把 $\operatorname{KL}_{G,\mathrm{crit},\mathrm{Ran}}$、$\operatorname{IndCoh}(\operatorname{Op}^{\mathrm{unr}}_{\check G})_{\mathrm{Ran}}$、$\operatorname{DMod}_{\mathrm{crit}}(\operatorname{Bun}_G)$、$\operatorname{IndCoh}(\operatorname{LocSys}_{\check G}(X))$ 连起来。
- $\operatorname{Poinc}^{\mathrm{spec}}$ 是沿如下对应的推前—拉回变换：这一对应比较全局局部系统与它在形式圆盘上的限制。
- 相应的谱对应为 $\operatorname{Op}_{\check G}(X\setminus\{x\})^{\mathrm{unr}}\longrightarrow\operatorname{Op}_{\check G}(D_x^\times)\times_{\operatorname{LocSys}_{\check G}(D_x^\times)}\operatorname{LocSys}_{\check G}(D_x)$。
- 后面证明 $\mathbb L$ 为等价时，还要使用这个图表、系数函子和无穷水平 FLE：图表以 $\operatorname{coeff}$、$\Gamma^{\mathrm{spec}}$ 连接 $\operatorname{DMod}_{\mathrm{crit}}(\operatorname{Bun}_G)$、$\operatorname{IndCoh}(\operatorname{LocSys}_{\check G}(X))$、$\operatorname{Whit}(\operatorname{Gr}_G)_{\mathrm{crit},\mathrm{Ran}}$、$\operatorname{Rep}(\check G)_{\mathrm{Ran}}$，并以 $\operatorname{FLE}_\infty$ 标识下方的等价。

## 关键公式

- $\operatorname{FLE}_{G,\mathrm{crit},\mathrm{Ran}}:\operatorname{KL}_{G,\mathrm{crit},\mathrm{Ran}}\xrightarrow{\sim}\operatorname{IndCoh}(\operatorname{Op}^{\mathrm{unr}}_{\check G})_{\mathrm{Ran}}$
- $\operatorname{Op}_{\check G}(X\setminus\{x\})^{\mathrm{unr}}:=\operatorname{Op}_{\check G}(X\setminus\{x\})\times_{\operatorname{LocSys}_{\check G}(X\setminus\{x\})}\operatorname{LocSys}_{\check G}(X)$
- $\operatorname{Op}_{\check G}(X\setminus\{x\})^{\mathrm{unr}}\longrightarrow\operatorname{Op}_{\check G}(D_x^\times)\times_{\operatorname{LocSys}_{\check G}(D_x^\times)}\operatorname{LocSys}_{\check G}(D_x)$

## 定理与证明

### 因子化 FLE（§15.5）（要点（有缺口））

$\operatorname{FLE}_{G,\mathrm{crit},\mathrm{Ran}}:\operatorname{KL}_{G,\mathrm{crit},\mathrm{Ran}}\xrightarrow{\sim}\operatorname{IndCoh}(\operatorname{Op}^{\mathrm{unr}}_{\check G})_{\mathrm{Ran}}$，且与到 $\operatorname{Bun}_G$ 的局部化函子及全局谱函子相容。

1. 把定理 15.2.1 的点态等价放到 Ran 空间上，逐点取因子化版本。  
   *为什么*：点态等价已在定理 15.2.1 中陈述；Ran 版本要求它与插入／因子化结构相容，这正是讲义所引 [ABC24a] 的内容。
2. 将因子化等价与局部化函子 $\operatorname{Loc}$、谱 Poincaré 函子 $\operatorname{Poinc}^{\mathrm{spec}}$ 拼成基本图表。  
   *为什么*：$\operatorname{Poinc}^{\mathrm{spec}}$ 沿「全局局部系统 vs 其形式圆盘限制」的对应作推前—拉回，使图表两路可比较。

> 缺口：讲义只述不证，引 [ABC24a]；点态情形见定理 15.2.1。

*出处*：§15.5（因子化版本）/ 原书 p.74


## 易错点

- $\operatorname{Op}_{\check G}(X\setminus\{x\})^{\mathrm{unr}}$ 不是 $\operatorname{Op}_{\check G}(X\setminus\{x\})$：要多一层「局部系统延拓到整个 $X$」的纤维积；$\operatorname{Poinc}^{\mathrm{spec}}$ 比较的正是这个差别。
- $\operatorname{Poinc}^{\mathrm{spec}}$ 是推前—拉回变换而不是函子之间的自然同构；把它当成等价会误读基本图表的交换性。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§15.5 因子化 FLE 及其与整体局部化的相容性，p.74-75（PDF p.74-75），`源码/chapters/ch15.tex:95-106（因子化 FLE、基本图表与谱对应）`

## 核验

状态：`external-confirmed`（2026-11-18）
- Arinkin–Beraldo–Campbell–Chen–Færgeman–Gaitsgory–Lin–Raskin–Rozenblyum, Proof of the geometric Langlands conjecture II: Kac–Moody localization and the FLE：https://arxiv.org/abs/2405.03648 — Theorem 0.1.2 交换图：DMod_crit(Bun_G) —L_G→ IndCoh_Nilp(LS_Ǧ)，左列 Loc_{G,crit}，右列 Poinc^spec_{Ǧ,*}，底行 FLE_{G,crit}: KL(G)_{crit,Ran}→IndCoh_*(Op^{mon-free}_{Ǧ})_Ran；支持 FLE_Ran、基本图表与 Poinc^spec。
- Arinkin–Beraldo–Campbell–Chen–Færgeman–Gaitsgory–Lin–Raskin–Rozenblyum, Proof of the geometric Langlands conjecture II: Kac–Moody localization and the FLE：https://arxiv.org/abs/2405.03648 — 引言 300-307 说明 Poinc^spec_{Ǧ,*} 沿 Op^{mon-free}_{Ǧ,x} ← Op^{mon-free,glob}_{Ǧ,x} → LS_Ǧ 作推前—拉回，中间项是「X 上的局部系统 + X−x 上的 oper 结构」；支持 Op(X\x)^unr 与谱对应。
- Arinkin–Beraldo–Campbell–Chen–Færgeman–Gaitsgory–Lin–Raskin–Rozenblyum, Proof of the geometric Langlands conjecture II: Kac–Moody localization and the FLE：https://arxiv.org/abs/2405.03648 — §17.6 定义 Γ^{spec,IndCoh}（full text 25925/27684），intro line 1091 给出 FLE_∞: Rep(Ǧ)→Whit_*(G)；支持第二图表的 coeff、Γ^spec、FLE_∞ 标签。

## 关联

- `glc/concept/pointwise-fle`
- `glc/concept/multipoint-localization`
- `glc/concept/global-langlands-functor`
