# 《局部 Langlands 对应的几何化：综述》中译注本

> 底本：Laurent Fargues, *Geometrization of the local Langlands correspondence: an overview*,
> 2016-02-02，**46 页**（Introduction p.1；§1 p.3；§2 p.16；§3 p.23；§4 p.28；§5 p.29；
> §6 p.31；§7 p.34；§8 p.36；§9 p.42；References p.46）。
> 发布编号：**SY02-29**（`RELEASE_REGISTER.csv` 现有至 SY02-28，无占用）。
> 工程根：`C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-29_局部Langlands几何化综述`

## 这是什么

这是「老蓝子钢铃」语料库**算术侧的主干道**。Fargues–Scholze 2021 那篇 356 页（本库 SY02-26）
把局部 Langlands 对应搬上 Fargues–Fontaine 曲线；而这篇 2016 年的 46 页综述，是那条路线
**第一次完整的公开交代**：曲线怎么造（§1）、`Bun_G` 是什么叠（§2）、`B_dR`-仿射 Grassmann 簇与
Hecke 叠怎么粘（§3）、猜想怎么陈述（§4）、特征层性怎么检查（§5）、`F`-等晶体与 `p`-可除群如何
给出两个周期态射（§6）、与 Shimura 簇上同调如何相容（§7）、Kottwitz 猜想如何被蕴含（§8）、
环面情形如何验证（§9）。

它的价值不在"新"，而在**可读**：356 页里被压缩成一句话的"可以逐字搬到曲线上"，
在这 46 页里往往仍有完整的动机与构造。因此本册适合作为 SY02-26 的**前置读本**：
先在这里建立曲线、叠、Grassmann 簇、两周期态射的直觉，再进 356 页的正文。

术语尚未稳定的地方（diamond、untilt、perfectoid、shtuka、v-层），本译本一律**先冻结再译**，
无法冻结的保留英文并出注；每处疑似笔误保留原样、出注、登记，绝不静默修改。

## 目录

| 路径 | 内容 |
|---|---|
| `源码/` | LaTeX 源：`main.tex`、`preamble.tex`、`sections/s00`–`s99`、`build.bat` |
| `工程文件/BRIEF.md` | 施工手册（页映射、文件所有权、质量门） |
| `工程文件/SPEC.md` | 体例规范（章节文件、环境、页锚、译注格式） |
| `工程文件/work/通读笔记.md` | 全书主旨、按节论证地图、体裁清单、阅读顺序 |
| `工程文件/work/疑点清单.tsv` | 64 行疑点（58 已解 / 6 待核），八列：位置/原文表述/类型/初步猜测/查证动作/结论/依据/状态 |
| `工程文件/work/glossary.tsv` | 87 条术语冻结表（四列，依据 A/B/I） |
| `工程文件/work/trace-*.md` | 各译手逐页对照与公式裁图核对记录（7 份） |
| `工程文件/reports/r-*.md` | 分章报告：编号对齐表、页锚表、疑点表、遗留 |
| `工程文件/reports/lead-log.md` | Lead 决策流水（术语裁定、版式事故、errata 政策） |
| `资料卡/` | 概念卡/推导卡（JSON，供语料与检索），`SCHEMA.md` 为字段规范 |
| `成品/` | 全本 PDF |

## 进度

| 阶段 | 内容 | 状态 |
|---|---|---|
| Phase 0 | 通读笔记 + 疑点清单 + 术语冻结表 87 条 | ✅ 完成 |
| Phase 1 | §1–§9 全译（7 名译手并行，Lead 自译导引与 §4） | ✅ 完成，48 个编号对象全部对号 |
| Phase 2 | 整书统稿：页锚 46/46、页眉、页边注、宏集中、编号核验 | ✅ 完成 |
| Phase 3 | 资料卡（概念卡 A–E + 符号索引 + 推导卡） | 进行中 |
| Phase 4 | 入仓：README / 投稿信息 / 精选片段 / datasets | ✅ 见 `03_translations_meta/SY02-29` |

## 怎么编译

```bat
cd 源码
build.bat                 :: 整书两遍（有索引时 xelatex → makeindex → xelatex ×2）
build.bat check sections\s04-bung.tex c   :: 单章自检，产出 _check_c.pdf
```

单章自检时编号会显示为 `1.x`（因为节计数器从 1 起）；并入 `main.tex` 后自动恢复为原文编号
（§1–§9 的节号与原文一致，环境共用 `[theorem]` 计数器）。

## 质量记录

| 门 | 结果 |
|---|---|
| 整书编译 | `main.pdf` **63 页**，0 error，0 Overfull |
| 页锚 | `main.pagemarks` 52 条、覆盖 p.1–p.46 全部 46 页，无缺页（文件边界重复属设计允许） |
| 编号 | 定义 20、命题 34、定理 12、引理 1、推论 9、例 5、猜想 7、期望 3、注 30，与原文逐条一致 |
| 译注 | 86 条（`\yizhu` 42 + `\yizhuw` 44），全部带来源或标注「无外部依据」 |
| 语言 | 「被……所」「进行……的」「对于……而言」全书 0 处 |
| 资料卡 | 46 张（概念 38 / 推导 8），`lint_cards.py` 0 错误；196 条 quote 全部逐字命中 |

## 纪律

一切按 `工程文件/SPEC.md` 与 `工程文件/BRIEF.md` 执行；母本是发布仓
`04_playbook/01_数学文献翻译纪律.md` v2.1：先通读后落笔、译注必须带来源、
来源白名单 nLab/Stacks/ProofWiki、黑名单知乎等。

底本 PDF 与本工程逐页文本**不入仓**，只随本地工程保留。
