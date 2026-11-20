# 资料卡队列 · SY01-26《镜像对称与代数几何》(Cox–Katz)

按《13 · 概念资料卡建设规范》立项。判据：①跨文献反复出现（Cox–Katz 全书 + Batyrev/Givental/Kontsevich/Morrison–Plesser/Dubrovin 等原始文献）；②教材分散（本书只给节内定义，完整链条要拼 2 本以上）；③有形式化落点（结构体/定理陈述级）；④有可算最小例子（五次三维簇、$\mathbb{P}^4$ 中的五次超曲面、$\mathbb{P}^1$ 情形等）。

分层：`L0` 几何/Hodge 基础；`L1` 量子上同调与 Gromov–Witten；`L2` 镜像构造与物理侧。

| id | zh | en | layer | prereqs | 主要书内位置 | 可算最小例子 |
|---|---|---|---|---|---|---|
| MS-01 | 镜像对称 | mirror symmetry | L2 | MS-04, MS-10 | 第 1 章 §1.1–1.3；第 2 章 §2.1 | 五次三维簇 $X_5\subset\mathbb{P}^4$ 与其镜像族 $\check X$ |
| MS-02 | 镜像映射 | mirror map | L2 | MS-01, MS-06 | 第 2 章 §2.4–2.5；第 6 章 | $q=c_1(x-770x^2+\cdots)$，$c_1=-1$ |
| MS-03 | 五次三维簇 | quintic threefold | L0 | — | 第 1 章 §1.4；第 2 章 | $X_5=\{x_0^5+\cdots+x_4^5=0\}\subset\mathbb{P}^4$ 的 $h^{1,1}=1,h^{2,1}=101$ |
| MS-04 | 量子上同调 | quantum cohomology | L1 | MS-05 | 第 6–7 章 | $QH^*(\mathbb{P}^n)$ 的环结构 $\mathbb{Z}[p]/(p^{n+1})-q$ |
| MS-05 | Gromov–Witten 不变量 | Gromov–Witten invariant | L1 | MS-15 | 第 7 章 §7.1–7.4 | 亏格 0、次数 $d$：$N_d$；$\mathbb{P}^2$ 中过 $3d-1$ 点的 $d$ 次曲线数 |
| MS-06 | Picard–Fuchs 方程 | Picard–Fuchs equation | L1 | MS-09 | 第 5 章 §5.1.2；第 2 章 | 五次超曲面 4 阶方程 (2.8) |
| MS-07 | 环面簇 | toric variety | L0 | MS-08 | 第 3 章 §3.1–3.4 | $\mathbb{P}^2$ 由三个射线的扇给出；$X_\Sigma$ 的 Chow 群 |
| MS-08 | 扇与多胞形 | fan and polytope | L0 | — | 第 3 章 §3.1–3.2 | $\Delta\subset\mathbb{R}^2$ 的极多胞形 $\Delta^\circ$；法扇 $\Sigma_\Delta$ |
| MS-09 | 自反多胞形 | reflexive polytope | L1 | MS-08 | 第 4 章 §4.1–4.3 | 二维 16 个自反多胞形；三维 4319 个（Batyrev） |
| MS-10 | Hodge 结构与滤过 | Hodge structure and filtration | L0 | — | 第 5 章 §5.1；前言 | 椭圆曲线 $H^1$ 的权 1 Hodge 结构 |
| MS-11 | Hodge 结构变分 | variation of Hodge structure | L1 | MS-10 | 第 5 章 §5.1.1 | 五次族的 $F^3\subset H^3$；Gauss–Manin 联络 |
| MS-12 | 单值性与最大幺幂 | monodromy and maximally unipotent | L1 | MS-11 | 第 5 章 §5.1.2–5.2；第 3 章 | 单参数族的 $T=I+N$，$N^2=0$；MUM 点 |
| MS-13 | 单值性定理与极限混合 Hodge 结构 | monodromy theorem and limiting mixed Hodge structure | L1 | MS-12 | 第 5 章 §5.1.3–5.1.4 | $m\ge0$ 使 $(T^m-I)^{n+1}=0$；极限滤过 $F^\bullet_{\lim}$ |
| MS-14 | 消失圈 | vanishing cycle | L1 | MS-12 | 第 5 章 §5.1.2；第 3 章 §3.5 | 五次族在锥形奇点处的 3-圈；Picard–Lefschetz 公式 |
| MS-15 | 稳定映射与虚基本类 | stable maps and virtual fundamental class | L1 | MS-16 | 第 7 章 §7.1–7.2 | $\overline{\mathcal M}_{0,3}(\mathbb{P}^1,1)$ 的 3 个点 |
| MS-16 | 预稳定曲线与模空间 | prestable curves and moduli | L1 | — | 第 7 章 §7.1 | $\overline{\mathcal M}_{0,4}\cong\mathbb{P}^1$ |
| MS-17 | 局部化与等变上同调 | localization and equivariant cohomology | L1 | MS-15 | 第 9 章 §9.1 | $\mathbb{P}^1$ 上的 $\mathbb{C}^*$ 作用，Atiyah–Bott 公式 |
| MS-18 | Frobenius 流形与 Dubrovin 联络 | Frobenius manifold and Dubrovin connection | L1 | MS-04, MS-11 | 第 8 章 | 五次族的 3 点函数 $\langle\phi_i\phi_j\phi_k\rangle$；WDVV |
| MS-19 | 量子超平面截面原理 | quantum hyperplane section principle | L1 | MS-04, MS-18 | 第 8 章 §8.5 | $\mathbb{P}^4$ 中五次超曲面的 GW 数 vs 环境空间的相对 GW 数 |
| MS-20 | 非线性 σ 模型与超共形场论 | nonlinear sigma model and SCF | L2 | MS-01 | 第 1 章 §1.1；附录 B | 世界面 $\Sigma$ 上的 $(2,2)$ SCF；$c=9$ |
| MS-21 | 规范线性 σ 模型与相 | gauged linear sigma model and phases | L2 | MS-20, MS-07 | 附录 B §B.5（PDF p.451–453）；§12.2 亦提及 | $\mathbb{P}^4$ 的 GLSM 在 $r\gg0$ / $r\ll0$ 的两相 |
| MS-22 | 极端跃迁与锥形奇点跃迁 | extremal and conifold transitions | L2 | MS-09, MS-21 | 第 3 章 §3.5；第 6 章 §6.4 | 五次族的锥形奇点跃迁；$b_3: 204\to202$ |
| MS-23 | nef 分拆与 Batyrev 镜像构造 | nef partition and Batyrev construction | L2 | MS-09 | 第 4 章 §4.5 | 五次三维簇：$\Delta$ 的 nef 分拆 $\nabla_0=\{0\},\nabla_1=\Delta$ |
| MS-24 | Berglund–Hübsch 转置与轨形镜像 | Berglund–Hübsch transpose and orbifold mirror symmetry | L2 | MS-23 | 附录 A；第 12 章 | Fermat 五次：$x_0^5+\cdots+x_4^5$ 的转置仍是五次；$\mathbb{Z}_5^3$ 轨形 |

## 生产顺序

1. 先 `L0`（MS-03/07/08/10/16），再 `L1`（MS-04/05/06/09/11–19），最后 `L2`（MS-01/02/20–24）。
2. 每张卡：`sources` ≥ 1 条 A 级（能落到定理号/页码），≥ 1 条 B 级（书内节号或 nLab/Stacks 索引），
   书内定位一律用**本书 PDF 物理页**（`\SourcePage{N}`，与译本页码页偏移 0），外部文献用原书页码/定理号。
3. 「待核清单」非空时 `status: draft`，不得写 `frozen`。
