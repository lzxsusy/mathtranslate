---
id: glc/concept/betti-local-to-global
type: concept
track: G
---

# Betti 局部到整体定理

> 谱范畴 $\operatorname{Perf}(\operatorname{Maps}(Y,B\check G))$ 在可对偶 DG 范畴上的作用，由与有限集映射相容的一族幺半函子编码。

**问题**：为什么单个谱范畴 $\operatorname{Perf}(\operatorname{Maps}(Y,B\check G))$ 能编码所有有限集合上的 Hecke 相容性？

## 定义

设 $Y$ 为同伦型，$\mathcal C$ 为可对偶 DG 范畴。Betti 局部到整体定理断言：谱幺半范畴 $\operatorname{Perf}(\operatorname{Maps}(Y,B\check G))$ 在 $\mathcal C$ 上的作用，或者在允许相应完备化时它的可呈示 $\operatorname{QCoh}$-完备化的作用，由下列因子化数据编码：对每个有限集合 $I$，有幺半函子
$$\operatorname{Rep}(\check G)^{\otimes I}\longrightarrow\operatorname{End}(\mathcal C)\otimes\operatorname{LocSys}(Y^I),$$
并且与有限集合之间的所有映射相容。

*记号*：$\operatorname{Perf}$ 为紧对象（完美复形）范畴；$\operatorname{End}(\mathcal C)$ 为自函子范畴；$Y^I$ 为 $I$ 重积；$\operatorname{Rep}(\check G)^{\otimes I}$ 为张量幂。

## 要点

- 对每个有限集合 $I$ 给出一枚幺半函子 $\operatorname{Rep}(\check G)^{\otimes I}\to\operatorname{End}(\mathcal C)\otimes\operatorname{LocSys}(Y^I)$。
- 这族函子与有限集合之间的所有映射相容。
- 若 $I\to J$ 是这样的映射，则相应的对角映射 $\Delta:Y^J\to Y^I$ 给出相容性方块，其纵向映射为 $\operatorname{Id}\otimes\Delta^*$。
- 要点在于：单个谱范畴 $\operatorname{Perf}(\operatorname{Maps}(Y,B\check G))$，或它的 $\operatorname{QCoh}$-完备化，把所有有限集合上的 Hecke 相容性统一编码起来。

## 关键公式

- $$\operatorname{Rep}(\check G)^{\otimes I}\longrightarrow\operatorname{End}(\mathcal C)\otimes\operatorname{LocSys}(Y^I)$$
- $$\operatorname{Id}\otimes\Delta^*:\operatorname{End}(\mathcal C)\otimes\operatorname{LocSys}(Y^I)\longrightarrow\operatorname{End}(\mathcal C)\otimes\operatorname{LocSys}(Y^J)$$

## 定理与证明

### Betti 局部到整体定理（要点（有缺口））

谱幺半范畴 $\operatorname{Perf}(\operatorname{Maps}(Y,B\check G))$（或其可呈示 $\operatorname{QCoh}$-完备化）在可对偶 DG 范畴 $\mathcal C$ 上的作用，由与有限集映射相容的一族幺半函子 $\operatorname{Rep}(\check G)^{\otimes I}\to\operatorname{End}(\mathcal C)\otimes\operatorname{LocSys}(Y^I)$ 编码。

1. 把 $\operatorname{Perf}(\operatorname{Maps}(Y,B\check G))$ 的作用限制到各张量因子，得到 $I$ 参数族的幺半函子。  
   *为什么*：$\operatorname{Rep}(\check G)^{\otimes I}$ 由各因子的表示张成。
2. 对 $I\to J$ 用对角映射 $\Delta:Y^J\to Y^I$ 的拉回 $\Delta^*$ 写出相容方块。  
   *为什么*：拉回沿对角映射兼容，正是因子化结构的相容性。

> 缺口：讲义只陈述定理（p.60–61），未给证明；证明见 [NY19]、[AGK20a]。

*出处*：定理（Betti 局部到整体定理，§12.2，讲义无编号） / 原书 p.60–61


## 易错点

- 不要把「作用由因子化数据编码」读成「作用与谱范畴同构」：这里编码的是作用本身；并且只有在允许相应完备化时才可换成 $\operatorname{QCoh}$-完备化。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§12.2 Betti 局部到整体定理，p.60-61（PDF p.60-61），`源码/chapters/ch12.tex:33-40（局部到整体定理，§12.2，跨 p.60–61）`

## 核验

状态：`source-only`（2026-11-18）
- arXiv:2010.01906 (AGK20a)：https://arxiv.org/abs/2010.01906 — 受限 QLisse 版本：QCoh(LocSys^restr) 作用与 Rep(Ĝ)^{⊗X-lisse} 作用之间的映射是同构；不是卡中 Betti 因子化数据的逐字陈述。
- arXiv:1611.04078 (NY19)：https://arxiv.org/abs/1611.04078 — 幂零奇异支撑层上的 Hecke 作用沿 X 局部常值，从而给出 Betti 模叠 Loc_{Ĝ}(X) 上完美复形的作用；只支持 Betti 作用的存在性，不含卡中的有限集因子化公式。

## 关联

- `glc/concept/betti-spectral-stack`
- `glc/concept/hecke-lisse-sheaves`
- `glc/concept/derham-ran-construction`
