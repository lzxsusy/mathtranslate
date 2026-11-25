# 格拉斯曼资料卡 · 骨架图

这张图是整套卡的地图：**上面是模空间与向量丛这条主线（原书 pp. 25–120 / 中译 pp. 30–115），左下是量子化与相交理论（pp. 1–80 / 中译 pp. 7–81），右下是辛几何与阿贝尔簇正则性（pp. 81–168 / 中译 pp. 82–159），最右是可约曲线上的收尾（pp. 169–179 / 中译 pp. 160–170）**。箭头旁标的是「哪章哪条批注/哪张卡在讲这件事」。

概念卡与例子卡就是这条链上的节点与边；跨章依赖的 15 个具体点在工程文件 `产出\汇总\交叉引用.md` 里有逐条坐标。

```mermaid
flowchart TD
    subgraph BASE["A · 跨章基础（4 张，全书共用）"]
        CS["凝聚系<br/>coherent system"]
        ASCS["α-稳定凝聚系<br/>alpha-stable"]
        KOS["Koszul 上同调<br/>ch2"]
        GV["GV-层<br/>ch8"]
        AG["仿射 Grassmannian<br/>ch5"]
    end

    subgraph L1["主线：模空间与向量丛"]
        CH2["ch2 · Koszul 上同调<br/>Betti 表、Clifford 指数、Green 猜想<br/>概念 11 / 例 3"]
        CH7["ch7 · α-稳定凝聚系<br/>Brill–Noether 数 β、Petri 映射<br/>概念 9 / 例 2"]
        CH9["ch9 · 可约曲线上的向量丛<br/>Seshadri/Gieseker 紧化、高秩 BN<br/>概念 6 / 例 1"]
        CH6["ch6 · 曲线上层的算术<br/>μ_n-gerbe、twisted sheaf、period-index<br/>概念 8 / 例 2"]
    end

    subgraph L2["量子化与相交理论"]
        CH1["ch1 · Hitchin 联络与 TQFT<br/>Verlinde 丛、Toeplitz 算子、曲线算子<br/>概念 8 / 例 2"]
        CH3["ch3 · Reider 与 Thaddeus 再探<br/>Bridgeland 稳定性、墙与穿墙<br/>概念 7 / 例 2"]
        CH4["ch4 · 奇异模空间的相交配对<br/>Kirwan 映射、平衡作用、留数公式<br/>概念 6 / 例 1"]
    end

    subgraph L3["辛几何与阿贝尔簇"]
        CH5["ch5 · BD Grassmannian<br/>几何 Satake、Hecke 修正、因子分解<br/>概念 7 / 例 2"]
        CH8["ch8 · 阿贝尔簇上的正则性<br/>M-正则、CGG、GV 层 nef 性<br/>概念 8 / 例 2"]
    end

    CH2 -->|"Koszul 退化轨迹 ↔ Green 猜想<br/>批注 ch2#13"| CH8
    CH2 -->|"BN 数 β 的两个来源<br/>批注 ch2#14"| CH9
    CH2 -->|"Clifford 指数 ↔ 高秩 Petri<br/>批注 ch7#15"| CH7
    CH3 -->|"墙与穿墙 ↔ α-稳定<br/>批注 ch3#15"| CH7
    CH3 -->|"Bridgeland 稳定性 ↔ 奇异模空间<br/>批注 ch3#16"| CH4
    CH4 -->|"扩张模空间 ↔ Hitchin 纤维化<br/>批注 ch4#17"| CH1
    CH5 -->|"Hecke 修正 ↔ 扭化层<br/>批注 ch5#16"| CH6
    CH6 -->|"twisted sheaf ↔ 凝聚系<br/>批注 ch6#15"| CH7
    CH7 -->|"曲线上凝聚系 ↔ 可约曲线<br/>批注 ch7#16"| CH9
    CH8 -->|"GV 层 ↔ Koszul 上同调<br/>批注 ch8#17"| CH2
    CH8 -->|"M-正则 ↔ 高秩 BN<br/>批注 ch8#18"| CH9
    CH1 -->|"曲线算子 ↔ 因子分解<br/>批注 ch1#16"| CH5

    CS --> CH7
    ASCS --> CH7
    KOS --> CH2
    GV --> CH8
    AG --> CH5
```

## 三条阅读路线

| 路线 | 顺序 | 一句话 |
|---|---|---|
| 一、模空间与向量丛 | ch2 → ch7 → ch9 → ch6 | 从 Koszul 同调到凝聚系、可约曲线、Brauer 群：**「分类空间」这条线怎么一路推广**。 |
| 二、量子化与相交理论 | ch1 → ch3 → ch4 | 从 Hitchin 联络与 TQFT 到 Bridgeland 稳定性、奇异模空间的相交数：**「量子化 + 计数」这条线**。 |
| 三、辛几何与阿贝尔簇 | ch5 → ch8 | 从仿射 Grassmannian/几何 Satake 到 M-正则与 GV-层：**「辛结构 + Fourier–Mukai」这条线**。 |

## 每章入口卡

| 章 | 先读这张 | 再读这张 |
|---|---|---|
| ch1 | `grassmann/concept/hitchin-connection` | `grassmann/example/factorization-along-a-curve` |
| ch2 | `grassmann/concept/koszul-cohomology` | `grassmann/concept/clifford-index` |
| ch3 | `grassmann/concept/bridgeland-stability-condition` | `grassmann/example/s-half-dichotomy` |
| ch4 | `grassmann/concept/balanced-action` | `grassmann/concept/residue-formula-for-pairings` |
| ch5 | `grassmann/concept/affine-grassmannian` | `grassmann/concept/geometric-satake-correspondence` |
| ch6 | `grassmann/concept/gerbe-banded-by-mu-n` | `grassmann/concept/period-and-index` |
| ch7 | `grassmann/concept/coherent-system` | `grassmann/concept/alpha-stable-coherent-system` |
| ch8 | `grassmann/concept/gv-sheaf` | `grassmann/concept/m-regular-sheaf` |
| ch9 | `grassmann/concept/reducible-nodal-curve-and-dual-graph` | `grassmann/example/limit-linear-series-on-a-chain-of-five-elliptic-curves` |
