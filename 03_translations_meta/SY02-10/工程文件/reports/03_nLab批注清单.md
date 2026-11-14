# nLab 批注清单（12 条译注）

全部批注均以脚注形式嵌在正文首现处（「译注｜」），文末附录「译注汇总」另有重列版本与 32 行对照表。
来源等级一律 **B**（nLab 属权威综述/百科级）。链接可访问性与修订日期核对于 2026-11-15，
词条原文已抓取进发布仓 `07_refs_nlab/pages/`（本次新增 16 条），故每条批注都可回溯到具体修订版本。

| # | 节 | 概念 | 批注要点 | nLab 词条（last revised） |
|---|---|---|---|---|
| 1 | §1.1 | Tannaka 对偶 | 把谱定理读成「表示范畴 ≃ 谱侧范畴」，是 Tannaka 对偶在交换群上的特例；谱侧是「颜色」的栖身之处 | `Tannaka+duality`（2025-07-28） |
| 2 | §1.4 | 朗兰兹对偶群 | $\check G$ 的组合定义只用根数据的对偶；给出 $\mathrm{SL}_{n}\leftrightarrow\mathrm{PGL}_{n}$、$\mathrm{SO}_{2n+1}\leftrightarrow\mathrm{Sp}_{2n}$ | `Langlands+dual+group`（2014-09-07） |
| 3 | §1.4 | S-对偶与 Kapustin–Witten | 「电磁对偶把 $G$ 换成 $\check G$」由 Montonen–Olive 实现，Kapustin–Witten 进一步化为 GLC | `S-duality`（2026-09-18）、`Kapustin-Witten+TQFT`（2026-09-28） |
| 4 | §2.1 | 六函子形式 | 六个操作在导出范畴层面公理化；「brave new harmonic analysis」= 积分/乘法/函数空间对应推前/张量积/导出范畴 | `six+operations`（2026-09-30） |
| 5 | §2.2.2 | Weil 单值化 | 阿代尔双陪集描述与 Weil 单值化定理是同一陈述（$\prod'G(\mathbb C(\!(z)\!))$ 模 $\prod G(\mathbb C[[z]])$） | `Weil+uniformization+theorem`（2023-04-04） |
| 6 | §2.4 | 几何类域论 | $G=\mathrm{GL}_{1}$ 情形即 $\mathrm{Pic}^{0}(C)\cong\mathrm{Loc}_{\mathrm{GL}_{1}}(C)$（Abel–Jacobi） | `geometric+class+field+theory`（2025-05-11） |
| 7 | §2.5 | 归纳凝聚层 | $\IndCoh$ 与 $\QCoh$ 之别（同时记录推前与反常推前，容纳「错维」层）；下标 $\Nilp$ = 幂零奇异支撑 | `ind-coherent+sheaves`（2015-10-05） |
| 8 | §3.2 | 因子化同调 | 局部数据 ⇒ 整体可观测量的装配机制；拓扑原型为 Ayala–Françis | `factorization+homology`（2026-05-30） |
| 9 | §3.3 | 几何 Satake 等价 | $\Sph_{G}$ 的 Tannaka 谱恰为 $\Rep(\check G)$，对偶群由自同构群重建——Tannaka 重构的几何版 | `geometric+Satake+equivalence`（2024-07-22） |
| 10 | §3.5 | 谱作用 | $\QCoh(\Loc_{\check G})$ 经因子化同调粘成整体作用；单点情形退回几何 Satake | `geometric+Langlands+correspondence`（2026-04-11） |
| 11 | §4.2 | 奇异支撑 | 相空间 $T^{*}X$ 中的子簇，记录「何处、沿何方向不光滑」，是波前集的代数对应物；对 D-模它与特征簇在 Riemann–Hilbert 下相合；$\Nilp$ 即自守层奇异支撑所在的锥 | `characteristic+variety`（2017-08-29）——**见下条说明** |
| 12 | §5.2 | 周期与相对 Langlands | 此「周期」非代数几何的周期积分，而是自守形式上的不变线性泛函 | `relative+Langlands+program`（2025-04-29） |

## 核词条时发现并修正的两处问题

1. **`singular+support` 不可用。** 该 slug 在 nLab 上重定向到 *support of a distribution*（分布的支集），
   与层论意义的「奇异支撑」不是一回事。初稿据此写「nLab 词条 singular support 定义了凝聚层的奇异支撑」是错的，
   已改为：正文脚注如实说明该页重定向、义项不同、故不作链接，另引 `characteristic+variety`（D-模的特征簇，
   与奇异支撑在 Riemann–Hilbert 对应下相合）作为可访问的入口。附录对照表同步更正。
2. **三个模栈 slug 全为重定向。** `moduli+stack+of+G-principal+bundles`、`moduli+stack+of+vector+bundles`
   都重定向到 *moduli space of bundles*，`geometric+Langlands+program` 重定向到 *geometric Langlands correspondence*。
   对照表因此合并为一行「$G$-主丛／向量丛模栈 → `moduli+stack`」，并删去与「模栈 → `stack`」重复的一行。

## 关于批注的边界

- **只补定义、给链接，不替作者立论。** 凡涉及「何为真、何为未决」的判断，一律回到原文措辞，
  译者不加评价。
- **不引非权威网络来源。** 若 nLab 无对应词条（如 opers、nilpotent cone、character variety），
  宁可不给链接，只作文字说明，也不改引其它百科或博客。
- **不与「原注」混排。** 作者原有脚注 14 条，译注 12 条，分别以「原注｜」「译注｜」起首，
  颜色与位置一致，读者可一眼区分哪些是 Ben-Zvi 自己的话。
- **重定向不冒充词条。** 页面跳到别的题目时，即使 HTTP 200 也不当作「nLab 有此概念」的证据；
  本次三处重定向都是这样被抓出来的。
