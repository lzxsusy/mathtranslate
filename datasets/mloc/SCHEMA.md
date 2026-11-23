# 局部化资料卡规范（mloc SCHEMA v1）

底本：Dragan Miličić《Localization and Representation Theory of Reductive Lie Groups》（作者自排讲义，129 印刷页，6 章 28 节）。
本库卡片依据本仓中译本（`08_source_code/SY07-11_局部化与约化李群的表示论（Miličić）/`）逐条抽取，**不是**从英文原文另起炉灶。

一卡一 JSON，UTF-8，缩进 2，`ensure_ascii=False`。`type` 两种：`concept`（定义/定理卡）与 `example`（可复算例子卡）。

## 0. 与 dmod 的关系

本书是作者前作《D-模的代数理论讲义》（本库 `datasets/dmod/`，工程 SY07-10）的**续篇**：前作造 D-模的语言，本书把它用到旗簇与表示论。
两库共享记号习惯（`$\mathcal{D}$`、`holonomic=完整`、`rights="rewritten"`），但**卡片不重复**：

- dmod 已有的通用概念（D-模、直像/逆像、完整模、特征簇、Riemann–Hilbert）在本库只作 `related` 链接，不另立卡；
- 本库只收本书**特有**的构造与定理：扭层、齐性扭层、`D_λ`、`U_θ`、局部化函子与 n-同调、交织函子、Harish-Chandra 层、Verma/广义 Verma 的 KL 算法。

## 1. 概念卡必填字段

| 字段 | 类型 | 约束 |
| --- | --- | --- |
| `id` | string | `mloc/concept/<slug>`，slug 小写连字符 |
| `type` | string | `"concept"` |
| `track` | string | `O A B C D E F G H` 之一（见 `taxonomy.md`） |
| `title` | string | 中文标题，可含公式 |
| `aliases` | string[] | ≥1，含英文名与常见译名 |
| `summary` | string | ≤120 汉字，一句话说清「是什么/为什么重要」 |
| `question` | string | 以问号结尾，这张卡要回答的问题 |
| `definition.text` | string | 定义正文；数学用 `$...$` / `$$...$$` |
| `definition.notation` | string | 记号说明 |
| `key_points` | string[] | ≥3，每条一个独立断言 |
| `formulas` | string[] | ≥1，关键公式 |
| `theorems` | object[] | 结构见下；纯定义卡可为空数组 |
| `pitfalls` | string[] | ≥1，常见错误 |
| `related` | string[] | ≥2，解析到本库或 dmod 的 `id` |
| `sources` | object[] | ≥1，见 §3 |
| `rights` | string | 固定 `"rewritten"` |
| `status` | string | `draft` / `reviewed` / `published` |
| `verification` | object | 见 §5；`published` 必填 |

`theorems[]`：`name`、`statement`、`proof{status, steps[], gap_note}`、`source`。

- `proof.status` 只能是 `complete` 或 `sketch`；`sketch` 必须给 `gap_note`（讲义没证什么、证明见谁）；
- `steps[]` 每条 `{no, text, why}`：`text` 这一步做什么，`why` 为什么可以这样做。

## 2. 例子卡必填字段

`id`（`mloc/example/<slug>`）、`type`、`track`、`title`、`summary`（≤100 汉字）、`question`、
`concept_refs`（≥1）、`setup`、`computation`（≥2 步，每步 `{no,text,why}`）、`result`、`check`、
`pitfalls`、`related`、`sources`、`rights`、`status`。

## 3. sources[] 字段

`book`（书名）、`section`（节/定理）、`pages`（**印刷页**）、`pdf_pages`（**PDF 页 = 印刷页 + 4**）、
`anchor`（锚点，如 `源码/chapters/ch02a.tex:88-96（引理 1.2）`）。`pages` 与 `pdf_pages` 为 list 时长度必须一致。

> 页码是本库与 dmod 的最大差别：本书印刷页从 1 开始，PDF 页从 5 开始（前 4 页是封面、空白、目录），
> 所以**每张卡都必须同时给 `pages` 与 `pdf_pages`**，否则无法回源。

## 4. 数学写作规则

1. 行内 `$...$`、行间 `$$...$$`；只用 MathJax 标准宏（`\operatorname`、`\mathbb`、`\mathcal`、`\mathfrak`、`\frac`），
   不得出现译本的自定义宏（`\D`、`\g`、`\h`、`\n` 等一律展开成 `\mathcal{D}`、`\mathfrak{g}`、`\mathfrak{h}`、`\mathfrak{n}`）。
2. 引用原文编号写「引理 1.2」「定理 2.3」（原书是「节.序号」），**跨章时前面加章**：「第 2 章引理 1.2」。
   不要写成 `2.1.2` 三段式——书里印的不是这个，读者对不上。页码写「p.18」。
3. 记号必须显式：`$D_\lambda$` 在本书第 2 章起指 `$D_{X,\lambda+\rho}$`（与第 1 章差 $\rho$），凡用到必须写明按哪一种。
   同理，凡出现 `$M(\lambda)$`、`$L(\lambda)$`、`$I(w,\lambda)$` 的卡，必须写明「参数 $\lambda$ ↔ 最高权 $\lambda-\rho$」；
   并注意书中 `$I(w,\lambda)$`（标准模）与 `$I(\lambda)$`（对偶 Verma 模）同字母异构造，不可混用。
4. 中文全角标点；公式内英文标点。
5. 不写「显然」「易见」；每一步为什么成立写进 `why`。
6. **不做超出原文的推广**：卡片陈述必须与该条一致，不加条件、不加等价、不举原文没有的例子。
7. **跨页条目**：一条 `sources` 覆盖两页（或更多）时，`pages` 写**连续并集**（如 `[87,88]`、`pdf_pages [91,92]`），
   保住「该段跨页」的信息；仍须逐项满足 `pdf_pages − pages = 4`。
8. **只引文献、底本未证的结果**（局部化定理 `L.1.1`/`L.1.2`/`L.4.1` 一类）：`proof.status` 写 `sketch`，
   `gap_note` 写明「底本只引文献、未给证明」，不得写成已证，也不得替作者补证明。

## 5. verification（联网核验）

```json
"verification": {
  "status": "external-confirmed | source-only | rejected",
  "checked_on": "2026-11-23",
  "checks": [
    {"source": "nLab", "entry": "localization", "url": "https://ncatlab.org/nlab/show/localization",
     "last_revised": "2026-10-16", "asserts": "与卡内定义的对应部分", "verdict": "match"}
  ]
}
```

- `external-confirmed`：至少一条 B 级白名单（nLab / Stacks Project / ProofWiki）或 A 级文献的公开页面
  明确支持卡内**全部数学断言**，核验员逐条读过并记录「哪句支持哪条断言」。
- `source-only`：外部页面找不到对应陈述（讲义自创的构造），只保证与讲义一致；不得声称「外部已核」。
- `rejected`：与权威陈述冲突且无法调和。**不得入库**。

核验记录另存 `verification.jsonl`（一行一卡：`id`、`status`、`checks`、`note`），与卡内字段一致。

## 6. 校验

`tools/lint.py` 检查：必填字段、id 前缀、track 枚举、summary 长度、`key_points`/`formulas`/`pitfalls` 下限、
证明步骤字段、`related`/`concept_refs` 可解析、sources 完整性、`pages` 与 `pdf_pages` 对齐（差值恒为 4）、
`verification` 合法性。**0 error 才允许入库**；`published` 的卡不得是 `source-only`。
