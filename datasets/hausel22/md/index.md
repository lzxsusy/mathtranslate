# Witten 2015（gtgl15）资料卡索引

共 29 张：概念卡 20 张、推导卡 9 张。


## 轨道 A · 镜像对称与几何 Langlands


**概念卡**

- [几何 Langlands 对应](concepts/geometric-langlands-correspondence.md) —— 几何 Langlands 对应把曲线上的 $\G$-局部系统变成 $\G^\vee$-丛模叠上的 holonomic $D$-模，并要求它是 Hecke 算子的特征层。
- [Hitchin 系统](concepts/hitchin-system.md) —— Hitchin 系统是 Higgs 丛模空间上由特征多项式给出的完全可积系统，一般纤维是阿贝尔簇的主齐性空间。
- [同调镜像对称](concepts/homology-mirror-symmetry.md) —— 同调镜像对称断言镜像两边的边界条件范畴等价：一侧的 Fukaya 范畴等于另一侧凝聚层的导出范畴。
- [Langlands 对偶群 $\G^\vee$](concepts/langlands-dual-group.md) —— 复约化群的 Langlands 对偶就是把根数据里的格与对偶格互换所得的群；它的 Hitchin 系统是原群的镜像。
- [镜像对称（三个方面）](concepts/mirror-symmetry.md) —— 镜像对称把 Calabi–Yau 流形 X 的复几何与镜像流形 Y 的辛几何对应起来；本文按拓扑、同调、SYZ 三个方面使用它。
- [SYZ 镜像对称](concepts/syz-mirror-symmetry.md) —— SYZ 猜想镜像的两个 Calabi–Yau 流形纤维化在同一底上、一般纤维是互为对偶的特殊拉格朗日环面。

**推导卡**

- [从 Hitchin 系统读出 SYZ 对偶纤维化](derivations/syz-from-hitchin.md) —— 把 Hitchin 系统的完全可积性、对偶阿贝尔簇纤维与 $J$ 结构下的特殊拉格朗日性三步拼起来，就得到 SYZ 图景所需的对偶特殊拉格朗日纤维化。

## 轨道 B · 拓扑镜像对称与 Hodge 数


**概念卡**

- [弦性 Hodge 数（$\alpha$-扭）](concepts/stringy-hodge-numbers.md) —— 弦性 Hodge 数是轨形上按不动点分层、带费米子移位与 gerbe 扭转重新组合出的 Hodge 数，用来陈述拓扑镜像对称。
- [拓扑镜像对称](concepts/topological-mirror-symmetry.md) —— 拓扑镜像对称断言 Langlands 对偶的 Hitchin 模空间之间 Hodge 数相等，镜像一侧用弦性 Hodge 数并带 gerbe 扭转。

**推导卡**

- [从混合 Hodge 数到 $\alpha$-扭弦性 Hodge 数](derivations/stringy-hodge-shift.md) —— 把轨形按 $\Gamma$-不动点分层、每层取 $L_\alpha$-扭上同调并作费米子移位，就得到与 $\SL_n$ 侧混合 Hodge 数可比的对象。

## 轨道 C · 增强镜像对称与膜


**概念卡**

- [几何 Langlands 的经典极限 $\mathscr{S}$](concepts/classical-limit-langlands.md) —— 经典极限是把增强镜像对称沿 Hitchin 底作一阶近似，得到 $\M_\Dol$ 与 $\M^\vee_\Dol$ 导出范畴之间的等价。
- [增强镜像对称](concepts/enhanced-mirror-symmetry.md) —— 增强镜像对称 = 同调镜像对称 + 超 Kähler 膜的匹配 + Wilson 算子与 Hecke 算子的交换，三项都来自四维 $S$ 对偶。
- [超 Kähler 膜的四类型](concepts/hyperkahler-branes.md) —— 超 Kähler 流形上，膜对三个复结构 $I,J,K$ 各取 A 型或 B 型；物理上允许的是 $(B,A,A)$、$(A,B,A)$、$(A,A,B)$ 与 $(B,B,B)$ 四种。
- [Kapustin–Witten 的 $S$ 对偶纲领](concepts/kapustin-witten-duality.md) —— Kapustin–Witten 用四维 $N=4$ 理论的 $S$ 对偶约化到二维，把几何 Langlands 对应解释成一种增强镜像对称。

**推导卡**

- [经典极限 $\mathscr{S}$ 与算子的交换](derivations/s-intertwines-operators.md) —— 把式 (3.12) 的交换性与式 (3.14) 的截面结构层对应合并，就得到猜想 3.19 三条的出发点：镜像是向量丛 $\Lambda_\mu$。

## 轨道 D · 幂零锥上的等变重数


**概念卡**

- [Białynicki–Birula 分解与上行流](concepts/bialynicki-birula-attraction.md) —— 在 $\T=\C^\times$ 的半射影作用下，簇按「沿 $\lambda\to0$ 的极限点」分解成上行流，按「沿 $\lambda\to\infty$ 的极限」给出芯。
- [等变重数 $m_\calE(t)$](concepts/equivariant-multiplicity.md) —— 等变重数是用 $\T$-等变 Euler 型写出的比值，对非常稳定 $\calE$ 是系数非负、回文、首一的多项式。
- [局部重数代数 $Q_\calE$](concepts/local-multiplicity-algebra.md) —— $Q_\calE$ 是上行流与幂零锥概形论交的坐标环，分次、有限维、Gorenstein 且满足 Poincaré 对偶。
- [非常稳定 Higgs 丛](concepts/very-stable-higgs-bundle.md) —— 非常稳定指上行流与芯只交于自身；等价地上行流是闭的，且 Hitchin 映射在其上 proper、有限。

**推导卡**

- [$Q_\calE$ 的 Gorenstein 性与 Poincaré 对偶](derivations/gorenstein-multiplicity-algebra.md) —— $h$ 是完备交，故 $Q_\calE$ 是 Artin 完全交，从而是 Gorenstein、有 socle 与 Poincaré 对偶，且 Poincaré 多项式等于 $m_\calE(t)$。
- [非常稳定 $\Rightarrow$ 重数是多项式](derivations/multiplicity-polynomial.md) —— 非常稳定使 Hitchin 映射在流上有限，于是等变 Euler 型比值的分母被约掉，只剩下系数非负、回文、首一的多项式。
- [定理 3.10：$Q_\delta$ 是 Grassmann 上同调环之积](derivations/q-delta-grassmann.md) —— 多步 Hecke 修改在每一点独立地挑一个子空间，既约条件保证交点恰为 Grassmann 之积，于是重数代数分解为上同调环的乘积。
- [非常稳定的四重等价链](derivations/very-stable-chain.md) —— 从「上行流与芯只交于自身」出发，经闭性、$0$-纤维条件，逐步得到 Hitchin 映射在流上的 proper 性与有限性。

## 轨道 E · 仿射 Grassmannian 与重数代数


**概念卡**

- [仿射 Grassmannian $\Gr$](concepts/affine-grassmannian.md) —— $\Gr=\GL_n((z))/\GL_n[[z]]$ 是按支配权分层的射影 ind 概形；极小权 $\omega_k$ 的层就是经典 Grassmann 簇。
- [jet 概形 $J_d(X)$](concepts/jet-scheme.md) —— $J_d(X)$ 是 $X$ 上 $d-1$ 阶 jet 的模概形，其 $\C$-点是从 $\Spec\C[z]/(z^d)$ 到 $X$ 的映射；它是猜想 3.12(4) 里的核心对象。
- [拉格朗日闭包 $\overline{\overline{W^+_\calE}}$](concepts/lagrangian-closure.md) —— 拉格朗日闭包是包含该上行流的最小闭上行流之并，即按 BB 分解取商后的闭包；定理 3.18 把它算成不大于 $\mu$ 的流的并。

**推导卡**

- [Hecke 修改把仿射 Grassmannian 嵌入上行流](derivations/hecke-to-wobbly.md) —— 在 $\Gr^\mu$ 中取点并作 Hecke 修改，得到 Hitchin 截面里的新点；合法修改的条件把 $\calH^\mu$ 变成 $W^+_{\delta^\mu_c}$ 上的同构。
- [$n=2$ 时的三个重数代数与 jet 概形](derivations/jet-scheme-n2.md) —— $n=2$、$\mu=(d+1)\omega_1$ 时，重数代数被显式写成三个商环，它们分别是 $\P^1$ 上同调环、其一次形变与二次形变。

## 轨道 总览


**概念卡**

- [总览：幂零锥尖端的增强镜像对称纲领](concepts/enhanced-mirror-program.md) —— 本文第一部分综述 Langlands 对偶 Hitchin 系统之间的镜像对称，第二部分在幂零锥上引入重数代数并猜想其镜像对应物。
