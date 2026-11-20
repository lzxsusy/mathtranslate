# sy0117 资料卡：Bocklandt《同调镜像对称性浅入门》二轮校订

> 语言：中文。底本：Raf Bocklandt, *A Gentle Introduction to Homological Mirror Symmetry*,
> CUP 2021 (LMS Student Texts 99)。中译校订本：`08_source_code/SY01-17_同调镜像对称性浅入门/`。
> 本数据集只发布改写后的卡片，不发布原书、译文全文或 PDF。

## 1. 规模

- **32 张卡**：20 张概念卡（每章至少 1 张）+ 12 张勘误卡。
- 每张概念卡至少携带 1 条批注；批注类型限 `易错预警` / `含糊点拨` / `背景直觉`。
- 12 张勘误卡对应二轮 89 处实际改动中的代表条目，`original` / `corrected` 只保留差异片段。

## 2. 文件

```
datasets/sy0117/
├── cards/concepts/*.json       # 20 张概念卡
├── cards/corrections/*.json    # 12 张勘误卡
├── index.jsonl                 # 逐卡摘要索引
├── verification.jsonl          # 核验台账
├── md/*.md                     # 人读渲染
├── taxonomy.md                 # 按章分类
├── MAP.md                      # 卡片地图
├── SCHEMA.md                   # 字段规范
├── README.md
├── workflow/PRODUCTION.md
└── tools/
    ├── cards_concepts.py       # 第 1–3 章概念卡数据
    ├── cards_concepts2.py      # 第 4–12 章概念卡数据
    ├── cards_corrections.py    # 勘误卡数据
    └── make_cards.py           # 校验与生成
```

## 3. 复跑

```bash
cd datasets/sy0117/tools
python make_cards.py --check   # 只校验
python make_cards.py           # 校验并重写 cards/、md/、index.jsonl、verification.jsonl、taxonomy.md、MAP.md
```

校验覆盖：id 唯一与前缀、必填字段、summary ≤ 120 汉字、question 问号结尾、
related ≥ 2 且可解析、annotations 类型、rights/status/verification、
anchor 文件存在且行号在文件内。

## 4. 权利与核验

- `rights: "rewritten"`：所有定义、解释与批注均为二轮校订时重写，不复制原书或译文长句；
  单处引文仅保留必要的差异片段。
- `verification.status: "source-only"`：只与中译定稿逐段对照、按数学自洽复核；
  **本机没有英文原书与页面图像**，未做逐页外部核验，故不标 `published`。
- `sources.pages` 留空：不凭记忆填原书页码；定位以 `section` + `anchor` 为准。

## 5. 与二轮校订的关系

- 89 处改动见 `工程文件/reports/ch01.md`–`ch12.md` 与 `工程文件/审校报告.md`。
- 12 张勘误卡是其中可独立成卡的代表条目，不替代逐章报告。
- 概念卡锚到修订后的 `源码/chapters/chNN.tex` 行号；若后续再改章节，需重跑校验并更新锚点。
