# 资料卡 JSON 规范（yao17 v1）

本包所有卡都是**一卡一 JSON**：UTF-8 编码、缩进 1 空格、`ensure_ascii=False`（中文与公式直接写，不转义）；文件名 = `id` 最后一段 + `.json`。两类卡共用 `id/type/title/aliases/track/summary/question/pitfalls/related/sources/rights/status/provenance_note`，其余字段按类型不同。

- id 前缀：`yao17/concept/<slug>` 或 `yao17/deriv/<slug>`，`slug` 只用小写字母、数字与连字符。
- 轨道（`track`）：`O` = 总览与主陈述（LLC 定理与更精细性质），`A` = Weil–Deligne 侧（§1），`B` = 自守侧（§2.1–§2.2），`C` = 分类与不变量（§2.3、§3），`D` = 惯性 Langlands 与类型（§4）。
- 来源字母（`sources[].text`）：`A` = 底本 Zijian Yao, *Notes on Local Langlands for GLn*（哈佛 2017 秋），**印刷页 1–36**；`B` = nLab / Stacks Project / ProofWiki 白名单与本库译注；`C` = 原始文献（Bernstein–Zelevinsky、Zelevinsky、Henniart、Bushnell–Kutzko、Paskunas 等）；`D` = 其他白名单或本库已交付工程（如 SY02-38、SY02-41）。
- `pages` 一律写**印刷页**（1–36），两个整数，`1 ≤ pages[0] ≤ pages[1] ≤ 36`。
- `anchor` 形如 `A p.5`、`A p.12`、`A p.8–9`。底本编号是「节.小节.条」三层（1.1.1、2.2.3 等），**不要**把编号塞进 `anchor`；写进 `sources[].section` 或 `provenance_note`。

## 概念卡

```json
{
  "id": "yao17/concept/bz-classification",
  "type": "concept",
  "title": "……",
  "aliases": ["……"],
  "track": "C",
  "summary": "……≤120 汉字（去公式与空白）",
  "question": "……？",
  "definition": {"text": "……", "notation": "……"},
  "key_points": ["……", "……", "……"],
  "formulas": ["……"],
  "theorems": [
    {
      "name": "……",
      "statement": "……",
      "proof": {"status": "complete|sketch|cited|none", "steps": [{"no": 1, "text": "……", "why": "……"}], "gap_note": "……"},
      "source": "A p.23"
    }
  ],
  "pitfalls": ["……", "……"],
  "related": ["yao17/concept/zelevinsky-segment"],
  "sources": [{"text": "A", "section": "§3.1.1", "pages": [23, 24], "anchor": "A p.23"}],
  "rights": "rewritten",
  "status": "dev",
  "provenance_note": "……"
}
```

- `summary` ≤120 汉字（去掉 `$…$` 与空白）；`question` 以问号结尾。
- `key_points` ≥3 条、`formulas` ≥1 条。
- `theorems[].proof.status` 四选一：`complete` 需 ≥2 步且每步有 `text`/`why`；`sketch`/`cited`/`none` 必须写 `gap_note`（`cited` 表示底本只引述不证明，`none` 表示底本连陈述都没给出证明计划）。
- `theorems` 可为空数组（纯定义性的卡）。
- `pitfalls` ≥2 条，写**容易读错的具体位置**，不写「很重要」。

## 推导卡

```json
{
  "id": "yao17/deriv/depth-zero-chain",
  "type": "derivation",
  "title": "……",
  "aliases": ["……"],
  "track": "C",
  "summary": "……≤120 汉字",
  "question": "……？",
  "goal": "……",
  "setup": ["……", "……"],
  "steps": [
    {"no": 1, "text": "……", "why": "……", "locator": "A p.30", "provenance": "A"}
  ],
  "result": "……",
  "gaps": ["……"],
  "pitfalls": ["……", "……"],
  "related": ["yao17/concept/conductor-depth"],
  "sources": [{"text": "A", "section": "§3.5", "pages": [30, 30], "anchor": "A p.30"}],
  "rights": "rewritten",
  "status": "dev",
  "provenance_note": "……"
}
```

- `steps` ≥3 条，每步四字段齐全：`text`（这一步在做什么）、`why`（凭什么 / 为什么不能省）、`locator`（`A p.19` 形式）、`provenance`（`A` 原文写了 / `B` 原文暗示、我们补的 / `C` 我们的判断）。
- `gaps` 写「底本没写、由我们补的」地方；`pitfalls` ≥2 条，写读推导时最容易走岔的地方。
- `setup` 只写推导真正用到的设定与引理，不重复底本整节内容。

## 校验

```bash
python tools/lint_cards.py cards --strict              # 本地（页码上界 36、track O–D）
python tools/card_spec_check.py --set yao17 --strict   # 仓级（在仓库根目录跑）
```

- 两套校验的差别：本地版额外检查 `steps`/`pitfalls`/`anchor` 句式与 `provenance` 取值；仓级版额外检查 `related` 是否指向真实存在的卡。
- `status` 目前一律 `dev`（已过两套 lint，但未经人工复核）；`rights` 一律 `rewritten`。
