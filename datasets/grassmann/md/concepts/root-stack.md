# 根叠

> `grassmann/concept/root-stack` · 轨道 6 · 曲线上层的算术 · 状态 draft

> **先自测**：为什么给一条除子「开 n 次方」这件事需要一个叠，而不能在概形范畴里完成？

## 一句话

沿除子取 n 次根得到的叠：在除子外是同构，在除子上留下 Bμ_n 剩余 gerbe，从而把分歧「铺平」。

## 定义

设 $R$ 是完备离散赋值环，$t$ 为一致化子，$\kappa$ 含本原 $n$ 次单位根。$\operatorname{Spec}R$ 闭点的 **$n$ 次根叠** 为
$$\mathscr{R}_{n}=[\operatorname{Spec}R[t^{1/n}]/\boldsymbol{\mu}_{n}],$$
其中 $\boldsymbol{\mu}_{n}$ 通过 $t^{1/n}\mapsto\zeta\,t^{1/n}$（$\zeta\in\boldsymbol{\mu}_{n}$）作用。一般地，对概形 $X$ 与其简单正规交叉除子 $D=\sum D_{i}$，**沿 $D$ 的 $n$ 次根叠** 是一个叠 $\pi: \mathscr{X}\to X$，满足：
(1) $\pi$ 在 $X\setminus D$ 上是同构；
(2) 在每个 $D_{i}$ 上方留下剩余 gerbe $\xi_{i}\cong\mathsf{B}\boldsymbol{\mu}_{n}$（模去分歧域 $\kappa_{i}$）；
(3) $\operatorname{Pic}(\mathscr{X})$ 比 $\operatorname{Pic}(X)$ 多出由 $\mathscr{O}(\xi_{i})$ 生成的自由部分，且
$$\mathscr{O}(\xi_{i})^{\otimes n}\cong\pi^{*}\mathscr{O}(D_{i}).$$
叠上的次数按特设定义算：若 $L$ 是 $\mathscr{X}$ 上可逆层且 $L^{\otimes n}\cong\pi^{*}M$，则 $\deg L=\frac{1}{n}\deg M$。

**记号约定**：$R$ 完备 DVR，$t$ 一致化子；$\mathscr{R}_{n}\to\operatorname{Spec}R$ 是闭点的 $n$ 次根叠；$D=\sum D_{i}$ 是 snc 除子；$\xi_{i}$ 是 $D_{i}$ 上方的剩余 gerbe；$\mathscr{O}(\xi_{i})$ 是相应可逆层；$\deg$ 为 $\mathbf{Q}$-值（可半整数）。

## 要点（为什么需要它）

- 根叠的唯一用途是「铺平分歧」：$t$ 在 $\mathscr{R}_{n}$ 上被开了 $n$ 次方（$t=(t^{1/n})^{n}$），于是任何 $\alpha\in\operatorname{Br}(K)[n]$ 都能延拓到 $\operatorname{Br}(\mathscr{R}_{n})$（命题 C.1(2)）——分歧在根叠上消失。
- 局部看它只改一个点：$\mathscr{R}_{n}\to\operatorname{Spec}R$ 在闭点之外是同构，闭点上方是一个 $\mathsf{B}\boldsymbol{\mu}_{n}$；所以根叠是「只在一个除子上加了一层惯性」的最小改动。
- 抛物丛版本（§4）：$\mathscr{P}\to\mathbf{P}^{1}$ 是在 $D=p_{1}+\cdots+p_{r}$ 上取平方根的叠，剩余 gerbe $\xi_{i}\cong\mathsf{B}\boldsymbol{\mu}_{2}$，且
$$\deg_{\mathscr{P}}\mathscr{O}(\xi_{i})=\frac{1}{2}\deg_{\mathbf{P}^{1}}\mathscr{O}(p_{i})=\frac{1}{2}[\kappa_{i}:k].$$
半整数不是笔误（批注 7）：这正是抛物权取 $\{0,\frac{1}{2}\}$ 而不是整数的原因。
- $\operatorname{Pic}$ 的记账：$\mathscr{O}(\xi_{i})^{\otimes n}\cong\pi^{*}\mathscr{O}(D_{i})$ 说明根叠上的可逆层不是「新造的」，而是 $D_{i}$ 的 $n$ 次根；这也解释了为什么 $\deg$ 要除以 $n$。
- 形式层面的用处（§5）：命题 5.1.3 说 $M^{*}_{\mathscr{C}/k}\otimes\overline{k}\cong M^{*}_{\mathscr{P}/k}$——扭曲层的模空间在 $\overline{k}$ 上就是抛物模空间，于是「分歧类的模空间」被识别成「抛物模空间」，可以用抛物丛的稳定性理论来算。

## 关键公式

$$
\mathscr{R}_{n}=[\operatorname{Spec}R[t^{1/n}]/\boldsymbol{\mu}_{n}],\qquad t^{1/n}\mapsto\zeta\,t^{1/n}
$$

$$
\mathscr{O}(\xi_{i})^{\otimes n}\cong\pi^{*}\mathscr{O}(D_{i})
$$

$$
\deg_{\mathscr{P}}\mathscr{O}(\xi_{i})=\frac{1}{2}\deg_{\mathbf{P}^{1}}\mathscr{O}(p_{i})=\frac{1}{2}[\kappa_{i}:k]
$$

$$
M^{*}_{\mathscr{C}/k}\otimes\overline{k}\cong M^{*}_{\mathscr{P}/k}
$$

## 定理与证明（或缺口）

### 命题 5.1.3（扭曲模空间在闭包上就是抛物模空间）

设 $C\to\operatorname{Spec}k$ 是光滑固有曲线，$\alpha\in\operatorname{Br}(C)$ 的 $n$ 次类，$\mathscr{C}\to C$ 为 $\boldsymbol{\mu}_{n}$-gerbe，$D=\sum D_{i}$ 是 $\alpha$ 的分歧除子。若 $\mathscr{P}\to C$ 是沿 $D$ 的 $n$ 次根叠，则存在同构
$$M^{*}_{\mathscr{C}/k}(n,L)\otimes\overline{k}\cong M^{*}_{\mathscr{P}/k}(n,L).$$

**证明状态：提纲（有缺口）**

1. 在 $\overline{k}$ 上分歧类被杀死：$\alpha$ 在 $\mathscr{P}\otimes\overline{k}$ 上延拓为 $\operatorname{Br}(\mathscr{P}\otimes\overline{k})$ 中的类（命题 C.1 的整体版本，推论 C.2），而这个类在 $\overline{k}$ 上是可裂的。
   - *为什么*：根叠 $\mathscr{P}$ 的构造正是为了让分歧可以延拓；基域代数闭时所有 Brauer 类都可裂。
2. 于是 $\mathscr{C}\otimes\overline{k}$ 与 $\mathscr{P}\otimes\overline{k}$ 只差一个可逆扭曲层（乘以它即把两者互变），模空间因此同构。
   - *为什么*：两个 $\boldsymbol{\mu}_{n}$-gerbe 若在 $\mathrm{H}^{2}(-,\boldsymbol{\mu}_{n})$ 中类相同，则其中一个乘可逆扭曲层得到另一个；模空间只依赖带化类，故同构。

> **缺口**：原文把证明归给「分裂分歧」的计算与命题 A.2.3 的粘合，未逐步写出；且译注 8 只对了一半（批注 16）：正文右端仍写作 $M^{*}_{\mathscr{P}/k}(n,L)$，按证明首句「可假定 $k=\overline{k}$」应补 $\otimes\overline{k}$。故记为 sketch 并注明这处不一致。


出处：ch6 §5.1 命题 5.1.3（中译 p. 111 / en PDF p. 121）

### 命题 4.3（根叠上的局部自由层等价于抛物丛）

设 $\mathscr{P}\to\mathbf{P}^{1}$ 是在 $D=p_{1}+\cdots+p_{r}$ 上取平方根的叠，抛物权为 $0\le a_{i}<b_{i}\le1$。则 $\mathscr{P}$ 上带指定权重的局部自由层范畴与 $\mathbf{P}^{1}$ 上相应抛物丛的范畴等价，且等价保持次数。

**证明状态：提纲（有缺口）**

1. 把 $\mathscr{P}$ 上的局部自由层沿 $\pi$ 拉回到 $\mathbf{P}^{1}$ 的覆盖上，得到带 $\boldsymbol{\mu}_{2}$-等变结构的层；在 $p_{i}$ 处的等变结构按特征标 $\{0,\frac{1}{2}\}$ 给出一个二步旗标，即抛物结构。
   - *为什么*：$\xi_{i}\cong\mathsf{B}\boldsymbol{\mu}_{2}$ 的惯性作用把层在 $p_{i}$ 上方劈成两个特征块，两个块的秩比就是抛物权。
2. 反向由抛物丛的旗标读出 $\boldsymbol{\mu}_{2}$-等变结构，再下降回 $\mathscr{P}$；次数由 $\deg_{\mathscr{P}}=(1/2)\deg_{\mathbf{P}^{1}}$（对 $\xi_{i}$ 方向）匹配。
   - *为什么*：根叠的次数定义使「$\mathscr{P}$ 上的次数」与「抛物次数」相差 $\frac{1}{2}[\kappa_{i}:k]$ 的部分，正是抛物权的作用。

> **缺口**：原文只陈述范畴等价与次数保持，把「两个方向互为逆」「次数公式的核对」留给读者（批注 18 指出 §4–§5 是未定型的工作）；故记为 sketch。


出处：ch6 §4 命题 4.3（中译 p. 106 / en PDF p. 116）

## 易错点

- 以为根叠改变了原来的概形：在 $D$ 之外 $\pi$ 是同构，根叠只在 $D$ 上加了惯性；把根叠说成「$X$ 的覆盖」会算错 $\operatorname{Pic}$。
- 把 $\deg\mathscr{O}(\xi_{i})$ 当成整数：它是 $\frac{1}{2}[\kappa_{i}:k]$（批注 7），抛物权必须取 $\{0,\frac{1}{2}\}$；用整数权会得到不存在的模空间。
- 把根叠与 gerbe 混为一谈：根叠整体上不是 gerbe（$D$ 外没有惯性），只是一个带 $\boldsymbol{\mu}_{n}$-惯性除子的叠；「$\mathscr{R}_{n}$ 是 $\mathsf{B}\boldsymbol{\mu}_{n}$-gerbe」只在闭点上方成立。
- 忘掉「$n$ 在基上可逆」与「$\kappa$ 含 $\mu_{n}$」：没有单位根就无法把循环扩张写成取根，根叠与分歧的对应在正特征下要小心。

## 相关卡

- [分歧正合列](../concepts/ramification-sequence.md)
- [μ_n-带化的 gerbe](../concepts/gerbe-banded-by-mu-n.md)
- [扭曲层](../concepts/twisted-sheaf.md)
- [Hecke 修正与 Hecke 型](../concepts/hecke-modification.md)

## 出处

- ch6 附录 C 根叠与命题 C.1（另见 §4 抛物丛、§5.1）；中译 p.116（英文 PDF p.126），源码 `chapters/ch06.tex:678`
