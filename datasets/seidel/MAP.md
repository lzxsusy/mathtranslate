# Seidel 资料卡 · 骨架图

全书三章是一条流水线：**第一章把 A∞ 语言搭好，第二章把辛几何装进去，第三章用 Lefschetz 纤维化把它变成可计算的数据**。下图节点旁标的是原书印刷页；括号里是卡 id 的末段。

```mermaid
flowchart TD
    subgraph CH1["第一章：A∞ 代数（p.7–95）"]
        A1["A∞ 代数<br/>μ^d，deg=2−d<br/>p.7（a-infinity-algebra）"]
        A2["A∞ 范畴<br/>hom 与复合<br/>p.9（a-infinity-category）"]
        A3["扭曲复形 Tw A<br/>下三角 δ + MC<br/>p.43（twisted-complex）"]
        A4["Karoubi 完备化<br/>幂等元分裂<br/>p.68（karoubi-envelope）"]
        A5["分裂生成<br/>Π(Tw A)<br/>p.71（split-generation）"]
        A6["正合三角<br/>Cone 与旋转<br/>p.41（exact-triangle）"]
        A1 --> A2 --> A3 --> A4 --> A5
        A3 --> A6
    end

    subgraph CH2["第二章：Fukaya 范畴（p.96–210）"]
        B1["正合 Lagrangian<br/>λ|L=da<br/>p.96（exact-lagrangian）"]
        B2["Floer 复形<br/>条带计数<br/>p.101（floer-complex）"]
        B3["Maslov 指标<br/>分次 α<br/>p.150（maslov-index）"]
        B4["行列式线<br/>定向<br/>p.150（determinant-line）"]
        B5["膜结构<br/>分次 + Pin<br/>p.163（brane-structure）"]
        B6["Fukaya 范畴 F(M)<br/>圆盘计数 μ^d<br/>p.113（fukaya-category）"]
        B1 --> B2 --> B6
        B3 --> B5 --> B6
        B4 --> B2
    end

    subgraph CH3["第三章：Picard–Lefschetz（p.211–314）"]
        C1["Lefschetz 纤维化<br/>z1²+…+zn²<br/>p.213（lefschetz-fibration）"]
        C2["消失圈<br/>S^{n−1}<br/>p.221（vanishing-cycle）"]
        C3["匹配圈<br/>两个消失圈之并<br/>p.224（matching-cycle）"]
        C4["顶针<br/>Lagrangian 盘<br/>p.229（thimble）"]
        C5["定理 A 归纳<br/>维数下降<br/>p.303（lefschetz-induction）"]
        C6["定理 B 构造 B<br/>directed A∞<br/>p.5 / §19（theorem-b-construction）"]
        C7["变异<br/>Hurwitz 移动<br/>p.272（mutation）"]
        C1 --> C2 --> C3 --> C4
        C2 --> C5
        C4 --> C6
        C3 --> C7
    end

    A3 -.->|"Tw 是三角化的容器"| B6
    A5 -.->|"分裂闭包"| C6
    B6 -.->|"F(X) 由消失圈生成"| C5
    C6 -.->|"Tw B ≃ F(X)"| A3
```

## 三章各回答什么

| 章 | 问题 | 关键机器 | 卡 |
|---|---|---|---|
| 第一章 | 链层次的复合不严格结合，怎么还能算？ | μ^d、Tw、Karoubi、分裂生成 | 6 概念 + 4 推导 |
| 第二章 | 辛流形的几何怎么变成 A∞ 范畴？ | 正合性、Floer 复形、Maslov、行列式线、膜结构 | 6 概念 |
| 第三章 | 怎么从 PL 数据真的算出 F(X)？ | 消失圈/匹配圈/顶针、归纳、directed A∞ | 4 概念 + 4 推导 |

## 读法

- 只想抓定理 A/B：先读 `lefschetz-induction`、`theorem-b-construction`，再回 `twisted-complex` 与 `fukaya-category` 补语言。
- 想补 A∞ 基础：按 A1 → A2 → A3 → A4 → A5 顺序；`exact-triangle` 可最后读。
- 想理解「为什么能算」：`vanishing-cycle` → `matching-cycle` → `thimble` → `mutation` → `lefschetz-induction`。
