# GRASSMANN-精读 · 《Grassmannians, Moduli Spaces and Vector Bundles》全书精读与审校

Clay Mathematics Proceedings 14（AMS / Clay Mathematics Institute, 2011）中译本（170 页，9 篇独立论文）的**逐章精读、译注核对与资料卡生产**工程。

- 底本：*Grassmannians, Moduli Spaces and Vector Bundles*，eds. P. E. Newstead, D. A. Ellwood, E. Previato；2006-10 剑桥 Clay 研讨会论文集。
- 中文源：9 章 LaTeX（本目录不含；在工程本地 `source/chapters/ch01–09.tex`），中译 PDF 170 页。
- 规模：中文源 77,000 字；已有译注 81 处（逐条复核，未改判）。
- 产物：9 章导读（15,669 汉字）、159 条批注、58 条 errata、9 章读书笔记（19,421 汉字）、90 张资料卡（见 `datasets/grassmann/`）。

## 目录

```
GRASSMANN-精读/
├── README.md            本文件
├── BRIEF.md             总任务书：Phase 0–4、页表、质量门、写入权限
├── STATUS.md            进度台账（全部 Phase 完成；中断恢复只看这里）
├── tools/
│   ├── preflight.py          Phase 0 闸门：页数、md5、章节首页探针、依赖
│   ├── pdf_pages.py          取 PDF 文字层 / 渲染单页（中文数学以 .tex 为准）
│   ├── chapter_task.py       生成 tmp/task-chNN.md 任务书
│   ├── extract_existing_notes.py  从 PROGRESS.md 抽 81 条已有译注
│   ├── check_chapter.py      逐章验收：六件套齐、字数、编号连续、anchor 可回查
│   ├── merge_errata.py       合并 9 份 errata → 00-审校总表.tsv（10 列口径）
│   ├── build_summary.py      生成汇总 README、修订补丁、统计表
│   ├── plan_cards.py         卡片候选去重、分轨、分组
│   └── gen_card_tasks.py     写 taxonomy.md 与四份卡片任务书
├── tmp/
│   ├── task-ch01–09.md       九章任务书（交给各章读者的原文）
│   ├── cardtask-{甲,乙,丙,丁}.md  四组卡片任务书
│   ├── cards-plan.tsv        87 条候选 → 90 张卡的计划表
│   └── cards-ids.md          全量 id 清单（related 只许取此）
└── 产出/
    ├── 导读/00-全书导读.md + chNN-导读.md        每章 ≥1200 字，五节
    ├── 批注/chNN-批注.md + chNN-errata.tsv       ≥12 条/章，五种类型
    ├── 批注/00-审校总表.tsv + 00-修订补丁.md      全书 58 条 errata 合并
    ├── 笔记/chNN-笔记.md                        每章 ≥1500 字，五节
    └── 汇总/README.md、交叉引用.md、审校方法.md、cards-chNN.tsv、章报告
```

## 流程（可重放）

1. **Phase 0**：`python tools/preflight.py` → 0 FAIL（170/190 页、md5 一致、9 章首页探针、pandoc、81 条译注）。
2. **Phase 1**：`python tools/chapter_task.py N` 生成任务书；九章并行交付六件套；`check_chapter.py N` 逐章验收。
3. **Phase 2**：`merge_errata.py` 合并 errata；`build_summary.py` 生成总表与修订补丁；人工复核 `existing-note-wrong`（0 条）。
4. **Phase 3**：`plan_cards.py` → `gen_card_tasks.py` → 四组卡片手 → `datasets/grassmann/tools/validate_cards.py --strict` 0 error。
5. **Phase 4**：全篇质量门（9×6 文件、字数、编号、anchor、卡片 90 张）+ 汇总。

## 结果

| 项 | 数值 |
|---|---|
| 导读 | 9 章，15,669 汉字 |
| 笔记 | 9 章，19,421 汉字 |
| 批注 | 159 条（数学-难点 / 数学-补证 / 译注-核对 / 译文-问题 / 联系-他章 / 背景-补充） |
| errata | 58 条（high 2 / medium 18 / low 38；original-error 22、translation-error 14、term 11、formula 5、typo 4、numbering 2） |
| 已有译注复核 | 81 条，全部内容正确；5 条 ch05 页码元数据 +1 |
| 资料卡 | 90 张（73 概念 + 17 例子），`validate_cards.py --strict` 0 error |
| 跨章依赖 | 15 个具体点（`产出/汇总/交叉引用.md`） |

三条实质发现：

1. **ch2 两处 high**：英文原书 p.41/p.45 把「用 $\mathbb{P}^1$ 接桥」写成「把点对粘合」，按字面亏格对不上（应为 $2d-3$，原文写成 $2d-1$ 处差 2）。
2. **ch4 定义 5.1**：$\beta\in A$ 与权 $\alpha\in t^*$ 类型错位，且 $0\in B$ 时作用不平衡，与定理 5.6 冲突。
3. **ch9 §4/§6**：扭转层 $E_i=E_{j(i)}(-aC'_i)$ 的符号与度数记账对不上；§6 算例按正文数据实算维数 6，原文写 $\rho=5$（英文原式六项算得 2）。

## 权利

- 本目录**不收录**底本原文 PDF、中译本 PDF 与中译本 LaTeX 源；批注中的原文摘录仅为定位与核对，权利归原作者与出版方。
- 导读、笔记、批注、errata、脚本为本工程自产，按仓库 `LICENSE` 自产层条款发布。
- 资料卡文字为改写（`rights: "rewritten"`），公式照录并逐条注出处。

## 已知偏差

- 页表：中译 p.N 一律用 `zh-译文.pdf` 页序。ch4 实测「中译 = 原书 + 2」（BRIEF 页表按 +1 起点写），ch9 页脚印刷号 = 中译 PDF − 6；errata 的 `loc_zh` 按实测标。
- 9 章 report 均为 `partial`，各有 2–6 条存疑（数学缺口或原书排印问题），逐条列在 `产出/汇总/chNN-report.md`，未强行补全。
