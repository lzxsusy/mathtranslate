---
id: glc/concept/torsion-sheaf-stack
type: concept
track: C
---

# 挠层叠 Tor 与按长度的分解

> 挠层叠 $\operatorname{Tor}$ 按长度分解为 $\operatorname{Tor}^d$；每个 $\operatorname{Tor}^d$ 是代数叠，以 Quot 概形开部分作图册。

**问题**：挠层叠 $\operatorname{Tor}$ 如何按长度分解，$\operatorname{Tor}^d$ 的代数叠结构由什么图册给出？

## 定义

设 $X$ 为 $k$ 上光滑射影连通曲线，$E$ 为 $X$ 上秩 $n$ 的局部系统。定义 $\operatorname{Tor}(S):=\{M\in\operatorname{Coh}(X\times S)\mid M\text{ 在 }S\text{ 上平坦，每个几何纤维均为挠层}\}$。它按长度分解：$\operatorname{Tor}=\coprod_{d\ge0}\operatorname{Tor}^d$，每个 $\operatorname{Tor}^d$ 都是代数叠。当 $X$ 真且 $H^0(X,\mathcal{O}_X)=k$ 时，可从 Quot 概形的开部分取得图册：$\operatorname{Quot}_{\mathcal{O}_X^{\oplus d}}^{\circ,d}=\{\mathcal{O}_X^{\oplus d}\twoheadrightarrow M\mid M\in\operatorname{Tor}^d,\ H^0(\mathcal{O}_X^{\oplus d})\xrightarrow{\sim}H^0(M)\}$；改变 $H^0(M)$ 中所选基得到 $\operatorname{GL}_d$ 作用，相应商叠为 $[\operatorname{Quot}_{\mathcal{O}_X^{\oplus d}}^{\circ,d}/\operatorname{GL}_d]\simeq\operatorname{Tor}^d$。

*记号*：$X$ 为 $k$ 上光滑射影连通曲线；$\operatorname{Coh}$ 为凝聚层范畴；$\operatorname{Tor}^d$ 记长度的部分；$\mathcal{O}_X$ 为结构层；$H^0(X,\mathcal{O}_X)=k$ 与 $X$ 真是图册存在的两个前提。

## 要点

- 挠层即局部自由层的有限长商，长度记作 $d$，故 $\operatorname{Tor}$ 按长度写成不交并 $\coprod_{d\ge0}\operatorname{Tor}^d$；这一分解在讲义中是定义的一部分。
- 图册用 Quot 概形的开部分：额外条件 $H^0(\mathcal{O}_X^{\oplus d})\xrightarrow{\sim}H^0(M)$ 保证整体截面对得上，从而 $\operatorname{GL}_d$ 的换基作用恰好落地为图册的群作用，商叠给出 $\operatorname{Tor}^d$。
- 例：若 $X=\mathbb{A}^1$，长度 $d$ 的挠层等同于一个带有一个自同态的 $d$ 维向量空间，因此 $\operatorname{Tor}^d\simeq\mathfrak{gl}_d/\operatorname{GL}_d$。
- 一般曲线上的 $\operatorname{Tor}^d$ 只是 étale 局部地与 $\mathfrak{gl}_d/\operatorname{GL}_d$ 类比：讲义开篇即声明局部描述在 étale 局部意义下，$\mathbb{A}^1$ 上的例子只是局部模型。

## 关键公式

- $\operatorname{Tor}(S):=\{M\in\operatorname{Coh}(X\times S)\mid M\text{ 在 }S\text{ 上平坦，每个几何纤维均为挠层}\}$
- $\operatorname{Tor}=\coprod_{d\ge0}\operatorname{Tor}^d$
- $[\operatorname{Quot}_{\mathcal{O}_X^{\oplus d}}^{\circ,d}/\operatorname{GL}_d]\simeq\operatorname{Tor}^d$
- $\operatorname{Tor}^d\simeq\mathfrak{gl}_d/\operatorname{GL}_d\qquad(X=\mathbb{A}^1)$
- $p:\operatorname{Hecke}_{\operatorname{GL}_n}^+\longrightarrow\operatorname{Tor},\qquad(M\hookrightarrow M')\longmapsto M'/M$

## 易错点

- 「挠层」不是「挠群」：这里指支集有限的凝聚层，长度 $d$ 才是有意义的离散不变量，不要与挠子群、挠模混为一谈。
- 图册的存在用到了 $X$ 真与 $H^0(X,\mathcal{O}_X)=k$；讲义把这两个条件写在前面，不能无条件引用该商叠表示。
- $\operatorname{Tor}^d\simeq\mathfrak{gl}_d/\operatorname{GL}_d$ 只在 $X=\mathbb{A}^1$ 字面成立；一般曲线要在次数 $d$ 除子附近取 étale 局部模型（§4.11 用 $\mathcal{N}_d/\operatorname{GL}_d$）。
- 这个叠是 §4.2 中整体正 Hecke 叠的靶：$p:\operatorname{Hecke}_{\operatorname{GL}_n}^+\to\operatorname{Tor}$ 记 $M\hookrightarrow M'$ 的挠商，故泛正 Hecke 核应是 $\operatorname{Tor}$ 上某个层的拉回，而那个层就是 $\mathcal{L}_E$。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§4.3 挠层叠，p.27-28（PDF p.27-28），`源码/chapters/ch04.tex:45-58（§4.3 挠层叠）`

## 核验

状态：`external-confirmed`（2026-11-18）
- FGKV98（Frenkel–Gaitsgory–Kazhdan–Vilonen, JAMS 11 (1998) 451–484；arXiv:alg-geom/9703022，本地文本 fgkv98.txt）：https://arxiv.org/abs/alg-geom/9703022 — 卡里『Tor(S) = {M ∈ Coh(X×S) | M 在 S 上平坦，每个几何纤维为挠层}』与该段 Coh 的定义逐句一致（相干、在 S 上有限平坦、几何纤维为有限长挠层）；卡里『Tor = ∐_{d≥0} Tor^d』对应同段 Coh_n = ∐_{m∈Z_+} Coh_{n,m}，Coh_{n,m} 分类 length m 的挠层。
- FGKV98：https://arxiv.org/abs/alg-geom/9703022 — 卡里『X=A^1 时 Tor^d ≅ gl_d/GL_d，长度 d 挠层=带一个自同态的 d 维向量空间』的局部模型对应原文 Coh_{m,m}(x) ≅ N_m/GL_m（N_m ⊂ gl_m 幂零矩阵，GL_m 共轭作用）。
- nLab：https://ncatlab.org/nlab/show/algebraic+stack — 卡里『每个 Tor^d 都是代数叠』所依据的定义（对角可被代数空间表示 + 存在概形 U 与满光滑 U→X）由该页给出；该页并称每个代数叠等价于光滑代数群胚。

## 关联

- `glc/concept/torsion-stratification`
- `glc/concept/springer-resolution`
- `glc/concept/laumon-sheaf`
