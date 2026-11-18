---
id: dmod/concept/irreducible-holonomic-classification
type: concept
track: G
---

# 不可约完整模的分类

> 不可约完整模都形如 $L(V,\tau)$：由光滑子簇 $V$ 上的不可约联络 $\tau$ 延拓而来；同构当且仅当闭包相同且 $\tau$ 在交叠上同构。

**问题**：不可约完整 $\mathcal D_X$-模如何由「光滑子簇 + 其上的不可约联络」这对数据分类，两个这样的模何时同构？

## 定义

设 $V\subset X$ 是连通光滑子簇，$j:V\to X$ 是自然浸入，$\tau$ 是 $V$ 上不可约联络。标准 $\mathcal D_X$-模定义为直像 $I(V,\tau)=j_+(\tau)$，它是完整 $\mathcal D_X$-模，支集等于 $\bar V$。由引理 5.4.1，$I(V,\tau)$ 含唯一的不可约 $\mathcal D_X$-子模，记为 $L(V,\tau)$，称为附属于 $(V,\tau)$ 的不可约模；其支集等于 $\bar V$，且商 $I(V,\tau)/L(V,\tau)$ 的支集含于 $\bar V\setminus V$（命题 5.4.3）。定理 5.4.4 断言每个不可约完整 $\mathcal D_X$-模都同构于某个 $L(V,\tau)$，并给出同构判据。

*记号*：$j_+$：沿浸入 $j$ 的（代数）直像；$I(V,\tau)=j_+(\tau)$：标准 $\mathcal D_X$-模；$L(V,\tau)$：$I(V,\tau)$ 的唯一不可约子模；$\bar V$：$V$ 在 $X$ 中的闭包；$\tau$：$V$ 上的不可约联络。

## 要点

- 标准模 $I(V,\tau)=j_+(\tau)$ 是完整的，支集为 $\bar V$；它含唯一的不可约子模 $L(V,\tau)$（引理 5.4.1）。
- 商 $I(V,\tau)/L(V,\tau)$ 的支集含于 $\bar V\setminus V$：标准模与不可约模只在边界上不同（命题 5.4.3）。
- 定理 5.4.4(i)：每个不可约完整 $\mathcal D_X$-模都同构于某个 $L(V,\tau)$，其中 $V$ 是其支集中的不可约开光滑仿射子簇。
- 定理 5.4.4(ii)：$L(V,\tau)\cong L(V',\tau')$ 当且仅当 $\bar V=\bar V'$ 且存在 $V\cap V'$ 的非空开仿射子簇 $V''$ 使 $\tau|_{V''}\cong\tau'|_{V''}$。
- 分类依赖于沿开集延拓的存在唯一性（推论 5.4.2）：支集取闭包，模由它在开集上的限制唯一决定。

## 关键公式

- $I(V,\tau)=j_+(\tau)$
- $L(V,\tau)\subset I(V,\tau),\qquad\operatorname{supp}L(V,\tau)=\bar V$
- $L(V,\tau)\cong L(V',\tau')\iff \bar V=\bar V'\ \text{且}\ \exists V''\subset V\cap V'\ \text{开仿射}:\ \tau|_{V''}\cong\tau'|_{V''}$

## 定理与证明

### 定理 5.4.4（不可约完整模的分类）（完整）

设 $X$ 是光滑簇。(i) 若 $\mathcal V$ 是不可约完整 $\mathcal D_X$-模，则存在 $\mathcal V$ 的支集中的不可约开光滑仿射子簇 $V$ 及 $V$ 上不可约联络 $\tau$，使 $\mathcal V\cong L(V,\tau)$。(ii) 设 $V,V'$ 是 $X$ 的不可约光滑仿射子簇，$\tau,\tau'$ 分别是其上的不可约联络；则 $L(V,\tau)\cong L(V',\tau')$ 当且仅当 (a) $\bar V=\bar V'$；(b) 存在 $V\cap V'$ 的非空开仿射子簇 $V''$ 使 $\tau|_{V''}\cong\tau'|_{V''}$。

1. (i) 取 $X$ 的开仿射子集 $U$ 使 $V=\operatorname{supp}(\mathcal V)\cap U$ 是 $U$ 的闭光滑子簇；由 Kashiwara 定理存在 $V$ 上不可约完整模 $\mathcal W$ 使 $(j_V)_+(\mathcal W)\cong\mathcal V|_U$。  
   *为什么*：$\mathcal V$ 的支集是不可约闭子集，$\mathcal V|_U$ 不可约完整；Kashiwara 定理把支集含于 $V$ 的模与 $V$ 上的模等同。
2. 把 $\mathcal W$ 限制到 $V$ 的开稠密仿射子簇 $V'$，使 $\mathcal W|_{V'}$ 是联络；必要时缩小 $U$，设 $\mathcal W$ 本身是联络，取 $\tau=\mathcal W$，则 $\mathcal V|_U\cong L(V,\tau)|_U$。  
   *为什么*：$\mathcal W$ 在其支集的开稠密子集上成为联络；由 $L$ 的构造 $L(V,\tau)|_U$ 与 $\mathcal V|_U$ 支集相同且不可约。
3. 由推论 5.4.2，$\mathcal V|_U\cong L(V,\tau)|_U$ 蕴含 $\mathcal V\cong L(V,\tau)$。  
   *为什么*：不可约完整模沿开集的延拓在同构意义下唯一，且支集取闭包。
4. (ii) 同构给出支集相等，得 (a)；设公共支集为 $S$，则 $V,V'$ 在 $S$ 中开稠密，取 $V''\subset V\cap V'$ 非空开仿射。由推论 5.4.2，$L(V,\tau)\cong L(V',\tau')$ 等价于 $j_+(\tau|_{V''})\cong j_+(\tau'|_{V''})$，再由 Kashiwara 定理等价于 $\tau|_{V''}\cong\tau'|_{V''}$，即 (b)。  
   *为什么*：Kashiwara 定理对闭浸入是范畴等价，故直像同构当且仅当原模同构；延拓的唯一性把整体同构归约到 $V''$ 上。

*出处*：定理 5.4.4 / 原书 V §4, p.139–140

### 命题 5.4.3（标准模的唯一不可约子模）（完整）

标准 $\mathcal D_X$-模 $I(V,\tau)$ 含唯一不可约子模 $L(V,\tau)$；$L(V,\tau)$ 的支集等于 $\bar V$，且 $I(V,\tau)/L(V,\tau)$ 的支集含于 $\bar V\setminus V$。

1. 记 $\mathcal Q=I(V,\tau)/L(V,\tau)$，取 $U=X\setminus(\bar V\setminus V)$，则 $V$ 在 $U$ 中闭。  
   *为什么*：$\bar V\setminus V$ 是 $\bar V$ 中闭的子集，去掉它后 $V$ 成为 $U$ 的闭子簇。
2. 把短正合列 $0\to L(V,\tau)\to I(V,\tau)\to\mathcal Q\to0$ 限制到 $U$，由引理 5.4.1 的构造得 $\mathcal Q|_U=0$，故 $\operatorname{supp}(\mathcal Q)\subset\bar V\setminus V$。  
   *为什么*：在 $U$ 上 $I(V,\tau)$ 的唯一不可约子模就是它本身（$V$ 在 $U$ 中闭），故商为零。

*出处*：命题 5.4.3 / 原书 V §4, p.139


## 易错点

- $V$ 不必是 $X$ 的闭子簇：$L(V,\tau)$ 的支集是闭包 $\bar V$，而 $V$ 本身只是支集中的开稠密光滑部分。
- 同构判据 (b) 只要求在交叠 $V\cap V'$ 的某个非空开仿射子簇上 $\tau\cong\tau'$，不是在整个 $V\cap V'$ 上；取限制是必要的。
- 标准模 $I(V,\tau)$ 一般不可约：它只含唯一的不可约子模 $L(V,\tau)$，两者相差一个支集在 $\bar V\setminus V$ 的商。
- 定理只分类不可约完整模；一般完整模有限长（定理 5.1.3），是这些不可约模的扩张，但扩张不唯一，故一般分类不由此直接给出。

## 出处

- Miličić《Lectures on the Algebraic Theory of D-Modules》中译本（校订批注本），V §4 不可约完整模的分类，p.139（PDF p.145），`源码/chapters/chap5.tex:239-253（定义与命题 5.4.3）`
- Miličić《Lectures on the Algebraic Theory of D-Modules》中译本（校订批注本），V §4 不可约完整模的分类，p.139-140（PDF p.145-146），`源码/chapters/chap5.tex:257-273（定理 5.4.4）`

## 核验

状态：`source-only`（2026-11-19）

## 关联

- `dmod/concept/holonomicity-preserved-by-direct-image`
- `dmod/concept/d-module-on-affine-line`
- `dmod/concept/riemann-hilbert-correspondence`
