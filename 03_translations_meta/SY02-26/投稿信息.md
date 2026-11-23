# 投稿信息 · SY02-26

TRANSLATION-STANDARD:v2.1 施工标准

## 一、书目

| 项 | 内容 |
| --- | --- |
| 编号 | SY02-26 |
| 原作 | Geometrization of the local Langlands correspondence |
| 作者 | Laurent Fargues、Peter Scholze |
| 主题 | 局部 Langlands 对应的几何化：Fargues–Fontaine 曲线、Bun_G、diamond、几何 Satake、shtuka 上同调、L-参数与谱作用 |
| 出处 | arXiv:2102.13459v4（2024-11-27 修订版） |
| 中译名 | 局部 Langlands 对应的几何化 |
| 体例 | 专著式长文；10 章，文献 351–356，页码与 PDF 页一致（偏移 0） |
| 学科 | 数论 / 算术几何 / p-进几何 / 几何 Langlands |
| 难度 | 极高（完满空间、菱形、六函子形式化、导出代数几何同时在线） |
| 篇幅 | 原文 356 页；**本包为第一章（导引，原文 p.7–44）译注校订本**，译本 36 页 |

## 二、交付物

```
SY02-26_局部Langlands对应的几何化/
├── 投稿信息.md                  ← 本文件
├── 精选片段.md                  ← 10 条判定链（含 2 条弯路）
├── 工程文件/
│   ├── BRIEF.md                 ← 任务、页映射、四阶段路线、文件所有权、体例、质量门、排期
│   ├── SPEC.md                  ← 章节文件命名、环境、译注命令、公式与图、常见坑
│   ├── reports/
│   │   ├── lead-log.md          ← Lead 决策流水（章数、术语、页锚、事故）
│   │   ├── chI-a.md / chI-b.md / chI-c.md     ← 三个译手的分块报告
│   │   └── proof-chI-a.md       ← 块 A 校对报告
│   ├── work/
│   │   ├── 通读笔记.md           ← 全书主旨、论证地图、阅读顺序
│   │   ├── 疑点清单.tsv         ← 40 行（概念/跳步/记号/歧义/笔误/术语）
│   │   ├── glossary.tsv         ← 207 条术语冻结表（四列，依据 A/B/I）
│   │   ├── symbols.tsv          ← 60 条记号表
│   │   ├── 术语裁定.md           ← Lead 裁定即冻结
│   │   ├── errata.tsv           ← E1–E6 勘误台账
│   │   ├── TASK-chI.md / TASK-proofread.md    ← 分块与校对任务书
│   │   ├── trace-chI-a/b/c.md   ← 译手决策记录（15/18/22 条）
│   │   └── pagemap_chI.tsv      ← 原文页 → 译本页
│   └── tools/
│       ├── check_pagemarks.py   ← 页锚是否真印出来
│       ├── page_map.py          ← 原文页 → 译本页
│       ├── check_yizhu.py       ← 译注是否被吞 / 是否有孤立脚注号
│       └── strip_optional_numbers.py
├── 源码/
│   ├── main.tex / preamble.tex / build.bat
│   └── sections/
│       ├── front-translator-note.tex   ← 译者说明（含脚注编号、勘误说明）
│       ├── s01-chI-1.tex   ← §I.1–I.4（原文 p.7–22）
│       ├── s02-chI-2.tex   ← §I.5–I.9（p.23–36）
│       ├── s02b-chI-10.tex ← §I.10（p.37–38，页界缺口补译）
│       ├── s03-chI-3.tex   ← §I.10 尾–I.13（p.39–44）
│       └── back-bibliography.tex
├── 资料卡/
│   ├── SCHEMA.md
│   ├── cards/concepts/   ← 10 张
│   ├── cards/derivations/← 3 张
│   └── tools/lint_cards.py, verify_quotes.py
└── 成品/
    └── SY02-26_第一章译注本.pdf   ← 42 页（含译者说明与目录）
```

## 三、质量记录

| 门 | 结果 |
| --- | --- |
| 整书编译 | `build.bat` → 42 页，0 error，0 overfull |
| 页锚 | `check_pagemarks.py main --start 7 --end 44 --pdf` → 38/38 全部可见 |
| 页映射 | `page_map.py` → 原文 p.7–44 ↔ 译本 p.1–36，无缺页 |
| 译注 | `check_yizhu.py main.pdf` → 36 条全部在 PDF 中出现，无孤立脚注号 |
| 编号 | 68 个编号对象，与原文逐条一致（I.2.1…I.11.1），无重复打印 |
| 资料卡 | `lint_cards.py --prefix fs21 --max-pages 356 --strict` → 13 张 0 错误 |
| 引文 | `verify_quotes.py --strict` → 51 条 quote 全部在原文页面对上 |

## 四、勘误（原文）

| 序 | 位置 | 原文 | 订正 | 置信度 | 状态 |
| --- | --- | --- | --- | --- | --- |
| E1 | p.22 | is a also consequence | is also a consequence | high | fixed |
| E2 | p.29 | etc. . | etc. | high | fixed |
| E3 | p.36 | congradients | contragredients | high | fixed |
| E4 | p.21 vs p.87 | 定理 I.4.1 与 III.0.2 的 (iv)/(v) 互换 | 原文自身不统一，译文照 p.21 | low | open |
| E5 | p.14 | a map S → Spa E（漏 ♯） | S♯ → Spa E | high | fixed |
| E6 | p.15 | "unipotent group diamond" 加引号而无定义 | 全书检索未见定义，存疑 | medium | open |

## 五、说明

- 本包只含**第一章（导引）**的译注校订本，II–X 章尚未开译；BRIEF §9 给出每章 1–2 天、全书 16–20 工作日的排期。
- 原文 PDF 与本工程逐页文本（`01_pages/`）**不入仓**，只随本地工程保留；仓内不含底本 PDF。
- 术语以 `工程文件/work/glossary.tsv` 与 `术语裁定.md` 为唯一裁决源；资料卡引用一律用 PDF 页序。
