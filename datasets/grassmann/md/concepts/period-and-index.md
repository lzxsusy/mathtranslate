# 周期与指标

> `grassmann/concept/period-and-index` · 轨道 6 · 曲线上层的算术 · 状态 draft

> **先自测**：为什么「周期整除指标」可以只用一个行列式层的技巧证明，而反方向却需要 de Jong 那样的深定理？

## 一句话

指标是扭曲层的最小非零秩，周期是 Brauer 类在 H²(η,G_m) 中的阶；per 整除 ind，ind 整除 per 的某个幂。

## 定义

设 $Z$ 是整 Noether 概形，一般点为 $\eta$，$\mathscr{Z}\to Z$ 是 $\mathbf{G}_m$-gerbe。$[\mathscr{Z}]$ 的**指标**（index）为
$$\operatorname{ind}([\mathscr{Z}])=\min\{\operatorname{rk}\mathscr{F}\ :\ \mathscr{F}\ \text{是凝聚}\ \mathscr{Z}\text{-扭曲层},\ \mathscr{F}\ne0\},$$
而 $[\mathscr{Z}]$ 的**周期**（period）是 $[\mathscr{Z}]_{\eta}$ 在 $\mathrm{H}^{2}(\eta,\mathbf{G}_m)$ 中的阶，记作 $\operatorname{per}([\mathscr{Z}])$。

当 $Z=\operatorname{Spec}K$ 时二者有具体含义：$\alpha\in\operatorname{Br}(K)$ 对应唯一的中心除环 $D$，$D$ 在 $K$ 上的维数为 $n^{2}$，则 $\operatorname{ind}(\alpha)=n$；$\operatorname{per}(\alpha)$ 就是 $\alpha$ 在 $\mathrm{H}^{2}(K,\mathbf{G}_m)$ 中的阶。

**记号约定**：$Z$ 整 Noether，$\eta$ 一般点；$\mathscr{Z}\to Z$ 是 $\mathbf{G}_m$-gerbe；$\mathrm{ind}$ 取凝聚扭曲层的最小非零秩；$\mathrm{per}$ 取一般点处类的阶；$\operatorname{Br}_{\infty}(C)$ 表示在所有位上都局部平凡的 Brauer 类子群。

## 要点（为什么需要它）

- $\operatorname{per}\mid\operatorname{ind}$ 的机制（批注 13）：若 $V$ 是秩为 $r$ 的 $\mathscr{Z}$-扭曲层，则 $\det V$ 是 $\mathscr{Z}_{r}$-扭曲层（$\mathbf{G}_m$ 以 $\lambda$ 作用 $V$、以 $\lambda^{r}$ 作用 $\det V$），而 $\det V$ 可逆，故 $[\mathscr{Z}_{r}]=0$，即 $r[\mathscr{Z}]=0$。取 $r=\operatorname{ind}$ 即得周期整除指标。
- 反方向 $\operatorname{ind}\mid\operatorname{per}^{h}$ 是 Gabber / de Jong 型的深定理（命题 B.5），一般域上 $h$ 是否可以只依赖 $K$ 仍是一个大问题；本章不证明它，只引用。
- 本章的目标（定理 3.4）：若猜想 2.3 成立，则整体域上曲线 $C$ 的任意 $\alpha\in\operatorname{Br}_{\infty}(C)$ 满足 $\operatorname{per}(\alpha)=\operatorname{ind}(\alpha)$——这正是引言里「周期-指标问题」的几何化。
- 证明骨架五步：带截面纤维化把分歧关进一条纤维 ⟹ 取 $\boldsymbol{\mu}_{n}$-gerbe 使 $[\mathscr{C}\otimes\overline{K}]=0$ ⟹ 模空间几何有理、$\mathrm{Br}(K)\to\mathrm{Br}(M)$ 是同构，故局部点提升为整体点 ⟹ 猜想 2.3 给次数 $1$ 的 $0$-闭链、提升成复形 $P^{\bullet}$（$\operatorname{rk}P^{\bullet}=n$）⟹ 一般点层的半单性给出秩 $n$ 的 $\mathscr{C}_{\eta}$-扭曲层，故 $\operatorname{ind}\mid n=\operatorname{per}$。
- 已知的无条件情形：有限域上曲线 $\operatorname{Br}(C)=0$（定理 3.1，Lang + Wedderburn）；代数闭域上曲面 $\operatorname{per}=\operatorname{ind}$（de Jong，定理 3.2）。曲线情形无条件的结果仍是 open，这就是为什么要假设猜想 2.3。

## 关键公式

$$
\operatorname{ind}([\mathscr{Z}])=\min\{\operatorname{rk}\mathscr{F}:\ 0\ne\mathscr{F}\ \text{coherent}\ \mathscr{Z}\text{-twisted}\}
$$

$$
\operatorname{per}(\alpha)\mid\operatorname{ind}(\alpha),\qquad \operatorname{ind}(\alpha)\mid\operatorname{per}(\alpha)^{h}
$$

$$
r[\mathscr{Z}]=0\qquad\text{for } r=\operatorname{ind}([\mathscr{Z}])
$$

$$
\operatorname{ind}(\alpha)\mid n=\operatorname{per}(\alpha)\qquad(\alpha\in\operatorname{Br}_{\infty}(C),\ \text{under Conjecture 2.3})
$$

## 定理与证明（或缺口）

### 命题 B.5（周期与指标的两个整除关系）

对任意 $\alpha\in\operatorname{Br}(K)$，存在正整数 $h$ 使得
$$\operatorname{per}(\alpha)\mid\operatorname{ind}(\alpha)\quad\text{且}\quad\operatorname{ind}(\alpha)\mid\operatorname{per}(\alpha)^{h}.$$

**证明状态：只引出处，原书不重证**


> 原文说这是 Galois 上同调中的一个练习，并把证明指给 [20, Lemma 2.1.1.3]，本章只使用结论（per | ind 另在批注 13 中用 $\det$ 给出几何证明）；因此按 reference 记。


出处：ch6 附录 B 命题 B.5（中译 p. 115 / en PDF p. 125）

### 定理 3.4（猜想 2.3 蕴含曲线上的周期 = 指标）

设 $K$ 是整体域，$S$ 是其整数概形，$C\to S$ 是带截面的固有相对曲线且一般纤维光滑。若猜想 2.3 成立，则任意 $\alpha\in\operatorname{Br}_{\infty}(C)$ 满足 $\operatorname{per}(\alpha)=\operatorname{ind}(\alpha)$。

**证明状态：完整**

1. 记 $n=\operatorname{per}(\alpha)$。由 $C\to S$ 有截面，可取 $\boldsymbol{\mu}_{n}$-gerbe $\mathscr{C}\to C$ 使 $[\mathscr{C}\otimes\overline{K}]=0\in\mathrm{H}^{2}(C\otimes\overline{K},\boldsymbol{\mu}_{n})$；由类域论，$\alpha$ 在点 $p\in C(K)$ 上的限制平凡。
   - *为什么*：截面给出 $C(K)$ 中的点 $p$；$\boldsymbol{\mu}_{n}$-带化的提升存在性由 $[\mathscr{C}\otimes\overline{K}]=0$ 与 Kummer 序列控制。
2. 令 $\chi: \mathscr{M}_{\mathscr{C}_{K}/K}(n,\mathscr{O}(p))\to M_{\mathscr{C}_{K}/K}(n,\mathscr{O}(p))$ 为 $\boldsymbol{\mu}_{n}$-gerbe。若每个完备化 $K_{\nu}$ 上叠 $\mathscr{M}_{\mathscr{C}_{K}/K}(n,\mathscr{O}(p))_{K_{\nu}}$ 非空，则其相伴 Brauer 类 $\beta$ 在每个 $\beta_{K_{\nu}}$ 处为零，故 $\beta=0$，从而 $M$ 的任意有理点都提升为叠的对象。
   - *为什么*：$M$ 的 Picard 群为 $\mathbf{Z}$ 且几何有理，故 $\mathrm{Br}(K)\to\mathrm{Br}(M)$ 是同构；类域论给出 $\mathrm{H}^{1}(K,\mathbf{Q}/\mathbf{Z})$ 的局部-整体原则，$\beta$ 局部平凡故整体平凡。
3. 假设猜想 2.3，粗空间上得到次数 $1$ 的 $0$-闭链：它给出两个有限代数 $L_{1},L_{2}/K$ 使 $[L_{1}:K]-[L_{2}:K]=1$ 且 $M_{\mathscr{C}\otimes L_{i}/L_{i}}(n,\mathscr{O}(p))_{L_{i}}\neq\varnothing$；前推得两个 $\mathscr{C}\otimes K$-扭曲层 $V_{1},V_{2}$，$\operatorname{rk}V_{1}-\operatorname{rk}V_{2}=n$，取复形 $P^{\bullet}=[V_{1}\to V_{2}]$（微分 $0$）。
   - *为什么*：沿有限平坦 $\mathscr{C}\otimes L_{i}\to\mathscr{C}$ 前推使秩乘以 $[L_{i}:K]$，故秩差的记账恰为 $n$；猜想 2.3 的作用正是把「有 $0$-闭链」提升为「有复形」。
4. $C$ 的一般点上的凝聚扭曲层范畴半单（它是除环上的有限模范畴），$K_{0}=\mathbf{Z}\cdot[D]$，故 $n$ 是单对象 $D$ 的倍数的整倍数，存在秩 $n$ 的 $\mathscr{C}_{\eta}$-扭曲层，于是 $\operatorname{ind}(\alpha)\mid n=\operatorname{per}(\alpha)$；结合 $\operatorname{per}\mid\operatorname{ind}$ 得等号。
   - *为什么*：半单性使「秩」是单对象秩的倍数；$P^{\bullet}$ 的秩为 $n$ 且一般点上可延拓为真层，故单对象的秩整除 $n$。
5. 余下是局部点：阿基米德位由稳定向量丛模空间在无穷域上有有理点给出；有限位用定理 3.1（$\operatorname{Br}(C\otimes F)=0$）与 Esnault 定理给出 $C\otimes F$ 上的稳定层，再由 $\mathscr{M}_{\mathscr{C}/S}$ 在 $S$ 上光滑形变到 $R$。
   - *为什么*：稳定层的模空间光滑射影且有理连通，故在有限域上有有理点（Esnault），$\boldsymbol{\mu}_{n}$-gerbe 在该点上分裂即给叠的对象。


出处：ch6 §3 定理 3.4（证明见原文 pp. 105–107）

### 定理 3.2（de Jong：曲面上的周期 = 指标）

设 $X$ 是代数闭域 $k$ 上的曲面，则对所有 $\alpha\in\operatorname{Br}(k(X))$ 有 $\operatorname{per}(\alpha)=\operatorname{ind}(\alpha)$。

**证明状态：只引出处，原书不重证**


> 原文只「勾勒」证明：爆破把分歧关进一条纤维、取 $[\mathscr{C}\otimes\overline{k(t)}]=0$ 的 gerbe、用单有理性与 Graber–Harris–Starr 得有理点、再用 Tsen 定理提升；细节（含 $\charop k>0$ 的归约）指给 [20]，故按 reference 记。


出处：ch6 §3 定理 3.2（de Jong）

## 易错点

- 把 $\operatorname{ind}$ 当成 $\operatorname{per}$ 的幂：一般只知道 $\operatorname{per}\mid\operatorname{ind}$ 与 $\operatorname{ind}\mid\operatorname{per}^{h}$，$h$ 可以很大；曲线情形无条件 $\operatorname{per}=\operatorname{ind}$ 仍是 open，只有猜想 2.3 下的条件结果（定理 3.4）。
- $\det V$ 落到的 gerbe 是 $\mathscr{Z}_{r}$ 而不是 $\mathscr{Z}$：忘了乘 $r$ 会得出 $[\mathscr{Z}]=0$ 或「指标无意义」的错误结论（批注 13）。
- 定理 3.4 里「$C$ 是一般纤维」不能省：$\dim=1$ 使一般点的扭曲层能延拓为局部自由层，这正是曲面情形必须另证（de Jong）的原因。
- 把猜想 2.3 的假设漏掉：定理 3.1、3.2 是无条件的，但曲线情形并没有无条件的 $\operatorname{per}=\operatorname{ind}$；引用时要说清依赖关系。

## 相关卡

- [扭曲层](../concepts/twisted-sheaf.md)
- [Faddeev 指标](../concepts/faddeev-index.md)
- [μ_n-带化的 gerbe](../concepts/gerbe-banded-by-mu-n.md)
- [α-稳定凝聚系](../concepts/alpha-stable-coherent-system.md)

## 出处

- ch6 附录 B 定义 B.4–命题 B.5（另见 §3 定理 3.1–3.4）；中译 p.115（英文 PDF p.125），源码 `chapters/ch06.tex:648`
