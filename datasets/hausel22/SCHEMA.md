# 资料卡 JSON 规范（hausel22 v1）

本包所有卡都是**一卡一 JSON**：UTF-8 编码、缩进 2 空格、`ensure_ascii=False`（中文与公式直接写，不转义）；文件名 = `id` 最后一段 + `.json`。两类卡共用 `id/type/title/aliases/track/summary/question/pitfalls/related/sources/rights/status/provenance_note`，其余字段按类型不同。

- id 前缀：`hausel22/concept/<slug>` 或 `hausel22/deriv/<slug>`，`slug` 只用小写字母、数字与连字符。
- 六条轨道（`track`）：`A` 镜像对称与几何 Langlands、`B` 拓扑镜像对称与 Hodge 数、`C` 增强镜像对称与膜、`D` 幂零锥上的等变重数、`E` 仿射 Grassmannian 与重数代数、`O` 总览。
- 来源字母（`sources[].text`）：`A` = 底本 Hausel, *Enhanced mirror symmetry for Langlands dual Hitchin systems*，Proc. ICM 2022 Vol. 3，印刷页 2228–2249；`B` = nLab（`07_refs_nlab/` 白名单缓存）；`C` = 原始文献（Hitchin 1987、Hausel–Thaddeus 2003、Kapustin–Witten 2007、Donagi–Pantev、Hausel–Hitchin、Groechenig–Wyss–Ziegler 等，见原文文献表）；`D` = 其他白名单（Stacks Project、EMS）或本库译注。
- `pages` 一律写**印刷页**（2228–2249），两个整数，`2228 ≤ pages[0] ≤ pages[1] ≤ 2249`（A 级强制；B/C/D 级放宽到 1–2249，用于外部文献页码）。
- `anchor` 形如 `A p.2237`、`A p.2243 eq (3.12)`、`B nLab: Hitchin fibration`。

## 概念卡

```json
{
  "id": "hausel22/concept/very-stable-higgs-bundle",
  "type": "concept",
  "title": "非常稳定 Higgs 丛",
  "aliases": ["very stable Higgs bundle", "非常稳定"],
  "track": "D",
  "summary": "上行流只与芯交于自身（等价于上行流闭）的 $\\C^\\times$-不动点 Higgs 丛。",
  "question": "为什么「非常稳定」这个看似技术性的条件能保证重数是多项式？",
  "definition": {"text": "……", "notation": "……"},
  "key_points": ["……", "……", "……"],
  "formulas": ["$$……$$"],
  "theorems": [
    {
      "name": "定理 3.2",
      "statement": "……",
      "proof": {"status": "sketch", "steps": [{"no": 1, "text": "……", "why": "……"}], "gap_note": "……"},
      "source": "A p.2237"
    }
  ],
  "pitfalls": ["……", "……"],
  "related": ["hausel22/concept/bialynicki-birula-attraction", "hausel22/concept/equivariant-multiplicity"],
  "sources": [{"text": "A", "section": "§3.1", "pages": [2237, 2237], "anchor": "A p.2237"}],
  "rights": "rewritten",
  "status": "dev",
  "provenance_note": "A=……；B=……；C=……。最没把握处：……"
}
```

## 推导卡

```json
{
  "id": "hausel22/deriv/very-stable-chain",
  "type": "derivation",
  "title": "非常稳定的四重等价链",
  "aliases": ["very stable equivalences"],
  "track": "D",
  "summary": "……",
  "question": "……",
  "goal": "……",
  "setup": ["……", "……"],
  "steps": [
    {
      "no": 1,
      "text": "……",
      "why": "……",
      "locator": "A p.2238",
      "provenance": "A"
    }
  ],
  "result": "……",
  "gaps": ["……"],
  "pitfalls": ["……", "……"],
  "related": ["hausel22/concept/very-stable-higgs-bundle"],
  "sources": [{"text": "A", "section": "§3.1", "pages": [2237, 2238], "anchor": "A p.2238"}],
  "rights": "rewritten",
  "status": "dev",
  "provenance_note": "A=……；B=……；C=……。最没把握处：……"
}
```

## 字段规则

| 字段 | 必填 | 规则 |
| --- | --- | --- |
| `id` | 是 | `hausel22/concept/<slug>` 或 `hausel22/deriv/<slug>`；与目录一致；`slug` = 文件名 |
| `type` | 是 | `concept` / `derivation` |
| `title` | 是 | 中文为主，可带英文；公式用 `$...$` |
| `aliases` | 是 | 数组，≥1；英文名与原术语 |
| `track` | 是 | `A/B/C/D/E/O` 之一 |
| `summary` | 是 | ≤120 汉字（去掉 `$...$` 与空白后的字符数）；一句话说清是什么 |
| `question` | 是 | 以 `？` 或 `?` 结尾；概念卡是"先自测"的问题 |
| `definition` / `goal` | 概念卡 / 推导卡 | 概念卡 `definition.text` 必填，`notation` 写记号；推导卡 `goal` 写结论目标 |
| `key_points` / `setup` | 概念卡 / 推导卡 | 概念卡 ≥3 条；推导卡 ≥1 条前提 |
| `formulas` | 概念卡是 | ≥1 条，`$$...$$` 包裹 |
| `theorems` | 概念卡是 | 每条有 `name/statement/proof{status}/source`；`complete` 需 ≥2 步且每步 `text/why`；`sketch`/`gap` 必须有 `gap_note` |
| `steps` | 推导卡是 | ≥3 步；每步 `text/why/locator/provenance` 齐全；`locator` 形如 `A p.2238 eq (3.4)`、`provenance ∈ {A,B,C}` |
| `result` | 推导卡是 | 一行结论 |
| `gaps` | 推导卡（任意一步非 A 时 ≥1） | 诚实列出缺的证明步骤 |
| `pitfalls` | 是 | ≥2 条；写"最容易讲错"的地方 |
| `related` | 是 | ≥1；**必须指向本包真实存在的 id** |
| `sources` | 是 | ≥1；每条 `text/section/pages/anchor`；`anchor` 形如 `A p.2238 eq (3.4)`；`pages` 用印刷页 |
| `rights` | 是 | 固定 `"rewritten"` |
| `status` | 是 | `"draft"` / `"dev"`；本包全用 `dev`，不许写 `prod`/`train` |
| `provenance_note` | 是 | 一句话说明 A/B/C 各占哪些内容，并点名**最没把握处** |

## 写作纪律

1. **断言必须带 locator**：`sources[].section` 写原文章节，`pages` 写印刷页，`anchor` 写成可查形式（`A p.2243 eq (3.12)` 这类）；不许编页码或编号。
2. **不抄原文**：中文用自己的话重写（`rights: "rewritten"`）；英文短引 ≤120 字符；公式可以照录。
3. **不写本机路径**：卡里不出现 `C:\\`、`/Users/`、`file://` 等（lint 会拦）。
4. **诚实标注**：原文只暗示的标 `B`，我们自己的判断标 `C`，并在推导卡的 `gaps` 与概念卡 `theorems.proof.gap_note` 写清楚。
5. **编号两套不混**：定理用印本编号 `3.1–3.20`、公式用 `(1.1)(2.1)–(2.5)(3.1)–(3.14)`；本包自己的卡编号（如 id 序号）不写进正文。
6. **术语统一**：超 Kähler、Higgs 丛、Hitchin 映射、非常稳定、重数代数、等变重数、幂零锥、上行流/下行流、芯、仿射 Grassmannian、jet 概形、拉格朗日闭包，与译本 `源码/` 一致。
