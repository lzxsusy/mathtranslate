# Clifford 环面

> `functoriality/concept/clifford-torus` ｜ track B ｜ draft

**一句话**：CP^n 中所有坐标同模的轨道 T^n_Cl，其 Floer 上同调由约化对应与带收缩同构归纳算出，同构于 Z^{2^n}。

**自测**：Clifford 环面的 Floer 上同调为什么能用辛约化与带收缩同构算出来，而不是直接硬算？

## 定义

Clifford 环面是 $\CP^n$ 中的拉格朗日子流形 $T^n_{\mathrm{Cl}}:=\{[z_0:\cdots:z_n]\mid |z_0|=\cdots=|z_n|\}\subset\CP^n$，即所有坐标模长相等的点构成的环面轨道。对每个真子集 $A\subsetneq\{1,\ldots,n\}$，相应的对应 $\Sigma_A$ 由 $\Sigma_A:=\{([z_j]_{j\notin A},[z])\mid |z_k|^2=\frac1{n+1}\sum_{j=0}^n|z_j|^2\ \forall k\in A\}$ 给出，它是 $\CP^n/\!/T^{\#A}$ 的矩对应。原文用强归纳证明 $\HF^*(T^n_{\mathrm{Cl}},T^n_{\mathrm{Cl}})\simeq\HF^*(T^{n-1}_{\mathrm{Cl}},T^{n-1}_{\mathrm{Cl}})^{\otimes2}$，故 $\HF^*(T^n_{\mathrm{Cl}},T^n_{\mathrm{Cl}})\cong\Z^{2^n}$。

记号：$\#A$ 是子集 $A$ 的元素个数；$[z_j]_{j\notin A}$ 是去掉 $A$ 中坐标后得到的射影点（落在 $\CP^{n-\#A}$ 中）；$\Sigma_A$ 读作「从 $\CP^{n-\#A}$ 到 $\CP^n$ 的对应」。

## 要点

- 计算路线是三条工具的串联：辛约化给出 $\Sigma_A$ 这类对应，拉格朗日对应给出函子性，带收缩同构把三个拉格朗日的拼接复形化归为两个。
- 归纳步的关键是图 24：四个不同的拼接 Floer 复形通过带收缩同构彼此同构，从而把 $n$ 维情形拆成两个 $n-1$ 维因子。
- 结论 $\HF^*(T^n_{\mathrm{Cl}},T^n_{\mathrm{Cl}})\cong\Z^{2^n}$ 与 $T^n_{\mathrm{Cl}}$ 是 $\CP^n$ 中的环面轨道相符：维数为 $2^n$，相当于每个坐标方向贡献一个二值选择。
- 它是检验整套函子性机器（约化对应 + 带收缩 + 拼接 Floer 上同调）能否真的算出几何量的标准算例。
- 严格计算仍依赖单调性等默认几何假设；原文的「强归纳」是在这些假设下进行的。

## 公式

$T^n_{\mathrm{Cl}}:=\{[z_0:\cdots:z_n]\mid |z_0|=\cdots=|z_n|\}\subset\CP^n$
$|z_k|^2=\frac1{n+1}\sum_{j=0}^n|z_j|^2\ \forall k\in A$
$\HF^*(T^n_{\mathrm{Cl}},T^n_{\mathrm{Cl}})\simeq\HF^*(T^{n-1}_{\mathrm{Cl}},T^{n-1}_{\mathrm{Cl}})^{\otimes2}$

## 定理与证明

### Clifford 环面的 Floer 上同调

在标准单调性假设下，HF*(T^n_Cl,T^n_Cl)≅HF*(T^{n-1}_Cl,T^{n-1}_Cl)^{⊗2}，从而 HF*(T^n_Cl,T^n_Cl)≅Z^{2^n}。

（sketch；来源：原书 p.35 §3.9）

1. 把 $\HF^*(T^n_{\mathrm{Cl}},T^n_{\mathrm{Cl}})$ 写成经过 $\Sigma_A$ 的拼接 Floer 上同调。  
   为什么：约化把环面拆成两部分，对应的函子性给出拼接表达式。
2. 对某个合适的子集 $A$ 用带收缩同构 (62)，把三重带（三片）收缩成双重带。  
   为什么：这一步把 $n$ 维拼接复形化归为两个 $n-1$ 维因子的张量积。
3. 得到 $\HF^*(T^n_{\mathrm{Cl}},T^n_{\mathrm{Cl}})\simeq\HF^*(T^{n-1}_{\mathrm{Cl}},T^{n-1}_{\mathrm{Cl}})^{\otimes2}$，作为归纳步。  
   为什么：这是归纳的递推式。
4. 对 $n$ 强归纳，基例为 $\HF^*(T^0_{\mathrm{Cl}},T^0_{\mathrm{Cl}})\cong\Z$，得 $\Z^{2^n}$。  
   为什么：每归纳一步自由度翻倍。

缺口：原文只说「强归纳」并指向图 24 的四个同构表达式，未写出 $\Sigma_A$ 的选择与每一步的链层构造；基例与维数记账亦未展开。

### 约化给出矩对应 Σ_A

对 A⊊{1,…,n}，Σ_A⊂CP^{n-#A}×CP^n 是 CP^n//T^{#A} 的矩对应。

（none；来源：原书 p.35 §3.9）


缺口：原文作为例 3.21 陈述并引 WW10b 定理 6.2.1，未给证明。

## 易错点

- 把 $T^n_{\mathrm{Cl}}$ 当成 $\CP^n$ 中的坐标环面 $(S^1)^n$ 的某个具体嵌入而忽略「所有坐标模长相等」这一条件。
- 把 $\Sigma_A$ 的两个因子写反：它是 $\CP^{n-\#A}\times\CP^n$ 中的对应，小因子在前。
- 以为归纳是直接对 Floer 链复形做分块，而不是经由带收缩同构把三重带换成双重带。
- 把 $\Z^{2^n}$ 当成 $\Z^{n+1}$ 之类的笔误：环面轨道在 $n+1$ 个坐标上各有一个二值选择，秩确实是 $2^n$。

## 参考与关联

- Abouzaid & Bottman, Functoriality in categorical symplectic geometry (arXiv:2210.11159v1)，§3.9，p.34–35（原书 p.34–35 §3.9）

关联：`functoriality/concept/symplectic-reduction`、`functoriality/concept/strip-shrinking`、`functoriality/concept/lagrangian-correspondence`、`functoriality/deriv/reduction-clifford-example`

来源说明：原书 p.35 §3.9（例 3.21 与图 24 的转述）；公式 (87)(88) 与归纳同构取自中译本 chapter3.tex。
