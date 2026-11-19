# Abouzaid–Bottman《范畴辛几何中的函子性》资料卡

Mohammed Abouzaid & Nathaniel Bottman, *Functoriality in categorical symplectic geometry*（arXiv:2210.11159v1，2022-10-20，68 页、43 幅插图）中文译注本的**可检索、可自测**资料卡。

一张卡只回答一个问题：**概念卡**回答「这是什么、为什么需要、哪里会错」，**推导卡**回答「这条论证怎么一步步走通、每步凭什么」，**勘误卡**回答「原文哪里写错、为什么必须改」。

- 底本：arXiv 英文原文 68 页；**PDF 页 = 印刷页**。卡中的 `原书 p.N` 一律指英文原文的印刷页。
- 材料：84 页中文译注本（43 条译注、209 条术语、62 条索引条目）——译稿本身**不入库**，只把其中的数学与校订结论裁成卡。
- 规模：**83 张** —— 56 张概念卡 + 14 张推导卡 + 13 张勘误卡；73 个推导步骤、266 条易错点，页锚覆盖原文 p.2–65 的 41 个印刷页。
- 权利：全部 `rights: "rewritten"`。定义、证明、要点用自己的话重写；公式照录（逐字取自中译本 chapter 源码，`check_formulas.py` 校验）；勘误卡给出「原文—应作—依据」三层，不复制原文整段。

## 30 秒入口

| 想做什么 | 打开 |
|---|---|
| 看全书骨架与卡的位置 | [MAP.md](MAP.md) |
| 按类型、轨道浏览 | [md/index.md](md/index.md) |
| 按 id / 页码检索 | [index.jsonl](index.jsonl) |
| 看一张概念卡 | [md/concepts/operadic-principle.md](md/concepts/operadic-principle.md) |
| 看一条推导链 | [md/derivations/mww-composition.md](md/derivations/mww-composition.md) |
| 看一条勘误 | [md/corrections/d01-cpn-should-be-cn.md](md/corrections/d01-cpn-should-be-cn.md) |
| 字段规范 | [SCHEMA.md](SCHEMA.md) |
| 生产与验收记录 | [workflow/PRODUCTION.md](workflow/PRODUCTION.md) |

## 四条轨道

| 轨道 | 主题 | 概念 | 推导 | 勘误 | 合计 |
|---|---|---|---|---|---|
| A | 辛流形、Floer 上同调、Fukaya 范畴、操作子原理、带曲率 A∞、边界上链与反常（第 1–2 章） | 15 | 4 | 2 | 21 |
| B | 凝聚层与拉格朗日对应、拼接 Floer、Φ#、A∞-双模、伴随、辛约化、Fukaya 构造复合（第 3 章） | 18 | 7 | 4 | 29 |
| C | 巫曲线与巫球、(A∞,2)-范畴 Symp、相对 2-操作子、奇点消去（第 4 章） | 9 | 1 | 2 | 12 |
| D | Dehn 扭转范畴化、Khovanov、Floer 场论、HMS、G-流形、形式群、Barr–Beck（第 5 章） | 14 | 2 | 5 | 21 |

## 这套卡是怎么来的

1. **翻译先行**：旧译源码逐句对读 arXiv 英文源码（`intro/prelim/functors/symp/applications` 五个文件）与 arXiv PDF 页图，重校成 84 页中译注本；术语按《数学文献翻译纪律 v2.0》冻结后统一，译注 43 条（每条带 A/B 级来源标记）。
2. **页码定锚**：由英文 PDF 逐页抽文（`pdftotext -layout`）建立「节号 → 印刷页区间」映射（35 条，见 `workflow/PRODUCTION.md`）；卡片的 `sources.pages` 与 anchor 照该表填，不凭印象。
3. **裁成卡片**：按 `workflow/cards_plan.tsv` 的 70 条计划（56 概念 + 14 推导）分五人并行写作，概念卡按「定义—要点—公式—定理与证明—易错点」重写；推导卡每步标 `provenance`（A 原文/ B 补出/ C 判断）并给 `locator`；勘误卡 13 张来自译注中登记的原文笔误（D01、D08–D13、D18、D20–D24）。
4. **机器质检**：
   - `lint_cards.py --strict`：字段、类型、长度、id 与文件名、related 可解析、页码 1–68、anchor 以「原书 p.」开头、禁本机绝对路径 —— **0 error / 0 warn**。
   - `audit_pages.py`：每卡页码范围落在所属节的页区间内、跨度 ≤3 页，且 anchor 页码落在 pages 内 —— 0 issue。
   - `check_formulas.py --corpus book/`：232 条公式在 5 个章节源码中**逐字命中 232/232**。
   - `build_index.py` 生成 83 行 `index.jsonl`；`render_md.py` 渲染 83 张 Markdown + `md/index.md`；`gen_map.py` 生成 `MAP.md`。

## 质检

```bash
python tools/lint_cards.py cards --strict    # 0 error 才算过
python tools/audit_pages.py cards            # 页锚点自洽
python tools/check_formulas.py cards --corpus <中译本 book 目录>   # 公式逐字核对
python tools/build_index.py                  # 重建 index.jsonl
python tools/render_md.py                    # 重建 md/
python tools/gen_map.py                      # 重建 MAP.md
```

## 已知限制

- 全部卡 `status: "draft"`：机器质检通过，但**未经人类逐卡认证**；按仓库规则只能标 `dev`，不能直接当 `train`。
- 推导卡的 `provenance` 里 B/C 是诚实的标记：综述多处「转述」他人结果（Fukaya 2017、WW16、Seidel 2019、EL19、AS19），这类卡 `proof.status` 只给 `sketch` 或 `none`，`gap_note` 写明缺在哪。
- 原文是 survey / research announcement：第 5 节的 expectation 5.14、5.15 与 conjecture 5.6 都是**猜想性陈述**，卡里按「预期」「猜想」措辞，不得当已证定理引用。
- 勘误卡只覆盖译注登记过的 13 处原文笔误，不是全文勘误；未登记的存疑处留在中译本工程的疑点清单里。
- 公式核对以中译本源码为准（`check_formulas.py`），语义核对以英文原文与页图为准；两处不一致时以英文原文为最终依据，并在卡中说明。
