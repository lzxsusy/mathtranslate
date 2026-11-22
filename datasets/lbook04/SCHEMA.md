# lbook04 卡片规范（v1）

字段与 `../glc/SCHEMA.md` 一致，另加 `annotations`。

| 字段 | 约束 |
|---|---|
| `id` | `lbook04/concept/<slug>`，slug 以小写英文短横线命名，带章前缀（`ch6-local-zeta`） |
| `type` | `concept` |
| `track` | `O` / `L` / `M` / `T` / `G` |
| `title` | ≤30 字 |
| `aliases` | ≥1，含英文原名 |
| `summary` | ≤120 汉字（去掉公式后计） |
| `question` | 以「？」结尾，指向本章的核心问题 |
| `definition.text` / `.notation` | 一句话定义 + 记号说明 |
| `key_points` | ≥3 |
| `formulas` | ≥1，LaTeX 字符串 |
| `theorems` | 列表，可空 |
| `pitfalls` | ≥1，常见误读 |
| `annotations` | ≥1，`{type: 易错预警\|含糊点拨\|背景直觉, title, text}`，须给具体信息 |
| `related` | ≥2，指向本数据集内其它卡的 slug |
| `sources` | ≥1，`{book, section, pages（印刷页）, pdf_pages（PDF 页）, anchor（chNN.tex:起-止）}` |
| `rights` | `rewritten` |
| `status` | `draft` / `reviewed` / `published`；`published` 必须 `verification.status = external-confirmed` |
| `verification` | `{status: external-confirmed\|source-only\|rejected, checked_on, checks: []}` |

## 页次

`pages` 用原书印刷页；`pdf_pages` 由 `base.py` 的 `OFFSET` 表按章推出（底本 PDF 缺 6 页，偏移 8→2，见中译注本 `工程文件/PAGE_MAP.md`）。

## 校验

`python tools/build.py --check`：字段齐全、id 前缀、track 合法、summary 长度、问号结尾、key_points/formulas/pitfalls 下限、related 可解析、annotations 类型、pages/pdf_pages 等长、anchor 含 `chNN.tex`。
