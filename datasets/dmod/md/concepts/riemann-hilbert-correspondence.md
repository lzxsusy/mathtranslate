---
id: dmod/concept/riemann-hilbert-correspondence
type: concept
track: G
---

# Riemann–Hilbert 对应

> 正则完整模的导出范畴与解析簇上可构造层的导出范畴等价：$\mathrm{dR}:D^b_{rh}(X)\cong D^b_c(X^{an},\mathbb C)$，经典情形即平坦联络与局部系。

**问题**：Riemann–Hilbert 对应把哪两个范畴等同起来，它与 §2 的「平坦联络 $\Leftrightarrow$ 局部系」是什么关系？

## 定义

设 $X$ 是光滑代数簇。Riemann–Hilbert 对应断言 de Rham 函子给出三角范畴的等价 $\mathrm{dR}:D^b_{rh}(X)\cong D^b_c(X^{an},\mathbb C)$，其中 $D^b_{rh}(X)$ 是正则完整 $\mathcal D_X$-模的有界导出范畴，$D^b_c(X^{an},\mathbb C)$ 是解析化 $X^{an}$ 上 $\mathbb C$-可构造层的有界导出范畴。经典情形（无奇点，或曲线的正则奇点情形）说的是 $\mathcal O_X$-模配平坦联络与局部系一一对应。讲义 §2 与 §4 的两条批注把它作为第五章的收束，并把该等价归于 Mebkhout–Kashiwara–Beilinson–Bernstein。

*记号*：$X^{an}$：$X$ 的解析化；$D^b_{rh}(X)$：正则完整 $\mathcal D_X$-模的有界导出范畴；$D^b_c(X^{an},\mathbb C)$：$\mathbb C$-可构造层的有界导出范畴；$\mathrm{dR}$：de Rham 函子。

## 要点

- 对应的一端是正则完整模的导出范畴 $D^b_{rh}(X)$，另一端是解析簇 $X^{an}$ 上 $\mathbb C$-可构造层的导出范畴 $D^b_c(X^{an},\mathbb C)$。
- 经典情形（零截面、无奇点）就是「配平坦联络的 $\mathcal O_X$-模 $\Leftrightarrow$ 局部系」，即 §2 批注所说的 Riemann–Hilbert 的经典情形。
- 取 de Rham 复形是从模到层的方向；批注把该等价归 Mebkhout–Kashiwara–Beilinson–Bernstein，未在讲义内证明。
- 讲义把它当作第五章的收束：该等价把「完整模的分类」翻译成「可构造层/反常层的分类」。
- $\dim X=1$ 的正则奇点情形是 Deligne 的「正则奇点方程必有解」：$D_{rh}(X)$ 的每个对象都来自局部系（§4 批注）。

## 关键公式

- $\mathrm{dR}:D^b_{rh}(X)\ \cong\ D^b_c(X^{an},\mathbb C)$
- $\mathrm{dR}:\{\text{平坦联络}\}\ \cong\ \{\text{局部系}\}\qquad(\text{经典情形})$

## 定理与证明

### 定理（Riemann–Hilbert 对应，§2 批注所述）（要点（有缺口））

设 $X$ 是光滑代数簇。de Rham 函子给出三角范畴的等价 $\mathrm{dR}:D^b_{rh}(X)\cong D^b_c(X^{an},\mathbb C)$，把正则完整 $\mathcal D_X$-模的有界导出范畴与解析化 $X^{an}$ 上 $\mathbb C$-可构造层的有界导出范畴等同。

1. 经典情形：配平坦联络 $\nabla$ 的 $\mathcal O_X$-模等价于局部系（局部常值层）。  
   *为什么*：这是 §2 批注直接陈述的经典 Riemann–Hilbert 情形，也是本卡公式第二行的内容。
2. 一般情形：取 de Rham 复形，得到 $\mathrm{dR}:D^b_{rh}(X)\cong D^b_c(X^{an},\mathbb C)$，从而把完整模的分类翻译成可构造层/反常层的分类。  
   *为什么*：这是 §2 批注的原话，并注明该等价归 Mebkhout–Kashiwara–Beilinson–Bernstein；讲义只述不证。

> 缺口：讲义在两处批注中只陈述该等价并注明归属，没有给出证明，也没有展开 $D^b_{rh}$ 中「正则」的定义；严格证明见 Mebkhout–Kashiwara–Beilinson–Bernstein 的原文。

*出处*：§2 批注 / 原书 V §2, p.136；另见 §4 批注, p.140


## 易错点

- 批注只陈述等价、未给证明；把 Riemann–Hilbert 对应写成讲义内的定理（带证明）是不合原文的。
- 「正则」不能省：对应的一端是 $D^b_{rh}(X)$ 而不是全部完整模；讲义没有定义正则性，本卡按惯例理解为正则完整（regular holonomic）。
- 经典情形（平坦联络 $\Leftrightarrow$ 局部系）只是对应在零截面处的特例；批注明确把它与一般的 $D^b_{rh}\cong D^b_c$ 区分开。
- 特征簇不能决定模（$\mathbb A^1$ 上的 $M_\alpha$ 例：特征簇相同而模不同），所以对应的信息在层一侧的单值化，不能只靠特征簇辨认。

## 出处

- Miličić《Lectures on the Algebraic Theory of D-Modules》中译本（校订批注本），V §2 联络（Connections），批注，p.136（PDF p.142），`源码/chapters/chap5.tex:132-134（批注：dR 等价）`
- Miličić《Lectures on the Algebraic Theory of D-Modules》中译本（校订批注本），V §4 不可约完整模的分类，批注，p.140（PDF p.146），`源码/chapters/chap5.tex:274-276（批注：一维情形与 Deligne）`

## 核验

状态：`external-confirmed`（2026-11-19）
- nLab：https://ncatlab.org/nlab/show/Riemann-Hilbert+correspondence — 条目断言 $\mathrm{dR}:D^b_{rh}(X)\cong D^b_c(X^{an},\mathbb C)$（Mebkhout–Kashiwara–Beilinson–Bernstein），与卡中定理陈述逐字对应。

## 关联

- `dmod/concept/flat-connection`
- `dmod/concept/local-system`
- `dmod/concept/deligne-regular-singular`
- `dmod/concept/irreducible-holonomic-classification`
