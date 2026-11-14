# 二维 $N=2$ 理论的相 —— 中文译注本

Edward Witten, *Phases of $N=2$ Theories in Two Dimensions*
IASSNS-HEP-93/3, arXiv:hep-th/9301042v3 [hep-th], 1993 年 1 月（v3: 1993-02-18），原文 92 页。

本目录是全文的**简体中文结构化 LaTeX 译注本**：逐段对译、公式逐式对照原文页面图像核对、
章节/公式/文献编号全部保持原样，并在源码中以注释形式插入学术审校批注。

---

## 一、交付清单

| 文件 | 说明 |
|---|---|
| `main.tex` | 全书主文件（导言区、标题页、摘要、译者说明、目录、分片装配） |
| `main.pdf` | 编译产物（A4，11pt，约 45 页） |
| `sections/s01-intro.tex` … `s07-references.tex` | 14 个正文分片（按原文章节切分，可单独编辑） |
| `sections/s05a2-comment.tex` | 补译分片：第 58 页顶部 §5.2 收尾 + "A General Comment" |
| `SPEC.md` | 翻译与排版契约（术语、公式、批注、结构的硬性规范） |
| `GLOSSARY.md` | 术语表（约 200 条，强制统一） |
| `VERIFY.md` | 独立审校规范 |
| `notes/review-report.md` | 审校报告：逐片审校结论、原文疑误清单、遗留问题 |
| `notes/consistency-audit.md` | 全稿一致性审计（公式交叉引用、术语变体、脚注、标题层级） |
| `build.ps1` | 一键编译脚本 |
| `tools/` | 辅助脚本：页面裁剪放大、分片 lint、全稿检查、排版后处理 |

**图、表**：原文经矢量图形与位图双重检测，**全篇无插图、无带框表格**（92 页中 0 个矢量图元、
0 个嵌入位图），因此本译本不含任何从 PDF 剥离的图像文件；图表在原文本就不存在，并非翻译遗漏。
（正文中所有"对齐数值"都是行间公式而非表格，已在正文用 `equation` 环境如实还原。）

---

## 二、编译

```powershell
# 方式 A：TeX Live（推荐，两遍以生成目录）
xelatex main.tex
xelatex main.tex

# 方式 B：tectonic（无需安装 TeX Live，自动拉取所需宏包）
tectonic -X compile main.tex
```

- 中文支持使用 `ctex` 的 `fandol` 字库（跨平台、不依赖系统字体，TeX Live 与 tectonic 均自带）。
  在 Windows 上若希望改用系统宋体/黑体，把 `main.tex` 中
  `\usepackage[UTF8,scheme=plain,fontset=fandol]{ctex}` 改为 `fontset=windows`。
- 本机使用 tectonic 时需设置缓存目录（沙箱环境）：
  `$env:TECTONIC_CACHE_DIR="<workspace>\.tools\texcache"`，或直接运行 `build.ps1`。
- 引擎要求 **XeLaTeX**（ctex + 中文字体）；pdfLaTeX 需改用 CJK 方案，不建议。

---

## 三、结构对照

原文 6 节、13 个子节；译文分片与原文章节一一对应：

| 原文 | 译文分片 | 原文页（PDF 页 = 印刷页） |
|---|---|---|
| 1. Introduction | `s01-intro` | 2–4 |
| 2. Field Theory Background | `s02a-fieldtheory`, `s02b-fieldtheory` | 4–15 |
| 3. The C-Y/L-G Correspondence | `s03a-model`, `s03b-singularity`, `s03c-applications`, `s03d-twisted` | 16–43 |
| 4. Some Geometrical Background | `s04-geometry` | 44–48 |
| 5. Generalizations | `s05a-wps-toric`, `s05a2-comment`, `s05b-grassmann-intersect`, `s05c-topology` | 49–74 |
| 6. Extension to (0,2) Models | `s06a-superfields`, `s06b-models` | 75–86 |
| References | `s07-references` | 87–92 |

每个分片在每页起始处带锚点注释（`% ==== 原文 PDF 第 N 页 ====`），便于与原文逐页对照。

---

## 四、翻译与审校流程（三阶段）

1. **语义级翻译**：14 个分片并行翻译。正文措辞参考 PDF 文字层，**但一切公式以 160 dpi 整页图像
   为唯一权威**（文字层会把分式、上下标、希腊字母拆散，已反复验证不可信）。每个带编号公式
   用 `\tag{x.y}` 锁死原编号；原文非编号公式保持不编号。
2. **独立逐式审校**（第二遍，另一人）：逐式对照页面图像核对符号；检查漏译、脚注、无编号小标题；
   复核每条 `% [Tutor Note]` 的技术断言（有无幻觉）。修正记录汇总在 `notes/review-report.md`。
3. **全稿一致性审计**：公式交叉引用（"式 (x.y)"）、术语变体、Unicode 数学符号、页码锚点覆盖、
   标题层级、脚注计数、断页衔接。

自动检查（`tools/check_book.py`）的硬指标：

- 带编号公式 **188 个**，编号连续性：§1 1.1–1.3、§2 2.1–2.35、§3 3.1–3.52、
  §4 4.1–4.3、§5 5.1–5.48、§6 6.1–6.47 —— **无缺号、无重号、无自创编号**；
- 页码锚点覆盖原文第 2–92 页（91 页，缺页 0）；
- 代码区无 Unicode 数学符号；无 `\ref`/`\cite` 式动态编号（全为字面编号，杜绝错位）。

---

## 五、记号与排版约定

- **编号**：公式 `(x.y)`、文献 `[n]`、章节号一律照抄原文；正文引用公式写「式 (x.y)」，不用 `\ref`。
- **微分号**：按原文排作**直立体** `\mathrm{d}`（如 `\mathrm{d}^4x`、`\mathrm{d}s_i`）。
- **射影空间**：按原文粗体排作 `\mathbf{CP}^{n-1}`、`\mathbf{WCP}^{n-1}_{q_1,...}`。
- **人名、模型名不译**：Calabi–Yau、Landau–Ginzburg、Wess–Zumino、Fayet–Iliopoulos、Gepner 等。
- **数学环境内一律不使用中文**，中文只出现在 `\text{}`/`\mbox{}` 中。
- 首行缩进、行距、页眉（"二维 N=2 理论的相"/"Witten, 1993（中文译注本）"）统一。

---

## 六、批注系统（源码注释，四类标记）

所有批注都是 LaTeX 注释，**不影响排版输出**，打开 `.tex` 即可阅读；搜索关键字可定位：

| 标记 | 用途 | 数量 |
|---|---|---|
| `% [Tutor Note: …]` | 推导补足、易错预警、物理图像说明 | 见审校报告 |
| `% [原文疑误: …]` | 已判定为原文笔误处，附依据与建议 | 见审校报告 |
| `% [存疑: …]` | 无法从图像确证但疑有问题处 | 见审校报告 |
| `% [背景补充: …]` | 对中文读者构成实质门槛的术语/背景 | 见审校报告 |
| `% [跨页接续: …]` | 原句跨页处的切分说明 | — |

---

## 七、说明

- 原文脚注全部保留为 `\footnote`；译文脚注编号由 LaTeX 重新生成，故与原文页码上的编号不同，
  这是排版系统的正常行为，不影响内容对应。
- 原文若干笔误（`sympectic`、`b_1 = b_1 = 0`、`Little is understand` 等）按「照录原文 + 批注」处理，
  未擅自改写；详见 `notes/review-report.md` 的「原文疑误清单」。
- 文献列表保留英文原貌（书目信息不可翻译），仅修正 TeX 连字与断行连字符，疑似作者姓名拼写问题
  已在注释中标出。
