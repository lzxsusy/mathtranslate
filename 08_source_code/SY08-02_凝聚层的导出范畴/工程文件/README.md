# 《凝聚层的导出范畴及其之间的等价》中文译注本 · 项目说明

## 一、这是什么

D. O. Orlov 2003 年综述 *Derived categories of coherent sheaves and equivalences between them*
（Russian Mathematical Surveys 58:3, 511–591；俄文原刊 Uspekhi Mat. Nauk 58:3, 89–172）的
**完整中文译本**，附四份附录：

| 附录 | 内容 |
| --- | --- |
| A | 英中术语对照表（约 200 条，含译名取舍原则，另附「按中文检索」） |
| B | 译注汇编（正文可见译注 + 不进正文的校勘记，按原书页码排列） |
| C | 概念批注：与 nLab 的对照（12 个概念的 nLab 条目、定义差异、读法建议） |
| D | 定理与定义索引（111 条陈述 + 55 个编号公式，标注原书页码） |

**成品**：`成品/凝聚层的导出范畴_中文译注本.pdf`，B5 开本，共 138 页（含封面、说明、目录、四个附录与参考文献）。

正文每章末有「本章回顾与评注」，每节首有「本节重点」，均为译者所加，非原书内容。

## 二、底本与页码

- 原书 81 页（书页 511–591），本书逐页对照：源码中每个原书页起首写 `% [原文 p.N]`，
  不进版面；附录 B、D 中给出的「原书 p.N」即印刷页码。
- PDF 页码与原书书页的换算：**书页 = PDF 页 + 510**（如 PDF 第 35 页 = 原书 545 页）。
- 陈述编号、公式编号一律照抄原书（定义 2.2.3、定理 3.2.1、式 (21) …），不用本书自动编号。
- 原书笔误、页图与文字层不一致之处**照录并批注**，不静默改字；这类批注集中在附录 B 的「［校勘］」条目。

## 三、编译

```powershell
cd src
lualatex -interaction=nonstopmode main.tex
lualatex -interaction=nonstopmode main.tex   # 目录与交叉引用需二至三遍
lualatex -interaction=nonstopmode main.tex
```

- 引擎：LuaLaTeX（XeLaTeX 亦可，但需注意 `enumitem` 的 `description` 用法差异）。
- 中文字体：ctex 默认字体集；西里尔字母由 `\cyrfont`（Times New Roman，缺则 DejaVu Serif）承担。
- 依赖：`ctex`、`amsmath/amsthm`、`tikz`+`tikz-cd`、`tcolorbox`、`geometry`、`fancyhdr`、`hyperref`、`newunicodechar`、`enumitem`。
- 生成物：`main.pdf`。目录：`src/chunks/` 按块组织，`main.tex` 用 `\InputIfFileExists` 逐块注入，
  缺某个块也能编译（便于分块施工）。

## 四、目录结构

```
源码/
  main.tex              主文件（frontmatter → 目录 → 正文各块 → 附录 → 参考文献）
  preamble.tex          版式、陈述环境、记号宏、译注盒子、TikZ 图
  frontmatter/          封面（titlepage.tex）、译注本说明（note.tex）
  chunks/               正文分块 + 附录 A–D + 参考文献
  figures/              图（现全部为源码内 TikZ，目录留空）
工程文件/
  STYLE_GUIDE.md        体例（陈述环境 API、译注两类、来源分级、语言与 LaTeX 规则）
  BRIEF.md              分块表与质量闸门
  deliverable/          成品 PDF、README、研读札记、术语对照表、译注汇总、阅读参考指南、统计数据
work/
  text/、src/           逐页与逐块的文字层提取（原文）
  pages/                原书 81 页 200 dpi 页图（核对公式与图用）
  reports/              各块译者报告（六节：范围/内容/陈述/公式/图/存疑）
  proposals/            各块术语提案
  glossary.tsv          冻结术语表
  通读笔记.md、疑点清单.tsv
```

## 五、体例速查（给要接着改的人）

- 陈述：`\begin{theorem}[附加名]{2.1.8}`，编号必填、照抄原书；带 `p` 后缀者证明紧随其后。
- 译注（可见）：`\yizhu{…}`，末尾必须有 `【来源：…】` 或 `〔译者按（上下文推断，无外部依据）：…〕`。
- 校勘（不进正文）：`% [Tutor Note: …]`，由 `tools/gen_notes.py` 汇总进附录 B。
- 公式：`\begin{equation} … \tag{21} \end{equation}`。
- 交换图：`\diag{ … }`（内部 tikzcd，`&` 写作 `\&`），一律 TikZ 重排，不贴原书位图。
- 页标记：`% [原文 p.545]`，每页一行。

## 六、来源与致谢

底本版权属原作者与出版方；本译注本仅供学习与研究，不用于商业用途。
nLab 条目引用按 nLab 的 CC BY-SA 条款注明出处（见附录 C 每条目的「出处」行）。
