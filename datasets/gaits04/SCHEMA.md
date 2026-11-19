# gaits04 卡片规范（v1）

> 本数据集收录 D. Gaitsgory《几何朗兰兹的非正式导论》的 23 张概念卡。
> 所有卡都是 `rights: "rewritten"`：用自己的话重写的事实与结构，不复制原书表达；
> 单处引文 ≤ 60 字并注出处。

## 1. 文件位置

```
datasets/gaits04/
├── cards/concepts/<slug>.json   # 一卡一文件，<slug> = id 最后一段
├── index.jsonl                  # 逐卡一行摘要索引
├── verification.jsonl           # 逐卡核验台账
├── md/<slug>.md                 # 渲染版（供人读）
├── taxonomy.md                  # 六轨分类
├── MAP.md                       # 卡片地图（含原书页）
├── SCHEMA.md                    # 本文件
├── README.md
├── workflow/PRODUCTION.md       # 生产流程与复跑方式
└── tools/                       # cards_1.py、cards_2.py、make_cards.py
```

## 2. 必填字段

| 字段 | 类型 | 约束 |
|---|---|---|
| `id` | string | `gaits04/concept/<slug>`，slug 与文件名一致 |
| `type` | string | 固定 `concept` |
| `track` | string | `O` / `A` / `B` / `C` / `D` / `E` |
| `title` | string | 中文标题，可含公式 |
| `aliases` | string[] | ≥ 1，英文术语或记号 |
| `summary` | string | 一句话，去公式后 ≤ 120 汉字 |
| `question` | string | 以 `？` 结尾，卡要回答的问题 |
| `definition.text` | string | 定义正文，自足，不引用「上文」 |
| `definition.notation` | string | 记号说明 |
| `key_points` | string[] | ≥ 3 |
| `formulas` | string[] | ≥ 1，LaTeX 源码（不带 `$`） |
| `theorems` | object[] | 可空；每项 `{name, statement, proof:{status,steps,gap_note}, source}` |
| `pitfalls` | string[] | ≥ 1，具体到「写错会怎样」 |
| `annotations` | object[] | ≥ 1，见 §3 |
| `related` | string[] | ≥ 2，必须解析到本数据集内已有 id |
| `sources` | object[] | 见 §4 |
| `rights` | string | 固定 `rewritten` |
| `status` | string | `draft` / `reviewed` / `published` |
| `verification` | object | `{status, checked_on, checks}`，见 §5 |

## 3. `annotations`（本数据集的关键字段）

用户要求「资料卡需要携带批注」。每张卡至少一条，类型限三种：

```json
{"type": "易错预警", "title": "同一符号，两个世界", "text": "……"}
```

- `易错预警`：读者大概率会写错/理解错的地方，必须说明「错在哪、正确是什么」。
- `含糊点拨`：原文一句带过、需要补出的推理或记号约定。
- `背景直觉`：为什么这个概念在此处重要，与其他部分如何衔接。

`type` 不在上述三值内一律校验失败。

## 4. `sources`

```json
{
  "book": "D. Gaitsgory《几何朗兰兹的非正式导论》，Bernstein–Gelbart 编《朗兰兹纲领导论》第 12 章，Birkhäuser 2004，pp. 269–281",
  "section": "§2.1",
  "pages": [274],
  "pdf_pages": [276],
  "anchor": "08_source_code/SY02-13_.../源码/chapters/ch12_sec2.tex:3-20（§2.1）"
}
```

- `pages` 是原书页码；`pdf_pages` 必须是 `pages` 各元素 + 2（底本 PDF 页 = 原书页 + 2）。
- `anchor` 指向中译本源码的确切行号区间。**无锚点不入库。**

## 5. `verification`

```json
{"status": "source-only", "checked_on": "2026-11-19", "checks": []}
```

- `source-only`：只与底本页图和译文逐条对照，未做外部独立核验。
- `external-confirmed`：另经 nLab / Stacks Project / 原论文等外部来源确认，`checks` 记来源与结论。
- 规则：`status: "published"` 的卡必须是 `external-confirmed`。本数据集目前全部为 `source-only`，故全部为 `reviewed`。

## 6. 校验

```bash
python tools/make_cards.py --check   # 只校验
python tools/make_cards.py           # 校验并重写全部产物
```

校验覆盖：id 前缀与唯一性、必填字段、track 合法、question 以问号结尾、
summary 长度、key_points/formulas/pitfalls 下限、related 可解析且非自指、
annotations 类型、rights/status/verification 取值、pages 与 pdf_pages 对齐、
anchor 存在且指向 `ch12_sec*.tex`。
