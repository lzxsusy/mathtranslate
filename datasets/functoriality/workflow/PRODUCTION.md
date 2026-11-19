# Functoriality 资料卡生产协议

本数据集由中译本《范畴辛几何中的函子性》（84 页，源码在 `book/`）与英文原稿
（arXiv:2210.11159v1，68 页）逐节裁切而来。每张卡一个 JSON，遵守 `SCHEMA.md`。

## 一、分工与写卡范围

- `workflow/cards_plan.tsv` 是唯一清单（70 张）：`slug / type / track / title / chapter / section / pages / owner / brief`。
- 按 `owner` 列分派，写者只写自己名下、对应目录里的 `<slug>.json`。
- 卡 id：`functoriality/{concept|deriv|correction}/<slug>`。

## 二、内容来源（三级）

1. **表述依据**：中译本源码 `book/chapterN.tex`（已按《数学文献翻译纪律》逐句对读英文重校，公式与术语可信）。
2. **数学核对**：英文作者源码 `en/intro.tex`（§1）、`en/prelim.tex`（§2）、`en/functors.tex`（§3）、
   `en/symp.tex`（§4）、`en/applications.tex`（§5）；页锚见 `work/pagemap.tsv`（节号→印刷页）。
3. **术语**：`work/术语表.tsv` 是唯一译名来源；卡里不自行改译名。
   需要外部依据时只查白名单：原论文/经典教材（A 级）、nLab、Stacks Project、EMS、MathWorld、DLMF（B 级）；
   知乎、百度百科、CSDN、公众号、博客、视频课笔记、AI 摘要一律不用。

## 三、硬性规则

1. `formulas` 逐字取自 `chapterN.tex`（含宏与上下标），不自行重排；工具会做子串回查。
2. 综述里「转述」的定理只能标 `proof.status = "sketch"` 或 `"none"`，不得编造完整证明。
3. `sources.section` / `pages` 照 `cards_plan.tsv` 抄；`anchor` 以「原书 p.」开头，页码在 `pages` 内。
4. `related` ≥2 条，必须是清单里存在的 id；优先同节或前后依赖。
5. `pitfalls` ≥2 条具体易错点；能落到本译本的译注（`book/chapterN.tex` 里的 `yizhu` 环境）就更好。
6. `status` 一律先写 `draft`，由 Lead 复核后改 `reviewed`。
7. 不复制原文整段（`rights: "rewritten"`），不写本机路径，不出图。

## 四、校验流程

```sh
python tools/lint_cards.py cards --allow-missing   # 结构（related 悬空可先放行）
python tools/audit_pages.py cards                  # 页锚 vs 节区间
python tools/check_formulas.py cards --corpus <中译本 book 目录>  # 公式子串回查
python tools/build_index.py                        # index.jsonl
python tools/render_md.py                          # md/
```

Lead 终审：公式回查 0 miss、`lint --strict` 0 error、`audit_pages` 0 issue，
再逐卡抽查数学正确性（定义、定理陈述、推理链）。
