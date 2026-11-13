# SEM-XXXX 研讨班工作区

这是一个空白模板。复制整个目录为 `seminars/SEM-<arXiv号或短名>/`，再按下面顺序填写。

## 第一小时

1. 改 `seminar.yaml`：标题、作者、页数、`page_offset`、角色。
2. 放底本：`source/original.pdf`、`source/translation.pdf`（若有）。
3. 建页图：`source/pages/p001.png` ...（150 dpi，灰度即可）。
4. 建文字层：`source/text/p001.txt` ...；公式仍以页图为准。
5. 改 `map.yaml`：章节、页码、核心问题、依赖。
6. 改 `brief.md`：分工、截止、报告格式。

## 角色

- Chair：立规矩、建页图、发分工、主持圆桌、写综合。
- r01 / r02 / r03：各读全文，写 `reports/rXX.md` 与 claims。
- Examiner：可兼任，写 `challenges/rXX_on_rYY.md`。
- Textual Critic：可兼任，对照原文页图与译本核对。

## 流程

S0 立项 → S1 预处理 → S2 地图 → S3 独立研读 → S4 交叉质询 → S5 回应 → S6 圆桌 → S7 综合 → S8 质检。

## 产出

`notes.md`、`transcript.md`、`one_pager.md`、`errata.md`、`claims/merged.jsonl`、`questions/merged.jsonl`、`manifest.json`。

详细规范见 `AI研讨班工程备忘.pdf` 与 `02_工程规范/研讨班运行手册_v0.1.md`。
