---
id: glc/concept/aut-e-cuspidal
type: concept
track: E
---

# $\operatorname{Aut}_E$ 的尖点性

> $\operatorname{Aut}_E$ 的真抛物常数项都消失：每个常数项函子经 $k<n$ 的 $\operatorname{Bun}_k$ 上平均操作分解，而几何不可约秩 $n$ 局部系统 $E$ 的平均定理使该贡献为零。

**问题**：为什么 $\operatorname{Aut}_E$ 的尖点性不需要逐项计算常数项，而可以由同一个消失定理一次性地给出？

## 定义

$\operatorname{Aut}_E$ 是尖点层。原因是洁净延拓论证中所用的同一个消失定理：$\operatorname{GL}_n$ 的每个真抛物常数项函子，都经由某个 $k<n$ 的 $\operatorname{Bun}_k$ 上的平均操作分解，而几何不可约秩 $n$ 局部系统 $E$ 的平均定理迫使该贡献消失。因此，$\operatorname{Aut}_E$ 的所有真抛物常数项均消失。所谓真抛物常数项函子，是沿抛物子群丛 $\operatorname{Bun}_P\to\operatorname{Bun}_n$ 的 $!$-推前再拉回的复合，对应经典自守表示里的常数项。

*记号*：$P\subset\operatorname{GL}_n$ 是真抛物子群，$\operatorname{Bun}_P$ 是 $P$-丛的叠，$\operatorname{Bun}_P\to\operatorname{Bun}_n$ 是遗忘映射；『常数项』指该映射的 $!$-推前再拉回；$k<n$ 指 $P$ 的 Levi 分块中某个 $\operatorname{GL}_k$ 因子的秩；『平均定理』指第 5 章关于 $\operatorname{Av}$ 的消失结论。

## 要点

- 对 $\operatorname{GL}_n$，真抛物 $P$ 的 Levi 是 $\operatorname{GL}_{d_1}\times\cdots\times\operatorname{GL}_{d_r}$（$r\ge2$），其中必有一块 $k<n$——这是『真』的算术含义。
- 常数项函子是『沿 $\operatorname{Bun}_P\to\operatorname{Bun}_n$ 的 $!$-推前再拉回』的复合，与经典自守表示里的常数项逐字对应。
- 关键不是逐项硬算，而是把每个真抛物常数项化成同一个消失定理：先到某个 $\operatorname{Bun}_k$（$k<n$）、再作平均，平均定理正给出这一项为零。
- 用的是『洁净延拓论证中所用的同一个消失定理』——同一工具在延拓与尖点性两处各用一次。
- 结论是对**所有**真抛物同时成立的，不需要对每个 $P$ 单独验证。

## 关键公式

- $\text{常数项}_P:\ D(\operatorname{Bun}_n)\xrightarrow{(\operatorname{Bun}_P\to\operatorname{Bun}_n)^*}D(\operatorname{Bun}_P)\xrightarrow{(\operatorname{Bun}_P\to\operatorname{Bun}_n)_!}D(\operatorname{Bun}_n)$
- $P\ \text{真抛物}\ \Longrightarrow\ \text{Levi}\ \operatorname{GL}_{d_1}\times\cdots\times\operatorname{GL}_{d_r}\ \text{中含某个}\ k<n$
- $\text{常数项}_P(\operatorname{Aut}_E)=0\quad\text{对一切真抛物}\ P$

## 定理与证明

### $\operatorname{Aut}_E$ 的尖点性（要点（有缺口））

$\operatorname{Aut}_E$ 的所有真抛物常数项均消失，即 $\operatorname{Aut}_E$ 是尖点层。

1. 对 $\operatorname{GL}_n$ 的任一真抛物 $P$，其 Levi 分块 $\operatorname{GL}_{d_1}\times\cdots\times\operatorname{GL}_{d_r}$（$r\ge2$）中必有一块秩 $k<n$。  
   *为什么*：若所有 $d_i=n$ 则 $r=1$、$P$ 不是真抛物；故真性等价于存在 $k<n$ 的块。
2. 于是该真抛物常数项函子经由某个 $k<n$ 的 $\operatorname{Bun}_k$ 上的平均操作分解。  
   *为什么*：常数项沿 $\operatorname{Bun}_P\to\operatorname{Bun}_n$ 作 $!$-推前再拉回，Levi 的每一块对应一次沿相应 $\operatorname{Bun}_{d_i}$ 的操作，其中 $k<n$ 的那一块留下平均。
3. 几何不可约秩 $n$ 局部系统 $E$ 的平均定理迫使该贡献消失，故 $\operatorname{Aut}_E$ 的所有真抛物常数项为零。  
   *为什么*：平均定理（定理 5.7.2）在 $\operatorname{rank} E=n$ 且 $E$ 几何不可约时给出 $\operatorname{Bun}_k$（$k<n$）上相应平均为零，正是洁净延拓论证中用过的同一个消失定理。

> 缺口：讲义只述不证：原书给出一段思路（『每个真抛物常数项函子都经由某个 $k<n$ 的 $\operatorname{Bun}_k$ 上的平均操作分解，而平均定理迫使该贡献消失』），未展开该分解的具体构造，平均定理本身也在第 5 章（定理 5.7.2）。

*出处*：§8.6 / 原书 p.47


## 易错点

- 尖点性只对**真**抛物而言：全抛物 $P=\operatorname{GL}_n$ 的常数项就是 $\operatorname{Aut}_E$ 自身，不为零。
- 平均定理要求 $E$ 几何不可约且 $\operatorname{rank} E=n$；少任何一个条件，消失性都不成立。
- 常数项函子是『$!$-推前再拉回』，方向与 $*$-版本不同；把它写成 $(\operatorname{Bun}_P\to\operatorname{Bun}_n)_*$ 会得到不同的函子。
- 不要把『所有真抛物常数项消失』误读为『$\operatorname{Aut}_E$ 在每个 $\operatorname{Bun}_k$（$k<n$）上的限制为零』：消失发生在平均操作之后，不是限制本身。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§8.6 延拓到整个 $\operatorname{Bun}_n$ 及尖点性，p.47（PDF p.47），`源码/chapters/ch08.tex:123（尖点性论证）；124-126 为编者注`

## 核验

状态：`source-only`（2026-11-18）
- arXiv：https://arxiv.org/abs/alg-geom/9703022 — 摘要两次强调所构造的是「unramified cuspidal automorphic functions on $\mathrm{GL}_n(\mathbb A)$」——支持卡里结论层面：$\operatorname{Aut}_E$ 对应的自守函数是尖点的，故 $\operatorname{Aut}_E$ 是尖点层；摘要不含「真抛物常数项经某个 $\operatorname{Bun}_k$（$k<n$）上的平均操作分解」的机制，也不含平均定理。

## 关联

- `glc/concept/top-hecke-relation`
- `glc/concept/aut-e-whittaker-laumon`
