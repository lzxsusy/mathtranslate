# Hilbert 紧化与 Hilbert 稳定性

> `grassmann/concept/hilbert-compactification` · 轨道 9 · 可约曲线上的向量丛 · 状态 draft

> **先自测**：为什么把「曲线 + 其上的向量丛」一起放进 Hilbert 概形，比只紧化向量丛更适合处理退化？

## 一句话

把稳定丛变成曲线在 Grassmann 流形中的嵌入点，取 Hilbert 概形的分支闭包再作 GIT 商；曲线不再固定，恰是退化所需。

## 定义

设 $C$ 光滑射影曲线，$E$ 是秩 $r$、次数 $d$ 的稳定丛。取 $d$ 充分大（用 $U(r,d)\cong U(r,d+kr)$，$E\mapsto E\otimes\mathscr{O}(kp)$），则 $E$ 整体生成，求值映射给出
$$\varphi:E\longrightarrow H^{0}(C,E),\qquad C\longrightarrow\operatorname{Gr}\bigl(H^{0}(C,E),\,r\bigr).$$
**Hilbert 紧化**的构造是：
(i) 取 $\operatorname{Gr}(H^{0}(E),r)$ 中具有适当 Hilbert 多项式 $P$ 的曲线的 Hilbert 概形 $\operatorname{Hilb}^{P}$；
(ii) 取对应"给定结点曲线浸入"的点所在连通分支的闭包；
(iii) 万有丛限制回曲线给出曲线上的向量丛，再对 $\operatorname{PGL}(H^{0}(E))$ 的作用取 Hilbert 稳定点之商，得到紧化 $\overline{M}^{H}(r,d)$。
**Hilbert 稳定性**即该 Hilbert 点在 $\operatorname{PGL}$ 线性化下的 GIT 稳定性（Hilbert–Mumford 判据）。

**记号约定**：$d$ 充分大的次数；$\varphi$ 由整体生成给出的嵌入；$\operatorname{Gr}(V,r)$ 格拉斯曼流形；$\operatorname{Hilb}^{P}$ 具 Hilbert 多项式 $P$ 的 Hilbert 概形；$\overline{M}^{H}(r,d)$ Hilbert 紧化；$\operatorname{PGL}(H^{0}(E))$ 线性群。

## 要点（为什么需要它）

- **三步构造**：$d$ 充分大 $\Rightarrow$ 整体生成 $\Rightarrow$ 嵌入 $\operatorname{Gr}(H^{0}(E),r)$；取 Hilbert 概形的分支闭包；万有丛拉回 + GIT 商。
- **优点**：每个点都对应某条曲线上的向量丛（万有丛的限制），不需要引入无挠层；**缺点**：曲线不再固定，中心纤维可以在原结点之间插入有理分支。
- **这个"缺点"正是特性**：§4 的极限线性系正是把中心纤维换成带额外有理分支的曲线，因此 Hilbert 紧化天然容纳退化。
- **与斜率稳定的关系**：光滑曲线上 Hilbert 稳定 $\iff$ 斜率稳定（Gieseker–Morrison 秩 $2$；一般秩由 Teixidor 证一个方向、Schmitt 证等价）；可约曲线上本章只断言"蕴含"，即 Hilbert 稳定 $\Rightarrow$ $(∗)$ 型次数分布条件与命题 2.2 型界。
- **有理分支的必要条件**：Hilbert 稳定曲线上的有理分支必须至少有两个结点，且向量丛在其上的限制形如 $\mathscr{O}^{\oplus j}\oplus\mathscr{O}(1)^{\oplus r-j}$（平衡分裂）。

## 关键公式

$$
U(r,d)\cong U(r,d+kr),\qquad \varphi:E\longrightarrow H^{0}(C,E),\qquad C\longrightarrow\operatorname{Gr}\bigl(H^{0}(C,E),r\bigr)
$$

$$
\overline{M}^{H}(r,d)=\operatorname{Hilb}^{P}\bigl(\operatorname{Gr}(V,r)\bigr)^{\mathrm{ss}}\Big/\!\!\operatorname{PGL}(V),\qquad V=H^{0}(C,E)
$$

$$
E|_{\mathbf{P}^{1}}\cong\mathscr{O}^{\oplus j}\oplus\mathscr{O}(1)^{\oplus r-j}
$$

## 定理与证明（或缺口）

### 定理（光滑曲线上 Hilbert 稳定 $\iff$ 斜率稳定）

设 $C$ 光滑射影曲线，$E$ 秩 $r$、次数 $d$ 充分大。则 $E$ 是 Hilbert 稳定的当且仅当 $E$ 是斜率稳定的。秩 $2$ 情形由 Gieseker–Morrison 证明，一般秩的等价由 Schmitt 证明。

**证明状态：只引出处，原书不重证**


> 本章（§3）只引文献：[GM]（秩 $2$）、[T4]（另一证明）、[T5]（一个方向）、[Sc1]（一般秩等价），未给证明。


出处：ch9 §3 Hilbert 稳定性与斜率稳定性（中译 p. 163 / en PDF p. 182）

### 命题（可约曲线上的必要条件）

设 $C$ 是结点曲线、$E$ 是 Hilbert 稳定的向量丛。则 (1) 各分支上的次数分布满足与命题 2.1 证明中 $(∗)$ 相同的条件（即与典范权下的斜率稳定性相容）；(2) 各分支上的限制不可能过于不稳定，命题 2.2 型的界成立。

**证明状态：提纲（有缺口）**

1. Hilbert 稳定性用典范权 $w_i=d_i/(2g-2)$（$d_i=\deg K_C|_{C_i}$）作对照，故多重次数必须落在 $(∗)$ 的区间内。
   - *为什么*：GIT 权计算把"分支上的次数"与"典范权"比较；偏离区间会给出负权，从而不稳定。
2. 对各分支的限制，把命题 2.2 的测试层（在一侧为零、在另一侧取线子丛截面）搬到 Hilbert 稳定的情形，仍得到 $\chi$ 的夹逼，故界成立。
   - *为什么*：测试层的 $\chi$ 记账只依赖层的构造与结点的消没条件，与"斜率稳定"还是"Hilbert 稳定"无关。

> **缺口**：原文只说「类似于命题 2.1 证明中 $(∗)$ 的条件得以满足」以及「类似地……条件也得以满足」，未给证明；完整证明在 Gieseker [G2a] 与 Schmitt [Sc2]（批注 6）。此为必要条件，不是充分条件。


出处：ch9 §3 可约曲线上的 Hilbert 稳定性（中译 p. 163 / en PDF p. 182）

## 易错点

- 以为 Hilbert 紧化固定曲线：它恰好不固定，中心纤维可以在结点间插入有理分支；把曲线当成参数的一部分才是正确读法。
- 以为两个紧化在可约曲线上等价：等价性只在光滑曲线上有定理；可约曲线上本章只给"蕴含"，反方向需要额外条件。
- 忘了先取 $d$ 充分大：不整体生成就没有到 $\operatorname{Gr}(H^{0}(E),r)$ 的映射，构造无法启动；用 $U(r,d)\cong U(r,d+kr)$ 把 $d$ 推大是第一步。
- 把有理分支的分裂型 $\mathscr{O}^{\oplus j}\oplus\mathscr{O}(1)^{\oplus r-j}$ 当成对所有分支都成立：它只对 Hilbert 稳定曲线上的有理分支（且至少两个结点）成立。

## 相关卡

- [高秩极限线性系](../concepts/limit-linear-series-higher-rank.md)
- [斜率稳定无挠层与深度 1](../concepts/slope-stable-torsion-free-sheaf.md)
- [可约曲线上的 Brill–Noether 簇](../concepts/brill-noether-locus-on-reducible-curves.md)
- [凝聚系](../concepts/coherent-system.md)

## 出处

- ch9 §3 Hilbert 紧化与 Hilbert 稳定性；中译 p.163（英文 PDF p.182），源码 `chapters/ch09.tex:113`
