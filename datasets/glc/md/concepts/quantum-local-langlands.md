---
id: glc/concept/quantum-local-langlands
type: concept
track: H
---

# 量子局部 Langlands 与 FLE 的边界值

> 临界 FLE 是量子局部几何 Langlands 的边界值：水平由参数 $c$ 配对，$c\to0$ 的极限即 FLE。

**问题**：为什么说 FLE 是量子局部 Langlands 的「边界值」？

## 定义

临界 FLE 是量子局部几何 Langlands 的一个边界值。离开边界后，对偶水平满足关系
$$\kappa=\kappa_{G,\mathrm{crit}}+c\,\kappa_{\mathrm{Kil},G},\qquad \check\kappa=\kappa_{\check G,\mathrm{crit}}+c^{-1}\kappa_{\mathrm{Kil},\check G}.$$

*记号*：$\kappa$ 与 $\check\kappa$ 为对偶水平，$\kappa_{G,\mathrm{crit}}$ 为临界水平，$\kappa_{\mathrm{Kil},G}$ 为 Killing 型给出的水平；$c\ne0$ 是量子参数。$\operatorname{Gr}_G$ 为仿射 Grassmann 簇，$\mathcal{F}\ell_G$ 为仿射旗簇。

## 要点

- 当 $c\ne0$ 时，预期的局部等价具有形式 $\widehat{\mathfrak g}_{\kappa}\text{-}\mathrm{Mod}^{L^+G}\simeq\operatorname{Whit}(D_{\check\kappa}(\operatorname{Gr}_{\check G}))$。
- 它在边界上的对应形式是标准的 Satake 与 Casselman–Shalika 等价。
- 在大水平极限中，球面与 Whittaker Grassmann 簇范畴退化为 $D(\operatorname{Gr}_G)^{L^+G}_{\mathrm{sph}}\simeq\operatorname{Rep}(\check G)$ 与 $\operatorname{Whit}(D(\operatorname{Gr}_{\check G}))\simeq\operatorname{Rep}(G)$。
- 当 $c\to0$ 时，$G$ 侧变为临界水平，而 $\check G$-Whittaker 侧变为 oper 的经典谱几何；极限等价就是 FLE $\widehat{\mathfrak g}_{\mathrm{crit}}\text{-}\mathrm{Mod}^{L^+G}\simeq\operatorname{IndCoh}(\operatorname{Op}^{\mathrm{unr}}_{\check G})$。
- 这是更广的量子局部对应表中的一行：$LG\text{-}\mathrm{Mod}_{\kappa}\leftrightarrow L\check G\text{-}\mathrm{Mod}_{\check\kappa}$、$\widehat{\mathfrak g}_{\kappa}\text{-}\mathrm{Mod}\leftrightarrow\operatorname{Whit}(D_{\check\kappa}(L\check G))$、$\operatorname{Whit}(D_{\kappa}(LG))\leftrightarrow\widehat{\check{\mathfrak g}}_{\check\kappa}\text{-}\mathrm{Mod}$、$D_{\kappa}(\operatorname{Gr}_G)\leftrightarrow D_{\check\kappa}(\operatorname{Gr}_{\check G})$、$D_{\kappa}(\mathcal{F}\ell_G)\leftrightarrow D_{\check\kappa}(\mathcal{F}\ell_{\check G})$。
- 在 $\kappa=\kappa_{\mathrm{crit}}$ 时，预期整个局部 $LG$-模理论是 $\operatorname{LocSys}_{\check G}(D^\times)$ 上的范畴层：$LG\text{-}\mathrm{Mod}_{\mathrm{crit}}\rightsquigarrow\operatorname{ShvCat}(\operatorname{LocSys}_{\check G}(D^\times))$；经 Whittaker／Drinfeld–Sokolov 约化后，这个 oper 上的范畴被识别为 $\operatorname{IndCoh}(\operatorname{Op}_{\check G}(D^\times))$，与 Feigin–Frenkel 中心的识别 $\operatorname{Spf}Z_{\mathrm{crit}}\simeq\operatorname{Op}_{\check G}(D^\times)$ 相容。

## 关键公式

- $\kappa=\kappa_{G,\mathrm{crit}}+c\,\kappa_{\mathrm{Kil},G},\qquad \check\kappa=\kappa_{\check G,\mathrm{crit}}+c^{-1}\kappa_{\mathrm{Kil},\check G}$
- $\widehat{\mathfrak g}_{\kappa}\text{-}\mathrm{Mod}^{L^+G}\simeq\operatorname{Whit}(D_{\check\kappa}(\operatorname{Gr}_{\check G}))$
- $D(\operatorname{Gr}_G)^{L^+G}_{\mathrm{sph}}\simeq\operatorname{Rep}(\check G),\qquad\operatorname{Whit}(D(\operatorname{Gr}_{\check G}))\simeq\operatorname{Rep}(G)$
- $LG\text{-}\mathrm{Mod}_{\mathrm{crit}}\rightsquigarrow\operatorname{ShvCat}(\operatorname{LocSys}_{\check G}(D^\times))$

## 定理与证明

### 猜想（量子局部 Langlands，FLE 为其边界值）（要点（有缺口））

$c\ne0$ 时预期 $\widehat{\mathfrak g}_{\kappa}\text{-}\mathrm{Mod}^{L^+G}\simeq\operatorname{Whit}(D_{\check\kappa}(\operatorname{Gr}_{\check G}))$；$c\to0$ 时左端变为临界水平、右端变为 oper 的经典谱几何，极限即 FLE。

1. 水平由参数 $c$ 配对：当 $c\ne0$ 时预期上述量子局部等价。  
   *为什么*：边界上的对应形式是标准的 Satake 与 Casselman–Shalika 等价。
2. 在大水平极限中球面与 Whittaker 范畴退化为 $\operatorname{Rep}(\check G)$ 与 $\operatorname{Rep}(G)$；$c\to0$ 时 $G$ 侧变为临界水平，$\check G$-Whittaker 侧变为 oper 的经典谱几何。  
   *为什么*：两侧极限合起来就是 FLE，故 FLE 是该猜想在 $c\to0$ 的边界值。

> 缺口：讲义把它作为「预期」陈述，未证明；本书只用到其边界值 FLE。

*出处*：无编号陈述 / 原书 p.74


## 易错点

- 把 $c$ 当成自由参数：$c$ 是两侧水平之和偏离临界值的量，$c\to0$ 才是 FLE 所在的边界；$c\to\infty$ 或取别的值得到的是别的退化。
- 把 $c\ne0$ 的预期等价当成已证定理：讲义原文用「预期的局部等价」，非临界水平的局部 Langlands 在此只是预期。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§15.4 与量子局部 Langlands 的关系，p.74（PDF p.74），`源码/chapters/ch15.tex:66-93（水平关系、预期等价、极限与对应表）`

## 核验

状态：`source-only`（2026-11-18）
- nLab：https://ncatlab.org/nlab/show/quantum+geometric+Langlands+correspondence — 页面给出全局等价 D^{k,λ}Mod(Bun_G) ≃ \hat D^{1/k,λ}Mod(Bun_{^LG})，并说 k=∞ 时退化为 p_*(O_{Loc_G})；支持 FLE 作为量子族边界值这一图景，但未给局部 κ 公式。
- Frenkel–Gaitsgory, Local geometric Langlands correspondence and affine Kac–Moody algebras：https://arxiv.org/abs/math/0508382 — 摘要讨论临界水平局部 Langlands 与幂零 oper 加厚，支持临界点作为量子族边界；未给 κ=κ_{G,crit}+cκ_{Kil,G} 的公式。

## 关联

- `glc/concept/pointwise-fle`
- `glc/concept/spectral-satake-hecke`
- `glc/concept/factorization-fle`
