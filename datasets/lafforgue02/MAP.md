# Lafforgue Tata 讲义（lafforgue02）资料卡 · 骨架图

这张图是 Lafforgue 讲义（IHES/M/02/45，56 页）的逻辑骨架：先把「Langlands 对应要证什么」摆出来，再说「为什么要在 chtouca 的模叠上做」，然后用截断 → 紧化 → 本质同调三步把证明逼出来，最后用赋值判据把紧合性落到一个关于 $\varphi$-格的代数命题上。节点是概念卡，边是推导卡；标注的页码是讲义**印刷页**。

```text
§I  p.3          [A] langlands-correspondence-function-field ──deriv──▶ trace-from-truncation
                        │  (i)_r 双射 / (ii)_r 局部匹配
                        ▼
§I  p.5–6        [A] drinfeld-chtouca ──▶ chtouca-moduli-stack
                        │                         │ (∞,0) 光滑、维 2r−2、非有限型
                        │                         ▼
                        │            [A] harder-narasimhan-truncation ──deriv──▶ truncation-to-compactification
                        ▼                         │
§I  p.7–8        [A] hecke-correspondence         │  三栏：开叠 / 截断 / 紧化
                        │                         ▼
§II p.10–11      [A] r-negligible-representation ──deriv──▶ essential-part-in-middle-degree
                        │  本质 = 非 r-可忽略           │  用配对 L-函数排除可忽略分量
                        ▼                              ▼
§II p.15         [A] lfunction-pairs          [A] trace-formula-essential-cohomology
                        │                              │  迹公式给出 Tr_π(f)
                        └──────────────┬───────────────┘
                                       ▼
§III p.19–26     [A] fourre-tout ──▶ complete-homomorphism
                        │  不分离叠、把所有截断紧化收作开子叠
                        ▼
§V  p.34–41      [A] valuative-criterion-properness ──deriv──▶ properness-by-valuative-criterion
                        │  紧合 ⇔ 每个 K_A-点延拓
                        ▼
§V  p.34–36      [B] iterated-phi-lattice ──▶ [B] degenerator
                        │                         │
                        ▼                         ▼
§V  p.41–45      [B] global-stability-hecke  ◀── 退化子族避开 N
```

## 一句话链

> 要在 $\Cht^r_N$ 上「分离出」$\bigoplus_\pi \pi\otimes\sigma_\pi\otimes\tilde\sigma_\pi(1-r)$，必须先截断（有限型）、再紧化（紧合，可用 Lefschetz）；紧化补进来的边界上同调恰好是 $r$-可忽略的，因此不污染答案；剩下的本质部分集中在中间次数 $2r-2$、纯权 $0$，由迹公式可算。

## 三条阅读路径

| 路径 | 卡片序列 |
| --- | --- |
| 证明主线（第 I–II 章） | drinfeld-chtouca → truncation-to-compactification → r-negligible-representation → essential-part-in-middle-degree → trace-from-truncation |
| 紧化怎么造（第 III–IV 章） | fourre-tout → complete-homomorphism → chtouca-moduli-stack |
| 紧合性怎么证（第 V–VI 章） | valuative-criterion-properness → iterated-phi-lattice → degenerator → properness-by-valuative-criterion |

## 四个最容易读错的地方

1. **「可忽略」是相对秩 $r$ 的**：同一个表示在秩 $r$ 可忽略，在秩 $r+1$ 可能变成本质的。
2. **紧化后 Hecke 对应还在，但 $\mathcal H^r_N$ 的模作用不在了**：逐元素作用存在且不结合，故只能用迹公式。
3. **fourre-tout 本身不紧合、不分离**：紧化是它里面的开子叠，不是它本身。
4. **赋值判据要对任意离散赋值环验证**：只验 $X$ 的局部环是特例，不足。

## 与译本的对应

| 讲义章 | 印刷页 | 译本文件 | 相关卡 |
| --- | --- | --- | --- |
| 引言 | 1–2 | `ch1_intro.tex` | — |
| I 证明的原理 | 3–11 | `ch2_I_a.tex`、`ch2_I_b.tex` | 前 5 张概念卡 + `truncation-to-compactification` |
| II 证明的大线条 | 12–19 | `ch3_II.tex` | `r-negligible-representation`、`lfunction-pairs`、`trace-formula-essential-cohomology` |
| III 无水平结构的紧化 | 19–26 | `ch4_III.tex` | `fourre-tout`、`complete-homomorphism` |
| IV 紧化上的截断与水平结构 | 26–33 | `ch5_IV.tex` | `chtouca-moduli-stack` |
| V 紧合性的赋值判据 | 34–41 | `ch6_V_a.tex`、`ch6_V_b2.tex` | `valuative-criterion-properness`、`global-stability-hecke`、`degenerator` |
| VI 判据的证明 | 42–55 | `ch7_VI_a.tex`、`ch7_VI_b.tex` | `iterated-phi-lattice`、`properness-by-valuative-criterion` |
