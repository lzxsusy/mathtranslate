# K–W 2006 资料卡索引

共 67 张：概念卡 40 张、推导卡 27 张。


## 轨道 A · 四维物理与对偶


**概念卡**

- [BPS 态](concepts/bps-state.md) —— 质量等于中心荷模的态（$M=|Z|$），保持部分超对称；其质量受保护，因此 BPS 谱是检验 S-对偶、确定超荷相因子的精确工具。
- [电磁对偶](concepts/electromagnetic-duality.md) —— 交换电场与磁场、把耦合常数取倒数并同时把规范群换成对偶群的对偶性；在 $\mathcal N=4$ 中它被提升为 S-对偶，是几何 Langlands 的物理源头。
- [GNO 对偶群](concepts/gno-dual-group.md) —— Goddard–Nuyts–Olive 对偶群：电核取 $G$ 的权格、磁核取对偶群 ${}^LG$ 的权格（即 $G$ 的余权格）；它把电磁对偶翻译成群论，也就是 Langlands 对偶群。
- [Langlands 对偶群](concepts/langlands-dual-group.md) —— 把 $G$ 的根数据取对偶（权格与余权格互换）得到的群 ${}^LG$：$\mathrm{SU}(N)\leftrightarrow\mathrm{PSU}(N)$、$E_8$ 自对偶；它同时是 GNO 对偶群，几何 Langlands 的右侧就出现它。
- [$\mathcal N=4$ 超对称杨–米尔斯理论](concepts/n4-sym-theory.md) —— 十维超对称杨–米尔斯降维得到的四维最大超对称规范理论：16 个超荷、$\mathrm{SU}(4)_R$ R-对称与复耦合 $\tau$；本文对它作拓扑扭化、紧化并读出几何 Langlands。
- [S-对偶](concepts/s-duality.md) —— 四维 $\mathcal N=4$ 的强弱对偶猜想：$\tau\mapsto-1/(n_g\tau)$，同时把 $G$ 换成 ${}^LG$、电换磁；它与 $T:\tau\mapsto\tau+1$ 生成离散群 $\Gamma$。
- [超荷](concepts/supercharge.md) —— 超对称变换的生成元 $Q$，把玻色子映成费米子；$\mathcal N=4$ 中有 16 个，其反对易子给出四维平移；扭化的目标就是把某个超荷变成标量且 $Q^2=0$。
- [$\theta$ 角](concepts/theta-angle.md) —— 规范理论中 $\int\mathrm{Tr}\,F\wedge F$ 拓扑项的系数，以 $2\pi$ 为周期；它与 $1/e^2$ 组成复耦合 $\tau$，$T:\tau\mapsto\tau+1$ 就是把 $\theta$ 平移 $2\pi$。

**推导卡**

- [从 GNO 对偶群到 Langlands 对偶群](derivations/gno-to-langlands.md) —— 从 GNO 关于电荷取权格、磁荷取对偶群权格的结果出发，经 Montonen–Olive 的耦合反演与群交换、Atiyah 的指认，得到 N=4 SYM 的 S-对偶是几何 Langlands 对偶的物理来源。
- [S-对偶生成元、SL(2,Z) 与超荷的双覆盖](derivations/sdual-sl2z.md) —— 从 $\mathrm{SL}(2,\mathbb Z)$ 的生成元 $S,T$ 出发，经中心荷的协变变换得到超荷在 $S$ 下的相位；该相位的平方根使对偶群须由 $(-1)^F$ 双覆盖，并定出 $S$ 在扭化参数 $t$ 上的作用。
- [非单边（non-simply-laced）群的 $n_g$ 修正与 Table 1](derivations/table1-and-ng.md) —— 从 Table 1 的七行对偶出发，说明 $n_g$ 只在 $\mathrm{Sp}(k)\leftrightarrow\mathrm{Spin}(2k+1)$ 这类李代数不同构的群对上出现，并由 $\tau$ 的归一化定出 $n_g=2$（$F_4$）与 $n_g=3$（$G_2$）。

## 轨道 B · 扭化与拓扑


**概念卡**

- [BRST 算子](concepts/brst-operator.md) —— 扭化后得到的幂零标量超荷 $Q$（$Q^2=0$），作用像 BRST 微分：物理量取 $Q$-上同调，$Q$-恰当项视为零；本文的 $Q$ 来自扭化而非规范固定。
- [上同调](concepts/cohomology.md) —— $Q$-闭模 $Q$-恰当得到的商空间；扭化理论的物理态与算子就是 $Q$ 的上同调类，$Q$-恰当的量视为零。
- [瞬子](concepts/instanton.md) —— 四维欧氏规范场的有限作用量经典解，以第二陈数 $k=\frac1{8\pi^2}\int\mathrm{Tr}\,F\wedge F$ 分类；$k\ne0$ 时扭化方程在 $t\ne0,\infty$ 无解，瞬子只在退化极限出现。
- [R-对称](concepts/r-symmetry.md) —— 作用在超荷上的内部对称群；$\mathcal N=4$ 时为 $\mathrm{SU}(4)_R\cong\mathrm{Spin}(6)$，扭化就是把它的一个 $U(1)$ 嵌进自旋群，其中心 $I$ 也标定 S-对偶的相因子。
- [拓扑量子场论](concepts/topological-qft.md) —— 只依赖流形光滑结构、不依赖度规的量子场论；存在标量超荷 $Q$ 使 $Q^2=0$ 且 $T_{\mu\nu}=\{Q,b_{\mu\nu}\}$，故配分函数与度规无关。
- [拓扑扭化](concepts/topological-twist.md) —— 把自旋群对角嵌入自旋群×R-对称群，重新分解超荷表示，使某个超荷成为标量并平方为零；不是截断，理论仍是同一个 $\mathcal N=4$。

**推导卡**

- [典范参数 Ψ：定义、S 作用与消去 t](derivations/canonical-parameter.md) —— 从拓扑项系数 eq (3.49) 出发，把 $t$ 与 $\tau$ 的组合定义为 $\Psi$ eq (3.50)；作用量写成 $I=\delta_tV+(i\Psi/4\pi)\int\mathrm{Tr}F\wedge F$，再用 $\delta'_t=\delta_t/\sqrt{1+t^2}$ 证明物理只依赖 $\Psi$，$S,T$ 在 $\Psi$ 上是 Möbius 变换。
- [一族拓扑场论：t ∈ CP¹ 与 Q² = 0](derivations/one-parameter-family.md) —— 从 GL 扭化留下的两个不变超荷出发，把 $Q=uQ_\ell+vQ_r$ 射影化为 $t=v/u\in\mathbb{CP}^1$；$Q$-不变方程化为 eq (3.29) 的椭圆方程组，$t=\pm i$ 给平坦联络、实 $t$ 给实椭圆族，故得到一整族 TQFT。
- [Ψ 的特殊点与为什么必须是 GL 扭化](derivations/psi-special-points.md) —— 从 $\Psi$ eq (3.50) 读出特殊点：$t=\pm i$ 给 $\Psi=\infty$ 且与 $\tau$ 无关，$t=\pm1$ 给 $\Psi=\mathrm{Re}\,\tau$，$|t|=1$ 给实 $\Psi$；逆式 eq (3.52) 说明弱耦合下 $t\to\pm1$，定向反转给 $\Psi\to-\Psi$。
- [GL 扭化的构造：选哪个 Spin(4)](derivations/twist-construction.md) —— 从弯曲四维流形上需要标量超荷出发，选同态 $\kappa$ 把 $\mathrm{Spin}(4)$ 嵌入 $\mathrm{Spin}(6)$，使 4 与 6 按 $(2,1)\oplus(1,2)$ 与 $(2,2)\oplus(1,1)$ 分解，得到不变旋量 $\varepsilon_\ell,\varepsilon_r$ 与标量超荷 $Q=uQ_\ell+vQ_r$。
- [Q-不变方程与消失定理](derivations/vanishing-theorem.md) —— 从 eq (3.29) 出发，用恒等式 eq (3.32) 与 eq (3.33)、(3.34) 证明：紧致无边四维流形上若 $\int\mathrm{Tr}F\wedge F\neq0$，则除 $t=0,\infty$ 外无解；且在一个 $t$ 有解则对所有 $t$ 有解，解为平坦 $G_{\mathbb C}$ 联络。

## 轨道 C · 舞台：曲线与模空间


**概念卡**

- [复结构](concepts/complex-structure.md) —— 切丛上满足 $I^2=-1$ 且可积的自同态；B-模型只依赖一个复结构，而 $M_H$ 上有一整族由 $S^2$ 参数化的复结构，扭化参数正是选它的参数。
- [希格斯丛](concepts/higgs-bundle.md) —— 曲线 $C$ 上的对 $(E,\varphi)$：$E$ 是 $G$-丛，希格斯场 $\varphi\in H^0(C,K_C\otimes\mathrm{ad}E)$；稳定对构成 $M_H$ 在复结构 $I$ 下的模型。
- [希格斯场](concepts/higgs-field.md) —— 紧化后在 $C$ 上留下的 $(1,0)$-形式场 $\varphi$，即 $K_C\otimes\mathrm{ad}E$ 的全纯截面；它与联络 $A$ 一起编码 Hitchin 方程，并在复结构 $J$ 下与 $A$ 合成平坦 $G_{\mathbb C}$ 联络。
- [Hitchin 纤维化](concepts/hitchin-fibration.md) —— 把 $(E,\varphi)$ 送到 Casimir 不变量的映射 $\pi:M_H\to B$：底与一般纤维的复维都占一半、一般纤维是复环面，使其成为完全可积系统，也是 SYZ 镜像的几何基础。
- [Hitchin 模空间](concepts/hitchin-moduli.md) —— Hitchin 方程 $F-\varphi\wedge\varphi=0,\ D\star\varphi=0$ 的解模规范群得到的空间 $M_H(G,C)$：复维 $(2g-2)\dim G$ 的超凯勒流形，是紧化后二维 sigma 模型的靶空间。
- [超凯勒流形](concepts/hyperkahler-manifold.md) —— 带三个复结构 $I,J,K$（满足四元数关系）与相容度量、且三个辛形式都闭的流形；超凯勒性使同一流形上有一整族复结构，是二维 A/B 模型可以互换的几何前提。
- [超凯勒商](concepts/hyperkahler-quotient.md) —— 对超凯勒流形取三个矩映射同时为零、再模去群作用，得 $X/\!/\!/H=\vec\mu^{-1}(0)/H$；它自动继承超凯勒结构，$M_H=\mathcal W/\!/\!/G$ 是主要例子。
- [可积系统](concepts/integrable-system.md) —— 有足够多（半维数）两两 Poisson 交换的 Hamilton 量的辛流形；$M_H$ 在复结构 $I$ 下完全可积，等值面就是 Hitchin 纤维，一般纤维是紧复环面。
- [矩映射](concepts/moment-map.md) —— 群作用在辛流形上给出的守恒量映射 $\mu:X\to\mathfrak h^*$，由 $\iota_{V(\epsilon)}\omega=\delta\mu_\epsilon$ 定义；Hitchin 方程正是三个矩映射同时为零。
- [Riemann 面](concepts/riemann-surface.md) —— 紧致的一维复流形（复代数曲线）；本文取亏格 $g>1$，使半单群 $G$ 的平坦联络一般不可约，它是 Hitchin 方程与几何 Langlands 的共同舞台。

**推导卡**

- [紧化到 Hitchin 方程：M = Σ×C](derivations/compactify-to-hitchin.md) —— 从 $M=\Sigma\times C$ 与尺度分层出发，用 §3.4 的平方和论证说明极小解在 $C$ 上满足 Hitchin 方程 $F-\varphi\wedge\varphi=0$、$D\varphi=D^*\varphi=0$；由此低能有效理论是以 $M_H$ 为靶的二维 sigma 模型。
- [Hitchin 系统的完全可积性与 Lagrange 纤维](derivations/hitchin-integrability.md) —— 从 Hitchin 纤维化 $\pi:M_H\to B$ 出发，用 Casimir 多项式次数算出 $\dim B=\frac12\dim M_H$；再构造 $\frac12\dim M_H$ 个对 $\Omega_I$ Poisson 对易的 $I$-全纯哈密顿量 $H_a$，证明 $M_H$ 在 $I$ 中完全可积、纤维一般为复环面。
- [超凯勒商与三个复结构 I, J, K](derivations/hyperkahler-quotient.md) —— 从场空间 $W$ 的平坦超凯勒度规出发，写出复结构 $I,J,K$ 与矩映射 $\mu_I,\mu_J,\mu_K$；$\mu_I=\mu_J=\mu_K=0$ 模去规范群即 $M_H=W///G$，而 $I$、$J$ 中的全纯条件分别给出 Hitchin 对与平坦 $G_{\mathbb C}$ 联络。
- [M_H 上的 sigma 模型数据与维数公式](derivations/mh-sigma-data.md) —— 从二维有效理论出发，确定 $M_H$ 上的度规与 $B$-场：物理度规是 $\mathrm{Im}\,\tau$ 倍的自然度规 eq (4.15)，$B$-场是 $-\mathrm{Re}\,\tau\,\omega_I$ eq (4.19)；并得到复维 $(2g-2)\dim G$ 与 Hitchin 纤维化的半维数公式。

## 轨道 D · 二维、膜与算子


**概念卡**

- [A-膜](concepts/a-brane.md) —— A-模型的边界条件：支撑上保留 A-型超荷，要求 Lagrange（$\omega|_N=0$）或余各向同性，并配平坦 Chan–Paton 丛；支撑维数至少是中维。
- [A-模型（A 扭化 sigma 模型）](concepts/a-model.md) —— 把二维 sigma 模型按一对复结构 $(J_+,J_-)$ 扭化、取 $J_+=-J_-=J$ 得到的拓扑模型；它只依赖辛形式 $\omega_J$，在本文 $\Psi=0$ 处出现。
- [B-膜](concepts/b-brane.md) —— B-模型的边界条件：支撑是复子流形、Chan–Paton 丛全纯；它与 A-膜在 S-对偶下互换，零膜与空间充满全纯丛都是 B-膜。
- [B-模型（B 扭化 sigma 模型）](concepts/b-model.md) —— 取 $J_+=J_-=\hat J$ 的扭化；方程合成 $(1-\mathrm i\hat J)\dd\Phi=0$ 故映射为常数，模型只依赖复结构 $\hat J$，在 $\Psi=\infty$ 处出现。
- [特征膜（eigenbrane）](concepts/eigenbrane.md) —— 线算子的特征膜：存在向量空间 $V$ 使 $XB\simeq B\otimes V$；特征值是向量空间而非数，交换的算子可同时有特征膜，$V$ 随基点连成平坦丛。
- [镜像对称（本文版本）](concepts/mirror-symmetry.md) —— 二维 sigma 模型的等价：A-模型与 B-模型互换。本文中 S-对偶把它实现为 $B_J(M_H(G))\cong A_K(M_H({}^LG))$，再复合 $I$ 得 $J$ 中的镜像对。
- ['t Hooft 算子](concepts/thooft-operator.md) —— 规范理论的 disorder 算子：指定经典场奇点再积分；$U(1)$ 时按磁荷 $m$ 分类，一般群按 $^L G$ 的不可约表示 $^L R$ 分类，记 $T(^L R,S)$。
- [Wilson 算子](concepts/wilson-operator.md) —— 规范理论的 order 算子 $\mathrm{Tr}_R P\exp(-\oint(A+\mathrm i\phi))$，在 $\Psi=\infty$ 处拓扑不变；作用在膜上即把 Chan–Paton 丛扭上 $E_q(R)$。

**推导卡**

- [特征膜：XB ≅ B ⊗ V 与同时对角化](derivations/eigenbranes.md) —— 线算子 $X$ 贴近边界把 $B$ 变成 $XB$；若 $XB\cong B\otimes V$ 就称 $B$ 为特征膜。不同点的算子自动交换，故可同时对角化；Wilson 与 't Hooft 侧的 OPE 分别生成 $\mathrm{Rep}(G)$ 与预期的 $\mathrm{Rep}({}^LG)$。
- [折叠：线算子变成边界条件](derivations/folding.md) —— 线算子把 $C$ 分成 $Y$、$Z$ 两块；翻转 $Z$ 的定向并折叠后，线成为 $(Y,Z)$-膜即新的边界条件，两边界之间的态空间 $H_{B_1,B_2}$ 是双模，$H_{B,B}$ 则是边界局部算子代数。
- [广义复几何：A/B 与 B-场的统一语言](derivations/generalized-complex.md) —— 用广义复结构 $\mathcal I$ 统一两类拓扑模型：$I_J$ 给 B-模型、$I_\omega$ 给 A-模型；$B$-场是 $M(B_0)$ 的共轭作用，约化族的 $I_t$ 只依赖 $J,\omega_I,\omega_K$，复化 Kähler 类写成 $[\omega_I]\Psi$。
- [Wilson 与 't Hooft 线算子及其分类](derivations/line-operators.md) —— 把 Wilson 与 't Hooft 线算子统一为保半超对称的算子：Wilson 由表示 $R$ 标号、't Hooft 由 $\rho:U(1)\to G$ 即 ${}^L\!R$ 标号；它们把边界 $B$ 变成 $XB$，OPE 分别生成 $\mathrm{Rep}(G)$ 与（预期）$\mathrm{Rep}({}^LG)$。
- [S-对偶 = 镜像对称（全文心脏）](derivations/sdual-mirror.md) —— $S$ 在参数 $\Psi$ 上作用为 $\Psi\mapsto-1/(n_g\Psi)$，交换 B-模型与 A-模型并把 $G$ 换成 ${}^LG$；复合复超凯勒旋转 $I:\varphi\mapsto\ii\varphi$ 后得到镜像对称，几何上是 SYZ 的纤维 T-对偶，膜层面交换零膜与 type F 膜。
- [二维理论：B-模型、A-模型与不变量 q](derivations/two-d-theories.md) —— 四维规范理论在 $\Sigma\times C$ 上约化得到一族二维理论，由 $CP^1_h\times CP^1_h$ 中一点标记；其不变量 $q=w_+/w_-=-t^2$ 区分 B-模型、A-模型与退化点。

## 轨道 E · Langlands 与翻译器


**概念卡**

- [仿射 Grassmannian](concepts/affine-grassmannian.md) —— 把丛在一点外固定平凡化后，Hecke 修改的空间就是仿射 Grassmannian $\mathrm{Gr}_G=G_{\mathbb C}((z))/G_{\mathbb C}[[z]]$；权 $^Lw$ 标号其 Schubert 胞腔。
- [Bogomolny 方程](concepts/bogomolny-equation.md) —— 三维单极子方程 $F=\star\dd_A\phi$；在 $\mathbb R\times C$ 上给定左右边界条件后，其解空间模规范等于 Hecke 修改空间。
- [典范余各向同性膜（c.c. 膜）](concepts/canonical-coisotropic-brane.md) —— 空间充满的 rank-1 A-膜，曲率由几何唯一决定：$F=(\Im\tau)\omega_J$ 且 $(\omega^{-1}F)^2=-1$；开弦代数是微分算子，是 §11 的翻译器。
- [D-模](concepts/d-module.md) —— 微分算子层上的模，几何 Langlands 的右端。本文论证 $K$ 中每张 A-膜给出 $\mathcal D_{K_M^{1/2}}$ 的模层，$\Psi=h$ 时就是普通 D-模。
- [几何 Langlands 对应](concepts/geometric-langlands.md) —— 曲线 $C$ 上的几何对应：$^L G$ 的局部系统对应 $\mathrm{Bun}_G$ 上的 Hecke 特征 D-模；本文用扭化 $\mathcal N=4$ 的膜范畴给它一个物理来源。
- [Hecke 特征层](concepts/hecke-eigensheaf.md) —— $\mathrm{Bun}_G$ 上的层 $\mathcal F$，被 Hecke 算子作用后满足 $\mathbb H_x^V(\mathcal F)\cong V\otimes\mathcal F$；它是几何 Langlands 中局部系统那一端的像。
- [Hecke 算子](concepts/hecke-operator.md) —— Hecke 算子：在曲线一点 $z$ 处把丛按权 $^Lw$ 修改，对应 $\mathrm{Bun}_G\times\mathrm{Bun}_G$ 中的 Hecke 对应；本文说明 't Hooft 算子的作用就是它。
- [局部系统](concepts/local-system.md) —— 曲线 $C$ 上的局部常值层，等价于基本群表示 $\pi_1(C)\to G_{\mathbb C}$；电特征膜的特征值 $V_p$ 正拼成这样的局部系统。

**推导卡**

- [c.c. A-膜、开弦代数与 A-膜→D-模](derivations/a-to-dmod.md) —— c.c. 膜是 $(A,B,A)$ 型自对偶 A-膜；$K$ 中 A-膜与它之间的开弦态是 $D_{K^{1/2}}$ 模，于是每个 $K$ 中 A-膜给出一个 D-模：无世界面瞬子，例中平坦 $(B,A,A)$ 膜给 $K_M^{1/2}$ 的全纯截面。
- [三类膜回到四维：§12 检查表](derivations/back-to-4d.md) —— 回到四维半空间 $\mathbb R^2_+\times C$：用对合 $T$ 猜费米子边界条件，由 $\delta\lambda$ 推出玻色条件，再检验超流法向消失，得到 $(B,B,B)$ 零膜、$(B,A,A)$ Hitchin 纤维与 $(A,B,A)$ c.c. 膜三类边界条件。
- [单极子冒泡、辛商与 OPE 代数](derivations/bubbling-ope.md) —— 把 Hecke 修改空间实现为 Bogomolny 方程的辛商 $Z=C_0/G_\mathbb C$；单极子冒泡使权退化 $(m+1,m-1)\to(m,m)$ 并给出 OPE 的额外项，几何上是卷积分解 $\pi_*(IC(w)\star IC(w'))=IC(w+w')\oplus\oplus_\alpha\tilde N_\alpha\otimes IC(w_\alpha)$。
- [中心 Z、离散 flux 与 S-对偶的作用](derivations/center-and-flux.md) —— 中心 $Z=\Lambda^\vee/\Lambda$ 通过完美配对 $\Upsilon$ 控制 't Hooft 算子的相位；紧流形上的离散 flux $(e,m)$ 与 $S$ 的作用 $(e,m)\mapsto(-m,e)$ 把理论分成电、磁两类分支。
- [电特征膜 = 平坦 ^LG_C 联络](derivations/electric-eigenbranes.md) —— 用 universal Higgs bundle 拉回的联络 $A+\ii\varphi$ 构造电特征膜；关键等式 $U_x\otimes E_q(R)=U_x\otimes E_q(R)|_x$ 说明零膜是电特征膜，其特征值是 $C$ 上的平坦 ${}^LG_\mathbb C$ 丛在 $x$ 的纤维。
- [Hecke 修改空间、仿射 Grassmannian 与 Schubert 胞腔](derivations/grassmann-schubert.md) —— Hecke 修改空间是仿射 Grassmannian $Gr_N=GL(N,\mathbb C((z)))/GL(N,\mathbb C[[z]])$ 中对应的 Schubert 胞腔，维数 $\Delta_{{}^Lw}=\sum_{i<j}(a_i-a_j)$；紧化需加入关联表示，minuscule 权给光滑紧空间。
- [Ψ ≠ 0：λ-连接与扭化 D-模](derivations/psi-lambda.md) —— 实 $\Psi$ 时 Hitchin 纤维不再是合法 A-膜；扭化后的 c.c. 膜把全纯结构旋转 $q$，纤维坐标变成 $\lambda=\ii\tan(q/2)$ 的 λ-连接，于是 D-模按 $\Psi$ 加权并写成 $D_{L^{\Psi-h}}$。
- ['t Hooft 算子的 Hecke 修改：U(1) 到 U(N)](derivations/toofty-hecke.md) —— 't Hooft 算子在 Higgs 丛上实现 Hecke 修改：$U(1)$ 时 $L_+\cong L_-\otimes O(p_0)^m$，$U(N)$ 时逐 $L_i\mapsto L_i\otimes O(p_0)^{m_i}$；磁荷数组 ${}^L\!w$ 同时是 Hecke 权与仿射 Grassmannian 中 Schubert 胞腔的标号。
- [universal bundle 的障碍与 twisted 丛](derivations/twisted-bundles.md) —— universal bundle 的粘接障碍由 $\zeta=\xi(E_{ad})\in H^2(W,Z)$ 度量；$\zeta$ 分解为三部分，$m_0$ 决定 $M_H(G_{ad})$ 的分支、$e_0$ 给出平坦 $B$-场与 twisted Chan-Paton 丛，$S$ 交换 $(e_0,m_0)$。
