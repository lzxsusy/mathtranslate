# 抛物丛与抛物次数

> `grassmann/concept/parabolic-bundle` · 轨道 6 · 曲线上层的算术 · 状态 draft

> **先自测**：抛物次数为什么要把 deg W 与各点的秩跳分开加权，直接取 deg W 会丢掉什么？

## 一句话

在 P¹ 上给每个抛物点配一个权在 {0,1/2} 的子丛过滤，抛物次数把底层次数与各点秩跳按权加权；它等于根叠上对应层的次数。

## 定义

设 $D=p_1+\dots+p_r\subset\mathbf{P}^1$ 是约化除子，$\pi: \mathscr{P}\to\mathbf{P}^1$ 是对 $D$ 各点取平方根得到的根叠，它有 $r$ 个非平凡剩余 gerbe $\xi_1,\dots,\xi_r$，每个在 $p_i$ 的剩余域上同构于 $\mathsf{B}\boldsymbol{\mu}_2$。$\mathscr{P}$ 上的局部自由层 $V$ 称**正则的**，如果每个限制 $V|_{\xi_i}$ 的相伴表示都是正则表示的若干拷贝的直和。设 $\{a_i\le b_i\}_{i=1}^r\subset\{0,\tfrac12\}$。秩为 $2$、抛物权为 $\{a_i\le b_i\}$ 的**抛物丛**是一对 $V_*=(W,F)$，其中 $W$ 是秩 $2$ 的局部自由层，$F\subset W_D$ 是子丛。$V_*$ 的**抛物次数**为
$$\mathrm{pardeg}(V_*)=\deg W+\sum_i a_i\big(\operatorname{rk}W-\operatorname{rk}F_{p_i}\big)+b_i\operatorname{rk}F_{p_i}.$$
给定 $\mathscr{P}$ 上非零局部自由层 $V$，其**斜率**为 $\mu(V)=\deg V/\operatorname{rk}V$；若对所有局部分裂的真子层 $W\subset V$ 有 $\mu(W)<\mu(V)$，称 $V$ **稳定**。

**记号约定**：$W$ 秩 2；$F_{p_i}$ 是 $F$ 在 $p_i$ 的纤维（$W_D$ 的子空间）；$a_i\le b_i$ 取在 $\{0,\frac12\}$ 中，$a_i$ 配「商」$b_i$ 配「子」；$\deg_{\mathscr{P}}$ 归一到 $\mathbf{P}^1$：$\deg_{\mathscr{P}}L=\frac12\deg_{\mathbf{P}^1}\mathscr{M}$，$L^{\otimes2}\cong\pi^*\mathscr{M}$。

## 要点（为什么需要它）

- 权只取 $\{0,\tfrac12\}$ 是本章的特例：$a_i$ 乘「被商掉的秩」$\operatorname{rk}W-\operatorname{rk}F_{p_i}$，$b_i$ 乘「保留的秩」$\operatorname{rk}F_{p_i}$，于是 $a_i=b_i$ 时退化回 $\deg W$。
- 根叠上的次数是分数：$\deg\mathcal{O}(\xi_i)=[\kappa_i:k]/2$，$\kappa_i$ 是 $p_i$ 的剩余域；这解释了为什么抛物次数要带 $1/2$ 的权。
- 命题 4.3 给出范畴等价：$\mathscr{P}$ 上的局部自由层 $\leftrightarrow$ $\mathbf{P}^1$ 上以 $D$ 为抛物除子、权在 $\{0,\frac12\}$ 的抛物层，且 $\deg_{\mathscr{P}}V=\mathrm{pardeg}(V_*)$——所以抛物次数不是人为定义，是根叠上的次数。
- 稳定性的检验对象是「局部分裂的」真子层：不局部分裂的子层会带 gerbe 上的扭结，直接比斜率不合法。

## 关键公式

$$
\mathrm{pardeg}(V_*)=\deg W+\sum_i a_i(\operatorname{rk}W-\operatorname{rk}F_{p_i})+b_i\operatorname{rk}F_{p_i}
$$

$$
\deg_{\mathscr{P}}V=\mathrm{pardeg}(V_*),\qquad \deg\mathcal{O}(\xi_i)=[\kappa_i:k]/2
$$

$$
\mu(V)=\frac{\deg V}{\operatorname{rk}V}
$$

## 定理与证明（或缺口）

### 根叠上的层与抛物层的范畴等价（命题 4.3）

$\mathscr{P}$ 上的局部自由层 $V$ 与 $\mathbf{P}^1$ 上以 $D$ 为抛物除子、权含于 $\{0,\tfrac12\}$ 的抛物层 $V_*$ 之间存在范畴等价，且 $\deg_{\mathscr{P}}V=\mathrm{pardeg}(V_*)$。

**证明状态：提纲（有缺口）**

1. 取 $W=\pi_*V$ 作为底层层；由包含 $V(-\sum_i\xi_i)\subset V$ 前推得子层 $W'\subset W$，令 $F$ 为 $W'_D\to W_D$ 的像。
   - *为什么*：$\pi$ 是有限平坦态射，前推保持局部自由；$\mathcal{O}(-\xi_i)$ 的截面在 $\xi_i$ 处消失一阶，正好给出 $p_i$ 处的过滤。

> **缺口**：正文把「这定义范畴等价」与「保持次数」两件事都留给读者作练习（L351），没有写出逆构造与 $\deg_{\mathscr{P}}V=\mathrm{pardeg}(V_*)$ 的逐项核对，故只能记成 sketch。


出处：中译 p.106（§4 命题 4.3）

## 易错点

- 把抛物次数写成 $\deg W+\sum_i(a_i+b_i)\operatorname{rk}F_{p_i}$：$a_i$ 乘的是被商掉的秩 $\operatorname{rk}W-\operatorname{rk}F_{p_i}$，符号一错，$a_i=b_i=\frac12$ 时就不再等于 $\deg W$。
- 把 $F\subset W_D$ 当成 $W$ 的子丛：$F$ 只在 $D$ 上定义（$W_D=W\otimes\mathcal{O}_D$），写成 $F\subset W$ 会以为抛物结构是整条曲线上的过滤。
- 把「秩为 $N$」照抄定义 4.2：原书此处印作 $N$，结合后文「$W$ 是秩为 $2$ 的局部自由层」及本节主题应为秩 2（译注已指出），按 $N$ 算 $\mathrm{pardeg}$ 的归一化会全错。

## 相关卡

- [根叠](../concepts/root-stack.md)
- [分歧正合列](../concepts/ramification-sequence.md)
- [凝聚系](../concepts/coherent-system.md)

## 出处

- ch6 §4 定义 4.1–4.4 与命题 4.3；中译 p.106（英文 PDF p.116），源码 `chapters/ch06.tex:330`
