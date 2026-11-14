# 四维规范场论中的纽结不变量（中译本）

> 底本：**Davide Gaiotto & Edward Witten, _Knot Invariants from Four-Dimensional Gauge Theory_,**
> arXiv:1106.4789v1 [hep-th], 23 Jun 2011（原文 120 页，含 29 幅图）。

本目录是对该论文的**中文本土化 + 结构化 LaTeX 源码**，附学术级审校批注，并已用 XeLaTeX 编译成 93 页 PDF。

---

## 一、目录结构

```
1106.4789/
├── 1106.4789_中译本.pdf     ← 编译好的中译本（93 页）
├── main.tex                 ← 主文件（\input 各 chunk）
├── preamble.tex             ← 导言区：ctex、数学宏包、原稿自定义宏、“本节重点”框等
├── frontmatter.tex          ← 标题页、中文摘要、译者说明、记号约定
├── chunk01.tex … chunk17.tex← 正文与附录（按原稿章节顺序切分，可独立编辑）
├── glossary.tex             ← 附录 D：英中术语对照表
├── bibliography.tex         ← 参考文献（保留英文原貌）
├── figs/
│   ├── Fig01.png … Fig29.png← 从原 PDF 逐幅裁剪的 29 幅图（400 dpi）
│   └── contact.png          ← 全部图片的缩略图总览（校对用）
├── 审校批注汇编.md          ← 121 条 % [Tutor Note: ...] 批注按章节汇编
├── 翻译规范.md              ← 本项目采用的翻译规范、术语表与验收标准
└── README.md                ← 本文件
```

## 二、编译

主文件按 **XeLaTeX** 编写（中文由 `ctex` 处理）：

```bash
xelatex main.tex
xelatex main.tex        # 第二遍生成目录与交叉引用
```

依赖宏包：`ctex, amsmath, amssymb, bm, graphicx, xcolor, tcolorbox, longtable,
booktabs, caption, hyperref`（TeX Live / MiKTeX 完整安装均自带）。

亦可使用 [Tectonic](https://tectonic-typesetting.github.io/)：
`tectonic -X compile main.tex`。

> 本 PDF 即由 Tectonic（XeTeX 引擎，TeX Live 2026 宏包集）编译；日志无错误、无未定义引用。

## 三、翻译与审校说明

1. **数学无损**：译文以作者原始 LaTeX 源码为底本，**所有公式逐字保留**（仅译出
   `\text{...}` 中的说明性文字）。合稿后用脚本对每个 chunk 做了
   “行内数学 + 显示公式环境”的多重集比对，与英文原文逐一对应；公式编号、
   `\label`、`\ref`、`\cite` 均与原文一致。
2. **术语本土化**：采用中文理论物理界通行译名（规范场论、和乐、反常、共形块、
   oper、Lefschetz thimble/针 等），人名与数学专名保留原文；详见附录 D。
3. **图表**：29 幅图全部从原 PDF 按图注位置精确裁剪（400 dpi），以 `figure`
   环境插入原文对应位置；图注译为中文并标注原稿页码。
4. **审校批注**：源码中含 **121 条** `% [Tutor Note: ...]` 批注，分五类：
   - 易错点（自对偶投影符号、$q$ 的分数幂、指标升降、留数约定等）；
   - 省略证明（作者写 “it is obvious/clearly” 而跳过的泛函分析或代数步骤）；
   - 约定差异（本文 $G$/$G^\vee$ 记号与文献相反、$\t$ 的参数地位等）；
   - 物理图像（用一句话点破公式的几何/物理含义）；
   - 原文疑似笔误（**不修改公式**，只标注，如 `\ref{nahmpole}` 应为 `\ref{nahm}`、
     附录 B 与附录 A 重复使用 `\label{mct}` 等）。
   全部批注另见 `审校批注汇编.md`。
5. **结构化**：8 个正文章节 + 3 个附录的每一节开头均有“本节重点（Key Takeaways）”
   方框，提炼物理图像、数学工具与主要结论；源码按章节切块，缩进规范，便于直接增改。

## 四、与原稿的已知差异

- 版式由 JHEP 单栏改为 `article + ctex`，页数由 120 页变为 93 页（中文更紧凑）。
- 原稿用 TeX 传统字体族 `cmmib/eurm/eusm`；XeLaTeX 下分别以
  `\boldsymbol` / `\mathrm` / `\mathcal` 等价替代（见 `preamble.tex`），不影响公式内容。
- 原稿附录 A、B 重复使用同一 `\label{mct}`（原稿交叉引用错误）；译文将附录 B 的标签改为
  `mctb` 以修正引用，公式本身未动，并加批注说明。
- 原稿 “参考文献” 条目保持英文原貌（学术惯例）。

## 五、快速核对建议

- 任取一页公式，与 `1106.4789.pdf` 原稿同编号公式逐符号对照；
- 对照 `figs/contact.png` 检查图片裁剪是否完整；
- 用编辑器的 “查找” 搜索 `% [Tutor Note:` 查看批注，或读 `审校批注汇编.md`。
