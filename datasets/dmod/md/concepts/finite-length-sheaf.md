---
id: dmod/concept/finite-length-sheaf
type: concept
track: C
---

# 有限长度 $\mathcal D_X$-模

> 有限长度指有有限滤过 $\{0\}=V_0\subsetneq\cdots\subsetneq V_n=V$ 使各商不可约，长度 $\ell(V)=n$；有限长度拟凝聚模自动凝聚，且可在开覆盖上局部检验。

**问题**：为什么有限长度模一定凝聚，而长度又可以在任意开覆盖上逐块计算再拼起来？

## 定义

设 $V$ 是拟凝聚 $\mathcal D_X$-模。$V$ 的滤过 $\{0\}=V_0\subsetneq V_1\subsetneq\cdots\subsetneq V_n=V$ 若每个商 $V_p/V_{p-1}$ 都是不可约 $\mathcal D_X$-模，则称其为 $V$ 的一个合成列，并记 $\ell(V)=n$ 为 $V$ 的长度。称 $V$ 有限长度，若这样的滤过存在。

*记号*：$\ell(V)$：$V$ 的长度；$V_p/V_{p-1}$：滤过的第 $p$ 个商。

## 要点

- 定义（chap3.tex:188-190）：有限滤过、各商不可约；长度 $\ell(V)$ 即滤过长度。
- 由命题 2.6，各商不可约故凝聚；再由凝聚模对扩张封闭（讲义 chap3.tex:190 的原话「由长度上的归纳和前面的命题」），得有限长度 $\Rightarrow$ 凝聚。
- 引理 2.8：$V$ 有限长度 $\iff$ 对任意开子集 $U$，$V|_U$ 有限长度 $\iff$ 存在开覆盖使每个 $V|_{U_i}$ 有限长度。
- 长度在短正合列上可加：$0\to U\to V\to W\to0$ 时 $\ell(V)=\ell(U)+\ell(W)$（引理 2.8 证明所用）。
- 有限长度是比凝聚更强的条件：凝聚模的支集可以任意大，有限长度模在不可约分支上才常见。

## 关键公式

- $\{0\}=V_0\subsetneq V_1\subsetneq\cdots\subsetneq V_n=V,\qquad \ell(V)=n$
- $\ell(V)=\ell(U)+\ell(W)\quad\text{若}\ 0\to U\to V\to W\to 0\ \text{正合}$
- $\ell(V|_{U_j})=\ell(U|_{U_j})+\ell(W|_{U_j})$

## 定理与证明

### 有限长度的模是凝聚的（完整）

光滑代数簇 $X$ 上任意有限长度的拟凝聚 $\mathcal D_X$-模都是凝聚 $\mathcal D_X$-模。

1. 对长度 $n$ 归纳。$n=0$ 时 $V=0$，平凡凝聚；设结论对长度 $<n$ 成立。  
   *为什么*：长度为零即零模，零模显然凝聚，归纳起点成立。
2. 取合成列 $\{0\}=V_0\subsetneq\cdots\subsetneq V_n=V$，考虑短正合列 $0\to V_{n-1}\to V\to V/V_{n-1}\to0$。商 $V/V_{n-1}$ 不可约，由命题 2.6 凝聚；$V_{n-1}$ 长度为 $n-1$，由归纳假设凝聚。  
   *为什么*：合成列的最后一段把 $V$ 写成「长度 $n-1$ 的部分」与「不可约商」的扩张。
3. 凝聚 $\mathcal D_X$-模对扩张封闭（讲义 chap3.tex:190 的说明；仿射时即诺特环上有限生成模的子模与扩张仍有限生成），故 $V$ 凝聚。  
   *为什么*：诺特环上有限生成性对子模与扩张封闭，层化后即凝聚性对扩张封闭。

*出处*：chap3.tex:188-190

### 引理 2.8（有限长度的局部性）（要点（有缺口））

设 $V$ 是拟凝聚 $\mathcal D_X$-模。则下列条件等价：(i) $V$ 有限长度；(ii) 对任意开子集 $U$，$V|_U$ 有限长度；(iii) 存在开覆盖 $(U_j)$ 使每个 $V|_{U_j}$ 有限长度。

1. (i)$\Rightarrow$(ii)：把合成列限制到 $U$，商 $(V_p/V_{p-1})|_U$ 仍不可约或为零（引理 2.5），删去重复项后得 $V|_U$ 的合成列。  
   *为什么*：不可约模在开子集上的限制仍不可约或为零，故限制后仍是合成列。
2. (ii)$\Rightarrow$(iii) 显然。(iii)$\Rightarrow$(i)：对覆盖用长度加性 $\ell(V|_{U_j})=\ell(U|_{U_j})+\ell(W|_{U_j})$，把各块的合成列并起来，用有限覆盖与归纳得到整体合成列。  
   *为什么*：长度在短正合列上可加，故各局部块的合成列可以拼成整体合成列。

> 缺口：讲义在 chap3.tex:201-209 用 ℓ 的加性与归纳给出完整证明；本卡只保留两条方向的主线，故记为 sketch。

*出处*：引理 2.8 / chap3.tex:192-199


## 易错点

- 长度有限不等于模有限生成于 $\mathcal O_X$：$V$ 是 $\mathcal D_X$-模，$\ell(V)$ 数的是 $D_X$-子模链的长度。
- 合成列中各商必须不可约，仅「层层嵌套且商非零」不足以定义长度。
- 引理 2.8 的 (iii) 需要覆盖是开的；在闭子集上做同样的事没有可加性保证。

## 出处

- Miličić《Lectures on the Algebraic Theory of D-Modules》中译本，第 III 章 §2 凝聚 $\mathcal D_X$-模，p.79（PDF p.85），`源码/chapters/chap3.tex:188-209（有限长度定义与引理 2.8）`

## 核验

状态：`source-only`（2026-11-19）

## 关联

- `dmod/concept/coherent-d-module`
- `dmod/concept/support-and-irreducibility`
