# CHANGELOG

## 2026-11-24 · v1.0

首个完整版本。

- 六篇全文译完（47 个 chunk）：Dat、Zhu、Fargues–Scholze、Emerton–Gee–Hellmann、Ben-Zvi–Chen–Helm–Nadler、Feng–Harris，另含前言与三份前置文件（译者说明、导读）。
- 全文 495 页，XeLaTeX 三遍：0 error / 0 Overfull / 0 undefined / 0 missing character。
- 术语表 314 条（A/I/B 三级依据），覆盖六篇；跨篇记号冲突按「篇内自洽 + 译注说明」处理。
- 页锚 562 个（`\ysrc`，印刷页 = PDF 页 − 13），页锚审计 0 缺失、0 重复。
- 编号陈述 802 条、带号公式 318 条、译者注 149 条。
- 资料卡五件套 + 对齐卡 6 条（`status: g`，只给候选 Lean 陈述，未形式化）。
- 四路自动审计脚本入库：`lint.py`（语言/术语/环境）、`pageaudit.py`（页锚）、`audit_num.py`（编号）、`coverage.py`（译幅覆盖率），报告在 `工程文件/reports/`。
- 权利：底本为 AMS 在版图书，按 R3 不发布成品 PDF，仓内只保留源码、工程记录与自产资料卡。
- 已知局限：未做逐句人工二校（结构层已全书复核）；`ProCoh` 暂保留原文。
