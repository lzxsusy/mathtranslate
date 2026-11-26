# lawrge24 · LAWRGE 2024 相对朗兰兹对偶笔记资料卡

底本：*LAWRGE 2024 NOTES — Relative Langlands Duality*，Ben-Zvi / Sakellaridis / Venkatesh 主讲的工作坊参会者笔记，2024-12-03，73 页，无 arXiv 号、无正式出版信息。笔记开篇自述「极不完整、未校订」（very incomplete and unpolished）。

中译注本见 `08_source_code/SY02-15_相对朗兰兹对偶/`（65 页，2026-11-21，v1.0）。

本目录把这部笔记拆成 **47 张中文资料卡**（41 张概念卡 + 6 张推导卡），用来回答「相对朗兰兹对偶到底说了什么、哪些是定理、哪些只是猜想、证明缺口在哪」。卡片是中文重写（`rights: rewritten`），不是原文翻译，也不替代中译注本与原文。

## 规模

| 轨道 | 名称 | 概念 | 推导 | 合计 |
| --- | --- | ---: | ---: | ---: |
| O | 总览：TQFT 语言与全书证明地图 | 3 | 0 | 3 |
| A | TQFT、配边与算术–拓扑字典（§1–§3） | 6 | 1 | 7 |
| B | 边界条件、raviolo 与 Hecke–Satake（§4、§7） | 8 | 0 | 8 |
| C | 球簇、相对 Cartan 与对偶群（§8–§10） | 8 | 2 | 10 |
| D | Plancherel、局部猜想与 shearing（§8、§11） | 5 | 1 | 6 |
| E | 周期层、L-层与整体猜想（§5、§12–§15） | 11 | 2 | 13 |
| **合计** | | **41** | **6** | **47** |

## 核验状态

| 状态 | 数量 | 含义 |
| --- | ---: | --- |
| `external-confirmed` | 0 | 尚未逐条对照 nLab / Stacks Project / 原始论文 |
| `source-only` | 47 | 已对齐 LAWRGE 2024 原文的节与页，`quote` 经 lint 逐字命中 |
| `rejected` | 0 | — |

全部卡片 `status: draft`。**这是「读懂笔记」的卡，不是「已核验定理」的卡。** 笔记本身是参会者整理，不是作者定稿；引用前请回到原文与所列参考文献。

已做的外部术语核对只有一项：译名对照香蕉空间（bananaspace.org）的社区用词，记录见 `08_source_code/SY02-15_相对朗兰兹对偶/工程文件/work/术语外部核对_香蕉空间.md`。该站对相对 Langlands 方向覆盖很薄（搜「朗兰兹」仅命中「局部类域论」一条），因此多数术语只能沿用本库既有译法。

## 目录

```text
lawrge24/
├── README.md
├── SCHEMA.md                  # 卡片体例（id、轨道、字段、硬规则）
├── _BRIEF.md                  # 施工简报：47 卡主清单与页码
├── index.jsonl                # 一行一卡（id/type/track/title/summary/path）
├── verification.jsonl         # 47 条来源对齐记录
├── taxonomy.md                # 按轨道分组的卡片总表
├── cards/concepts/*.json      # 41 张概念卡
├── cards/derivations/*.json   # 6 张推导卡
└── tools/
    ├── pages.py               # 按 `===== PDF PAGE N =====` 页末标记切页
    ├── lint_cards.py          # 结构、页码、quote 逐字命中
    ├── build_index.py         # 生成 index.jsonl
    ├── gen_docs.py            # 生成 taxonomy.md
    └── make_verification.py   # 生成 verification.jsonl
```

## 复现

在仓库根目录：

```bash
python datasets/lawrge24/tools/lint_cards.py
python datasets/lawrge24/tools/build_index.py
python datasets/lawrge24/tools/gen_docs.py
python datasets/lawrge24/tools/make_verification.py
```

当前结果：`cards=47 errors=0 warnings=0`。

## 怎么用

- 想先看全局：`O` 轨的 `relative-langlands-duality`、`a-and-b-theories`、`proof-map`。
- 想理解「为什么 Langlands 对偶是四维 TQFT」：`A` 轨，从 `tqft-axioms`、`bordism-category` 到 `langlands-as-4d-tqft`、`arithmetic-topological-dictionary`。
- 想抓局部硬定理：`B` 轨（几何 Satake、谱作用、derived Satake）与 `D` 轨（Plancherel、局部猜想）。
- 想理解球簇与对偶群怎么组装：`C` 轨，`spherical-variety` → `multiplicity-free` → `rank-one-freeness` → `dual-group` → `relative-cartan`。
- 想追整体猜想：`E` 轨，`period-sheaf` → `l-sheaf` → `global-conjecture`，再看 `tate-example`、`eisenstein-example`、`whittaker-sheaf`、`hitchin-gaiotto`、`miraculous-duality`。

## 与其他层的关系

- `08_source_code/SY02-15_相对朗兰兹对偶/资料卡/`：工程级五件套（速览、结果清单、论证地图、条款索引、术语文献勘误），按译本页码组织，适合随译文查。
- 本目录：卡片层，按**原文 PDF 页**锚定，适合检索与交叉引用；被 `make_stats.py` 与站点索引统计。
- `datasets/benzvi_glc/`：Ben-Zvi 2026 几何 Langlands 综述的 42 张卡，主题相邻但底本不同（arXiv:2605.23167）。
