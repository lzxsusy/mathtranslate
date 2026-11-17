---
id: glc/concept/irreducibility-laumon-sheaf
type: concept
track: C
---

# $\mathcal{L}_E^d$ 的几何不可约性（引理 4.6.2）

> 若局部系统 $E$ 几何不可约，则 $\mathcal{L}_E^d$ 反常且几何不可约；证明用 Schur 引理与花环积 $\pi_1(X_{\bar k})^d\rtimes S_d$ 的自同态代数。

**问题**：$E$ 几何不可约时，为什么 $\mathcal{L}_E^d$ 也几何不可约？

## 定义

若 $E$ 几何不可约，则 $\mathcal{L}_E^d\in\operatorname{Perv}(\operatorname{Tor}^d)$ 几何不可约。证明（讲义标为「概要」）：基变换到 $\bar k$ 后，Schur 引理给出 $\operatorname{End}_{\pi_1(X_{\bar k})}(E_{\bar x})=e$；无重数配置轨迹上的局部系统 $E^{(d)}$ 对应不可约外张量积 $E_{\bar x}^{\otimes d}$ 作为花环积群 $\pi_1(X_{\bar k})^d\rtimes S_d$ 的表示，其自同态代数为 $\operatorname{End}_{\pi_1(X_{\bar k})^d\rtimes S_d}(E_{\bar x}^{\otimes d})=(e^{\otimes d})^{S_d}=e$，故它不可约；拉回到标量自同构胚叠保持不可约性，中间延拓保持底层反常层的不可约性。

*记号*：$e$ 为系数域；$\rtimes$ 为半直积（花环积）；$\operatorname{End}_{\pi_1}(E_{\bar x})=e$ 是「几何不可约」的刻画。

## 要点

- 第一步是几何化：基变换到 $\bar k$，于是 $\pi_1(X_{\bar k})$ 的不可约表示才可以用 Schur 引理数自同态。
- 关键是花环积而不是直积：$E^{(d)}$ 在 $X^{(d),\mathrm{rss}}$ 上是对称化的，其对偶群是 $\pi_1^d\rtimes S_d$；$S_d$ 只置换 $d$ 个因子，故取不变后自同态恰为 $e$。
- 最后两步是「操作保持不可约」：拉回到标量自同构胚叠不改变不可约性，中间延拓保持底层反常层的不可约性——讲义对这两点只作断言。
- 该引理给 §4.9 的分解一个前提：局部公式把 $\mathcal{L}_{E,x}^d[-d]$ 分解成 $B_{\lambda,x}$ 的直和，而 $\mathcal{L}_E^d$ 本身的不可约性与此分解不矛盾，因为局部化与取直和项是两回事。

## 关键公式

- $\operatorname{End}_{\pi_1(X_{\bar k})}(E_{\bar x})=e$
- $\operatorname{End}_{\pi_1(X_{\bar k})^d\rtimes S_d}(E_{\bar x}^{\otimes d})=(e^{\otimes d})^{S_d}=e$
- $\mathcal{L}_E^d=(\operatorname{Spr}_E^d)^{S_d}\in\operatorname{Perv}(\operatorname{Tor}^d)$

## 定理与证明

### 引理 4.6.2（要点（有缺口））

若 $E$ 几何不可约，则 $\mathcal{L}_E^d\in\operatorname{Perv}(\operatorname{Tor}^d)$ 几何不可约。

1. 基变换到 $\bar k$，用 Schur 引理得 $\operatorname{End}_{\pi_1(X_{\bar k})}(E_{\bar x})=e$。  
   *为什么*：几何不可约的定义就是其单值群表示不可约，故自同态只有标量，而 $e$ 上标量即 $e$。
2. 在无重数配置轨迹上把 $E^{(d)}$ 认成 $E_{\bar x}^{\otimes d}$ 作为 $\pi_1(X_{\bar k})^d\rtimes S_d$ 的表示。  
   *为什么*：$X^{d,\mathrm{rss}}\to X^{(d),\mathrm{rss}}$ 是有序覆盖，$S_d$ 置换 $d$ 个因子。
3. 算出 $\operatorname{End}_{\pi_1^d\rtimes S_d}(E_{\bar x}^{\otimes d})=(e^{\otimes d})^{S_d}=e$，故该表示不可约。  
   *为什么*：外张量积的自同态是张量积，$S_d$ 不变部分只剩标量。
4. 拉回到标量自同构胚叠、再作中间延拓，两步都保持不可约性，回到 $\mathcal{L}_E^d$。  
   *为什么*：讲义把这两步并作一句断言，未给细节。

> 缺口：讲义把证明明确标为「概要」：只给出自同态代数的计算，未补全「拉回标量胚叠保持不可约」与「中间延拓保持底层反常层不可约」的论证。

*出处*：§4.6 引理 4.6.2（原书 p.29）


## 易错点

- 「几何不可约」是在基变换到 $\bar k$ 之后说的；在 $k$ 上不可约不足以让 Schur 引理给出 $\operatorname{End}=e$。
- $E^{(d)}$ 的自同态要在花环积 $\pi_1^d\rtimes S_d$ 下算，而不是在 $\pi_1^d$ 下算：$S_d$ 的置换作用会把不同的张量因子混起来。
- 不可约的是 $\mathcal{L}_E^d$（$\operatorname{Tor}^d$ 上的反常层），不是 $\operatorname{Spr}_E^d$：后者带 $S_d$ 作用，按定义是可约的（分解成各等型）。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§4.6 引理 4.6.2，p.29（PDF p.29），`源码/chapters/ch04.tex:101-108（§4.6 引理 4.6.2）`

## 核验

状态：`source-only`（2026-11-18）
- FGKV98：https://arxiv.org/abs/alg-geom/9703022 — 外部最接近的陈述是 Laumon 猜想：E（σ）不可约时，自守层 S_E 限制到 M_n 每个连通分支是（差一个移位）不可约 perverse sheaf——这是整体模空间上的猜想；卡里引理 4.6.2 是 Tor^d 上的命题（花环积自同态 (e^{⊗d})^{S_d}=e），两者不是同一陈述，不能互相确认。

## 关联

- `glc/concept/laumon-sheaf`
- `glc/concept/laumon-extension-theorem`
- `glc/concept/local-factorization`
