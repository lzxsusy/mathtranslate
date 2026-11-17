# csw 资料卡规范（SCHEMA v1）

一卡一 JSON，UTF-8，缩进 2。`type` 只有两种：`concept`（概念/定理卡）与 `example`（可复算例子卡）。

## 概念卡必填字段

| 字段 | 类型 | 约束 |
| --- | --- | --- |
| `id` | string | `csw/concept/<slug>`，slug 小写连字符 |
| `type` | string | `"concept"` |
| `track` | string | `O A B C D E F G H` 之一 |
| `title` | string | 中文标题，可含公式 |
| `aliases` | string[] | ≥1，含英文名与常见译名 |
| `summary` | string | ≤120 汉字，一句话说清“是什么/为什么重要” |
| `question` | string | 以问号结尾，这张卡要回答的问题 |
| `definition.text` | string | 定义正文；数学用 `$...$` / `$$...$$` |
| `definition.notation` | string | 记号说明（归一化、符号约定） |
| `key_points` | string[] | ≥3，每条一个独立断言 |
| `formulas` | string[] | ≥1，关键公式（`$...$`） |
| `theorems` | object[] | ≥1，见下 |
| `pitfalls` | string[] | ≥1，常见错误 |
| `related` | string[] | ≥2，解析到本库 `id` |
| `sources` | object[] | ≥1，见下 |
| `rights` | string | 固定 `"rewritten"` |
| `status` | string | `draft` / `reviewed` / `published` |

`theorems[]` 字段：`name`、`statement`、`proof{status, steps[], gap_note}`、`source`。
- `proof.status` 只能是 `complete` 或 `sketch`；
- `sketch` 必须给 `gap_note`（本文没证什么、谁补的）；
- `steps[]` 每条 `{no, text, why}`：`text` 是这一步做什么，`why` 是为什么可以这样做。

## 例子卡必填字段

| 字段 | 类型 | 约束 |
| --- | --- | --- |
| `id` | string | `csw/example/<slug>` |
| `type` | string | `"example"` |
| `track` | string | 同上 |
| `title` / `summary` | string | summary ≤100 汉字 |
| `question` | string | 问号结尾 |
| `concept_refs` | string[] | ≥1，指向概念卡 |
| `setup` | string | 设定（参数、群、曲面、归一化） |
| `computation` | object[] | ≥2 步，每步 `{no, text, why}` |
| `result` | string | 结果 |
| `check` | string | 可手算或可脚本复核的核对方式 |
| `pitfalls` / `related` / `sources` | | 同概念卡 |

## sources[] 字段

`book`（文献名）、`section`（节/定理）、`pages`（印刷页，int 或 list）、`pdf_pages`（PDF 页，= 印刷页 + 偏移，本库按原文 49 页页图取 +1）、`anchor`（锚点，如 `witten1989/sections/s04-canonical.tex §3.1`）。`pages` 与 `pdf_pages` 为 list 时长度必须一致。

## 数学写作规则

1. 行内 `$...$`、行间 `$$...$$`；只用 MathJax 标准宏（`\operatorname`、`\mathbb`、`\frac`），不要用某本书的自定义宏。
2. 引用原文编号写「(3.4)」「命题 1.22」，页码写「p.371」。
3. 归一化必须显式声明：本文的 $L=\frac{k}{4\pi}\int\operatorname{Tr}(A\wedge dA+\frac23A^3)$ 与河野的 $\mathrm{CS}=\frac1{8\pi^2}\int\cdots$ 差常数，比较前先对齐（见 `appA_conventions` / 讲义附录 A）。
4. 中文全角标点；公式内英文标点。
5. 不写“显然”“易见”；每一步为什么成立写进 `why`。

## 校验

`tools/lint_csw.py` 检查：必填字段、id 前缀、track 枚举、summary 长度、`key_points`/`formulas`/`pitfalls` 下限、证明步骤字段、`related`/`concept_refs` 可解析、sources 完整性、pages/pdf_pages 对齐。**0 error、0 warning 才允许入库**。
