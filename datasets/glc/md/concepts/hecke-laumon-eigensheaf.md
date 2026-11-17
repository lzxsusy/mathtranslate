---
id: glc/concept/hecke-laumon-eigensheaf
type: concept
track: E
---

# Hecke–Laumon 特征层

> 若 $\mathcal K$ 配有同构 $\mathrm{HL}_k^d(\mathcal K)\xrightarrow\sim\mathcal L_E^d\boxtimes\mathcal K$，则称它以 $E$ 为特征值。

**问题**：为什么 Hecke–Laumon 特征性质需要一族 $\alpha_d$（$d\ge0$）而不是单个同构，『迭代相容』又在比较什么？

## 定义

若反常层 $\mathcal K\in\operatorname{Perv}(\operatorname{Coh}_k)$ 配备同构 $\alpha_d:\mathrm{HL}_k^d(\mathcal K)\xrightarrow{\sim}\mathcal L_E^d\boxtimes\mathcal K$（$d\ge0$），满足 $d=0$ 时显然的归一化，且这些同构与迭代修改相容，则称它为以 $E$ 为特征值的 Hecke–Laumon 特征层。更明确地，对 $d=d_1+d_2$，比较通过 $0\to M'\to M\to\mathcal T'\to0$、$0\to M''\to M'\to\mathcal T''\to0$ 从 $M$ 转到 $M''$ 的两种方式。这种两步修改的叠既映到 $\mathrm{HL}_k^d$，也映到 $\operatorname{Tor}^{d_1}\times\mathrm{HL}_k^{d_2}$；所需相容性要求由 $\mathrm{HL}_k^{d_2}\circ\mathrm{HL}_k^{d_1}\simeq((s,q)_!m^*\boxtimes\mathrm{Id})\circ\mathrm{HL}_k^d$ 得到的图与第 7 章的因子化同构 $(s,q)_!m^*\mathcal L_E^d\simeq\mathcal L_E^{d_1}\boxtimes\mathcal L_E^{d_2}$ 交换，其中 $m,s,q$ 是挠层短正合列叠 $0\to\mathcal T''\to\mathcal T\to\mathcal T'\to0$ 中的映射。

*记号*：$\alpha_d$ 是 $\operatorname{Tor}^d\times\operatorname{Coh}_k$ 上的同构；$\mathcal L_E^d$ 是第 7 章的 Laumon 层；$(s,q)_!m^*$ 是挠层短正合列叠上的『推拉』操作（$m$ 取中间项、$s$ 取子、$q$ 取商）；$\boxtimes$ 是外积。

## 要点

- 特征性质是一族同构 $\{\alpha_d\}_{d\ge0}$：每个 $d$ 都要求 $\mathrm{HL}_k^d(\mathcal K)$ 是 $\mathcal L_E^d\boxtimes\mathcal K$。
- $d=0$ 给归一化：此时 $\mathrm{HL}_k^0$ 是恒等对应，$\alpha_0$ 就是恒等（『显然的归一化』）。
- 迭代相容比较的是『一次改 $d$ 步』与『先改 $d_1$ 步再改 $d_2$ 步』：两步修改的叠同时映到 $\mathrm{HL}_k^d$ 与 $\operatorname{Tor}^{d_1}\times\mathrm{HL}_k^{d_2}$，相容性要求两个方向得到同一结果。
- 相容性的关键输入正是第 7 章的因子化同构 $(s,q)_!m^*\mathcal L_E^d\simeq\mathcal L_E^{d_1}\boxtimes\mathcal L_E^{d_2}$——没有它，$\alpha_d$ 的迭代无法闭合。
- $k=0$ 时这恰好是 Laumon 因子化定理：$\mathcal L_E\in\operatorname{Perv}(\operatorname{Tor})$ 是 Hecke–Laumon 特征层。
- 前几章的 Fourier 归纳继而对 $k$ 归纳，给出 $F_k\in\operatorname{Perv}(C'_k)$ 也是 Hecke–Laumon 特征层；于是 $\operatorname{Aut}'_E|_{C_n^{\prime,\circ}}$ 满足该性质，下降后 $\operatorname{Aut}_E|_{C_n^\circ}$ 继承之。

## 关键公式

- $\alpha_d:\mathrm{HL}_k^d(\mathcal K)\xrightarrow{\sim}\mathcal L_E^d\boxtimes\mathcal K\qquad(d\ge0)$
- $\mathrm{HL}_k^{d_2}\circ\mathrm{HL}_k^{d_1}\simeq((s,q)_!m^*\boxtimes\mathrm{Id})\circ\mathrm{HL}_k^d$
- $(s,q)_!m^*\mathcal L_E^d\simeq\mathcal L_E^{d_1}\boxtimes\mathcal L_E^{d_2}$
- $0\to M'\to M\to\mathcal T'\to0,\qquad 0\to M''\to M'\to\mathcal T''\to0$
- $F_k\in\operatorname{Perv}(C'_k)$

## 定理与证明

### $k=0$ 情形恢复 Laumon 因子化定理（完整）

取 $k=0$，Hecke–Laumon 特征性质退化为：$\mathcal L_E\in\operatorname{Perv}(\operatorname{Tor})$ 是 Hecke–Laumon 特征层，即第 7 章的 Laumon 因子化定理。

1. $k=0$ 时 $\operatorname{Coh}_0$ 上的对象是秩 $0$ 的层（挠层），$\mathrm{HL}_0^d$ 的三项 $M',M,\mathcal T$ 全为挠层，叠就是 $\operatorname{Tor}$ 上的短正合列叠。  
   *为什么*：秩 $0$ 无挠层即挠层，故整个构造落在挠层范畴内。
2. 此时 $\alpha_d$ 正是第 7 章证明的因子化同构 $(s,q)_!m^*\mathcal L_E^d\simeq\mathcal L_E^{d_1}\boxtimes\mathcal L_E^{d_2}$ 的逐 $d$ 版本，$d=0$ 归一化为恒等，迭代相容由该同构的结合性给出。  
   *为什么*：第 7 章的同构恰是『一次取 $d$ 个点』与『分批取』之间的比较，与这里 $\alpha_d$ 的相容性要求逐字对应。

*出处*：§8.4 / 原书 p.46


## 易错点

- $\alpha_d$ 是**同构**不是态射：方向必须是 $\mathrm{HL}_k^d(\mathcal K)\xrightarrow{\sim}\mathcal L_E^d\boxtimes\mathcal K$，反向写会与 $d$ 的加法方向冲突。
- 『$d=0$ 时的归一化』不是可有可无的装饰：没有它，$d\ge1$ 的 $\alpha_d$ 可以随意乘常数。
- 迭代相容要同时对照两条路径（$\mathrm{HL}_k^d$ 侧与 $\operatorname{Tor}^{d_1}\times\mathrm{HL}_k^{d_2}$ 侧），只写一侧不算相容。
- 这是**无编号**的 `definition*`；引用时写『§8.4 的定义（Hecke–Laumon 特征层）』，不要编造编号 8.4.x。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§8.4 Hecke–Laumon 对应，p.46（PDF p.46），`源码/chapters/ch08.tex:66-83（定义*、迭代相容与 $k=0$ 的 Laumon 因子化）`

## 核验

状态：`source-only`（2026-11-18）
- JAMS：https://www.ams.org/journals/jams/2002-15-02/S0894-0347-01-00388-5/S0894-0347-01-00388-5.pdf — 「Let $\mathcal K$ be a perverse sheaf on $\mathrm{Bun}_n$, which is a Hecke eigensheaf with respect to $E$. Is it true that the Goresky–MacPherson extension of $\mathcal K$ to $\mathcal{C}oh_n$ has the Hecke–Laumon property with respect to $E$? We conjecture that the answer is affirmative.」证明「Hecke–Laumon 性质」是 FGKV02 已命名的概念、且与 IC（Goresky–MacPherson）延拓配套；卡里 $\alpha_d:\mathrm{HL}_k^d(\mathcal K)\xrightarrow{\sim}\mathcal L_E^d\boxtimes\mathcal K$、$d=0$ 归一化与迭代相容的具体形式在片段中未逐字出现。
- nLab：https://ncatlab.org/nlab/show/Hecke+eigensheaf — 「A Hecke eigensheaf is an object that is taken to a tensor-multiple of itself under the integral transform induced by a Hecke correspondence.」支持「特征值 $E$ 即张量倍」的语义；页面没有 $\mathrm{HL}$ 叠、$\alpha_d$ 与相容性条件。

## 关联

- `glc/concept/hecke-laumon-stack`
- `glc/concept/laumon-factorization`
- `glc/concept/aut-e-whittaker-laumon`
