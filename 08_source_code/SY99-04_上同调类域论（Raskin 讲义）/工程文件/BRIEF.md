# 工程任务书：Raskin《上同调类域论》中文试译与校订

本文件是**施工时**的任务书原件（2026-11-25 立项，2026-11-26 校对轮），保留原样以便追溯口径；
路径已按发布仓结构改成相对路径。

## 目标

1. 把底本的讲义正文（23 讲）译成中文 LaTeX，合稿编译成 PDF。
2. 译手在翻译过程中用检索插件（`kb_locate / kb_get / kb_ctx`）实测，留下可核验的记录。
3. 产出：成品 PDF（`成品/`）、`工程文件/REPORT.md`、`ERRATA.md`、术语表（已冻结，随 PDF 附）。

## 底本

- Sam Raskin, *Lectures on Cohomological Class Field Theory*, MIT 18.786（2016 春季）课程讲义，
  Oron Propp 整理，2017-08-21 版，119 页（印刷页 1–115）/ 23 讲。
- 公开来源：MIT OpenCourseWare 18.786 课程页（CC BY-NC-SA 4.0）。**底本 PDF 属 L4，不入仓**。

## 硬约束

- 术语必须按 `工程文件/work/glossary.tsv`（已冻结，109 条：102 冻结 + 7 追加）；不得自行改译。
- 公式按数学含义重排 LaTeX；拿不准的标 `% [TODO: 公式待核]`，不许猜数字/上下标。
- 书目保留英文原条目，只加中文标题对照。
- 校对轮起改用「能确证的排印错误直接订正 + `% [原文疑误：…]` 注释留痕」的口径（注释不进 PDF），
  逐条登记于 `ERRATA.md`。

## 工作流（历史记录）

`src/lecture01..23.txt`（由底本 PDF 抽出、按讲切分）→ `zh/lectureNN.tex`（LaTeX 片段）→
`assemble.py` 合稿 + 三遍 xelatex → `成品/*.pdf`；
分块派单为 R1–R9（8 并发 + 1 排队），每块交 `reports/R-blockNN.md`（术语使用、插件测试、存疑）。
发布仓里保留的是合稿后的 `源码/chunks/*.tex`（等价于原 `zh/*.tex`）。

## 质量门

1. 每讲逐段对照，无整段漏译；陈述编号（定义/定理/例/式）与原文一一对应（自动比对 `missing` 全空）。
2. `$`/`\[` 成对、环境配对；三遍 xelatex **0 error / 0 undefined**。
3. 校对轮：对照公开底本 PDF（`pdftotext -layout` + 页面渲染）逐讲复核公式、交换图与陈述，误差登记在案。
