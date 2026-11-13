# TIMELINE.md — 分块表（Lead 独占维护；队友只读）

**页码换算：PDF 页 = 印刷页码 + 9。**

底本结构（来自原书 Contents，印刷页码）：

| 章 | 标题 | 印刷页 | PDF 页 |
|---|---|---|---|
| 1 | Riemann Surfaces and Stable Curves | 1 | 10 |
| — | 1.1 Compact Riemann surfaces | 1 | 10 |
| — | 1.2 Stable $N$-pointed curves | 17 | 26 |
| — | 1.3 Deformation of pointed curves | 25 | 34 |
| — | 1.4 Versal family of stable pointed curves | 31 | 40 |
| 2 | Affine Lie Algebras and Integrable Highest Weight Representations | 37 | 46 |
| — | 2.1 Affine Lie algebras | 37 | 46 |
| — | 2.2 Energy-momentum tensor | 40 | 49 |
| 3 | Conformal Blocks and Correlation Functions | 47 | 56 |
| — | 3.1 Conformal blocks | 47 | 56 |
| — | 3.2 Formal neighbourhoods | 52 | 61 |
| — | 3.3 Basic properties of the space of conformal blocks | 54 | 63 |
| — | 3.4 Correlation functions | 67 | 76 |
| 4 | Sheaf of Conformal Blocks | 73 | 82 |
| — | 4.1 Sheaf of conformal blocks | 73 | 82 |
| — | 4.2 Local freeness I (smooth case) | 76 | 85 |
| — | 4.3 Local freeness II (general case) and factorization | 82 | 91 |
| 5 | Projectively Flat Connections | 91 | 100 |
| — | 5.1 Projectively flat connections | 91 | 100 |
| — | 5.2 Sheaf of twisted differential operators | 96 | 105 |
| — | 5.3 Differential equations near the boundary | 101 | 110 |
| — | 5.4 Conformal blocks of one-pointed elliptic curves | 109 | 118 |
| — | 5.5 Verlinde formula | 111 | 120 |
| — | 5.6 Moduli space of parabolic bundles and Hitchin's connection | 116 | 125 |
| 6 | Vertex Operators and KZ Equations | 131 | 140 |
| — | 6.1 Conformal blocks on the Riemann sphere $\PP^1$ | 131 | 140 |
| — | 6.2 KZ equations | 136 | 145 |
| — | 6.3 Vertex operators | 140 | 149 |
| — | 6.4 Fundamental solutions of the KZ equations | 145 | 154 |
| — | 6.5 $A_n^{(1)}$ and Hecke algebra | 151 | 160 |
| — | Appendix | 161 | 170 |
| — | Bibliography | 163 | 172 |
| — | Index | 167 | 176 |

> 正文共 168 个印刷页（p.1–168），PDF p.170–177 对应印刷 p.161–168。

## 分块与归属

| 块 | 文件 | 内容 | 印刷页 | PDF 页 | 译手 |
|---|---|---|---|---|---|
| B01 | `src/b01.tex` | §1.1 紧黎曼曲面 | 1–17（到 §1.2 标题前） | 10–26 | tr-ch1a |
| B02 | `src/b02.tex` | §1.2 稳定 N-点曲线 | 17–25（到 §1.3 标题前） | 26–34 | tr-ch1a |
| B03 | `src/b03.tex` | §1.3 带点曲线的形变 | 25–31（到 §1.4 标题前） | 34–40 | tr-ch1b |
| B04 | `src/b04.tex` | §1.4 稳定带点曲线的通用族 | 31–36 | 40–45 | tr-ch1b |
| B05 | `src/b05.tex` | 第 2 章（§2.1–2.2） | 37–46 | 46–55 | tr-ch1b |
| B06 | `src/b06.tex` | §3.1–3.2 | 47–54（到 §3.3 标题前） | 56–63 | tr-ch3 |
| B07 | `src/b07.tex` | §3.3 共形块空间的基本性质 | 54–67（到 §3.4 标题前） | 63–76 | tr-ch3 |
| B08 | `src/b08.tex` | §3.4 关联函数 | 67–72 | 76–81 | tr-ch3 |
| B09 | `src/b09.tex` | §4.1–4.2 | 73–82（到 §4.3 标题前） | 82–91 | tr-ch4 |
| B10 | `src/b10.tex` | §4.3 局部自由性 II 与因子化 | 82–90 | 91–99 | tr-ch4 |
| B11 | `src/b11.tex` | §5.1–5.2 | 91–101（到 §5.3 标题前） | 100–110 | tr-ch5a |
| B12 | `src/b12.tex` | §5.3–5.5 | 101–116（到 §5.6 标题前） | 110–125 | tr-ch5a |
| B13 | `src/b13.tex` | §5.6 抛物丛的模空间与 Hitchin 联络 | 116–130 | 125–139 | tr-ch5b |
| B14 | `src/b14.tex` | §6.1–6.2 | 131–140（到 §6.3 标题前） | 140–149 | tr-ch6a |
| B15 | `src/b15.tex` | §6.3–6.4 | 140–151（到 §6.5 标题前） | 149–160 | tr-ch6a |
| B16 | `src/b16.tex` | §6.5 $A_n^{(1)}$ 与 Hecke 代数 | 151–160 | 160–169 | tr-ch6b |
| B17 | `src/b17.tex` | 附录 + 参考文献 + 索引 | 161–168 | 170–177 | tr-ch6b |

## 小节标题（标准译名；块内 `\subsection{…}` 必须逐字用这里的用字）

块的首行（若该块从某小节开头开始）或块内小节交界处，**由该块自己写小节标题**，例如 `\subsection{紧黎曼曲面}`；编号自动生成，与原文一致。

| 节 | 英文原题 | 标准中文标题（逐字照用） |
|---|---|---|
| 1.1 | Compact Riemann surfaces | 紧黎曼曲面 |
| 1.2 | Stable $N$-pointed curves | 稳定 $N$-点曲线 |
| 1.3 | Deformation of pointed curves | 带点曲线的形变 |
| 1.4 | Versal family of stable pointed curves | 稳定带点曲线的通用族 |
| 2.1 | Affine Lie algebras | 仿射李代数 |
| 2.2 | Energy-momentum tensor | 能量-动量张量 |
| 3.1 | Conformal blocks | 共形块 |
| 3.2 | Formal neighbourhoods | 形式邻域 |
| 3.3 | Basic properties of the space of conformal blocks | 共形块空间的基本性质 |
| 3.4 | Correlation functions | 关联函数 |
| 4.1 | Sheaf of conformal blocks | 共形块层 |
| 4.2 | Local freeness I (smooth case) | 局部自由性 I（光滑情形） |
| 4.3 | Local freeness II (general case) and factorization | 局部自由性 II（一般情形）与因子化 |
| 5.1 | Projectively flat connections | 射影平坦联络 |
| 5.2 | Sheaf of twisted differential operators | 扭曲微分算子层 |
| 5.3 | Differential equations near the boundary | 边界附近的微分方程 |
| 5.4 | Conformal blocks of one-pointed elliptic curves | 单点椭圆曲线的共形块 |
| 5.5 | Verlinde formula | Verlinde 公式 |
| 5.6 | Moduli space of parabolic bundles and Hitchin's connection | 抛物丛的模空间与 Hitchin 联络 |
| 6.1 | Conformal blocks on the Riemann sphere $\PP^1$ | 黎曼球面 $\PP^1$ 上的共形块 |
| 6.2 | KZ equations | KZ 方程 |
| 6.3 | Vertex operators | 顶点算子 |
| 6.4 | Fundamental solutions of the KZ equations | KZ 方程的基本解 |
| 6.5 | $A_n^{(1)}$ and Hecke algebra | $A_n^{(1)}$ 与 Hecke 代数 |

## 边界约定

- 每块从**本节标题之后**开始（小节标题由块自己写，见上表），到**下一节标题之前**结束。
- 边界页由前后两块共用：**各译各的，不跨界**。跨页句子"开始者写完"。
- 各章标题页、小节标题页的第一段往往紧接标题，注意不要漏译标题下的第一句。

## 编号提醒

- 公式 `(章.序)`、环境（Definition/Theorem/Lemma/Proposition/Corollary/Example/Remark）都是**章内连续**，块内不要重排、不要补号。
- 若原文确实跳号/重号，照原文排并在批注与 `ERRATA:` 中说明。
