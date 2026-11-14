# 中文精译 + 学术审校版 LaTeX 工程说明

**原文**：A. Balasubramanian, J. Teschner,
*Supersymmetric field theories and geometric Langlands: The other side of the coin*,
arXiv:1702.06499v2（String-Math 2016 会议文集）

**成品**：`main.pdf`（48 页）+ `main.tex` 及其全部依赖；已实测编译通过（0 error，0 missing character）。

---

## 一、目录结构

```
1702.06499v2_中文精译_几何Langlands/
├── main.tex              主文件（标题页、摘要、目录、各节 \input、参考文献、译校说明、术语表）
├── preamble.tex          导言区：宏包、版心、中文字体、定理环境、全部记号宏
├── sections/
│   ├── sec1.tex          第 1 节  引言
│   ├── sec2.tex          第 2 节  综述（5 个子节）
│   ├── sec3.tex          第 3 节  余二维缺陷与面算符
│   ├── sec4.tex          第 4 节  配分函数与共形块
│   ├── sec5.tex          第 5 节  另一类面算符
│   ├── sec6.tex          第 6 节  重新得到几何 Langlands 对应
│   ├── sec7.tex          第 7 节  对 sigma 模型的诠释？
│   └── sec8.tex          附录      Hitchin 模空间（\appendix 之后）
├── references.tex        参考文献（由原文 .bbl 改写为内嵌 thebibliography，50 条）
├── glossary.tex          术语译名对照表
├── trans_note.tex        译校说明（底本、方法、图表清单、原文可疑处 14 条）
├── main.pdf              已编译成品
├── README.md             本文件
├── STYLE_GUIDE.md        翻译工作规范（术语统一、公式保真、批注格式）
├── verify_tex.py         静态自检脚本（括号/环境/宏/引用/批注计数）
├── fonts/                Fandol 中文字体（离线编译 tectonic 时使用）
└── 编译工具/
    ├── tectonic.exe      自包含 TeX 引擎（首次使用会联网下载约 100 MB 宏包）
    └── build.bat         一键编译脚本（成功后生成 main.pdf）
```

## 二、如何编译

### 方式 A：本机已装 TeX Live / MiKTeX（推荐）

```bat
xelatex main.tex
xelatex main.tex
```

- **必须用 XeLaTeX**（中文支持依赖 `ctex` 宏包；pdfLaTeX 无法直接编译）。
- 使用 `ctex` 默认字体方案时，Windows 会自动选用系统自带的 SimSun/SimHei；若本机无中文字体，
  可在 `preamble.tex` 中把 `\usepackage[UTF8]{ctex}` 改为 `\usepackage[UTF8,fontset=fandol]{ctex}`
  并使用本目录 `fonts/` 中的 Fandol 字体。

### 方式 B：用附带的 tectonic（无需安装 TeX）

双击 `编译工具\build.bat`。脚本会设置本地缓存目录并调用同目录的 `tectonic.exe`。
首次编译需要联网下载宏包（约 100 MB，只需一次）。也可手动执行：

```bat
set TECTONIC_CACHE_DIR=%~dp0..\_tectonic_cache
编译工具\tectonic.exe -X compile --keep-logs --outdir . main.tex
```

> 说明：`main.pdf` 即由 tectonic（XeTeX 内核）编译生成，排版引擎与 xelatex 相同；
> 字体方面 tectonic 走 TeX Live 的 Fandol 方案，本机 xelatex 走系统字体，字形略有差异，内容完全一致。

## 三、翻译与审校说明

1. **底本**：以 arXiv 公开的 LaTeX 源码为主、PDF 为辅；公式、指标、上下标、希腊字母逐字保留，
   未重排、未化简。原文中被作者注释掉的公式保持注释状态。
2. **术语**：统一采用 `glossary.tex` 中的译名（如 gauge theory=规范场论、holonomy=和乐、
   anomaly=反常、conformal block=共形块），人名保留拉丁字母。
3. **批注**：正文源码中插入 **44 条** `% [Tutor Note: ...]` 批注，分“易错提醒”（指标/符号约定/
   整体因子）与“跳步点拨”（作者略去的证明与所用定理）两类。批注为 LaTeX 注释，不影响排版，
   阅读 `.tex` 源码时可见。
4. **本节重点**：每节开头设 `keytakeaways` 环境，提炼物理图像、数学工具与关键结论（译者所加，非原文内容）。
5. **图表**：经核查原文 PDF **不含任何图像对象**（35 页，图像计数为 0），故无图可裁；
   原文两张表格（第 3、5 节的膜支撑方向表）已原样保留并翻译表头。
6. **原文可疑处**：共整理 14 条，集中于 `trans_note.tex` 第三节，例如 §2.5 的 “Langslands” 拼写、
   §3 式 (3.3) 的 $\mathfrak t_+/\mathfrak t_-$ 不一致、§4 的系统性指标错位、附录括号不配对与
   $\mathrm{End}\to\mathrm{End}_0$ 等。译文一律保留原样、另以批注说明。

## 四、自检

```bat
python verify_tex.py
```

检查花括号配平、环境配对、未定义宏、`\cite` 与 `\bibitem` 对应、`\ref` 与 `\label` 对应、
批注条数。注意：脚本中“数学模式内全角标点”一项对跨行行内公式无法可靠配对，其结果仅作提示，
**以实际编译为准**（本次编译 0 error、0 missing character、0 undefined reference）。
