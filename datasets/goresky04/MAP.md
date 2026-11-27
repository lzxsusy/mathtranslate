# MAP —— goresky04 论证地图（一页纸）

```
                        ┌──────────────────────────────────────────┐
                        │  §2  猜想：两侧一一对应，特征值逐素数相等 │
                        │      (2.0.1) 对应；(2.0.2) 特征值对应      │
                        └───────────────────┬──────────────────────┘
                                            │  要把每个词讲清楚
              ┌─────────────────────────────┴─────────────────────────────┐
              │                                                           │
   ┌──────────▼───────────┐                                   ┌───────────▼──────────┐
   │ §3  域：整体 / 局部   │                                   │ §5–§6  自守侧         │
   │  数域、p 进、函数域   │                                   │  模形式 → Hecke 算子  │
   │  局部–整体原则        │                                   │  → 特征形式 → 自守表示 │
   └──────────┬───────────┘                                   │  → Satake 参数        │
              │                                               └───────────┬──────────┘
   ┌──────────▼───────────┐                                               │
   │ §4  Galois 侧         │                                               │
   │  平展上同调 H^i_ét     │                                               │
   │  Frobenius 元素 Fr_p   │                                               │
   │  ζ(Y,s) 与 Deligne     │                                               │
   └──────────┬───────────┘                                               │
              │                                                           │
              └───────────────────────┬───────────────────────────────────┘
                                      │
                        ┌─────────────▼─────────────┐
                        │ §7  对照                   │
                        │  n=2：Eichler–Shimura (7.1.1) │
                        │  n≥3：Shimura 簇不存在 → 断  │
                        └─────────────┬─────────────┘
                                      │
                        ┌─────────────▼─────────────┐
                        │ §8  换群 / 换域 / 换范畴   │
                        │  8.2 对偶群 8.5 几何Langlands │
                        │  8.6 函子性（六节正文全空） │
                        └───────────────────────────┘
```

## 三条硬约束

1. **两侧的数据类型必须一致**：左侧是 $\\Fr_p$ 的特征值（无序组），右侧是 $\\mathrm{Satake}$ 参数（无序组）。有序组或单个矩阵都无法比较。
2. **非分歧是前提，不是细节**：$\\Fr_p$ 只在非分歧处良定义，Satake 参数只在非分歧处存在。几乎所有 $p$ 满足，但有限个 $p$ 要另设局部因子。
3. **几何载体是 $n=2$ 的特权**：$\\GL(n)$ 的对称空间是 Hermitian 的当且仅当 $n=2$；$n\\ge3$ 没有 Shimura 簇，整条上同调路线断掉。

## 原文自认的空白

| 位置 | 原文状态 | 后果 |
| --- | --- | --- |
| §7.3「$\\GL(1)$ 又如何？」 | 只有标题 | 类域论作为「$n=1$ 原型」被跳过 |
| §8.2 对偶群 | 只有标题 | $L$-群没定义，§8.5 的左侧无法精确陈述 |
| §8.3 Hermitian 情形 | 只有标题 | 西群情形被跳过 |
| §8.4 局部域 | 只有标题 | 局部朗兰兹被跳过 |
| §8.5 几何 Langlands | 只有标题 | **本文的落点，但一字未写** |
| §8.6 函子性 | 只有标题 | 主干推广只留名字 |
| §8.7 重大结果抽样 | 只有标题 | 参考文献 [F] 的成果没被引进来 |

**读法**：这些空白不是缺陷，是文章的结构特征。作者把「已知」写满、把「未知与未写」留成标题，读者据此可以判断这一领域在 2004 年的边界在哪里。

## 卡与节的对应

| 原文 | 卡 |
| --- | --- |
| §2 | `concept/langlands-conjecture-statement` |
| §1 + §7 | `concept/two-sides-map` |
| §3 | `concept/global-and-local-fields` |
| §4.1 | `concept/etale-cohomology` |
| §4.2 | `concept/zeta-function-of-variety` |
| §4.3–4.4 | `concept/frobenius-element`、`deriv/local-zeta-factor` |
| §5.1–5.3 | `concept/modular-form-classical` |
| §5.4 | `concept/hecke-operator` |
| §5.5–5.6 | `concept/hecke-eigenform` |
| §6.1 | `concept/adele-ring`、`deriv/adelic-equivalence` |
| §6.2–6.3 | `concept/automorphic-representation` |
| §6.4 | `concept/satake-parameter` |
| §7.1 | `concept/eichler-shimura-theorem`、`concept/shimura-variety`、`deriv/eichler-shimura-decomposition` |
| §7.2 | `concept/obstruction-n-ge-3` |
| §2 + §6.4 | `deriv/hecke-to-frobenius` |
| §8.2 | `concept/dual-group` |
| §8.5 | `concept/geometric-langlands` |
| §8.6 | `concept/functoriality` |
