# 数语规范 · 汇总

> 本文件与同目录 `TERMS.tsv` / `SYMBOLS.tsv` / `CONFLICTS.tsv` / `MACROS.tsv` 由 `tools/build_norm.py` 生成，
> **不要手改**。要改数据，改 `01_corpus_zh/termbase.jsonl`、`terms_frozen_*.tsv`、`symbols_frozen_*.tsv` 后重跑。

## 一、表规模

| 表 | 行数 | 覆盖 |
|---|---|---|
| 术语（TERMS.tsv） | 2277 | 9 个工程；去重键＝外文＋语种＋译名＋工程 |
| 记号（SYMBOLS.tsv） | 76 | 1 个工程（仅 FUNCTORIALITY 有冻结记号表） |
| 冲突（CONFLICTS.tsv） | 91 | 高 11 / 中 31 / 低 49 |
| 宏（MACROS.tsv） | 697 | 跨工程同名不同含义；其中出现在 ≥5 个工程的 364 个 |

## 二、术语分级

| 等级 | 条数 | 含义 |
|---|---|---|
| A | 170 | 原文页码/式号锚定 |
| B | 167 | 外部权威（nLab 等） |
| I | 135 | 本库定案 |
| D | 1805 | 未标级（待考） |

语种：en 1724 / ja 325 / other 228。状态：frozen 468 / confirmed 4 / candidate 1805。

## 三、冲突分类

| 类型 | 条数 | 含义 |
|---|---|---|
| 一外多中 | 14 | 同一外文有两个以上真正不同的译名——最需要裁决的一类 |
| 一中多外 | 32 | 同一译名对应多个外文（同语种才算撞车） |
| 等级不一致 | 38 | 同一译名在不同工程里标了不同等级 |

## 四、优先处理（高严重度）

| 类型 | 键 | 候选 | 建议 |
|---|---|---|---|
| 一外多中 | `Hamiltonian vector field` | 哈密顿向量场（B，1 处） ｜ Hamilton 向量场（D，1 处） | 取「哈密顿向量场」（等级更高） |
| 一外多中 | `Solution` | 解（A，1 处） ｜ 解答（D，1 处） | 取「解」（等级更高） |
| 一外多中 | `almost complex structure` | 殆复结构（B，1 处） ｜ 概复结构（D，1 处） | 取「殆复结构」（等级更高） |
| 一外多中 | `cocycle` | 余循环（I，1 处） ｜ 上闭链（D，1 处） | 取「余循环」（等级更高） |
| 一外多中 | `exact triangle` | 正合三角（B，1 处） ｜ 正合三角形（D，1 处） | 取「正合三角」（等级更高） |
| 一外多中 | `idempotent` | 幂等（B，1 处） ｜ 幂等元（D，1 处） | 取「幂等」（等级更高） |
| 一外多中 | `monodromy` | 单值性（I，1 处） ｜ 单值化作用（D，1 处） | 取「单值性」（等级更高） |
| 一外多中 | `obstruction` | 障碍（A，1 处） ｜ 阻碍（D，1 处） | 取「障碍」（等级更高） |
| 一外多中 | `skyscraper sheaf` | 摩天层（B，1 处） ｜ 摩天楼层（D，1 处） | 取「摩天层」（等级更高） |
| 一外多中 | `spin structure` | spin 结构（B，1 处） ｜ 旋量结构（D，1 处） ｜ 自旋结构（D，1 处） | 取「spin 结构」（等级更高） |
| 一外多中 | `unipotent` | 幂幺（B，1 处） ｜ 幺幂（I，1 处） | 取「幂幺」（等级更高） |

## 五、宏：形式化之前必须先对齐的部分

同一个宏名在不同工程的 `preamble.tex` 里被定义成不同含义，换算子文本时最容易出错。按出现工程数排序的前 8 个：

| 宏 | 出现工程数 | 不同含义数 | 含义变体 |
|---|---|---|---|
| `\R` | 83 | 6 | \ensuremath{\mathbb{R}} ｜ \mathbb{R} ｜ \mathbf R |
| `\Z` | 82 | 4 | \ensuremath{\mathbb{Z}} ｜ \mathbb{Z} ｜ \mathbf Z |
| `\C` | 80 | 4 | \ensuremath{\mathbb{C}} ｜ \mathbb{C} ｜ \mathbf C |
| `\Hom` | 79 | 5 | Hom ｜ \mathop{\mathrm{Hom}} ｜ \operatorname{Hom} |
| `\Tr` | 77 | 7 | Tr ｜ \mathop{\mathrm{Tr}}\nolimits ｜ \mathsf{Tr} |
| `\id` | 70 | 6 | \mathbf{1} ｜ \mathsf{Id} ｜ \operatorname{id} |
| `\Aut` | 69 | 5 | Aut ｜ \operatorname{Aut} ｜ \operatorname{\text{Aut}} |
| `\End` | 66 | 6 | End ｜ \operatorname{End} ｜ \operatorname{\text{End}} |

完整清单见 `MACROS.tsv`。注意：`\R` 这类「同一含义的多种写法」已在判定时折算（`\Bbb`→`\mathbb`、`\operatorname{}`/`\text{}`/`{\rm }`→`\mathrm{}`），
剩下的 `真冲突` 才是语义不同。

## 六、怎么用

1. 写译文前先查 `TERMS.tsv`：有登记就照用，不新造；查不到按 `STYLE_NL.md` §术语 处理并登记回源表。
2. 公式里的记号先查 `SYMBOLS.tsv` 与 `工程文件/preamble.tex`；不在表内的记号登记后再用。
3. `CONFLICTS.tsv` 的「建议」列是机械推断，**裁定权在仓主**；裁定后改源表，不要改生成物。
4. 改完跑 `python tools/build_norm.py --check`；表与源数据不一致会让闸门失败，确认无误再重建。

本表由 `tools/build_norm.py` 生成于 2026-11-21（术语 2277 / 记号 76 / 冲突 91 / 宏 697）。
