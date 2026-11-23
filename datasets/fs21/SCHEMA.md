# 资料卡体例（fs21）

底本：《局部 Langlands 对应的几何化》arXiv:2102.13459v4，356 页。
卡片 id 前缀 **fs21**；页码一律 **PDF 页序**（= 印刷页）。

---

## 1. 文件与命名

```
资料卡/cards/concepts/<slug>.json      id: fs21/concept/<slug>
资料卡/cards/derivations/<slug>.json   id: fs21/deriv/<slug>
```
slug 用小写字母、数字、连字符（`fargues-fontaine-curve`）。文件名必须等于 slug。

## 2. 轨道（track）

| 轨道 | 范围 | 典型卡 |
|---|---|---|
| A | Fargues–Fontaine 曲线、向量丛、p-进 Hodge 理论 | `fargues-fontaine-curve`、`isocrystal`、`banach-colmez-space` |
| B | Bun_G、shtuka、模空间与几何 | `bun-g-stack`、`local-shtuka`、`harder-narasimhan` |
| C | diamond、v-层、六函子形式、同调代数 | `diamond`、`v-sheaf`、`ula-sheaf`、`six-functors` |
| D | 几何 Satake、Hecke 与表示论 | `geometric-satake`、`spherical-hecke`、`affine-flag-variety` |
| E | L-参数、谱作用、局部 Langlands 对应 | `l-parameter`、`spectral-action`、`bernstein-center` |
| O | 记号、元理论、跨篇对照 | `notation-index` |

## 3. 概念卡字段

```json
{
  "id": "fs21/concept/fargues-fontaine-curve",
  "type": "concept",
  "track": "A",
  "title": "Fargues–Fontaine 曲线",
  "aliases": ["FF 曲线", "the Fargues–Fontaine curve"],
  "summary": "≤120 汉字的定义性概括（去掉公式计字数）",
  "question": "它为什么能替代 Spec E 上的 '空间'？",
  "definition": {"text": "中文定义（用自己的话重写，不要贴原文译文段）",
                 "notation": "$X_{FF}$；$X_{FF}=\mathrm{Spa}(E,\oo_E)/\varphi^{\mathbb{Z}}$"},
  "key_points": ["≥3 条，每条一句话，讲清为什么重要/常见误读"],
  "formulas": ["$\\Bun_G$ …（关键公式，最多 5 条）"],
  "theorems": [
    {"name": "定理 I.3.2", "statement": "中文陈述",
     "proof": {"status": "sketch|complete|gap",
               "steps": [{"no": 1, "text": "…", "why": "…"}],
               "gap_note": "status≠complete 时必填：缺口在哪"},
     "source": "A p.19 §I.3"}
  ],
  "pitfalls": ["≥2 条：与哪个概念易混/常见错误"],
  "related": ["fs21/concept/adic-space"],
  "sources": [
    {"text": "A", "book": "Fargues–Scholze 2024", "section": "§I.3",
     "pages": [19, 21], "anchor": "A p.19 §I.3",
     "quote": "12–120 字符的英文原句，逐字"}
  ],
  "rights": "rewritten",
  "status": "draft",
  "provenance_note": "哪些内容是我们重构的、依据是什么"
}
```

## 4. 推导卡字段

```json
{
  "id": "fs21/deriv/curve-classification",
  "type": "derivation", "track": "A",
  "title": "曲线的分类定理怎么证的",
  "aliases": ["classification of vector bundles"],
  "summary": "…", "question": "…",
  "goal": "把 … 归约到 …",
  "setup": ["前提 1", "前提 2"],
  "steps": [
    {"no": 1, "text": "本步做什么", "why": "为什么这么做（动机/依据）",
     "locator": "A p.19 §I.3", "provenance": "A"}
  ],
  "result": "结论一句话",
  "pitfalls": ["≥2 条"], "related": ["fs21/concept/fargues-fontaine-curve"],
  "sources": [{"text": "A", "pages": [19, 30], "anchor": "A p.19 §I.3", "quote": "…"}],
  "rights": "rewritten", "status": "draft", "provenance_note": "…"
}
```

## 5. 硬规则

1. **sources.text**：`A`=本篇底本；`B`=本库既有卡片/已译篇（写工程号）；`C`=外部文献（nLab/Stacks/原始论文）；`D`=沿引。
2. **A 类必须带 quote**：12–120 字符、逐字英文原句、不得含中文。写不出 quote 的出处等于没出处。
3. **pages** 两整数、`1 ≤ p1 ≤ p2 ≤ 356`；`anchor` 形如 `A p.19 §I.3` 或 `A p.20 eq(I.3.4)`。
4. `rights` 固定 `"rewritten"`（中文重写；公式照录；英文短引 ≤120 字符；不收录原文段落）。
5. `status` 只用 `"draft"` / `"dev"`。
6. `summary` ≤120 汉字（公式不计）；`question` 以问号结尾；`pitfalls` ≥2；`related` ≥1 且指向真实卡。
7. 每个推导步必须四字段齐全：`text` / `why` / `locator` / `provenance`（A 原文明写，B 我们重建，C 判断）。
8. 不得出现本机绝对路径。

## 6. 质检

```bat
python 资料卡\tools\lint_cards.py 资料卡\cards --prefix fs21 --max-pages 356 --no-pkg --strict
python 资料卡\tools\verify_quotes.py 资料卡\cards --strict
```
两条都必须 `错误 0` / `问题 0`、exit 0。逐条修到通过再交付。

- `lint_cards.py` 管结构与字段（id、轨道、question、pitfalls、steps、related、禁本机路径）。
- `verify_quotes.py` 管**引文真实性**：把每条 `sources[].quote` 归一化后在 `01_pages/pNNN.txt`
  里逐字搜，报「页码不符（卡片写 p.X，实际 p.Y）」「全局搜不到」「长度不在 12–120」「含中文」。
  本工程原文页 = PDF 页，所以直接按 `pages` 范围取文。（ggl 那套按 `txt/<NN>/` 组织的
  `verify_pages.py` 在本工程不适用，已换成这一支。）

## 7. 配额（Lead 在任务书里给具体数）

- 一章 8–12 张概念卡 + 2–4 张推导卡；
- 356 页全书记划约 120 张卡（Lead 汇总时校准）。
