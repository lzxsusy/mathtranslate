---
id: glc/concept/quantum-local-gl
type: concept
track: O
---

# 量子局部几何 Langlands（猜想）

> 扭曲 $D$ 模变形：应有几乎等价 $LG\text{-}\mathrm{Mod}_\kappa\simeq L\check{G}\text{-}\mathrm{Mod}_{\check\kappa}$，且关于 $G$ 与对偶群对称。

**问题**：量子局部几何 Langlands 的等价在哪两个范畴之间，五个自守对象怎样配对？

## 定义

设定同猜想 1.4.1：$D^\circ=\operatorname{Spec} K_v$ 是穿孔圆盘，$LG$ 是环路群，$\operatorname{DMod}_\kappa$ 表示扭曲 $D$ 模，$\mathrm{KM}_{\mathfrak{g},\kappa}$ 是水平 $\kappa$ 下仿射 Lie 代数 $\widehat{\mathfrak{g}}$ 的表示范畴。猜想断言存在几乎等价 $LG\text{-}\mathrm{Mod}_\kappa\simeq L\check{G}\text{-}\mathrm{Mod}_{\check\kappa}$，具有五组对应：$\operatorname{DMod}_\kappa(\operatorname{Gr}_G)\mapsto\operatorname{DMod}_{\check\kappa}(\operatorname{Gr}_{\check{G}})$，$\operatorname{DMod}_\kappa(\mathcal{F}\ell_G)\mapsto\operatorname{DMod}_{\check\kappa}(\mathcal{F}\ell_{\check{G}})$，$\operatorname{DMod}_\kappa(\operatorname{Bun}_G^{\infty;v})\mapsto\operatorname{DMod}_{\check\kappa}(\operatorname{Bun}_{\check{G}}^{\infty;v})$，$\operatorname{Whit}_\kappa(LG)\mapsto\mathrm{KM}_{\check{\mathfrak{g}},\check\kappa}$，$\mathrm{KM}_{\mathfrak{g},\kappa}\mapsto\operatorname{Whit}_{\check\kappa}(L\check{G})$。

*记号*：$\kappa$ 与 $\check{\kappa}$：$G$ 与其对偶群 $\check{G}$ 上配对的两个水平；$\operatorname{DMod}_\kappa$：扭曲 $D$ 模；$\operatorname{Whit}_\kappa$：相应水平的 Whittaker 模型；$\mathrm{KM}_{\check{\mathfrak{g}},\check\kappa}$：$\check{G}$ 一侧水平 $\check\kappa$ 的表示范畴（与猜想 1.4.1 不同，这里不取临界水平）。

## 要点

- 量子形式由扭曲 $D$ 模（$\operatorname{DMod}_\kappa$）给出，是猜想 1.4.1 的变形。
- 预期的量子局部等价关于 $G$ 及其 Langlands 对偶群是对称的：两边分别是 $LG\text{-}\mathrm{Mod}_\kappa$ 与 $L\check{G}\text{-}\mathrm{Mod}_{\check\kappa}$。
- 最后一对对应是互换：$\operatorname{Whit}_\kappa(LG)$ 对应 $\mathrm{KM}_{\check{\mathfrak{g}},\check\kappa}$，而 $\mathrm{KM}_{\mathfrak{g},\kappa}$ 对应 $\operatorname{Whit}_{\check\kappa}(L\check{G})$。
- 这个表格的对称性，就是 Langlands 对偶的量子版本。

## 关键公式

- $LG\text{-}\operatorname{Mod}_\kappa\simeq L\check{G}\text{-}\operatorname{Mod}_{\check\kappa}$
- $\begin{aligned}\operatorname{DMod}_\kappa(\operatorname{Gr}_G)&\longmapsto\operatorname{DMod}_{\check\kappa}(\operatorname{Gr}_{\check{G}}),\\ \operatorname{DMod}_\kappa(\mathcal{F}\ell_G)&\longmapsto\operatorname{DMod}_{\check\kappa}(\mathcal{F}\ell_{\check{G}}),\\ \operatorname{DMod}_\kappa(\operatorname{Bun}_G^{\infty;v})&\longmapsto\operatorname{DMod}_{\check\kappa}(\operatorname{Bun}_{\check{G}}^{\infty;v}),\\ \operatorname{Whit}_\kappa(LG)&\longmapsto\mathrm{KM}_{\check{\mathfrak{g}},\check\kappa},\\ \mathrm{KM}_{\mathfrak{g},\kappa}&\longmapsto\operatorname{Whit}_{\check\kappa}(L\check{G})\end{aligned}$

## 定理与证明

### 猜想 1.5.1（量子局部几何 Langlands）（要点（有缺口））

存在几乎等价 $LG\text{-}\mathrm{Mod}_\kappa\simeq L\check{G}\text{-}\mathrm{Mod}_{\check\kappa}$，关于 $G$ 与其 Langlands 对偶群对称，并具有五组对应：$\operatorname{DMod}_\kappa(\operatorname{Gr}_G)\mapsto\operatorname{DMod}_{\check{\kappa}}(\operatorname{Gr}_{\check{G}})$，$\operatorname{DMod}_\kappa(\mathcal{F}\ell_G)\mapsto\operatorname{DMod}_{\check{\kappa}}(\mathcal{F}\ell_{\check{G}})$，$\operatorname{DMod}_\kappa(\operatorname{Bun}_G^{\infty;v})\mapsto\operatorname{DMod}_{\check{\kappa}}(\operatorname{Bun}_{\check{G}}^{\infty;v})$，$\operatorname{Whit}_\kappa(LG)\mapsto\mathrm{KM}_{\check{\mathfrak{g}},\check{\kappa}}$，$\mathrm{KM}_{\mathfrak{g},\kappa}\mapsto\operatorname{Whit}_{\check{\kappa}}(L\check{G})$。


> 缺口：这是猜想：讲义只陈述等价与对应表，未证明。

*出处*：猜想 1.5.1 / 原书 p.11


## 易错点

- 两边都带扭曲：$\kappa$ 与 $\check{\kappa}$ 是配对的两个水平，不能把右边写成未扭曲的 $\operatorname{DMod}$。
- $\operatorname{Whit}$ 与 $\mathrm{KM}$ 在表中互换位置（$\operatorname{Whit}_\kappa(LG)\leftrightarrow\mathrm{KM}_{\check{\mathfrak{g}},\check\kappa}$，$\mathrm{KM}_{\mathfrak{g},\kappa}\leftrightarrow\operatorname{Whit}_{\check\kappa}(L\check{G})$），不是各自对应自己。
- 这是「几乎」等价，与猜想 1.4.1 一样掩盖了凝聚/重整化的技术性不匹配。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§1.5 量子局部几何 Langlands 等价，p.11（PDF p.11），`源码/chapters/ch01.tex:295-308（猜想 1.5.1）`

## 核验

状态：`source-only`（2026-11-18）
- nLab：https://ncatlab.org/nlab/show/quantum+geometric+Langlands+correspondence — 页面陈述量子整体对应 D^{k,λ}Mod(Bun_G)≃D̂^{1/k,λ}Mod(Bun_{^L G})，两边带对偶扭曲；abelian case 由 Fourier–Mukai 构造（Polishchuk–Rothstein）。这支持卡里「两边都扭曲、关于 G 与 Ĝ 对称」的总体形状，但没有陈述局部 LG-Mod_κ≃LĜ-Mod_κ̂ 或五行对应表。

## 关联

- `glc/concept/local-gl-schematic`
- `glc/concept/cuspidal-de-rham`
- `glc/concept/unramified-global-gl`
