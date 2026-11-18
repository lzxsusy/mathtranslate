---
id: dmod/concept/coherent-d-module
type: concept
track: C
---

# 凝聚 $\mathcal D_X$-模

> $\mathcal D_X$-模凝聚指局部存在正合列 $\mathcal D_U^p\to\mathcal D_U^q\to V|_U\to0$；凝聚模的支集恰为 $V_x\neq0$ 的点集。

**问题**：为什么 $\mathcal D_X$-凝聚性可以用「局部有限表现」而不是「有限生成」来定义，二者在光滑情形为何等价？

## 定义

设 $X$ 是光滑代数簇。称拟凝聚 $\mathcal D_X$-模 $V$ 凝聚，若每点 $x$ 有开邻域 $U$ 与正合列 $\mathcal D_U^p\to\mathcal D_U^q\to V|_U\to0$（$p,q\in\mathbb Z_+$）。仿射时这等价于 $V\cong\Delta(V_0)$，其中 $V_0$ 是有限生成 $D_X$-模（引理 2.1）；由于光滑仿射簇上 $D_X$ 诺特（定理 II.3.7），凝聚性就是有限生成性的层化版本。

*记号*：$\mathcal M_{coh}(\mathcal D_X)$：凝聚 $\mathcal D_X$-模的全子范畴；$\mathcal D_U^p$：$p$ 个 $\mathcal D_U$ 的直和；$V_x$：$x$ 处的茎。

## 要点

- 仿射时凝聚 $\iff$ $V\cong\Delta(V_0)$ 且 $V_0$ 有限生成（定义 + 引理 2.1），等价说法是局部有 $\mathcal D_U^p\to\mathcal D_U^q\to V|_U\to0$。
- 凝聚性可在仿射开覆盖上检验（命题 2.2），$\mathcal M_{coh}(\mathcal D_X)$ 是 Abel 范畴（chap3.tex:124）。
- 凝聚时 $\operatorname{supp}(V)=\{x\in X:V_x\neq0\}$（命题 2.3），比拟凝聚情形的「取闭包」更强。
- 诺特性是前提：$\mathcal D_X$ 在正特征下不是诺特环，$\mathcal O_X$-凝聚与 $\mathcal D_X$-凝聚因此不一致（nLab D-module）。
- 不可约拟凝聚 $\mathcal D_X$-模自动凝聚（命题 2.6），这是有限长度模凝聚性的来源。

## 关键公式

- $\mathcal D_U^p\longrightarrow\mathcal D_U^q\longrightarrow V|_U\longrightarrow 0$
- $\operatorname{supp}(V)=\{x\in X\mid V_x\neq0\}$
- $V\cong\Delta(V_0)=\mathcal D_X\otimes_{D_X}V_0$

## 定理与证明

### 引理 2.1（凝聚性的两种刻画）（完整）

设 $X$ 是光滑仿射簇，$V$ 是拟凝聚 $\mathcal D_X$-模。则下列条件等价：(i) $V$ 是凝聚 $\mathcal D_X$-模；(ii) 对任意 $x\in X$ 存在开邻域 $U$ 与正合列 $\mathcal D_U^p\to\mathcal D_U^q\to V|_U\to0$。

1. (i)$\Rightarrow$(ii)：$V\cong\Delta(V_0)$，$V_0$ 有限生成；由 $D_X$ 诺特存在正合列 $D_X^p\to D_X^q\to V_0\to0$，局部化得 $\mathcal D_X^p\to\mathcal D_X^q\to V\to0$，故每点取 $U=X$ 即可。  
   *为什么*：诺特环上有限生成模有有限自由表现，而 $\Delta$ 右正合保持满射。
2. (ii)$\Rightarrow$(i)：取 $f$ 使 $f(x)\neq0$、$X_f\subset U$，缩小后可设 $U$ 为主开集；则 $\mathcal D_U^p\to\mathcal D_U^q\to\Gamma(U,V)\to0$ 正合，$\Gamma(U,V)$ 是有限生成 $D_U$-模。  
   *为什么*：仿射开集上整体截面函子正合，故正合列在截面上仍正合。
3. 由 $\Gamma(U,V)=\Gamma(X,V)_f$ 与 $X$ 的拟紧性取有限覆盖，把这些局部生成元并起来得满射 $\mathcal D_X^m\to V$，进而 $\Gamma(X,V)$ 有限生成，故 $V$ 凝聚。  
   *为什么*：有限多个局部生成元给出整体生成元，整体生成即 $\Gamma(X,V)$ 有限生成。

*出处*：引理 2.1 / chap3.tex:99-111

### 命题 2.3（凝聚模的支集）（完整）

设 $V$ 是光滑代数簇 $X$ 上凝聚 $\mathcal D_X$-模。则 $\operatorname{supp}(V)=\{x\in X:V_x\neq0\}$。

1. 由命题 2.2 可化到仿射情形，只需证 $\{x:V_x\neq0\}$ 是闭集。取 $y$ 在其闭包中，$U$ 是 $y$ 的仿射邻域，$V(U)$ 由 $s_1,\dots,s_n$ 作为 $D_U$-模生成。  
   *为什么*：凝聚性在仿射邻域上给出有限生成的整体截面，故可用有限个截面控制整层。
2. 令 $Z=\bigcup_{i=1}^n\operatorname{supp}(s_i)$，它是 $U$ 中含于 $\{x:V_x\neq0\}$ 的闭子集。  
   *为什么*：每个截面的支集是闭集，有限并仍闭，且支集上的点处该截面非零。
3. 若 $y\notin Z$，取 $y$ 的开邻域 $W\subset U$ 使 $s_1,\dots,s_n$ 在 $W$ 上全为零，则 $V|_W=0$，与 $y\in\operatorname{supp}(V)$ 矛盾；故 $y\in Z$。  
   *为什么*：生成元在一个邻域上全为零即该邻域上模为零，故 $y$ 不可能在支集中。

*出处*：命题 2.3 / chap3.tex:128-135


## 易错点

- 定义中的 $p,q$ 必须有限：用无限直和得到的只是拟凝聚，不是凝聚。
- 命题 2.3 的等式只在凝聚时成立；拟凝聚时 $\operatorname{supp}(V)$ 只是 $\{V_x\neq0\}$ 的闭包（命题 1.3），两者不可混用。
- 以上都以 $X$ 光滑（$D_X$ 诺特）为前提：正特征或非光滑情形下 $\mathcal O_X$-凝聚与 $\mathcal D_X$-凝聚不再一致。

## 出处

- Miličić《Lectures on the Algebraic Theory of D-Modules》中译本，第 III 章 §2 凝聚 $\mathcal D_X$-模，p.79（PDF p.85），`源码/chapters/chap3.tex:97-135（凝聚定义、引理 2.1、命题 2.3）`

## 核验

状态：`external-confirmed`（2026-11-19）
- Stacks Project：https://stacks.math.columbia.edu/tag/01BU — 该节给出 $\mathcal O_X$-凝聚模的标准定义与基本性质：局部存在 $\mathcal O_U^{\oplus p}\to\mathcal O_U^{\oplus q}\to\mathcal F|_U\to0$，凝聚性可局部检验。本卡把同一「局部有限表现」判据搬到 $\mathcal D_X$ 上（chap3.tex:99-113），并用命题 2.2 的仿射开覆盖检验与之对照。
- nLab：https://ncatlab.org/nlab/show/D-module — 该条目指出：正特征下 $D_X$ 不是诺特环，$\mathcal O_X$-凝聚与 $\mathcal D_X$-凝聚因此是不同的概念（Katz、Gieseker 的例子为此方向的标准依据）。这解释了本卡为何处处假定 $k$ 特征零且 $X$ 光滑。

## 关联

- `dmod/concept/quasi-coherent-d-module`
- `dmod/concept/characteristic-variety-sheaf`
- `dmod/concept/coherator`
