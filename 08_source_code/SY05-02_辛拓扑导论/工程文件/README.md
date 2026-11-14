# 辛拓扑导论（A Symplectic Prolegomenon）· 中文译注版

> 原文：**Ivan Smith**, *A Symplectic Prolegomenon*, arXiv:1401.0269v2（`math.SG`，2014 年 9 月修订版，47 页，11 幅插图）。
> 本目录是其**中文结构化 LaTeX 译注本**：公式逐字符保留、图表自原 PDF 以 400 dpi 裁出、附学术级批注与「本节重点」。
>
> 成品：**53 页 PDF · 约 3.4 万汉字 · 76 条审校批注 · 12 幅图**（含原文 1 幅无编号示意图）。

---

## 一、目录结构

```
1401.0269v2(1)(1)/
├── 1401.0269v2(1)(1).tex    ← 单文件完整源码（自包含，推荐直接用）
├── 1401.0269v2(1)(1).pdf    ← 编译好的成品（xelatex）
├── main.tex                 ← 模块化主文件（\input sections/*.tex）
├── preamble.tex             ← 导言区：宏包、定理环境、「本节重点」盒子、全部记号宏
├── sections/
│   ├── s00-front.tex        ← 封面、题词、摘要、译者说明、凡例、术语表
│   ├── s01-intro.tex        ← §1 引言
│   ├── s02-background.tex   ← §2 辛拓扑背景
│   ├── s03a-floer.tex       ← §3 Floer 上同调（3.1–3.5）
│   ├── s03b-floer.tex       ← §3 Floer 上同调（3.6–3.9）
│   ├── s04a-fukaya.tex      ← §4 Fukaya 范畴（4.1–4.4）
│   ├── s04b-fukaya.tex      ← §4 Fukaya 范畴（4.5–4.8）
│   ├── s05-examples.tex     ← §5 例子
│   ├── s06-further.tex      ← §6 若干方向
│   └── s07-biblio.tex       ← 参考文献（保留英文原样，106 条）
├── figs/                    ← 12 幅图（自原 PDF 精确裁剪，400 dpi，PNG）
├── 审校批注索引.md            ← 全部 % [Tutor Note: ...] 批注的逐条索引
├── QA-REPORT.md             ← 自动质量检查报告（规模、批注数、英文残留、重复 label）
└── README.md                ← 本文件
```

## 二、编译

```bash
xelatex 1401.0269v2(1)(1).tex     # 两遍，第二遍生成目录与交叉引用
```

或模块化编译：

```bash
xelatex main.tex
xelatex main.tex
```

依赖 TeX Live（`ctex, amsmath, amssymb, amsthm, mathrsfs, euscript, xy, graphicx,
xcolor, hyperref, geometry, epigraph, etoolbox, caption, enumitem, tcolorbox,
array, booktabs, longtable`）。字体：Windows 下 `ctex` 自动使用宋体/黑体；Linux/macOS
可用 `\documentclass[UTF8, fontset=fandol]{ctexart}` 或安装相应中文字体。

## 三、翻译与排版约定

1. **数学无损**：所有公式、上下标、指标、$\bZ_2$-分次、符号约定与原文逐字符一致；
   公式编号按节编号，与原文完全对应（如 (3.7)、(4.12)），便于逐式对照。
2. **术语统一**：采用中文学界通行译名（Floer 上同调、Fukaya 范畴、Dehn 扭转、消没圈、
   和乐、单值、通量……），人名与专名保留英文；英汉对照见文中「术语表」。
3. **图表还原**：12 幅图均自原 PDF 以 400 dpi 裁出（含原文一幅未编号示意图、一幅原为
   `picture` 环境手绘的亏格 2 曲面图），图题译为中文并注明原文位置（Figure $n$，第 $p$ 页）。
4. **本节重点**：每节开头有「本节重点（Key Takeaways）」盒子，概括核心图像、工具与结论。
5. **审校批注**：源码中插入 `% [Tutor Note: ...]` 整行注释（PDF 中不显示），分三类：
   易错预警（指标、符号、分次、定向）、含糊点拨（作者跳过的证明依赖什么）、概念辨析。
   全部批注已索引于《审校批注索引.md》，亦可在源码中检索 `Tutor Note`。

## 四、与原文的已知差异

- 原文使用 `mathabx` 宏包，该宏包只提供 Metafont 字型、XeLaTeX 无法嵌入，故译本略去；
  正文所需 `\pitchfork`、`\maltese` 等符号改由 `amssymb` 提供，数学含义不变。
- 原文第 7 幅图（亏格 2 曲面）为 `picture` 环境手绘矢量图，译本改用同位置裁剪的图片。
- 其余排版（页边距、字号、定理编号方式）按中文单栏 A4 阅读习惯重排，不影响内容。

## 五、关于底本作者与主题（重要）

委托原始说明中提及 Edward Witten 的文章；经核对，本 PDF 的实际作者是 **Ivan Smith**（剑桥大学），
内容为辛拓扑与导出 Fukaya 范畴的数学综述，并非 Witten 的物理论文。译文据实以底本为准，
未作任何「向物理靠拢」的改写。Witten 关于镜像对称与拓扑弦的物理论述与本主题密切相关，
可作背景参考，但不应与本文混为一谈。

## 六、致谢与免责

译文与批注由 DSH 学术翻译组完成；数学内容一律以原文为准，译者批注仅供理解参考。
若发现公式或术语问题，欢迎直接在源码上修订（所有内容均为可编辑的 LaTeX 源码）。
