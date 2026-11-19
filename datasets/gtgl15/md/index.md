# Witten 2015（gtgl15）资料卡索引

共 40 张：概念卡 30 张、推导卡 10 张。


## 轨道 A · Hitchin 几何与谱曲线


**概念卡**

- [阿贝尔化与 Prym 簇](concepts/abelianization-prym.md) —— 阿贝尔化把希格斯丛 $(E,\varphi)$ 换成谱曲线上的线丛 $\mathcal L$（$E=\psi_*\mathcal L$），于是 Hitchin 一般纤维落在 $D$ 的 Prym 簇里。
- [特选截面](concepts/distinguished-section.md) —— 特选截面 $\zeta:\mathcal V\to\MH$ 在每个 Hitchin 纤维里挑一个“标准”稳定希格斯丛（opers 的版本），$SU(2)$ 时 $\varphi$ 写成 companion 矩阵。
- [希格斯丛与希钦对](concepts/higgs-bundle.md) —— 希格斯丛是复曲线 $C$ 上全纯丛 $E$ 与取值于 $K$ 的希格斯场 $\varphi$ 组成的对，它同时是希钦方程解与谱曲线几何的载体。
- [希钦方程](concepts/hitchin-equations.md) —— 希钦方程把希格斯场与酉联络耦合起来：$F_{z\bar z}-[\varphi_z,\varphi_{\bar z}]=0$ 且 $\varphi$ 全纯，是二维自对偶方程在紧黎曼面上的形式。
- [希钦纤维化](concepts/hitchin-fibration.md) —— 希钦纤维化 $\pi:\MH\to\mathcal V$ 把希格斯丛映到其特征多项式，是 $\MH$ 上的完全可积系统；一般纤维是复环面，维数恰为 $\MH$ 的一半。
- [希钦模空间 $\MH$](concepts/hitchin-moduli.md) —— $\MH$ 是 $C$ 上稳定希格斯丛的模空间，也是希钦方程解模去规范群的结果；它是复维 $2(g-1)\dim G$ 的非紧完备超凯勒流形。
- [超凯勒商与复结构 I、J、K](concepts/hyperkahler-quotient.md) —— $\MH$ 是平坦超凯勒空间 $\mathcal W=T^*\mathcal Y$ 对规范群 $G$ 的超凯勒商；三个复结构 $I,J,K$ 分别把 $\MH$ 读成希格斯丛、平坦联络和第三种模型。
- [完全可积性与对易哈密顿量](concepts/integrable-system.md) —— $\MH$ 上有 $\frac12\dim_\mathbb{C}\MH$ 个 $I$-全纯、两两对易的哈密顿量（Casimir 乘上同调类积分），构成 Hitchin 完全可积系统。
- [核线丛与余核线丛](concepts/kernel-cokernel.md) —— 沿谱覆盖，$\varphi-y$ 的核给出本征向量线丛 $\mathcal N$，余核给出线丛 $\mathcal L$；两者由 $\mathcal L\cong\mathcal N(\mathcal R)\cong\mathcal N\otimes\psi^*K^{N-1}$ 相联系。
- [谱覆盖、判别式与分歧除子](concepts/spectral-cover.md) —— 谱覆盖 $D\to C$ 的分歧轨迹由判别式 $\Delta(\varphi)\in H^0(C,K^{N(N-1)})$ 刻画，一般有 $2N(N-1)(g-1)$ 个分歧点；$K^{1/2}$ 的选取影响纤维的典范结构。
- [谱曲线](concepts/spectral-curve.md) —— 谱曲线 $D\subset K$ 由 $\det(y-\varphi)=0$ 定义，是 $C$ 上的 $N$ 重覆盖；它把希格斯丛的几何翻译成 $D$ 上线丛的几何。
- [稳定丛模空间与余切丛](concepts/stable-locus.md) —— $\varphi=0$ 把稳定全纯丛模空间 $\mathcal M$ 嵌入 $\MH$，成为 $I$-全纯 Lagrangian 子流形；其余切丛 $T^*\mathcal M$ 在 $\mathcal M$ 附近开嵌入 $\MH$。

**推导卡**

- [维数计数：$\sum(2d_i-1)=\dim G$](derivations/dimension-count.md) —— 由 $\dim H^0(C,K^d)=(2d-1)(g-1)$ 与 Casimir 次数和 $\sum_i(2d_i-1)=\dim G$，得 $\dim\mathcal V=(g-1)\dim G=\frac12\dim_\mathbb{C}\MH=\dim F$。
- [希钦方程 = 超凯勒矩映射商](derivations/hitchin-as-moment-map.md) —— Hitchin 方程是 $\mathcal W=T^*\mathcal Y$ 上超凯勒矩映射 $(\nu_I,\nu_J,\nu_K)$ 的零点条件模去复规范群 $\mathcal G_\mathbb{C}$，故 $\MH=\mathcal W/\!/\!/\mathcal G$。
- [核与余核线丛的关系 $\mathcal L\cong\mathcal N(\mathcal R)$](derivations/kernel-cokernel-relation.md) —— 用 $2\times2$ 局部模型 $\varphi\sim\bigl(\begin{smallmatrix}0&z\\1&0\end{smallmatrix}\bigr)$、$y^2=z$ 显式算出核线丛 $\mathcal N$ 与余核线丛 $\mathcal L$ 相差分歧除子：$\mathcal L\cong\mathcal N(\mathcal R)\cong\mathcal N\otimes\psi^*K^{N-1}$。
- [一般纤维的阿贝尔化：$F\cong\mathrm{Prym}(D/C)$](derivations/prym-abelianization.md) —— 利用非分歧点的本征分解 $E_p=\bigoplus_i\mathcal L_{q_i}$ 与推前 $E=\psi_*\mathcal L$，一般纤维是 $\mathrm{Prym}(D/C)$ 的 torsor，维数吻合。
- [谱曲线亏格与分歧点计数](derivations/spectral-genus.md) —— 由 Riemann–Hurwitz 与判别式次数，$g_D=g_C+(N^2-1)(g-1)$，分歧点数为 $2N(N-1)(g-1)$。

## 轨道 B · 对偶环面与 T-对偶


**概念卡**

- [对偶环面纤维化与 T-对偶](concepts/dual-torus-fibration.md) —— $\MH$ 的每个 Hitchin 纤维是复环面 $F$，其对偶环面 $F'$ 给出镜像一侧的纤维化；4d $\mathcal N=4$ 的 S-对偶表现为纤维上的 T-对偶加底空间对称。
- [辛形式 $\Omega_I$ 与耦合常数](concepts/symplectic-form.md) —— $\MH$ 上有全纯辛形式 $\Omega_I=\frac1\pi\int_C\operatorname{Tr}\delta\varphi_z\wedge\delta A_z$，且 $\Omega_I=\omega_J+i\omega_K$；它决定纤维上的辛结构和对偶的周期匹配。
- ['t Hooft flux 与 $PSU(N)$ 分量](concepts/thooft-flux-psu.md) —— $PSU(N)=SU(N)/\mathbb Z_N$ 的希格斯丛按 't Hooft flux $\xi\in H^2(C,\mathbb Z_N)$ 分成 $N$ 个分量，其 Hitchin 纤维是 $\mathrm{Pic}$ 模掉 $\mathrm{Jac}(C)$。

**推导卡**

- [辛形式的周期匹配与 $S$-对偶 $=$ $T$-对偶](derivations/symplectic-period-matching.md) —— 用谱曲线写出 $\Omega_I=\sum dH_a\wedge d\oint_\gamma\omega^a$，纤维坐标由周期给出；$S$-对偶交换 $\tau\leftrightarrow-1/\tau$ 正是把周期与对偶周期互换，即纤维 $T$-对偶。

## 轨道 C · 膜、线算符与本征膜


**概念卡**

- [膜、$A$-膜与 $B$-膜](concepts/branes-ab.md) —— $\MH$ 上的边界条件由膜描述：$B$-膜是复子流形加全纯 sheaf，$A$-膜是 Lagrangian 子流形加平坦 $U(1)$ 联络；超凯勒三个复结构给出 $(B,B,B)$、$(B,A,A)$ 等不同类型。
- [本征膜](concepts/eigenbranes.md) —— 若线算符 $L$ 作用在膜 $B$ 上得到 $LB\cong B\otimes V$（$V$ 是向量空间），则称 $B$ 是本征膜，而“本征值”是向量空间 $V$ 而不是数。
- [电本征膜](concepts/electric-eigenbranes.md) —— 对 Wilson 线同时本征的膜叫电本征膜；零维膜（摩天楼层）是典型例子，Wilson 作用为 $U\mapsto U\otimes E_{H,{}^LR}|_{p\times\MH}$。
- [线算符](concepts/line-operators.md) —— 4d 理论的线算符沿 $\Sigma$ 中的线支撑；在 2d 描述里它成为作用在膜上的局部算符 $L$，把边界条件 $B$ 变成 $LB$。
- [磁本征膜](concepts/magnetic-eigenbranes.md) —— §4 猜测并在 §5 验证：$G$ 侧对 't Hooft 线本征的磁本征膜正是 $F$ 型膜，即 Hitchin 纤维上的秩 1 $A$-膜配平坦 Chan–Paton 线丛。
- [二维 $\sigma$-模型与靶空间 $\MH$](concepts/sigma-model-mh.md) —— 4d $\mathcal N=4$ 规范理论紧致化在 $\Sigma\times C$ 上（$\Sigma$ 很大）给出 2d $\sigma$-模型，靶空间是 $C$ 上希格斯丛的超凯勒模空间 $\MH$；这解释了“2+2=4”。
- [摩天楼层（零维膜）](concepts/skyscraper-zero-brane.md) —— 在 $\MH$ 的一点 $m$ 处的摩天楼层 sheaf 给出零维膜，它是最简单的电本征膜（$(B,B,B)$ 型）；S-对偶把它变成磁侧的 $F$ 型膜。
- [$\mathbf F$ 型膜](concepts/type-f-brane.md) —— $F$ 型膜 = Hitchin 纤维上的秩 1 $A$-膜 + 平坦 Chan–Paton 线丛（flat Spin$^c$ 结构编码它在对偶纤维中的位置），是 §4–§7 中磁本征膜的具体形态。
- [万有丛、万有希格斯丛与陈–帕顿丛](concepts/universal-bundles.md) —— 万有丛 $\mathcal E\to C\times M$ 与万有希格斯丛 $\mathcal E_H\to C\times M_H$ 把一个点处的场编码成向量空间；陈–帕顿丛则是膜上的 sheaf，线算符作用通过它实现。

**推导卡**

- [电本征膜的作用公式与零维膜](derivations/electric-action-formula.md) —— Wilson 线作用为 $U\mapsto U\otimes\mathcal E_{H,{}^LR}|_{p\times\MH}$；零维膜是电本征膜，因为该限制在点上只是固定向量空间。

## 轨道 D · 't Hooft 算符与赫克修正


**概念卡**

- [赫克修正与赫克变换](concepts/hecke-modification.md) —— 赫克修正在单点 $p$ 处改变全纯丛的局部结构（$E_-\to E_+$）；在谱覆盖上它只是给线丛乘一个 $\mathcal O(q_i)$，并保持特征多项式，从而作用在 Hitchin 纤维上。
- ['t Hooft 算符](concepts/thooft-operator.md) —— 't Hooft 算符是带 Dirac 单极奇点的磁线算符；一般 $G$ 由同态 $U(1)\to G$（GNO 对偶权）分类，在 $\Sigma\times C$ 描述里它变成 $p$ 处的赫克修正。

**推导卡**

- ['t Hooft 算符 $\leftrightarrow$ $p$ 处赫克修正（$U(1)$）](derivations/thooft-hecke-u1.md) —— 以 $U(1)$ 显式单极子解为边界条件，把 3d 超对称方程化成复方程；$[D_1,D_2]=0$ 使全纯结构只在 $p$ 处跳变，故 't Hooft 算符 $=$ 赫克修正 $\mathcal O\mapsto\mathcal O(mp)$。

## 轨道 E · 行列式线丛与本征值


**概念卡**

- [行列式线丛与配对 $\langle\mathcal L,\mathcal M\rangle$](concepts/determinant-line-pairing.md) —— 对 $D$ 上度数 0 的线丛，行列式线丛给出典范配对 $\langle\mathcal L,\mathcal M\rangle=\det H^*(\mathcal L)\otimes\det H^*(\mathcal M)/\det H^*(\mathcal L\otimes\mathcal M)\otimes\det H^*(\mathcal O)$，它是 Poincaré 线丛的 twisted 版本。
- [Gerbe 与 $B$-场（离散电/磁荷）](concepts/gerbe-bfield.md) —— Gerbe 是线丛的上一层对象（局部平凡、两个平凡化差一线丛）；中心非平凡的对偶理论在模空间上带非平凡 gerbe，其平坦 $B$-场编码离散电/磁荷。
- [Pfaffian 线丛与 theta 函数](concepts/pfaffian-theta.md) —— Pfaffian 线丛是行列式线丛在 spin 结构下的“平方根”，其截面给 theta 函数；$K^{1/2}$ 的选取（偶 $N$）与它对偶侧的 $Z_2$ gerbe 都由此而来（背景补全，原文未用此名）。

**推导卡**

- [磁本征膜的赫克本征值（$U(1)$ 与 $SU(N)$）](derivations/magnetic-hecke-eigenvalue.md) —— 由对偶把 $F$ 型膜的 Chan–Paton 丛写成 $\langle L,M\rangle$，'t Hooft 作用对应的赫克变换 $M\mapsto M\otimes\mathcal O(p)^{d}$ 给出 $\prod T^{(d_i)}\hat B=\hat B\otimes(\otimes_i L|_{p_i}^{d_i})$；非阿贝尔情形逐本征空间得到同一形式。

## 轨道 总览


**概念卡**

- [四维 $\mathcal N=4$ 超杨–米尔斯与部分拓扑场论](concepts/n4-sym-partial-tqft.md) —— 底本是 4d $\mathcal N=4$ 超杨–米尔斯（16 超荷、耦合 $\tau$）；它经拓扑扭曲只在“部分”意义下成为拓扑场论：配分函数未必良定义，但膜范畴仍良定义，$\MH$ 非紧需选边界条件。

**推导卡**

- [从 4d $\mathcal N=4$ 到 2d $\sigma$-模型](derivations/compactify-to-sigma.md) —— 在 $\Sigma\times C$（$\Sigma\gg C$）上紧致化：$C$ 方向零模是 Hitchin 方程解，$\Sigma$ 方向有效理论是靶为 $\MH$ 的 2d $\sigma$-模型。
