# BRIEF —— SY02-41 局部 Langlands 对应的几何化：Berkeley 讲义

## 一、任务

把 Peter Scholze 讲授、Tony Feng 记录的课程讲义

> Peter Scholze (lectures), Tony Feng (notes), *Geometrization of the Local Langlands
> Correspondence*, Berkeley 课程，2020-10-30 至 2021-02-12，27 讲 + 参考文献，共 148 页
> （作者自排 pdfLaTeX 文稿，pdfTeX 1.40.17，2022-03-19 生成；无出版方版式）。

译成中文译注本，并配套资料卡与外部核验。底本文件由用户提供（微信收件箱中的
`27-Feng_Notes_Scholze_Geometrization_of_Local_Langlands_Berkeley_course(2).pdf`）；
本工程只保留逐页文本与页面图，**不复制 PDF 原件**。

本工程与同主题的 [SY02-26《局部 Langlands 对应的几何化》](../SY02-26_局部Langlands对应的几何化/)
（Fargues–Scholze 2021 正式论文，356 页）配对：SY02-26 是论文，本工程是**同一套理论的课程版本**，
术语一律沿用 SY02-26 已冻结的译名（见 `work/glossary.tsv`）。

## 二、底本判读

- **印刷页码 = PDF 页码**（偏移 0）：PDF 第 2 页页眉下即「1. Introduction (Oct 30)」，页脚印 2。
- 共 148 页：封面与目录 p.1，正文 p.2–147，参考文献 p.148。
- 页眉固定为 `LECTURES BY PETER SCHOLZE, NOTES BY TONY FENG`。
- **讲次 = 章（`\section`）**，共 27 讲；每讲内部小节编号为「讲次.序」（如 1.1、1.2），
  定理类条目**按讲连续编号且所有类型共用一个计数器**（Definition 1.1、Example 1.2、Theorem 1.3…）。

| 讲 | 页 | 讲 | 页 | 讲 | 页 |
|---|---|---|---|---|---|
| 1 Introduction | 2 | 10 The stack of vector bundles | 49 | 19 The Jacobian criterion | 102 |
| 2 FF curve I | 7 | 11 G-bundles | 55 | 20 ét(Bun_G,Λ) revisited | 108 |
| 3 FF curve II | 12 | 12 B⁺_dR-affine Grassmannian | 60 | 21 Geometric Satake | 113 |
| 4 FF curve III | 17 | 13 Bun_G | 66 | 22 Perverse sheaves | 118 |
| 5 relative FF curve | 22 | 14 Étale cohomology of diamonds | 72 | 23 Beilinson–Drinfeld Grassmannian | 124 |
| 6 Diamonds and rel. FF curve | 27 | 15 Smoothness | 79 | 24 Geometric Satake, cont. | 128 |
| 7 Untilts, O(1), Lubin–Tate | 32 | 16 ét(Bun_G) | 84 | 25 Geometric Satake, finale | 133 |
| 8 Banach–Colmez spaces | 37 | 17 Cohomological smoothness | 90 | 26 L-parameters | 138 |
| 9 Families of vector bundles | 42 | 18 Universal local acyclicity | 95 | 27 Construction of L-parameters | 143 |
| | | | | References | 148 |

- 讲次日期：原文只印月日，未印年份。按「周一/周五」的排课节律与 pdfTeX 生成时间（2022-03-19）推断为
  **2020–2021 学年**（2020-10-30 至 2021-02-12）。各讲标题只保留印出的月日；仅封面与译本说明
  给出推断后的完整日期，并在 `资料卡/04-术语文献勘误.md` §四说明推断依据（27 个日期中 25 个落在
  2020–2021 学年的周一或周五，Nov 5、Nov 21 疑为 Nov 6、Nov 20 之误）。

## 三、方法（九步流程的裁剪版）

1. **通读**：全文速读，产出 `work/通读笔记.md`；逐讲登记 `work/疑点清单.tsv`（六类：概念/术语/记号/跳步/笔误/歧义）。
2. **定术语**：`work/glossary.tsv` 冻结 215 条，沿用 SY02-26；本库缺的词先核香蕉空间
   （结论见 `work/术语外部核对_香蕉空间.md`）。
3. **分讲翻译**：译手按讲并行，各自只写自己的 `源码/sections/sNN-*.tex`；契约见 `work/TASK-translator.md`。
4. **核公式**：逐符号对页面图（`work/pages/pNNN.png`，150 dpi）核；编号、交叉引用逐一对照。
5. **编译**：`源码/build.bat`（xelatex 三遍）。
6. **报告**：每讲一份 `reports/chNN.md`（改动、裁定、遗留）。
7. **资料卡**：五件套见 `资料卡/00-速览.md`。
8. **外部核验**：对照 Fargues–Scholze 2021（arXiv:2102.13459）逐讲核术语与陈述，产出 `资料卡/04-术语文献勘误.md`。
9. **入库**：`RELEASE_REGISTER.csv` 登记行、`03_translations_meta/SY02-41/`、`tools/make_stats.py --write`。

## 四、交付物

| 位置 | 内容 |
| --- | --- |
| `源码/` | `main.tex`、`preamble.tex`、`sections/s00–s27`、`build.bat` |
| `成品/` | 编译出的 PDF（入库时按仓库规范命名） |
| `工程文件/` | 本 BRIEF、`STYLE_GUIDE.md`、`work/`（通读笔记、疑点清单、术语表、逐页文本、页面图、术语外部核对）、`reports/` |
| `资料卡/` | 五件套：`00-速览.md`、`01-结果清单.md`、`02-论证地图.md`、`03-条款索引.md`、`04-术语文献勘误.md` |

## 五、硬约束（摘自 04_playbook/01）

- 数学正确性优先；不臆造，底本疑难只进批注与疑点清单，**不改正文**。
- 译注必须带来源等级 A/B/I；黑名单站点不看、不引、不缓存。
- 只改本工程文件；不改 label/ref/编号；术语改名须三同步（正文、术语表、资料卡）。
- 中文数学文风；一句 ≤ 60–70 汉字；中英之间半角空格；全角标点。
- 交付前 `grep` 旧术语 = 0（shtuka 的「块」、diamond 的「钻石」等只许出现在译注里）。

## 六、进度

见 `work/进度.md`（由 lead 维护）。

- [x] 底本判读、逐页文本与页面图
- [x] 术语外部核对（香蕉空间）
- [x] 27 讲译文 + 编译三遍（152 页，0 error；24 幅图 TikZ 重绘；译注 30 条）
- [x] 资料卡五件套（00 速览 / 01 结果清单 135 条 / 02 论证地图 / 03 条款索引 484 条 / 04 术语文献勘误）
- [x] 外部核验（22 条文献经 Crossref + zbMATH + arXiv 核到卷期页；原文 39 处笔误与不一致登记）
- [x] 对齐卡 3 张进 `datasets/leanstmt/`（gap 卡，`lint_cards.py --strict` 0 error）
- [x] 登记入库并推送（`RELEASE_REGISTER.csv` 第 146 行、`03_translations_meta/SY02-41/`）

### 数字口径

| 项 | 值 |
| --- | --- |
| 原文页 / 讲次 / 编号条目 | 148 / 27 / 484 |
| 译本页数 | 152（xelatex 三遍，0 error，11 处 Overfull 均为数个 pt） |
| 汉字 | 53858（总字符 160140） |
| 术语表 | 215 条（`work/glossary.tsv`） |
| 绘重图 | 24 幅（宏 `\figP{...}`，文件 `sections/figs-batch1.tex`、`figs-batch2.tex`） |
| 译注 | 30 条（A/B/I 分级，`\yizhu`） |
| 疑点清单 | 215 条（`work/疑点清单.tsv`）；勘误成条 39 条 |
| 资料卡 | 五件套；01 收 135 条结果、03 覆盖 484 条 |

### 遗留与已知限制

1. 底本有 11 处轻微 Overfull（数个 pt），未调整断行；不影响阅读。
2. 开课年份底本未印，按周一/周五排课推断为 2020–2021 学年；Nov 5、Nov 21 两个日期疑为 Nov 6、Nov 20 之误，已记入 `资料卡/04-术语文献勘误.md` §四。
3. 香蕉空间个别页面需人机验证，术语核对以导航框、正文例句与 transbox 为准，未逐页通读其正文。
4. 与香蕉空间译名分歧处（完全胚空间/钻石/斜置/正置/进制空间）一律从本库，差异与理由见 `资料卡/04-术语文献勘误.md` §二。
