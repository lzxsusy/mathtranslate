# leanstmt 地图（26 卡）

三条读法，按目的选一条。

## 路线 1：从原文到 Lean（想学「怎么转写」）

Witten 2015 §2.6.6 't Hooft 磁通 → W15-S01 → S02 → S03（有限群三步：有界、循环、挠）
→ §4.1/§7.1 本征值 → W15-S04 → S05（单位根两步：定义、计数）
→ §3.2 GNO 对偶 → W15-S06 → S07（双对偶、同秩）
→ Witten 2008 §2 对偶群 → W08-S01（中心 μ_N）→ §3 纤维 T-对偶 → W08-S02 → S03
→ §5 非正则奇点 → W08-S04（系数伸缩律）→ §6.1 四维提升 → W08-S05（currying）

## 路线 2：从 Lean 到原文（想核「这句 Lean 对不对」）

W15-S01–S05（`discrete-core`，只依赖 ZMod 与 RootsOfUnity 两个模块）
W15-S06–S07（`algebraic-core`，只依赖 Dual 与 Finrank）
W15-S08–S10（`arithmetic-core`，`ring` 级恒等式，几何前提在 G01/G02）
W08-S01（`algebraic-core`，SL(N,ℂ) 的中心，依赖 SpecialLinearGroup）
W08-S02–S03、S05（`discrete-core`，依赖 PontryaginDuality 与 Equiv.curry）
W08-S04（`algebraic-core`，复数幂的基础算术）

## 路线 3：缺口清单（想知道「为什么这么多做不了」）

W15-G01 谱曲线亏格 → 缺曲线亏格/分歧除子/黎曼–胡尔维茨
W15-G02 Hitchin 纤维维数 → 缺 `Bun_G`/稳定性/辛结构
W08-G01 Y 的模空间 → 缺平坦丛模空间/表示簇/复辛流形
W08-G02 A/B 模型 → 缺超凯勒流形与二维拓扑场论
W08-G03 Hitchin 方程 → 缺黎曼面联络/Hodge 星/ad(E) 值 1-形式
W08-G04 解 ↔ 平坦联络 ↔ 希格斯丛 → 缺希格斯丛与稳定性（GIT）
W08-G05 Hitchin 纤维化 → 缺特征多项式映射/阿贝尔簇/Lagrange 子流形
W08-G06 主定理：镜像对称 → 缺 SYZ/T-对偶与镜像对称本身
W08-G07 tame ramification → 缺 𝔤 值留数与单值理论
W08-G08 wild ramification/辫群 → 缺 Stokes 现象、等单值变形、辫群
W08-G09 四维提升与栈 → 缺四维规范理论与 `Bun_G` 无整体商定理

## 卡片索引

| 卡 | 内容 | scope | 状态 |
| --- | --- | --- | --- |
| W15-S01 | 't Hooft 磁通所在的群 ℤ_N 有 N 个元素 | discrete-core | certified |
| W15-S02 | ℤ_N 由 1 生成，加法阶为 N | discrete-core | certified |
| W15-S03 | ℤ_N 中每个元素都是 N-挠的 | discrete-core | certified |
| W15-S04 | N 次单位根的刻画 | discrete-core | certified |
| W15-S05 | ℂ 中 N 次单位根恰有 N 个 | discrete-core | certified |
| W15-S06 | 电荷格的双对偶回到自身 | algebraic-core | certified |
| W15-S07 | 对偶格与原格同秩 | algebraic-core | certified |
| W15-S08 | 典范丛次数为偶数，自旋结构存在 | arithmetic-core | certified |
| W15-S09 | Prym 的维数 = (N²−1)(g−1) | arithmetic-core | certified |
| W15-S10 | 分歧除子的次数 = 2N(N−1)(g−1) | arithmetic-core | certified |
| W15-G01 | 缺口：谱曲线的亏格 N²(g−1)+1 | gap | gap |
| W15-G02 | 缺口：Hitchin 纤维维数 (g−1)·dim G | gap | gap |
| W08-S01 | SU(N) 的中心是 ℤ_N（对偶群 PSU(N) 的核） | algebraic-core | certified |
| W08-S02 | 有限对偶环面的影子：Hom(ℤ_N, U(1)) 有 N 个元素 | discrete-core | certified |
| W08-S03 | T-对偶的离散同构：ℤ_N ≅ Hom(ℤ_N, U(1)) | discrete-core | certified |
| W08-S04 | 非正则奇点系数在 z = λw 下的伸缩律 | algebraic-core | certified |
| W08-S05 | 规范变换群的 currying | discrete-core | certified |
| W08-G01 | 缺口：Y(G,C) 复辛、维数 2(g−1)dim G、典范丛平凡 | gap | gap |
| W08-G02 | 缺口：A-模型与 B-模型的数据 | gap | gap |
| W08-G03 | 缺口：Hitchin 方程 (2.1) | gap | gap |
| W08-G04 | 缺口：Hitchin 解 ↔ 复平坦联络 ↔ 半稳定希格斯丛 | gap | gap |
| W08-G05 | 缺口：Hitchin 纤维化的底与一般纤维 | gap | gap |
| W08-G06 | 缺口（本文主定理）：Hitchin 纤维化上的镜像对称 | gap | gap |
| W08-G07 | 缺口：tame ramification 的单值 exp(−2π(α−iγ)) | gap | gap |
| W08-G08 | 缺口：wild ramification 与辫群 B(G) ≅ B(^LG) | gap | gap |
| W08-G09 | 缺口：四维提升与 Bun_G 无有限维整体商 | gap | gap |
