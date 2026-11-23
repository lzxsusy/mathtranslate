# 资料卡体例（sy29）

底本：Laurent Fargues, *Geometrization of the local Langlands correspondence: an overview*,
2016-02-02，46 页。
卡片 id 前缀 **sy29**；页码一律 **PDF 页序**（= 印刷页，偏移 0，范围 1–46）。

本工程与 `datasets/sy02-29/` 是同一套卡片的两份副本（交付时同步）。

---

## 1. 文件与命名

```
资料卡/cards/concepts/<slug>.json      id: sy29/concept/<slug>
资料卡/cards/derivations/<slug>.json   id: sy29/deriv/<slug>
```
slug 用小写字母、数字、连字符（`fargues-fontaine-curve`）。文件名必须等于 slug。

## 2. 轨道（track）

| 轨道 | 范围 | 典型卡 |
|---|---|---|
| A | 曲线 $X_S$、$Y_S$、untilt、$B^+_{\mathrm{dR}}$、Cartier 除子、本原元 | `fargues-fontaine-curve`、`untilts-and-primitive-elements` |
| B | $\Bun_G$、$B(G)$、HN 分层、$J_b$ 与基本点单值化 | `bun-g-stack`、`kottwitz-set` |
| C | 完满、菱形、倾斜、Banach–Colmez 空间、$F$-等晶体 | `diamond`、`perfectoid-space` |
| D | $\BdR$-仿射 Grassmann 簇、Hecke 叠、Beauville–Laszlo、几何 Satake | `hecke-stack`、`bdR-affine-grassmannian` |
| E | Langlands 参数、$S_\varphi$、$L$-包、特征层性、Kottwitz 猜想 | `langlands-parameter`、`character-sheaf-property` |
| O | 记号、元理论、跨篇对照 | `notation-index` |

## 3. 概念卡字段

```json
{
  "id": "sy29/concept/fargues-fontaine-curve",
  "type": "concept",
  "track": "A",
  "title": "Fargues–Fontaine 曲线",
  "aliases": ["FF 曲线", "the curve"],
  "summary": "≤120 汉字的定义性概括（去掉公式计字数）",
  "question": "它为什么能替代 Spec E 上的空间？",
  "definition": {"text": "中文定义（用自己的话重写，不要贴原文译文段）",
                 "notation": "$X_S=Y_S/\\varphi^{\\mathbb Z}$"},
  "key_points": ["≥3 条，每条一句话，讲清为什么重要/常见误读"],
  "formulas": ["最多 5 条关键公式"],
  "theorems": [
    {"name": "定理 1.29", "statement": "中文陈述",
     "proof": {"status": "sketch|complete|gap",
               "steps": [{"no": 1, "text": "…", "why": "…"}],
               "gap_note": "status≠complete 时必填：缺口在哪"},
     "source": "A p.14"}
  ],
  "pitfalls": ["≥2 条：与哪个概念易混/常见错误"],
  "related": ["sy29/concept/adic-space"],
  "sources": [
    {"text": "A", "book": "Fargues 2016", "section": "§1.1",
     "pages": [3, 4], "anchor": "A p.3 §1.1",
     "quote": "12–120 字符的英文原句，逐字，不得含中文"}
  ],
  "rights": "rewritten",
  "status": "draft",
  "provenance_note": "哪些内容是我们重构的、依据是什么"
}
```

## 4. 推导卡字段

```json
{
  "id": "sy29/deriv/untilt-to-cartier-divisor",
  "type": "derivation", "track": "A",
  "title": "untilt 怎么变成曲线上的 Cartier 除子",
  "aliases": ["untilts as Cartier divisors"],
  "summary": "…", "question": "…",
  "goal": "把 untilt 这一 Hodge 理论对象翻成曲线上的除子",
  "setup": ["前提 1", "前提 2"],
  "steps": [
    {"no": 1, "text": "本步做什么", "why": "为什么这么做（动机/依据）",
     "locator": "A p.8 §1.4", "provenance": "A"}
  ],
  "result": "结论一句话",
  "pitfalls": ["≥2 条"],
  "related": ["sy29/concept/untilts-and-primitive-elements"],
  "sources": [{"text": "A", "pages": [8, 9], "anchor": "A p.8 命题 1.22", "quote": "…"}],
  "rights": "rewritten", "status": "draft", "provenance_note": "…"
}
```

## 5. 硬规则

1. **sources.text**：`A`=本篇底本；`B`=本库既有卡片/已译篇（写工程号）；`C`=外部文献（nLab/Stacks/原始论文）；`D`=沿引。
2. **A 类必须带 quote**：12–120 字符、逐字英文原句、不得含中文、必须真在所写 pages 范围内。
3. **pages** 两整数、`1 ≤ p1 ≤ p2 ≤ 46`；`anchor` 形如 `A p.14 §1.5.4` 或 `A p.15 命题 1.33`。
4. `rights` 固定 `"rewritten"`（中文重写；公式照录；英文短引 ≤120 字符；不收录原文段落）。
5. `status` 只用 `"draft"` / `"dev"`。
6. `summary` ≤120 汉字（公式不计）；`question` 以问号结尾；`pitfalls` ≥2；`related` ≥1 且指向真实卡。
7. 每个推导步四字段齐全：`text` / `why` / `locator` / `provenance`。
8. 不得出现本机绝对路径。

## 6. 质检

```bat
python 资料卡\tools\lint_cards.py 资料卡\cards --prefix sy29 --max-pages 46 --strict
python 资料卡\tools\verify_quotes.py 资料卡\cards --root . --strict
```
两条都必须 `错误 0` / `问题 0`、exit 0。

- `lint_cards.py` 管结构（id、轨道、question、pitfalls、steps、related、禁本机路径）。
- `verify_quotes.py` 管引文真实性：把 `sources[].quote` 归一化后在 `工程文件/work/src/pNNN.txt`
  里逐字搜，报页码不符、全局搜不到、长度越界、含中文。

## 7. 配额

- 全书 46 页，计划 **36 张概念卡 + 8 张推导卡**。
- 按轨分配：A 10、B 7、C 7、D 7、E 7（含 O 1）。

## 8. 与译文的互链

卡片 `related` 只指向本工程卡片；译文中的术语第一次出现处由译注给出简短定义，
详尽内容留给资料卡，两者不重复堆砌。
