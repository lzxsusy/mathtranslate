# lawrge24 卡片规范（SCHEMA v1.0）

底本：**LAWRGE 2024 NOTES — Relative Langlands Duality**，2024-12-03 生成，73 页，15 讲；Ben-Zvi / Sakellaridis / Venkatesh 主讲，研讨会参会者笔记（无 arXiv 号、无正式出版信息；原文自述「极不完整、未校订」）。
中译注本：`08_source_code/SY02-15_相对朗兰兹对偶/`（v1.0，65 页）。

本目录把这份笔记拆成**中文重写**的概念卡与推导卡，回答「相对朗兰兹对偶在说什么、哪一步是证明、哪一步只是期望」。卡片不是译文，也不替代原文；引用原文一律短句 + 页码。

---

## 1. 文件与标识

```
cards/concepts/<slug>.json      id: lawrge/concept/<slug>
cards/derivations/<slug>.json   id: lawrge/deriv/<slug>
```

- slug 用小写字母、数字、连字符；文件名 = slug。
- `type`：`concept` / `derivation`。
- `track`：`O` / `A` / `B` / `C` / `D` / `E`。

| 轨道 | 范围 | 节 |
|---|---|---|
| O | 总览：主陈述、两侧理论、证明地图 | §3、§13、全书 |
| A | TQFT 语言与算术–拓扑字典 | §1–§3 |
| B | 边界条件、raviolo、Hecke、几何 Satake | §4、§7 |
| C | 球簇、对偶群、小 Weyl 群、超球 | §8–§10 |
| D | Plancherel、局部范畴化猜想、shearing | §8、§11 |
| E | 周期层、L-层、整体猜想、L-函数与例子 | §5、§12–§15 |

## 2. 页码与引文（硬规则）

- `pages` = **原文 PDF 页序**（1–73，偏移 0）；`pdf_pages` 与 `pages` 相同。
- `anchor` 形如 `A p.37`；`text` 固定 `"A"`；`book` 固定
  `"LAWRGE 2024 Notes, Relative Langlands Duality (2024-12-03, 73 pp.)"`。
- `section` 形如 `"§8"`，必须与 `pages` 所在讲次一致（§N ↔ `chNN.txt`）。
- `quote`：**逐字英文原句，12–120 字符，不含中文**，必须原样出现在该页文本中
  （`工程文件/work/原文/chNN.txt` 的 `===== PDF PAGE N =====` 分页；页 N 的正文在标记 N+1 之前）。
- 一条 `sources` 只引一页；跨页请写两条。
- 卡片正文不得出现本机绝对路径。

## 3. 概念卡字段

```json
{
  "id": "lawrge/concept/<slug>",
  "type": "concept",
  "track": "C",
  "title": "中文标题（可夹 $\\LaTeX$）",
  "aliases": ["英文名", "$\\LaTeX$ 记号", "中文别译"],
  "summary": "≤120 汉字的定义性概括",
  "question": "这张卡要回答的问题？",
  "definition": {"text": "中文定义（重写，不整段贴译文）",
                 "notation": "$X$、$\\check X$、$M=T^*X$ …"},
  "key_points": ["≥3 条，每条讲清机制或为什么重要"],
  "formulas": ["≥1 条关键公式"],
  "theorems": [
    {"name": "定理 8.19（原文编号）", "statement": "中文陈述",
     "proof": {"status": "complete|sketch|gap",
               "steps": [{"no": 1, "text": "…", "why": "…"}],
               "gap_note": "status≠complete 时必填：缺什么、原文是否只给引用"},
     "source": "§8, p.38"}
  ],
  "pitfalls": ["≥2 条：与什么易混、常见误读、条件在哪一步不可省"],
  "related": ["lawrge/concept/<slug>", "…≥2 条，必须能解析"],
  "sources": [{"text": "A", "book": "LAWRGE 2024 Notes, Relative Langlands Duality (2024-12-03, 73 pp.)",
               "section": "§8", "pages": [38, 38], "pdf_pages": [38, 38],
               "anchor": "A p.38", "quote": "英文原句 12–120 字符"}],
  "rights": "rewritten",
  "status": "draft",
  "verification": {"status": "source-only", "checked_on": "2026-11-27"},
  "provenance_note": "哪些内容是重写的、依据哪几页；未做外部核验"
}
```

- `track` 为 `O` 的总览卡可只引 1 页，但 `related` 仍须 ≥2。
- `theorems` 可为空数组；有则 `proof.status` 只能取 `complete|sketch|gap`，`sketch/gap` 必须写 `gap_note`。
- `status` 一律 `draft`（本批未做外部逐条核验）；`verification.status` 一律 `source-only`。
- `summary` 按汉字计 ≤120（公式不计）；`question` 以全角 `？` 结尾。

## 4. 推导卡字段

```json
{
  "id": "lawrge/deriv/<slug>",
  "type": "derivation",
  "track": "D",
  "title": "……",
  "aliases": ["…"],
  "summary": "≤120 汉字",
  "question": "……？",
  "goal": "本推导要解决的问题（一句话）",
  "setup": ["前提 1", "前提 2", "……"],
  "steps": [
    {"no": 1, "text": "本步做什么", "why": "为什么这么做",
     "locator": "A p.48", "provenance": "A|B|C"}
  ],
  "result": "结论一句话",
  "pitfalls": ["≥2 条"],
  "related": ["lawrge/concept/<slug>"],
  "sources": [{"text": "A", "…": "同上"}],
  "rights": "rewritten",
  "status": "draft",
  "verification": {"status": "source-only", "checked_on": "2026-11-27"},
  "provenance_note": "……"
}
```

- `steps` ≥4 步，每步都有 `locator`；`provenance` 取 `A`（原文直接写出）/`B`（原文提示、本卡补全）/`C`（本卡的整理，需在 `provenance_note` 说明）。
- 推导卡不假装证明原文没证的东西：原文只给期望的，`result` 用「若…则…」或「原文期望」措辞。

## 5. 质量闸门

```bash
python datasets/lawrge24/tools/lint_cards.py
```

检查：必填字段、id 前缀、track 枚举、summary 汉字数、question 全角问号、key_points≥3、formulas≥1、pitfalls≥2、theorems 证明字段、related 可解析且非自身、sources 完整、`pages`/`pdf_pages` 等长、**quote 逐字命中对应页**、quote 长度与语言。退出码 0 才入库。

## 6. 与五件套的关系

`08_source_code/SY02-15_相对朗兰兹对偶/资料卡/00–04` 是**工程级**速览、结果清单、论证地图、条款索引、术语勘误；本目录是**卡片层**，一卡一概念/一推导，供站点索引与跨书检索。两者内容应一致；本目录不重复五件套的表格，只把「一个概念讲透」。
