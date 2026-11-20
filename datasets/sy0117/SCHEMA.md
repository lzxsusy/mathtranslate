# sy0117 卡片规范（v1）

> 本数据集收录 Bocklandt《同调镜像对称性浅入门》中译二轮校订的 32 张资料卡：
> 20 张概念卡、12 张勘误卡。每张概念卡携带至少一条批注。
> 所有卡 `rights: "rewritten"`，`verification.status: "source-only"`。

## 1. 文件位置

```
datasets/sy0117/
├── cards/concepts/<slug>.json
├── cards/corrections/<slug>.json
├── index.jsonl
├── verification.jsonl
├── md/<slug>.md
├── taxonomy.md
├── MAP.md
├── SCHEMA.md
├── README.md
├── workflow/PRODUCTION.md
└── tools/{cards_concepts.py,cards_concepts2.py,cards_corrections.py,make_cards.py}
```

`<slug>` 是 `id` 最后一段，与文件名一致。

## 2. 共用字段

| 字段 | 类型 | 约束 |
|---|---|---|
| `id` | string | `sy0117/concept/<slug>` 或 `sy0117/correction/<slug>` |
| `type` | string | `concept` / `correction` |
| `track` | string | `第1章` … `第12章` |
| `title` | string | 中文标题，可含公式 |
| `summary` | string | 一句话，去公式后 ≤ 120 汉字 |
| `question` | string | 以 `？` 或 `?` 结尾 |
| `annotations` | object[] | ≥ 1，见 §3 |
| `related` | string[] | ≥ 2，必须解析到本数据集内已有 id |
| `sources` | object[] | 见 §4 |
| `rights` | string | 固定 `rewritten` |
| `status` | string | `draft` / `reviewed` / `published` |
| `verification` | object | `{status, checked_on, checks}` |

## 3. `annotations`

用户要求「资料卡需要携带批注」。类型限三种：

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
  "book": "Raf Bocklandt《同调镜像对称性浅入门》中译校订本（据 CUP 2021 英文版）",
  "section": "§1.1",
  "pages": [],
  "pdf_pages": [],
  "anchor": "08_source_code/SY01-17_同调镜像对称性浅入门/源码/chapters/ch01.tex:4-43",
  "page_note": "原书页码从略：本机无英文原书与页面图像，只以中译本节号与源码行号定位。"
}
```

- `anchor` 必须指向中译本源码的确切行号区间；无锚点不入库。
- `pages` / `pdf_pages` 允许为空。若填写，`pdf_pages = pages + 12`（本书 PDF 页 = 原书页 + 12）。
- **不凭记忆填原书页码**；没有页面图像时留空并写 `page_note`。

## 5. 概念卡专有字段

| 字段 | 类型 | 约束 |
|---|---|---|
| `aliases` | string[] | ≥ 1，英文术语或记号 |
| `definition.text` | string | 自足，不引用「上文」 |
| `definition.notation` | string | 记号说明，可空 |
| `key_points` | string[] | ≥ 3 |
| `formulas` | string[] | ≥ 1，LaTeX 源码（不带 `$`） |
| `theorems` | object[] | 可空 |
| `pitfalls` | string[] | ≥ 1，具体到「写错会怎样」 |

## 6. 勘误卡专有字段

| 字段 | 类型 | 约束 |
|---|---|---|
| `location` | string | 节号 + `chNN.tex:行号` |
| `original` | string | 只保留差异片段，不复制整段译文 |
| `corrected` | string | 只保留差异片段 |
| `why` | string | 必须给依据（上下文、数学自洽、定义），不得写「更通顺」 |
| `note` | string | 说明核验边界，如「未逐页核对英文原书」 |

## 7. 校验

```bash
python tools/make_cards.py --check
```

返回 0 表示全部通过。校验项见 `tools/make_cards.py` 的 `validate()`。
