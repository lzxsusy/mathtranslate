---
id: glc/concept/derived-satake
type: concept
track: F
---

# 导出 Satake 等价

> 把几何 Satake 提升到导出层：球面范畴 $\operatorname{Sph}_{G,x}$ 等价于谱 Hecke 叠上幂零支撑的 ind-凝聚层。

**问题**：导出 Satake 的右端为什么要限制奇异支撑落在幂零锥里？

## 定义

与 Arinkin–Gaitsgory 的奇异支撑形式体系（[AG15]）相容的局部球面范畴为 $\operatorname{Sph}_{G,x}:=\operatorname{DMod}(G(\mathcal{O}_x)\backslash G(\mathcal{K}_x)/G(\mathcal{O}_x))$，其中 $\mathcal{O}_x$ 是 $x$ 处的完备化局部环、$\mathcal{K}_x$ 是其分式域。通常的几何 Satake 等价给出心范畴 $\operatorname{Rep}(\check G)$。在导出范畴层面，正确的谱对象是谱 Hecke 叠 $\operatorname{Hecke}^{\mathrm{spec}}_{\check G}:=\mathrm{pt}/\check G\times_{\check{\mathfrak g}/\check G}\mathrm{pt}/\check G\simeq(\mathrm{pt}\times_{\check{\mathfrak g}}\mathrm{pt})/\check G$。导出 Satake 定理断言 $\operatorname{Sph}_{G,x}\simeq\operatorname{IndCoh}_{\mathrm{Nilp}(\check{\mathfrak g}^*)/\check G}(\operatorname{Hecke}^{\mathrm{spec}}_{\check G})$。

*记号*：$\mathcal{O}_x$、$\mathcal{K}_x$ 分别是 $x$ 处的整数环与分式域；$\operatorname{Hecke}^{\mathrm{spec}}_{\check G}$ 是谱 Hecke 叠；下标 $\mathrm{Nilp}(\check{\mathfrak g}^*)/\check G$ 表示允许的奇异支撑范围。

## 要点

- 局部球面范畴 $\operatorname{Sph}_{G,x}:=\operatorname{DMod}(G(\mathcal{O}_x)\backslash G(\mathcal{K}_x)/G(\mathcal{O}_x))$ 的心是 $\operatorname{Rep}(\check G)$（几何 Satake）。
- 谱 Hecke 叠 $\operatorname{Hecke}^{\mathrm{spec}}_{\check G}:=\mathrm{pt}/\check G\times_{\check{\mathfrak g}/\check G}\mathrm{pt}/\check G\simeq(\mathrm{pt}\times_{\check{\mathfrak g}}\mathrm{pt})/\check G$。
- 导出 Satake：$\operatorname{Sph}_{G,x}\simeq\operatorname{IndCoh}_{\mathrm{Nilp}(\check{\mathfrak g}^*)/\check G}(\operatorname{Hecke}^{\mathrm{spec}}_{\check G})$。
- $\operatorname{Sing}(\operatorname{Hecke}^{\mathrm{spec}}_{\check G})\simeq\check{\mathfrak g}^*/\check G$，幂零锥 $\mathrm{Nilp}(\check{\mathfrak g}^*)/\check G$ 恰好是允许的奇异支撑。
- 这是全局范畴 $\operatorname{IndCoh}_{\mathrm{Nilp}}(\operatorname{LocSys}_{\check G})$ 的局部模型。

## 关键公式

- $\operatorname{Sph}_{G,x}:=\operatorname{DMod}(G(\mathcal{O}_x)\backslash G(\mathcal{K}_x)/G(\mathcal{O}_x))$
- $\operatorname{Sph}_{G,x}\simeq\operatorname{IndCoh}_{\mathrm{Nilp}(\check{\mathfrak g}^*)/\check G}(\operatorname{Hecke}^{\mathrm{spec}}_{\check G})$

## 定理与证明

### 导出 Satake（§10.3，未编号）（要点（有缺口））

$\operatorname{Sph}_{G,x}\simeq\operatorname{IndCoh}_{\mathrm{Nilp}(\check{\mathfrak g}^*)/\check G}(\operatorname{Hecke}^{\mathrm{spec}}_{\check G})$。

1. 在心上退化到通常的几何 Satake：$\operatorname{Sph}_{G,x}$ 的心是 $\operatorname{Rep}(\check G)$。  
   *为什么*：导出等价必须先与已知的心等价相容，否则不是提升。
2. 把谱侧的奇异支撑限制在 $\operatorname{Sing}(\operatorname{Hecke}^{\mathrm{spec}}_{\check G})\simeq\check{\mathfrak g}^*/\check G$ 的幂零锥上。  
   *为什么*：幂零锥是允许的奇异支撑，这与全局 $\operatorname{IndCoh}_{\mathrm{Nilp}}$ 的局部模型一致。

> 缺口：讲义只陈述该等价并指出其谱对象与允许支撑，未给证明；这是把几何 Satake 从心范畴提升到导出范畴，证明不在本章范围内。

*出处*：§10.3 / 原书 p.54


## 易错点

- 允许支撑住在 $\check{\mathfrak g}^*/\check G$ 上（$\operatorname{Sing}(\operatorname{Hecke}^{\mathrm{spec}}_{\check G})\simeq\check{\mathfrak g}^*/\check G$）；§10.2 里用不变形式把 $A$ 看成 $\check{\mathfrak g}$ 的元素，两处记号差一个对偶。
- 导出 Satake 的右端是 $\operatorname{IndCoh}_{\mathrm{Nilp}}$，不是 $\operatorname{QCoh}$：$\operatorname{QCoh}$ 看不见奇异支撑，会把幂零条件丢掉。
- $\operatorname{Sph}_{G,x}$ 是局部对象（依赖点 $x$），别把它与全局的 $\operatorname{DMod}(\operatorname{Bun}_G)$ 混为一谈。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§10.3 相容性检验一：导出 Satake，p.54（PDF p.54），`§10.3 相容性检验一：导出 Satake（ch10.tex:73-86，p.54）`

## 核验

状态：`source-only`（2026-11-18）
- nLab：https://ncatlab.org/nlab/show/geometric+Satake+equivalence — 页面给出经典几何 Satake：DMod(Gr_G)^{L^+G} ≃ Rep(^L G)；支持本卡「通常几何 Satake 的心范畴为 Rep(Ĝ)」。页面没有导出 Satake、Hecke^spec 或 IndCoh_{Nilp(ĝ^*)/Ĝ}。
- nLab：https://ncatlab.org/nlab/show/geometric+Langlands+correspondence — 页面只给全局猜想/Nilp_Glob 条件与证明状态，没有 Sph_{G,x}≃IndCoh_{Nilp(ĝ^*)/Ĝ}(Hecke^spec) 或 Sing(Hecke^spec)≃ĝ^*/Ĝ 的陈述。

## 关联

- `glc/concept/nilpotent-singular-support`
- `glc/concept/tempered-object`
- `glc/concept/scheme-of-singularities`
