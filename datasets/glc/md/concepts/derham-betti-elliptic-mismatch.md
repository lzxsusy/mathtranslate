---
id: glc/concept/derham-betti-elliptic-mismatch
type: concept
track: F
---

# 椭圆曲线上 de Rham 与 Betti 局部系统的分歧

> 对 $G=\mathbb G_m$、$X=E$，de Rham 侧是 $E^\vee$ 上的 $\mathbb A^1$-丛，Betti 侧是 $\mathbb G_m^2$；Riemann–Hilbert 只识别复点。

**问题**：为什么 Riemann–Hilbert 对应不能推出两个局部系统叠在代数上同构？

## 定义

取 $X=E$ 为椭圆曲线并选 $e\in E$，比较秩一情形 $G=\mathbb G_m=\mathrm{GL}_1$ 的两个刚性化局部系统叠。在 de Rham 侧，
$$\operatorname{LocSys}^{\mathrm{dR},\mathrm{rig}}_{\mathbb G_m,e}(E)\longrightarrow\operatorname{Pic}^0_E\simeq E^\vee$$
是普遍向量扩张；在 Betti 侧，
$$\operatorname{LocSys}^{\mathrm{Betti},\mathrm{rig}}_{\mathbb G_m,e}(E)\simeq\operatorname{Hom}(\mathbb Z^2,\mathbb G_m)\simeq\mathbb G_m^2.$$

*记号*：$E^\vee=\operatorname{Pic}^0_E$ 是椭圆曲线的对偶；$\mathbb G_a$-挠子与 $\mathbb A^1$-丛等价；下标 $e$ 表示在 $e$ 处刚性化。

## 要点

- de Rham 侧的映射 $\operatorname{LocSys}^{\mathrm{dR},\mathrm{rig}}_{\mathbb G_m,e}(E)\to\operatorname{Pic}^0_E$ 是普遍向量扩张，因此 $\operatorname{LocSys}^{\mathrm{dR},\mathrm{rig}}_{\mathbb G_m,e}(E)$ 是 $E^\vee$ 上的 $\mathbb G_a$-挠子。
- 等价地，它是 $E^\vee$ 上的一个 $\mathbb A^1$-丛，而不是 $\mathbb G_m^2$ 那样的平凡群簇。
- Riemann–Hilbert 对应在解析意义下识别它们的复点，但这一对应使用指数映射，并不识别代数结构。

## 关键公式

- $$\operatorname{LocSys}^{\mathrm{dR},\mathrm{rig}}_{\mathbb G_m,e}(E)\longrightarrow\operatorname{Pic}^0_E\simeq E^\vee$$
- $$\operatorname{LocSys}^{\mathrm{Betti},\mathrm{rig}}_{\mathbb G_m,e}(E)\simeq\operatorname{Hom}(\mathbb Z^2,\mathbb G_m)\simeq\mathbb G_m^2$$

## 定理与证明

### 秩一情形下两个叠不匹配（要点（有缺口））

对椭圆曲线 $E$，$\operatorname{LocSys}^{\mathrm{dR},\mathrm{rig}}_{\mathbb G_m,e}(E)$ 是 $E^\vee$ 上的 $\mathbb A^1$-丛，而 $\operatorname{LocSys}^{\mathrm{Betti},\mathrm{rig}}_{\mathbb G_m,e}(E)\simeq\mathbb G_m^2$；Riemann–Hilbert 只识别复点，不识别代数结构。

1. 把 de Rham 侧写成到 $\operatorname{Pic}^0_E$ 的普遍向量扩张。  
   *为什么*：秩一带联络挠子的模空间正是 $E^\vee$ 上的普遍向量扩张。
2. 把 Betti 侧用 $\pi_1(E)=\mathbb Z^2$ 的表示写成 $\operatorname{Hom}(\mathbb Z^2,\mathbb G_m)\simeq\mathbb G_m^2$。  
   *为什么*：Betti 局部系统由单值表示给出。
3. 指出 Riemann–Hilbert 通过指数映射比较复点。  
   *为什么*：指数映射是解析的，不保持代数结构。

> 缺口：讲义只陈述此例，未证明「普遍向量扩张」这一识别；Riemann–Hilbert 只识别复点一句亦只述不证（证明不在本章）。

*出处*：例（§11.2，讲义无编号） / 原书 p.57–58


## 易错点

- 不能由 Riemann–Hilbert 在解析意义下识别复点，就推断两个叠在代数上同构：de Rham 侧还带有 $E^\vee$ 上 $\mathbb A^1$-丛的额外结构。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§11.2 Betti 局部系统与 de Rham 局部系统，p.57-58（PDF p.57-58），`源码/chapters/ch11.tex:38-45（椭圆曲线例子，§11.2，跨 p.57–58）`

## 核验

状态：`external-confirmed`（2026-11-18）
- arXiv：https://arxiv.org/abs/1606.08523 — L215-222：『Conn_{GL_1}(E,0)→Jac(E,0)=Pic^0(E,0)≃E … is an A^1-bundle, specifically the unique nontrivial A^1-bundle, called the Serre surface』；L232 补一句它是『the twisted cotangent bundle of E associated to the divisor 0 … sections are 1-forms on E with simple poles at 0 of residue 1』。这正是卡里『LocSys^{dR,rig}_{G_m,e}(E)→Pic^0_E≃E^∨ 是普遍向量扩张 / E^∨ 上的 𝔸^1-丛』。
- arXiv：https://arxiv.org/abs/1606.08523 — L224-230：『Loc_{GL_1}(E,0)≃Spec C[π_1(Jac(E,0))]≃C^××C^×』，并给出『Loc(Jac(E,0))≃QCoh(Loc_{GL_1}(E,0))』——即卡里 LocSys^{Betti,rig}_{G_m,e}(E)≃Hom(Z^2,G_m)≃G_m^2。
- arXiv：https://arxiv.org/abs/1606.08523 — L242：『The variety G_m×G_m carries the algebraic symplectic form dz/z∧dw/w, which is analytically equivalent to the form on E^♭』——两侧只在解析意义上等同，支持卡里『Riemann–Hilbert 只识别复点，不识别代数结构』。

## 关联

- `glc/concept/betti-local-systems`
- `glc/concept/quasi-lisse-sheaves`
