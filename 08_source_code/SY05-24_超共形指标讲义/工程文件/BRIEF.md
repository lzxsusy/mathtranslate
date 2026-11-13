# BRIEF.md — SY05-24《超共形指标讲义》中文译注本 · 施工总纲

## 0. 一句话

把 Abhijit Gadde, *Lectures on the Superconformal Index*（arXiv:2006.13630v1，32 页）全文译成中文，保留全部 110 条编号公式、8 个编号习题、2 张表格，术语按 `glossary.tsv` 冻结；成品由 Lead 统一编译。

## 1. 底本事实

| 项 | 值 |
|---|---|
| 标题 | Lectures on the Superconformal Index |
| 作者 | Abhijit Gadde（Department of Theoretical Physics, TIFR, Mumbai 400005） |
| 出处 | Prepared for submission to JHEP；TIFR/TH/20-20；arXiv:2006.13630v1 [hep-th]，24 Jun 2020；YRISW 2020 冬季学校讲义，拟刊 JPhysA 专辑 |
| 页数 | 32 页（PDF 页 1 是 JHEP 标题页；**PDF 页 = 印刷页码 + 1**） |
| 文件 | `工程文件\底本_arXiv-2006.13630.pdf` |
| 结构 | §0 讲义提纲；§1 Witten 指标（1.1 超对称谐振子、1.2 整体对称性）；§2 超共形指标（2.1 手征多重态、2.2 规范理论、2.3 重组下的不变性、2.4 插叙：超对称拉氏量）；§3 $\sN=2$ 理论（3.1 超对称极限、3.2 S 对偶、3.3 Class S 与 TQFT）；§4 大 $N$ 极限（4.1 黑洞呢？）；致谢；参考文献 [1]–[47] |
| 编号公式 | 110 条，按节编号 (1.1)…(4.16) |
| 编号习题 | 8 个：1.1 p6、1.2 p8、2.1 p10、2.2 p13、2.3 p15、3.1 p21、3.2 p22、4.1 p28 |
| 表格 | Table 1 p10、Table 2 p13（纯文字 tabular，须复刻） |
| 插图 | 无 |

## 2. 目录与文件分工

| 块 | 文件（源码\） | PDF 页 | 公式号 | 环境 |
|---|---|---|---|---|
| c01 | `abstract.tex` + `sec0.tex` | p1–2 | — | — |
| c02 | `sec1a.tex` | p3–5 | (1.1)–(1.17) | — |
| c03 | `sec1b.tex` | p6–7 | (1.18)–(1.30) | 习题 1.1 |
| c04 | `sec2a.tex` | p8–12 | (2.1)–(2.16) | 习题 1.2、2.1；Table 1 |
| c05 | `sec2b.tex` | p13–18 | (2.17)–(2.29) | 习题 2.2、2.3；Table 2 |
| c06 | `sec3a.tex` | p19–22 | (3.1)–(3.19) | 习题 3.1、3.2 |
| c07 | `sec3b.tex` | p23–25 | (3.20)–(3.35) | — |
| c08 | `sec4.tex` | p26–30 | (4.1)–(4.16) | 习题 4.1；致谢在 p30 |
| c09 | `refs.tex` | p31–32 | — | 参考文献 [1]–[47] |

**只改自己那一块的文件。** `main.tex`、`preamble.tex`、`build.ps1`、`check_block.py`、`glossary.tsv` 一律不许改；确实缺宏 → 在 `preamble.tex` 末尾「追加区」加 `\newcommand`，并在回报里写明，或改用 `<span>` 级别的替代写法。

## 3. 施工顺序

1. 读本文件 → `STYLE_GUIDE.md` → `probe.md` → `TIMELINE.md` → `glossary.tsv`。
2. 认领一块；按 `TIMELINE.md` 的页区间逐页读 `工程文件\split\pNN.txt` 定位，**公式与表格一律看页面图** `工程文件\pages\pNN.png`（或 `crop.py` 放大）。
3. 写块文件（UTF-8 无 BOM、LF 换行），写完跑自检直到 `OK`：
   ```
   $env:PYTHONIOENCODING='utf-8'
   <本地路径> 工程文件\check_block.py 源码\sec1a.tex
   ```
4. 回报：块名、tags a/b、env c/d、批注条数、行数、未决疑点。

## 4. 铁律（八条，不得违反）

1. **数学只信页面图。** 文字层的分式、上下标、矩阵、根号会塌；凡公式必看 `pages\pNN.png`。图片不存在或模糊 → 用 `crop.py` 裁切放大。
2. **编号是王。** 原文每个编号公式都要用 `\tag{1.1}` 形式手工编号，一条不多一条不少；正文引用写「式 (2.14)」，**不许** `\eqref`。编号习题/定义等用带参环境，手工给号（如 `\begin{exercise}[2.1]`）。
3. **正文照译。** 不增删句子、不合并段落、不「润色」掉作者的语气（这是一份讲义，第一人称和口语化表达要保留）。
4. **批注只加在真有价值处。** 用 `% [Tutor Note: …]` 或注解环境，四类：术语说明、物理动机、易错点、与其它文献的对应。整块不少于 8 条，单条不超过 3 行。
5. **表格要复刻，插图不存在。** Table 1/2 用 `tabular` 按页面图逐格重建（列宽用 `C{宽度}`），删去原文的竖线风格差异可接受，内容一字不差。
6. **文件纪律。** 只写自己那一块；UTF-8 无 BOM、LF；不写 `\documentclass`/`\usepackage`/`\section`/`\newtheorem`；不写 Markdown 粗体（`**`）；不在数学环境外写 Unicode 数学符号（如 α、≤、→）。
7. **不自作主张编译。** 不跑 `build.ps1`，不生成 PDF；编译由 Lead 做。
8. **不确定就写批注，不要猜。** 原文疑似笔误：照译并在批注里指出正确形式，同时写入 `工程文件\ERRATA.md` 的候选区（回报时提一句）。

## 5. 上下文节约

- 按页读 `split\pNN.txt`（一次 1–3 页），**不要**读整本 `full.txt`（32 页 ≈ 3 万 token）。
- `eqs_raw.txt` 只是机械抓号的结果，可用于快速核对「本页应有哪些号」，但**不能**作为排版依据；`probe_raw.txt` 含元数据与逐页首末行，只在开工时读一次。
- 看页面图用 `read_image`，一次一张；需要看公式细节用 `crop.py` 裁小区域，别整页反复读。

## 6. 工具

- 页面图：`工程文件\pages\pNN.png`（200 dpi，NN 为 PDF 页序两位，如 p03.png）。
- 裁切：`python 工程文件\crop.py 10 0.0 0.30 out.png`（第 10 页，上 30%）；`--dpi 600` 可更清。
- 自检：`python 工程文件\check_block.py 源码\secXX.tex`。
- 术语：`工程文件\glossary.tsv`（215 条，`en<TAB>zh<TAB>注`）；查不到的先按惯例译，并在回报里列出「新增术语建议」。

## 7. 完成判据

- 你负责的每一块：`check_block.py` 输出 `OK`，tags 与 env 全中，无禁用命令，无 BOM/CRLF。
- 数字自检：本块公式号首尾与 `TIMELINE.md` 一致；习题号齐；表格与页面图逐格一致。
- 回报格式：
  ```
  [块 c0X 完成] 文件 sec1a.tex | tags 17/17 | env 0/0 | 批注 11 条 | 行数 412
  未决：p5 的 (1.17) 第二行分母疑为 2ε 而非 ε，已在批注标出
  新增术语建议：letter → 字母；plethystic → 齐次
  ```
