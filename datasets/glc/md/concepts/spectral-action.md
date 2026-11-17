---
id: glc/concept/spectral-action
type: concept
track: F
---

# 谱作用

> 预期谱侧的拟凝聚层作用在 $\operatorname{DMod}(\operatorname{Bun}_G)$ 上，$E$ 处纤维切出 $E$-Hecke 范畴。

**问题**：为什么逐点的 $\operatorname{Rep}(\check G)\otimes D(X)$ 作用不是所需的作用，而非要换成 Ran 空间上的因子化作用？

## 定义

在几何 Langlands 的 de Rham 形式中，纲要上预期有文献 [GR24a, AG15] 的谱作用及幂零支撑表述：$\operatorname{DMod}(\operatorname{Bun}_G)^{\mathrm{temp}}\simeq\operatorname{QCoh}(\operatorname{LocSys}_{\check G})$ 与 $\operatorname{DMod}(\operatorname{Bun}_G)\simeq\operatorname{IndCoh}_{\mathrm{Nilp}}(\operatorname{LocSys}_{\check G})$。将右边限制到紧对象，这常常启发式地表现为谱叠上的凝聚层，因此 $\operatorname{QCoh}(\operatorname{LocSys}_{\check G})$ 应当作用于 $\operatorname{DMod}(\operatorname{Bun}_G)$。这一作用并非任意：对 $E\in\operatorname{LocSys}_{\check G}$，纤维函子 $(-)_E:\operatorname{QCoh}(\operatorname{LocSys}_{\check G})\to\operatorname{Vect}$ 应通过基变换切出 $E$-Hecke 范畴，即 $\operatorname{DMod}(\operatorname{Bun}_G)\otimes_{\operatorname{QCoh}(\operatorname{LocSys}_{\check G})}\operatorname{Vect}\simeq\operatorname{DMod}(\operatorname{Bun}_G)_{E\text{-Hecke}}$，右边由 Hecke 变换可通过与局部系统 $E$ 作张量积得到的对象组成。

*记号*：$\check G$ 是 $G$ 的 Langlands 对偶群；$\operatorname{LocSys}_{\check G}$ 是 $X$ 上 de Rham $\check G$-局部系统的导出叠；$\operatorname{IndCoh}_{\mathrm{Nilp}}$ 是幂零奇异支撑的 ind-凝聚层范畴（第 10 章）。

## 要点

- 两个预期等价分别对应温和部分（$\operatorname{QCoh}$）与整体范畴（$\operatorname{IndCoh}_{\mathrm{Nilp}}$）。
- $\operatorname{QCoh}(\operatorname{LocSys}_{\check G})$ 作用于 $\operatorname{DMod}(\operatorname{Bun}_G)$，且该作用应使 $E$ 处的基变换切出 $E$-Hecke 范畴。
- $E$-Hecke 特征层是配备同构 $H_V(\mathcal{K})\simeq\mathcal{K}\boxtimes V_E$ 的对象 $\mathcal{K}$，同构对所有 $V\in\operatorname{Rep}(\check G)$ 给出，并配备 $X^I$ 上的高阶相容性。
- 在固定点 $x\in X$ 处几何 Satake 给出 $\operatorname{Rep}(\check G)\otimes D(\operatorname{Bun}_G)\to D(\operatorname{Bun}_G)$；让点移动则得到到 $D(\operatorname{Bun}_G\times X)$ 的函子。
- 朴素函子 $\operatorname{Rep}(\check G)\otimes D(X)\to\operatorname{End}(D(\operatorname{Bun}_G))$ 虽是函子却不是所需意义下的幺半函子：点碰撞时卷积由几何 Satake 的幺半结构控制，于是必须有 $H_{V,x}\circ H_{W,y}=H_{V,W;x,y}$（$x\ne y$）与 $H_{V,W;x,x}=H_{V\otimes W,x}$，这正是因子化条件。

## 关键公式

- $\operatorname{DMod}(\operatorname{Bun}_G)\otimes_{\operatorname{QCoh}(\operatorname{LocSys}_{\check G})}\operatorname{Vect}\simeq\operatorname{DMod}(\operatorname{Bun}_G)_{E\text{-Hecke}}$
- $H_V(\mathcal{K})\simeq\mathcal{K}\boxtimes V_E$

## 易错点

- 讲义说这两个等价是“纲要上预期”的启发式，不是已证定理；不要把它们当成可直接引用的定理。
- 特征层的同构要对所有 $V\in\operatorname{Rep}(\check G)$ 同时成立并带 $X^I$ 上的高阶相容性，只对单个 $V$ 给出同构不够。
- 把 $\operatorname{Rep}(\check G)\otimes D(X)$ 的作用当成幺半作用：$x\ne y$ 与 $x=y$ 两种情形的复合规则不同，缺了因子化条件就只是函子。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§9.2 谱作用的启发式解释，p.48-49（PDF p.48-49），`§9.2 谱作用的启发式解释（ch09.tex:19-42，p.48-49）`

## 核验

状态：`external-confirmed`（2026-11-18）
- Gaitsgory-Raskin, Proof of the geometric Langlands conjecture I: construction of the functor：https://arxiv.org/abs/2405.03599 — §0.3.6 引入局部化 u: D-mod(Bun_G)^temp ⇄ D-mod(Bun_G): u_R，并说「The tempered version of GLC says that the functor L_{G,temp} is an equivalence」，其中 L_{G,temp}: D-mod(Bun_G)^temp → QCoh(LS_Ǧ)——支持卡中「纲要上预期 DMod(Bun_G)^temp ≃ QCoh(LocSys_Ǧ)」（以温和 Langlands 的形式陈述）。
- Gaitsgory, Recent progress in geometric Langlands theory (Seminaire Bourbaki, talk of 2016-02-16)：https://arxiv.org/abs/1606.09462 — §3.3 引入 IndCoh_Nilp(LocSys) 修正并陈述 Conjecture 3.3.4：L_G: IndCoh_Nilp(LocSys) → D(Bun_G) 为等价；Remark 3.3.5 说 Arthur 参数是对象落入 QCoh(LocSys) 本质像（temperedness）的障碍——支持卡中第二条预期等价及「Nilp 下标」。
- Gaitsgory-Raskin, Proof of the geometric Langlands conjecture I: construction of the functor：https://arxiv.org/abs/2405.03599 — 「Loc^spec_Ǧ: Rep(Ǧ)_Ran → QCoh(LS_Ǧ)」是幺半局部化（右伴随全忠实），Theorem 1.2.4「The action of Rep(Ǧ)_Ran on D-mod(Bun_G) factors via the functor (1.2)」，§1.2.5「We refer to it as the spectral action」——支持卡中「QCoh 应当作用于 DMod(Bun_G)」及谱作用之名。
- nLab, geometric Satake equivalence：https://ncatlab.org/nlab/show/geometric+Satake+equivalence — 原文「one has an equivalence of symmetric monoidal abelian categories DMod(Gr_G)^{L^+G} ≃ Rep(^L G)」——支持卡中「Rep(Ǧ) 是球面范畴的 Satake 心」这一前提。

## 关联

- `glc/concept/averaging-vanishing-theorem`
- `glc/concept/ran-hecke-action`
- `glc/concept/categorical-langlands-conjecture`
