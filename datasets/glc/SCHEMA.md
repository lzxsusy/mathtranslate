# 几何 Langlands 资料卡规范（glc SCHEMA v1）

一卡一 JSON，UTF-8，缩进 2，`ensure_ascii=False`。`type` 两种：`concept`（定义/定理卡）与 `example`（可复算例子卡）。
本规范沿用 [`../csw/SCHEMA.md`](../csw/SCHEMA.md) v1，另加 `verification` 字段与联网核验流程（见 §5）。

## 1. 概念卡必填字段

| 字段 | 类型 | 约束 |
| --- | --- | --- |
| `id` | string | `glc/concept/<slug>`，slug 小写连字符 |
| `type` | string | `"concept"` |
| `track` | string | `O A B C D E F G H` 之一（见 `taxonomy.md`） |
| `title` | string | 中文标题，可含公式 |
| `aliases` | string[] | ≥1，含英文名与常见译名 |
| `summary` | string | ≤120 汉字，一句话说清“是什么/为什么重要” |
| `question` | string | 以问号结尾，这张卡要回答的问题 |
| `definition.text` | string | 定义正文；数学用 `$...$` / `$$...$$` |
| `definition.notation` | string | 记号说明（归一化、符号约定） |
| `key_points` | string[] | ≥3，每条一个独立断言 |
| `formulas` | string[] | ≥1，关键公式 |
| `theorems` | object[] | 结构见下；纯定义卡可为空数组 |
| `pitfalls` | string[] | ≥1，常见错误 |
| `related` | string[] | ≥2，解析到本库 `id` |
| `sources` | object[] | ≥1，见 §3 |
| `rights` | string | 固定 `"rewritten"` |
| `status` | string | `draft` / `reviewed` / `published` |
| `verification` | object | 见 §5；`published` 必填 |

`theorems[]`：`name`、`statement`、`proof{status, steps[], gap_note}`、`source`。
- `proof.status` 只能是 `complete` 或 `sketch`；`sketch` 必须给 `gap_note`（讲义没证什么、证明见谁）；
- `steps[]` 每条 `{no, text, why}`：`text` 这一步做什么，`why` 为什么可以这样做。

## 2. 例子卡必填字段

`id`（`glc/example/<slug>`）、`type`、`track`、`title`、`summary`（≤100 汉字）、`question`、
`concept_refs`（≥1，指向概念卡）、`setup`、`computation`（≥2 步，每步 `{no,text,why}`）、`result`、`check`、
`pitfalls`、`related`、`sources`、`rights`、`status`。

## 3. sources[] 字段

`book`（文献名）、`section`（节/定理）、`pages`（印刷页）、`pdf_pages`（PDF 页；本讲义印刷页=PDF 页）、
`anchor`（锚点，如 `源码/chapters/ch02.tex:23-35（定理 2.2.1）`）。`pages` 与 `pdf_pages` 为 list 时长度必须一致。

## 4. 数学写作规则

1. 行内 `$...$`、行间 `$$...$$`；只用 MathJax 标准宏（`\operatorname`、`\mathbb`、`\mathcal`、`\frac`），
   不得出现本讲义的自定义宏（`\Bun`、`\cF`、`\Qell`、`\thref` 等一律展开）。
2. 引用原文编号写「定理 2.2.1」「定义 2.1.1」，页码写「p.13」（印刷页 = PDF 页）。
3. 记号约定必须显式：$^\heartsuit$ 指 $t$-结构的心、$[d](d/2)$ 是移位叠扭转、$X^*(\check T)$ 是特征格。
4. 中文全角标点；公式内英文标点。
5. 不写“显然”“易见”；每一步为什么成立写进 `why`。
6. **不做超出原文的推广**：卡片陈述必须与讲义该条一致，不加条件、不加等价、不举原文没有的例子。

## 5. verification（联网核验，glc 扩展）

```json
"verification": {
  "status": "external-confirmed | source-only | rejected",
  "checked_on": "2026-11-18",
  "checks": [
    {"source": "nLab", "entry": "perverse sheaf", "url": "https://ncatlab.org/nlab/show/perverse+sheaf",
     "last_revised": "2026-10-16", "asserts": "与卡内定义的对应部分", "verdict": "match"}
  ]
}
```

- `external-confirmed`：至少一条 B 级白名单（nLab / Stacks Project / ProofWiki）或 A 级文献的公开页面
  明确支持卡内**全部数学断言**，核验员逐条读过并记录「哪句支持哪条断言」。
- `source-only`：外部页面找不到对应陈述（讲义自创的构造、尚未成文的定理），此时只保证与讲义一致；
  这类卡不得声称“外部已核”。
- `rejected`：核验发现与权威陈述冲突且无法调和。**不得入库**（lint 报错）。

核验记录另存 `verification.jsonl`（一行一卡：`id`、`status`、`checks`、`note`），与卡内字段一致。

## 6. 校验

`tools/lint_glc.py` 检查：必填字段、id 前缀、track 枚举、summary 长度、`key_points`/`formulas`/`pitfalls` 下限、
证明步骤字段、`related`/`concept_refs` 可解析、sources 完整性、pages/pdf_pages 对齐、`verification` 合法性。
**0 error 才允许入库**；`published` 的卡不得是 `source-only`。
