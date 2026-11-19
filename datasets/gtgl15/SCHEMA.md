# 资料卡 JSON 规范（gtgl15 v1）

本包所有卡都是**一卡一 JSON**：UTF-8 编码、缩进 2 空格、`ensure_ascii=False`（中文与公式直接写，不转义）；文件名 = `id` 最后一段 + `.json`。两类卡共用 `id/type/title/aliases/track/summary/question/pitfalls/related/sources/rights/status/provenance_note`，其余字段按类型不同。

- id 前缀：`gtgl15/concept/<slug>` 或 `gtgl15/deriv/<slug>`，`slug` 只用小写字母、数字与连字符。
- 六条轨道（`track`）：`A` Hitchin 几何与谱曲线、`B` 对偶环面与 T-对偶、`C` 膜、线算符与本征膜、`D` 't Hooft 算符与赫克修正、`E` 行列式线丛与本征值、`O` 总览。
- 来源字母（`sources[].text`）：`A` = 底本 arXiv:1506.04293v3（印刷页 1–78）；`B` = KW06（hep-th/0604151）；`C` = Hitchin 1987、Donagi–Pantev 等原始文献；`D` = nLab / Stacks Project / EMS 白名单。
- `pages` 一律写**印刷页**（= PDF 页 − 1），两个整数，`1 ≤ pages[0] ≤ pages[1] ≤ 240`。

## 概念卡

```json
{
  "id": "gtgl15/concept/eigenbranes",
  "type": "concept",
  "title": "本征膜",
  "aliases": ["eigenbrane", "本征膜"],
  "track": "C",
  "summary": "线算符作用后只差张量一个向量空间的膜叫本征膜。",
  "question": "为什么本征值是向量空间而不是数？",
  "definition": {"text": "……", "notation": "……"},
  "key_points": ["……", "……", "……"],
  "formulas": ["$$……$$"],
  "theorems": [
    {
      "name": "定理名",
      "statement": "……",
      "proof": {"status": "sketch", "steps": [{"no": 1, "text": "……", "why": "……"}], "gap_note": "……"},
      "source": "A p.37"
    }
  ],
  "pitfalls": ["……", "……"],
  "related": ["gtgl15/concept/line-operators", "gtgl15/concept/magnetic-eigenbranes"],
  "sources": [{"text": "A", "section": "§4.1", "pages": [37, 37], "anchor": "A p.37"}],
  "rights": "rewritten",
  "status": "dev",
  "provenance_note": "A=……；B=……；C=……。最没把握处：……"
}
```

## 推导卡

```json
{
  "id": "gtgl15/deriv/magnetic-hecke-eigenvalue",
  "type": "derivation",
  "title": "磁本征膜的赫克本征值（U(1) 与 SU(N)）",
  "aliases": ["magnetic eigenvalue", "Hecke eigenvalue"],
  "track": "E",
  "summary": "……",
  "question": "……",
  "goal": "……",
  "setup": ["……", "……"],
  "steps": [
    {
      "no": 1,
      "text": "……",
      "why": "……",
      "locator": "A p.71 eq (7.6)",
      "provenance": "A"
    }
  ],
  "result": "……",
  "gaps": ["……"],
  "pitfalls": ["……", "……"],
  "related": ["gtgl15/concept/magnetic-eigenbranes", "gtgl15/concept/determinant-line-pairing"],
  "sources": [{"text": "A", "section": "§7.1.1", "pages": [68, 71], "anchor": "A p.71 eq (7.6)"}],
  "rights": "rewritten",
  "status": "dev",
  "provenance_note": "A5：……；B=……。最没把握处：……"
}
```

## 字段规则

| 字段 | 必填 | 规则 |
| --- | --- | --- |
| `id` | 是 | `gtgl15/concept/<slug>` 或 `gtgl15/deriv/<slug>`；与目录一致；`slug` = 文件名 |
| `type` | 是 | `concept` / `derivation` |
| `title` | 是 | 中文为主，可带英文；公式用 `$...$` |
| `aliases` | 是 | 数组，≥1；英文名与原术语 |
| `track` | 是 | `A/B/C/D/E/O` 之一 |
| `summary` | 是 | ≤120 汉字（去掉 `$...$` 与空白后的字符数）；一句话说清是什么 |
| `question` | 是 | 以 `？` 或 `?` 结尾；概念卡是“先自测”的问题 |
| `definition` / `goal` | 概念卡 / 推导卡 | 概念卡 `definition.text` 必填，`notation` 写记号；推导卡 `goal` 写结论目标 |
| `key_points` / `setup` | 概念卡 / 推导卡 | 概念卡 ≥3 条；推导卡 ≥1 条前提 |
| `formulas` | 概念卡是 | ≥1 条，`$$...$$` 包裹 |
| `theorems` | 概念卡是 | 每条有 `name/statement/proof{status}/source`；`complete` 需 ≥2 步且每步 `text/why`；`sketch`/`gap` 必须有 `gap_note` |
| `steps` | 推导卡是 | ≥3 步；每步 `text/why/locator/provenance` 齐全；`locator` 形如 `A p.38 eq (4.4)`、`provenance ∈ {A,B,C}` |
| `result` | 推导卡是 | 一行结论 |
| `gaps` | 推导卡（任意一步非 A 时 ≥1） | 诚实列出缺的证明步骤 |
| `pitfalls` | 是 | ≥2 条；写“最容易讲错”的地方 |
| `related` | 是 | ≥1；**必须指向本包真实存在的 id** |
| `sources` | 是 | ≥1；每条 `text/section/pages/anchor`；`anchor` 形如 `A p.38 eq (4.4)`；`pages` 用印刷页 |
| `rights` | 是 | 固定 `"rewritten"` |
| `status` | 是 | `"draft"` / `"dev"`；本包全用 `dev`，不许写 `prod`/`train` |
| `provenance_note` | 是 | 一句话说明 A/B/C 各占哪些内容，并点名**最没把握处** |

## 写作纪律

1. **断言必须带 locator**：`sources[].section` 写原文章节，`pages` 写印刷页，`anchor` 写成可查形式（`§2.6 p.12 eq (2.15)` 这类）；不许编页码或编号。
2. **不抄原文**：中文用自己的话重写（`rights: "rewritten"`）；英文短引 ≤120 字符；公式可以照录。
3. **不写本机路径**：卡里不出现 `C:\`、`/Users/`、`file://` 等（lint 会拦）。
4. **诚实标注**：原文只暗示的标 `B`，我们自己的判断标 `C`，并在推导卡的 `gaps` 与概念卡 `theorems.proof.gap_note` 写清楚。
5. **术语统一**：希格斯丛、希钦纤维化、谱曲线、本征膜、电本征膜、磁本征膜、赫克修正、陈–帕顿、摩天楼层、行列式线丛，与中文初译本一致。
