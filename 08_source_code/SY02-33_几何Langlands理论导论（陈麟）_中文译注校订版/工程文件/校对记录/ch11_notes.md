## 待注 ch11.tex:17–19（原 PDF p57）

- 原文：The general categorical principle is the following: if $L_{ij}:\mathcal C_i\rightleftarrows\mathcal C_j:R_{ij}$ are adjoint functors between presentable categories, then $\operatorname{colim}_{L_{ij}}\mathcal C_i\simeq\lim_{R_{ij}}\mathcal C_i$.
- 概念：沿一对伴随函子，左伴随保持余极限、右伴随保持极限；在可呈示范畴上，按 $L_{ij}$ 取的余极限与按 $R_{ij}$ 取的极限可以互换。这正是光滑下降的极限定义与下文的余极限写法相等的原因。
- 读者缺什么：不知道这条原理的出处与适用范围（为何要求范畴可呈示），也看不出它就是下面把 $\Shv^{\mathrm{all}}(Y)$ 写成余极限的依据。
- 建议来源：nLab "adjoint functor theorem"；nLab "locally presentable category"。

## 待注 ch11.tex:31（原 PDF p57）

- 原文：This description is only a first approximation: the Betti moduli used in categorical Langlands is derived, with tangent complex governed by cochains of $X(\mathbb C)$ with coefficients in the adjoint local system.
- 概念：导出 Betti 模空间：经典截断只保留 $\Hom(\pi_1(X(\mathbb C),x),\check G)$，导出结构还带切复形；切复形由 $X(\mathbb C)$ 上系数在伴随局部系统中的上链给出，记录一次形变的方向（$G=\Gm$ 时对应的就是 §11.3 的椭圆曲线因子）。
- 读者缺什么：不清楚“导出的”在此为何必要、切复形落在哪一（上）同调次数、它与经典切空间如何对应，也不知道它与 §11.3 中 $E$ 因子的关系。
- 建议来源：nLab "derived algebraic geometry"；nLab "cotangent complex"。

## 待注 ch11.tex:68–70（原 PDF p58）

- 原文：More precisely, if a tangent direction $v\in T_sS$ is annihilated by all covectors in $\mathrm{SS}(\mathcal F)_s$, then $\mathcal F$ is locally acyclic, or lisse, along that direction.
- 概念：Kashiwara–Schapira 的微支撑 $\mathrm{SS}(\mathcal F)\subset T^*S$；$\mathrm{SS}(\mathcal F)_s$ 是 $s$ 处的锥形纤维，方向 $v$ 被其中所有余向量消去等价于 $v$ 落在 $\mathrm{SS}(\mathcal F)$ 的零化子内，此时 $\mathcal F$ 沿 $v$ 的微茎为零（局部无圈），即沿该方向局部常值。
- 读者缺什么：不知道“沿方向局部无圈”的定量含义、$\mathrm{SS}$ 与 $D$ 模特征簇/特征圈的关系，也不明白为什么零支撑范畴恰是拟光滑（QLisse）范畴。
- 建议来源：nLab "constructible sheaf"；nLab "D-module"。

## 待注 ch11.tex:76（原 PDF p58）

- 原文：In the AGKRRV normalization this means the left completion of the ind-category of finite-rank local systems.
- 概念：左完备化是相对于 $t$-结构（Lurie，SAG 意义下）的完备化，不是普通的 Ind-完备化：把 $\operatorname{Ind}(\text{有限秩局部系统})$ 中沿 $t$-结构正向收敛的对象补进来，得到与“零奇异支撑层”一致的 $\operatorname{QLisse}$。
- 读者缺什么：容易把“左完备化”读成“取 Ind-完备化”或“取导出完备化”，不知道它依赖 $t$-结构，也不知道 AGKRRV 为何要用它来定义 $\operatorname{QLisse}$。
- 建议来源：nLab "t-structure"；nLab "ind-object"。

## 待注 ch11.tex:100–101（原 PDF p59）

- 原文：where $(\text{--})_{\Omega_X}$ denotes the $\Gm$-twist coming from dilation on $\mathfrak g^*$. With homogeneous generators $p_i$ of degrees $d_i$, this target is $\bigoplus_i H^0(X,\Omega_X^{d_i})$.
- 概念：$\mathfrak g^*$ 上的伸缩 $\Gm$-作用给不变量 $\mathbb C[\mathfrak g^*]^G$ 的齐次生成元 $p_i$ 赋次数 $d_i$；$(\text{--})_{\Omega_X}$ 把权重 $d$ 的表示与 $\Omega_X^{\otimes d}$ 张量（扭转），于是不变量截面落在 $\bigoplus_i H^0(X,\Omega_X^{d_i})$，这正是 Hitchin 靶空间 $\cA_G$（Hitchin 基）。
- 读者缺什么：看不出“扭转”具体怎么做、$d_i$ 从何而来、为什么目标空间是分次直和（而不是 $H^0(X,(\mathfrak g^*\!/\!/G)\otimes\Omega_X)$ 这种朴素写法），也不知道 $\cA_G$ 就是 Hitchin 基。
- 建议来源：nLab "geometric Langlands correspondence"；nLab "invariant theory"。
