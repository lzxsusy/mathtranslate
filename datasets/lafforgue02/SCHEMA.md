# 资料卡 JSON 规范（lafforgue02 v1）

本包所有卡都是**一卡一 JSON**：UTF-8 编码、缩进 2 空格、`ensure_ascii=False`（中文与公式直接写，不转义）；文件名 = `id` 最后一段 + `.json`。两类卡共用 `id/type/title/aliases/track/summary/question/pitfalls/related/sources/rights/status/provenance_note`，其余字段按类型不同。

- id 前缀：`lafforgue02/concept/<slug>` 或 `lafforgue02/deriv/<slug>`，`slug` 只用小写字母、数字与连字符。
- 轨道（`track`）：`A` = 证明主线（对应、chtouca、截断、可忽略性、迹公式），`B` = 紧化与紧合性（fourre-tout、$\varphi$-格、退化子、稳定性），`O` = 总览。
- 来源字母（`sources[].text`）：`A` = 底本 Lafforgue, *Cours à l'Institut Tata sur les chtoucas de Drinfeld et la correspondance de Langlands*，IHES/M/02/45，**印刷页 1–56**；`B` = nLab / Stacks Project 白名单与本库译注；`C` = 原始文献（Drinfeld、Lafforgue 1997/1998/2002、Laumon，见讲义文献表）；`D` = 其他白名单或本库已交付工程。
- `pages` 一律写**印刷页**（1–56），两个整数，`1 ≤ pages[0] ≤ pages[1] ≤ 56`（A 级强制；B/C/D 级亦限制在同一区间内，外部文献请用 `anchor` 注明）。
- `anchor` 形如 `A p.12`、`A p.43`、`B nLab: Harder–Narasimhan filtration`。**本讲义无公式编号**，故 anchor 不写 `eq (...)`。

## 概念卡

```json
{
  "id": "lafforgue02/concept/drinfeld-chtouca",
  "type": "concept",
  "title": "Drinfeld chtouca（带水平结构）",
  "aliases": ["chtouca", "shtuka"],
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
      "source": "A p.6"
    }
  ],
  "pitfalls": ["……", "……"],
  "related": ["lafforgue02/concept/chtouca-moduli-stack"],
  "sources": [{"text": "A", "section": "§I", "pages": [5, 6], "anchor": "A p.6"}],
  "rights": "rewritten",
  "status": "dev",
  "provenance_note": "……"
}
```

- `summary` ≤120 汉字（去掉 `$…$` 与空白）；`question` 以问号结尾。
- `key_points` ≥3 条、`formulas` ≥1 条。
- `theorems[].proof.status`：`complete` 需 ≥2 步且每步有 `text`/`why`；`sketch` 与 `gap` 必须写 `gap_note`。
- `pitfalls` ≥2 条，写**容易读错的具体位置**，不写「很重要」。

## 推导卡

```json
{
  "id": "lafforgue02/deriv/truncation-to-compactification",
  "type": "derivation",
  "title": "……",
  "aliases": ["……"],
  "track": "A",
  "summary": "……",
  "question": "……？",
  "goal": "这条推导要证/要说明什么",
  "setup": ["前提 1", "前提 2"],
  "steps": [
    {"no": 1, "text": "这一步做什么", "why": "凭什么（原文写了什么/为什么成立）", "locator": "A p.10", "provenance": "A"}
  ],
  "result": "结论",
  "gaps": ["哪一步是我们补的、原文没写"],
  "pitfalls": ["……", "……"],
  "related": ["lafforgue02/concept/harder-narasimhan-truncation"],
  "sources": [{"text": "A", "section": "§I", "pages": [10, 11], "anchor": "A p.10"}],
  "rights": "rewritten",
  "status": "dev",
  "provenance_note": "……"
}
```

- `setup` ≥1、`steps` ≥3，每步 `locator` 与 `provenance` 必填。
- `provenance`：`A` = 讲义原话或原式；`B` = 由讲义的上下文可推出、但原文未写出；`C` = 我们据标准结果补的（此时 `gaps` 必须 ≥1 条并点名）。
- `gaps` 只列**真实的**缺口（原文只给思路、引用了别处、或我们补了话），不写「需要更多细节」这类空话。

## 写作纪律（四不）

1. **不写课本**：每张卡只回答它自己那个问题，不把整章内容搬进来。
2. **不抄原文**：公式可照录；命题陈述用自己的话重写；法文原文短引 ≤120 字符。
3. **不编页码与编号**：本讲义无编号定理、无编号公式，任何 `A p.n` 都必须与译本 `\origpage{n}` 锚一致。
4. **不写本机路径**：卡里只出现仓库内相对路径或讲义页码。

## 校验

```bash
python tools/lint_cards.py      # 0 error 才算通过
python tools/build_index.py     # 重建 index.jsonl
python tools/render_md.py       # 重建 md/
```
