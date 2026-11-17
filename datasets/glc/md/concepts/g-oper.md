---
id: glc/concept/g-oper
type: concept
track: G
---

# $\check G$-oper

> 相对 $X$ 的 $D_X$-概形 $Y$ 上的 $(\check B,\nabla)$ 二元组，其 $\check B$-约化的第二基本形式落在开轨道内（简单负根分量处处非零）。

**问题**：oper 条件用第二基本形式 $c(\nabla)$ 怎样表述，为什么 $Y\mapsto\operatorname{Op}_{\check G}(Y)$ 可表？

## 定义

令 $\pi:Y\to X$ 为 $D_X$-概形。依照 Beilinson–Drinfeld [BD05]，$Y$ 上相对于 $X$ 的 $\check G$-oper 是一个二元组 $(\mathcal F_{\check B},\nabla)$，其中 $\mathcal F_{\check B}$ 是 $Y$ 上的 $\check B$-挠子，$\nabla$ 是诱导的 $\check G$-挠子 $\mathcal F_{\check G}:=\check G\times^{\check B}\mathcal F_{\check B}$ 上相对于 $\pi$ 的联络，并且 $\check B$-约化的第二基本形式满足 oper 条件：$c(\nabla)\in\Gamma(Y,(\check{\mathfrak g}/\check{\mathfrak b})_{\mathcal F_{\check B}}\otimes\pi^*\Omega_X)$ 位于由简单负根方向组成的子丛中的开 $\check B$-轨道；等价地，它的简单负根分量处处非零。函子 $Y\mapsto\operatorname{Op}_{\check G}(Y)$ 由一个 $D_X$-概形表示，记为 $\operatorname{Op}^D_{\check G}\to X$；它的全局截面是通常的 oper 空间 $\operatorname{Op}_{\check G}(X)$。

*记号*：$\pi:Y\to X$ 为 $D_X$-概形；$\check B\subset\check G$ 为固定 Borel 子群，$\check{\mathfrak b}=\operatorname{Lie}\check B$；$\Omega_X$ 为 $X$ 的典范丛；$(\check{\mathfrak g}/\check{\mathfrak b})_{\mathcal F_{\check B}}$ 为相应伴随丛；$c(\nabla)$ 为 $\check B$-约化的第二基本形式。

## 要点

- oper 是二元组：$\check B$-挠子 $\mathcal F_{\check B}$ 加上诱导 $\check G$-挠子 $\mathcal F_{\check G}$ 上相对于 $\pi$ 的联络。
- oper 条件是第二基本形式 $c(\nabla)$ 落在开 $\check B$-轨道内；等价说法是它的简单负根分量处处非零。
- $Y\mapsto\operatorname{Op}_{\check G}(Y)$ 由 $D_X$-概形 $\operatorname{Op}^D_{\check G}\to X$ 表示。
- $\operatorname{Op}_{\check G}(X)$ 是 $\operatorname{Op}^D_{\check G}\to X$ 的全局截面，即通常的 oper 空间。

## 关键公式

- $\mathcal F_{\check G}:=\check G\times^{\check B}\mathcal F_{\check B}$
- $c(\nabla)\in\Gamma(Y,(\check{\mathfrak g}/\check{\mathfrak b})_{\mathcal F_{\check B}}\otimes\pi^*\Omega_X)$ 落在开 $\check B$-轨道内，即简单负根分量处处非零

## 易错点

- 「开 $\check B$-轨道」在 $(\check{\mathfrak g}/\check{\mathfrak b})$ 中只有一个，条件是简单负根分量处处非零，而不是「$c(\nabla)\ne0$」。
- $\operatorname{Op}^D_{\check G}\to X$ 是表示该函子的 $D_X$-概形，$\operatorname{Op}_{\check G}(X)$ 是它的全局截面；两者不是同一个对象。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§14.1 oper 作为 Hitchin 底空间上的挠子，p.68（PDF p.68），`源码/chapters/ch14.tex:12-18（oper 的定义与可表性）`

## 核验

状态：`external-confirmed`（2026-11-18）
- BD：https://math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf — “c: Conn(FG) → (g/b)F⊗ωX … c^{-1}(0)=Conn(FB)”；“A G-oper on X is a pair (FB,∇), ∇∈Γ(X,Conn(FG)) such that (1) c(∇)∈gr−1 gF⊗ωX ⊂ (g/b)F⊗ωX (2) For any simple negative root α the α-component c(∇)α does not vanish at any point of X”——逐条支持卡的 oper 条件公式、开 B̌-轨道与“简单负根分量处处非零”。
- Frenkel05：https://arxiv.org/abs/hep-th/0512172 — “A g-oper is by definition a triple (F,∇,FB+), where F is a principal G-bundle … ∇ is a connection … FB+ is a B+-reduction … such that … ∇∂/∂t has the form (8.9)”——支持“B̌-挠子 + 联络 + B-约化满足规范形”的等价定义。
- nLab: Drinfeld-Sokolov reduction：https://ncatlab.org/nlab/show/Drinfeld-Sokolov+reduction — 页面只列 Drinfel'd–Sokolov 1981/1985、De Sole–Kac–Valeri、Frenkel–Kac–Wakimoto、Feigin–Frenkel 等文献，无数学陈述；只能支持“Drinfeld–Sokolov 归约/规范”这一概念有原始文献。
- BD：https://math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf — “G-opers form a smooth algebraic stack … if G is adjoint then OpG(X)=Opg(X) is a scheme isomorphic to the affine space … via (43)”——支持函子由 D_X-概形 Op^D_{Ǧ} 表示（相对情形为形式推广）。

## 关联

- `glc/concept/opers-hitchin-torsor`
- `glc/concept/drinfeld-sokolov-gauge`
- `glc/concept/hitchin-base`
