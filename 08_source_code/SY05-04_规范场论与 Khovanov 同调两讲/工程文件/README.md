# 1603.03854 中译本（规范场论与 Khovanov 同调两讲）

Edward Witten, *Two Lectures On Gauge Theory And Khovanov Homology*,
arXiv:1603.03854v2（2017-01-31，27 页）之中文本土化 LaTeX 译本，附学术审校批注。

## 文件清单

```
1603.03854/
├── 1603.03854_zh.tex     主文件（约 1770 行，含全部正文/公式/图/批注）
├── 1603.03854_zh.pdf     已编译成品（22 页，A4）
├── figs/
│   ├── fig01.png … fig13.png   从原 PDF 裁切的 13 幅插图（300 dpi）
├── 审校报告.md            公式核对表、原文笔误清单、术语表、阅读警示
└── README.md              本文件
```

## 编译

```text
xelatex 1603.03854_zh.tex
xelatex 1603.03854_zh.tex
```

- 需要 XeLaTeX（或 LuaLaTeX）；`ctexart` 文档类，自动使用系统中文字体。
- 本成品已用 **Tectonic 0.17**（XeTeX 内核，`tectonic -X compile`）实测编译：
  22 页，0 error、0 missing character，仅 1 处 0.5 pt 的 overfull hbox（可忽略）。
- 所需宏包：`ctex, amsmath, amssymb, amsthm, mathrsfs, bm, graphicx,
  geometry, xcolor, caption, enumitem, float, hyperref`（均为标准包）。
- 图文件按 `figs/figNN.png` 引用，请保持目录结构。

## 译本结构

| 部分 | 内容 |
|---|---|
| 标题页 | 中译标题、作者、摘要、译者说明 |
| 第一讲 | 从 Jones 多项式到 Hecke 修正、Bogomolny 方程、KW 方程、Morse 范畴化 |
| 第二讲 | $q$-分次与边界条件、Nahm 极点解、Weitzenböck 公式族、带纽结模型解与椭圆性 |
| 附录 A | $(0,2)$ 六维理论的扭曲与紧化：单/双分次 Khovanov 同调的物理来源 |
| 参考文献 | 26 条，与原编号一一对应 |

## 批注

- `% [Tutor Note: …]`：LaTeX 注释，编译后不可见。分三类：
  **易错预警**（符号、指标、归一化约定）、**含糊点拨**（作者以
  “obvious / a short calculation” 略去的证明及应查文献）、**原文笔误**。
- 各节开头“本节重点（Key Takeaways）”：译者所加阅读导引（原文无此内容）。
- 公式编号完全保留原文 `(1.1)–(2.17)`；原文未编号的三个公式标为
  `(∗) (†) (‡)` 并在批注中注明。

## 说明

- 正文翻译以“无损”为唯一标准：不增删论证，不改动作者的行文逻辑与语气。
- 图注译为中文并标注“原文 Figure N，第 X 页”；图内文字保持原样。
- 原文笔误（如 “Langlanda-GNO”、“the we can think”、“Weitenbock”）
  一律照录并在批注/审校报告中指出，未擅自改动。
- 已实测编译通过（见上）；另有环境配对、引用、文献键、图片路径、
  括号平衡等静态检查记录（详见《审校报告》§8）。
