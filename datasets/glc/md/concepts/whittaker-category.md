---
id: glc/concept/whittaker-category
type: concept
track: C
---

# Whittaker 范畴

> Wh(Ġr_{G,x}) ≃ Rep(Ĝ)；取手征积分后预期整体化为 Rep(Ĝ) 的手征积分，Whittaker 模型因而是 Hecke 特征层与 LocSys_Ĝ 上层的桥。

**问题**：Whittaker 范畴的局部等价是什么，取手征积分后预期得到什么？

## 定义

上述局部陈述具有以下几何形式（讲义引 [Gai18]）：$\operatorname{Wh}(\dot{\operatorname{Gr}}_{G,x})\simeq\operatorname{Rep}(\check G)$。在曲线上取手征积分后，预期有 $\int_X^{\mathrm{ch}}\operatorname{Wh}(\dot{\operatorname{Gr}}_{G,x})\simeq\int_X^{\mathrm{ch}}\operatorname{Rep}(\check G)$。左边是对阿代尔 Whittaker 商的层论替代，右边则映到 $\check G$-局部系统叠上的拟凝聚层。

*记号*：$\dot{\operatorname{Gr}}_{G,x}$ 为 $\rho$ 移位的仿射 Grassmann 簇；$\int_X^{\mathrm{ch}}$ 为手征积分（讲义未在此定义，只说它是局部 Whittaker 范畴的整体化）；$\operatorname{LocSys}_{\check G}$ 为 $\check G$-局部系统叠。

## 要点

- 整体图景（讲义 p.22 的图）：$\operatorname{Shv}((\dot N(\mathbb{A}),\Psi)\backslash\dot G(\mathbb{A})/\dot G(\mathcal{O}))$ 对 $\operatorname{QCoh}(\operatorname{LocSys}_{\check G})$，经 $\operatorname{Av}_!$ 到 $\operatorname{Shv}(\dot Q_1(F)\backslash\dot G(\mathbb{A})/\dot G(\mathcal{O}))_{\mathrm{cusp}}$ 对 $\operatorname{QCoh}(\operatorname{LocSys}_{\check G}^{\mathrm{irred}})$，再经猜想箭头到 $\operatorname{Shv}(\operatorname{Bun}_G)_{\mathrm{cusp}}$ 对 $\operatorname{QCoh}(\operatorname{LocSys}_{\check G}^{\mathrm{irred}})$。
- 因此 Whittaker 模型是在 $\operatorname{Bun}_G$ 上的 Hecke 特征层与 $\operatorname{LocSys}_{\check G}$ 上的层之间建立联系的局部到整体桥梁。
- 右边映到的是「$\check G$-局部系统叠上的拟凝聚层」，不是表示范畴本身；局部等价里的 $\operatorname{Rep}(\check G)$ 只有取手征积分后才整体化为 $\operatorname{QCoh}(\operatorname{LocSys}_{\check G})$。
- $\delta_E$ 是局部系统 $E$ 处的摩天层，左边的手征积分是局部 Whittaker 范畴的整体化（讲义在紧接的图与 §3.7 末尾使用）。

## 关键公式

- $\operatorname{Wh}(\dot{\operatorname{Gr}}_{G,x})\simeq\operatorname{Rep}(\check G)$
- $\int_X^{\mathrm{ch}}\operatorname{Wh}(\dot{\operatorname{Gr}}_{G,x})\simeq\int_X^{\mathrm{ch}}\operatorname{Rep}(\check G)$

## 定理与证明

### Whittaker 形式的几何 Satake（讲义引 [Gai18]）（要点（有缺口））

$\operatorname{Wh}(\dot{\operatorname{Gr}}_{G,x})\simeq\operatorname{Rep}(\check G)$；取手征积分后期望 $\int_X^{\mathrm{ch}}\operatorname{Wh}(\dot{\operatorname{Gr}}_{G,x})\simeq\int_X^{\mathrm{ch}}\operatorname{Rep}(\check G)$。

1. 在局部取 Whittaker 范畴与 $\check G$ 表示范畴的等价。  
   *为什么*：讲义引 [Gai18]，未给证明。
2. 对曲线取手征积分，期望得到整体版本。  
   *为什么*：讲义用「预期有」，即尚未成为定理。

> 缺口：局部等价是 [Gai18] 的结果，讲义只引述；手征积分一侧讲义明说「预期」，属猜想性陈述，不是已证定理。

*出处*：§3.6（原书 p.22–23）


## 易错点

- 左边的 $\operatorname{Wh}$ 定义在 $\rho$ 移位的 $\dot{\operatorname{Gr}}_{G,x}$ 上；把 $\dot{\operatorname{Gr}}$ 换成普通 $\operatorname{Gr}$ 得到的是球面（Satake）版本而不是 Whittaker 版本。
- 手征积分那条是「预期」，不是定理；引用时不要把它和局部等价混为同一级别的陈述。
- 图景右下角是 $\operatorname{LocSys}_{\check G}^{\mathrm{irred}}$（不可约局部系统）而不是整个 $\operatorname{LocSys}_{\check G}$：从 $\operatorname{Av}_!$ 之后处处带 irred 上标。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§3.6 几何预览：Whittaker 范畴，p.22-23（PDF p.22-23），`源码/chapters/ch03.tex:106-125（§3.6）`

## 核验

状态：`source-only`（2026-11-18）
- Lurie：https://www.math.ias.edu/~lurie/papers/moduli.pdf — Wh(Gr_{G^∨})≃Rep(G)（卡：Wh(Ġr_{G,x})≃Rep(Ĝ)）
- nLab：https://ncatlab.org/nlab/show/geometric+Satake+equivalence — DMod(Gr_G)^{L^+G}≃Rep(^L G)（卡：D^Wh(Ġr)≃D^b(Rep(Ĝ)) 的球面版）
- nLab：https://ncatlab.org/nlab/show/Whittaker+function — 手征积分 ∫_X^ch 的两条对应

## 关联

- `glc/concept/local-whittaker-eigenfunction`
- `glc/concept/generic-reduction-whittaker`
- `glc/concept/laumon-sheaf`
