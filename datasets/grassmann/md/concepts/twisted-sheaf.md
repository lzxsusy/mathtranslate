# 扭曲层

> `grassmann/concept/twisted-sheaf` · 轨道 6 · 曲线上层的算术 · 状态 draft

> **先自测**：为什么「μ_n 作用等于标量」这一条就能让 gerbe 上的层论与普通层论完全平行？

## 一句话

惯性 μ_n 作用等于标量的层：它等价于 gerbe 叠上的 O-模，因此形变理论照搬，Brauer 类由此变成可算的模空间。

## 定义

一个 **$\mathscr{X}$-扭曲层**（$\mathscr{X}$-twisted sheaf）是一个 $\mathcal{O}_{\mathscr{X}}$-模层 $\mathscr{F}$，使得（由惯性诱导的）自然左作用
$$\boldsymbol{\mu}_n\times\mathscr{F}\longrightarrow\mathscr{F}$$
等于标量乘法。

**可用来做计算的下降刻画**：设 $\pi: \mathscr{X}\to X$ 是 $\boldsymbol{\mu}_n$-gerbe，取 étale 覆盖 $U\to X$ 与 $\pi$ 在 $U$ 上的截面 $s$。则 $\mathscr{X}$-扭曲层等价于一对 $(\mathscr{F}_{U},\varphi)$，其中 $\mathscr{F}_{U}$ 是 $X$ 上的层、$\varphi: \mathrm{pr}_{1}^{*}\mathscr{F}_{U}\to\mathrm{pr}_{2}^{*}\mathscr{F}_{U}$ 是 $U\times_{X}U$ 上的同构，满足上闭链 $\varphi_{13}=\varphi_{23}\circ\varphi_{12}\in U\times_{X}U\times_{X}U$，并且 $\boldsymbol{\mu}_n$ 的作用（$\zeta$ 乘以 $\zeta$）与 $\varphi$ 相容。等价地，$\mathscr{X}$-扭曲层就是叠 $\mathscr{X}$ 的 étale 拓扑斯上的 $\mathcal{O}$-模，故形变理论（定理 A.2.1）可以逐字搬过来。

**记号约定**：$\pi: \mathscr{X}\to X$ 是 $\boldsymbol{\mu}_n$-gerbe；$\mathscr{F}$ 是 $\mathscr{X}$-扭曲层；$U\to X$ 是 étale 覆盖，$\varphi$ 是下降数据；$\mathrm{pr}_{i}$ 是 $U\times_{X}U\to U$ 的投影；可逆扭曲层指秩 $1$ 的扭曲层。

## 要点（为什么需要它）

- 三档等价：$\mathscr{X}$-扭曲层 $=$ 带 $\boldsymbol{\mu}_n$-带化下降数据的层 $=$ 叠 $\mathscr{X}$ 上的 $\mathcal{O}$-模。第三种说法让 Illusie 的形变理论直接可用，第一种说法给出可写的公式，第二种说法用于粘合。
- 可逆扭曲层给出次数：$L^{\otimes n}$ 带平凡惯性，故下降为 $X$ 上可逆层 $L'$，令 $\deg L=\frac{1}{n}\deg L'$。这正是「半整数次数」的来源，也是根叠上抛物权取 $\{0,\frac{1}{2}\}$ 的原因。
- 扭曲层是 Brauer 类的见证：存在可逆 $\mathscr{X}$-扭曲层当且仅当 $[\mathscr{X}]=0$（命题 B.3(1)）。所以「Brauer 类」可以被一组几何对象（扭曲层）完全刻画，而不只是上同调类。
- 模叠 $\mathscr{M}_{X/k}(n,L)$ 是 $k$ 上局部有限型的代数叠；当 $X$ 是光滑固有曲线、$[\mathscr{X}\otimes\bar{k}]=0$ 且 $(n,d)=1$ 时它拟固有。这几条是本章 §3、§5 反复引用的技术底座。
- 局部粘合（命题 A.2.3）：给定覆盖上的局部扭曲层，只要在重叠处给出同构并使其满足上闭链，就能粘成整体扭曲层——§5 把完备 DVR 上的局部模型粘成整体 $\mathscr{C}$-扭曲层正是靠它。

## 关键公式

$$
\boldsymbol{\mu}_n\times\mathscr{F}\to\mathscr{F}\quad\text{equals the scalar multiplication}
$$

$$
L^{\otimes n}\cong\pi^{*}L',\qquad \deg L=\frac{1}{n}\deg L'
$$

$$
\varphi_{13}=\varphi_{23}\circ\varphi_{12}\qquad\text{on }U\times_{X}U\times_{X}U
$$

$$
\exists\ \text{invertible }\mathscr{X}\text{-twisted sheaf}\iff[\mathscr{X}]=0
$$

## 定理与证明（或缺口）

### 命题 A.2.3（局部资料粘合成整体扭曲层）

设 $\pi: \mathscr{X}\to X$ 是 $\boldsymbol{\mu}_n$-gerbe，$\{U_{i}\to X\}$ 是 étale 覆盖，在每个 $\mathscr{X}_{U_{i}}$ 上给定扭曲层 $\mathscr{F}_{i}$，在重叠处给定同构 $\varphi_{ij}:\mathscr{F}_{i}|_{U_{ij}}\to\mathscr{F}_{j}|_{U_{ij}}$ 满足上闭链。则存在整体扭曲层 $\mathscr{F}$ 粘合这些资料。特别地，若 $\mathscr{C}\to\mathscr{P}$ 是曲线上的 gerbe，局部（在完备化上）构造的正则扭曲层可以粘成整体。

**证明状态：提纲（有缺口）**

1. 在每个 $\mathscr{X}_{U_{i}}$ 上取 $\mathscr{F}_{i}$ 与转移同构 $\varphi_{ij}$，把 $\mathscr{F}$ 定义为这些局部对象的「粘合」：在 $\mathscr{X}$ 的 étale 拓扑斯上取等化子（equalizer）。
   - *为什么*：层范畴是 étale 拓扑斯，等化子存在且给出唯一的整体 $\mathcal{O}$-模；关键是等化子在拟凝聚层范畴内封闭。
2. 验证粘合出的 $\mathscr{F}$ 满足扭曲条件：$\boldsymbol{\mu}_n$ 的作用在每块 $\mathscr{F}_{i}$ 上是标量，转移同构 $\varphi_{ij}$ 与作用相容，故整体作用仍是标量。
   - *为什么*：扭曲条件是局部条件，且在 $\mathcal{O}$-模同构下不变，故可逐块验证后下降。

> **缺口**：原文只给思路并引用 [19] 的粘合引理，未写出「等化子与 $\boldsymbol{\mu}_n$-等变结构相容」的细节；真正的技术难点是把局部 $\mathscr{E}nd(V)=A$ 的同构粘成整体 Azumaya 代数，需要 $\mathrm{Ext}^{1}$-扭子的语言（无自然基点）。


出处：ch6 附录 A 命题 A.2.3（中译 p. 114 / en PDF p. 124）

### 命题 B.3(1)（可逆扭曲层存在当且仅当类平凡）

设 $\mathscr{Z}\to Z$ 是 $\mathbf{G}_m$-gerbe。则存在可逆 $\mathscr{Z}$-扭曲层当且仅当 $[\mathscr{Z}]=0\in\mathrm{H}^{2}(Z,\mathbf{G}_m)$。

**证明状态：完整**

1. 若 $[\mathscr{Z}]=0$，则 $\mathscr{Z}\cong\mathsf{B}\mathbf{G}_m\times Z$ 有截面，$\mathcal{O}_{Z}$ 的拉回就是可逆 $\mathscr{Z}$-扭曲层。
   - *为什么*：平凡 gerbe 上的秩 $1$ 自由层惯性作用为标量，故是扭曲层。
2. 反之若存在可逆 $\mathscr{Z}$-扭曲层 $L$，则 $L$ 给出 $\mathscr{Z}\to Z$ 的一个截面（在每个点处 $L$ 局部自由秩 $1$，选取局部基即得平凡化），故 gerbe 有截面即平凡，$[\mathscr{Z}]=0$。
   - *为什么*：gerbe 的截面与「带化被杀死」是同一件事：有截面即 $\mathscr{Z}\cong\mathsf{B}\mathbf{G}_m\times Z$，其类为零。


出处：ch6 附录 B 命题 B.3(1)（中译 p. 115 / en PDF p. 125）

## 易错点

- 把扭曲层写成「带 $\boldsymbol{\mu}_n$-作用的层」而漏掉「作用等于标量」：差一个特征标就是 $\chi$-扭曲层，属于另一个 $\mathrm{H}^{2}$ 类，两者不能相加。
- 上闭链方向写反：本书是 $\varphi_{13}=\varphi_{23}\circ\varphi_{12}$；推广到非交换结构群时写反会得到不同的下降对象（$\boldsymbol{\mu}_n$ 交换时看不出来，所以更容易在推广时踩坑）。
- 以为 $\deg L$ 总是整数：它是 $\frac{1}{n}\deg L'$，在根叠上会出现半整数（批注 7）；用整数值的稳定性判据会把抛物权算错。
- 把「存在可逆扭曲层」当成「所有扭曲层都可逆」：秩 $>1$ 的扭曲层才是模空间的主要对象，它们的 $\det$ 又给出一层可逆扭曲层的账（批注 13，per | ind 的证明就用它）。

## 相关卡

- [μ_n-带化的 gerbe](../concepts/gerbe-banded-by-mu-n.md)
- [Faddeev 指标](../concepts/faddeev-index.md)
- [根叠](../concepts/root-stack.md)
- [凝聚系](../concepts/coherent-system.md)

## 出处

- ch6 附录 A 定义 A.2–命题 A.2.3；中译 p.112（英文 PDF p.122），源码 `chapters/ch06.tex:527`
