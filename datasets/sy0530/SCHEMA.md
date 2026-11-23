# sy0530 卡片格式（SCHEMA）

一张卡 = `cards/concepts/<slug>.json` 或 `cards/work/<slug>.json`，UTF-8、LF、2 空格缩进。字段名与 `datasets/sy0117` 一致（插件 ingest 只认这一套）。

## 必填

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `id` | string | `<集>/<type>/<slug>`，如 `sy0530/concept/analytic-double` |
| `type` | `concept` \| `work` | 概念卡 / 书目卡 |
| `track` | string | 本卷用「第2章」 |
| `title` | string | 中文题名 |
| `aliases` | string[] | 英文原词 + 常见变体 |
| `summary` | string | 一句话，≤160 字，读者只读这一句也能用 |
| `question` | string | 这张卡回答的那个「为什么/怎么」问题 |
| `definition` | `{text, notation}` | `text` 是可独立引用的定义；`notation` 是记号约定 |
| `key_points` | string[] | 3–6 条，每条一个可验证的断言 |
| `formulas` | string[] | LaTeX 片段（不带 `$`） |
| `theorems` | object[] | 见下 |
| `pitfalls` | string[] | 至少 1 条；写「容易怎么错」而不是「注意」 |
| `related` | string[] | 其他卡的 `id` |
| `sources` | object[] | 见下 |
| `rights` | string | 本卷一律 `rewritten`（自撰，不抄原文） |
| `status` | string | `reviewed` |
| `verification` | object | `{status, checked_on, checks[]}` |

## theorems[]

| 字段 | 说明 |
| --- | --- |
| `name` | 定理/命题/引理号，如「命题 2.2.8」 |
| `statement` | 陈述，可带 LaTeX |
| `proof.status` | `full` / `sketched` / `cited` / `absent` |
| `proof.steps[]` | `{no, text, why}`；`why` 必填，写「这一步凭什么成立」 |
| `proof.gap_note` | 原书没证或只给主线时的说明；`full` 时留空串 |
| `source` | 「§2.2.2，印刷页 87」这样的位置串 |

## sources[]

| 字段 | 说明 |
| --- | --- |
| `book` | 书名 + 编号 |
| `section` | 底本小节号 |
| `pages` | 印刷页码数组；无页码用 `[]` |
| `pdf_pages` | 底本 PDF 页码数组（= 印刷页 + 10） |
| `anchor` | 译稿路径 + 行号，如 `…/chapters/ch02e.tex:127-150` |
| `page_note` | 可选，页码口径有歧义时写清楚 |

## 与插件的关系

`kb/ingest.py json` 读 `datasets/**/cards/**/*.json`，按 `id` 去重；没有 `pages` 的卡会被 `build_kb.py` 判为不可索引（「可检索 = 可回溯」）。本集每张卡都有页码，全部可索引。

## 不做的事

- 不写 `review.reviewer`：本卷没有第二人复核，写了就是假账。
- 不把 `verification.status` 写成 `blindtest-passed`：没做盲测。
