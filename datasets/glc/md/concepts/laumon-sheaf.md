---
id: glc/concept/laumon-sheaf
type: concept
track: C
---

# Laumon 层 $\mathcal{L}_E$ 与 $\mathcal{L}_E^d$

> $\mathcal{L}_E^d:=\operatorname{Hom}_{S_d}(\mathrm{triv},\operatorname{Spr}_E^d)$ 是 $\operatorname{Tor}^d$ 上秩 $n^d$ 反常层。

**问题**：$\mathcal{L}_E^d$ 如何从 $\operatorname{Spr}_E^d$ 取出，它作为 $X^{(d),\mathrm{rss}}$ 上的局部系统与 $\operatorname{Sym}^d E$ 有何不同？

## 定义

Laumon 层是 $S_d$ 作用的平凡等型直和项：$\mathcal{L}_E^d:=\operatorname{Hom}_{S_d}(\mathrm{triv},\operatorname{Spr}_E^d)=(\operatorname{Spr}_E^d)^{S_d}\in\operatorname{Perv}(\operatorname{Tor}^d)$。等价地，若在 $X^{(d),\mathrm{rss}}$ 上令 $E^{(d)}:=(r_{\mathrm{rss},*}E^{\boxtimes d})^{S_d}$，则 $\mathcal{L}_E^d\simeq j_{\mathrm{rss},!*}(s_{\mathrm{rss}}^*E^{(d)}[d])$。这个局部系统在无重数轨迹上秩为 $n^d$，不应与 $\operatorname{Sym}^d E$ 混淆。最后，对 $\mathcal{L}_E\in\operatorname{Perv}(\operatorname{Tor})$ 定义 $\mathcal{L}_E^d:=\mathcal{L}_E|_{\operatorname{Tor}^d}$。

*记号*：$E$ 为 $X$ 上秩 $n$ 的局部系统；$\operatorname{Perv}$ 为反常层范畴；$\mathrm{triv}$ 为 $S_d$ 的平凡表示；$E^{(d)}$ 是 $X^{(d),\mathrm{rss}}$ 上的局部系统。

## 要点

- 取 $S_d$ 不变（等价地取平凡等型）后，$\operatorname{Tor}^d$ 上留下一个反常层；这一步把 $\operatorname{Spr}_E^d$ 的 $S_d$ 单值作用「商掉」，与 $\operatorname{Sym}^d$ 的取法形式相同但对象不同。
- 两个表达式互相印证：直接取 $S_d$ 不变得 $(\operatorname{Spr}_E^d)^{S_d}$；先在 $X^{(d),\mathrm{rss}}$ 上取不变得 $E^{(d)}$ 再中间延拓，得到同一个层（用定理 4.6.1）。
- 秩 $n^d$ 而不是 $\binom{n+d-1}{d}$：在无重数轨迹上 $E^{(d)}$ 的纤维是 $E_x^{\otimes d}$ 的 $S_d$ 不变部分，维数仍为 $n^d$；讲义因此强调它「不应与 $\operatorname{Sym}^d E$ 混淆」。
- $\mathcal{L}_E$ 作为 $\operatorname{Tor}$ 上的反常层，其在 $\operatorname{Tor}^d$ 上的限制记作 $\mathcal{L}_E^d$；这与逐 $d$ 构造的 $\mathcal{L}_E^d$ 是同一个记号，讲义在 §4.6 末尾如此定义，§4.7 起就只用这个限制。

## 关键公式

- $\mathcal{L}_E^d:=\operatorname{Hom}_{S_d}(\mathrm{triv},\operatorname{Spr}_E^d)=(\operatorname{Spr}_E^d)^{S_d}\in\operatorname{Perv}(\operatorname{Tor}^d)$
- $E^{(d)}:=(r_{\mathrm{rss},*}E^{\boxtimes d})^{S_d}\quad\text{（在 }X^{(d),\mathrm{rss}}\text{ 上）}$
- $\mathcal{L}_E^d\simeq j_{\mathrm{rss},!*}(s_{\mathrm{rss}}^*E^{(d)}[d])$
- $\operatorname{rank}_{X^{(d),\mathrm{rss}}}\big(E^{(d)}\big)=n^d$
- $\mathcal{L}_E^d:=\mathcal{L}_E|_{\operatorname{Tor}^d},\qquad \mathcal{L}_E\in\operatorname{Perv}(\operatorname{Tor})$

## 定理与证明

### $\mathcal{L}_E^d$ 的两种描述一致（要点（有缺口））

$\mathcal{L}_E^d=(\operatorname{Spr}_E^d)^{S_d}$ 与 $\mathcal{L}_E^d\simeq j_{\mathrm{rss},!*}(s_{\mathrm{rss}}^*E^{(d)}[d])$ 给出同一个反常层，其中 $E^{(d)}=(r_{\mathrm{rss},*}E^{\boxtimes d})^{S_d}$；它在无重数轨迹上秩 $n^d$，不应与 $\operatorname{Sym}^d E$ 混淆。

1. 由定理 4.6.1 把 $\operatorname{Spr}_E^d$ 写成 $j_{\mathrm{rss},!*}(s_{\mathrm{rss}}^*r_{\mathrm{rss},*}(E^{\boxtimes d})[d])$。  
   *为什么*：这是延拓定理的内容，故本卡依赖它而非另证。
2. $\operatorname{Hom}_{S_d}(\mathrm{triv},-)$ 与 $!*$、$s_{\mathrm{rss}}^*$ 交换，把不变性搬到 $X^{(d),\mathrm{rss}}$ 上。  
   *为什么*：讲义以「等价地」直接给出，未解释交换性细节。
3. 在 $X^{(d),\mathrm{rss}}$ 上取 $S_d$ 不变得 $E^{(d)}$，并在无重数轨迹上数出秩 $n^d$。  
   *为什么*：$E^{\boxtimes d}$ 的秩为 $n^d$，取不变不改变 $X^{(d)}$ 上每点的纤维维数。

> 缺口：讲义只陈述两种描述相等与秩 $n^d$，未给 $\operatorname{Hom}_{S_d}(\mathrm{triv},-)$ 与中间延拓交换的证明；它依赖定理 4.6.1（讲义只述不证）。

*出处*：§4.6（原书 p.29）


## 易错点

- 秩是 $n^d$，不是 $\operatorname{Sym}^d$ 的 $\binom{n+d-1}{d}$：讲义专门警告这一点；两者的差别在于 $E^{(d)}$ 记的是有序支撑处的张量积再取不变，而不是对称幂。
- $\mathcal{L}_E^d$ 上标 $d$ 与 $\operatorname{Tor}^d$ 的上标同义（限制到长度 $d$ 的那一片），与 $\operatorname{Spr}_E^d$ 的上标也一致；不要把它读成某种「$d$ 次幂」。
- $\mathcal{L}_E$ 是 $\operatorname{Tor}$ 上的对象，$\mathcal{L}_E^d$ 是它到 $\operatorname{Tor}^d$ 的限制；§4.6 末尾的同名定义是记号重叠，不是两个不同构造。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§4.6 Laumon 层与 Laumon 直和项，p.29（PDF p.29），`源码/chapters/ch04.tex:96-112（§4.6）`

## 核验

状态：`external-confirmed`（2026-11-18）
- FGKV98：https://arxiv.org/abs/alg-geom/9703022 — 卡里『E^{(d)} := (r_{rss,*}E^⊠d)^{S_d}』与原文逐字同式：『E^{(m)} = (π_*E^⊠m)^{S_m}』（sheaf of invariants under the natural action of S_m）。
- FGKV98：https://arxiv.org/abs/alg-geom/9703022 — 卡里『L_E^d ≃ j_{rss,!*}(s_{rss}^*E^{(d)}[d])』对应原文『L_E|Coh_{n,m} = j_{!*}L^0_{E,m}』——同为从 rss 开子叠出发的 Goresky–MacPherson（中间）延拓。
- FGKV98：https://arxiv.org/abs/alg-geom/9703022 — 卡里『L_E^d = (Spr_E^d)^{S_d}』对应原文『L_{E,m,x} ≃ (Sp_m ⊗ (E_x)^{⊗m})^{S_m}|Coh_{n,m}』。

## 关联

- `glc/concept/laumon-extension-theorem`
- `glc/concept/local-factorization`
- `glc/concept/local-laumon-formula`
