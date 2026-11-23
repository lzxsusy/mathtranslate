# 重言丛 $\mathcal B,\mathcal N$ 与 $\mathfrak b^\circ,\mathfrak n^\circ,\mathfrak h^\circ$

> `mloc/concept/borel-and-nilpotent-radical-sheaves` · type=concept · track=B · status=draft · verification=source-only

**别名**：tautological bundle、$\mathfrak b^\circ$、$\mathfrak n^\circ$、$\mathfrak h^\circ$、Cartan 代数

## 摘要

$\mathfrak b^\circ,\mathfrak n^\circ$ 是 $\mathfrak g^\circ$ 的理想层；$\mathfrak h^\circ=\mathcal O_X\otimes\mathfrak h$。

## 问题

旗簇上 Borel 子代数随点变化，怎样把它写成层，$\mathfrak b^\circ$ 与 $\mathfrak n^\circ$ 为什么是理想层？

## 定义

设 $\mathfrak g$ 是复半单李代数，$G=\operatorname{Int}(\mathfrak g)$，$X$ 是 $\mathfrak g$ 的旗簇（全体 Borel 子代数构成的簇）。$G$ 作用在平凡丛 $X\times\mathfrak g$ 上，以 $\mathfrak b_x$ 为纤维的 $G$-齐次子丛 $\mathcal B$ 称重言向量丛；幂零根 $\mathfrak n_x$ 构成子丛 $\mathcal N$，$B_x$ 是 $x$ 在 $G$ 中的稳定化子。置 $\mathfrak g^\circ=\mathcal O_X\otimes_\mathbb C\mathfrak g$，括号为 $[f\otimes\xi,g\otimes\eta]=f\tau(\xi)g\otimes\eta-g\tau(\eta)f\otimes\xi+fg\otimes[\xi,\eta]$；$\mathfrak b^\circ,\mathfrak n^\circ$ 分别是 $\mathcal B,\mathcal N$ 的局部截面层，$\mathfrak h^\circ=\mathfrak b^\circ/\mathfrak n^\circ$。

记号：$\mathcal B$：重言丛；$\mathcal N$：幂零根丛；$H=\mathcal B/\mathcal N$；$\mathfrak b_x,\mathfrak n_x,\mathfrak h_x=\mathfrak b_x/\mathfrak n_x$；$\mathfrak h$：Cartan 代数；$\tau:\mathfrak g^\circ\to T_X$。

## 要点

- $\mathcal B$ 不是平凡丛：$X\times\mathfrak g$ 平凡，但 Borel 子代数随 $x$ 转动；$\mathcal B$ 是 $G$-齐次子丛，$\mathfrak b_x$ 是 $x$ 对应的 Borel 子代数。
- $\mathfrak h_x=\mathfrak b_x/\mathfrak n_x$ 上 $B_x$ 平凡作用（环面部分交换、幂幺部分 $\equiv1\bmod\mathfrak n_x$），故 $H=\mathcal B/\mathcal N$ 是平凡丛；其整体截面李代数 $\mathfrak h$ 称 $\mathfrak g$ 的 Cartan 代数，$\mathfrak h\cong\mathfrak b_x/\mathfrak n_x$ 与 $x$ 无关。
- $\ker(\tau:\mathfrak g^\circ\to T_X)=\mathfrak b^\circ$：$\tau(\xi)$ 在 $x$ 处为 $0$ 当且仅当 $\xi\in\mathfrak b_x$。
- 第 2 章引理 1.1：$\mathfrak b^\circ$ 是 $\mathfrak g^\circ$ 的理想层（$\tau$ 是李代数层同态），且 $\mathfrak b^\circ$ 上的括号 $\mathcal O_X$-线性；$\mathfrak n^\circ$ 也是理想层（用齐性求导）。
- $\mathfrak b^\circ$ 上括号的 $\mathcal O_X$-线性保证 $\mathfrak b^\circ U^\circ$、$\mathfrak n^\circ U^\circ$ 是双边理想，从而 $\mathcal D_X=U^\circ/\mathfrak b^\circ U^\circ$、$\mathcal D_\mathfrak h=U^\circ/\mathfrak n^\circ U^\circ$ 是环层。

## 公式

$$\mathfrak g^\circ=\mathcal O_X\otimes_\mathbb C\mathfrak g$$

$$[f\otimes\xi,g\otimes\eta]=f\tau(\xi)g\otimes\eta-g\tau(\eta)f\otimes\xi+fg\otimes[\xi,\eta]$$

$$\mathfrak b^\circ=\ker(\tau:\mathfrak g^\circ\to T_X)$$

$$\mathfrak h^\circ=\mathfrak b^\circ/\mathfrak n^\circ=\mathcal O_X\otimes_\mathbb C\mathfrak h$$

## 相关定理

### 第 2 章引理 1.1（$\mathfrak b^\circ$ 与 $\mathfrak n^\circ$ 是理想层）

(i) 层 $\mathfrak b^\circ$ 是 $\mathfrak g^\circ$ 中的理想层，且 $\mathfrak b^\circ$ 上的换位子是 $\mathcal O_X$-线性的。(ii) 层 $\mathfrak n^\circ$ 是 $\mathfrak g^\circ$ 中的理想层。

证明状态：`complete`

1. (i) 第一句由 $\mathfrak b^\circ=\ker\tau$ 得出：$\tau$ 是李代数层同态，故其核是理想层。
   - 为什么：李代数同态的核自动是理想：$[s,t]\in\ker$ 当 $\tau(t)=0$。
2. 对 $\sum_i f_i\otimes\xi_i\in\mathfrak b^\circ$、$g\otimes\eta\in\mathfrak g^\circ$ 展开括号，含 $\tau(\xi_i)g$ 的项消失，剩下 $g[\sum_i f_i\otimes\xi_i,1\otimes\eta]$——故括号 $\mathcal O_X$-线性。
   - 为什么：$\xi_i$ 的像在 $\mathfrak b^\circ$ 中即 $\tau(\xi_i)=0$；这正是「$\mathfrak b^\circ$ 中的元素在每点属于 $\mathfrak b_x$」的层化表述。
3. (ii) 对 $\sum_i f_i\otimes\xi_i\in\mathfrak n^\circ$ 与 $\eta\in\mathfrak g$，由齐性 $g(\sum_i f_i\otimes\xi_i)\in\mathfrak n^\circ$；对 $g$ 求导得 $\sum_i\tau(\eta)f_i\otimes\xi_i+\sum_i f_i\otimes[\eta,\xi_i]\in\mathfrak n^\circ$，而它等于 $[1\otimes\eta,\sum_i f_i\otimes\xi_i]$。
   - 为什么：$\mathfrak n^\circ$ 是 $G$-不变子层，$G$ 作用可微，导数仍落在其中（$\mathfrak n^\circ$ 在每点取值 $\mathfrak n_x$ 是闭条件）。
4. 故 $\mathfrak n^\circ$ 是理想层。
   - 为什么：第 3 步给出与 $1\otimes\eta$ 的括号落在 $\mathfrak n^\circ$，再由 $\mathcal O_X$-线性对任意 $g\otimes\eta$ 成立。

### 命题（$H$ 平凡、$\mathfrak h^\circ=\mathcal O_X\otimes\mathfrak h$）

$H=\mathcal B/\mathcal N$ 是 $X$ 上的平凡向量丛，其整体截面李代数 $\mathfrak h$ 与 $\mathfrak b_x/\mathfrak n_x$ 自然同构（对任意 $x$ 皆然），且 $\mathfrak h^\circ=\mathcal O_X\otimes_\mathbb C\mathfrak h$。

证明状态：`complete`

1. $B_x$ 在 $\mathfrak b_x/\mathfrak n_x$ 上作用平凡：环面部分 $T_x$ 交换，故伴随作用固定 Cartan 子代数 $\mathfrak c$ 逐点；幂幺部分 $N_x$ 的伴随作用是 $1+\mathfrak n_x$，模 $\mathfrak n_x$ 为恒等。
   - 为什么：$\mathfrak b_x=\mathfrak c\oplus\mathfrak n_x$，$[\mathfrak c,\mathfrak c]=0$，$[\mathfrak n_x,\mathfrak b_x]\subset\mathfrak n_x$；故 $\operatorname{Ad}$ 在商上平凡。
2. 于是 $H=G\times_{B_x}(\mathfrak b_x/\mathfrak n_x)$ 是纤维表示平凡的齐次丛，即 $H\cong X\times\mathfrak h$。
   - 为什么：齐次丛 $G\times_{B_x}V$ 在 $V$ 上作用平凡时同构于 $G/B_x\times V$。
3. 故 $\mathfrak h^\circ=\mathfrak b^\circ/\mathfrak n^\circ$ 是 $\mathfrak h$ 的常值层 $\mathcal O_X\otimes\mathfrak h$，且 $\mathfrak h$ 与 $x$ 无关。
   - 为什么：平凡丛的截面层就是常值层；$\mathfrak h^\circ$ 作为商层逐点取值为 $\mathfrak b_x/\mathfrak n_x\cong\mathfrak h$。

## 易错点

- $\mathcal B$ 是子丛而不是商丛：$\mathfrak b^\circ$ 是「取值落在 $\mathfrak b_x$ 中」的截面层，不是 $\mathfrak g^\circ$ 的商。
- $\mathfrak n^\circ$ 是 $\mathfrak b^\circ$ 的理想，但不是 $\mathcal O_X$-模的直和项意义上的「补」；$\mathfrak h^\circ=\mathfrak b^\circ/\mathfrak n^\circ$ 只是在商的意义下等于 $\mathcal O_X\otimes\mathfrak h$，局部截面需要选 Cartan 才能提升。
- $\mathfrak b^\circ=\ker\tau$ 的「核」是李代数层同态的核；不要把它与 $\mathcal O_X\to U^\circ$ 的核混淆，后者是零。
- 第 2 章引理 1.1 的 (i) 中「括号 $\mathcal O_X$-线性」只对 $\mathfrak b^\circ$ 的第一个变量成立（第二个变量上仍有 $\tau$ 项）；把整条括号说成 $\mathcal O_X$-双线性是错的。

## 相关卡

- `mloc/concept/homogeneous-twisted-sheaf`
- `mloc/concept/d-h-sheaf`
- `mloc/concept/d-lambda-sheaf`

## 出处

- Miličić, Localization and Representation Theory of Reductive Lie Groups · 第 2 章 §1 旗簇上的齐性扭层 · p.[17]（PDF [21]） · `源码/chapters/ch02a.tex:9-15（重言丛、$\mathfrak b^\circ,\mathfrak n^\circ$ 与括号）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · 第 2 章 §1 旗簇上的齐性扭层 · p.[17, 18]（PDF [21, 22]） · `源码/chapters/ch02a.tex:17-33（第 2 章引理 1.1 及证明）`
