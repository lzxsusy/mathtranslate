# 卡片手任务书：乙组（ch2 + ch7）

你是这一组的卡片手。本组共 **22 张卡**（概念 17、例子 5）。

## 开工先读

1. `C:\Users\admin\Downloads\_cards_grassmann\SCHEMA.md` 全文（字段规范，冲突时以它为准）
2. `C:\Users\admin\Downloads\_cards_grassmann\workflow\PRODUCTION.md`
3. `C:\Users\admin\Downloads\Grassmannians-精读\tmp\cards-ids.md`（全量 id，related 只能从这里取）
4. 你负责各章的 `产出\导读\chNN-导读.md`、`产出\笔记\chNN-笔记.md`、`产出\批注\chNN-批注.md`
5. 已有种子卡 3 张，看一张就知道语气与细致程度：`_cards_grassmann\cards\concepts\coherent-system.json`

## 本组清单

| # | id | 标题 | 章 | anchor |
|---|---|---|---|---|
| 1 | `grassmann/concept/clifford-index` | Clifford 指标 | ch02 | `chapters/ch02.tex:17` |
| 2 | `grassmann/concept/graded-minimal-resolution-and-betti-numbers` | 极小分次自由分解与分次 Betti 数 | ch02 | `chapters/ch02.tex:126` |
| 3 | `grassmann/concept/greens-conjecture` | Green 猜想 | ch02 | `chapters/ch02.tex:604` |
| 4 | `grassmann/concept/greens-dimension-formula` | Green 维数公式 | ch02 | `chapters/ch02.tex:248` |
| 5 | `grassmann/concept/kernel-bundle` | 核丛 | ch02 | `chapters/ch02.tex:209` |
| 6 | `grassmann/concept/koszul-cycle` | Koszul 闭链与退化轨迹 | ch02 | `chapters/ch02.tex:487` |
| 7 | `grassmann/concept/koszul-duality` | Koszul 对偶 | ch02 | `chapters/ch02.tex:235` |
| 8 | `grassmann/concept/maximal-rank-conjecture` | 极大秩猜想 | ch02 | `chapters/ch02.tex:803` |
| 9 | `grassmann/concept/minimal-syzygy-conjecture` | 极小合冲猜想 | ch02 | `chapters/ch02.tex:904` |
| 10 | `grassmann/concept/property-np` | 性质 (N_p) | ch02 | `chapters/ch02.tex:203` |
| 11 | `grassmann/concept/slope-of-effective-divisor` | 有效除子的斜率 | ch02 | `chapters/ch02.tex:77` |
| 12 | `grassmann/example/degree-6-genus-3-quadric` | (6,3,3) 上二次曲面上的曲线 | ch02 | `chapters/ch02.tex:813` |
| 13 | `grassmann/example/enriques-babbage-petri` | Enriques–Babbage–Petri 定理即 K_{1,2}=0 | ch02 | `chapters/ch02.tex:616` |
| 14 | `grassmann/example/max-noether-theorem` | Max Noether 定理即 K_{0,2}=0 | ch02 | `chapters/ch02.tex:612` |
| 15 | `grassmann/concept/brill-noether-number` | Brill–Noether 数 β | ch07 | `chapters/ch07.tex:98` |
| 16 | `grassmann/concept/dual-span` | 对偶张成 | ch07 | `chapters/ch07.tex:212` |
| 17 | `grassmann/concept/existence-region-d0` | $d_0$ 与存在域 $U(n,d,k)$ | ch07 | `chapters/ch07.tex:165` |
| 18 | `grassmann/concept/model-theorem` | 模型定理 | ch07 | `chapters/ch07.tex:170` |
| 19 | `grassmann/concept/petri-curve` | Petri 曲线 | ch07 | `chapters/ch07.tex:126` |
| 20 | `grassmann/concept/petri-map` | Petri 映射 | ch07 | `chapters/ch07.tex:113` |
| 21 | `grassmann/example/example-genus-10-d0` | $g=10$、$(2,12,4)$ 的 $d_0$ 例子（例 7.5） | ch07 | `chapters/ch07.tex:508` |
| 22 | `grassmann/example/example-non-stability-large-alpha` | 大 $\alpha$ 下不半稳定的例子（例 5.3） | ch07 | `chapters/ch07.tex:281` |

每张卡开工时：先在 `source\chapters\ch{NN}.tex` 里定位 anchor 那一行，上下读 60–120 行，
把定义/定理的措辞抄准；再看该章批注里同一位置的条目（那里有中译/原书/英文 PDF 三个页码与坑）。

# 通用要求（每张卡都必须满足，`validate_cards.py` 会逐条查）

1. **只写你自己的卡**：`_cards_grassmann\cards\concepts\<slug>.json` 或 `examples\<slug>.json`，
   文件名必须等于 id 最后一段；除此之外只写 `产出\汇总\card<组>-report.md`。
   不许改别人的卡、不许改 SCHEMA/taxonomy/源文件/BRIEF/STATUS。
2. **以中译为准**：中文数学与公式一律照 `Grassmannians-精读\source\chapters\chNN.tex`；
   PDF 文字层公式是碎的，只用来定位版面与页码。卡片里的 LaTeX 必须能在中译正文里找到对应说法。
3. 字段硬要求：
   - `id` = `grassmann/concept/<slug>` 或 `grassmann/example/<slug>`；`type` 与 id 一致；
     `title` 中文术语；`aliases` 数组（英文术语、常见别名）；
   - `track` 用任务书表格里给的，**不要自己改**；
   - `summary` **20–120 个汉字**（只数 CJK；英文术语不算），一句话说清「是什么 + 为什么重要」；
   - `question` 一个真会卡住读者的问题，**必须以「？」结尾**；
   - `definition.text` 用中译措辞 + 公式（`$...$`），`definition.notation` 写记号约定（别留空，空只是 warn 但要求写）；
   - `key_points` ≥3 条，每条一句、具体、不写套话；
   - `formulas` ≥1 条，每条 `$` 必须成对；
   - `theorems` ≥1 条：`{name, statement, source, proof}`。
     `proof.status` 三选一：`complete`（本章有证明，steps ≥2，每步 `{text, why}`，why 说清为什么这步成立）、
     `sketch`（有思路但缺一步，**必须**写 `gap_note` 说清缺哪一步、为什么补不出来）、
     `reference`（本章只引文献，`steps` 可空、`gap_note` 空）；
   - `pitfalls` ≥1 条：**真坑**（从该章批注/笔记里挑），写成「容易把 X 当成 Y，因为…」；
   - `related` ≥2 条，必须是 `tmp\cards-ids.md` 里真实存在的 id（不许编），其中至少 1 条跨组；
   - `sources` ≥1 条：`book` 固定写 `Grassmannians, Moduli Spaces and Vector Bundles (Clay 14)`，
     `section` 写章内位置（如 `ch3 §4 定理 4.1`），`pages_zh`/`pages_en` 写页码，
     `anchor` 必须是 `chapters/chNN.tex:行号` 且**指向非空行、内容与卡片对应**（在候选行 ±20 行内校正）；
   - `rights` = `"rewritten"`，`status` = `"draft"`；
   - 全文不得出现本机绝对路径（`C:\...`）、不得含 tab；JSON 里反斜杠写两个（`\\subseteq`→`\subseteq`）。
     建议用 Python `json.dump(obj, f, ensure_ascii=False, indent=2)` 落盘，避免手写转义出错。
4. **页码怎么拿到**：该卡 anchor 附近的内容在 `产出\批注\chNN-批注.md` 里通常已有同一条，
   位置行写着「中译 p.X / 原书 p.Y / en PDF p.Z」，直接抄；找不到就按 `tools\pdf_pages.py` 自己核。
5. **例子卡额外字段**：`concept_refs` ≥2 条（必须是概念卡 id）、`setup`（场景/数据/记号）、
   `computation`（把数算出来，带中间步骤与结果）。
6. **校验**：改完一批就跑
   `cd C:\Users\admin\Downloads\_cards_grassmann && python tools\validate_cards.py`
   只看自己文件名的 ERROR/WARN 并修掉；别的组的报错不要动。
   （不要用 `--strict`：taxonomy 要等 Lead 最后收口。）
7. **report**：`产出\汇总\card<组>-report.md`，含：写了多少概念/例子、每张卡的一句话摘要、
   哪些 card 的 proof 只能 sketch 及原因、id/related 上遇到的冲突、3–5 条「存疑」。


## 交付

- 卡片 JSON 全部落盘且 `validate_cards.py` 里**你负责的文件** 0 error；
- `产出\汇总\card乙-report.md` 写好；
- 最后用一段话回报：写了多少张、哪几张 proof 只能 sketch、踩过的坑。
