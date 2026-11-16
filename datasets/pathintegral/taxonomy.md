# 路径积分资料卡 · 总表

书名：李思《量子力学与几何》（中文译注本）第 2 章「路径积分形式」。

共 **50 张**：1 张总览 + 29 张概念卡 + 20 张例子卡。页码为原书印刷页（80–160）；PDF 页 = 印刷页 + 1。

## 阅读顺序

```text
O 总览 → A 定义与时间切片 → B 高斯/谐振子（精确答案）
        → C 驻定相位与半经典（近似机器）
        → D 格林函数/WKB/隧穿（物理输出）
        → E 威克/费曼图/Moyal/HKR（代数输出）
```

## O · 总览（1 张）

先看这一张，再决定读哪条轨道。

| 卡片 | 标题 | 印刷页 | 源码 |
|---|---|---|---|
| [`overview-path-integral`](md/concepts/overview-path-integral.md) | 路径积分总览：从费曼核到量子 HKR | 80–107 | `ch02a.tex:8-1466` |

## A · 基础与时间切片（6 张）

费曼核、位置/动量表示、时间切片、路径积分定义、虚时间。

| 卡片 | 标题 | 印刷页 | 源码 |
|---|---|---|---|
| [`feynman-kernel`](md/concepts/feynman-kernel.md) | 费曼核与传播子 | 80–82 | `ch02a.tex:13-85` |
| [`position-momentum-representation`](md/concepts/position-momentum-representation.md) | 位置与动量表示（连续谱基） | 82–84 | `ch02a.tex:86-222` |
| [`free-particle-kernel`](md/concepts/free-particle-kernel.md) | 自由粒子的精确核 $K_0$ | 84–85 | `ch02a.tex:225-287` |
| [`time-slicing`](md/concepts/time-slicing.md) | 时间切片与复合律 | 85–87 | `ch02a.tex:288-390` |
| [`path-integral-definition`](md/concepts/path-integral-definition.md) | 路径积分的定义与形式测度 | 87–88 | `ch02a.tex:391-444` |
| [`imaginary-time`](md/concepts/imaginary-time.md) | 虚时间与欧氏路径积分 | 88–89 | `ch02a.tex:445-482` |

## B · 高斯路径积分与谐振子（4 张）

唯一能精确求和的两类模型；后面所有近似都要在它们身上退化。

| 卡片 | 标题 | 印刷页 | 源码 |
|---|---|---|---|
| [`gaussian-integral`](md/concepts/gaussian-integral.md) | 有限维高斯积分 | 89–90 | `ch02a.tex:485-555` |
| [`zeta-regularization`](md/concepts/zeta-regularization.md) | zeta 函数正则化与泛函行列式 | 90–93 | `ch02a.tex:556-712` |
| [`harmonic-oscillator-propagator`](md/concepts/harmonic-oscillator-propagator.md) | 谐振子传播子（Mehler 核） | 93–95 | `ch02a.tex:715-834` |
| [`harmonic-oscillator-partition`](md/concepts/harmonic-oscillator-partition.md) | 谐振子配分函数 | 95 | `ch02a.tex:835-881` |

## C · 渐近方法与半经典（8 张）

拉普拉斯、最速下降、莫尔斯流、斯托克斯、半经典核、雅可比场。

| 卡片 | 标题 | 印刷页 | 源码 |
|---|---|---|---|
| [`semiclassical-kernel`](md/concepts/semiclassical-kernel.md) | 半经典费曼核 | 108–109 | `ch02b.tex:31-88` |
| [`jacobi-field-van-vleck`](md/concepts/jacobi-field-van-vleck.md) | 雅可比场与 Van Vleck 行列式 | 109–115 | `ch02b.tex:89-465` |
| [`time-slicing-determinant`](md/concepts/time-slicing-determinant.md) | 时间切片方法的行列式极限 | 115–117 | `ch02b.tex:466-566` |
| [`laplace-method`](md/concepts/laplace-method.md) | 拉普拉斯方法 | 96–98 | `ch02a.tex:887-1020` |
| [`steepest-descent`](md/concepts/steepest-descent.md) | 最速下降法 | 98–100 | `ch02a.tex:1021-1136` |
| [`morse-flow`](md/concepts/morse-flow.md) | 莫尔斯流与最速下降曲线 | 100–102 | `ch02a.tex:1137-1211` |
| [`stokes-phenomenon`](md/concepts/stokes-phenomenon.md) | 斯托克斯现象与艾里函数 | 102–104 | `ch02a.tex:1212-1296` |
| [`stokes-rays-asymptotic-summation`](md/concepts/stokes-rays-asymptotic-summation.md) | 斯托克斯射线与渐近求和 | 104–107 | `ch02a.tex:1297-1466` |

## D · 格林函数、WKB 与隧穿（5 张）

传播子的傅里叶变换，以及它在允许区/禁区的两种面孔。

| 卡片 | 标题 | 印刷页 | 源码 |
|---|---|---|---|
| [`fixed-energy-green-function`](md/concepts/fixed-energy-green-function.md) | 固定能量格林函数 | 117–121 | `ch02b.tex:569-808` |
| [`semiclassical-green-function`](md/concepts/semiclassical-green-function.md) | 半经典格林函数 | 121–131 | `ch02b.tex:809-1249` |
| [`wkb-path-integral`](md/concepts/wkb-path-integral.md) | 经由路径积分的 WKB | 131–132 | `ch02b.tex:1250-1293` |
| [`quantum-tunneling`](md/concepts/quantum-tunneling.md) | 量子隧穿 | 132–133 | `ch02b.tex:1294-1365` |
| [`connection-formula`](md/concepts/connection-formula.md) | 连接公式再探 | 133–137 | `ch02b.tex:1366-1538` |

## E · 微扰与代数结构（6 张）

威克定理、费曼图、Moyal 乘积、S¹ 关联、Hochschild 与量子 HKR。

| 卡片 | 标题 | 印刷页 | 源码 |
|---|---|---|---|
| [`wick-theorem`](md/concepts/wick-theorem.md) | 威克定理与高斯矩的配对 | 138–142 | `ch02c.tex:81-273` |
| [`feynman-diagrams`](md/concepts/feynman-diagrams.md) | 费曼图的组合定义与展开公式 | 142–146 | `ch02c.tex:274-520` |
| [`weyl-quantization-moyal`](md/concepts/weyl-quantization-moyal.md) | 外尔量子化与 Moyal 乘积 | 146–151 | `ch02c.tex:521-785` |
| [`s1-correlators`](md/concepts/s1-correlators.md) | $S^1$ 上的传播子与关联函数 | 151–155 | `ch02c.tex:786-1045` |
| [`hochschild-homology`](md/concepts/hochschild-homology.md) | 霍赫希尔德同调 | 155–157 | `ch02c.tex:1046-1151` |
| [`quantum-hkr`](md/concepts/quantum-hkr.md) | 量子 HKR 映射 | 157–160 | `ch02c.tex:1152-1374` |

## 例子卡（20 张）

每个编号例子一张卡；`对应概念` 指回它训练的那张概念卡。

| 卡片 | 标题 | 对应概念 | 印刷页 | 源码 |
|---|---|---|---|---|
| [`two-point-function`](md/examples/two-point-function.md) | 两点函数与逆矩阵传播子 | `wick-theorem` | 141 | `ch02c.tex:212-222` |
| [`four-point-function`](md/examples/four-point-function.md) | 四点函数与三种完全配对 | `wick-theorem` | 141 | `ch02c.tex:224-234` |
| [`wick-shift`](md/examples/wick-shift.md) | 平移后的四次多项式与部分配对 | `wick-theorem` | 141 | `ch02c.tex:251-271` |
| [`theta-graph`](md/examples/theta-graph.md) | Θ 图的顶点、半边与边 | `feynman-diagrams` | 143 | `ch02c.tex:329-344` |
| [`theta-automorphisms`](md/examples/theta-automorphisms.md) | $\Theta$ 图的自同构群 | `feynman-diagrams` | 143–144 | `ch02c.tex:371-395` |
| [`vacuum-graph-automorphisms`](md/examples/vacuum-graph-automorphisms.md) | 两个自环加一条连边图的自同构群 | `feynman-diagrams` | 144 | `ch02c.tex:397-404` |
| [`free-particle-semiclassical`](md/examples/free-particle-semiclassical.md) | 自由粒子的半经典核 | `semiclassical-kernel`、`jacobi-field-van-vleck` | 114 | `ch02b.tex:400-422` |
| [`harmonic-oscillator-semiclassical`](md/examples/harmonic-oscillator-semiclassical.md) | 谐振子的半经典核 | `semiclassical-kernel`、`jacobi-field-van-vleck` | 115 | `ch02b.tex:425-464` |
| [`theta-weight`](md/examples/theta-weight.md) | $\Theta$ 图的权重 $\omega_\Gamma$ | `wick-theorem`、`weyl-quantization-moyal` | 144–145 | `ch02c.tex:429-450` |
| [`free-green-function`](md/examples/free-green-function.md) | 自由粒子的固定能量格林函数 | `fixed-energy-green-function` | 118–119 | `ch02b.tex:630-681` |
| [`scattering-asymptotics`](md/examples/scattering-asymptotics.md) | 散射态的渐近行为 | `fixed-energy-green-function`、`wkb-path-integral` | 119–121 | `ch02b.tex:702-807` |
| [`free-semiclassical-green`](md/examples/free-semiclassical-green.md) | 自由粒子的半经典格林函数 | `semiclassical-green-function` | 124 | `ch02b.tex:960-982` |
| [`gamma-asymptotics`](md/examples/gamma-asymptotics.md) | Gamma 函数的拉普拉斯渐近 | `laplace-method` | 97 | `ch02a.tex:963-992` |
| [`linear-potential`](md/examples/linear-potential.md) | 线性势的半经典格林函数 | `semiclassical-green-function`、`connection-formula` | 124–131 | `ch02b.tex:984-1248` |
| [`s1-two-point`](md/examples/s1-two-point.md) | $S^1$ 上的两点关联 | `s1-correlators` | 155 | `ch02c.tex:992-1023` |
| [`s1-three-point`](md/examples/s1-three-point.md) | $S^1$ 上的三点关联 | `s1-correlators`、`wick-theorem` | 155 | `ch02c.tex:1025-1044` |
| [`fresnel-integral`](md/examples/fresnel-integral.md) | $\int_C e^{\mathrm{i}z^2}\,\mathrm{d}z$ 的围道计算 | `steepest-descent` | 98–99 | `ch02a.tex:1029-1072` |
| [`hochschild-commutator`](md/examples/hochschild-commutator.md) | 零阶霍赫希尔德同调与换位子 | `hochschild-homology` | 156 | `ch02c.tex:1095-1101` |
| [`steepest-descent-gaussian`](md/examples/steepest-descent-gaussian.md) | 高斯积分 $\int_C e^{\mathrm{i}\lambda z^2}\mathrm{d}z$ 的最速下降围道 | `steepest-descent`、`morse-flow` | 100 | `ch02a.tex:1120-1135` |
| [`stokes-rays-linear`](md/examples/stokes-rays-linear.md) | $\alpha z^2/2$ 的鞍点流线与最速下降围道 | `morse-flow`、`steepest-descent` | 100–101 | `ch02a.tex:1152-1188` |

## 页码与出处

- `pages` 为原书印刷页；`pdf_pages = pages + 1`。
- `anchor` 指底本 `ch02a.tex`（§2.1–§2.5）、`ch02b.tex`（§2.6–§2.7）、`ch02c.tex`（§2.8）的行段；底本不随本目录发布。
- 每张卡的 `sources` 还带小节名，便于回书核对。
