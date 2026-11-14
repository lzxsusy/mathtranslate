# 量子场论的数学思想与概念（中文精译 · 学术审校版）

**原文：** Pavel Etingof, *Mathematical Ideas and Notions of Quantum Field Theory*,
arXiv:2409.03117v1（2024 年 9 月 4 日提交；MIT 数学系研究生课程讲义，2002 年与 2023 年讲授），206 页。
**说明：** 本任务原始需求中曾提及 Witten 的文章；经核对，`2409.03117v1.pdf` 的实际作者是 MIT 的
Pavel Etingof（文末致谢中亦感谢 Witten 等）。本译本严格以该 PDF 及其 arXiv LaTeX 源码为底本。

---

## 一、交付内容

```
2409.03117v1_中文精译_量子场论的数学思想与概念/
├─ main.tex              主文件（标题页、译者说明、目录、各章 \input 顺序）
├─ preamble.tex          导言区（页面、中文支持、定理环境、图题宏、要点环境）
├─ macros.tex            原文导言区的全部记号宏，逐字照搬，保证公式记号无损
├─ sections/             17 个分节 .tex（sec00-intro … sec13-cft）+ 参考文献 sec-refs.tex
├─ figures/              24 幅图（fig-01.png … fig-24.png，600 dpi）
│   └─ 原图矢量代码.tex   原文 eepic/pict2e 绘图代码（备查、可重排）
├─ main.pdf              已编译成品（175 页）
├─ REVIEW-NOTES.md       全书 % [Tutor Note] 批注汇编（99 条，按章索引）
├─ glossary.md           术语对照表（强制统一译名）
├─ STYLE_GUIDE.md        翻译与审校工作规范
└─ 编译工具/
    ├─ build.bat         一键编译脚本
    └─ tectonic.exe      TeX 引擎（XeTeX 内核，自带宏包管理）
```

## 二、编译方法

**方式一（推荐，零配置）**：双击 `编译工具/build.bat`。它调用同目录的 `tectonic.exe` 以 XeTeX 内核编译
`main.tex`，首次运行需联网下载缺失宏包，之后离线可编译。产物为 `main.pdf`。

**方式二（本机已装 TeX Live / MiKTeX）**：在根目录执行
```
xelatex main.tex
xelatex main.tex
```
必须使用 **XeLaTeX**（中文由 ctex + Fandol 字体支持）。若本机字体环境不同，可把 `preamble.tex` 中
`\usepackage[UTF8,fontset=fandol]{ctex}` 改为 `fontset=windows` 或 `fontset=macnew`。

## 三、翻译与审校说明

1. **底本**：以 arXiv:2409.03117v1 的 LaTeX 源码（`qftlect.tex`）为权威底本逐段精译，并以 PDF 版核对版式与图表。
   所有数学公式、`\label`、`\cite`、`\ref`、定理环境结构逐字保留、未作改写。
2. **公式无损校验**：每一分节都用脚本把译文与底本的**行间公式序列**逐字比对（忽略空白与 `\text{}` 内容），
   并比对**行内公式多重集合**、`\label`/`\cite`/`\ref` 键集合、环境数量；全部通过后才进入总装。
   校验脚本见 `STYLE_GUIDE.md` 第 6 节所述流程（`tools/check_section.py`，随工作目录提供）。
3. **图表**：原文 24 幅图由 `eepic/pict2e` 矢量绘制。本译本将每幅图单独重排、以 600 dpi 输出 PNG，
   用 `\begin{figure}` + `\includegraphics` 插回原位；图题译为中文，并在图题后以灰色小字标注
   “原文：第 X 页，Figure N”。原文图内标注文字保留原样（重排为中文会破坏原图坐标与版式）。
   原图矢量源码完整保留在 `figures/原图矢量代码.tex`，需要时可自行重排。
4. **批注**：全书 99 条 `% [Tutor Note: ...]`，分“易错预警”（符号约定、指标、$i$ 因子、$2\pi$ 因子、
   归一化、Grassmann 符号、正规序等）与“含糊点拨”（作者跳步处所依据的定理与文献）。批注在源码中可见，
   编译后不显示；汇编见 `REVIEW-NOTES.md`。
5. **每章要点**：各章开头有 `keytakeaways` 环境，列出物理图像、数学工具、关键结论，为译者所加（非原文内容）。
6. **术语**：按 `glossary.md` 统一；人名、专名保留拉丁字母（Feynman、Witten、Deligne、Berezinian 等）。

## 四、与原书的差异（如实说明）

- 原文 **Index（索引）** 由 `makeindex` 生成，本译本未收录（约 235 个索引项已从源码移除）；
  PDF 书签与目录完整保留，可按关键词检索。
- **参考文献**保留英文原条目（共 9 条），未作翻译；正文 `\cite` 链接正常。
- 原文个别笔误保留原样并在批注中指出（例如引言 “a number of ins applications” 当为 “nice applications”）。
- 原文页码标注按 arXiv v1 的 PDF 页码；印刷版（AMS GSM 254，405 页）页码不同。

## 五、统计

| 项目 | 数值 |
|---|---|
| 原文页数 | 206 |
| 中译本页数 | 175 |
| 正文汉字数 | 约 82232 |
| 行间公式 | 886 个（逐字无损） |
| 图 | 24 幅（全部重排为图片，图题已译） |
| 审校批注 | 99 条 |
| 分节文件 | 18 个（含参考文献） |

---

*本译本仅供学术研究与教学参考；原文版权归原作者与 AMS 所有。*
