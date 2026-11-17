---
id: glc/concept/ran-hecke-action
type: concept
track: F
---

# Ran 空间与 Ran Hecke 作用

> 用 Ran 空间把逐点 Hecke 作用粘成因子化幺半作用，再由局部化函子落到谱叠的拟凝聚层上。

**问题**：为什么 Hecke 函子的正确参数空间是 Ran 空间，而不是 $X$ 或 $X^I$？

## 定义

令 $\operatorname{Ran}(X)=\{I\subset X\mid 0<|I|<\infty\}$，它理解为各幂 $X^I$ 沿满射所形成的余极限。因子化范畴 $\operatorname{Rep}(\check G)_{\mathrm{Ran}}$ 在有限集合 $I\subset X$ 上的纤维为 $\bigotimes_{x\in I}\operatorname{Rep}(\check G)$，点碰撞时进行融合。Hecke 函子组合成幺半作用 $\operatorname{Rep}(\check G)_{\mathrm{Ran}}\to\operatorname{End}(\operatorname{DMod}(\operatorname{Bun}_G))$。还有幺半“局部化”函子 $\operatorname{Loc}_{\check G}:\operatorname{Rep}(\check G)_{\mathrm{Ran}}\to\operatorname{QCoh}(\operatorname{LocSys}_{\check G})$，它将集合 $(V_x)_{x\in I}$ 映为 $\operatorname{LocSys}_{\check G}$ 上的取值向量丛 $\bigotimes_{x\in I}V_{E,x}$。

*记号*：$I$ 取遍 $X$ 的非空有限子集；沿满射 $I\twoheadrightarrow J$ 的余极限把带标号的点粘成任意有限子集；$\bigotimes_{x\in I}$ 是张量积而非直积，因为 $\operatorname{Rep}(\check G)$ 是张量范畴。

## 要点

- $\operatorname{Ran}(X)$ 是各幂 $X^I$ 沿满射的余极限，点碰撞时发生融合。
- 纤维写成 $\bigotimes_{x\in I}\operatorname{Rep}(\check G)$ 而不是 $\prod$：纤维里的对象是各点处表示的张量积。
- Hecke 函子组合成幺半作用 $\operatorname{Rep}(\check G)_{\mathrm{Ran}}\to\operatorname{End}(\operatorname{DMod}(\operatorname{Bun}_G))$。
- 局部化函子把 $(V_x)_{x\in I}$ 送到谱叠上的取值向量丛 $\bigotimes_{x\in I}V_{E,x}$。
- 定理 9.3.1（Gaitsgory–Lurie）：$\operatorname{Loc}_{\check G}$ 把 $\operatorname{QCoh}(\operatorname{LocSys}_{\check G})$ 实现为 $\operatorname{Rep}(\check G)_{\mathrm{Ran}}$ 的 Verdier 商；等价地，其右伴随全忠实。
- 该定理的证明在形式上来自 $\operatorname{LocSys}_{\check G}=\{B\check G\times X\to X\text{ 的水平截面}\}$ 这一描述，同一论证适用于任何配备相对于 $X$ 的联络的叠 $Z\to X$。

## 关键公式

- $\operatorname{Ran}(X)=\{I\subset X\mid 0<|I|<\infty\}$
- $\operatorname{Loc}_{\check G}:\operatorname{Rep}(\check G)_{\mathrm{Ran}}\longrightarrow\operatorname{QCoh}(\operatorname{LocSys}_{\check G}),\qquad (V_x)_{x\in I}\longmapsto\bigotimes_{x\in I}V_{E,x}$

## 定理与证明

### Gaitsgory–Lurie，局部到整体（定理 9.3.1）（要点（有缺口））

局部化函子 $\operatorname{Loc}_{\check G}$ 将 $\operatorname{QCoh}(\operatorname{LocSys}_{\check G})$ 实现为 $\operatorname{Rep}(\check G)_{\mathrm{Ran}}$ 的 Verdier 商。等价地，$\operatorname{Loc}_{\check G}$ 的右伴随全忠实。

1. 把 $\operatorname{LocSys}_{\check G}$ 写成 $B\check G\times X\to X$ 的水平截面所组成的对象。  
   *为什么*：在这个描述里，“取值向量丛”只是沿 $X$ 的求值，局部化函子变成形式上的拉回—推回。
2. 对任意配备相对于 $X$ 的联络的叠 $Z\to X$ 重复同一论证。  
   *为什么*：论证只用到“有联络”这一形式性质，与 $\check G$ 的具体结构无关，故可整体搬过来。

> 缺口：讲义只写“证明在形式上来自”水平截面的描述，未展开细节；完整论证见 [Gai10]。

*出处*：定理 9.3.1 / 原书 p.49


## 易错点

- 取“沿满射”的余极限是因为 $X^I$ 只记住带标号的点：满射 $I\twoheadrightarrow J$ 允许把若干点合并，缺了这层粘合就没有点碰撞时的融合。
- 纤维用 $\bigotimes$ 不用 $\prod$：融合把两点的张量积在碰撞极限下乘成一个。
- “等价地，右伴随全忠实”是 Verdier 商刻画的等价说法，不是额外的独立结论。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§9.3 Ran 作用与局部到整体，p.49（PDF p.49），`定理 9.3.1（ch09.tex:57-59，p.49）；§9.3 的一般讨论见 ch09.tex:44-63`

## 核验

状态：`external-confirmed`（2026-11-18）
- nLab, Ran space：https://ncatlab.org/nlab/show/Ran+space — nLab 页把 Ran X 定义为 X 的全部非空有限子集、带「若干重合点合并成一点」的几何结构；代数情形 Ran_X := colim_I X^I，I 取非空有限集、态射为满射——支持卡中 Ran(X)={I⊂X|0<|I|<∞} 及「沿满射的余极限」的描述（该句为转述，非逐字引文）。
- Gaitsgory, Recent progress in geometric Langlands theory (Seminaire Bourbaki, talk of 2016-02-16)：https://arxiv.org/abs/1606.09462 — §2.2.7 脚注说 Rep(Ǧ,Ran(X)) 是「非空有限集与满射」上 I↦Rep(Ǧ)^{⊗I} 与 I↦D(X^I) 两个函子在 DGCat 里的 coend，§2.2.8 说几何 Hecke 作用就是它在 D(Bun_G) 上的作用——支持卡的纤维 ⊗_{x∈I}Rep(Ǧ) 与幺半作用两条。
- Gaitsgory, Recent progress in geometric Langlands theory (Seminaire Bourbaki, talk of 2016-02-16)：https://arxiv.org/abs/1606.09462 — 「The functor Ev admits a fully faithful right adjoint」，即 QCoh(LocSys_Ǧ) 是 Rep(Ǧ)_Ran 对幺半理想的 Verdier 商——逐字支持卡中定理 9.3.1 及其「等价地右伴随全忠实」。
- Gaitsgory, A generalized vanishing conjecture (manuscript, 2010-10-18)：https://people.mpim-bonn.mpg.de/gaitsgde/GL/GenVan.pdf — §1.4 对任意带相对 X 联络的 Artin 叠 Z→X 写出 Loc_Z: QCoh(Z_Ran)→QCoh(§^∇(X,Z))，并说「It is likely that Theorem 1.2 holds, as is, in this more general context」——支持卡中「同一论证适用于任何 Z→X」，但原文只作 likely 的猜测，故记 partial。

## 关联

- `glc/concept/spectral-action`
- `glc/concept/generalized-vanishing-theorem`
- `glc/concept/averaging-kernel`
