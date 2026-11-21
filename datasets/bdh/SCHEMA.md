# bdh 卡片规范（v1）

> 本数据集收录 Beilinson–Drinfeld《Quantization of Hitchin’s Integrable System and Hecke
> Eigensheaves》（386 页，2020 年 pdfTeX 重排版）中译校订本的资料卡：概念卡 + 勘误卡。
> 每张概念卡至少携带一条批注；每张勘误卡对应译本的一处实际修改或一处原文笔误的判定。
> 全部卡 `rights: "rewritten"`，锚点指向仓内中译源码的确切行号。

## 1. 文件位置

```
datasets/bdh/
├── cards/concepts/<slug>.json      # 手写，唯一权威来源
├── cards/corrections/<slug>.json   # 手写
├── index.jsonl                     # 由 tools/make_cards.py 生成
├── verification.jsonl              # 由 tools/make_cards.py 生成
├── md/<slug>.md                    # 由 tools/make_cards.py 生成
├── taxonomy.md                     # 生成
├── MAP.md                          # 生成
├── SCHEMA.md                       # 本文件
├── README.md
├── workflow/PRODUCTION.md
└── tools/make_cards.py
```

`<slug>` 是 `id` 的最后一段，与文件名一致，只允许小写字母、数字与连字符。
**不要手改**生成物；改卡后跑 `python tools/make_cards.py` 重新生成。

## 2. 共用字段

| 字段 | 类型 | 约束 |
|---|---|---|
| `id` | string | `bdh/concept/<slug>` 或 `bdh/correction/<slug>` |
| `type` | string | `concept` / `correction` |
| `track` | string | `§0`…`§10`、`§N.M`、`参考文献` |
| `title` | string | 中文标题，可含公式 |
| `summary` | string | 一句话，去掉 `$...$` 后汉字 ≤ 120 |
| `question` | string | 以 `？` 或 `?` 结尾 |
| `annotations` | object[] | ≥ 1，见 §3 |
| `related` | string[] | ≥ 2，必须解析到本数据集内已有 id，不得指向自身 |
| `sources` | object[] | ≥ 1，见 §4 |
| `rights` | string | 固定 `rewritten` |
| `status` | string | `draft` / `reviewed`；`published` 仅限 `external-confirmed` |
| `verification` | object | `{status, checked_on, checks}` |

## 3. `annotations`

卡上的批注，类型限三种：

```json
{"type": "易错预警", "title": "同一符号，两个世界", "text": "……"}
```

- `易错预警`：读者大概率会写错/理解错的地方，必须说明「错在哪、正确的是什么、错一步会得到什么错结论」。
- `含糊点拨`：原文一句带过、需要补出的推理或记号约定（对应译本里的 `[含糊点拨]` 译注）。
- `背景直觉`：为什么这个概念在此处重要、与前后文如何衔接、在物理与几何两侧分别对应什么。

`type` 不在上述三值内一律校验失败；每条 `text` 少于 40 汉字会被警告。

## 4. `sources`

```json
{
  "book": "A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本）",
  "section": "§3.1",
  "pages": [61, 62],
  "pdf_pages": [61, 62],
  "anchor": "08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch02.tex:12-140",
  "page_note": "页码为原文印刷页；本书 PDF 页 = 印刷页，偏移 0。"
}
```

- `anchor` 必须指向仓内中译源码的确切行号区间，文件必须存在且 `1 ≤ a ≤ b ≤ 行数`；不满足就不入库。
- `pages` 取原书**印刷页码**（本书 PDF 页 = 印刷页，偏移 0），`pdf_pages` 必须严格等于 `pages`。
- 页码来自原书 PDF（386 页）的页眉，本轮逐页核对；不确定的页宁可把区间写宽，不要编造。
- `page_note` 写明页码口径或「只以节号与源码行号定位」。

## 5. 概念卡专有字段

| 字段 | 类型 | 约束 |
|---|---|---|
| `aliases` | string[] | ≥ 1，英文术语或记号 |
| `definition.text` | string | 自足，不引用「上文」；先给数学定义，再给物理图像 |
| `definition.notation` | string | 记号说明，可空 |
| `key_points` | string[] | ≥ 3，每条一个可检验的断言 |
| `formulas` | string[] | ≥ 1，LaTeX 源码**不带 `$`** |
| `theorems` | object[] | 可空；`{name, statement, proof{status, steps[], gap_note}, source}` |
| `pitfalls` | string[] | ≥ 2，具体到「写错会怎样」 |

## 6. 勘误卡专有字段

| 字段 | 类型 | 约束 |
|---|---|---|
| `location` | string | 节号 + `sXX.tex:行号` |
| `original` | string | 只保留差异片段，不复制整段译文 |
| `corrected` | string | 只保留差异片段；必须与 `original` 不同 |
| `why` | string | 必须给依据（英文原文、上下文、数学自洽、术语表），不得写「更通顺」 |
| `note` | string | 核验边界：改了什么、没改什么、哪一步是判断而非事实 |

勘误卡分两类，在 `note` 里注明：
1. **译本改译**：本轮实际改动了中译源码（`original` → `corrected`），锚点区间必须包含该处。
2. **原文笔误判定**：原文本身有误、译本照录并加 `[原文疑误]` 译注；此时 `original` 写原文/原译的写法，`corrected` 写建议写法，`note` 必须先写「译文未改，照原文保留」。

## 7. 校验与生成

```bash
python tools/make_cards.py --check     # 只校验，0 表示通过
python tools/make_cards.py             # 校验并重新生成 index/md/MAP/taxonomy
python tools/make_cards.py --strict    # 警告也算失败
```

校验项：字段齐全、`track` 形态、`question` 问号、`summary` 汉字上限、`annotations` 类型与厚度、
`related` 可解析且不自指、`sources` 页码对齐（`pdf_pages = pages`）、`anchor` 落在仓内源码行号区间、
勘误卡片段能在锚点区间里找到、概念卡 `key_points`/`formulas`/`pitfalls` 下限。

## 8. 写作纪律

- 断言带锚点：每个 `key_point`、`pitfall` 都应该能在 `sources` 的区间里找到依据。
- 不复制原文：英文短引 ≤ 120 字符；译文片段只摘差异部分。
- 不写本机路径；不写「本数据集」「本卡」之类的自我指涉。
- 诚实标核验：`checks` 逐条写清做了什么（对照原文源码、对照原文 PDF 页、公式号核对、仅中译自洽），
  没做的写「未做……」，不要用「已全面核验」这类空话。
