---
id: glc/concept/extension-stack-vanishing
type: concept
track: E
---

# 扩张叠 $H$ 与紧支撑消失引理

> 参数化『$M_k$ 嵌入 $M$、商为固定挠层 $J$』的扩张叠，其上的紧支撑消失 $\mathrm{R}\Gamma_c(H,q_H^*\mathcal L_E)=0$ 是洁净性证明缺的最后一步。

**问题**：$q_H:H\to\operatorname{Tor}$ 记录的是什么，为什么消失是在 $H$ 上而不是在 $\operatorname{Tor}$ 上？

## 定义

固定 $M_k\in\operatorname{Bun}_k^0$（$\operatorname{Bun}_k^0$ 表示作为 Whittaker 旗终点出现的归一化次数零分支）、$J\in\operatorname{Tor}^\ell$、$\mathring M\in\operatorname{Bun}_k$ 以及 $a:M_k\to J$，并假设 $\mathring M\oplus J\in C_k$。考虑叠 $H:=\bigl\{0\to\mathring M\to M\to J\to0,\ M\in C_k;\ u:M_k\hookrightarrow M;\ (M_k\xrightarrow{u}M\twoheadrightarrow J)=a\bigr\}$。它有映射 $q_H:H\to\operatorname{Tor}$，$(M,u)\mapsto M/M_k$。洁净性证明所需的引理是紧支撑消失 $\mathrm{R}\Gamma_c(H,q_H^*\mathcal L_E)\simeq0$。

*记号*：$C_k$ 为洁净性论证所用的好开子叠（见好开子叠条目）；$\operatorname{Tor}^\ell$ 是长度为 $\ell$ 的挠层叠；$M_k\hookrightarrow M$ 表示 $M_k$ 作为子层嵌入 $M$；$\mathrm{R}\Gamma_c$ 为紧支撑上同调。

## 要点

- $H$ 的对象是『$M_k$ 经 $u$ 嵌入 $M$、且复合成给定的 $a:M_k\to J$』的 $C_k$ 中扩张 $0\to\mathring M\to M\to J\to0$；即 $H$ 记住扩张与嵌入两件数据。
- $q_H$ 记录的是商 $M/M_k$（落在 $\operatorname{Tor}$ 上），不是 $M$ 本身——这正是 $H$ 成为 $\operatorname{Tor}$ 上族的方式。
- 整个第 7 章的目标就是证 $\mathrm{R}\Gamma_c(H,q_H^*\mathcal L_E)=0$，它完成后洁净性证明即闭合。
- 讲义先对 $C_k$ 作技术性加强，使条件 $M\in C_k$ 在逐纤维计算中可以忽略。

## 关键公式

- $H:=\Bigl\{0\to\mathring M\to M\to J\to0,\ M\in C_k;\ u:M_k\hookrightarrow M;\ (M_k\xrightarrow{u}M\twoheadrightarrow J)=a\Bigr\}$
- $q_H:H\to\operatorname{Tor},\quad (M,u)\mapsto M/M_k$
- $\mathrm{R}\Gamma_c(H,q_H^*\mathcal L_E)\simeq0$

## 定理与证明

### 扩张叠上的紧支撑消失（要点（有缺口））

在 $M_k\in\operatorname{Bun}_k^0$、$J\in\operatorname{Tor}^\ell$、$\mathring M\in\operatorname{Bun}_k$、$a:M_k\to J$ 且 $\mathring M\oplus J\in C_k$ 的设定下，对 $q_H:H\to\operatorname{Tor}$、$(M,u)\mapsto M/M_k$，有 $\mathrm{R}\Gamma_c(H,q_H^*\mathcal L_E)\simeq0$。

1. 满射情形（§7.2）：若 $a:M_k\twoheadrightarrow J$，置 $\mathring M_k=\ker(a)$，则 $H$ 等同于修改叠 $\{\mathring M_k\}\times_{\operatorname{Bun}_k}\operatorname{Mod}_k^d\times_{\operatorname{Bun}_k}\{\mathring M\}$，$\mathrm{R}\Gamma_c$ 化为 $\operatorname{Av}_E^d$ 在 $\mathring M$ 处的茎。  
   *为什么*：满射时 $J$ 由 $M_k$ 商掉 $\mathring M_k$ 得到，$H$ 的自由数据只剩『$M_k$ 到 $\mathring M$ 的修改』。
2. 次数估计：$\mathring{\deg}M_k=0$，故 $\mathring{\deg}\mathring M_k=-\ell$；条件 $\mathring M\oplus J\in C_k$ 给出 $\mathring{\deg}\mathring M>nk(2g-2)$，于是 $d=\mathring{\deg}\mathring M-\mathring{\deg}\mathring M_k>nk(2g-2)+\ell>nk(2g-2)$，落入 $\operatorname{Av}_E^d$ 的消失范围。  
   *为什么*：$\operatorname{Av}_E^d$ 的消失定理对 $d>nk(2g-2)$ 成立（讲义 §9.1 的定理 9.1.1，取 $r=n$、$m=k$）。
3. 一般情形（§7.3）：令 $J'\subset J$ 为 $a$ 的像、$J''=J/J'$、$\mathring M_k=\ker(M_k\twoheadrightarrow J')$，并以 $H'$ 记以 $J'$ 为目标的满射版本。商序列 $0\to M'/M_k\to M/M_k\to M/M'\to0$ 给出 $H\to\operatorname{Tor}^{\mathrm{ses}}$，而 $H\to\operatorname{Tor}^{\mathrm{ses}}\times_{\operatorname{Tor}\times\operatorname{Tor}}H'$ 是仿射丛，故基变换成立，问题归约为证 $\mathrm{R}\Gamma_c\bigl((s,q)_!m^*\mathcal L_E|_{H'}\bigr)=0$。  
   *为什么*：仿射丛上 $!$ 推前只差一个常值移位与 Tate 扭转，而仿射丛的维数在连通分支上恒定，故不改变消失性。
4. 收尾（§7.5）：用命题 7.4.1 得 $(s,q)_!m^*\mathcal L_E|_{H'}\simeq(\mathcal L_E\boxtimes\mathcal L_E)|_{H'}$；第一个因子正是 $M_k\twoheadrightarrow J'$ 的满射情形，第二个因子是固定的剩余商 $J/J'$，故沿 $H'$ 的 $!$ 推前由满射情形消失，再由仿射丛基变换得 $\mathrm{R}\Gamma_c(H,q_H^*\mathcal L_E)=0$。  
   *为什么*：因子化把 $H'$ 上的对象拆成两个独立因子，其中依赖 $H'$ 的那个已经由满射情形处理，剩下的因子与 $H'$ 无关。

> 缺口：讲义把本引理的证明拆在 §7.2（满射情形）、§7.3（归约到像）、§7.5（收尾）三处，§7.1 只给陈述；且满射情形依赖 §9.1 的平均函子消失定理（定理 9.1.1），该定理在 §9 才证明。

*出处*：第 7 章（陈述 §7.1 / 原书 p.40；证明 §7.2–§7.5 / p.40–43）


## 易错点

- $q_H$ 不是 $(M,u)\mapsto M$：它记录商 $M/M_k$，所以 $q_H^*\mathcal L_E$ 拉回的是 $\operatorname{Tor}$ 上的 Laumon 层，而不是 $\operatorname{Bun}_k$ 上的对象。
- 消失是紧支撑 $\mathrm{R}\Gamma_c$ 的消失；换成 $\mathrm{R}\Gamma$ 就没有这个结论，推导中用到的是 $!$ 推前的性质。
- $H$ 带着 $M\in C_k$ 的开条件；不做 §7.1 的技术性加强，逐纤维计算时无法把这一条件去掉，$H$ 就不是仿射丛。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§7.1 洁净性中剩下的引理，p.40（PDF p.40），`源码/chapters/ch07.tex:4-7（$H$ 与 $q_H$ 的定义）、113-120（§7.5 收尾）`

## 核验

状态：`source-only`（2026-11-18）
- arXiv：https://arxiv.org/abs/math/0204081 — 摘要：「the vanishing of a certain functor Av_E^d ... implies the geometric Langlands conjecture. In this paper we establish the required vanishing result」——只支持卡中「由 Av_E^d 的消失定理得 0」这一步的输入存在，未给 d>rm(2g-2) 的定量界，也未涉及本卡的 H 叠与 q_H 归约。

## 关联

- `glc/concept/good-open-substack`
- `glc/concept/surjective-case-av`
- `glc/concept/affine-bundle-base-change`
- `glc/concept/laumon-factorization`
