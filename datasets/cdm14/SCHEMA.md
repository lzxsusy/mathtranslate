# 资料卡 JSON 规范（cdm14 v1）

本包所有卡都是**一卡一 JSON**：UTF-8 编码、缩进 2 空格、`ensure_ascii=False`（中文与公式直接写，不转义）；文件名 = `id` 最后一段 + `.json`。两类卡共用 `id/type/title/aliases/track/summary/question/pitfalls/related/sources/rights/status/provenance_note`，其余字段按类型不同。

- id 前缀：`cdm14/concept/<slug>` 或 `cdm14/deriv/<slug>`，`slug` 只用小写字母、数字与连字符。
- 八条轨道（`track`）：`A` de Rham 预栈与晶体定义（§1）、`B` 左/右晶体与 IndCoh/Kashiwara（§2）、`C` 下降与归纳函子（§3）、`D` t-结构（§4）、`E` 与 D-模的关系（§5）、`F` 扭化（§6）、`G` 扭晶体（§7）、`O` 总览。
- 来源字母（`sources[].text`）：`A` = 底本 arXiv:1111.2087v4（印刷页 1–65，**印刷页 = PDF 页**）；`B` = 作者其他论文（[GR1] DG indschemes、[IndCoh] Ind-coherent sheaves、[Lu2] Higher Algebra）；`C` = 经典原始文献（[Gr] Grothendieck、[BB] Beilinson–Bernstein、[Si] Simpson）；`D` = nLab / Stacks Project 等白名单。
- `pages` 一律写**印刷页**，两个整数，`1 ≤ pages[0] ≤ pages[1] ≤ 65`。
- `anchor` 形如 `A p.12`、`A p.26–27`、`A p.47 eq (5.2)`；必须能被 lint 的正则匹配。

## 概念卡

```json
{
  "id": "cdm14/concept/left-crystal",
  "type": "concept",
  "title": "左晶体：$\\Crys^l(Y)=\\QCoh(Y_{\\mathrm{dR}})$",
  "aliases": ["left crystal", "Crys^l", "左晶体"],
  "track": "B",
  "summary": "……（≤120 字，去掉公式与空白后计）",
  "question": "……？",
  "definition": {"text": "……", "notation": "……"},
  "key_points": ["……", "……", "……"],
  "formulas": ["$$……$$"],
  "theorems": [
    {
      "name": "定理名",
      "statement": "……",
      "proof": {"status": "sketch", "steps": [{"no": 1, "text": "……", "why": "……"}], "gap_note": "……"},
      "source": "A p.17"
    }
  ],
  "pitfalls": ["……", "……"],
  "related": ["cdm14/concept/right-crystal", "cdm14/concept/upsilon-comparison"],
  "sources": [{"text": "A", "section": "§2.1", "pages": [15, 17], "anchor": "A p.15"}],
  "rights": "rewritten",
  "status": "dev",
  "provenance_note": "A=……；B=……。最没把握处：……"
}
```

## 推导卡

```json
{
  "id": "cdm14/deriv/upsilon-equiv",
  "type": "derivation",
  "title": "命题 2.4.4 的证明：逐层 $\\Upsilon$ 拼成全化上的等价",
  "aliases": ["Upsilon equivalence proof"],
  "track": "B",
  "summary": "……",
  "question": "……？",
  "goal": "……",
  "setup": ["……", "……"],
  "steps": [
    {"no": 1, "text": "……", "why": "……", "locator": "A p.22", "provenance": "A"}
  ],
  "result": "……",
  "gaps": ["……"],
  "pitfalls": ["……", "……"],
  "related": ["cdm14/concept/upsilon-comparison"],
  "sources": [{"text": "A", "section": "§2.4", "pages": [22, 22], "anchor": "A p.22"}],
  "rights": "rewritten",
  "status": "dev",
  "provenance_note": "A=命题 2.4.4 的证明；B=[GR1]。最没把握处：……"
}
```

## 硬规则（lint 会查）

- `summary` 去掉 `$...$` 与空白后 ≤120 字符；`question` 以 `？` 结尾。
- `pitfalls` ≥2；`related` ≥1 且必须指向包内真实 id；`sources` 非空、`anchor` 匹配正则。
- 概念卡：`definition.text` 非空、`key_points` ≥3、`formulas` ≥1（`$$...$$`）；每个 `theorem.proof.status ∈ {complete, sketch, gap}`，`complete` 需 ≥2 步且每步有 `text/why`，`sketch`/`gap` 必须有 `gap_note`。
- 推导卡：`goal` 非空、`setup` ≥1、`steps` ≥3 且每步 `text/why/locator/provenance` 齐全、`provenance ∈ {A,B,C}`；任一步非 `A` 时 `gaps` ≥1。
- `rights` 一律 `"rewritten"`；`status` 一律 `"dev"`（人工逐张认证后才升 `draft`）。
- 卡内禁止本机绝对路径与私有链接。
