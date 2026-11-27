# BRIEF —— SY02-48 Ben-Zvi 几何 Langlands 课程讲义（UT Austin M390C 2021 春）

## 一、任务

把 David Ben-Zvi 讲授、Arun Debray 记录的 UT Austin M390C《Geometric Langlands》课程讲义

> David Ben-Zvi (lectures), Arun Debray (notes), *M390C Notes: Geometric Langlands*,
> UT Austin 2021 春季学期，2021-01-19 至 2021-06-03，**31 讲，89 页**，
> live-TeX 现场记录，文稿生成日期 2021-06-03。

译成中文译注本，并配套资料卡与外部核验。底本文件由用户提供（微信收件箱中的
`ba566ae34f33f2d33e6e6a6714259b29.pdf`）；本工程只保留逐讲文本与页面图，**不复制 PDF 原件**。

## 二、底本判读

- **印刷页码 = PDF 页码**（偏移 0）：PDF 第 2 页页眉下即「1. Overview and a perspective on
  modular forms: 1/19/21」，页脚印 1；正文 p.2–89。
- 全书结构：标题页与目录 p.1，正文 p.2–89，参考文献 p.89（31 讲末尾）。
- 页眉为记录者标记；**讲次 = 章（`\section`）**，讲内无小节编号，
  编号条目（Definition / Theorem / Example / Remark 等）**按讲连续、所有类型共用一个计数器**，
  自动排成「讲次.序号」（如 9.8、13.4），与底本编号一一对应。
- **只有 1 幅嵌入图**，正文以散文与行间公式为主；公式按讲编号（如 (9.8)），译本一律不编号。
- 第 10 讲（2/25/21）底本**只有一行日期、没有标题也没有正文**；第 25 讲（4/27/21）
  底本标题为空但正文完整。两处均在译本说明与报告 §三 登记。

### 逐讲页数与条目数

| 讲 | 底本标题 | 日期 | 页 | 页数 | 条目 |
|---|---|---|---|---|---|
| 1 | Overview and a perspective on modular forms | 1/19/21 | 2–5 | 4 | 1 |
| 2 | A tale of two TFTs | 1/21/21 | 5–8 | 4 | 1 |
| 3 | Spectral theory and sheaf theory | 1/26/21 | 8–11 | 4 | 9 |
| 4 | Some Fourier theory | 1/28/21 | 11–15 | 5 | 1 |
| 5 | Pontrjagin and Cartier duality | 2/2/21 | 15–18 | 4 | 4 |
| 6 | Electric-magnetic duality | 2/4/21 | 18–21 | 4 | 4 |
| 7 | Lagrangian quantum field theory | 2/9/21 | 21–24 | 4 | 3 |
| 8 | Topological quantum mechanics, topological Maxwell theory, and class field theory | 2/11/21 | 24–27 | 4 | 1 |
| 9 | Class field theory and function fields | 2/23/21 | 27–29 | 3 | 1 |
| 10 | （无标题、无正文） | 2/25/21 | 29 | 1 | 0 |
| 11 | Boundary conditions and extended TFT | 3/2/21 | 29–33 | 5 | 4 |
| 12 | Extended TFT and topological Maxwell theory | 3/4/21 | 33–35 | 3 | 0 |
| 13 | Geometric class field theory | 3/9/21 | 35–38 | 4 | 2 |
| 14 | Tannakian reconstruction | 3/11/21 | 38–41 | 4 | 6 |
| 15 | 1-Shifted Cartier duality | 3/23/21 | 41–43 | 3 | 4 |
| 16 | Betti and de Rham | 3/25/21 | 43–46 | 4 | 0 |
| 17 | The moduli stack of principal G-bundles on a curve | 3/30/21 | 46–49 | 4 | 4 |
| 18 | Hecke algebras | 4/1/21 | 49–53 | 5 | 5 |
| 19 | Hecke algebras on arithmetic locally symmetric spaces | 4/6/21 | 53–57 | 5 | 5 |
| 20 | Topological field theory, interfaces, and boundary conditions | 4/8/21 | 57–59 | 3 | 3 |
| 21 | Commutative algebras of local operators | 4/13/21 | 59–62 | 4 | 1 |
| 22 | Spectral decomposition in topological field theory | 4/15/21 | 62–65 | 4 | 4 |
| 23 | Defects and defect operators | 4/20/21 | 65–67 | 3 | 0 |
| 24 | Defect operators and Maxwell theory | 4/22/21 | 67–69 | 3 | 0 |
| 25 | （无标题） | 4/27/21 | 69–71 | 3 | 2 |
| 26 | The affine Grassmannian | 4/29/21 | 71–74 | 4 | 2 |
| 27 | The geometric Satake correspondence | 5/4/21 | 74–76 | 3 | 1 |
| 28 | Parabolic induction and restriction | 5/6/21 | 76–78 | 3 | 2 |
| 29 | More on the geometric Satake correspondence | 5/20/21 | 78–81 | 4 | 4 |
| 30 | Categorification | 5/27/21 | 81–85 | 5 | 4 |
| 31 | Classical Langlands | 6/3/21 | 85–89 | 5 | 0 |
| 合计 | 31 讲 | — | 2–89 | 88 | **78** |

（「页数」按讲首末页相减计，相邻讲共享页时各算一次，故逐讲页数之和 118 大于正文页数 88。）

## 三、方法

1. **抽取与切分**：PyMuPDF 抽全文（37 万字符，文本层干净），按 `Lecture N.` 标记切 31 讲，
   页界行统一为 `% ===== 原文 pN =====`；L31 末尾 References 切到 `lectures/refs.txt`。
2. **通读与定术语**：`work/通读笔记.md` 记内容脉络与每讲要点；`work/glossary.tsv`
   306 条（沿用 SY02-41 的 215 条 + 本工程新增 91 条），表外词查 `01_corpus_zh/数语规范/TERMS.tsv`
   与 SY02-26 glossary，都没有就保留英文并在报告 §5 登记。
3. **分讲翻译**：8 名译手并行，各写自己的 `源码/sections/sNN-*.tex`，契约见 `work/TASK-translator.md`；
   每人交稿前跑 `check_sections.py` 到 0 问题。
4. **核公式**：逐符号对页面图（`work/pages/pNNN.png`，150 dpi）核；页锚、编号条目逐一对照。
5. **编译**：`源码/build.bat`（xelatex 三遍）。
6. **报告**：每讲一份 `reports/chNN.md`（范围、术语、疑点、遗留）。
7. **资料卡**：五件套见 `资料卡/00-速览.md`；至少 1 张 gap 对齐卡进
   `datasets/leanstmt/cards/statements/`。
8. **登记入库**：`RELEASE_REGISTER.csv` 一行、`03_translations_meta/SY02-48/`、
   `python make_stats.py --write`、`tools/check_numbers.py`、`tools/build_norm.py --check`。

## 四、交付物

| 位置 | 内容 |
| --- | --- |
| `源码/` | `main.tex`、`preamble.tex`、`sections/s00–s31`、`s99-bibliography`、`build.bat` |
| `成品/` | 编译出的 PDF（入库时按仓库规范命名） |
| `工程文件/` | 本 BRIEF、`STYLE_GUIDE.md`、`work/`（通读笔记、疑点清单、术语表、条目总表、逐讲文本、页面图）、`reports/chNN.md` |
| `资料卡/` | 五件套：`00-速览.md`、`01-结果清单.md`、`02-论证地图.md`、`03-条款索引.md`、`04-术语文献勘误.md` |

## 五、硬约束

- 数学正确性优先；不臆造，底本疑难只进译注与疑点清单，不改底本意思。
- 全库禁 `\eqref` / `\ref` / `\label` / `\cite`；行间公式不编号；原文公式号回指改写为「前式」等。
- 编号一律交给 LaTeX（`\section` 与定理环境），**禁止手写编号**。
- 每页首段前 `\srcpage{N}`；页界落在句中用 `\srcpageinl{N}`。
- 原文脚注 → `\footnote`；译注 → `\yizhu{内容}{等级（出处）}`，每讲 ≤ 6 条。
- 一句 ≤ 60–70 汉字；中文与拉丁字母之间半角空格；全角标点；人名/定理名/软件名不译。
- 只改本工程文件；术语改名须三同步（正文、术语表、资料卡）。

## 六、进度

- [x] 底本判读、逐讲切分文本与 89 页页面图
- [x] 骨架复用 SY02-41（preamble / build.bat / 工具脚本）、31 个节文件占位
- [x] 通读笔记、术语表 306 条、译手契约
- [x] 31 讲译文 + 编译三遍 0 error（107 页）
- [x] 31 份 reports
- [x] 资料卡五件套 + 对齐卡（2 张 gap 卡）
- [ ] 登记入库并推送（进行中）

### 数字口径

| 项 | 值 |
| --- | --- |
| 原文页 / 讲次 / 编号条目 | 89 / 31 / 78 |
| 译本汉字 | 约 7.67 万 |
| 译本页数 | 107（xelatex 三遍，0 error、0 Underfull、11 处 Overfull ≤15.1pt） |
| 术语表 | 306 条（新增 91 条） |
| 译注 | 44 条 |

### 遗留与已知限制

1. 第 10 讲底本无正文，译本只给节标题与说明，不补写内容。
2. 第 25 讲底本标题为空，译本用「无标题的一讲」，正文照译。
3. 底本是课堂现场记录，含作者口头插话与 `(TODO: …)` 自注，译本照译保留。
