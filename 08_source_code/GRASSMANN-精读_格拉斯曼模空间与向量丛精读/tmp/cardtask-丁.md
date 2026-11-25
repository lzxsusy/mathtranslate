# 卡片手任务书：丁组（ch4 + ch6 + ch9）

你是这一组的卡片手。本组共 **24 张卡**（概念 20、例子 4）。

## 开工先读

1. `C:\Users\admin\Downloads\_cards_grassmann\SCHEMA.md` 全文（字段规范，冲突时以它为准）
2. `C:\Users\admin\Downloads\_cards_grassmann\workflow\PRODUCTION.md`
3. `C:\Users\admin\Downloads\Grassmannians-精读\tmp\cards-ids.md`（全量 id，related 只能从这里取）
4. 你负责各章的 `产出\导读\chNN-导读.md`、`产出\笔记\chNN-笔记.md`、`产出\批注\chNN-批注.md`
5. 已有种子卡 3 张，看一张就知道语气与细致程度：`_cards_grassmann\cards\concepts\coherent-system.json`

## 本组清单

| # | id | 标题 | 章 | anchor |
|---|---|---|---|---|
| 1 | `grassmann/concept/balanced-action` | 平衡作用 | ch04 | `chapters/ch04.tex:153` |
| 2 | `grassmann/concept/extended-moduli-space` | 扩张模空间 | ch04 | `chapters/ch04.tex:30` |
| 3 | `grassmann/concept/intersection-pairing-via-vm` | 用 V_M 表示的相交配对 | ch04 | `chapters/ch04.tex:198` |
| 4 | `grassmann/concept/kirwan-map-and-class-d` | Kirwan 映射与正根类 | ch04 | `chapters/ch04.tex:53` |
| 5 | `grassmann/concept/partial-desingularization` | 部分消奇异 | ch04 | `chapters/ch04.tex:28` |
| 6 | `grassmann/concept/residue-formula-for-pairings` | 配对的留数公式 | ch04 | `chapters/ch04.tex:265` |
| 7 | `grassmann/example/wall-crossing-term-m20` | M(2,0) 的穿墙项 | ch04 | `chapters/ch04.tex:119` |
| 8 | `grassmann/concept/faddeev-index` | Faddeev 指标 | ch06 | `chapters/ch06.tex:426` |
| 9 | `grassmann/concept/gerbe-banded-by-mu-n` | $\mu_n$-带化的 gerbe | ch06 | `chapters/ch06.tex:521` |
| 10 | `grassmann/concept/isotrivial-family` | 等平凡族 / 簇的形式 | ch06 | `chapters/ch06.tex:70` |
| 11 | `grassmann/concept/parabolic-bundle` | 抛物丛与抛物次数 | ch06 | `chapters/ch06.tex:330` |
| 12 | `grassmann/concept/period-and-index` | 周期与指标 | ch06 | `chapters/ch06.tex:648` |
| 13 | `grassmann/concept/ramification-sequence` | 分歧正合列 | ch06 | `chapters/ch06.tex:673` |
| 14 | `grassmann/concept/root-stack` | 根叠 | ch06 | `chapters/ch06.tex:678` |
| 15 | `grassmann/concept/twisted-sheaf` | 扭曲层 | ch06 | `chapters/ch06.tex:527` |
| 16 | `grassmann/example/bicyclic-algebra-faddeev-4` | Faddeev 指标 4 的双四元数例子 | ch06 | `chapters/ch06.tex:463` |
| 17 | `grassmann/example/isotrivial-torelli` | 等平凡 Torelli 定理 | ch06 | `chapters/ch06.tex:191` |
| 18 | `grassmann/concept/brill-noether-locus-on-reducible-curves` | 可约曲线上的 Brill–Noether 簇 | ch09 | `chapters/ch09.tex:212` |
| 19 | `grassmann/concept/hilbert-compactification` | Hilbert 紧化与 Hilbert 稳定性 | ch09 | `chapters/ch09.tex:113` |
| 20 | `grassmann/concept/limit-linear-series-higher-rank` | 高秩极限线性系 | ch09 | `chapters/ch09.tex:136` |
| 21 | `grassmann/concept/maximal-subbundle-and-langes-conjecture` | 极大子丛与 Lange 猜想 | ch09 | `chapters/ch09.tex:175` |
| 22 | `grassmann/concept/reducible-nodal-curve-and-dual-graph` | 可约结点曲线与对偶图 | ch09 | `chapters/ch09.tex:49` |
| 23 | `grassmann/concept/slope-stable-torsion-free-sheaf` | 斜率稳定无挠层与深度 1 | ch09 | `chapters/ch09.tex:43` |
| 24 | `grassmann/example/limit-linear-series-on-a-chain-of-five-elliptic-curves` | 五条椭圆曲线链上的极限线性系算例 | ch09 | `chapters/ch09.tex:246` |

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
- `产出\汇总\card丁-report.md` 写好；
- 最后用一段话回报：写了多少张、哪几张 proof 只能 sketch、踩过的坑。
