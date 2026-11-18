# 可引用的外部来源清单（dmod）

只列**已逐条核对正文**的来源。`verification.checks[]` 的 `source` / `entry` / `url` / `last_revised` 只能从这里取；
本清单没有的条目一律写 `verification.status = "source-only"`，不编 URL、不编日期。

## 1. nLab（本地缓存 `07_refs_nlab/pages/`，URL 前端统一 `https://ncatlab.org/nlab/show/`）

| slug | last revised | 可引用的断言 |
| --- | --- | --- |
| `D-module` | 2024-07-27 | $D$-模的六种运算；正特征下 $D_X$ 非诺特、$\mathcal O_X$-凝聚 $\ne$ $D_X$-凝聚（Katz/Gieseker） |
| `holonomic+D-module` | 2014-02-16 | 完整（holonomic）当且仅当特征簇维数 $=n$；此时特征簇为余切丛中的锥且 Lagrangian |
| `six+operations` | 2026-09-30 | 六运算公理；Beck–Chevalley：$(p_2)_!\\circ(p_1)^*\\cong g^*\\circ f_!$ |
| `flat+connection` | 2023-06-04 | 平坦联络等价于局部系统（Riemann–Hilbert 的经典情形） |
| `Riemann-Hilbert+correspondence` | 2024-08-09 | $\\mathrm{dR}:D^b_{rh}(X)\\cong D^b_c(X^{an},\\mathbb C)$（Mebkhout–Kashiwara–Beilinson–Bernstein） |
| `local+system` | 2025-04-10 | 局部系统 = 局部常值层 |
| `de+Rham+complex` | 2026-09-26 | 平坦联络的 de Rham 复形 |
| `flag+variety` | 2026-09-28 | 旗簇 $=SL(n,k)/B$ |
| `characteristic+variety` | 2017-08-29 | **只有文献列表，无陈述**，不可作断言来源 |
| `coherent+D-module` | 2021-10-01 | **空壳**，不可作来源 |
| `lattice` | — | 序论 lattice，**不可**用于模论的「格」 |

## 2. Stacks Project（`https://stacks.math.columbia.edu/tag/<TAG>`，标签已核对正文）

| Tag | 条目 | 可引用的断言 |
| --- | --- | --- |
| `00IN` | Lemma 10.51.2 (Artin–Rees) | $R$ 诺特、$I$ 理想、$N\\subset M$ 有限生成 ⇒ $\\exists c>0$，$I^nM\\cap N=I^{n-c}(I^cM\\cap N)$（$n\\ge c$） |
| `00IP` | Lemma 10.51.4 (Krull 交) | $R$ 诺特局部、$I$ 真理想、$M$ 有限生成 ⇒ $\\bigcap_{n\\ge0}I^nM=0$ |
| `00KE` | Definition 10.60.2 | 环的 Krull 维数 |
| `0055` | Definition 5.10.1 | 拓扑空间的 Krull 维数（素链长度上确界） |
| `00LA` | Definition 10.63.1 | 结合素（associated prime） |
| `07BK` | Definition 10.131.2 | Kähler 微分模 $\\Omega_{S/R}$ 及 $\\mathrm d$ |
| `01BD` | Section 17.10 | 拟凝聚模的定义与基本性质 |
| `01BU` | Section 17.12 | 凝聚模的定义与基本性质 |
| `0A6Y` | Lemma 47.12.3 | 局部化里 torsion 与 complete 的对偶（$R\\Gamma_Z$ 的形式对照，**不是**局部上同调的定义） |

## 3. 底本自身的页码（允许作 `source-only` 的来源）

`sources[].pages` / `pdf_pages`：印刷页 = PDF 页 − 6。第 I 章 p1–54（PDF 7–60）、II p55–76（61–82）、
III p77–95（83–102）、IV p97–132（103–138）、V p133–141（139–147）。
`anchor` 写 `源码/chapters/chapN.tex:行号-行号（定理 N.M）`，行号以入库时的校订批注本为准。
