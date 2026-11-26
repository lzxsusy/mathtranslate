# 09 工作流程

## 顺序与每步产出

1. **读规范**（约 15 分钟）：`TASK.md`、`XREF.md`、`BRIEF.md` §9–10、`cards/SCHEMA.md`，并抽看 `out/08_ggl08` 的 `notes.md`、`trace.md` 与两张卡，确定字段形状与 status 流程。
2. **通读正文**（约 2 小时）：用 `read` 逐页读 `txt/09/p001.txt`–`p037.txt`（37 页），边读边在笔记里记「页—式号—一句话」。这一步产出：节结构、11 条主定理候选、约 60 条逐字引文。
3. **建外部证据**（约 1 小时）：下载 arXiv v1 到 `external/` 并 `pdftotext -layout` 出 `v1.txt` 做 diff；抓 nLab "Nahm's equation"；查 `datasets/kw06`、`datasets/bdh` 与旧卡 ggl12/ggl21 的相关卡；把 p.11、p.19 渲染成 PNG 核对称号（`external/pages/`）。
4. **定卡表**（约 30 分钟）：按「概念 8±2、推导 3±1」定 10 概念 + 4 推导；每张卡先写一行「它回答什么问题」，再分配 A 源页码，确认每张卡至少 3 条 quote 能在对应页找到。
5. **写卡**（约 2 小时）：先写概念卡，再写推导卡；`sources` 全部用 A，`anchor` 写 `A p.N eq (x.y)`，`related` 只指向本包已存在的 id。写完后统一 `status: draft`。
6. **自检迭代**（约 1.5 小时）：`lint_cards.py --strict` → 改 id 大小写、补 notes；`verify_pages.py --strict` → 按报告的实际页码改 `pages` 或换 quote；`term_index.py check` → 改撞名标题/别名；`audit_locators.py` → 核对每个 anchor 的式号确实在该页出现。
7. **写文档**（约 1 小时）：`notes.md`（骨架、主定理、接口、核对与勘误、不懂）、`terms.tsv` 27 行、`excerpts.md` 3 段、`errata.tsv` 1 条、`trace.md` 14 条、`workflow.md`。
8. **收尾**：四检全绿后把 14 张卡的 `status` 从 `draft` 改为 `dev`，再跑一遍 lint/verify 确认状态改动没破坏结构。

## 最耗时 / 最易错

- **最耗时**：逐字引文与页码核对。`verify_pages.py` 只查 `sources.quote`，而 quote 必须 12–120 字符且逐字；同一句话在 txt 里常被换行/连字拆开，选短句最稳。其次是式号核对：`audit_locators.py` 要求 `p.N` 那一页真的出现 `(x.y)`，所以 anchor 不能凭记忆写。
- **最易错**：
  1. 把 txt 的提取缺陷当成原文——本例是 $\sigma$ 上的横线（(2.3)）与 (2.15) 的 $\vee$；必须以 PDF 渲染为准。
  2. `--max-pages 37` 对**所有** text（A/B/C/D）生效，引 KW06 p.127 会被拒；外部大页数证据只能写 notes。
  3. `id` 的 slug 必须全小写（`bB-dual-of-xi` 会被 lint 拒）。
  4. `related` 指向的卡必须已存在，且 `corrections[].id` 必须能在 `errata.tsv` 找到。
  5. `errata.tsv` 每行必须 ≥9 个 tab 字段，`high` 必须有依据2；`low` 只保留原文并标存疑。

## 重做怎么改

若重来，顺序改为：先定 14 张卡的 id 与标题并跑 `term_index` 预检（避免写完再改名），再按卡分配 quote 并立即跑 `verify_pages`（避免一次性攒 60 条引文后集体对不上），最后才写 notes 的长表。`notes.md` 的外部来源表可以先从 `external/xref.json` 的参考文献列表生成骨架，再补定位。
