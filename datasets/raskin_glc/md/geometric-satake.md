# 几何 Satake 等价

- id：`raskin_glc/concept/geometric-satake`
- 类型：concept　轨道：D　状态：dev
- 一句话：局部 Hecke 叠 $L^+G\backslash LG/L^+G$ 上的反常层范畴与 $\operatorname{Rep}(\check G)$ 等价，$V\mapsto\mathcal{S}_V$；整体 Hecke 函子 $\mathrm{H}_V$ 用它定义。

**问题**：为什么几何 Satake 的卷积积对应 $\operatorname{Rep}(\check G)$ 的张量积，而不是某种更大的结构？

## 定义

设 $x\in X$，$L_xG=G(k((t_x)))$，$L^+_xG=G(k[[t_x]])$。局部 Hecke 叠为 $\operatorname{Hecke}^{\mathrm{loc}}_x:=L^+_xG\backslash L_xG/L^+_xG$，它分类 $D_x=\operatorname{Spec} k[[t_x]]$ 上两个 $G$-丛及其在 $D_x^\circ$ 上的同构。几何 Satake 等价断言：存在典范幺半函子 $\operatorname{Rep}(\check G)\to\operatorname{Shv}(\operatorname{Hecke}^{\mathrm{loc}}_x)$，$V\mapsto\mathcal{S}_V$，它是范畴等价（到适当的反常层子范畴）。

记号：$L_xG$ 为圈群；$L^+_xG$ 为正圈群；$\operatorname{Hecke}^{\mathrm{loc}}_x$ 为局部 Hecke 叠；$\mathcal{S}_V$ 为 $V$ 对应的 Satake 层。

## 要点

- 几何 Satake 是「局部」陈述：只依赖 $x$ 处的形式圆盘 $D_x$，不依赖整体曲线 $X$；因此 $\mathcal{S}_V$ 与 $t_x$ 的选取无关（原文 Remark）。
- 整体 Hecke 函子 $\mathrm{H}_{V,x}(\mathcal{F}):=\overrightarrow{h}_*(\overleftarrow{h}^!\mathcal{F}\otimes^!\pi^!\mathcal{S}_V)$ 把局部 Satake 层 $\mathcal{S}_V$ 沿整体 Hecke 对应拉回，得到 $\operatorname{Bun}_G\times X$ 上的层。
- 卷积积对应张量积：$\mathrm{H}_{V_1,x}\circ\mathrm{H}_{V_2,x}\cong\mathrm{H}_{V_1\otimes V_2,x}$（练习 4.1.6），这正是 Satake 幺半性的整体体现。
- 对 $G=\mathrm{PGL}_2$，$\check G=\mathrm{SL}_2$，$V=\mathrm{std}$ 时 $\mathrm{H}_{\mathrm{std}}$ 回到 §3.3 的 Hecke 作用（练习 4.1.5）。
- 几何 Satake 的证明用仿射 Grassmann 簇的卷积与 perverse 层的 Beilinson–Drinfeld–Gaitsgory 分解；它不是本文的证明目标，而是作为黑箱引用。

## 公式

$$ \operatorname{Rep}(\check G)\simeq\operatorname{Shv}(L^+_xG\backslash L_xG/L^+_xG) $$

$$ \mathrm{H}_{V,x}(\mathcal{F}):=\overrightarrow{h}_*\left(\overleftarrow{h}^!\mathcal{F}\otimes^!\pi^!\mathcal{S}_V\right) $$

$$ \mathrm{H}_{V_1,x}\circ\mathrm{H}_{V_2,x}\cong\mathrm{H}_{V_1\otimes V_2,x} $$

## 定理与证明状态

### 定理 4.1.2（几何 Satake）

存在典范幺半函子 $\operatorname{Rep}(\check G)\to\operatorname{Shv}(\operatorname{Hecke}^{\mathrm{loc}}_x)$，$V\mapsto\mathcal{S}_V$，且它是范畴等价。

- 证明状态：`cited`
- 说明：归功于 Mirković–Vilonen（以及 Beilinson–Drinfeld 的框架）；讲义只引用，不证明。
- 出处：§4.1，原文 p.12

### 练习 4.1.5 / 4.1.6

(4.1.5) 对 $G=\mathrm{PGL}_2$、$\check G=\mathrm{SL}_2$、$V=\mathrm{std}$，$\mathrm{H}_{\mathrm{std}}$ 与 §3.3 的 Hecke 作用一致；(4.1.6) $\mathrm{H}_{V_1,x}\circ\mathrm{H}_{V_2,x}\cong\mathrm{H}_{V_1\otimes V_2,x}$。

- 证明状态：`none`
- 说明：练习；按定义与 Satake 幺半性展开。
- 出处：§4.1，原文 p.13

## 易错点

- 局部 Hecke 叠 $L^+G\backslash LG/L^+G$ 不是整体 $\operatorname{Bun}_G$ 的 Hecke 叠；前者只记录一个点的形式数据，后者记录整条曲线上的修改。
- $\mathcal{S}_V$ 是 Hecke 叠上的层，$V_\sigma$ 是 $X$ 上的局部系统，二者不能混：前者是「核」，后者是「本征值」。
- $L^+_xG=G(k[[t_x]])$ 依赖 $x$ 的局部参数 $t_x$；Satake 层 $\mathcal{S}_V$ 不依赖 $t_x$ 的选取，但 $H_{V,x}$ 的定义里出现了 $\pi^!\mathcal{S}_V$，需把 $\mathcal{S}_V$ 沿 $\pi$ 拉回。
- 几何 Satake 是等价，不是仅仅「有函子」；忘记全忠实/本质满射会把 Hecke 特征层的分类问题看轻。

## 出处

- Sam Raskin 讲授、Lin Chen 笔记《Notes for "Geometric Langlands for Projective Curves"》（2025-07-07/11，18 页），§4.1 几何 Satake 与 Hecke 函子，pp. 12, 13；`源码/sections/s04-hecke.tex:L48-L110（Theorem 4.1.2 与 Definition 4.1.4）`
  > Theorem 4.1.2 (Geometric Satake). ... Rep(Ĝ) → Shv(L^+_xG \ L_xG / L^+_xG), V ↦ S_V.

## 相关卡

- `raskin_glc/concept/hecke-eigensheaf`
- `raskin_glc/concept/pgl2-geometric-langlands`

## 核验（source-only，2026-11-27）

- 无外部逐条核验；见上方说明。

未抓取 nLab 的 geometric Satake 条目正文，故不写外部核验；定理以原文 §4.1 与 Mirković–Vilonen 为准。
