# 资料卡 JSON 规范（kw06 v1）

一张卡一个 JSON 文件，UTF-8、缩进 2 空格、`ensure_ascii=False`。
概念卡放 `cards/concepts/`，推导卡放 `cards/derivations/`，文件名 = id 最后一段。

两类卡共用：`id` / `type` / `title` / `track` / `summary` / `question` / `pitfalls` / `related` / `sources` / `rights` / `status` / `provenance_note`。

---

## 概念卡

```json
{
  "id": "kw/concept/hitchin-moduli",
  "type": "concept",
  "title": "Hitchin 模空间 M_H",
  "aliases": ["Hitchin moduli space", "M_H", "希格斯丛模空间"],
  "track": "C",
  "summary": "不超过 120 汉字的摘要（去掉公式与空白后计数）",
  "question": "卡片正面的自测题，一句话，以问号结尾",
  "definition": {
    "text": "定义的完整陈述，可含 LaTeX 行内公式 $...$ 与行间公式 $$...$$",
    "notation": "符号约定；没有就写空字符串"
  },
  "key_points": ["要点 1", "要点 2", "要点 3"],
  "formulas": ["$$F - \\varphi\\wedge\\varphi=0,\\qquad D\\varphi=D^\\ast\\varphi=0$$"],
  "theorems": [
    {
      "name": "命题的名字",
      "statement": "完整陈述",
      "proof": {
        "status": "complete",
        "steps": [
          {"no": 1, "text": "推导的一步", "why": "为什么这一步成立 / 为什么需要它"}
        ],
        "gap_note": ""
      },
      "source": "B p.44 eq (4.1)"
    }
  ],
  "pitfalls": ["真正的易错点，不是废话"],
  "related": ["kw/concept/higgs-bundle", "kw/deriv/hitchin-equations"],
  "sources": [
    {
      "text": "B",
      "section": "§4.1",
      "pages": [40, 44],
      "anchor": "B p.40–44 eq (4.1)"
    }
  ],
  "rights": "rewritten",
  "status": "draft",
  "provenance_note": "A=原文明写；B=原文暗示我们重建；C=我们的判断"
}
```

## 推导卡

```json
{
  "id": "kw/deriv/sdual-to-mirror",
  "type": "derivation",
  "title": "S-对偶在二维变成镜像对称",
  "aliases": ["S-duality = mirror symmetry", "Ψ=∞ 处的 S-对偶"],
  "track": "D",
  "summary": "不超过 120 汉字的摘要",
  "question": "这条推导要回答的问题，以问号结尾",
  "goal": "要得到的结论（一句话）",
  "setup": ["前提 1：仅考虑 Ψ=∞（t=±i）的 B-模型", "前提 2：..."],
  "steps": [
    {
      "no": 1,
      "text": "这一步做什么",
      "why": "为什么必须这样 / 依据是什么",
      "locator": "B p.70 eq (5.9)",
      "provenance": "A"
    }
  ],
  "result": "推导最终得到什么（可以带公式）",
  "gaps": ["原文只写「应该」，没有逐条验证的地方"],
  "pitfalls": ["这条推导最常见的错误"],
  "related": ["kw/concept/mirror-symmetry"],
  "sources": [
    {"text": "B", "section": "§5.4–§5.5", "pages": [70, 77], "anchor": "B p.70–77 eq (5.9)"}
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
| `id` | 是 | `kw/concept/<slug>` 或 `kw/deriv/<slug>`；slug 只含小写字母、数字、连字符 |
| `type` | 是 | `concept` 或 `derivation` |
| `title` | 是 | 中文标题，可带英文原名 |
| `aliases` | 是 | 数组，至少 1 条（英文名 / 缩写 / 别名） |
| `track` | 是 | `A` 四维物理与对偶 / `B` 扭化与拓扑 / `C` 舞台：曲线与模空间 / `D` 二维、膜与算子 / `E` Langlands 与翻译器 / `O` 总览 |
| `summary` | 是 | ≤120 汉字（去掉 `$...$` 与空白后计数） |
| `question` | 是 | 以 `？` 或 `?` 结尾 |
| `definition` / `goal`+`setup` | 是 | 概念卡用 `definition`；推导卡用 `goal` + `setup`（≥1 条） |
| `key_points` | 概念卡 | ≥3 条 |
| `formulas` | 概念卡 | ≥1 条，LaTeX 写作 `$...$` 或 `$$...$$` |
| `theorems` | 概念卡 | 可为空数组；每条的 `proof.status` ∈ `complete` / `sketch` / `gap`；`complete` 要求 ≥2 步且 `text`、`why` 非空；`sketch` / `gap` 必须有 `gap_note` |
| `steps` | 推导卡 | ≥3 步；每步 `text` / `why` / `locator` / `provenance` 都必填；`provenance` ∈ `A`/`B`/`C` |
| `result` | 推导卡 | 非空 |
| `gaps` | 推导卡 | 数组（可为空，但若任一步 provenance ≠ A，应至少 1 条） |
| `pitfalls` | 是 | ≥2 条 |
| `related` | 是 | 数组，元素是卡 id，必须能在本数据集里解析（`O` 总览卡可指向任意卡） |
| `sources` | 是 | ≥1 条；`text` ∈ `A`(Frenkel 2009) / `B`(K–W 2006) / `C`(Witten 2008) / `D`(Ben-Zvi 综述)；`pages` 是两个整数且 `2 ≤ pages[0] ≤ pages[1] ≤ 222`（A/C/D 用各自 PDF 页，凡引用 B 都用印刷页）；`anchor` 形如 `B p.38 eq (4.1)` 或 `C p.6` |
| `rights` | 是 | 固定 `rewritten`（原创改写，不复制原文长段） |
| `status` | 是 | `draft`（AI 自检未过）或 `dev`（AI 自检通过，待人类认证）；**不许写 `prod`/`train`** |
| `provenance_note` | 是 | 一句话说明本卡的 A/B/C 构成与最没把握处 |

## 写作纪律

1. **断言带 locator**：每条事实性断言都要能在 `sources` 或单步 `locator` 里找到出处。
2. **不复制原文**：英文短引 ≤120 字符；公式可以照抄（公式不是版权文本），但叙述必须自己写。
3. **不写本机路径**、不写 `C:\Users\...`。
4. **诚实标注**：原文只写 "we expect" / "should be" 的，provenance 记 `B` 或 `C`，并在 `gaps` 里写明。
5. **术语统一**：twist=扭化，eigenbrane=特征膜，Hecke eigensheaf=Hecke 特征层，
   canonical coisotropic brane=典范余各向同性（A-）膜，'t Hooft 算子不译。
