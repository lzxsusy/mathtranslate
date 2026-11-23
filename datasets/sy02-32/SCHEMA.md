# 资料卡体例（sy32）

底本：Edward Frenkel, Robert Langlands, Ngô Bao Châu,
*Formule des traces et fonctorialité : le début d'un programme*，
arXiv:1003.4578v2，2010-09-29，法文 54 页。
卡片 id 前缀 **sy32**；页码一律 **PDF 页序**（= 印刷页，偏移 0，范围 1–54）。

本工程与 `08_source_code/SY02-32_迹公式与函子性_一个纲领的开端/资料卡/` 是同一套卡片的两份副本（交付时同步）。

---

## 1. 文件与命名

```
datasets/sy02-32/cards/concepts/<slug>.json      id: sy32/concept/<slug>
datasets/sy02-32/cards/derivations/<slug>.json   id: sy32/deriv/<slug>
```

slug 用小写字母、数字、连字符（`formule-des-traces-stable`）。文件名必须等于 slug。

## 2. 轨道（track）

| 轨道 | 范围 | 典型卡 |
|---|---|---|
| A | 纲领、$L$ 函数与 $L$ 包：函子性、Arthur 参数、Ramanujan 型 | `fonctorialite`、`parametre-d-arthur` |
| B | 函数域的几何侧：$\Bun_G$、Hecke 叠、$\ell$-进层、几何 Satake | `bun-g`、`satake-geometrique` |
| C | 稳定化：拟分裂、稳定共轭类、$z$-扩张、Steinberg–Hitchin 基 | `base-steinberg-hitchin`、`z-extension` |
| D | 测度与 $\theta$：加法特征、自对偶测度、Tamagawa 数、轨道积分 | `mesure-de-tamagawa`、`theta-v` |
| E | 主项：$\hat\theta(0)$、极赋值集、基本局部系统 | `terme-dominant`、`lieu-tres-valuatif` |

本套卡无 O 轨（记号索引并入了 `03-条款索引.md`）。

## 3. 概念卡字段

```json
{
  "id": "sy32/concept/formule-des-traces-stable",
  "type": "concept",
  "track": "A",
  "title": "稳定迹公式",
  "aliases": ["formule des traces stable"],
  "summary": "≤120 汉字的定义性概括（去掉公式计字数）",
  "question": "以问号结尾的一句话问题",
  "definition": {"text": "定义正文", "notation": "记号约定"},
  "key_points": ["≥3 条要点"],
  "formulas": ["≤5 条关键公式（LaTeX）"],
  "theorems": [
    {"name": "命题名", "statement": "陈述",
     "proof": {"status": "sketch|complete|gap",
               "steps": [{"no": 1, "text": "步骤", "why": "理由"}],
               "gap_note": "缺口说明（sketch/gap 必填）"},
     "source": "A p.30 (3.17)"}
  ],
  "pitfalls": ["≥2 条易错点"],
  "related": ["sy32/concept/..."],
  "sources": [
    {"text": "A", "book": "Frenkel–Langlands–Ngô 2010",
     "section": "§3.4", "pages": [30, 31],
     "anchor": "A p.30 §3.4",
     "quote": "12–120 字符的原文逐字引文（不得含中文）"}
  ],
  "rights": "rewritten",
  "status": "draft",
  "provenance_note": "改写自原文何处；若参考本库卡片，在此注明（不进 sources）"
}
```

## 4. 推导卡字段

```json
{
  "id": "sy32/deriv/theta-zero",
  "type": "derivation",
  "track": "E",
  "title": "θ̂(0) 等于积分：从 (5.2) 到命题 5.6",
  "aliases": [],
  "summary": "≤120 字",
  "question": "以问号结尾",
  "goal": "这条推导要得到什么",
  "setup": ["前提 1", "前提 2"],
  "steps": [
    {"no": 1, "text": "步骤", "why": "为什么成立",
     "locator": "A p.47", "provenance": "A"}
  ],
  "result": "结论",
  "pitfalls": ["≥2 条"],
  "related": ["sy32/..."],
  "sources": [{"text": "A", "...": "同上"}],
  "rights": "rewritten",
  "status": "draft",
  "provenance_note": "…"
}
```

`steps[].provenance` ∈ `A|B|C`（A=原文，B=标准参考，C=本库译注）。

## 5. 硬规则（由 `tools/lint_cards.py` 与 `tools/verify_quotes.py` 检查）

1. `id` 必须 `<prefix>/(concept|deriv)/<slug>`，slug = 文件名。
2. `track` ∈ A–E。
3. `summary` 去掉 `$...$` 后 ≤120 字；`question` 以问号结尾。
4. `pitfalls` ≥2；`related` ≥1 且必须指向已存在的卡。
5. `sources` 中 `text` 为 `A` 的，必须带 `quote`：12–120 字符、不含中文、且**逐字**出现在所写 `pages` 范围内的原文中。
6. `pages` 为两个整数，1 ≤ p1 ≤ p2 ≤ 54。
7. `proof.status` 为 `complete` 时 ≥2 步；为 `sketch`/`gap` 时必须写 `gap_note`。
8. 不得出现本机绝对路径。

## 6. 质检

```bash
cd 08_source_code/SY02-32_迹公式与函子性_一个纲领的开端
python 资料卡/tools/lint_cards.py 资料卡/cards --prefix sy32 --no-pkg
python 资料卡/tools/verify_quotes.py 资料卡/cards --root .
```

两者都须 exit 0。当前结果：31 张卡（24 概念 + 7 推导）、lint 错误 0、31 条引文全部逐字命中。

## 7. 入库

```bash
python kb/ingest.py json     # datasets/**/cards/**/*.json → kb/cards/<work>.jsonl
python kb/build_kb.py
python kb/q.py stats
```

`work_of("sy02-32")` = `sy02-32`；卡片 id 加前缀后形如 `sy02-32.sy32/concept/...`，检索键仍含 `sy32` 片段。
