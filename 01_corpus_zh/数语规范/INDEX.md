# 数语规范 · 汇总

> 本文件与同目录 `TERMS.tsv` / `SYMBOLS.tsv` / `CONFLICTS.tsv` / `MACROS.tsv` 由 `tools/build_norm.py` 生成，
> **不要手改**。要改数据，改 `01_corpus_zh/termbase.jsonl`、`terms_frozen_*.tsv`、`symbols_frozen_*.tsv` 后重跑。

## 一、表规模

| 表 | 行数 | 覆盖 |
|---|---|---|
| 术语（TERMS.tsv） | 2502 | 10 个工程；去重键＝外文＋语种＋译名＋工程 |
| 记号（SYMBOLS.tsv） | 76 | 1 个工程（仅 FUNCTORIALITY 有冻结记号表） |
| 冲突（CONFLICTS.tsv） | 85 | 高 0 / 中 31 / 低 54 |
| 宏（MACROS.tsv） | 742 | 跨工程同名不同含义；其中出现在 ≥5 个工程的 388 个 |

## 二、术语分级

| 等级 | 条数 | 含义 |
|---|---|---|
| A | 306 | 原文页码/式号锚定 |
| B | 205 | 外部权威（nLab 等） |
| I | 238 | 本库定案 |
| D | 1753 | 未标级（待考） |

语种：en 1949 / ja 325 / other 228。状态：frozen 686 / confirmed 11 / candidate 1805。

## 三、冲突分类

| 类型 | 条数 | 含义 |
|---|---|---|
| 一中多外 | 35 | 同一译名对应多个外文（同语种才算撞车） |
| 等级不一致 | 36 | 同一译名在不同工程里标了不同等级 |
| 命名不合规 | 1 | 机械可判的命名毛病（句读、残片、过长） |

## 四、优先处理（高严重度）

（当前没有高严重度冲突。）

## 五、宏：形式化之前必须先对齐的部分

同一个宏名在不同工程的 `preamble.tex` 里被定义成不同含义，换算子文本时最容易出错。按出现工程数排序的前 8 个：

| 宏 | 出现工程数 | 不同含义数 | 含义变体 |
|---|---|---|---|
| `\R` | 89 | 6 | \ensuremath{\mathbb{R}} ｜ \mathbb{R} ｜ \mathbf R |
| `\Hom` | 89 | 5 | Hom ｜ \mathop{\mathrm{Hom}} ｜ \operatorname{Hom} |
| `\Z` | 88 | 4 | \ensuremath{\mathbb{Z}} ｜ \mathbb{Z} ｜ \mathbf Z |
| `\C` | 86 | 4 | \ensuremath{\mathbb{C}} ｜ \mathbb{C} ｜ \mathbf C |
| `\Tr` | 80 | 7 | Tr ｜ \mathop{\mathrm{Tr}}\nolimits ｜ \mathsf{Tr} |
| `\Aut` | 76 | 5 | Aut ｜ \operatorname{Aut} ｜ \operatorname{\text{Aut}} |
| `\id` | 75 | 6 | \mathbf{1} ｜ \mathsf{Id} ｜ \operatorname{id} |
| `\End` | 73 | 6 | End ｜ \operatorname{End} ｜ \operatorname{\text{End}} |

完整清单见 `MACROS.tsv`。注意：`\R` 这类「同一含义的多种写法」已在判定时折算（`\Bbb`→`\mathbb`、`\operatorname{}`/`\text{}`/`{\rm }`→`\mathrm{}`），
剩下的 `真冲突` 才是语义不同。

## 六、怎么用

1. 写译文前先查 `TERMS.tsv`：有登记就照用，不新造；查不到按 `STYLE_NL.md` §术语 处理并登记回源表。
2. 公式里的记号先查 `SYMBOLS.tsv` 与 `工程文件/preamble.tex`；不在表内的记号登记后再用。
3. `CONFLICTS.tsv` 的「建议」列是机械推断，**裁定权在仓主**；裁定后改源表，不要改生成物。
4. 改完跑 `python tools/build_norm.py --check`；表与源数据不一致会让闸门失败，确认无误再重建。

本表由 `tools/build_norm.py` 生成于 2026-11-21（术语 2502 / 记号 76 / 冲突 85 / 宏 742）。
