---
id: glc/concept/good-open-substack
type: concept
track: E
---

# 好开子叠 $C_k$ 的技术性加强

> 为使扩张逐纤维计算可行，给好开子叠 $C_k$ 加开条件 $\operatorname{Hom}(M,L^{\mathrm{est}})=0$，从而『$\mathring M\oplus J\in C_k$』推出『$M\in C_k$』。

**问题**：为什么加了 $\operatorname{Hom}(M,L^{\mathrm{est}})=0$ 之后，纤维计算里就可以忽略 $M\in C_k$？

## 定义

设 $C_k$ 是洁净性论证所用的良好开子叠。可以对 $C_k$ 作一个技术性加强，要求对每个扩张 $0\to\mathring M\to M\to J\to0$ 都有 $\mathring M\oplus J\in C_k\Rightarrow M\in C_k$。确保这一蕴涵的一种方法是选取线丛 $L^{\mathrm{est}}$ 并施加额外的开条件 $\operatorname{Hom}(M,L^{\mathrm{est}})=0$：事实上，对挠层 $J$ 和无挠目标 $L^{\mathrm{est}}$ 有 $\operatorname{Hom}(J,L^{\mathrm{est}})=0$，因此 $\mathring M\oplus J\in C_k$ 等价于 $\mathring M\in C_k$，对扩张应用 $\operatorname{Hom}(-,L^{\mathrm{est}})$ 便得到 $M\in C_k$。于是在纤维计算中可以忽略条件 $M\in C_k$。

*记号*：$L^{\mathrm{est}}$ 是一个选定的线丛（无挠），上标 est 只是讲义给它的名字；$\operatorname{Hom}(-,-)$ 为层同态群；$C_k$ 与 $J$ 的约定同扩张叠 $H$ 条目。

## 要点

- 加强的实质是把 $C_k$ 缩小：多要求一条开条件 $\operatorname{Hom}(M,L^{\mathrm{est}})=0$，使 $C_k$ 变小但仍是开子叠。
- 消去的关键是 $\operatorname{Hom}(J,L^{\mathrm{est}})=0$：$J$ 是挠层、$L^{\mathrm{est}}$ 无挠，两者之间没有非零同态。
- 由此 $\mathring M\oplus J\in C_k\iff\mathring M\in C_k$；对扩张取 $\operatorname{Hom}(-,L^{\mathrm{est}})$ 即把 $\mathring M$ 一侧的消去传给中间项 $M$。
- 收益：扩张 $0\to\mathring M\to M\to J\to0$ 自动落在 $C_k$ 内，$H$ 的逐纤维描述不必再带 $C_k$ 条件，才成为仿射丛。

## 关键公式

- $\mathring M\oplus J\in C_k\ \Longrightarrow\ M\in C_k$
- $\operatorname{Hom}(M,L^{\mathrm{est}})=0$
- $\operatorname{Hom}(J,L^{\mathrm{est}})=0$

## 定理与证明

### 技术性加强（扩张保持 $C_k$）（完整）

设 $L^{\mathrm{est}}$ 为线丛，并把开条件 $\operatorname{Hom}(M,L^{\mathrm{est}})=0$ 纳入 $C_k$ 的定义。则对任何扩张 $0\to\mathring M\to M\to J\to0$（$J$ 挠），只要 $\mathring M\oplus J\in C_k$，就有 $M\in C_k$。

1. 由 $J$ 挠、$L^{\mathrm{est}}$ 无挠得 $\operatorname{Hom}(J,L^{\mathrm{est}})=0$，故 $\mathring M\oplus J\in C_k$ 中的 $J$ 分量不贡献条件，等价于 $\mathring M\in C_k$。  
   *为什么*：挠层到无挠层的同态必为零。
2. 对短正合列 $0\to\mathring M\to M\to J\to0$ 应用 $\operatorname{Hom}(-,L^{\mathrm{est}})$：$\operatorname{Hom}(M,L^{\mathrm{est}})\hookrightarrow\operatorname{Hom}(\mathring M,L^{\mathrm{est}})$，右端为零，故 $\operatorname{Hom}(M,L^{\mathrm{est}})=0$，即 $M\in C_k$。  
   *为什么*：$\operatorname{Hom}(-,L^{\mathrm{est}})$ 把短正合列变为左正合列，于是 $\operatorname{Hom}(M,L^{\mathrm{est}})$ 是 $\operatorname{Hom}(\mathring M,L^{\mathrm{est}})$ 的子对象。

*出处*：§7.1 / 原书 p.40


## 易错点

- $L^{\mathrm{est}}$ 必须是线丛（无挠）：若换成有挠对象，$\operatorname{Hom}(J,L^{\mathrm{est}})=0$ 不再成立，整个消去论证失效。
- 这不是『扩张一般地保持 $C_k$』的定理，而是通过加开条件人为做到的：$C_k$ 因此变小，引用 $C_k$ 的非空性时要按加强后的定义理解。
- 消去的是 $M\in C_k$ 这一条，不是 $J\in\operatorname{Tor}^\ell$ 或 $\mathring M\in\operatorname{Bun}_k$ 的前提。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§7.1 洁净性中剩下的引理，p.40（PDF p.40），`源码/chapters/ch07.tex:9-13（技术性加强与 $L^{\mathrm{est}}$ 论证）`

## 核验

状态：`source-only`（2026-11-18）
- nLab：https://ncatlab.org/nlab/show/coherent+sheaf — 页面只给 O_X-模/拟凝聚层与有限性的一般定义，未讨论「挠层到无挠线丛的 Hom 为 0」；卡中 Hom(J,L^{est})=0 是标准事实，但本页未载，无逐句支持。

## 关联

- `glc/concept/extension-stack-vanishing`
- `glc/concept/affine-bundle-base-change`
