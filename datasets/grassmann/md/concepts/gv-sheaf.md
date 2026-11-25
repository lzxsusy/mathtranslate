# $GV$-层

> `grassmann/concept/gv-sheaf` · 轨道 A · 跨章基础 · 状态 draft

> **先自测**：为什么把上同调支集轨迹的余维下界写成 $\ge i$，就能等价于 Fourier–Mukai 变换的支集条件？

## 一句话

$GV$-层是阿贝尔簇上满足 $\operatorname{codim}V^i(\mathcal F)\ge i$ 的凝聚层，等价于 Fourier–Mukai 变换的支集余维条件；它是把「正则性」翻译成「无挠性」的入口。

## 定义

设 $X$ 是 $g$ 维阿贝尔簇，$\widehat X=\operatorname{Pic}^0(X)$，$P$ 是 $X\times\widehat X$ 上的正规化 Poincaré 丛，$\mathbf R\widehat{\mathcal S}(\mathcal F)=\mathbf R p_{\widehat X*}(p_X^*\mathcal F\otimes P)$。对凝聚层 $\mathcal F$ 与 $i\ge0$ 定义**上同调支集轨迹** $V^i(\mathcal F)=\{\alpha\in\widehat X\mid h^i(X,\mathcal F\otimes\alpha)>0\}$。称 $\mathcal F$ 为 **$GV$-层**，若对所有 $i>0$ 有 $\operatorname{codim}\operatorname{Supp}(R^i\widehat{\mathcal S}\mathcal F)\ge i$；等价地，$\operatorname{codim}V^i(\mathcal F)\ge i$。

**记号约定**：$\mathbf R\Delta\mathcal F=\mathbf R\mathcal H om(\mathcal F,\mathcal O_X)$；$IT_0$ 指 $i>0$ 时 $V^i(\mathcal F)=\varnothing$；$WIT_k$ 指 $R^i\widehat{\mathcal S}\mathcal G=0$ 对 $i\ne k$。

## 要点（为什么需要它）

- 两个条件的等价靠基变换：由基变换有 $\operatorname{Supp}(R^i\widehat{\mathcal S}\mathcal F)\subset V^i(\mathcal F)$，反向再由基变换与余维比较得到。
- 定理 2.3 给出第三种刻画：$\mathcal F$ 是 $GV$-层，当且仅当 $\mathbf R\Delta\mathcal F$ 满足 $WIT_g$。
- $IT_0$ 是最强情形：此时 $\mathbf R\widehat{\mathcal S}\mathcal F=R^0\widehat{\mathcal S}\mathcal F$ 是局部自由层。
- $M$-正则层把 $\ge i$ 加严为 $>i$；每个 $M$-正则层都是 $GV$-层，反之不然。

## 关键公式

$$
V^i(\mathcal F)=\{\alpha\in\widehat X\mid h^i(X,\mathcal F\otimes\alpha)>0\}
$$

$$
\operatorname{codim}\operatorname{Supp}(R^i\widehat{\mathcal S}\mathcal F)\ge i
$$

$$
\mathbf R\widehat{\mathcal S}(\mathcal F)=\mathbf R p_{\widehat X*}(p_X^*\mathcal F\otimes P)
$$

## 定理与证明（或缺口）

### 定理 2.3（$GV$ 的三种等价刻画）

设 $X$ 是 $g$ 维阿贝尔簇，$\mathcal F$ 是 $X$ 上的凝聚层。则以下条件等价：(1) $\mathcal F$ 是 $GV$-层；(2) 对 $\widehat X$ 上任意充分正的充裕线丛 $A$，$H^i(\mathcal F\otimes\widehat{A^{-1}})=0$ 对所有 $i>0$ 成立；(3) $\mathbf R\Delta\mathcal F$ 满足 $WIT_g$。

**证明状态：只引出处，原书不重证**


出处：中译 p.138（§2，引 [PP4, 推论 3.10]）

## 易错点

- $V^i$ 只记录 $h^i>0$，不记录支集；$\operatorname{Supp}(R^i\widehat{\mathcal S}\mathcal F)$ 只是 $V^i$ 的子集，两个条件等价要额外论证。
- 把 $GV$ 与 $M$-正则混同：$GV$ 是 $\ge i$，$M$-正则是 $>i$；$\mathcal O_X$ 连 $GV$ 都不是（$V^i=\widehat X$）。
- 定理 2.3(2) 里的 $\widehat{A^{-1}}$ 不是线丛，而是 $A^{-1}$ 的 Fourier–Mukai 变换（一般为高秩向量丛），不能直接对它用 Kodaira。
- 对偶的方向：$\mathbf R\Delta\mathcal F=\mathbf R\mathcal H om(\mathcal F,\mathcal O_X)$，定理 2.3(3) 说的是 $\mathbf R\Delta\mathcal F$ 满足 $WIT_g$，不是 $\mathcal F$。

## 相关卡

- [Koszul 上同调](../concepts/koszul-cohomology.md)
- [凝聚系](../concepts/coherent-system.md)

## 出处

- ch8 §2 $GV$-层的定义；中译 p.137（英文 PDF p.152），源码 `chapters/ch08.tex:44`
- ch8 §2 定理 2.3；中译 p.138（英文 PDF p.153），源码 `chapters/ch08.tex:63`
