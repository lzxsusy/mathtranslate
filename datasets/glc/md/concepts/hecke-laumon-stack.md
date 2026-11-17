---
id: glc/concept/hecke-laumon-stack
type: concept
track: E
---

# Hecke–Laumon 叠与函子 $\mathrm{HL}_k^d$

> $\mathrm{HL}_k^d$ 是『秩 $k$ 凝聚层的子层-商对，商为长度 $d$ 挠层』的叠；函子沿记 $M$ 的映射拉回、再沿记 $(\mathcal T,M')$ 的紧支撑推前，附移位 $[dk]$ 与扭转 $(dk/2)$。

**问题**：Hecke–Laumon 叠为什么用『$0\to M'\to M\to\mathcal T\to0$』而不是通常 Hecke 对应的修改格，函子两侧又为什么一拉一推？

## 定义

对 $k\ge0$、$d\ge0$，定义 Hecke–Laumon 叠 $\mathrm{HL}_k^d:=\{0\to M'\to M\to\mathcal T\to0\mid M,M'\in\operatorname{Coh}_k,\ \mathcal T\in\operatorname{Tor}^d\}$。它具有映射 $\operatorname{Coh}_k\xleftarrow{\overleftarrow h}\mathrm{HL}_k^d\xrightarrow{\overrightarrow h}\operatorname{Tor}^d\times\operatorname{Coh}_k$，其中 $\overleftarrow h$ 记住 $M$，$\overrightarrow h$ 记住 $(\mathcal T,M')$。相应函子为 $\mathrm{HL}_k^d(\mathcal K):=\overrightarrow h_!\overleftarrow h^*\mathcal K[dk](dk/2)$，$\mathcal K\in D(\operatorname{Coh}_k)$。

*记号*：$\operatorname{Coh}_k$ 是秩 $k$ 无挠凝聚层（向量丛）的叠，$\operatorname{Tor}^d$ 是长度 $d$ 挠层的叠；$\overleftarrow h$ 取『大层 $M$』，$\overrightarrow h$ 取『商 $\mathcal T$ 与子层 $M'$』；$[dk]$ 是移位、$(dk/2)$ 是 Tate 扭转；$D(-)$ 是导出范畴。

## 要点

- 一个点就是一条短正合列：$M'$ 是子层、$M$ 是大层、$\mathcal T$ 是长度 $d$ 的挠商；三者互相决定其中之二。
- 两个映射的分工是『记住哪一部分』：$\overleftarrow h$ 只记 $M$（丢掉子层与商），$\overrightarrow h$ 只记 $(\mathcal T,M')$（丢掉中间的大层）。
- 函子是『拉回 + 紧支撑推前』的复合，两个映射各用一次；这不是通常 Hecke 对应的『沿对应推拉』，而是『沿两条腿一拉一推』。
- 移位与扭转同时出现为 $[dk](dk/2)$：一个管维数、一个管 Tate 归一化，二者合在一起构成该函子的标准归一化。
- $d=0$ 时 $\mathcal T=0$、$M'=M$，叠退化为 $\operatorname{Coh}_k$ 上的恒等对应，这是定义*中『$d=0$ 时显然的归一化』的几何来源。

## 关键公式

- $\mathrm{HL}_k^d:=\{0\to M'\to M\to\mathcal T\to0\mid M,M'\in\operatorname{Coh}_k,\ \mathcal T\in\operatorname{Tor}^d\}$
- $\operatorname{Coh}_k\xleftarrow{\overleftarrow h}\mathrm{HL}_k^d\xrightarrow{\overrightarrow h}\operatorname{Tor}^d\times\operatorname{Coh}_k$
- $\mathrm{HL}_k^d(\mathcal K):=\overrightarrow h_!\overleftarrow h^*\mathcal K[dk](dk/2),\qquad\mathcal K\in D(\operatorname{Coh}_k)$

## 易错点

- $\mathrm{HL}_k^d$ 里的 $M,M'$ 都是秩 $k$ 的无挠层（$\operatorname{Coh}_k$），$\mathcal T$ 才是挠层；不要以为 $M'$ 是挠的。
- $\overrightarrow h$ 记的是 $(\mathcal T,M')$ 这一对，不是单独 $\mathcal T$；忘记 $M'$ 会丢掉子层信息，无法还原 $M$。
- $[dk]$ 与 $(dk/2)$ 不能只取其一：两者分别对应移位与扭转，缺一个就得不到与 Hecke–Laumon 特征层定义相容的归一化。
- 这是『叠 + 函子』的构造卡，本身不含定理；特征性质要到 Hecke–Laumon 特征层的定义才出现。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§8.4 Hecke–Laumon 对应，p.45-46（PDF p.45-46），`源码/chapters/ch08.tex:56-61（$\mathrm{HL}_k^d$ 的定义、两条腿与函子）`

## 核验

状态：`source-only`（2026-11-18）
- JAMS：https://www.ams.org/journals/jams/2002-15-02/S0894-0347-01-00388-5/S0894-0347-01-00388-5.pdf — 正文：「the stack $\mathcal{HL}_n^d$ classifies short exact sequences $0\to\mathcal M'\to\mathcal M\to\mathcal T\to0$ with $\mathcal M'\in\mathcal{C}oh_n$, $\mathcal T\in\mathcal Coh_0^d$」，两投影分别送 $\mathcal M$ 与 $(\mathcal M',\mathcal T)$，记作 $\mathcal{C}oh_n\xleftarrow{h^-}\mathcal{HL}_n^d\xrightarrow{h^-}\mathcal Coh_0^d\times\mathcal{C}oh_n$。与卡里 $\mathrm{HL}_k^d$ 的定义及 $\overleftarrow h/\overrightarrow h$ 双向投影一致；检索片段未出现 $[dk](dk/2)$ 的移位/扭转归一化。

## 关联

- `glc/concept/hecke-laumon-eigensheaf`
- `glc/concept/torsion-stack-local-model`
- `glc/concept/laumon-factorization`
