# 资料卡 JSON 规范（sandvik25 v1）

本包所有卡都是**一卡一 JSON**：UTF-8 编码、缩进 2 空格、`ensure_ascii=False`（中文与公式直接写，不转义）；文件名 = `id` 最后一段 + `.json`。两类卡共用 `id/type/title/aliases/track/summary/question/pitfalls/related/sources/rights/status/provenance_note`，其余字段按类型不同。

- id 前缀：`sandvik25/concept/<slug>` 或 `sandvik25/deriv/<slug>`，`slug` 只用小写字母、数字与连字符。
- 轨道（`track`）：`O` = 总览（三条路线与主定理结论），`A` = 中心层与 Wakimoto 层（§2），`B` = Springer 侧与三造函子（§3），`C` = Iwahori–Whittaker 侧（§2.6、§4），`D` = 主等价（§5）。
- 来源字母（`sources[].text`）：`A` = 底本 Sandvik, *The Arkhipov–Bezrukavnikov Equivalence*, BunG Seminar 2025-01-29，**印刷页 1–13**；`B` = nLab / Stacks Project 白名单与本库译注；`C` = 原始文献（[ArBe] 2009、[AcRi]、[BNP] 2017、[Gai1] 2001、[Gai2] 2020）；`D` = 其他白名单或本库已交付工程。
- `pages` 一律写**印刷页**（1–13），两个整数，`1 ≤ pages[0] ≤ pages[1] ≤ 13`。
- `anchor` 形如 `A p.5`、`A p.12`。底本有 8 条编号公式 (1)–(8)，需要时可写 `A p.5 eq (6)`；但 `anchor` 字段本身只验收 `^(A|B|C|D) (p\.\d+|nLab: .+)$`，公式编号请写在 `provenance_note` 或 `theorems[].statement` 里。

## 概念卡

```json
{
  "id": "sandvik25/concept/central-affine-grassmannian",
  "type": "concept",
  "title": "中心仿射 Grassmann 簇 $\\mathrm{Gr}^{\\mathrm{cen}}_G$",
  "aliases": ["central affine Grassmannian"],
  "track": "A",
  "summary": "……≤120 汉字（去公式与空白）",
  "question": "……？",
  "definition": {"text": "……", "notation": "……"},
  "key_points": ["……", "……", "……"],
  "formulas": ["……"],
  "theorems": [
    {
      "name": "……",
      "statement": "……",
      "proof": {"status": "sketch|complete|gap", "steps": [{"no": 1, "text": "……", "why": "……"}], "gap_note": "……"},
      "source": "A p.3"
    }
  ],
  "pitfalls": ["……", "……"],
  "related": ["sandvik25/concept/nearby-cycles"],
  "sources": [{"text": "A", "section": "§2.4", "pages": [3, 3], "anchor": "A p.3"}],
  "rights": "rewritten",
  "status": "dev",
  "provenance_note": "……"
}
```

- `summary` ≤120 汉字（去掉 `$…$` 与空白）；`question` 以问号结尾。
- `key_points` ≥3 条、`formulas` ≥1 条。
- `theorems[].proof.status`：`complete` 需 ≥2 步且每步有 `text`/`why`；`sketch` 与 `gap` 必须写 `gap_note`。
- `theorems` 可为空数组（纯定义性的卡，如 `central-affine-grassmannian`、`functor-f2`）。
- `pitfalls` ≥2 条，写**容易读错的具体位置**，不写「很重要」。

## 推导卡

```json
{
  "id": "sandvik25/deriv/fully-faithful-hom",
  "type": "derivation",
  "title": "主定理的全忠实：$\\mathrm{Hom}$ 两边的显式计算",
  "track": "D",
  "summary": "……≤120 汉字",
  "question": "……？",
  "goal": "这条推导要证什么（一句话）",
  "setup": ["已知前提 1", "已知前提 2"],
  "steps": [
    {"no": 1, "text": "……", "why": "……", "locator": "A p.12", "provenance": "A"}
  ],
  "result": "结论一句话",
  "gaps": ["原文省略的步 / 我们没补的步"],
  "pitfalls": ["……", "……"],
  "related": ["sandvik25/concept/functor-fiw"],
  "sources": [{"text": "A", "section": "§5", "pages": [12, 12], "anchor": "A p.12"}],
  "rights": "rewritten",
  "status": "dev",
  "provenance_note": "……"
}
```

- `setup` ≥1 条；`steps` ≥3 步，每步 `text/why/locator/provenance` 齐全；`provenance ∈ {A,B,C}`：`A` = 原文写了，`B` = 原文暗示、我们补的中间步，`C` = 我们的判断。
- 任意一步非 `A` 时，`gaps` 至少一条，点名「哪一步是补的、凭什么这样补」。

## 两条通用纪律

- **不写本机路径、不写猜测页**：页码必须对回 PDF 页核过；原文笔误（如 p.3 把特殊纤维也印成 $\mathrm{Gr}^{\mathrm{cen},\times}_G$）在 `pitfalls` 里明确标注「原文笔误」，不改原文措辞。
- **`why` 写「为什么这一步成立」，不写「这一步在做什么」**：前者是卡的价值所在，后者看 `text` 就够了。
