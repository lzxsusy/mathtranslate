---
id: glc/concept/restricted-local-systems
type: concept
track: F
---

# 受限局部系统叠

> de Rham 之外层论里替换 $\operatorname{LocSys}_{\check G}$ 的受限叠，用取值在 $\operatorname{QLisse}(X)$ 里的张量函子描述。

**问题**：为什么换到 Betti／可构造层论时，谱侧不能原样用 $\operatorname{LocSys}_{\check G}$？

## 定义

对于 de Rham $D$ 模以外的层理论，前述论证中的谱叠要替换为受限局部系统叠（文献 [AGK20a]），非正式地记为 $\operatorname{LocSys}_{\check G}^{\mathrm{restr}}$。它可以用点函子描述：$\operatorname{LocSys}_{\check G}^{\mathrm{restr}}(S)=\{\operatorname{Rep}(\check G)\xrightarrow{\otimes}\operatorname{QCoh}(S)\otimes\operatorname{QLisse}(X)\}$，即取值在 $\operatorname{QLisse}(X)$ 中的张量函子；而在 de Rham 情形，将 $\operatorname{QLisse}(X)$ 替换为 $\operatorname{DMod}(X)$ 就有平行的表达式。

*记号*：$\operatorname{QLisse}(X)$ 是 quasi-lisse 局部系统范畴：$\operatorname{IndLisse}(X)$（Lisse 局部系统的 ind-完备化）的左完备化，即允许无穷直和的拟光滑对象（不是「拟凝聚的局部系统」）；$S$ 取遍测试概形，点函子给出叠的定义。

## 要点

- 受限局部系统叠用点函子描述为张量函子 $\operatorname{Rep}(\check G)\to\operatorname{QCoh}(S)\otimes\operatorname{QLisse}(X)$。
- de Rham 情形的平行表述是把 $\operatorname{QLisse}(X)$ 换成 $\operatorname{DMod}(X)$。
- 在 Betti／可构造情形，已知的因子化陈述落在具有幂零奇异支撑的范畴中，纲要上为 $\operatorname{Rep}(\check G)_{\mathrm{Ran}}^{\operatorname{QLisse}}\to\operatorname{QCoh}(\operatorname{LocSys}_{\check G}^{\mathrm{restr}})\to\operatorname{End}(D_{\mathrm{Nilp}}(\operatorname{Bun}_G))$。
- 因此它本身并不蕴涵整个 $D(\operatorname{Bun}_G)$ 上完整的消失定理。
- 对一般约化群，预期陈述相同：$V\in\operatorname{Rep}(\check G)$、$E$ 为不可约向量局部系统、$\operatorname{rank}(E)>\dim V$ 时，$\operatorname{Sym}^d(V\otimes E)$ 应在 $D(\operatorname{Bun}_G)$ 上作用为零，只要 $d>(2g-2)\dim(V\otimes E)$。
- de Rham 理论中这由广义消失定理加同样的上同调计算推出；在 $\ell$-进情形，这一表述中的相应陈述仍作为猜想性输入处理。

## 关键公式

- $\operatorname{LocSys}_{\check G}^{\mathrm{restr}}(S)=\{\operatorname{Rep}(\check G)\xrightarrow{\otimes}\operatorname{QCoh}(S)\otimes\operatorname{QLisse}(X)\}$
- $d>(2g-2)\dim(V\otimes E)\quad\Longrightarrow\quad\operatorname{Sym}^d(V\otimes E)\ \text{acts by zero on}\ D(\operatorname{Bun}_G)$

## 易错点

- Betti／可构造情形的因子化陈述只落在 $D_{\mathrm{Nilp}}(\operatorname{Bun}_G)$（幂零奇异支撑子范畴）里，不能据此宣布整个 $D(\operatorname{Bun}_G)$ 上的消失定理成立——讲义特意点明“它本身并不蕴涵”。
- 点函子把叠描述成“张量函子到 $\operatorname{QCoh}(S)\otimes\operatorname{QLisse}(X)$”，不要漏掉张量性：只写函子是把叠写大了。
- 一般约化群的门槛 $(2g-2)\dim(V\otimes E)$ 与 $\operatorname{GL}_m$ 的 $rm(2g-2)$ 一致（把 $V$ 换成 $\mathrm{St}_m$），但 $\ell$-进情形只是猜想性输入。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§9.5 其他层理论与一般约化群，p.51（PDF p.51），`§9.5 其他层理论与一般约化群（ch09.tex:101-109，p.51）`

## 核验

状态：`external-confirmed`（2026-11-18）
- Arinkin-Gaitsgory-Kazhdan-Raskin-Rozenblyum-Varshavsky, The stack of local systems with restricted variation and geometric Langlands theory with nilpotent singular support：https://arxiv.org/abs/2010.01906 — §0.5.4「Consider its ind-completion, denoted IndLisse(X). Finally, let QLisse(X) be the left completion of [IndLisse(X)]」，并说 S=Spec(A) 点时 LocSys^restr 的 S-点是对称幺半函子 Rep(G)→A-mod⊗QLisse(X)（右 t-正合）、e-点即 G-局部系统——支持卡中点函子定义与 de Rham 平行表述。
- Arinkin-Gaitsgory-Kazhdan-Raskin-Rozenblyum-Varshavsky, The stack of local systems with restricted variation and geometric Langlands theory with nilpotent singular support：https://arxiv.org/abs/2010.01906 — 同一段把 QLisse(X) 定义为有限秩局部系统范畴 Lisse(X) 的 ind-完备化 IndLisse(X) 在自然 t-结构下的左完备化（quasi-lisse），并非「拟凝聚的局部系统」；卡中 definition.notation 已按此写成「IndLisse 的左完备化」，与之一致。
- Beraldo, On the geometric Ramanujan conjecture：https://arxiv.org/abs/2103.17211 — Ber21 摘要「any cuspidal D-module on Bun_G is tempered」，§1.1.2 给出尖点定义 CT_P(F)=0（P 真抛物）——支持卡中「Betti/可构造情形落在 D_Nilp」与「本身不蕴涵整个 D(Bun_G) 的消失定理」的背景（讲义 ch09.tex:101-109 同述）。

## 关联

- `glc/concept/averaging-vanishing-theorem`
- `glc/concept/generalized-vanishing-theorem`
- `glc/concept/betti-categorical-conjecture`
