# 《同调镜像对称性浅入门》中文译本交付说明

- **书名**：同调镜像对称性浅入门
- **作者**：Raf Bocklandt（阿姆斯特丹大学）
- **底本**：*A Gentle Introduction to Homological Mirror Symmetry*, London Mathematical Society Student Texts 99, Cambridge University Press, 2021
- **版本**：校订版 v4.0（第四轮校订，对照英文原书 · 101 处修订 + 208 处术语统一 · 36 张资料卡）
- **日期**：2026-11-21

## 一、内容概要

本书译自 Bocklandt 的同调镜像对称入门讲义，按原书结构排为三部分、十二章：

- **第一部分　$A_\infty$ 及其更远处**：范畴（第 1 章）、上同调（第 2 章）、高阶乘积（第 3 章）、箭图（第 4 章）。建立 $A_\infty$ 形式体系，并以箭图的两种几何解释初见镜像对称。
- **第二部分　镜中一瞥**：来自物理的动机（第 5 章）、A 侧（第 6 章）、B 侧（第 7 章）、镜像对称（第 8 章）。从路径积分与超对称出发，引入 A／B 模型及其 $A_\infty$ 范畴与环面镜像。
- **第三部分　曲面上的思考**：粘合（第 9 章）、分次（第 10 章）、稳定化（第 11 章）、变形（第 12 章）。用温和代数与粘合显式构造曲面 Fukaya 范畴，并处理 $\mathbb Z$ 分次、稳定性与变形理论。

全书含前言、三部分十二章中译正文、257 个原书插图（另加 1 个从原书 PDF 裁出的矢量小图）、258 条英文参考文献（保留原文，编号可点击跳转）、中文索引，以及“译校说明”“附录：校订批注”。正文另加 **60 个“本节重点”**、**12 篇章末评注（“本章回顾与评注”，约 9 900 字）** 与 **90 条校订批注**。成书 365 页（PDF 页数，含封面与前置页）。

## 二、v2.0 更新说明

本轮针对三方面作系统修订，全部改动可追溯至 `reports/` 下的分章记录与 `审校报告.md`：

1. **术语复核与纠偏**。确立“有稳定通行译名者用中文，无则保留英文，不硬造生词”的原则：
   - 保留英文：`wrapped` / `partially wrapped` / `thimble`（Lefschetz thimble）/ `stop`（原译“消失帐篷”“停止子”“卷绕”均已废弃）；这些术语在中文里无稳定译名，硬译反碍对照文献。首现处与“译校说明”均作解释；
   - 改译：托里克簇→**环簇**（toric variety）、充足／非常充足线丛→**丰富／极丰富线丛**（ample / very ample）；
   - 统一：第 6 章 exact 语境由“恰当”改为**正合**（与第 8、9 章一致）；curved 统一作**带曲率**（否定形“无曲率”）；filtered 统一作**滤过**；Euler form 改译**Euler 型**；proper $A_\infty$ 范畴保留英文 proper。
   - 索引键（`\index{拼音@显示名}`）与 `index-terms.tsv` 已同步改写。
2. **语言流畅度**。清除翻译腔（长定语、被动滥用、“进行……的”、“对……而言”、“以及”等 as-well-as 直译），在数学内容、符号、编号与交叉引用不变的前提下重写部分句子。
3. **章末评注**。每章末尾新增“本章回顾与评注”方框（`\chapterreview{...}`），五段式：全章地位、知识脉络、核心结论、辨析与提醒、评注；用于复习本章知识点、串讲逻辑链，并对作者的处理方式、局限与后续章节的衔接作专业评论。原书无此内容，可在 `main.tex` 中用 `\showchapterreviewfalse` 整体隐藏。

## 三、v3.0 二轮校订说明

2026-11-20 完成第二轮独立校订。本轮不是对 v2.0 的润色，而是 12 章各由一名审稿人独立通读、主校逐条复核后，只改确定的误译、漏译、数学/记号/体例错误：

- 共修订 **89 处**（各章 8/6/4/9/11/8/9/14/7/3/6/4），逐条见 `reports/chNN.md`；
- 代表性修正：面映射补回 $x_0$、辛形式补 $i$ 与 $dz\wedge d\bar z$、三维 LG 模型统一为 $UV=W_t$、第 11 章删除定理中未使用的 $A$、第 12 章 $\Lambda_Z\to E_Z^{\pm}$ 等；
- 保留 **90 条**校订批注（类型与各章条数不变），仅修正第 10 章批注中的 $2-k\to k-2$；
- 本机无英文原书与页面图像，本轮以中文定稿的内部数学一致性、记号、术语、交叉引用与体例自洽为主，**未逐页对照英文原文**；报告中如实说明；
- 配套 **32 张资料卡**（20 概念 + 12 勘误）见仓库 `datasets/sy0117/`，每张概念卡携带至少一条批注，锚到本工程源码行号；
- 成书仍 **365 页**，编译 0 未定义引用、0 重复书签、0 Overfull、0 缺字。

### v4.0 第四轮校订（2026-11-21，首次对照英文原书）

2026-11-21 完成第四轮校订。本轮首次取得英文原书 PDF（CUP 2021 扫描本，365 页，与译本页数一致），把全书按页切分后交 12 名审稿人逐段对照中译复核，主校逐条复核并统一跨章术语：

- 逐章修订 **101 处**（各章 6/7/5/3/10/22/4/18/6/7/8/5），逐条见 `work/review3/chNN.json`；
- 全局术语修订 **208 处**：解消→消解 11、保典解消→crepant 消解 3、泛型→通有 20、温和代数→gentle 代数 68、相干层/拟相干层→凝聚层/拟凝聚层 97、吹起→爆破 7、区分三角→正合三角 1、盘泡→圆盘泡 1；
- 阿米巴（amoeba）首见处加译注，说明词源、数学定义（Log 映射下的像）与 GKZ 来源；`frontmatter_note.tex` 补术语说明；
- 新编《中英术语表》`术语表.md`（323 条、30 条关键术语释义、附录 A 分章表、附录 B 英文索引）与机器可读 `glossary.tsv`；
- 修正编译级问题：第 6 章 `% [Tutor Note: ...]` 与正文同行导致整句被注释吞掉；
- 配套资料卡增至 **36 张**（24 概念 + 12 勘误），新增 amoeba、toric-variety、crepant-resolution、gentle-algebra 四张；
- 成书仍 **365 页**，编译 0 未定义引用、0 重复书签、1 Overfull hbox、0 缺字（Overfull 为版式微溢，非缺字）。

## 四、文件清单

以下路径相对本目录。

| 路径 | 内容 |
|---|---|
| `main.tex` | 主文档：文档类、封面、目录、三部分与十二章的 `\input`、附录批注、参考文献与索引设置；“本节重点”“章末评注”两个开关 |
| `chapters/ch01.tex`—`ch12.tex` | 十二章中译正文（含 `\takeaway`、章末 `\chapterreview`、图注与 `% [Tutor Note: ...]` 批注源码） |
| `figures/` | 257 个原书插图文件（`Fig_NNN_PDFxxx_Bookyyy.pdf`，`Bookyyy` 为原书页码）及 1 个裁出的矢量小图 |
| `references.tex` | 258 条英文参考文献及 `\hyperlink{ref:...}` 锚点 |
| `同调镜像对称性浅入门_中文精译.pdf` | 编译产物（成书 PDF，365 页） |
| `审校报告.md` | 二轮（v3.0）校订总报告：范围与方法、89 处修订统计、主要修正、批注、存疑未改、编译与验证 |
| `第四轮校订报告.md` | 第四轮（v4.0）校订报告：对照英文原书的方法、101 处修订、208 处术语、术语表、编译数据、存疑未改 |
| `术语表.md` | 《中英术语表》v4.0：323 条术语、30 条关键释义、保留英文清单、变更记录、外部依据、分章与英文索引 |
| `glossary.tsv` | 术语表机器可读版（EN / CN / 拼音 / 首见页 / 章） |
| `work/review3/` | 第四轮过程记录：12 份分章 JSON、digest、uncertain、GUIDE |
| `审校批注索引.md` | 90 条校订批注按章、节的索引与类型分布 |
| `术语对照表.md` | v2.0 术语统一过程的审计记录（v4.0 定稿见 `术语表.md`） |
| `数学文献翻译纪律.md` | 给后续智能体／译者的通用工作手册：术语判定、数学核对、中文文风、LaTeX 工程、协作与交付检查清单，附本项目踩坑案例 |
| `reports/` | 过程记录：12 份二轮分章校订报告、批注索引源 `notes_index.md`、全书审计 `audit.md`、交叉引用审计 `refs_audit.md`、v2.0 自动审计 `audit_v2.md`、全局修订日志 `global_fix_log.md` 与 `lead_fix_log.md`；首轮报告原件在 `reports/_v1_archive/`（仅本地备份，不随仓库发布） |

另有 `glossary.md`（术语底稿）、`index-terms.tsv`（索引词条与拼音键）、`elegantbook.cls`（文档类）、`cover.png`（封面）、`appendix_notes.tex`（自动生成的附录批注）、`frontmatter_note.tex`（译校说明）、`校订规范.md`（校订规范，含 v2.0 术语规则）、`tools/`（编译、附录生成、术语批处理与审计脚本）。

## 五、编译方法

### 5.1 一键编译（推荐）

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File tools\build.ps1
```

脚本使用随工作区提供的便携 TeX Live，依次执行 `xelatex` → `makeindex` → `xelatex` ×2，并在结束时检查未定义引用、重复书签、Overfull box 与缺字，输出形如：

```
pages=365  undefined_refs=0  duplicate_dest=0  overfull=0  missing_glyph=0
BUILD OK
```

单章草稿（语法自检）用 `-Chapter NN`（NN 为两位数），只编译指定章并输出 `build/checkNN.pdf`：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File tools\build.ps1 -Chapter 06
```

### 5.2 手动编译

使用 **XeLaTeX** 编译，先编译一遍生成交叉引用与索引数据，运行 **MakeIndex**，再编译两遍更新目录、书签、页码与超链接（`imakeidx` 以 `noautomatic` 加载，索引须手动生成）：

```powershell
cd <本书目录>
New-Item -ItemType Directory -Force build
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
makeindex -o build/main.ind build/main.idx
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
```

所需环境与宏包：

- XeLaTeX、MakeIndex；
- ElegantBook 4.7 文档类（已随书提供 `elegantbook.cls`）及其依赖，如 `tcolorbox`（“本节重点”“章末评注”方框）、`imakeidx`、`float`、`hyperref`、`booktabs` 等；
- 系统可供 XeLaTeX 调用的中文字体（文档类以 `lang=cn, scheme=chinese` 加载中文方案）。

已交付的 PDF 已嵌入所用字体，阅读该 PDF 不依赖读者设备上安装这些字体。

## 六、体例说明

1. **“本节重点”开关**：`main.tex` 中以 `\newif\ifshowtakeaway`、`\showtakeawaytrue` 控制；将其改为 `\showtakeawayfalse` 即可一次性隐藏全书 60 个“本节重点”方框，不影响其余排版。方框内容由各章 `\takeaway{...}` 给出，位于每节标题（若有导读段则在导读段）之后，练习节不设。
2. **章末评注开关**：`main.tex` 中以 `\newif\ifshowchapterreview`、`\showchapterreviewtrue` 控制；改为 `\showchapterreviewfalse` 即可隐藏全书 12 篇“本章回顾与评注”。方框内容由各章 `\chapterreview{...}` 给出，位于每章最后一个练习之后。
3. **图注与页码**：249 个 `figure` 环境、220 条题注，题注末尾统一标注“（原书 p.N）”，给出该图在原书中的页码，便于对照纸本。第 4 章 27 幅按原书面貌不加题注（原书亦无 Figure 编号），第 9 章 Fig_157、Fig_158 为原书未编号示意图，同样无题注。
4. **校订批注**：正文中的 LaTeX 注释 `% [Tutor Note: ...]` 不进入 PDF，书末“附录：校订批注”按章、节自动生成并与之一一对应；批注分易错预警、含糊点拨、背景直觉三类，凡原书疑似笔误亦在批注中如实说明。全部批注的索引见 `审校批注索引.md`。
5. **编号与引用**：沿用 ElegantBook 默认设置，定义／定理／引理／例各自独立计数，与原书“连续编号的单序列”不同；正文批注以“原书 p.N”与名称指代原书编号，跨章引用一律使用 `\ref` 标签。此差异及其取舍见 `审校报告.md` 第五节。
6. **术语**：以 `术语表.md`（v4.0）与“译校说明”为准；`术语对照表.md` 为 v2.0 审计记录。v2.0 起 `wrapped`、`thimble`、`stop` 等保留英文；未统一／存疑条目在该表第六节列出。

## 七、版本与日期

- 版本：校订版 v4.0（v1.0 十二章分章校订 + 全书主校合并；v2.0 术语复核、流畅度修订、章末评注；v3.0 二轮独立校订、89 处修订、32 张资料卡；v4.0 第四轮对照英文原书校订、101 处修订 + 208 处术语、36 张资料卡）
- 日期：2026-11-21
- v1.0 摘要：完成全书逐段对照与公式逐式核对，全书 60 个“本节重点”、89 条校订批注，执行术语与体例的全局统一，汇总原书疑似笔误 91 条；编译通过，未定义引用、重复定义与 Overfull box 均为 0。
- v2.0 摘要：术语层面作系统性纠偏（保留英文 4 组、改译 2 组、统一 4 组，索引与索引词表同步），全书流畅度修订，新增 12 篇章末评注（约 9 900 字）与 1 条批注（共计 90 条）；编译通过，未定义引用、重复书签、Overfull box 与缺字均为 0，成书 365 页。
- v4.0 摘要：首次对照 CUP 2021 英文原书逐页复核 12 章，逐章修订 101 处、全局术语 208 处，阿米巴等术语加译注，新编 323 条《中英术语表》，36 张资料卡；编译通过，365 页，0 未定义引用、0 重复书签、1 Overfull box、0 缺字。
- v3.0 摘要：12 章独立二轮复核，89 处修订（数学/记号/译文/体例），90 条批注保留并修正 1 条，配套 32 张资料卡（20 概念 + 12 勘误）；无英文原书/页面图像，本轮未逐页对照原文；编译通过，未定义引用、重复书签、Overfull box 与缺字均为 0，成书 365 页。
