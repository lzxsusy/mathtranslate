# 资料卡体例（sy38）

底本：Johannes Anschütz, *Lecture notes for an introductory course on the Langlands program*
（含 Ben Heuer 的三讲），2020-07-22 修订稿，103 页。
卡片 id 前缀 **sy38**；页码一律 **PDF 页序**（= 印刷页，偏移 0，范围 1–103）。
`SOURCE.md` 的 `text` 记号统一为 **A**（对应 `sources[].text = "A"`、`anchor = "A p.NN"`）。

本工程与 `08_source_code/SY02-38_朗兰兹纲领入门课程讲义/资料卡/` 是同一套卡片的两份副本（交付时同步）。

---

## 1. 文件与命名

```
cards/concepts/<slug>.json      id: sy38/concept/<slug>
cards/derivations/<slug>.json   id: sy38/deriv/<slug>
```
slug 用小写字母、数字、连字符（`eichler-shimura-isomorphism`）。文件名必须等于 slug。

## 2. 轨道（track）

| 轨道 | 范围 | 典型卡 |
|---|---|---|
| A | 阿代尔、L²(G(Q)\G(A))、约化群、玉河数、自守表示、谱分解（讲 2） | `automorphic-representation`、`tamagawa-number` |
| B | 模形式、线丛 ω^{⊗k}、(g,K)-模判据、Hecke 代数与特征系统、新形式（讲 3–5） | `modular-form-weight-k`、`newform-conductor` |
| C | ℓ-进 Galois 表示、Frobenius 迹、Langlands 互反、de Rham/Hodge–Tate（讲 6、9–10） | `langlands-reciprocity-conjecture`、`de-rham-representation` |
| D | 模曲线、模空间、Eichler–Shimura 关系与同构（讲 7–9） | `modular-curve`、`eichler-shimura-relation` |
| E | 一般约化群、Satake 参数、L-群与 L-参数、Langlands 群、Shimura 簇（讲 11–12） | `satake-parameter`、`l-group` |
| O | 记号、元理论、跨篇对照、术语与勘误 | `notation-index` |

## 3. 概念卡字段

```json
{
  "id": "sy38/concept/<slug>",
  "type": "concept",
  "track": "A",
  "title": "中文标题（可用 $\\LaTeX$）",
  "aliases": ["英文名", "$\\LaTeX$ 记号", "中文别译"],
  "summary": "≤120 汉字的定义性概括（去公式计字数）",
  "question": "这张卡要回答的问题？",
  "definition": {"text": "中文定义（重写，不贴译文段）",
                 "notation": "$X_{\\Gamma_1(N)}$"},
  "key_points": ["≥3 条，每条讲清为什么重要/常见误读"],
  "formulas": ["1–5 条关键公式"],
  "theorems": [
    {"name": "定理 9.1", "statement": "中文陈述",
     "proof": {"status": "sketch|complete|gap",
               "steps": [{"no": 1, "text": "…", "why": "…"}],
               "gap_note": "status≠complete 时必填：缺口在哪"},
     "source": "A p.74"}
  ],
  "pitfalls": ["≥2 条：与哪个概念易混/常见错误"],
  "related": ["sy38/concept/<slug>"],
  "sources": [
    {"text": "A", "book": "Anschütz 2020", "section": "§9",
     "pages": [73, 74], "anchor": "A p.74",
     "quote": "12–120 字符的英文原句，逐字，不得含中文"}
  ],
  "rights": "rewritten",
  "status": "draft",
  "provenance_note": "哪些内容是重构的、依据是什么"
}
```

## 4. 推导卡字段

```json
{
  "id": "sy38/deriv/<slug>",
  "type": "derivation", "track": "D",
  "title": "……",
  "aliases": ["…"],
  "summary": "≤120 汉字", "question": "……？",
  "goal": "本推导要解决的问题",
  "setup": ["前提 1", "前提 2"],
  "steps": [
    {"no": 1, "text": "本步做什么", "why": "为什么这么做",
     "locator": "A p.74", "provenance": "A"}
  ],
  "result": "结论一句话",
  "pitfalls": ["≥2 条"],
  "related": ["sy38/concept/<slug>"],
  "sources": [{"text": "A", "book": "Anschütz 2020", "section": "§9",
               "pages": [73, 74], "anchor": "A p.74",
               "quote": "英文原句 12–120 字符"}],
  "rights": "rewritten", "status": "draft",
  "provenance_note": "……"
}
```

## 5. 硬规则

1. **quote 逐字英文**：从 `工程文件/work/pages/pNNN.txt` 抄，12–120 字符，不得含中文、不得改写、不得拼接。
2. **pages 两整数**且 1 ≤ 起 ≤ 止 ≤ 103；`anchor` 形如 `A p.74`。
3. `summary` ≤120 汉字（公式不计），`question` 以问号结尾，`pitfalls` ≥2，`related` ≥1 且指向本包已存在的卡。
4. `rights` 一律 `rewritten`；卡内不得出现本机绝对路径。
5. 定义/定理**用自己的话重写**，不整段贴译文；证明只给 `status=sketch` 的骨架或 `gap`（本书大量结论「不给证明」，此时 `gap` + `gap_note` 说明「原文未证，引自 [GH19] 等」）。
6. 每张卡的 `source` 精确到命题/定理编号与页；编号按原书（如 `定理 9.1`、`命题 8.4`、`定义 11.1`）。

## 6. 质检

```bash
python datasets/sy0238/tools/lint_cards.py datasets/sy0238/cards --prefix sy38 --max-pages 103
python datasets/sy0238/tools/verify_quotes.py ...
```
包级检查还需 `notes.md` 的「核对与勘误」节与 `errata.tsv`（9 列：序/位置/原写法/订正/依据1/依据2/置信度/影响卡片/状态）。
