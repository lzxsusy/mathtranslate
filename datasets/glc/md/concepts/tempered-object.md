---
id: glc/concept/tempered-object
type: concept
track: F
---

# 温和对象与 Færgeman–Raskin 定理

> 用球面 Hecke 作用经左完备化的谱 Hecke 范畴分解来定义温和对象；所得子范畴与所选点无关。

**问题**：温和性为什么用球面 Hecke 作用来定义，而不用 Whittaker 系数？

## 定义

对每个 $x\in X$，范畴 $\operatorname{Sph}_{G,x}$ 以幺半方式作用于 $\operatorname{DMod}(\operatorname{Bun}_G)$。在导出 Satake 等价下 $\operatorname{Sph}_{G,x}\simeq\operatorname{IndCoh}_{\mathrm{Nilp}}(\mathrm{pt}/\check G\times_{\check{\mathfrak g}/\check G}\mathrm{pt}/\check G)$，而温和的、也称为左完备化的谱 Hecke 范畴是 $\operatorname{QCoh}(\mathrm{pt}/\check G\times_{\check{\mathfrak g}/\check G}\mathrm{pt}/\check G)$。若由 $\mathcal{F}\in\operatorname{DMod}(\operatorname{Bun}_G)$ 生成的 $\operatorname{Sph}_{G,x}$-模经由上述左完备化范畴分解，则称 $\mathcal{F}$ 是温和的。

*记号*：$\operatorname{Sph}_{G,x}$ 是局部球面范畴；左完备化指把 $\operatorname{IndCoh}_{\mathrm{Nilp}}$ 换成 $\operatorname{QCoh}$ 的谱 Hecke 范畴；“由 $\mathcal{F}$ 生成的 $\operatorname{Sph}_{G,x}$-模”指 $\operatorname{Sph}_{G,x}$ 作用于 $\mathcal{F}$ 所张成的模。

## 要点

- $\operatorname{Sph}_{G,x}$ 幺半作用于 $\operatorname{DMod}(\operatorname{Bun}_G)$（对每个 $x\in X$）。
- 导出 Satake 下 $\operatorname{Sph}_{G,x}\simeq\operatorname{IndCoh}_{\mathrm{Nilp}}(\mathrm{pt}/\check G\times_{\check{\mathfrak g}/\check G}\mathrm{pt}/\check G)$。
- 温和（左完备化）的谱 Hecke 范畴是 $\operatorname{QCoh}(\mathrm{pt}/\check G\times_{\check{\mathfrak g}/\check G}\mathrm{pt}/\check G)$——与上一条只差把 $\operatorname{IndCoh}_{\mathrm{Nilp}}$ 换成 $\operatorname{QCoh}$。
- 定义：若由 $\mathcal{F}$ 生成的 $\operatorname{Sph}_{G,x}$-模经该左完备化范畴分解，则 $\mathcal{F}$ 温和。
- Færgeman–Raskin 定理（[FR23]）：由此得到的子范畴与所选的点 $x$ 无关。
- 思想背景：温和部分是可被 Whittaker 系数检测到的部分；局部输入是仿射 Grassmann 簇 Whittaker 范畴的手征同调与 $\operatorname{Rep}(\check G)$ 的手征同调相匹配，但这只给生成对象，单凭它不能识别定义温和子范畴的 Verdier 商。

## 关键公式

- $\operatorname{Sph}_{G,x}\simeq\operatorname{IndCoh}_{\mathrm{Nilp}}(\mathrm{pt}/\check G\times_{\check{\mathfrak g}/\check G}\mathrm{pt}/\check G),\qquad \operatorname{QCoh}(\mathrm{pt}/\check G\times_{\check{\mathfrak g}/\check G}\mathrm{pt}/\check G)$

## 定理与证明

### Færgeman–Raskin 定理（§10.5）（要点（有缺口））

由上述定义得到的温和子范畴与所选的点 $x\in X$ 无关。

1. 讲义直接引用 [FR23] 的结论，未复述证明。  
   *为什么*：该定理的作用是保证用球面 Hecke 作用给出的温和性定义不依赖点 $x$，从而可以逐点检验。

> 缺口：讲义只引用 [FR23] 的结论，未给证明。

*出处*：§10.5 / 原书 p.56


## 易错点

- 温和性是对“由 $\mathcal{F}$ 生成的 $\operatorname{Sph}_{G,x}$-模”提的条件，不是对 $\mathcal{F}$ 本身逐点提的条件。
- 左完备化的谱 Hecke 范畴用 $\operatorname{QCoh}$，导出 Satake 用 $\operatorname{IndCoh}_{\mathrm{Nilp}}$：同一叠上两个范畴差在奇异支撑条件，这正是温和与整体的差别。
- Whittaker 系数只提供生成对象与思想背景，单凭它不能识别定义温和子范畴的 Verdier 商——实际定义用的是球面 Hecke 作用。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§10.5 温和对象与 Whittaker 检测，p.56（PDF p.56），`§10.5 温和对象与 Whittaker 检测（ch10.tex:117-127，p.56）`

## 核验

状态：`source-only`（2026-11-18）
- arXiv：https://arxiv.org/abs/2108.02719 — 摘要：AG 定义 Bun_G 上的 tempered D-modules，猜想等价于 LocSys_Ĝ 上的 QCoh（not ind-coherent!）；定义依赖曲线上的辅助点，他们猜想与点无关，本文给出无条件证明。支持本卡「DMod(Bun_G)^temp≃QCoh(LocSys_Ĝ)」与 FR23 子范畴与 x 无关。摘要未提 Sph 幺半作用或左完备化定义。
- nLab：https://ncatlab.org/nlab/show/geometric+Langlands+correspondence — 页面只给全局猜想/Nilp_Glob 条件与证明状态，未给 Sph_{G,x} 作用、左完备化 QCoh 或「生成的模分解」这一定义。

## 关联

- `glc/concept/tempered-categorical-conjecture`
- `glc/concept/derived-satake`
- `glc/concept/tempered-quotient`
