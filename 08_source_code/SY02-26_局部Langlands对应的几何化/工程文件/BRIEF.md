# BRIEF —— 《局部 Langlands 对应的几何化》中译注本 施工手册

> 底本：Laurent Fargues, Peter Scholze, *Geometrization of the local Langlands correspondence*,
> arXiv:2102.13459v4（2024-11-27），**356 页**（PDF p.356 = 文献表末页）。
> 工程根：`C:\Users\admin\Downloads\FarguesScholze_局部朗兰兹几何化`
> 本手册是硬约束。与本手册冲突的临时指令，以用户当场指令为准，但必须记进 `reports/`。

---

## 0. 一句话任务

把这篇 356 页的论文**逐章**译成中文、加可追溯的译注、双校定稿、做成资料卡，最后按发布仓规范入仓
（`08_source_code/SY02-26_局部Langlands对应的几何化/` + `datasets/fs21/`）。
> 编号已核：`RELEASE_REGISTER.csv` 到 SY02-24，工作树里 SY02-25 被「顶点代数与代数曲线（第二版）」占用，故取 **SY02-26**。

**不是**摘要、不是导读、不是"讲大意"。是逐段可对照的译本 + 批注。

---

## 1. 页映射与源文本（先读这一节）

- **印刷页 = PDF 页（偏移 0）**。已核：PDF p.7 = Chapter I 首页（页脚 7）、PDF p.100 页脚 100、PDF p.356 页脚 356。
  目录里 "Chapter I. Introduction 7" 指的就是 PDF 第 7 页。所有 `\srcpage{N}`、批注里的 p.N、报告的页码，**一律用 PDF 页序**。
- 逐页文本：`01_pages/pNNN.txt`（p001–p356），每页首行是 `===== PDF PAGE n (printed m) =====`。
- 原文 PDF 只读副本：`00_原文/fargues-scholze-2102.13459v4.pdf`（**不许改写、不许入仓**）。
- **文本提取只可作索引**：公式、上下标、交换图、花体字在提取里必失真。凡写进译文的公式/定义/定理陈述，
  必须 `pymupdf` 渲染该页（dpi 150–200）看图像核对（见 §5.3）。
- 章页范围（PDF 页）：

| 章 | 标题 | 页 | 篇幅 |
|---|---|---|---|
| I | Introduction | 7–44 | 38 |
| II | The Fargues–Fontaine curve and vector bundles | 45–86 | 42 |
| III | Bun_G | 87–106 | 20 |
| IV | Geometry of diamonds | 107–166 | 60 |
| V | D_ét(Bun_G) | 167–186 | 20 |
| VI | Geometric Satake | 187–242 | 56 |
| VII | D■(X) | 243–276 | 34 |
| VIII | L-parameter | 277–316 | 40 |
| IX | The Hecke action | 317–338 | 22 |
| X | The spectral action | 339–350 | 12 |
| — | 目录 p.3–6，文献表 351–356 | | |

> **全书 10 章**（2026-11-23 由通读员按目录页 p.3–5 核定：章首 I 7 / II 45 / III 87 / IV 107 / V 167 / VI 187 / VII 243 / VIII 277 / IX 317 / X 339，文献表 351 起）。
> 原表只列到 VII 是有误的，已按目录改正；Ch VII–X 的标题见 `工程文件/work/通读笔记.md`。

---

## 2. 路线图（分四阶段，禁止跳阶段）

**Phase 0 通读 + 术语（全书只做一次）**
- 产物：`工程文件/work/通读笔记.md`、`工程文件/work/疑点清单.tsv`、`工程文件/work/glossary.tsv`（冻结）。
- 门槛：疑点清单 `未解` = 0，术语表核心条目「依据」列非空。**没到门槛不许开译。**

**Phase 1 样板章（Lead 亲定）**：Chapter I（pp.7–44）——它是全书路线图，先译它最有价值。
- 由 3 名译手分块并行（I.1–I.4 / I.5–I.9 / I.10–I.13），Lead 合并、统稿、定体例。
- 这一章的译法、句式、译注写法就是**全书样板**，后面各章照抄，不许各写各的。

**Phase 2 逐章推进**：每章一名译手（大章 IV/VI 可拆两半）+ 一名校对（不同人）。
- 规矩：一章译完 → 校 → 修 → 编译通过 → 才动下一章。不许全书齐头并进。

**Phase 3 全书统稿**：术语终检、编号对象对齐、索引、文献表、译者说明、全书编译 0 error。

**Phase 4 资料卡 + 入仓**：每章 8–12 张卡（详见 §6），最后统一 ship。

---

## 3. 文件所有权（违反即返工）

| 谁能写 | 文件 |
|---|---|
| 每名译手 | **只**自己那块 `源码/sections/sNN-*.tex` + `工程文件/reports/chNN.md` + `工程文件/work/trace-chNN.md` |
| 校对人 | 被分配章节的 tex（在译手的 diff 基础上改）+ `reports/chNN-review.md` |
| Lead（本会话主控） | `源码/main.tex`、`preamble.tex`、`工程文件/*`（除 work 下译手文件）、`资料卡/`、`deliverable/` |

- **谁都不许**：改 `00_原文/`、`01_pages/`、别人的 sections、`glossary.tsv`（只许 Lead 追加）、`main.tex`、`preamble.tex`。
- 需要全局改动（新宏、新环境、节结构）→ 写进 `reports/` 交 Lead，不要自己动 preamble。
- 术语冲突：报 Lead 裁定，裁定结果由 Lead 写进 glossary；执行者不得自行统一。

---

## 4. 体例（译前必读，配合 `工程文件/SPEC.md`）

1. **逐段对照**：一段英文 → 一段中文，段落顺序、编号、环境类型（定理/定义/注/例）一律保持原样。
2. **章内节结构**照原文：`\chapter{导引}` + `\section{I.1 局部 Langlands 对应}`，
   编号不重排；原文的 `I.2.3` 之类小节号写进 `\subsection*{}` 或段落首，保持可对照。
3. **原文页码锚点**：每页起点处放 `\srcpage{7}`（页边小字），使读者能回原文定位。**每页都要有，不许漏**。
4. **译注**：`\yizhu{注文}{来源}`；无来源用 `\yizhuw{注文}`（自动标「译者按（无外部依据）」）。
   三类必注：①术语首次出现（为何这样译）；②原文跳步/引用外部结果（补一句它是什么）；③疑似笔误/歧义（保留原文，说明）。
   **不许**把注写成"我觉得作者想说……"式推测——推测只能以「译者按」形式出现。
5. **保留英文的项**：人名、机构、专有名词（Fargues–Fontaine 曲线、Hitchin、Drinfeld、Satake、Banach–Colmez、
   shtuka、diamond 视情况）、`\ell`-adic 等。术语表里标"不译"的，一律照办。
6. **公式**：编号 `\begin{equation}...\label{eq:I.2.1}` 编号照原文（`(2.1)` 之类），不许重编；
   多行用 `align`；交换图一律 `tikz-cd`（不截图、不用图片代替）。**公式一个符号都不许自己改**；
   原文看着不对 → 照排 + 译注 + 记疑点。
7. **标点与空格**：中文全角标点；英文术语/数字与汉字之间半角空格（`$\ell$-进层`、`第 3 章`）。
8. **禁止**译文里出现本机绝对路径、`C:\`、`/Users/`。

---

## 5. 质量门（每章必过，缺一不算完成）
- `python ../工程文件/tools/check_yizhu.py main.pdf --tex sections`：必须 `[ok]` 两条（每条译注都出现在 PDF 中；无孤立脚注号）。凡批量挪动译注后必须重跑——行尾 `%` 会把整条译注静默注释掉，编译不会报错。


### 5.1 编译
- 单章：`源码/build.bat check sections/sNN-*.tex` → `_check.pdf`，**0 error**。
- 整书：`xelatex main` ×2 → `main.pdf`，未定义引用 0、缺字 0、Overfull 记录在报告里。

### 5.2 编号对象对齐
- 报告里给一张表：原文的定理/命题/引理/定义/注/例/公式编号 → 译文 label → 是否一致。
- 数量必须对得上（少一个就是漏译）。

### 5.3 公式回图核对
- 每个含公式的段落，译手自检时必须至少渲染一次原页图像比对（`pymupdf` dpi 150）。
- 报告里写：核对了哪些页、发现几处提取错误（提取错不等于原文错，别混）。

### 5.4 术语与黑名单
- 旧译名残留 = 0（脚本 grep）；术语与 `glossary.tsv` 一致。
- 来源黑名单（知乎/百度百科/CSDN/简书/公众号/博客）命中 = 0。

### 5.5 译注来源
- 每条译注带 `[来源：A/B/I …]` 或 `[译者按（无外部依据）]`；抽查 5 条必须真实可查。
- 来源白名单：nLab、Stacks Project、ProofWiki（B 级，须与 A 级交叉）；A 级 = 原始论文/经典教材/作者原文。

---

## 6. 资料卡（Phase 4）

- 目录：`资料卡/`，JSON 一张一文件，`concepts/` 与 `derivations/` 分开放。
- 体例照本库 GGL 卡（`ggl_文献库/cards/SCHEMA.md`）：`id` 前缀 `fs21/`，`rights="rewritten"`，
  `sources[].quote` 为 12–120 字符英文原句（**写不出 quote 的出处等于没出处**），页码用 PDF 页序。
- 每章配额：概念卡 8–12 张、推导卡 2–4 张（大章按页数放大，Lead 在任务书里给数）。
- 卡片写不出原文依据时标 `provenance="B"`（我们重建）并在 `provenance_note` 说明。
- 质检：`python 资料卡\tools\lint_cards.py 资料卡\cards --prefix fs21 --max-pages 356 --no-pkg --strict` 与 `python 资料卡\tools\verify_quotes.py 资料卡\cards --strict` 都必须 exit 0（后者查引文页码与真实性）。

---

## 7. 交付注意事项（**每个 agent 开工前逐条读**）

1. **先读再写**：`BRIEF.md` → `SPEC.md` → `work/通读笔记.md` → `work/glossary.tsv` → 你这块对应的原页（`01_pages`）+ 渲染图像。
   没读完原页不许落笔。
2. **只写自己的文件**（§3）。越界改动会被 diff 检出并整块退回。
3. **控制台是 GBK**：不要 `print` 中文到 stdout；要看输出就写 UTF-8 文件再读。
4. **文件编码**：UTF-8 无 BOM、LF 换行。用 write 工具写，不要用 shell 重定向写中文。
5. **不编造**：原文没有的内容不补；不懂就登记 `疑点清单.tsv`，并在报告里列出来。宁可留白加注，不许猜。
6. **不许 git push**、不许动发布仓。入仓由 Lead 走 `mt_daily`。
7. **交付物清单（每章，缺一不退）**：
   - [ ] `源码/sections/sNN-*.tex`（编译通过）
   - [ ] `工程文件/reports/chNN.md`（编号对齐表、核对页清单、疑点列表、遗留问题）
   - [ ] `工程文件/work/trace-chNN.md`（决策记录 ≥10 条，四栏「判断点/依据/结论与理由/事后确认」，**其中 ≥2 条是走过又退回的弯路**，只写真实发生过的）
   - [ ] `工程文件/work/疑点清单.tsv` 追加行（不改别人的行）
   - [ ] 术语新增项（写在报告里，由 Lead 并入 glossary）
8. **时间**：一章之内允许慢，不允许糊。宁可少译一节标「未完成」，不要整章看起来齐整实则失真。
9. **失败要显式**：编译不过就修；修不动就报告里写明「卡在哪一行、报什么错」，不要假装完成。
10. **回报格式**（≤15 行）：完成了哪几节、页范围、编译结果（0 error?）、编号对象数、译注条数、
    新增术语数、疑点（未解 n 条）、trace 条数与弯路条数、遗留问题。

---

## 8. 训练数据（与 GGL 流水线同规）

- `trace-chNN.md` + `reports/chNN.md` + 译稿 tex 一起构成本章的"工程原文件 + 工作流 + 思考链"。
- 不额外造假样本；入仓时由 Lead 用 `ggl_文献库/tools/build_train.py` 的同类逻辑抽 SFT 样本。

---

## 9. 排期（Lead 维护，见 `README.md` 的进度表）

- 今日（2026-11-23）：Phase 0 + Chapter I 样板章。
- 之后每章 1 天一译一校；Chapter IV（60 页）、VI（56 页）各给 2 天。
- 全书预计 16–20 个工作日；每章完成即更新 README 进度表。
