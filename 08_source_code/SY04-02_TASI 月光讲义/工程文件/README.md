# TASI Lectures on Moonshine —— 中文译注版

> 交付目录：`1807.00723v1(2)(1)/`
> 底本 PDF：`1807.00723v1(2)(1).pdf`（78 页）

---

## 0. 先读：底本与作者核实

你提供的 PDF（文件名为 `1807.00723v1(2)(1).pdf`）经逐页核对，实际是
**Vassilis Anagiannis 与 Miranda C. N. Cheng** 的
*“TASI Lectures on Moonshine”*（arXiv:1807.00723v1 [hep-th]，2018 年 7 月 2 日，78 页；
作者在 TASI 2017 暑期学校所作的两组讲座讲义）。

**它不是 Witten 的论文**，主题也不是一般意义上的 QFT/弦论综述，而是“月光”
（moonshine：有限群表示与模对象之间的意外联系）及其物理（弦论/K3）实现。
按“先读懂再评论”的原则，译文与批注均以这份底本的实际内容为准，未把作者观点
改写成 Witten 的框架或观点。

中文版编译后 72 页（中文更紧凑，另加入“本节重点”与批注注释，故页数与原文不同）。

---

## 1. 交付清单

| 文件/目录 | 内容 |
|---|---|
| `1807.00723v1(2)(1).tex` | **完整单文件 LaTeX 源码**（自包含：导言区 + 全部章节 + 参考文献内联；仅 `figures/` 为外部依赖） |
| `1807.00723v1(2)(1).pdf` | 编译成品（72 页，含 3 图 1 表、目录、参考文献） |
| `figures/` | 从原 PDF 裁出的 3 幅矢量插图（PDF）+ PNG 预览 |
| `分章源码/` | 可维护版本：`main.tex`、`preamble.tex`、`references.tex`、`chapters/ch00–ch09.tex` |
| `译校报告/` | 各章译者报告（范围、公式/label 核对、批注统计、疑似笔误、自检记录） |
| `术语表.md` | 术语冻结表（中英对照、裁定记录） |
| `译校批注索引.md` | 212 条 `% [Tutor Note: ...]` 批注的逐条索引（按章节/源码行号） |

---

## 2. 编译方法

需要 **XeLaTeX**（中文由 `ctex` 宏包处理）。

```text
# 方式一：TeX Live / MiKTeX（推荐）
xelatex "1807.00723v1(2)(1).tex"     # 两遍，以生成目录与交叉引用
xelatex "1807.00723v1(2)(1).tex"

# 方式二：Tectonic（单二进制，自动下载宏包）
tectonic -X compile "1807.00723v1(2)(1).tex" --keep-logs
```

- Windows 下文档类默认 `fontset=windows`（SimSun/SimHei/KaiTi）。
  在无 Windows 字体的系统（Linux/macOS）上，把首行
  `\documentclass[11pt,a4paper,fontset=windows]{ctexart}` 改为
  `fontset=fandol` 即可（TeX Live 自带的 Fandol 中文字体）。
- 本交付的 PDF 是用 **Tectonic 0.17（XeTeX 引擎，TeX Live bundle）** 编译的；
  最终验收：`0 error / 0 undefined reference / 0 overfull / 0 missing character / 0 duplicate label`。
- 分章源码版本编译：进入 `分章源码/`，执行 `xelatex main.tex` 两遍。

---

## 3. 体例说明

1. **本节重点（Key Takeaways）**：9 个 Section（导言 + 第 1–9 节）开头各有一块
   `keytakeaways`，提炼该节的核心对象、数学工具与结论。源码中为
   `\begin{keytakeaways} ... \end{keytakeaways}`，可整体删除而不影响正文。
2. **译校批注**：关键处共 **212 条** `% [Tutor Note: ...]` 源码注释，分三类：
   *易错预警*（指标/符号/归一化/约定）、*含糊点拨*（作者以“显然/易得”带过的论证，
   指出其依据与可查文献）、*背景直觉*（一两句点破物理图像）。
   批注是 LaTeX 注释，**不进入排版**，便于在源码中逐条查阅；
   全部批注的索引见 `译校批注索引.md`。
3. **公式**：全部 **193 个行间公式**（90 个 `equation` + 71 个 `\be…\ee` 宏块 +
   15 个 `gather` + 4 个 `align` + 13 个 `\[…\]`）与行内公式均**逐字符照录原文 LaTeX**，
   编号顺序与原文一致（(1.1)–(9.x)）；已用脚本把每个公式块与 arXiv 源码逐字符比对。
4. **图表**：原文共 3 幅插图、1 张表格，全部保留并译为中文图注/表注：
   - 图：月光示意图（原文 p.2，原文无图注，译注版补图注并声明）→ 编译后图见 5 页；
   - 图 1：ADE Dynkin 图（原文 p.10）→ 图注“图 1 …（原文 p.10，图 1）”；
   - 图 2：本影月光的构造（原文 p.52）→ 图注“图 2 …（原文 p.52，图 2）”；
   - 表 1：$\mathcal{A}_6$ 的特征标表（原文 p.14）。
   插图内部英文标注（如 “Modular forms”、“Finite groups”）按原样保留，其含义见中文图注。
5. **术语**：以中文学界通行译名为准（monstrous moonshine=魔群月光、
   umbral moonshine=本影月光、vertex operator algebra=顶点算子代数、
   elliptic genus=椭圆亏格 等），首次出现括注英文；无稳定中译的术语
   （twining、Hauptmodul、Mock modular 相关专名等）保留英文。详见 `术语表.md`。
6. **参考文献**：147 条，保持英文原貌与编号顺序（utphys 风格）。

---

## 4. 校对、技术处理与“原文疑似笔误”记录

### 4.1 验收（全部通过）

- 每章 `check_chapter.py`：行间公式块计数一致 + 逐块逐字符匹配 + `\label` 集合一致
  + `\ref/\cite` 集合一致 → 全部 PASS；
- 全稿编译：`0 error / 0 undefined reference / 0 overfull / 0 missing character /
  0 duplicate label`（`main.log` 已核对）。

### 4.2 编辑性技术处理（均在源码批注中写明，未改变任何数学内容）

| 位置 | 原文写法 | 本版处理 | 原因 |
|---|---|---|---|
| §4 (4.12) | `\rm{Aut}V(\Lambda)` | `{\rm Aut}V(\Lambda)` | 老式 `\rm{}` 在 XeTeX+ctex 下使 `\Lambda` 丢字形（编译报 `Missing character U+0003`，PDF 显示为 `V()`）；改为 `{\rm Aut}` 后正常 |
| §5 | `\label{conj_mock}` 重复定义 | 第二处改为 `conj:mock_umbral`，并同步该节内指向本影猜想的引用 | 消除 `multiply defined label`；引用指向与出版版 PDF 一致 |
| §5/§6 | `\label{rep_mock}` 重复定义（(5.6)/(5.8)） | 第二处改为 `rep_mock_umbral`，§6 相应引用同步 | 同上；并把 §5 中本应指向 (5.6) 的引用恢复为 (5.6)（出版 PDF 因重复 label 误指向 (5.8)） |
| §2 (2.38) | 超长公式 | 局部 `\footnotesize` 缩排 | 消除 42pt Overfull，公式内容未动 |
| §2 | 长行内公式段 | 局部 `\sloppy` | 消除 3.6pt Overfull |
| 参考文献 | `\cite{cheng2013mathieu}` 在作者 .bbl 中缺失（出版 PDF 显示 `[?]`） | 保留引用，并在文献表末尾加“译者补注”条目说明 | 不臆造文献信息，留待原作者核对 |

### 4.3 原文疑似笔误（均“照录原文 + 批注指出”，未擅改）

- p.11：`8E_8` 应为 `3E_8`（秩 64≠24）；
- p.14：式 (1.22) 与 Frame shape 定义中指标 `r/s` 混用；
- p.22：不完全 gamma 函数写作 `Γ(1−w,x)=∫_x^∞ e^{−t}t^{w}dt`，按标准定义应为 `t^{−w}`；
- p.33：式 (3.28) 右端求和指标为 `j` 而项写 `ch_i`；
- p.39：“largest sporadic group” 指 $M_{24}$，但最大散在群是魔群；
- p.39：精确除子定义 `(f,N/f)=1` 应为 `(e,N/e)=1`；同一页 `c(n)` 未定义（应即 `a_n`）；
- p.61：Witten 指标第二式仍写 `ch_{1/4,0}(z=0)=-2`，应为 `ch_{1/4,1/2}`；
- p.61–62：式 (8.6) 与 (8.7) 相差因子 2（(8.7) 疑漏写 1/2 或反之），需对照 Cheng–Duncan–Harvey 原文核定；
- 英文拼写小误（`cycle groups`/`exponenets`/`superconfomal`/`McKay–Thompsen` 等）按正确含义译出，并在批注中注明原文拼写。

---

## 5. 统计

| 项目 | 数量 |
|---|---|
| 章节 | 导言 + 第 1–9 节（三部分：背景 / 月光 / 月光与弦论） |
| 小节 | 23 |
| 行间公式 | 193 块（其中 109 个编号环境 + 71 个 `\be` 宏块 + 13 个 `\[ \]`） |
| 中文字符 | 约 50,000 |
| 译校批注 | 212 条 |
| 本节重点 | 9 块 |
| 图 / 表 | 3 图 + 1 表 |
| 参考文献 | 147 条 |
| 成品页数 | 72 页 |

---

## 6. 未决问题（如实列出）

1. 式 (8.7) 因子 2 疑点：需对照 Cheng–Duncan–Harvey 的原文核定；本版按原 PDF 照录并加批注。
2. 原文标为 “In preparation” 的若干文献（如 `umstar`、`class_nr_moonshine`）无法核对，按原样保留。
3. 插图内的英文标注保留原样；如需重绘为中文矢量图，可在此基础上另行处理。
4. 底本 PDF 文件名含 `(2)(1)` 后缀，与 arXiv 正式编号 `1807.00723v1` 对应；本交付文件沿用原文件名。

---

*本译注版由 AI 助手按用户要求完成；所有术语裁定、批注与疑似笔误记录均可在源码与报告中追溯。*
