# 分歧正合列

> `grassmann/concept/ramification-sequence` · 轨道 6 · 曲线上层的算术 · 状态 draft

> **先自测**：为什么「一个 Brauer 类在一点分歧」这件事可以被编码成剩余域的一个循环扩张？

## 一句话

完备 DVR 上 Brauer 类的分歧正合列，把分歧类送到剩余域的循环扩张群 H¹(κ,Q/Z)，末端群可显式算。

## 定义

设 $R$ 是完备离散赋值环，$t$ 是一致化子，$K$ 与 $\kappa$ 分别是分式域与剩余域，$j: \operatorname{Spec}K\to\operatorname{Spec}R$。只考虑周期与 $\charop(\kappa)$ 互素的 Brauer 类，记 $\operatorname{Br}(K)'$ 为这些类组成的子群。除子理论给出 $\operatorname{Spec}R$ 上 étale 层的正合列
$$0\to\mathbf{G}_m\to j_{*}\mathbf{G}_m\to\mathbf{Z}_{(t)}\to0,$$
它诱导
$$\mathrm{H}^{2}(\operatorname{Spec}R,j_{*}\mathbf{G}_m)\to\mathrm{H}^{2}(\operatorname{Spec}R,\mathbf{Z}_{(t)})=\mathrm{H}^{2}(\kappa,\mathbf{Z})=\mathrm{H}^{1}(\kappa,\mathbf{Q}/\mathbf{Z});$$
再由 Leray 谱序列 $\mathrm{H}^{2}(\operatorname{Spec}R,j_{*}\mathbf{G}_m)'=\operatorname{Br}(K)'$，合起来得到**分歧正合列**
$$0\to\operatorname{Br}(R)'\to\operatorname{Br}(K)'\to\mathrm{H}^{1}(\kappa,\mathbf{Q}/\mathbf{Z}).$$
$\alpha$ 的**分歧**就是它在 $\mathrm{H}^{1}(\kappa,\mathbf{Q}/\mathbf{Z})$ 中的像；像为零当且仅当 $\alpha$ 延拓为 $R$ 上的 Azumaya 代数（非分歧）。

**可核对的显式公式**：若 $\kappa$ 含本原 $n$ 次单位根，则循环代数 $(a,b)$ 的分歧由
$$\kappa\Big(\sqrt[n]{(-1)^{v(a)v(b)}\,a^{v(b)}/b^{v(a)}}\Big)$$
给出；特别地，$(u,t)$（$u\in R^{\times}$，$\overline{u}$ 为 $u$ 在 $\kappa^{\times}$ 中的像）的分歧扩张是 $\kappa(\overline{u}^{1/n})$。

**记号约定**：$R$ 完备 DVR；$t$ 一致化子；$K=\operatorname{Frac}R$；$\kappa$ 剩余域；$v$ 赋值；$j: \operatorname{Spec}K\to\operatorname{Spec}R$；$\operatorname{Br}(K)'$ 表示周期与 $\charop\kappa$ 互素的类；$\mathrm{H}^{1}(\kappa,\mathbf{Q}/\mathbf{Z})$ 参数化 $\kappa$ 的循环扩张。

## 要点（为什么需要它）

- 正合列的来源是两步：除子理论的正合列 $0\to\mathbf{G}_m\to j_{*}\mathbf{G}_m\to\mathbf{Z}_{(t)}\to0$ 给出边界映射，Leray 谱序列把 $\mathrm{H}^{2}(\operatorname{Spec}R,j_{*}\mathbf{G}_m)'$ 识别为 $\operatorname{Br}(K)'$——关键在于「任意分歧类都有非分歧分裂域」。
- 末端群 $\mathrm{H}^{1}(\kappa,\mathbf{Q}/\mathbf{Z})=\operatorname{Hom}(\mathrm{Gal}(\bar{\kappa}/\kappa),\mathbf{Q}/\mathbf{Z})$ 参数化 $\kappa$ 的循环扩张：$\kappa$ 含 $\mu_{n}$ 时每个 $n$ 次循环扩张都由抽取某个 $\overline{u}$ 的 $n$ 次根得到，故分歧可以被「算」出来而不是抽象地存在。
- 「分歧 $=0$」当且仅当类落在 $\operatorname{Br}(R)'$ 的像里，即延拓为 $R$ 上的 Azumaya 代数；所以分歧正合列是把「局部可延拓性」写成一个群论条件。
- 命题 C.1 是这个正合列的两个直接用途：(1) 任何 $\alpha\in\operatorname{Br}(K)[n]$ 都等价于「$\operatorname{Br}(R)$ 中的元素 $+\,(u,t)$」，即分歧只由一个 $(u,t)$ 承担；(2) $\alpha$ 总能延拓到根叠 $\mathscr{R}_{n}$ 上，这就是「用叠分裂分歧」。
- 推论 C.2 把局部的延拓搬到整体曲线：$\alpha\in\operatorname{Br}(k(C))[n]$ 在 $p_{1},\dots,p_{r}$ 分歧时，$\alpha$ 延拓到 $p_{1}+\cdots+p_{r}$ 的 $n$ 次根叠 $\mathscr{C}\to C$ 上——这是 §4、§5 里「分歧塞进根叠」的根据。

## 关键公式

$$
0\to\operatorname{Br}(R)'\to\operatorname{Br}(K)'\xrightarrow{\ \partial\ }\mathrm{H}^{1}(\kappa,\mathbf{Q}/\mathbf{Z})
$$

$$
0\to\mathbf{G}_m\to j_{*}\mathbf{G}_m\to\mathbf{Z}_{(t)}\to0
$$

$$
\partial(a,b)=\kappa\Big(\sqrt[n]{(-1)^{v(a)v(b)}a^{v(b)}/b^{v(a)}}\Big)
$$

$$
\partial(u,t)=\kappa(\overline{u}^{1/n})\qquad(u\in R^{\times})
$$

## 定理与证明（或缺口）

### 命题 C.1（分歧类的标准化与根叠上的延拓）

假定 $\kappa$ 包含本原 $n$ 次单位根 $\zeta$，固定 $\alpha\in\operatorname{Br}(K)[n]$。则
(1) 存在 $u\in R^{*}$ 与 $\alpha'\in\operatorname{Br}(R)$，使得 $\alpha=\alpha'+(u,t)\in\operatorname{Br}(K)$；
(2) 存在 $\beta\in\operatorname{Br}(\mathscr{R}_{n})$，其在限制映射下的像为 $\alpha$，其中 $\mathscr{R}_{n}\to\operatorname{Spec}R$ 是 $\operatorname{Spec}R$ 闭点的 $n$ 次根叠。

**证明状态：完整**

1. 对 (1)：由分歧正合列的显式描述，可取 $u\in R^{*}$ 使 $(u,t)$ 与 $\alpha$ 有相同的分歧；两者相减落入分歧映射的核，即 $\operatorname{Br}(R)$。
   - *为什么*：分歧映射的核正是 $\operatorname{Br}(R)'$ 的像（正合性），而 $\mathrm{H}^{1}(\kappa,\mathbf{Q}/\mathbf{Z})$ 中每个元素都可由某个 $(u,t)$ 实现。
2. 对 (2)：由 (1) 只需对 $(u,t)$ 证明。回顾 $\mathscr{R}_{n}=[\operatorname{Spec}R[t^{1/n}]/\boldsymbol{\mu}_{n}]$；在 $(u,t)_{K(t^{1/n})}$ 中令 $\tilde{y}=y/t^{1/n}$，则 $\boldsymbol{\mu}_{n}$ 在 $t^{1/n}$ 上的自然作用给出一个 $\boldsymbol{\mu}_{n}$-等变 Azumaya 代数，它下降为 $\mathscr{R}_{n}$ 上的 Azumaya 代数，其类限制到 $K$ 即 $\alpha$。
   - *为什么*：$x^{n}=u$、$y^{n}=t$、$xy=\zeta yx$ 生成的 $(u,t)$ 在开 $n$ 次方后，$\tilde{y}$ 满足 $\tilde{y}^{n}=1$，$\boldsymbol{\mu}_{n}$ 的等变结构使代数在叠商上下得来；这正是「根叠铺平分歧」的机制。


出处：ch6 附录 C 命题 C.1（中译 p. 117 / en PDF p. 127）

### 推论 C.2（曲线上的分歧延拓到根叠）

设 $C$ 是域 $k$ 上的固有正则曲线，且对某个在 $k$ 中可逆的 $n$，$k$ 包含本原 $n$ 次单位根。设 $\alpha\in\operatorname{Br}(k(C))[n]$ 在 $p_{1},\dots,p_{r}$ 处分歧，$\mathscr{C}\to C$ 是 $p_{1}+\cdots+p_{r}$ 的 $n$ 次根叠。则存在 $\alpha'\in\operatorname{Br}(\mathscr{C})[n]$，它在一般点上的限制为 $\alpha$。

**证明状态：提纲（有缺口）**

1. 取 $k(C)$ 上 Brauer 类为 $\alpha$ 的中心单代数 $A$，在某个开子叠 $U\subset\mathscr{C}$ 上找到一般类为 $\alpha$ 的 Azumaya 代数 $B$。
   - *为什么*：$\alpha$ 只可能在有限个点分歧，去掉这些点后 $A$ 是 Azumaya 的，故可在 $U$ 上取 $B$。
2. 对每个闭点 $q\in C\setminus U$，取 $m$ 使 $\widehat{\mathscr{C}}_{q}$ 上存在 Azumaya 代数 $B'$，其限制同构于 $M_{m}(B)_{\widehat{\eta}}$，再与 $M_{m}(B)$ 粘合，把 $U$ 扩到 $U\cup\{q\}$。
   - *为什么*：局部存在性来自命题 C.1（在完备化上用根叠铺平），粘合则用命题 A.2.3 的论证与 [22]。

> **缺口**：原文给出上述两步，但把「$\widehat{\mathscr{C}}_{q}$ 上的 Azumaya 代数与 $M_{m}(B)$ 粘合」的细节推给命题 A.2.3 的证明与文献 [22]；$m$ 的一致性（要在有限多个 $q$ 上同时取到同一个 $m$）也需要额外一句说明。故记为 sketch。


出处：ch6 附录 C 推论 C.2（中译 p. 117 / en PDF p. 127）

### 命题 C.4（分歧与相对 Picard 叠的扭子）

设 $\pi: \mathscr{X}\to X$ 是 $\boldsymbol{\mu}_{n}$-gerbe，$\mathscr{Y}\to X$ 是另一个 $\boldsymbol{\mu}_{n}$-gerbe。则相对 Picard 叠 ${}_{\tau}\mathscr{P}ic_{\mathscr{Y}/\mathscr{X}}$ 是 $\mathbf{Z}/n$-扭子 $T$ 上的 $\mathbf{G}_m$-gerbe，并且 $\mathscr{Y}$ 的 Brauer 类是 $\mathscr{X}$ 上某个类的拉回，当且仅当 $T$ 平凡。

**证明状态：只引出处，原书不重证**


> 原文只陈述结论并以之说明「经典分歧扩张与模空间给出的循环扩张同构」（末段），完整证明未展开，故按 reference 记。


出处：ch6 附录 C 命题 C.4（中译 p. 117 / en PDF p. 127）

## 易错点

- 撇号 $'$ 的含义：$\operatorname{Br}(R)'$、$\operatorname{Br}(K)'$ 是「阶与 $\charop(\kappa)$ 互素」的子群，不是「非分歧」；把 $\operatorname{Br}(R)'$ 读成全体 $\operatorname{Br}(R)$ 会让正合列在正特征下失效。
- 分歧公式的指数顺序：是 $(-1)^{v(a)v(b)}a^{v(b)}/b^{v(a)}$，不是 $a^{v(a)}/b^{v(b)}$；写反后 $(u,t)$ 的分歧会算成 $\kappa(\overline{u}^{1/n})$ 之外的东西。
- 原文在命题 C.1 证明里把 $(u,t)_{K(t^{1/n})}$ 印成 $(u,t)_{K(t^{1/u})}$（译注 12 已改）：这不是笔误无害，$t^{1/u}$ 根本不是域扩张。
- 把「非分歧」当成「平凡」：非分歧类可以是 $\operatorname{Br}(R)$ 中非零的元素（例如常数代数），分歧正合列只判断能否延拓，不判断是否为 $0$。

## 相关卡

- [根叠](../concepts/root-stack.md)
- [周期与指标](../concepts/period-and-index.md)
- [扭曲层](../concepts/twisted-sheaf.md)
- [凝聚系](../concepts/coherent-system.md)

## 出处

- ch6 附录 C 分歧正合列–命题 C.4；中译 p.116（英文 PDF p.126），源码 `chapters/ch06.tex:673`
