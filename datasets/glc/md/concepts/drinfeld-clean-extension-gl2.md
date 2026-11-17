---
id: glc/concept/drinfeld-clean-extension-gl2
type: concept
track: D
---

# Drinfeld 的 GL_2 洁净延拓定理

> Drinfeld 定理：E 几何不可约、秩 2 时，d>4(g−1) 保证 j_!q^*L_E^d 在线丛部分 Bun_1^d 上洁净。

**问题**：Drinfeld 洁净延拓定理的证明把边界消失最终化归为哪条定理？

## 定义

设 $X$ 为 $k$ 上光滑射影连通曲线，$g$ 为其亏格。限制到线丛 $\operatorname{Bun}_1\subset\operatorname{Coh}_1$。由于线丛之间的映射要么为零、要么为单射，在 $\operatorname{Bun}_1$ 上有
\[
\operatorname{Bun}'_1\xrightarrow{j}\operatorname{Bun}_1^+\xleftarrow{i}\operatorname{Bun}_1,
\]
其中 $i$ 为零截面，$j$ 为它的开补集。$q:\operatorname{Coh}'_1\to\operatorname{Tor}$ 为 $s$ 的余核给出的商映射。

*记号*：$\operatorname{Bun}'_1$ 是 $s:\mathcal{O}_X\hookrightarrow M$ 在一般点单射的线丛对；$\operatorname{Bun}_1^+$ 允许 $s$ 为零；$i$ 为零截面。

## 要点

- 洁净性等价于 $i^*j_*\mathcal{F}=0$，因为 $j$ 的补集恰是零截面。
- 证明的关键是收缩原理把边界消失化为 $\pi_!\mathcal{F}$，再化为 Abel–Jacobi 映射的紧支撑消失。
- 对 $n=2$，Deligne 条件 $d>n(2g-2)$ 恰好是 $d>4(g-1)$。
- 结论只在线丛部分 $\operatorname{Bun}_1^d\subset\operatorname{Coh}_1$ 上，不是整个 $\operatorname{Coh}_1$。

## 关键公式

- $i^*j_*\mathcal{F}=0$
- $i^!j_!\mathcal{F}\simeq\pi_!\mathcal{F}$
- $d>n(2g-2)\ \Longrightarrow\ \operatorname{AJ}^d_!(E^{(d)})=0$

## 定理与证明

### Drinfeld 洁净延拓定理（$\operatorname{GL}_2$）（要点（有缺口））

假设 $E$ 几何不可约且秩为 $2$。若 $d>4(g-1)$，则层 $j_!q^*\mathcal{L}_E^d$ 在 $\operatorname{Bun}_1^d\subset\operatorname{Coh}_1$ 上洁净。

1. 在 $\operatorname{Bun}'_1$ 上令 $\mathcal{F}=q^*\mathcal{L}_E^d$。洁净性指 $j_!\mathcal{F}\to j_*\mathcal{F}$ 为同构；由于锥支撑于零截面，这等价于 $i^*j_*\mathcal{F}=0$。  
   *为什么*：洁净性的定义即 $j_!=j_*$，而 $j$ 的补集是零截面。
2. 由 Verdier 对偶，只需对 $\mathcal{F}$ 及其对偶证明紧支撑的边界消失。  
   *为什么*：Verdier 对偶把 $*$-消失与 $!$-消失互换。
3. 对向量丛 $\operatorname{Bun}_1^+\to\operatorname{Bun}_1$ 上 $\mathbb{G}_m$ 的伸缩作用，收缩原理给出 $i^!j_!\mathcal{F}\simeq\pi_!\mathcal{F}$，其中 $\pi:\operatorname{Bun}'_1\to\operatorname{Bun}_1$ 为投影。  
   *为什么*：伸缩作用把 $\operatorname{Bun}_1^+$ 收缩到零截面，$!$-推前沿纤维可用投影代替。
4. 模去叠性的 $\mathbb{G}_m$ 因子后，$\pi$ 是 Abel–Jacobi 映射 $\operatorname{AJ}^d:X^{(d)}\to\operatorname{Pic}^d$。  
   *为什么*：$\operatorname{Bun}'_1\to\operatorname{Bun}_1$ 在忘掉 $\mathbb{G}_m$ 后把除子映为其线丛。
5. 由 Deligne 定理，$d>n(2g-2)$ 时 $\operatorname{AJ}^d_!(E^{(d)})=0$；对 $n=2$ 即 $d>4(g-1)$，于是边界项消失。  
   *为什么*：这正是讲义引用的 Deligne 关于 Abel–Jacobi 的消失定理。

> 缺口：讲义把边界项的消失归约为 Deligne 关于 Abel–Jacobi 的消失定理（对几何不可约、秩 $n>1$ 的 $E$：$d>n(2g-2)\Rightarrow\operatorname{AJ}^d_!(E^{(d)})=0$），该定理只引用不证明；完整证明见讲义所引 [KL85]（并见 [FGKV98]）。

*出处*：定理 5.4.1 / 原书 p.34


## 易错点

- 不能去掉「几何不可约」：若 $E$ 含来自真抛物子群或真子局部系统的分量，$E^{(d)}$ 混入低秩成分，消失一般不成立。
- 注意 $i$ 是零截面的闭嵌入，$i^!$ 才是与紧支撑推前天然配对的那一个。
- 定理的界是 $d>4(g-1)$，不是 $d\ge4(g-1)$。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§5.4 Drinfeld 关于 GL_2 的洁净延拓定理，p.34（PDF p.34），`源码/chapters/ch05.tex:53-74（定理 5.4.1 及其证明）`

## 核验

状态：`source-only`（2026-11-18）
- nLab：https://ncatlab.org/nlab/show/geometric+Langlands+correspondence — The page does not state Drinfeld's clean-extension theorem or the bound d>4(g−1).

## 关联

- `glc/concept/gl2-fourier-description`
- `glc/concept/vanishing-theorem`
- `glc/concept/cleanness-expected`
