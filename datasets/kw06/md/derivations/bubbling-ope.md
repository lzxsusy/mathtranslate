# 单极子冒泡、辛商与 OPE 代数

> `kw/deriv/bubbling-ope` · 轨道 E · Langlands 与翻译器 · 状态 dev · 11 步

> **要回答的问题**：Hecke 修改空间怎样实现为 Bogomolny 模空间，单极子冒泡在 OPE 中扮演什么角色？

## 一句话

把 Hecke 修改空间实现为 Bogomolny 方程的辛商 $Z=C_0/G_\mathbb C$；单极子冒泡使权退化 $(m+1,m-1)\to(m,m)$ 并给出 OPE 的额外项，几何上是卷积分解 $\pi_*(IC(w)\star IC(w'))=IC(w+w')\oplus\oplus_\alpha\tilde N_\alpha\otimes IC(w_\alpha)$。

## 目标

从边界条件与矩映射得到辛商 $Z=C_0/G_\mathbb C$，说明冒泡与 OPE 的修正项，并把结论提升为 Hecke 特征层。

## 前提

- B p.152 eq (10.1)：线性化 Bogomolny 方程与边界条件给出椭圆复形。
- B p.161 eq (10.19)：矩映射 $\mu(\varepsilon)=\int_W\mathrm{Tr}\,\varepsilon(F_{23}-hD_y\varphi_0)+\int_{\partial W}\mathrm{Tr}\,\varepsilon\varphi_0\,h$。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 在 $W=I\times C$ 上取边界条件：左端 $C_-$ 固定 $A_-$（Dirichlet）而 $\varphi_0$ 自由；右端 $C_+$ 令 $\varphi_0=0$，于是协变 Neumann 条件 $\iota_nF=0$ 出现。 | 两种边界条件正好对应上一节两个方向的选择，后面才知道它们把解空间切成 Hecke 修改的两端。 | `B p.152` | A·原文明确写了 |
| 2 | 线性化 Bogomolny 方程加边界条件得到椭圆复形 (10.1)，其指标给出光滑点的维数：$\dim Z=\mathrm{index}$。 | 这是把无穷维方程的解空间变成有限维流形的标准手段，也是计算 Hecke 修改空间维数的第一条路线。 | `B p.152 eq (10.1)` | A·原文明确写了 |
| 3 | 没有 't Hooft 算子时由 $\int\mathrm{Tr}(F-\star D\varphi_0)\wedge\star(\cdots)=0$ 及边界项消失得 $F=D\varphi_0=0$；有算子时每个 $T(\rho)$ 贡献 $\Delta_\rho=\sum_k c_k$（(10.4)）。 | 前者说明无算子的解是平坦的，后者把算子贡献加成为维数，二者共同确定 $\dim Z$。 | `B p.155 eq (10.4)` | A·原文明确写了 |
| 4 | 把 Bogomolny 方程改写为 $[D_y-\ii\varphi_0,D_z]=0$、$F_{23}=hD_y\varphi_0$，并取辛形式 $\omega=\int_W\mathrm{Tr}(\delta A_2\wedge\delta A_3-h\delta A_1\wedge\delta\varphi_0)$；矩映射 (10.19) 的 $\mu=0$ 恰好给出这两式加边界条件。 | 这一步把规范场方程翻译成超凯勒商的条件，于是解空间可以按辛几何处理。 | `B p.161 eq (10.19)` | A·原文明确写了 |
| 5 | 两种边界选择（$\varepsilon=0$ 或 $\varphi_0=0$）正是 $C_\pm$，故 $\mu^{-1}(0)$ 上的商就是辛商；由于此处无稳定性问题，辛商等于复商 $Z=C_0/G_\mathbb C$。 | 复商才带有自然的复结构，而 $Z$ 的复结构正是 Hecke 修改空间的复结构。 | `B p.161` | A·原文明确写了 |
| 6 | $Z$ 的复结构沿 $C$ 方向变化（沿 $y$ 只改辛结构、沿 $C$ 只改复结构），因此 $Z$ 的复结构与 Hecke 修改空间一致；这一致性使 Bogomolny 模空间与代数几何的修改空间可以互相比对。 | 两套构造若不一致，后面的 OPE 计算就不能直接搬回 Hecke 侧。 | `B p.161` | A·原文明确写了 |
| 7 | 冒泡：$U(1)$ 以 $(z_1,z_2)\mapsto(e^{\ii\theta}z_1,e^{\ii\theta}z_2)$ 作用在 $\mathbb C^2$，商 $\mathbb C^2/U(1)\cong\mathbb R^3$；等变瞬子可缩成点，形成单极子泡。特征公式 $\chi(E_0')=\chi(E_0)+\chi(H_1)(2-e^{\ii\theta}-e^{-\ii\theta})$ 给出权变 $(m+1,m-1)\to(m,m)$（(10.12)、(10.13)）。 | 冒泡不改变拓扑型却让两个权互相靠拢，这正是 OPE 中同型算子混合的几何机制。 | `B p.157 eq (10.13)` | A·原文明确写了 |
| 8 | OPE 极限：$p'\to p$ 时 $T(w,p)\,T(w',p')\to T(w+w',p')+\sum_i c_iT(w_i,p')$，其中 $w_i$ 是关联权（(10.20)）。 | 这是把冒泡几何翻译成算子乘积展开：主项是权和，修正项来自权退化的中间态。 | `B p.165 eq (10.20)` | A·原文明确写了 |
| 9 | 几何版：blowdown $\pi:Z(w,z,y;w',z,y')\to Z(w+w')$ 下 $\pi_*(IC(w)\star IC(w'))=IC(w+w')\oplus\bigoplus_\alpha\tilde N_\alpha\otimes IC(w_\alpha)$，首项系数一维，且 $\tilde N_\alpha\cong N_\alpha$（(10.33)，依赖 LGMV 定理）。 | 这给出 OPE 的结构常数与相交上同调维数的严格对应，是几何 Langlands 中 Hecke 特征层乘法的核心。 | `B p.178 eq (10.33)` | A·原文明确写了 |
| 10 | 放弃时间反演后取 $\varphi=\varphi_0dx^0+\pi^*\tilde\varphi$、$A=A_0dx^0+\tilde A$，在 $A_y=0$ 规范下退化方程 (10.36) 为 $D_{\bar z}\varphi_z=0$、$\partial_yA_{\bar z}=-\ii D_{\bar z}\varphi_0$、$\partial_y\varphi_z=-\ii[\varphi_z,\varphi_0]$、$F_{z\bar z}-[\varphi_z,\varphi_{\bar z}]=(\ii h/2)\partial_y\varphi_0$。 | 第一式说明每个截面上的 $(E,\varphi)$ 都是 Higgs 丛，后几式说明 $y$ 方向只差规范变换；这是把 Hecke 修改与 Hitchin 纤维联系起来的关键。 | `B p.180 eq (10.36)` | A·原文明确写了 |
| 11 | 于是 $\varphi$ 不能在一个点被任意改动：给定 $y<y_0$ 的全纯 $\varphi$，越过 $y_0$ 后一般会出现极点，Hecke 修改只发生在有限个点；并且 $\varphi$ 的特征多项式与 $y$ 无关，Hecke 变换保持 Hitchin 纤维，故支撑在纤维上的膜是磁特征膜。 | 这把「Hecke 修改作用在片上」升格为「Hecke 变换保持 Hitchin 纤维结构」，正是 §8 磁特征膜预言的内在解释。 | `B p.182` | B·原文暗示、我们补的中间步 |

## 结论

带奇点的 Bogomolny 方程的解空间是辛商 $Z=C_0/G_\mathbb C$，其复结构就是 Hecke 修改空间。单极子冒泡使权 $(m+1,m-1)\to(m,m)$ 退化，从而在 OPE 中产生修正项 $T(w,p)T(w',p')\to T(w+w',p')+\sum c_iT(w_i,p')$。几何上这对应卷积分解 $\pi_*(IC(w)\star IC(w'))=IC(w+w')\oplus\bigoplus_\alpha\tilde N_\alpha\otimes IC(w_\alpha)$，常量由 LGMV 定理保证。§10.5 进一步说明 Hecke 变换保持 Hitchin 纤维，故磁特征膜的预言是自洽的。

## 缺口

- 维数公式 (10.4) 引自 Pauly–Kronheimer，本文未重新证明（B p.155）。
- $\tilde N_\alpha\cong N_\alpha$ 依赖 LGMV 定理，属于数学输入而非本文的物理推导（B p.169、p.178）。
- Hecke 修改是有限集这一说法只对正则半单的 $\varphi(z_0)$ 成立，原文用「strongly suggests」（B p.180-182）。

## 最容易讲错的地方

- 辛商与复商在这里相同只是因为 $\mu^{-1}(0)$ 上无稳定性问题；不要把它当成普遍结论。
- 冒泡不改变拓扑型、只让权退化；不要把冒泡误当成「算子相加」。
- (10.36) 的 $D_{\bar z}\varphi_z=0$、$\partial_yA_{\bar z}=-\ii D_{\bar z}\varphi_0$ 都带横线，文本抽取会丢 bar，必须以原文排版为准。

## 相关卡

[Hecke 修改空间、仿射 Grassmannian 与 Schubert 胞腔](../derivations/grassmann-schubert.md) · ['t Hooft 算子的 Hecke 修改：U(1) 到 U(N)](../derivations/toofty-hecke.md) · [超凯勒商](../concepts/hyperkahler-quotient.md) · [Bogomolny 方程](../concepts/bogomolny-equation.md)

## 出处（印刷页）

- B p.152–182（B p.178 eq (10.33)）

> 说明：steps 的 provenance 分布：A×10、B×1（共 11 步）；gaps 3 条、pitfalls 3 条。
