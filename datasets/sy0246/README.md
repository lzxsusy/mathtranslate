# sy0246 · Laumon《Drinfeld–Langlands 对应：Frenkel、Gaitsgory 与 Vilonen 的工作》资料卡集

底本：Gérard Laumon, *Travaux de Frenkel, Gaitsgory et Vilonen sur la correspondance de Drinfeld–Langlands*, Séminaire Bourbaki, 54e année, 2001–2002, exposé n° 906, juin 2002；19 页，法语；arXiv:math/0207078v1（2002-07-09）。
中译注本：`08_source_code/SY02-46_Laumon布尔巴基906Drinfeld-Langlands对应/`。

本集共 14 张卡：13 张 `concept`（覆盖全文论证主线）+ 1 张 `correction`（底本参考文献年份疑误，属外部书目核验，不涉及正文数学）。

## 口径

- **页码**：`pages` 与 `pdf_pages` 都取底本 PDF 页序 1–19，与印刷页眉 `906-N` 的 N 相同（第 1 页为标题页）。本篇两者相等，故一律不写 `page_note`。
- **引文**：`quote` 为法文原文逐字，取自 arXiv 版 PDF 文本层并与 TeX 源码 `Bourbaki2002.tex` 对校；公式下标在上标/下标被文本层压平时以 TeX 源码为准，引文只截取不含复杂公式的完整句段。
- **锚点**：`anchor` 指向中译注本 `源码/sections/*.tex` 的行号区间（`L起-L止`），是“这句话在译稿的哪里”的机械可解析答案；原文页码由 `pages` 给出。
- **验证**：`verification.checks[]` 每条为 `{entry, url, asserts, verdict}`，只允许真实可点开的 E1（底本 arXiv PDF 页锚、TeX 源码）与 E2（FGV/Gaitsgory/Braverman–Gaitsgory 原始论文、nLab 条目）。`verification` 只是线索，不是证据；卡片的证据是 `sources[].quote` 与原文页。
- **层级**：底本使用 `Théorème / Proposition / Corollaire / Lemme / Définition / Remarque`，卡片 `theorems[].name` 与 `kind` 不升不降；§0 的三条对象在底本中不编号，卡片中记作 `(0.2)` 等原文记号并注明“未编号”。
- **术语**：与 `工程文件/work/glossary.tsv` 一致；`proper`（反常层意义下）保留不译，`faisceau gratte-ciel` 译“摩天层”，`modification inférieure` 译“下修改”。

## 文件

```
sy0246/
  README.md            本文件
  SCHEMA.md            字段与校验口径
  MAP.md               原文页码 → 卡片 → 论证位置
  cards/concepts/*.json
  cards/corrections/*.json
  index.jsonl          由 tools/gen_index.py 生成
  verification.jsonl   由 tools/gen_index.py 生成（每条 check 一行）
  tools/make_cards.py  卡片源数据（唯一真源），生成 cards/*.json
  tools/gen_index.py   生成 index.jsonl 与 verification.jsonl
```

## 校验

```bash
python tools/card_spec_check.py --set sy0246 --strict
python datasets/sy0246/tools/gen_index.py --check
```

新卡或返工必须 `--strict` 且 hard=0、legacy=0；`index.jsonl` 与 `verification.jsonl` 必须与卡片一致。
