---
id: glc/concept/whittaker-equivalence
type: concept
track: H
---

# Whittaker 形式与 oper 上的 IndCoh

> 临界 Whittaker 范畴 $\simeq\operatorname{IndCoh}(\operatorname{Op}_{\check G}(D^\times))$；再加「局部系统延拓到 $D$」即得 FLE 的谱侧。

**问题**：Whittaker 形式与 FLE 的谱空间差在哪一步？

## 定义

在临界水平，Drinfeld–Sokolov 约化的增强版本取值于穿孔圆盘上 oper 空间上的层，相应的 Whittaker 陈述读作
$$\widehat{\mathfrak g}_{\mathrm{crit}}\text{-}\mathrm{Mod}^{\mathrm{Whit}}\simeq\operatorname{IndCoh}(\operatorname{Op}_{\check G}(D^\times)).$$
这里 $D^\times=\operatorname{Spec} k((t))$ 是穿孔圆盘。

*记号*：$\operatorname{Whit}$ 型上标指 Whittaker 范畴（对 $\mathfrak n((t))$ 取 Whittaker 向量）；$\operatorname{Op}_{\check G}(D^\times)$ 是穿孔圆盘上的 oper 空间，比 $\operatorname{Op}^{\mathrm{unr}}_{\check G}$ 少一个「局部系统延拓到 $D$」的纤维积。

## 要点

- 这是 FLE 的 Whittaker 形式：把球面／Kazhdan–Lusztig 子范畴换成 Whittaker 范畴。
- 从 Whittaker 形式转到球面／KL 子范畴，在谱侧相当于施加底层局部系统可延拓到 $D$ 的条件。
- 因此谱空间由 $\operatorname{Op}(D^\times)$ 换成 $\operatorname{Op}^{\mathrm{unr}}_{\check G}=\operatorname{Op}_{\check G}(D^\times)\times_{\operatorname{LocSys}_{\check G}(D^\times)}\operatorname{LocSys}_{\check G}(D)$。
- $\Psi$ 的增强版本落在 $\operatorname{Op}_{\check G}(D^\times)$ 上的层，而不是 $\operatorname{Op}^{\mathrm{unr}}_{\check G}$ 上。
- Whittaker 侧与球面侧的谱侧差别就是这一替换：从 $\operatorname{Op}_{\check G}(D^\times)$ 换成 $\operatorname{Op}^{\mathrm{unr}}_{\check G}$，与抛物子群 $P=G$ 无关（$P=G$ 是第 16 章导出 Satake 的边界情形）。

## 关键公式

- $\widehat{\mathfrak g}_{\mathrm{crit}}\text{-}\mathrm{Mod}^{\mathrm{Whit}}\simeq\operatorname{IndCoh}(\operatorname{Op}_{\check G}(D^\times))$
- $\operatorname{Op}^{\mathrm{unr}}_{\check G}=\operatorname{Op}_{\check G}(D^\times)\times_{\operatorname{LocSys}_{\check G}(D^\times)}\operatorname{LocSys}_{\check G}(D)$

## 定理与证明

### 临界 Whittaker 等价（§15.3）（要点（有缺口））

$\widehat{\mathfrak g}_{\mathrm{crit}}\text{-}\mathrm{Mod}^{\mathrm{Whit}}\simeq\operatorname{IndCoh}(\operatorname{Op}_{\check G}(D^\times))$。

1. 取 Drinfeld–Sokolov 约化在临界水平的增强版本，它取值于穿孔圆盘上 oper 空间上的层。  
   *为什么*：增强版本自然落在 $\operatorname{Op}_{\check G}(D^\times)$ 上，因为圆盘内部（$t=0$ 处）没有延拓条件。

> 缺口：讲义只述不证：它是临界 FLE 的 Whittaker 形式，原书引 [FG05]、[FG07]。

*出处*：§15.3（Whittaker 陈述）/ 原书 p.73


## 易错点

- 把 $\operatorname{IndCoh}(\operatorname{Op}_{\check G}(D^\times))$ 与 FLE 的 $\operatorname{IndCoh}(\operatorname{Op}^{\mathrm{unr}}_{\check G})$ 混为一谈：二者只差「底层局部系统可延拓到 $D$」这一条件，但它正是 Whittaker 范畴与球面／KL 子范畴的分别。
- $D^\times$ 是穿孔圆盘 $\operatorname{Spec} k((t))$，不是形式圆盘 $D=\operatorname{Spec} k[[t]]$；写错会把这个等价读成圆盘上的陈述。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§15.3 Drinfeld–Sokolov 约化与 Whittaker 形式，p.73（PDF p.73），`源码/chapters/ch15.tex:53-55（Whittaker 陈述与 $\operatorname{Op}^{\mathrm{unr}}$ 的替换）`

## 核验

状态：`source-only`（2026-11-18）
- Frenkel–Gaitsgory, Local geometric Langlands correspondence and affine Kac–Moody algebras：https://arxiv.org/abs/math/0508382 — 摘要：临界水平某商范畴 ≃ 幂零 oper 加厚上的 QCoh；支持「临界 Whittaker 侧对应 oper 空间上的层」的方向，但未写 IndCoh(Op(D^×)) 的精确形式。
- Frenkel–Gaitsgory, Local geometric Langlands correspondence: the spherical case：https://arxiv.org/abs/0711.1132 — 主定理只处理球面（unramified）情形，结论是 QCoh(Op^unr)，不支持 Whittaker 侧的 Op(D^×)。

## 关联

- `glc/concept/drinfeld-sokolov-reduction`
- `glc/concept/pointwise-fle`
- `glc/concept/unramified-oper`
