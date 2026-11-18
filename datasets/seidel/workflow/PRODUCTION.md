# seidel 资料卡生产流程

## 0. 输入

| 材料 | 位置（本机，不入库） | 用途 |
|---|---|---|
| 原书 PDF | `Seidel, Fukaya categories and Picard–Lefschetz theory(1).pdf`（334 页） | 核对定义、公式、页码 |
| 译稿源码 | `seidel_fukaya_work/src/`（82 个章文件） | 187 条 `\znote`、31 处修订 |
| 译者注总表 | `work/精选数据/译者注总表.tsv`（187 行） | 卡片的数学内容与页锚 |
| 修订总表 | `work/精选数据/修订总表.tsv`（40 行） | 勘误卡 |
| 页码对照 | `work/精选数据/page_map.csv`（81 文件） | `\SourcePage` → 印刷页 |
| 分章报告 | `work/review/report-A01…A12.md` | 存疑、原书笔误、上下文 |

## 1. 定卡

- 概念卡：只收「全书反复使用、且译者注已给出实质解释」的概念；一张卡一个定义 + 一个可检验的定理。
- 推导卡：只收「跨节、跨章、原书只给路线」的论证；每步必须有 `locator` 与 `provenance`（A=原书，B=由原文推出，C=我们的判断）。
- 勘误卡：只收 `修订总表.tsv` 里实际改过的条目；不把「存疑未改」写成勘误。

## 2. 写卡

- 定义与证明用**自己的话**重写；公式照录，但必须回原书页面图像核对上下标与符号。
- `sources.pages` 取印刷页；`anchor` 一律 `原书 p.N`。
- 勘误卡：`original`/`corrected` 各不超过 60 字；超过就截取并说明；`why` 用分章报告的理由，不另编。
- 每张卡至少 2 条 `related`，且必须能在本数据集内解析。

## 3. 质检与发布

```bash
python tools/lint_cards.py cards --strict
python tools/build_index.py
python tools/render_md.py
```

- `lint` 0 error 才提交；`status` 保持 `draft`，直到有人逐卡复核。
- 提交前检查：无本机绝对路径、无译本正文段落、引文累计不超过单卡 10%。

## 4. 门禁

| 门 | 检查 | 结果 |
|---|---|---|
| G0 来源 | 每张卡有 `sources`，页码 1–326，anchor 合法 | lint 强制 |
| G1 结构 | 概念/推导/勘误三类字段齐全 | lint 强制 |
| G2 引用 | related 全部可解析 | lint 强制 |
| G3 权利 | `rights=rewritten`，无长段引文 | lint + 人工抽检 |
| G4 渲染 | `md/` 与 `index.jsonl` 可重建 | build/render 成功 |
| G5 内容 | 定义、定理与原文页一致 | **抽样核对，未全量**（诚实缺口） |

## 5. 已知缺口

- 证明多为 `sketch`，完整证明需回原书 §9、§12、§16、§19。
- 勘误卡只覆盖 40 条修订；原书笔误与「存疑未改」留在分章报告，未落卡。
- 页码为译稿 `\SourcePage` 推导，未逐卡回 PDF 复核。
