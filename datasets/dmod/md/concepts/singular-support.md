---
id: dmod/concept/singular-support
type: concept
track: B
---

# 奇异支集

> 奇异支集是特征簇中 $\xi\neq0$ 的点投影回底空间所得的闭子簇，标出支集中出现非零余方向的位置。

**问题**：为什么特征簇里「非零余方向」那部分的投影是闭子簇，它与支集是什么关系？

## 定义

设 $M$ 是有限生成 $D(n)$-模。$M$ 的\emph{奇异支集}定义为 $$\operatorname{sing\,supp}(M)=\{x\in k^n\mid (x,\xi)\in\operatorname{Ch}(M)\ \text{对某个}\ \xi\neq0\}.$$ 等价地，它是 $\operatorname{Ch}(M)\setminus(k^n\times\{0\})$ 在投影 $\pi(x,\xi)=x$ 下的像。

*记号*：$k^n\times\{0\}\subset k^{2n}$ 是余切丛的零截面；$\pi:k^{2n}\to k^n$ 是投影；$\operatorname{Ch}(M)$ 是特征簇（见「特征簇」卡）。

## 要点

- $\operatorname{sing\,supp}(M)\subset\operatorname{supp}(M)$，因为 $\operatorname{supp}(M)=\pi(\operatorname{Ch}(M))$ 而奇异支集只取 $\xi\neq0$ 的点。
- $\operatorname{sing\,supp}(M)$ 是 $\operatorname{supp}(M)$ 的闭子簇（引理 7.6）。
- 证明把 $\operatorname{Ch}(M)\setminus(k^n\times\{0\})$ 经 $1\times p$ 映入 $k^n\times P^{n-1}(k)$，再用完全簇 $P^{n-1}(k)$ 上投影是闭映射。
- $\operatorname{Ch}(\mathcal O_n)=k^n\times\{0\}$ 给出 $\operatorname{sing\,supp}(\mathcal O_n)=\varnothing$；$\operatorname{Ch}(\Delta_n)=\{0\}\times k^n$ 给出 $\operatorname{sing\,supp}(\Delta_n)=\{0\}$。
- 奇异支集只记录「有非零余方向」的底空间点；零截面部分不贡献它。

## 关键公式

- $\operatorname{sing\,supp}(M)=\{x\in k^n\mid \exists\,\xi\neq0,\ (x,\xi)\in\operatorname{Ch}(M)\}$
- $\operatorname{sing\,supp}(M)=\pi\bigl(\operatorname{Ch}(M)\setminus(k^n\times\{0\})\bigr)$
- $\operatorname{sing\,supp}(M)\subset\operatorname{supp}(M)=\pi(\operatorname{Ch}(M))$

## 定理与证明

### 引理 7.6（奇异支集是闭子簇）（完整）

设 $M$ 是有限生成 $D(n)$-模，则 $\operatorname{sing\,supp}(M)$ 是 $\operatorname{supp}(M)$ 的闭子簇。

1. 令 $p:k^n\setminus\{0\}\to P^{n-1}(k)$ 为自然投射。则 $1\times p$ 把 $\operatorname{Ch}(M)\setminus(k^n\times\{0\})$ 映入 $k^n\times P^{n-1}(k)$ 中对应于齐次理想 $J(M)$ 的闭子簇。  
   *为什么*：$J(M)$ 关于 $\xi_1,\dots,\xi_n$ 齐次，故其零点集沿 $\xi$ 的伸缩不变，可以下降到射影空间。
2. 该像是 $k^n\times P^{n-1}(k)$ 中的闭子簇。  
   *为什么*：它是射影化后的闭子簇（构造上是闭集），闭子簇的像在有限型映射下仍为闭。
3. 投影 $k^n\times P^{n-1}(k)\to k^n$ 是闭映射。  
   *为什么*：$P^{n-1}(k)$ 是完全簇，完全簇到仿射簇的投影把闭集送到闭集。
4. 该闭子簇在此投影下的像正是 $\operatorname{sing\,supp}(M)$，故它是闭的；又它含于 $\operatorname{supp}(M)$，故是后者的闭子簇。  
   *为什么*：像的定义逐点对应「存在 $\xi\neq0$ 使 $(x,\xi)\in\operatorname{Ch}(M)$」。

*出处*：引理 7.6 / 原书 p.27


## 易错点

- 漏掉 $\xi\neq0$：把 $(x,0)$ 也算进去得到的是整个 $\operatorname{supp}(M)$，不再标出非零余方向。
- 奇异支集可以严格小于支集：$\mathcal O_n$ 的奇异支集为空，而支集是整个 $k^n$。
- 证明用到 $P^{n-1}(k)$ 的完全性（$k$ 代数闭）；这是该论证的关键输入，不能省略。
- 奇异支集是 $k^n$ 的子簇，不是 $k^{2n}$ 的子簇；后者是特征簇。

## 出处

- Miličić《Lectures on the Algebraic Theory of D-Modules》（中译校订批注本，150 页），§7 特征簇，p.27（PDF p.33），`源码/chapters/chap1.tex:991-1013（命题 7.5、引理 7.6）`

## 核验

状态：`source-only`（2026-11-19）

## 关联

- `dmod/concept/characteristic-variety`
- `dmod/concept/characteristic-ideal`
- `dmod/concept/holonomic-module`
