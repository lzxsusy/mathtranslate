---
id: glc/concept/canonical-borel-torsor
type: concept
track: G
---

# 典范 $\check B$-挠子与到 $\operatorname{Bun}_{\check G}$ 的常值映射

> 主 $\mathfrak{sl}_2$ 三元组给出 $X$ 上典范 $\check B$-挠子 $\mathcal F^{\mathrm{op}}_{\check B}$，任何 oper 的底层 $\check B$-挠子都是其拉回。

**问题**：引理 14.1.4 用主 $\mathfrak{sl}_2$ 三元组造出了什么，它为什么使「遗忘联络」成为常值映射？

## 定义

在 $\check{\mathfrak g}$ 中选定主 $\mathfrak{sl}_2$ 三元组 $(e,h,f)$。存在依赖于这一选择的 $X$ 上典范 $\check B$-挠子 $\mathcal F^{\mathrm{op}}_{\check B}$，使得对于任意 $Y\to X$ 上的每个 $\check G$-oper，其底层 $\check B$-挠子都典范地等于 $\mathcal F^{\mathrm{op}}_{\check B}$ 的拉回。相应的 $\operatorname{Bun}_{\check G}$ 中的点，在连通分支的意义下与辅助选择无关。特别地，遗忘联络给出到 $\operatorname{Bun}_{\check G}$ 的常值映射。

*记号*：$(e,h,f)$ 为 $\check{\mathfrak g}$ 中的主 $\mathfrak{sl}_2$ 三元组，$e$ 为主幂零元；$\operatorname{Bun}_{\check G}$ 为 $\check G$-丛叠；$\operatorname{LocSys}_{\check G}(X)$ 为 $\check G$-局部系统的叠。

## 要点

- $\mathcal F^{\mathrm{op}}_{\check B}$ 依赖主 $\mathfrak{sl}_2$ 三元组 $(e,h,f)$ 的选择。
- 任何 $Y\to X$ 上 $\check G$-oper 的底层 $\check B$-挠子都典范地是 $\mathcal F^{\mathrm{op}}_{\check B}$ 的拉回。
- 对应的 $\operatorname{Bun}_{\check G}$ 中的点，在连通分支的意义下与辅助选择无关。
- 特别地，遗忘联络给出到 $\operatorname{Bun}_{\check G}$ 的常值映射。

## 关键公式

- $\text{底层}\ \check B\text{-挠子}\ \mathcal F_{\check B}\simeq\pi^*\mathcal F^{\mathrm{op}}_{\check B}$
- $\operatorname{Op}_{\check G}(X)\longrightarrow\operatorname{Bun}_{\check G}(X)\ \text{为常值映射}$

## 定理与证明

### 引理 14.1.4（典范 $\check B$-挠子的存在）（要点（有缺口））

选定主 $\mathfrak{sl}_2$ 三元组 $(e,h,f)$ 后，存在 $X$ 上典范 $\check B$-挠子 $\mathcal F^{\mathrm{op}}_{\check B}$，使任意 $Y\to X$ 上每个 $\check G$-oper 的底层 $\check B$-挠子都典范地等于 $\mathcal F^{\mathrm{op}}_{\check B}$ 的拉回；相应的 $\operatorname{Bun}_{\check G}$ 中的点在连通分支意义下与辅助选择无关。

1. 取定主 $\mathfrak{sl}_2$ 三元组后构造 $X$ 上的典范 $\check B$-挠子。  
   *为什么*：讲义以引理形式断言其存在，未给构造。
2. 验证任意 oper 的底层 $\check B$-挠子都是它的拉回。  
   *为什么*：这一步使遗忘联络成为常值映射。

> 缺口：讲义只陈述该引理（§14.1）而未在本章证明；它被用来证明命题 14.1.1 并给出到 $\operatorname{Bun}_{\check G}$ 的常值映射。

*出处*：引理 14.1.4 / 原书 p.68


## 易错点

- 典范性依赖主 $\mathfrak{sl}_2$ 三元组的选择；只有 $\operatorname{Bun}_{\check G}$ 中的点在连通分支意义下与选择无关。
- 得到的是到 $\operatorname{Bun}_{\check G}$ 的常值映射，不是到 $\operatorname{LocSys}_{\check G}(X)$ 的常值映射（后者由 oper 的联络给出）。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§14.1 oper 作为 Hitchin 底空间上的挠子，p.68（PDF p.68），`源码/chapters/ch14.tex:39-44（引理 14.1.4 与常值映射方块）`

## 核验

状态：`external-confirmed`（2026-11-18）
- BD：https://math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf — “FB is isomorphic to a certain canonical B-bundle F0B which does not depend on F … F0B is the push-forward of the canonical (Aut0 O)-bundle … by a certain homomorphism iBσπ: Aut0 O → B”——支持“存在依赖主 sl2 三元组的典范 B̌-挠子，任意 oper 的底层 B̌-挠子典范等于其拉回”。
- BD：https://math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf — “i(Opg(X)) = π^{-1}(S) where π: LocSysG → BunG corresponds to forgetting the connection and S ⊂ BunG is the locally closed substack of G-bundles isomorphic to F0G”——支持“相应的 Bun_{Ǧ} 中的点在连通分支意义下与辅助选择无关”。

## 关联

- `glc/concept/opers-hitchin-torsor`
- `glc/concept/g-oper`
- `glc/concept/hitchin-base`
