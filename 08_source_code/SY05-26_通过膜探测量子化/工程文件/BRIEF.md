# BRIEF —— SY05-26《通过膜探测量子化》

## 目标

把 Gaiotto–Witten 的 *Probing Quantization Via Branes*（arXiv:2107.12251v2，101 页）完整译为中文，产出一部可编译、可校对的译注本，并随仓库源码归档。

## 底本

- 主底本：作者 LaTeX 源码 `Draft_D.tex`（4335 行，来自 arXiv 源码包），存 `work/原文/`。
- 核对底本：`Probing Quantization Via Branes.pdf`（101 页），页面图存 `work/pages/`。
- 页映射：PDF 页 = 印刷页 + 2。

## 范围

- 译：摘要、§1–§5、附录 A–D、致谢。
- 不译：源码中注释掉的旧节（3375–3403 Gauged quantization、3526–3584、4249 起 More On Cotangent Bundles）；这些节不在 PDF 成文中。
- 不做：资料卡（按用户要求，待正文稳定后再补）。

## 交付物

```
源码/            main.tex、preamble.tex、sections/*.tex、figures/*.pdf
工程文件/
  BRIEF.md       本文件
  STYLE_GUIDE.md 语言与体例规范
  build.ps1      一键编译与质量门
  work/          通读笔记、疑点清单、glossary、原文、页面图
  deliverable/   术语对照表、译注汇总、工程总结、阅读参考指南、统计数据
投稿信息.md      投稿/发布元信息
```

## 硬约束

1. 公式与编号沿用原文，不重排、不改变量记号（源码的单字母宏整体照搬）。
2. 术语冻结于 `work/glossary.tsv`，首现中英对照。
3. 每条解释性译注标来源等级（A/B/I）或“译者按（无外部依据）”。
4. 编译质量门：0 error、0 undefined、0 overfull。
5. 原文笔误只改明显笔误，并在 `deliverable/译注汇总.md` 记录；有歧义者保留原文并加校勘。

## 状态

- 全文译毕，69 页，编译通过（2026-11-20）。
- 遗留：译注偏少（4 条）、无 B 级来源、未做资料卡。详见 `deliverable/工程总结.md` 第六节。
