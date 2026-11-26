# 资料卡 JSON 规范（GGL 汉化流水线 v1）

沿用 `datasets/gtgl15` 与 `datasets/kw06` 的字段与纪律，只把「单一的文献字母表」换成
「每篇一篇底本」的写法。一张卡一个 JSON 文件，UTF-8、缩进 2 空格、`ensure_ascii=False`。
概念卡放 `cards/concepts/`，推导卡放 `cards/derivations/`，文件名 = id 最后一段。

`id` 前缀 = 数据集的 `ggl<NN>`（NN 为合集里的序号），与 `datasets/ggl<NN>/` 同名。

---

## 概念卡

```json
{
  "id": "ggl03/concept/rigid-surface-operator",
  "type": "concept",
  "title": "刚性曲面算子",
  "aliases": ["rigid surface operator", "刚性曲面缺陷"],
  "track": "D",
  "summary": "不超过 120 汉字的摘要（去掉公式与空白后计数）",
  "question": "卡片正面的自测题，一句话，以问号结尾",
  "definition": {
    "text": "定义的完整陈述，可含行内 $...$ 与行间 $$...$$",
    "notation": "符号约定；没有就写空字符串"
  },
  "key_points": ["要点 1", "要点 2", "要点 3"],
  "formulas": ["$$F-\\varphi\\wedge\\varphi=0$$"],
  "theorems": [
    {
      "name": "命题的名字",
      "statement": "完整陈述",
      "proof": {
        "status": "complete",
        "steps": [{"no": 1, "text": "一步推导", "why": "为什么成立 / 为什么要它"}],
        "gap_note": ""
      },
      "source": "A p.44 eq (4.1)"
    }
  ],
  "pitfalls": ["真正的易错点", "第二条"],
  "related": ["ggl03/concept/other-slug", "ggl03/deriv/some-chain"],
  "sources": [
    {"text": "A", "section": "§4.1", "pages": [40, 44], "anchor": "A p.40–44 eq (4.1)"}
  ],
  "rights": "rewritten",
  "status": "draft",
  "provenance_note": "A=原文明写；B=原文暗示、我们重建；C=我们的判断"
}
```

## 推导卡

```json
{
  "id": "ggl03/deriv/sdual-to-rigid",
  "type": "derivation",
  "title": "S-对偶把 XX 送到 YY",
  "aliases": ["S-duality on surface operators"],
  "track": "D",
  "summary": "不超过 120 汉字的摘要",
  "question": "这条推导要回答的问题，以问号结尾",
  "goal": "要得到的结论（一句话）",
  "setup": ["前提 1", "前提 2"],
  "steps": [
    {
      "no": 1,
      "text": "这一步做什么",
      "why": "为什么必须这样 / 依据是什么",
      "locator": "A p.70 eq (5.9)",
      "provenance": "A"
    }
  ],
  "result": "推导最终得到什么（可以带公式）",
  "gaps": ["原文只写「应该」、没有逐条验证的地方"],
  "pitfalls": ["这条推导最常见的错误"],
  "related": ["ggl03/concept/some-slug"],
  "sources": [
    {"text": "A", "section": "§5.4–§5.5", "pages": [70, 77], "anchor": "A p.70–77 eq (5.9)"}
  ],
  "rights": "rewritten",
  "status": "draft",
  "provenance_note": "..."
}
```

---

## 字段规则

| 字段 | 必填 | 规则 |
|---|---|---|
| `id` | 是 | `<前缀>/concept/<slug>` 或 `<前缀>/deriv/<slug>`；slug 只含小写字母、数字、连字符 |
| `type` | 是 | `concept` 或 `derivation` |
| `title` | 是 | 中文标题，可带英文原名 |
| `aliases` | 是 | 数组，至少 1 条（英文名 / 缩写 / 别名） |
| `track` | 是 | `A` 四维物理与对偶 / `B` 扭化与拓扑 / `C` 曲线与模空间 / `D` 二维、膜与算子 / `E` Langlands 与翻译器 / `O` 总览 |
| `summary` | 是 | ≤120 汉字（去掉 `$...$` 与空白后计数） |
| `question` | 是 | 以 `？` 或 `?` 结尾 |
| `definition` / `goal`+`setup` | 是 | 概念卡用 `definition`；推导卡用 `goal` + `setup`（≥1 条） |
| `key_points` | 概念卡 | ≥3 条 |
| `formulas` | 概念卡 | ≥1 条，LaTeX 写作 `$...$` 或 `$$...$$` |
| `theorems` | 概念卡 | 可为空；`proof.status` ∈ `complete`/`sketch`/`gap`；`complete` 要求 ≥2 步且 `text`、`why` 非空；`sketch`/`gap` 必须有 `gap_note` |
| `steps` | 推导卡 | ≥3 步；每步 `text`/`why`/`locator`/`provenance` 必填；`provenance` ∈ A/B/C |
| `result` | 推导卡 | 非空 |
| `gaps` | 推导卡 | 数组；若任一步 provenance ≠ A，至少 1 条 |
| `pitfalls` | 是 | ≥2 条 |
| `related` | 是 | ≥1 条，元素必须是本数据集内已存在的卡 id |
| `sources` | 是 | ≥1 条；`text` ∈ `A`（本篇底本）/`B`（Kapustin–Witten 2006, hep-th/0604151）/`C`（其他，须在 `section` 写清出处）/`D`；`pages` 是两个整数且落在 1..本篇页数；`anchor` 形如 `A p.38 eq (4.1)`；`quote` 写**支撑这条出处的英文原句**（12–120 字符，逐字抄，可用 `...` 省略中间）——`tools/verify_pages.py` 拿它在原文里回查页码，写不出 quote 的出处等于没出处 |
| `rights` | 是 | 固定 `rewritten` |
| `status` | 是 | `draft`（自检未过）或 `dev`（自检通过、待人类认证）；**不许写 `prod`/`train`** |
| `provenance_note` | 是 | 一句话说明 A/B/C 构成与最没把握处 |
| `corrections` | 否 | 数组；本篇原文有笔误时登记，每条 `{"id":"E1","note":"原文…，依…订正"}`。`id` 必须存在于本包 `errata.tsv`，`note` 要写清原文写法、订正依据（来源+定位） |

### 关于外部核对

卡片里的每个公式都要求「三源定则」（`BRIEF.md` §9）：本篇 + 至少两处独立出处。
若两处出处一致而本篇不同，按订正写并加 `corrections`；只有一处冲突则**保留原文**
并在 `provenance_note` 里标「存疑（见 errata E№）」，不擅自改。抄错一个符号，
整张卡在语料里就是坏的——这比少一张卡严重得多。

## 写作纪律

1. **断言带 locator**：每条事实性断言都要能在 `sources` 或单步 `locator` 里找到出处。
2. **不复制原文**：英文短引 ≤120 字符；公式可以照抄（公式不是版权文本），叙述必须自己写。
3. **不写本机路径**。
4. **诚实标注**：原文只写 "we expect" / "should be" 的，provenance 记 B 或 C，并写进 `gaps`。
5. **术语统一**：twist=扭化，eigenbrane=特征膜，Hecke eigensheaf=Hecke 特征层，
   canonical coisotropic brane=典范余各向同性膜，'t Hooft 算子不译，BPS 不译，
   ramification=分歧，wild ramification=野分歧，endoscopy=内窥。
