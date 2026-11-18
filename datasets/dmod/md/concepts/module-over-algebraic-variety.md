---
id: dmod/concept/module-over-algebraic-variety
type: concept
track: C
---

# 代数簇上的模与拟凝聚性

> 代数簇上的模层经整体截面函子 $\Gamma$ 与 $R(X)$-模相联系；局部化 $\Delta(V)=\mathcal O_X\otimes_{R(X)}V$ 是其左伴随，仿射时由 Serre 定理成为范畴等价。

**问题**：$\mathcal O_X$-模与 $R(X)$-模之间的过渡靠哪一对函子，拟凝聚性为什么可以只在仿射开邻域上检验？

## 定义

设 $X$ 是特征零代数闭域 $k$ 上的代数簇，$R(X)$ 是 $X$ 上正则函数环，$A=\mathcal O_X$。局部化函子 $\Delta:\mathcal M(R(X))\to\mathcal M(\mathcal O_X)$ 由 $\Delta(V)=A\otimes_{R(X)}V$ 给出，它与整体截面函子 $\Gamma(X,-)$ 构成伴随对 $\operatorname{Hom}_A(\Delta(V),W)=\operatorname{Hom}_A(V,\Gamma(X,W))$。$X$ 仿射时称 $\mathcal O_X$-模 $V$ 拟凝聚，若 $V\cong\Delta(V)$；一般 $X$ 上称 $V$ 拟凝聚，若每点有仿射开邻域 $U$ 使 $V|_U$ 拟凝聚。拟凝聚 $\mathcal O_X$-模构成全子范畴 $\mathcal M_{qc}(\mathcal O_X)$，它是 Abel 范畴。

*记号*：$R(X)=\Gamma(X,\mathcal O_X)$；$\Delta(V)=\mathcal O_X\otimes_{R(X)}V$；$\mathcal M_{qc}(\mathcal O_X)\subset\mathcal M(\mathcal O_X)$ 为全子范畴。

## 要点

- $\Delta$ 是 $\Gamma$ 的左伴随：$\operatorname{Hom}_{\mathcal O_X}(\Delta(V),W)=\operatorname{Hom}_{R(X)}(V,\Gamma(X,W))$，这是把 $R(X)$-模陈述翻译成层陈述的唯一入口。
- $X$ 仿射时 $\Delta$ 与 $\Gamma$ 互为拟逆，$\mathcal M_{qc}(\mathcal O_X)$ 与 $\mathcal M(R(X))$ 等价（Serre 定理）。
- 拟凝聚性是局部性质：先在一个仿射开邻域内用 $\Delta$ 判据，再逐点粘起来。
- $\mathcal M_{qc}(\mathcal O_X)$ 是 Abel 范畴，故拟凝聚模之间的核、像、余核仍在其中。
- 层的支集是闭集：$\operatorname{supp}(F)$ 是使 $F|_U=0$ 的最大开集之补（chap3.tex:52）。

## 关键公式

- $\Delta(V)=\mathcal O_X\otimes_{R(X)}V$
- $\operatorname{Hom}_{\mathcal O_X}(\Delta(V),W)=\operatorname{Hom}_{R(X)}(V,\Gamma(X,W))$
- $\operatorname{supp}(F)=X-\bigcup\{U\subset X\ \text{开}\mid F|_U=0\}$

## 定理与证明

### 引理（$\Delta$ 是 $\Gamma$ 的左伴随，chap3.tex:7-15）（完整）

对任意 $R(X)$-模 $V$ 与 $\mathcal O_X$-模 $W$ 有自然同构 $\operatorname{Hom}_{\mathcal O_X}(\Delta(V),W)=\operatorname{Hom}_{R(X)}(V,\Gamma(X,W))$，即 $\Delta$ 是整体截面函子 $\Gamma$ 的左伴随。

1. 记 $A=\mathcal O_X$，则 $\Delta(V)=A\otimes_A V$；对任意 $A$-模 $V$、$W$ 有张量-同态伴随 $\operatorname{Hom}_A(A\otimes_A V,W)=\operatorname{Hom}_A(V,\operatorname{Hom}_A(A,W))$。  
   *为什么*：这是模范畴的张量-同态伴随律，逐开集验证后再层化即得层版本。
2. 有自然同构 $\operatorname{Hom}_A(A,W)\cong\Gamma(X,W)$，它把 $A$-模态射 $T$ 映为 $T(1_X)$。  
   *为什么*：$A$-模态射由单位元的像唯一决定，故取值映射给出双射。
3. 合成两步即得 $\operatorname{Hom}_{\mathcal O_X}(\Delta(V),W)=\operatorname{Hom}_{R(X)}(V,\Gamma(X,W))$，也就是 $\Delta\dashv\Gamma$。  
   *为什么*：伴随性按定义就是这两个 Hom 集之间的自然同构。

*出处*：引理 / chap3.tex:7-15

### Serre 定理（仿射情形，chap3.tex:25）（要点（有缺口））

若 $X$ 仿射，则 $\Delta:\mathcal M(R(X))\to\mathcal M_{qc}(\mathcal O_X)$ 是范畴等价，$\Gamma:\mathcal M_{qc}(\mathcal O_X)\to\mathcal M(R(X))$ 是它的拟逆。

1. $\Delta$ 是 $\Gamma$ 的左伴随（本卡上一条定理）。  
   *为什么*：伴随性是下述等价陈述的形式前提。
2. 仿射时 $\Gamma\circ\Delta\cong\operatorname{id}$ 与 $\Delta\circ\Gamma\cong\operatorname{id}$ 同时成立。  
   *为什么*：这正是 Serre 定理的内容，讲义直接引用而未证。

> 缺口：讲义在 chap3.tex:25 直接引用 Serre 定理，未给出证明；本卡只记录陈述与其在 $\mathcal D_X$-模情形（chap3.tex:31-49）的类比证明思路。

*出处*：Serre 定理 / chap3.tex:25


## 易错点

- $\Delta$ 只右正合，一般不左正合；$\Gamma$ 是左正合的。混用两者的正合性方向是最常见的错误。
- 拟凝聚性在仿射与非仿射情形的定义方式不同：一般 $X$ 上是逐点找仿射开邻域，$V\cong\Delta(V)$ 这个判据只在该邻域内部有效。
- 支集是层（整体）的支集，等于「使限制为零的最大开集」之补；不要与某个截面 $s$ 的支集混淆。

## 出处

- Miličić《Lectures on the Algebraic Theory of D-Modules》中译本，第 III 章 §1 拟凝聚 $\mathcal D_X$-模，p.77（PDF p.83），`源码/chapters/chap3.tex:5-31（局部化函子与拟凝聚定义）`

## 核验

状态：`external-confirmed`（2026-11-19）
- Stacks Project：https://stacks.math.columbia.edu/tag/01BD — 该节给出拟凝聚 $\mathcal O_X$-模的标准定义与基本性质：仿射上是 $\widetilde M$ 型模，拟凝聚性可局部检验，拟凝聚模的全子范畴是 Abel 范畴。这与本卡仿射判据 $V\cong\mathcal O_X\otimes_{R(X)}V$ 及「逐点仿射邻域检验」的说法一致。

## 关联

- `dmod/concept/quasi-coherent-d-module`
- `dmod/concept/dz-structure-sheaf`
