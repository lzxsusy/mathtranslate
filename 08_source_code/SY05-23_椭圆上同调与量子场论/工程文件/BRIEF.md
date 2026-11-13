# BRIEF.md — 项目总览（施工总纲，动手前必读）

## 项目

把 **Daniel Berwick-Evans, _Elliptic cohomology and quantum field theory_（arXiv:2408.07693v1 [math.AT], 2024-08-14, 34 页）** 译成**中文 LaTeX 译注本**：

> 中文正文 + 原文全部 56 条编号公式 + 全部编号环境（猜想/定义/注/例/定理/命题/推论/假设，手工编号严格对齐原文）+ 8 幅图的图注译文（图不复刻）+ 参考文献条目保留原文 + 学术级 Tutor Note 批注（LaTeX 注释形式，另汇总 `译注汇总.md`）。

主题一句话：**Stolz–Teichner 纲领**——椭圆上同调（TMF）的上闭链应当由 2 维超对称量子场论给出；Witten 亏格 / Witten 指标、K 理论类比、配边范畴、等变推广。这正是「椭圆上同调 × 超对称（共形）场论」这条线的**数学侧总览**。

## 目录（全部在 `<本地路径>`）

| 路径 | 内容 |
|---|---|
| `工程文件\BRIEF.md` | 本文件：施工总纲 |
| `工程文件\STYLE_GUIDE.md` | **硬性规范**，违反即返工 |
| `工程文件\TIMELINE.md` | 分块表：页码、章节、公式号归属 |
| `工程文件\glossary.tsv` | 术语冻结表（en→zh，制表符分隔） |
| `工程文件\pages\pNN.png` | 34 页 200 dpi 渲染（**公式的唯一真值**） |
| `工程文件\split\pNN.txt` | 逐页文字层（定位用；**数学不可信**） |
| `工程文件\full.txt` | 全书文字层（全局检索，别整本读） |
| `工程文件\eqs_raw.txt` | 机械提取的公式号清单（`p<页>\t(<号>)`），需人工核对 |
| `工程文件\probe_raw.txt` | 底本元数据、TOC、逐页首末行 |
| `工程文件\probe.md` | 备料说明：素材怎么用、看公式的正确姿势、已知坑 |
| `工程文件\底本_arXiv-2408.07693.pdf` | 底本 PDF 原件 |
| `工程文件\prep.py` | 备料脚本（已跑过，可重跑） |
| `工程文件\crop.py` | 裁图放大（看公式用） |
| `工程文件\check_block.py` | 单块静态自检（交稿前必须跑到 OK） |
| `工程文件\build.ps1` | 一键编译 + 日志验收 |
| `源码\preamble.tex` | 导言区（Lead 独占；队友只读） |
| `源码\main.tex` | 主文件（Lead 独占：封面/目录/章节骨架） |
| `源码\sec1.tex` … `refs.tex` | 各块译文（只写自己那一个） |
| `工程文件\ERRATA.md` | 原文笔误登记（Lead 汇总） |
| `工程文件\README.md` | 交付说明（统计数字最后填） |
| `成品\` | 最终 PDF |

## 底本事实（已实测）

- 34 页；**PDF 页号 = 印刷页码**（偏移 0）。
- 目录：§1 Introduction p1；§2 The homotopy type of quantum mechanics p6；§3 Supersymmetric quantum mechanics and K-theory p13；§4 Elliptic cohomology and 2-dimensional supersymmetric field theories p20；References p30–34。
- 编号公式 **56 条**，全文单序列 `(1)`–`(56)`（分布见 TIMELINE）。
- 编号环境按**节内共享计数器**编号（`Conjecture 1.1`、`Remark 3.21`、`Hypothesis 4.18` …），定义/注/例/定理/命题/推论/猜想/假设全部共用每节一套号。
- 图 **8 幅**（Figure 1–8）：一律不复刻，用 `\figomit{编号}{图注中译}`。
- 原文**没有摘要**；正文直接从 `1. Introduction` 开始。
- 脚注 9 处（编号 ¹…⁹，跨全文连续）。

## 分块与分工

| 块 | 文件 | 原文页 | § | 负责公式号 |
|---|---|---|---|---|
| c01 | `源码/sec1.tex` | p1–5 | §1 Introduction（含 Conjecture 1.1、Definition 1.5/1.9/1.10、Conjecture 1.11、§1.5 Acknowledgements） | (1)–(5) |
| c02 | `源码/sec2.tex` | p6–12 | §2 The homotopy type of quantum mechanics（§2.1–2.3） | (6)–(19) |
| c03 | `源码/sec3.tex` | p13–19 | §3 Supersymmetric quantum mechanics and K-theory（§3.1–3.6） | (20)–(38) |
| c04 | `源码/sec4a.tex` | p20–25 | §4.1–§4.2（2 维超对称场论的基本数据、逼近场论范畴） | (39)–(50) |
| c05 | `源码/sec4b.tex` | p26–30 | §4.3–§4.5（配边范畴重述、Additional insights、The final frontier；p30 在「References」之前的正文与式 (56) 都归本块） | (51)–(56) |
| c06 | `源码/refs.tex` | p30–34 | References（条目整条保留原文，不译） | — |

> `\section{}` 标题由 Lead 写在 `main.tex`；块文件里只允许 `\subsection`/`\subsubsection`，**不许写 `\section`**。

## 铁律（摘要，细则见 STYLE_GUIDE.md）

1. **数学必须看图抄**：`pages/pNN.png` 是唯一真值。文字层里 `\frac{m}{2}`→`2m`、矩阵碎成单字符、`\overline` 丢失都是常态。
2. **编号是王**：`\tag{n}` 一个不能少、不能重、不能自造；编号环境的手工号必须与原文逐条对齐。
3. **正文照译不许改**：原文笔误照排，只在批注里指出（并登记 ERRATA）。
4. **批注写成 `% [Tutor Note: ...]`**，不进排版；每条要有价值（核对方法/补论证/指笔误/辨记号）。
5. **不插图、不造表**、不补文献、不写 markdown 粗体、不写 `\newcommand`、不写 `\section`。
6. **只写自己的文件**；UTF-8 无 BOM + LF；用 Python 写，别用 PowerShell `Out-File`。
7. **不自己编译整书**（Lead 统一编译）；交前跑 `python check_block.py secXX.tex` 到 `OK`。
8. **不确定就写批注问，绝不编造数学**；搞不定的写 `% [TODO-LEAD: ...]` 并在回报里说清。

## 工具用法（PowerShell）

```powershell
$env:PYTHONIOENCODING='utf-8'                                  # 必设，否则中文 print 崩
$py = '<本地路径>'
cd '<本地路径>'
& $py crop.py 16 0.30 0.55 d16_mid.png                         # 页 16，纵向 30%–55%，整宽，400dpi
& $py crop.py 16 0.10 0.85 0.30 0.65 d16_eq.png                # 页 16，x 10%–85%，y 30%–65%
& $py check_block.py sec2.tex
```

看裁图用 `read_image` 工具（不要用 `read` 读 PNG）。一次裁 1/4 页以内能看清上下标。
编译（仅 Lead）：`powershell -File build.ps1`，XeLaTeX 来自 MiKTeX（`xelatex` 已在 PATH）。
`build.ps1` 存为 UTF-8 **带 BOM**（PowerShell 5.1 读无 BOM 的中文脚本会乱码）；MiKTeX 往 stderr 打
「major issue: So far, you have not checked for MiKTeX updates.」是正常噪音，不影响编译。
**骨架已验证**：2026-11-13 用空桩跑通两遍，产出 3 页（封面 + 空白录），46 KB；块文件为空时只报缺 tag 属正常。

## 上下文节约

- 不要整本读 `full.txt`；按页读 `split/pNN.txt`。
- 每页先看渲染图，再对着文字层定位段落。
- `STYLE_GUIDE.md` 读一遍记住要点，别反复读。

## 回报

一条消息，格式见 STYLE_GUIDE.md §10。Lead 汇总编译后会把编译错误定向派回。
