---
id: glc/concept/all-sheaves-on-stack
type: concept
track: F
---

# 代数叠上的所有层

> 用光滑下降把「所有层」从仿射概形延拓到代数叠：取拉回过渡的极限，等价地取左伴随过渡的余极限。

**问题**：为什么 $\operatorname{Shv}^{\mathrm{all}}(\operatorname{Bun}_G)$ 可以写成光滑图册上的余极限？

## 定义

对 $\mathbb C$ 上有限型仿射概形 $S$，置
$$\operatorname{Shv}^{\mathrm{all}}(S):=\operatorname{Shv}^{\mathrm{all}}(S(\mathbb C)),$$
不加任何可构造性条件。若 $Y$ 为代数叠，则通过光滑下降定义 $Y$ 上的层：
$$\operatorname{Shv}^{\mathrm{all}}(Y):=\lim_{(S\to Y)\in(\operatorname{Aff}^{\mathrm{sm}}_{/Y})^{\mathrm{op}}}\operatorname{Shv}^{\mathrm{all}}(S),$$
其中过渡函子为拉回。

*记号*：$S(\mathbb C)$ 指 $S$ 的复点集；$\operatorname{Aff}^{\mathrm{sm}}_{/Y}$ 是光滑仿射概形到 $Y$ 的范畴；极限取在 $({-})^{\mathrm{op}}$ 上，过渡映射为拉回。$\operatorname{Bun}_G$ 为 $X$ 上 $G$-丛的模叠。

## 要点

- 该定义不施加任何可构造性条件，因此 $\operatorname{Shv}^{\mathrm{all}}$ 与可构造层范畴 $\operatorname{Shv}_{\mathrm{cons}}$ 是两个不同的出发点。
- 等价地，利用伴随关系可写成余极限 $\operatorname{Shv}^{\mathrm{all}}(Y)\simeq\operatorname{colim}_{S\to Y,\ S\ \text{光滑}}\operatorname{Shv}^{\mathrm{all}}(S)$，此时过渡函子取相应的左伴随。
- 两种写法一致，依据的是一般范畴原理：若 $L_{ij}:\mathcal C_i\rightleftarrows\mathcal C_j:R_{ij}$ 是可呈示范畴之间的一对伴随函子，则 $\operatorname{colim}_{L_{ij}}\mathcal C_i\simeq\lim_{R_{ij}}\mathcal C_i$。
- 因此 $\operatorname{Shv}^{\mathrm{all}}(\operatorname{Bun}_G)$ 是一个由 $\operatorname{Bun}_G$ 的解析图册构成的大可呈示范畴。

## 关键公式

- $$\operatorname{Shv}^{\mathrm{all}}(Y):=\lim_{(S\to Y)\in(\operatorname{Aff}^{\mathrm{sm}}_{/Y})^{\mathrm{op}}}\operatorname{Shv}^{\mathrm{all}}(S)$$
- $$\operatorname{Shv}^{\mathrm{all}}(Y)\simeq\operatorname{colim}_{S\to Y,\ S\ \text{光滑}}\operatorname{Shv}^{\mathrm{all}}(S)$$
- $$\operatorname{colim}_{L_{ij}}\mathcal C_i\simeq\lim_{R_{ij}}\mathcal C_i$$

## 定理与证明

### $\operatorname{Shv}^{\mathrm{all}}(\operatorname{Bun}_G)$ 的可呈示性（要点（有缺口））

$\operatorname{Shv}^{\mathrm{all}}(\operatorname{Bun}_G)$ 是一个由 $\operatorname{Bun}_G$ 的解析图册构成的大可呈示范畴。

1. 沿 $\operatorname{Bun}_G$ 的解析图册，把 $\operatorname{Shv}^{\mathrm{all}}$ 写成光滑下降的极限。  
   *为什么*：光滑下降正是叠上层范畴的定义方式。
2. 用可呈示范畴的伴随原理，把该极限改写为按左伴随取的余极限。  
   *为什么*：可呈示性保证 $\operatorname{colim}_{L}\simeq\lim_{R}$。

> 缺口：讲义只以「因此」一句给出结论，未证明可呈示性；图册的选取与极限的可呈示性细节讲义均未展开。

*出处*：定义（§11.1，讲义无编号） / 原书 p.57


## 易错点

- 「所有层」不等于「可构造层的 ind-完备化」：原文明确不加可构造性条件；到 §11.6 才指出 $\operatorname{Shv}^{\mathrm{all}}(\operatorname{Bun}_G)$ 一般不是紧生成的。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§11.1 代数叠上的所有层，p.57（PDF p.57），`源码/chapters/ch11.tex:7-22（定义与伴随原理，§11.1）`

## 核验

状态：`source-only`（2026-11-18）
- nLab：https://ncatlab.org/nlab/show/algebraic+stack — 页面只把代数叠定义为 fppf 拓扑上的 (2,1)-预层与光滑群胚的商叠（『every internal groupoid in algebraic spaces represents a (2,1)-presheaf on the fppf-site … the quotient stack』），既没有『Shv^all(Y)=lim_{(S→Y)∈(Aff^sm_{/Y})^op} Shv^all(S)』这种取极限的层范畴定义，也没有『大可呈示』的陈述；卡里定义与定理两层都无法在外部逐字对上。

## 关联

- `glc/concept/quasi-lisse-sheaves`
- `glc/concept/shv-nilpotent-support`
