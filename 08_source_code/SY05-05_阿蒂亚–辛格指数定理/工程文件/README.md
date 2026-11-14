# 2107.03557v1(2) 中译本（阿蒂亚–辛格指数定理）

Daniel S. Freed, *The Atiyah–Singer Index Theorem*, arXiv:2107.03557v1 [math.HO]
（2021-07-08，52 页；为纪念 Michael Atiyah 而作）的**中文本土化 + 结构化 LaTeX 译本**，
附学术审校批注（`% [Tutor Note: …]`）与「本节重点」。

## 文件清单

```
2107.03557v1(2)/
├── 2107.03557v1(2)_zh.tex     主文件（单文件、可直接编译）
├── 2107.03557v1(2)_zh.pdf     已编译成品（77 页，XeLaTeX 引擎）
├── 审校报告.md                 公式核对、原文笔误清单、术语决策、批注统计、编译记录
└── README.md                  本文件
```

**原文无图**：经逐页核对，Freed 此文 52 页中 Figure 数为 0（仅有 127 个 `equation`
环境与若干定理/注记环境）。因此本译本不含插图与图注——这是原文事实，不是缺漏。

## 编译

```text
xelatex 2107.03557v1(2)_zh.tex
xelatex 2107.03557v1(2)_zh.tex     % 第二遍为目录/交叉引用
```

- 文档类沿用原文的 `amsart`（完整保留原版式、公式编号与定理环境；若需 `article`
  版可整体替换文类，正文无需改动）。
- 需要 XeTeX 引擎 + `xeCJK` + 中文字体（默认 SimSun/SimHei/KaiTi/FangSong，
  Windows 自带）；宏包：`amsmath, amssymb, amsthm, mathrsfs, eucal, mathabx,
  amscd, enumitem, marginnote, comment, color, xy, hyperref, longtable, booktabs`。
- 本成品已用 **Tectonic 0.17**（XeTeX 内核）实测编译：**77 页，0 error，
  0 missing character，8 处轻微 overfull hbox（< 26 pt，均在附录批注中）**。
- 参考文献保留原文英文条目与编号，正文 `\cite` 全部可解析。

## 译本结构

| 部分 | 内容 |
|---|---|
| 卷首 | 中译标题、作者、摘要、目录、译者说明 |
| §1 | 引言：从黎曼球面上的亚纯函数计数到指数定理 |
| §2 | 代数几何/拓扑前史：Riemann–Roch、Hirzebruch、Grothendieck、整性定理 |
| §3 | 分析前史：de Rham/Hodge/Dolbeault、椭圆算子与 Fredholm 指数 |
| §4 | 指数定理及两种证明（配边、K 理论）、Dirac 算子 |
| §5 | 变奏：等变、带边、实、Clifford 线性、族、von Neumann 代数 |
| §6 | 热方程证明与局部指数定理 |
| §7 | Dirac 算子的几何不变量：号差亏损、APS η 不变量、行列式线丛 |
| §8 | 反常与指数理论（含 Witten 的整体反常） |
| 附录 A | 审校批注汇编（正文中为注释，编译后不显示；此处汇总 303 条） |
| 附录 B | 核心术语英–中对照表 |

## 批注体例

- `% [Tutor Note: 类别——内容]`：LaTeX 注释，编译后不可见。四类：
  **易错**（符号、指标、归一化、定向/spin 结构等高风险处）、
  **含糊**（作者以 "obvious / standard / a short calculation" 略去的证明实质，附可查文献）、
  **笔误**（原文疑似错误，照录并指出，正文一律不改）、
  **术语**（易混译名与概念边界）。
- 每节开头「本节重点（Key Takeaways）」为译者所加阅读导引（原文无此内容）。
- 公式编号完全保留原文体系；正文引用一律用 `\eqref/\ref`，与原文印刷号一致。

## 说明

- 正文翻译以“无损”为唯一标准：不增删论证、不改动作者行文逻辑与语气、不添加原文没有的
  物理/数学阐释；全部公式、定理环境、`\label`、`\cite` 键与原 LaTeX 源码逐字符一致
  （唯一例外：`\text{…}` 内自然语言译为中文，及三处英文序数上标按中文习惯改写）。
- 原文笔误一律照录并在批注中指出（清单见《审校报告》§4），未擅自改动正文数学内容。
