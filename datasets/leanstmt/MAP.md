# leanstmt 地图（试点 12 卡）

三条读法，按目的选一条：

## 路线 1：从原文到 Lean（想学「怎么转写」）

§2.6.6 't Hooft 磁通 → S01 → S02 → S03（有限群三步：有界、循环、挠）
→ §4.1/§7.1 本征值 → S04 → S05（单位根两步：定义、计数）
→ §3.2 GNO 对偶 → S06 → S07（双对偶、同秩）

## 路线 2：从 Lean 到原文（想核「这句 Lean 对不对」）

S01–S05（`discrete-core`，只依赖 ZMod 与 RootsOfUnity 两个模块）
S06–S07（`algebraic-core`，只依赖 Dual 与 Finrank）
S08–S10（`arithmetic-core`，`ring` 级恒等式，几何前提在 G01/G02）

## 路线 3：缺口清单（想知道「为什么这么多做不了」）

G01 谱曲线亏格 → 缺曲线亏格/分歧除子/黎曼–胡尔维茨
G02 Hitchin 纤维维数 → 缺 `Bun_G`/稳定性/辛结构

## 卡片索引

| 卡 | 内容 | scope | 状态 |
| --- | --- | --- | --- |
| S01 | ℤ_N 有 N 个元素 | discrete-core | certified |
| S02 | ℤ_N 由 1 生成 | discrete-core | certified |
| S03 | ℤ_N 的 N-挠性 | discrete-core | certified |
| S04 | N 次单位根的刻画 | discrete-core | certified |
| S05 | ℂ 中 N 次单位根恰有 N 个 | discrete-core | certified |
| S06 | 双对偶回到自身 | algebraic-core | certified |
| S07 | 对偶格同秩 | algebraic-core | certified |
| S08 | 典范丛次数为偶数 | arithmetic-core | certified |
| S09 | Prym 维数 (N²−1)(g−1) | arithmetic-core | certified |
| S10 | 分歧除子次数 2N(N−1)(g−1) | arithmetic-core | certified |
| G01 | 谱曲线亏格 N²(g−1)+1 | gap | gap（sorry 1） |
| G02 | Hitchin 纤维维数 (g−1)dim G | gap | gap（sorry 1） |
