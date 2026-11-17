# csw 卡片总表（taxonomy）

按轨道（track）分组。“证明”列：complete = 卡内给出完整步骤；sketch = 给要点并标缺口。

## O · 总览（1 张）

| id | 标题 | 类型 | 说明 |
| --- | --- | --- | --- |
| `csw/concept/overview-cs-wzw` | 总览：从 Chern–Simons 作用量到共形块 | concept | 三维 CS 理论只有作用量、没有度规；把它沿曲面切开正则量子化，相空间是平坦联络模空间，几何量子化后得到共形块的有限维空间，Jones 多项式是其可计算推论。 |

## A · 三维理论：作用量、level、Wilson 线（3 张）

| id | 标题 | 类型 | 说明 |
| --- | --- | --- | --- |
| `csw/concept/cs-action` | Chern–Simons 作用量 | concept | 在三维流形上积一个 3-形式 $\operatorname{Tr}(A\wedge dA+\frac23A^3)$：只依赖定向、不依赖度规，变分给出 $F=0$。 |
| `csw/concept/level-quantization` | $k$ 的整性：大规范变换 | concept | 绕数为 $m$ 的大规范变换把作用量平移 $2\pi km$；量子理论要求 $e^{iL}$ 单值，于是 $k$ 必须是整数。 |
| `csw/concept/wilson-line` | Wilson 线 | concept | 沿闭曲线 $C$ 取联络的路径序指数再取迹：不需要度规，只依赖曲线的同伦类与表示，是三维理论的“可观测量”。 |

## B · 相空间：约束、辛商、平坦联络模空间（5 张）

| id | 标题 | 类型 | 说明 |
| --- | --- | --- | --- |
| `csw/concept/flat-connection-moduli` | 平坦联络模空间 | concept | CS 的物理相空间是 $\Sigma$ 上平坦联络模去规范变换，即 $\operatorname{Hom}(\pi_1\Sigma,G)/G$；$g>1$ 时实维数 $(2g-2)d$。 |
| `csw/concept/gauss-law-constraint` | 高斯定律作为第一类约束 | concept | $A_0$ 是拉格朗日乘子，对它的变分给出 $\varepsilon^{ij}F_{ij}=0$；这条约束是第一类约束，生成规范变换。 |
| `csw/concept/narasimhan-seshadri` | Narasimhan–Seshadri：平坦联络与稳定全纯丛 | concept | degree 0 的稳定全纯 $G_{\mathbb{C}}$-丛与不可约平坦酉联络一一对应；它把 $M$ 变成 Kähler 模空间，从而可以谈“全纯截面”。 |
| `csw/concept/symplectic-quotient` | 辛商（Marsden–Weinstein 约化） | concept | 相空间 $P$ 带第一类约束时，物理相空间是约束面 $\mu^{-1}(0)$ 模掉约束生成的群作用，辛形式自动下降。 |
| `csw/example/pillowcase-dimension` | 枕头套与 $g=1$ 的维数例外 | example | $SU(2)$、$g=1$ 的平坦联络模空间是枕头套 $T^2/\{\pm1\}$（实维 2），不是点；$(2g-2)d=0$ 的公式失效。 |

## C · 几何量子化机器：预量子化、极化、全纯截面、半形式（9 张）

| id | 标题 | 类型 | 说明 |
| --- | --- | --- | --- |
| `csw/concept/half-form-correction` | 半形式修正与 $k\to k+h^\vee$ | concept | 把量子态从 $\cL^{\otimes k}$ 的截面换成 $\cL^{\otimes k}\otimes K^{1/2}$ 的截面；在 $SU(2)$ 上这把 level 平移为 $k+2$，即 $k+h^\vee$。 |
| `csw/concept/hitchin-connection` | Hitchin 联络与 KZ 联络 | concept | 在 Teichmüller 空间上，把全纯截面空间沿“复结构改变”的方向求导，得到 Hitchin 联络；在 $g=0$ 带标记点时它显式化为 KZ 方程。 |
| `csw/concept/holomorphic-sections` | 全纯截面空间作为量子 Hilbert 空间 | concept | CS 的量子 Hilbert 空间是 $\cH_\Sigma=H^0(\cM_J,\cL^{\otimes k})$：模空间上的全纯截面空间，有限维。 |
| `csw/concept/polarization` | 极化 | concept | 在复化切丛里选一个拉格朗日、可积且维数为 $n$ 的子丛 $P$，把“沿 $P$ 协变常数”的截面当作量子态；它把 $2n$ 个变量砍成 $n$ 个。 |
| `csw/concept/prequantization-determinant-line` | 预量子化：行列式线丛 | concept | 在模空间上取行列式线丛 $\cL$（Quillen 度规）；$c_1(\cL)=[\omega]$，所以 $[\cL^{\otimes k}]=k[\omega]$，整性自动满足。 |
| `csw/concept/projective-flat-connection` | 射影平坦丛与“与 $J$ 无关” | concept | $H^0(\cM_J,\cL^{\otimes k})$ 随 $J$ 构成 Teichmüller 空间上的向量丛，只带射影平坦联络：平行移动在整体相位上有歧义，单值性给出映射类群的射影表示。 |
| `csw/example/abelian-torus-dimension` | U(1) 在环面上的 Hilbert 空间维数 = k | example | $U(1)_k$ 在 $T^2$ 上的态空间维数为 $k$；一般亏格 $g$ 为 $k^g$。 |
| `csw/example/level-shift-check` | 半形式修正的数值检验：$k$ 与 $k+2$ | example | 对比“$k$ 个 theta 截面”与“$k+1$ 个可积表示”：多出的 1 来自半形式 $K^{1/2}=\cL^{-2}$，即 $k\to k+2$。 |
| `csw/example/su2-torus-theta` | $SU(2)$ 环面：$k$ 个截面，半形式后 $k+1$ | example | $SU(2)_k$ 环面模空间是枕头套；$\cL^{\otimes k}$ 给 $k$ 个截面，加半形式后 $k+1$。 |

## D · Wilson 线的穿刺点与 Borel–Weil–Bott（5 张）

| id | 标题 | 类型 | 说明 |
| --- | --- | --- | --- |
| `csw/concept/borel-weil-bott` | Borel–Weil–Bott 与表示的几何化 | concept | 不可约表示 $R_\lambda$ 就是旗流形 $G/T$ 上全纯线丛 $\cL_\lambda$ 的全纯截面空间：$H^0(G/T,\cL_\lambda)=R_\lambda$（$\lambda$ 支配整）。 |
| `csw/concept/flag-orbit-symplectic` | 旗流形上的辛形式与轨道方法 | concept | $G/T$ 上的辛形式 $\omega_\lambda(X,Y)=\frac12\langle\lambda,[X,Y]\rangle$ 由最高权给出；$G/T$ 就是这个权对应的余伴随轨道。 |
| `csw/concept/integrable-representation` | 可积表示与 $2j\le k$ 截断 | concept | 只有“可积”的表示才给出非零共形块：$SU(2)$ 时 $2j\le k$；一般 $G$ 时 $\lambda$ 属 level $k$ 的仿射 Weyl 群基本域。 |
| `csw/concept/puncture-gauss-law` | 穿刺点上的高斯定律 | concept | 在标记点 $P_s$ 处，高斯定律的右端多出算符值源 $T^a_{(s)}$：$(k/8\pi)\varepsilon^{ij}F^a_{ij}(x)=\sum_s\delta^2(x-P_s)T^a_{(s)}$。 |
| `csw/example/bwb-su2` | $SU(2)$ 的 BWB：$H^0(G/T,\cL_j)=R_j$ | example | $SU(2)$ 的旗流形是 $S^2$；$H^0(S^2,\cL_j)$ 的维数是 $2j+1$，即自旋 $j$ 表示。 |

## E · WZW 一侧：仿射代数、Sugawara、共形块、KZ、融合（7 张）

| id | 标题 | 类型 | 说明 |
| --- | --- | --- | --- |
| `csw/concept/affine-lie-algebra` | 仿射 Lie 代数与 OPE | concept | WZW 的对称代数是 $\hat{\mathfrak{g}}_k$：$[J^a_n,J^b_m]=if^{abc}J^c_{n+m}+kn\delta^{ab}\delta_{n+m,0}$；$k$ 就是 level。 |
| `csw/concept/conformal-blocks` | 共形块 | concept | 带标记点 $(\Sigma;P_i,R_i)$ 的共形块空间 $\cH_\Sigma$ 是 WZW 的手征态空间；在 CS 里它就是 $H^0(\cM_J,\cL^{\otimes k})$。 |
| `csw/concept/fusion-rules` | 融合规则与 Verlinde 公式 | concept | 融合规则 $R_i\otimes R_j=\bigoplus_kN_{ij}^kR_k$ 的系数由 $S$ 矩阵给出：$N_{ij}^k=\sum_l\frac{S_{il}S_{jl}S_{kl}}{S_{0l}}$。 |
| `csw/concept/knizhnik-zamolodchikov` | Knizhnik–Zamolodchikov 方程 | concept | 共形块作为 $z_i$ 的函数满足 $\kappa\partial_{z_i}\Psi=\sum_{j\ne i}\frac{\Omega_{ij}}{z_i-z_j}\Psi$，$\kappa=k+h^\vee$。 |
| `csw/concept/sugawara-construction` | Sugawara 构造与中心荷 | concept | $T(z)=\frac1{2(k+h^\vee)}\sum_a:J^aJ^a:$ 给出 Virasoro 代数，中心荷 $c=k\dim G/(k+h^\vee)$。 |
| `csw/concept/wzw-action` | Wess–Zumino–Witten 作用量与 level | concept | $S_{WZW}=S_\sigma+k\Gamma$：动能项 $S_\sigma$ 与拓扑项 $\Gamma$（Wess–Zumino 项）；$e^{iS}$ 单值要求 $k\in\mathbb{Z}$。 |
| `csw/example/kz-two-point` | KZ 两点函数与共形权 | example | 两点共形块 $\Psi=(z_1-z_2)^{-2h_j}$，指数是共形权 $h_j$；$SU(2)$、$k=1$ 时 $h_{1/2}=1/4$。 |

## F · 对偶与映射类群（2 张）

| id | 标题 | 类型 | 说明 |
| --- | --- | --- | --- |
| `csw/concept/cs-wzw-duality` | CS/WZW 对偶：态空间的等同 | concept | 三维 CS 在 $\Sigma\times\mathbb{R}$ 上的量子 Hilbert 空间等于二维 WZW 在 $\Sigma$ 上的共形块空间；这是“态空间等同”，不是动力学等价。 |
| `csw/concept/mapping-class-group` | 映射类群与模函子 | concept | $\operatorname{MCG}(\Sigma)$ 通过“剪开-扭转-粘回”作用于 $\Sigma$，得到 $\cH_\Sigma$ 上的射影表示；Segal 的模函子把这套结构公理化。 |

## G · 计算：手术、S 矩阵、Verlinde、Jones（7 张）

| id | 标题 | 类型 | 说明 |
| --- | --- | --- | --- |
| `csw/concept/jones-from-cs` | Jones 多项式从 CS 来 | concept | $S^3$ 上沿链环 $L$ 的 Wilson 线期望值 $\langle\prod W_{R_i}(K_i)\rangle$ 在 $G=SU(N)$ 定义表示时给出两变量 Jones 多项式（变量 $N$ 与 $k$）。 |
| `csw/concept/s-matrix` | 模 S 矩阵与 T 矩阵 | concept | $S$ 与 $T$ 是 $SL(2,\mathbb{Z})$ 在共形块空间上的表示；$T$ 对角，$S$ 由正弦公式给出（$SU(2)$）。 |
| `csw/concept/surgery-formula` | 手术公式：沿环面切开-粘合 | concept | 沿环面上的 $K$ 个 Wilson 线做手术，配分函数由 $S$ 矩阵与链环不变量给出：$Z_k(M)=S_{00}C^{\sigma(L)}\sum_\lambda S_{0\lambda}J$。 |
| `csw/concept/verlinde-formula` | Verlinde 公式 | concept | $N_{ijk}=\sum_l\frac{S_{il}S_{jl}S_{kl}}{S_{0l}}$：融合系数 = 三点共形块维数 = $S$ 矩阵的组合。 |
| `csw/example/s3-normalization` | $Z(S^3)=S_{00}$ 的数值检验 | example | $Z(S^3)=\sqrt{\frac{2}{k+2}}\sin\frac{\pi}{k+2}$：$k=1$ 给 $1/\sqrt2$，$k=2$ 给 $1/2$。 |
| `csw/example/su2-k2-s-matrix` | $SU(2)$、$k=2$ 的 $S$ 矩阵 | example | $k=2$ 的可积表示 $j=0,\frac12,1$；$S$ 是 $3\times3$ 对称矩阵，$S_{00}=\frac12$，$S^2=1$。 |
| `csw/example/trefoil-jones` | 三叶结的 Jones 多项式 | example | $V_{\text{trefoil}}(t)=-t^{-4}+t^{-3}+t^{-1}$；它是 $SU(2)$、$k$ 足够大时的 Wilson 线期望值。 |

## H · 边界：CS/WZW 与 AdS₃/CFT₂ 的区别（1 张）

| id | 标题 | 类型 | 说明 |
| --- | --- | --- | --- |
| `csw/concept/cs-vs-ads3-cft2` | CS/WZW 与 AdS₃/CFT₂：两码事 | concept | CS/WZW 是“态空间等同”（拓扑理论，无引力子）；AdS₃/CFT₂ 是“动力学等价”（体引力 + 边界 CFT + 全息字典）。两者不是同一种对偶。 |

## 例子卡（按依赖的概念排序）

| id | 标题 | 依赖概念 |
| --- | --- | --- |
| `csw/example/abelian-torus-dimension` | U(1) 在环面上的 Hilbert 空间维数 = k | `holomorphic-sections`、`level-quantization` |
| `csw/example/bwb-su2` | $SU(2)$ 的 BWB：$H^0(G/T,\cL_j)=R_j$ | `borel-weil-bott`、`flag-orbit-symplectic` |
| `csw/example/kz-two-point` | KZ 两点函数与共形权 | `knizhnik-zamolodchikov`、`conformal-blocks` |
| `csw/example/level-shift-check` | 半形式修正的数值检验：$k$ 与 $k+2$ | `half-form-correction`、`holomorphic-sections` |
| `csw/example/pillowcase-dimension` | 枕头套与 $g=1$ 的维数例外 | `flat-connection-moduli`、`holomorphic-sections` |
| `csw/example/s3-normalization` | $Z(S^3)=S_{00}$ 的数值检验 | `s-matrix`、`surgery-formula` |
| `csw/example/su2-k2-s-matrix` | $SU(2)$、$k=2$ 的 $S$ 矩阵 | `s-matrix`、`verlinde-formula` |
| `csw/example/su2-torus-theta` | $SU(2)$ 环面：$k$ 个截面，半形式后 $k+1$ | `holomorphic-sections`、`half-form-correction` |
| `csw/example/trefoil-jones` | 三叶结的 Jones 多项式 | `jones-from-cs`、`wilson-line` |
