# Hecke 修正与 Hecke 型

> `grassmann/concept/hecke-modification` · 轨道 5 · BD Grassmannian 与辛纽结同调 · 状态 draft

> **先自测**：Hecke 型凭什么与局部坐标、局部平凡化的选取无关，从而可以在曲线上逐点谈论？

## 一句话

在一点处换掉主丛、在点外保持同构的初等变换叫 Hecke 修正；型的记录使这种变换离散化，并给出仿射格拉斯曼流形的分层。

## 定义

设 $X$ 是光滑曲线、$x\in X$。对含 $x$ 的开集 $U$，定义 $$\Gr_{U,x}:=\bigl\{(P,\phi):\ P\text{ 是 }U\text{ 上的主 }G^\vee\text{-丛},\ \phi:P_0|_{U\setminus x}\to P|_{U\setminus x}\text{ 是同构}\bigr\},$$ 其中 $P_0$ 是平凡丛。取 $x$ 处局部坐标得同构 $\Gr_{U,x}\cong\Gr$（模去 $\Aut(\mathcal{O})$ 的作用后唯一），把 $\Gr^\lambda$ 的原像记为 $\Gr_{U,x}^\lambda$，并称其中元素 $(P,\phi)$ 在 $x$ 处具有 **Hecke 型** $\lambda$。更一般地，若 $P_1,P_2$ 是 $X$ 上的主 $G^\vee$-丛、$\phi:P_1|_{X\setminus x}\to P_2|_{X\setminus x}$ 是同构，选取 $P_1$ 在 $x$ 附近的平凡化后 $\phi$ 给出 $\Gr_{U,x}$ 中一点，若该点型为 $\lambda$，就称 $\phi$ 在 $x$ 处具有 Hecke 型 $\lambda$。

**记号约定**：$\mathcal{K}=\mathbb{C}((t))$、$\mathcal{O}=\mathbb{C}[[t]]$；$\Gr=G^\vee(\mathcal{K})/G^\vee(\mathcal{O})$；$\Gr^\lambda$ 是经过 $t^\lambda$ 的轨道；$\Gr^\lambda_{U,x}$ 称 Hecke 型的轨迹（stratum）。

## 要点（为什么需要它）

- Hecke 修正是「在一点换丛」的初等变换；型 $\lambda$ 记录换了多少，它是离散数据，因此 $\Gr$ 被拆成可数的分层。
- 单点版 $(P,\phi)\in\Gr_{U,x}$ 与双丛版 $(P_1,P_2,\phi)$ 都有型，两种用法在 §2 交替出现，不能只认一种。
- $\mathbb{P}^1$ 上型 $\le\lambda$ 另有可计算的判据（命题 2.2）：每个相伴向量丛被夹在 $V_\beta^{P_1}(-\langle\beta,\lambda\rangle x)$ 与 $V_\beta^{P_1}(\langle\beta,\lambda\rangle x)$ 之间，且拓扑类型相差 $[\lambda]\in\pi_1(G^\vee)=\Lambda/Q$。
- $G^\vee$ 单连通时命题 2.2 的第二个条件自动成立，于是型完全由向量丛的夹逼关系决定。

## 关键公式

$$
\Gr_{U,x}:=\bigl\{(P,\phi):\ \phi:P_0|_{U\setminus x}\to P|_{U\setminus x}\text{ 是同构}\bigr\}\cong\Gr
$$

$$
V_\beta^{P_1}(-\langle\beta,\lambda\rangle x)\subset V_\beta^{P_2}\subset V_\beta^{P_1}(\langle\beta,\lambda\rangle x)
$$

$$
[P_2]-[P_1]=[\lambda]\in\pi_1(G^\vee)=\Lambda/Q
$$

## 定理与证明（或缺口）

### Hecke 型的良定义性

如上定义的 Hecke 型与 $P_1$ 在 $U$ 上的平凡化选取、以及开邻域 $U$ 的选取都无关，因此「$\phi$ 在 $x$ 处的 Hecke 型」是良定义的。

**证明状态：完整**

1. 换 $P_1$ 在 $U$ 上的平凡化：新得到的点 $L\in\Gr_{U,x}$ 只差 $G^\vee(U)$ 的作用，而 $G^\vee(U)$ 保持按 Hecke 型的分层，故 $L$ 所在的轨迹 $\Gr^\lambda_{U,x}$ 不变。
   - *为什么*：$G^\vee(U)$ 作用在 $\Gr_{U,x}$ 上并把 $\Gr^\lambda_{U,x}$ 送到自身（正文 108 行末句），所以型不变。
2. 缩小开邻域 $U$：两个局部坐标之间的过渡只差 $\Aut(\mathcal{O})$ 的作用，而 $\Gr^\lambda$ 是 $\Aut(\mathcal{O})$-不变的，故原像轨迹不变。
   - *为什么*：局部坐标给出的同构只在模 $\Aut(\mathcal{O})$ 的意义下唯一，而 $\Gr^\lambda$ 对该群不变，所以轨迹 $\Gr^\lambda_{U,x}$ 与坐标选取无关。


出处：中译 p.85（§2.2，108–112 行的论证）

### 命题 2.2（$\mathbb{P}^1$ 上 Hecke 型的判据，Finkelberg–Mirković）

设 $X=\mathbb{P}^1$。$\phi$ 在 $x$ 处具有 Hecke 型 $\le\lambda$ 当且仅当 (i) 对 $G^\vee$ 的所有不可约表示 $V_\beta$ 有 $V_\beta^{P_1}(-\langle\beta,\lambda\rangle x)\subset V_\beta^{P_2}\subset V_\beta^{P_1}(\langle\beta,\lambda\rangle x)$，且 (ii) $P_2$ 与 $P_1$ 的拓扑类型相差 $[\lambda]\in\pi_1(G^\vee)=\Lambda/Q$。

**证明状态：只引出处，原书不重证**


出处：中译 p.85（§2.2 命题 2.2，引 [FM] 命题 10.2）

## 易错点

- 容易把「该同构在 $\Aut(\mathcal{O})$ 对 $\Gr$ 的作用意义下是良定义的」读成「这个作用是良定义的」：原意是同构只有模去该作用后才唯一（英文 well defined up to），中译 p.85 丢了 up to，按字面读会接不上下一句「由于 $\Gr^\lambda$ 是 $\Aut(\mathcal{O})$-不变的」。
- 容易以为 Hecke 型只对丛对 $(P_1,P_2)$ 才有定义：单个 $(P,\phi)\in\Gr_{U,x}$ 的型是更基本的概念，丛对版是借局部平凡化归到它。

## 相关卡

- [局部卷积格拉斯曼流形](../concepts/local-convolution-grassmannian.md)
- [整体奇异格拉斯曼流形](../concepts/global-singular-grassmannian.md)
- [仿射格拉斯曼流形](../concepts/affine-grassmannian.md)
- [抛物丛与抛物次数](../concepts/parabolic-bundle.md)

## 出处

- ch5 §2.2 Hecke 型的概念；中译 p.85（英文 PDF p.94），源码 `chapters/ch05.tex:108`
