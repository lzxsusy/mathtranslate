# 弦紧致化的几何工具（TASI 2017 讲座）——中文译注本

> **TASI Lectures on Geometric Tools for String Compactifications**
> Lara B. Anderson, Mohsen Karkheiran（Virginia Tech, Department of Physics）
> arXiv:1804.08792v1 [hep-th], 24 Apr 2018；PoS（TASI 2017 Summer School, Boulder, Colorado）
> 原文 61 页（PDF 页码 = 印刷页码 + 1）；原文许可 CC BY-NC-ND 4.0。

## 0. 重要说明：作者不是 Witten

本 PDF 的作者是 **Lara B. Anderson 与 Mohsen Karkheiran**，不是 Edward Witten。
原文中 Witten 只作为文献作者出现（如 Gukov–Vafa–Witten 超势、Green–Schwarz–Witten 教材 [11]、
Candelas–Horowitz–Strominger–Witten [1]）。本译本未在任何位置把本文署名为 Witten 的工作。

## 1. 交付内容

```
1804.08792v1_TASI2017_弦紧致化的几何工具_中文译注本/
├── main.tex                  # 主文件（装配 + 标题页 + 译者说明 + 目录）
├── preamble.tex              # 导言区（宏包、版式、keytakeaway 框、常用宏）
├── sections/                 # 正文分片（按原文页码切分，可直接编辑）
│   ├── s01-intro.tex         #   §1 引言（PDF p2–4）
│   ├── s02-heterotic.tex     #   §2 杂化弦紧致化、SU(3) 结构、表 1（p4–8）
│   ├── s03a-cy.tex           #   §3 开头、3.1、3.2，图 3–7（p9–15）
│   ├── s03b.tex              #   3.3、3.4，图 8、9（p15–26）
│   ├── s03c.tex              #   3.5–3.7（p26–33）
│   ├── s04-bundles.tex       #   §4 丛与谱、表 2（p34–45）
│   ├── s05-conclusions.tex   #   §5 结论、附录 A、图 10（p45–54）
│   └── s06-refs.tex          #   参考文献 [1]–[136]（p54–61，英文照录）
├── figures/fig01.png … fig10.png   # 原文全部 10 幅插图（自 PDF 剥离）
├── main.pdf                  # 编译产物（60 页）
├── 1804.08792v1_弦紧致化的几何工具_中文译注本.pdf   # 成品 PDF（与 main.pdf 相同）
├── notes/
│   ├── annotations-index.md  # 全部源码批注（Tutor Note/原文疑误/存疑/背景补充）汇总索引
│   └── eq-inventory.md       # 原文逐页公式编号清单（核对用）
├── 原PDF页面图/page-01.png … page-61.png   # 原文每页 150 dpi 图像（逐页对照用）
├── 原PDF文字层/page-01.txt … page-61.txt   # 原文每页文字层（仅作定位，公式不可信）
├── 1804.08792v1(2).pdf       # 原文 PDF（对照用）
├── README.md / SPEC.md / GLOSSARY.md / REVIEW-NOTES.md
└── tools/                    # 本项目使用的脚本（crop/render/verify/build 等）
```

## 2. 编译

需要 **XeLaTeX**（pdfLaTeX 不能处理中文）：

```
xelatex main.tex
xelatex main.tex      # 第二遍生成目录与交叉引用
```

- 中文使用 `ctex` 自带的 **fandol** 字库，随 TeX Live 分发，无需安装系统字体。
  若本机有宋体/黑体，可把 `main.tex` 第一行文档类选项改为 `fontset=windows`。
- 依赖宏包均为 TeX Live 标准包：`ctex, amsmath, amssymb, amsthm, graphicx, booktabs,
  longtable, array, multirow, enumitem, xcolor, tcolorbox, caption, float, fancyhdr, hyperref`。
- 也可用脚本：`python tools/build.py`（调用 xelatex 两遍，产物在 `build/main.pdf`）。
- 图表路径相对 `main.tex`（`\graphicspath{{figures/}}`），编译时须保持目录结构。

## 3. 体例与标记约定

| 标记 | 含义 |
|---|---|
| `% [Tutor Note: ...]` | 学术批注：易错预警、含糊点拨、几何/物理直觉（不进入排版） |
| `% [原文疑误: ...]` | 判定为原文笔误/排印错误，附判断依据；**正文照录原文、不静默改动** |
| `% [存疑: ...]` | 无法完全确证的可疑之处 |
| `% [背景补充: ...]` | 为中文读者补足的必要背景 |
| `% ==== 原文 PDF 第 N 页 ====` | 页锚注释，保证与原文逐页对照（印刷页码 = N − 1） |
| `% [跨页接续: ...]` | 原文跨页断句说明 |
| `% EN: ...` | 章节标题的英文原文，便于对照 |

- 每个大章节（§1–§5、附录 A）开头有 **“本节重点（Key Takeaways）”** 框，给出核心物理图像／数学工具／主要结论；
  3.3、3.4 两个最长的子节另设小结框以便阅读。
- 所有带编号公式均用 `\tag{}` 锁定为原文编号（(2.1)–(2.27)、(3.1)–(3.58)、(4.1)–(4.34)、(A.1)–(A.46)，共 **165** 个），
  不随排版漂移；原文无编号公式不编号。
- 图表：图题译为中文并标注“（原文 Figure N，原文 PDF 第 P 页）”；表 1、表 2 用 `booktabs` 按原表重建。
- 参考文献按原文逐条照录英文，未翻译；文献编号与原文一致。

## 4. 质量指标与核对方法

| 项目 | 数量/状态 |
|---|---|
| 带编号公式 | 165 / 165（脚本逐条核对 `\tag`，无缺号、无重号） |
| 插图 | 10 / 10（图 1–图 10，均含中文图题与原文位置） |
| 表格 | 2 / 2（表 1 挠率类、表 2 E₈ 破缺与粒子谱） |
| 参考文献 | 136 条（照录） |
| 源码批注 | 110+ 条（74 条 Tutor Note、28 条原文疑误、8 条存疑、1 条背景补充；多行批注按末行计） |
| 编译 | XeLaTeX 两遍通过，0 error |
| 版面 | 60 页；目录、页眉、公式编号、图表编号均正常 |

核对方式：机器辅助初译后，逐页对照**原文页面图像**核录全部公式与图表（文字层被拆碎的公式一律不采信），
再用脚本 `tools/verify.py` 检查公式编号完整性、Unicode 数学符号、图表引用、页锚与结构，
最后以 `tools/test_fragment.py` 与整稿编译验证。

## 5. 已知局限

1. 本译本由 AI 辅助生成并经逐页核对、编译验证，属**学习用参考译本**；凡与原文有出入处，一切以原文为准。
2. 原文中的笔误、拼写瑕疵、缺失变音符号均**照录并出注**（完整清单见 `REVIEW-NOTES.md`），
   未做静默修正；个别符号（如 (A.29) 与 (A.34) 之间的陈类符号约定）原文本身不自洽，已在批注中给出核对建议。
3. 插图由原 PDF 内嵌位图剥离，部分图（如原文 Figure 2、Figure 4）原始分辨率有限，放大印刷时可能偏软。
4. 附录的小节层级按原文的“•/–”项目符号还原为 `\subsection*`/`\subsubsection*`，标题的视觉层级与原文一致，
   但并非原文的严格编号结构（原文附录本无编号小节）。
5. 页锚注释中的“第 N 页”指**原文 PDF 页码**；本译本自身的页码因排版不同而不同，二者请勿混淆。

## 6. 版权

原文 © Lara B. Anderson & Mohsen Karkheiran，采用 CC BY-NC-ND 4.0 许可（PoS 会议文集）。
本译文仅供学习研究，不得用于商业用途；引用请以原文为准并注明出处。
