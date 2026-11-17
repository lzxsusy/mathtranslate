---
id: glc/concept/critical-kazhdan-lusztig-category
type: concept
track: H
---

# 临界 Kazhdan–Lusztig 范畴

> 临界水平 $\widehat{\mathfrak g}_{\mathrm{crit}}$ 的 $L^+G$-模范畴；FLE 把它等同于非分歧 oper 上的 IndCoh。

**问题**：真空生成子范畴上的几何 Satake 陈述与 FLE 的差别在哪里？

## 定义

令 $D=\operatorname{Spec} k[[t]]$、$D^\times=\operatorname{Spec} k((t))$、$L^+G=G[[t]]$、$LG=G((t))$。临界 Kazhdan–Lusztig 范畴定义为
$$\operatorname{KL}_{G,\mathrm{crit}}:=\widehat{\mathfrak g}_{\mathrm{crit}}\text{-}\mathrm{Mod}^{L^+G}.$$
定理 15.2.1（临界 FLE）断言它与 $\operatorname{IndCoh}(\operatorname{Op}^{\mathrm{unr}}_{\check G})$ 等价。

*记号*：$\widehat{\mathfrak g}_{\mathrm{crit}}$ 为临界水平的仿射 Kac–Moody 代数，$L^+G=G[[t]]$；上标 $L^+G$ 表示 $L^+G$-等变结构。$\operatorname{Rep}(\check G)$ 为对偶群的表示范畴，$\mathbb V_{\mathrm{crit}}$ 为真空模。

## 要点

- 上标「$\mathbb V$-生成」表示由真空模生成的子范畴。
- 对点 $x\in X$，Beilinson–Drinfeld 局部化函子给出 $\operatorname{Loc}_x:\widehat{\mathfrak g}_{\mathrm{crit},x}\text{-}\mathrm{Mod}^{L^+G_x}\longrightarrow\operatorname{DMod}_{\mathrm{crit}}(\operatorname{Bun}_G)$，而中心通过将局部 oper 上的函数拉回到全局 oper 来作用。
- 对 $V\in\operatorname{Rep}(\check G)$，几何 Satake 与临界全局截面给出 $\operatorname{Sat}_x(V)\star\mathbb V_{\mathrm{crit},x}\simeq F_x(V)\otimes_{\mathfrak z_{\mathrm{crit}}(D_x)}\mathbb V_{\mathrm{crit},x}$，其中 $F_x(V)$ 是 $\operatorname{Op}_{\check G}(D_x)\simeq\operatorname{Spec}\mathfrak z_{\mathrm{crit}}(D_x)$ 上与普遍 $\check G$-局部系统关联的向量丛。
- 基本局部等价用整个球面临界范畴的等价，替换这一真空生成的陈述。
- $\operatorname{Rep}(\check G)_{\mathrm{Ran}}$ 在整体自守范畴上的局部 Hecke 作用是 FLE 之外的另一个输入（§16.1 用它刻画粗 Langlands 函子）。

## 关键公式

- $\operatorname{KL}_{G,\mathrm{crit}}:=\widehat{\mathfrak g}_{\mathrm{crit}}\text{-}\mathrm{Mod}^{L^+G}$
- $\operatorname{Loc}_x:\widehat{\mathfrak g}_{\mathrm{crit},x}\text{-}\mathrm{Mod}^{L^+G_x}\longrightarrow\operatorname{DMod}_{\mathrm{crit}}(\operatorname{Bun}_G)$
- $\operatorname{Sat}_x(V)\star\mathbb V_{\mathrm{crit},x}\simeq F_x(V)\otimes_{\mathfrak z_{\mathrm{crit}}(D_x)}\mathbb V_{\mathrm{crit},x}$

## 易错点

- 把 $\operatorname{Sat}_x(V)\star\mathbb V_{\mathrm{crit},x}\simeq F_x(V)\otimes_{\mathfrak z_{\mathrm{crit}}(D_x)}\mathbb V_{\mathrm{crit},x}$ 当成 FLE：它只是真空生成子范畴上的陈述，FLE 的内容正是用整个球面临界范畴的等价替换它。
- $F_x(V)$ 是 $\operatorname{Op}_{\check G}(D_x)$ 上的向量丛，而 $\operatorname{Op}_{\check G}(D_x)\simeq\operatorname{Spec}\mathfrak z_{\mathrm{crit}}(D_x)$ 是 Feigin–Frenkel 型的中心识别；把 $F_x(V)$ 写成 $\mathbb V_{\mathrm{crit},x}$ 上的模会丢掉这一点。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§15.2 非分歧 oper，p.72（PDF p.72），`源码/chapters/ch15.tex:16-18（$\operatorname{KL}_{G,\mathrm{crit}}$ 的定义）`
- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§15.1 从 Beilinson–Drinfeld 到局部等价，p.72（PDF p.72），`源码/chapters/ch15.tex:7-13（$\operatorname{Loc}_x$ 与真空生成陈述）`

## 核验

状态：`source-only`（2026-11-18）
- Arinkin–Beraldo–Campbell–Chen–Færgeman–Gaitsgory–Lin–Raskin–Rozenblyum, Proof of the geometric Langlands conjecture II: Kac–Moody localization and the FLE：https://arxiv.org/abs/2405.03648 — 引言 0.1.1 把 KL(G)_{crit,Ran} 定义为临界水平、对弧群 L^+(G) 可积的 Kac–Moody 模；支持卡里 KL_{G,crit}:=ĝ_crit-Mod^{L^+G} 的定义与 FLE 的左右端。
- Frenkel–Gaitsgory, Local geometric Langlands correspondence: the spherical case：https://arxiv.org/abs/0711.1132 — 摘要与主定理：球面临界 ĝ_crit-mod^{G[[t]]} ≃ QCoh(Op^unr)；支持卡里 FLE 的球面情形与「用整个球面范畴替换真空生成陈述」。
- Frenkel–Gaitsgory, Local geometric Langlands correspondence: the spherical case：https://arxiv.org/abs/0711.1132 — 全文没有 Satake 字样，未找到 Loc_x 与 Sat_x(V)⋆V_crit ≃ F_x(V)⊗_{z_crit} V_crit 的逐字陈述。

## 关联

- `glc/concept/unramified-oper`
- `glc/concept/pointwise-fle`
- `glc/concept/spectral-satake-hecke`
