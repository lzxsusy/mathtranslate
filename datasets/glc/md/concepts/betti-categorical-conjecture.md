---
id: glc/concept/betti-categorical-conjecture
type: concept
track: F
---

# Betti 与 \ell-进情形的范畴猜想

> 其他层论中自守范畴也须受奇异支撑限制：$\operatorname{Shv}_{\mathrm{Nilp}}\simeq\operatorname{IndCoh}_{\mathrm{Nilp}}$。

**问题**：Betti 情形为什么不能直接用 $\operatorname{Shv}(\operatorname{Bun}_G)$ 作左端？

## 定义

对于其他层理论，特别是 Betti 层或 $\ell$-进层，自守范畴本身也必须受到奇异支撑的限制（[BZN16, NY19, AGK20a]）。在 Betti 情形，$\operatorname{LocSys}_{\check G}$ 是 $\pi_1(X)$ 到 $\check G$ 的表示所组成的导出特征叠；在最精确的层论表述中，还可以将它替换为相应的受限变体。猜想的形式为 $\operatorname{Shv}_{\mathrm{Nilp}}(\operatorname{Bun}_G)\simeq\operatorname{IndCoh}_{\mathrm{Nilp}}(\operatorname{LocSys}_{\check G})$。这里 $\operatorname{Shv}_{\mathrm{Nilp}}(\operatorname{Bun}_G)$ 用微局部奇异支撑定义。

*记号*：$\operatorname{Shv}$ 是所选层论（Betti 情形为 $\operatorname{Bun}_G(\mathbb{C})$ 上的层）；$\operatorname{Shv}_{\mathrm{Nilp}}$ 表示微局部奇异支撑落在全局幂零锥内的子范畴；$\pi_1(X)$ 是曲线的拓扑基本群。

## 要点

- Betti 情形 $\operatorname{LocSys}_{\check G}$ 是 $\pi_1(X)\to\check G$ 的表示所组成的导出特征叠。
- 最精确的层论表述中可把它替换为相应的受限变体。
- 自守范畴本身也必须受奇异支撑限制：即左端不是整个 $\operatorname{Shv}(\operatorname{Bun}_G)$。
- 猜想形式：$\operatorname{Shv}_{\mathrm{Nilp}}(\operatorname{Bun}_G)\simeq\operatorname{IndCoh}_{\mathrm{Nilp}}(\operatorname{LocSys}_{\check G})$。
- 与 de Rham 猜想相比，右端不变，左端从 $\operatorname{DMod}(\operatorname{Bun}_G)$ 换成微局部奇异支撑受限的 $\operatorname{Shv}_{\mathrm{Nilp}}(\operatorname{Bun}_G)$。

## 关键公式

- $\operatorname{Shv}_{\mathrm{Nilp}}(\operatorname{Bun}_G)\simeq\operatorname{IndCoh}_{\mathrm{Nilp}}(\operatorname{LocSys}_{\check G})$

## 定理与证明

### Betti 范畴猜想（§10.6，未编号 conjecture）（要点（有缺口））

$\operatorname{Shv}_{\mathrm{Nilp}}(\operatorname{Bun}_G)\simeq\operatorname{IndCoh}_{\mathrm{Nilp}}(\operatorname{LocSys}_{\check G})$。

1. 把 de Rham 的 $\operatorname{DMod}(\operatorname{Bun}_G)$ 换成 Betti 层范畴 $\operatorname{Shv}(\operatorname{Bun}_G)$。  
   *为什么*：层论换了，右侧的谱叠描述（$\pi_1(X)$ 的表示）也随之改变。
2. 再对自守侧施加微局部奇异支撑落在 $\mathrm{Nilp}_{\mathrm{glob}}$ 内的条件，得到 $\operatorname{Shv}_{\mathrm{Nilp}}(\operatorname{Bun}_G)$。  
   *为什么*：讲义明确说其他层论中自守范畴本身也必须受奇异支撑限制，否则两侧的幂零条件不对等。

> 缺口：这是猜想，讲义未给证明；它属于 [BZN16, NY19, AGK20a] 所讨论的 Betti／$\ell$-进框架。

*出处*：§10.6 / 原书 p.56


## 易错点

- 左端不是整个 $\operatorname{Shv}(\operatorname{Bun}_G)$：Betti 情形必须换成幂零微局部奇异支撑的子范畴，这是与 de Rham 版本的关键差别。
- Betti 情形的谱侧是 $\pi_1(X)\to\check G$ 的导出特征叠，不是 de Rham 的 $\check G$-局部系统叠；同一记号 $\operatorname{LocSys}_{\check G}$ 在两种层论下指不同对象。
- “最精确的表述中还可以替换为受限变体”——受限变体是可选项，不是猜想的必要条件。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§10.6 Betti 理论与其他层理论，p.56（PDF p.56），`§10.6 Betti 理论与其他层理论（ch10.tex:134-139，p.56）`

## 核验

状态：`source-only`（2026-11-18）
- arXiv：https://arxiv.org/abs/1606.08523 — 摘要：Betti 形式 GLC；automorphic category = suitable C-sheaves on Bun_G(X)，spectral category = suitable O-modules on character stack Loc_G^(S) of G^-local systems on S；支持本卡 Betti 设定与谱侧特征叠。摘要未给 Shv_Nilp≃IndCoh_Nilp 或 restricted variant。
- arXiv：https://arxiv.org/abs/2010.01906 — 摘要：定义 stack of local systems with restricted variation；对任意 constructible sheaf theory（如 ℓ-进）表述范畴 GLC；支持本卡「可换受限变体」与 ℓ-进推广。摘要未给精确 Nilp 公式。

## 关联

- `glc/concept/nilpotent-cone-microsupport`
- `glc/concept/categorical-langlands-conjecture`
- `glc/concept/restricted-local-systems`
