---
id: dmod/concept/deligne-regular-singular
type: concept
track: G
---

# Deligne 正则奇点定理

> 曲线上的正则奇点线性微分方程必有解：$D_{rh}(X)$ 的每个对象都来自局部系，$\dim X=1$ 时完整模的分类由此完全算出。

**问题**：Deligne 关于正则奇点的结论在讲义里被表述成什么，它为什么使一维情形成为唯一能完全算出分类的情形？

## 定义

设 $X$ 是 $k$ 上光滑曲线（$\dim X=1$）。按 §4 批注，正则奇点情形指 $\mathcal D_X$-模可以由局部系（单值数据）单值化：局部单值化给出 Deligne 的结论「正则奇点方程必有解」，即 $D_{rh}(X)$ 的每个对象都来自局部系。讲义没有给出正则奇点性的形式定义，也没有给出证明；本卡只记录批注所述的这一结论及其在分类中的地位。批注同时指出：$\dim X=1$ 时完整模是 $X$ 上有限秩平坦联络的推广，而正则奇点情形是全书中唯一能完全算出分类的情形。

*记号*：$\dim X=1$：$X$ 是光滑曲线；$D_{rh}(X)$：正则奇点（正则完整）模构成的范畴；「局部单值化」：由局部系（单值表示）恢复模。

## 要点

- $\dim X=1$ 时完整 $\mathcal D_X$-模是 $X$ 上有限秩平坦联络的推广（§4 批注）。
- 正则奇点情形下局部单值化给出 Deligne 的「正则奇点方程必有解」：$D_{rh}(X)$ 的每个对象都来自局部系。
- 这是全书中唯一能完全算出分类的情形（§4 批注）。
- 与 Riemann–Hilbert 对应一致：批注把一维正则情形等同于平坦联络/局部系的经典对应。
- 讲义只以批注陈述该结论，未给证明，也未展开正则奇点性的定义。

## 关键公式

- $\mathrm{dR}:D^b_{rh}(X)\ \cong\ D^b_c(X^{an},\mathbb C)\qquad(\dim X=1)$
- $\mathcal V\in D_{rh}(X)\ \Longrightarrow\ \mathcal V\ \text{来自某个局部系}\ \mathcal L$

## 定理与证明

### 定理（Deligne：正则奇点方程必有解）（要点（有缺口））

设 $X$ 是 $k$ 上光滑曲线，$\mathcal V$ 是 $X$ 上正则奇点的线性微分方程（正则完整 $\mathcal D_X$-模）。则 $\mathcal V$ 在 $X$ 上有解；等价地，$D_{rh}(X)$ 的每个对象都来自局部系。

1. 把 $\mathcal V$ 限制到去掉奇点的开集 $U$：在 $U$ 上 $\mathcal V$ 是平坦联络，取水平截面得到局部系 $\mathcal L_U$。  
   *为什么*：$U$ 上没有奇点，$\mathcal V|_U$ 是有限秩平坦联络（§2 的联络与平坦性）。
2. 正则奇点条件保证 $\mathcal L_U$ 可以延拓过奇点，并把 $\mathcal V$ 与延拓后的局部系等同。  
   *为什么*：这正是批注所说的「局部单值化」，也就是 Deligne 定理的内容。

> 缺口：讲义 §4 批注只引述该定理并注明「局部单值化」，未给证明；严格证明见 Deligne 的原文，讲义未展开正则奇点性的定义。

*出处*：§4 批注 / 原书 V §4, p.140；另见 I §12 批注, p.51


## 易错点

- 批注没有给出「正则奇点」的形式定义，也没有证明 Deligne 定理；本卡只复述批注，不能当作讲义内已证的定理引用。
- 结论被限定在「正则奇点情形」：不要把它推广成「任意奇点的方程必有解」。
- $\dim X=1$ 是关键：批注说这是全书中唯一能完全算出分类的情形，高维没有对应的完整分类。
- 不要与 §2 的经典情形混淆：后者是无奇点的平坦联络 $\Leftrightarrow$ 局部系，Deligne 处理的是带正则奇点的情形。

## 出处

- Miličić《Lectures on the Algebraic Theory of D-Modules》中译本（校订批注本），V §4 不可约完整模的分类，批注，p.140（PDF p.146），`源码/chapters/chap5.tex:274-276（批注：Deligne 与局部单值化）`
- Miličić《Lectures on the Algebraic Theory of D-Modules》中译本（校订批注本），I §12 Kashiwara 定理，批注，p.51（PDF p.57），`源码/chapters/chap1.tex:1894-1896（批注：一维情形即 Deligne 定理）`

## 核验

状态：`external-confirmed`（2026-11-19）
- nLab：https://ncatlab.org/nlab/show/Riemann-Hilbert+correspondence — 条目给出正则完整模与可构造层的 de Rham 等价；$\dim X=1$ 时层一侧化为局部系，对应卡中「$D_{rh}(X)$ 的每个对象都来自局部系」。

## 关联

- `dmod/concept/riemann-hilbert-correspondence`
- `dmod/concept/local-system`
- `dmod/concept/d-module-on-affine-line`
