# sy0246 · 卡片字段规范

本集卡片是 `datasets/` 下的机器可读资料卡，遵循 `04_playbook/23_资料卡制作规范_v1.md` 与仓库根 `tools/card_spec_check.py --strict`；本文件只写本集的补充口径。

## 文件与命名

- 路径：`cards/concepts/<slug>.json` 或 `cards/corrections/<slug>.json`
- `id`：`sy0246/<type>/<slug>`，必须与路径一致（`tools/check_cards.py` 会核）。
- 编码 UTF-8（无 BOM），LF 换行，2 空格缩进，单卡 ≤ 12 KB。
- 每张卡由 `tools/make_cards.py` 生成；**手改 JSON 会被下一次生成覆盖**，改内容请改 `make_cards.py`。

## 通用字段

| 字段 | 必填 | 说明 |
|---|---|---|
| `id` | 是 | 见上 |
| `type` | 是 | `concept` 或 `correction` |
| `track` | 是 | 所属节：`§0 预备` / `§1 几何类域论` / … |
| `title` | 是 | 中文标题，20 字以内 |
| `aliases` | 是 | 法文原词、英文通行名、仓库别名（如“Hecke 特征层”） |
| `summary` | 是 | ≤160 字，只陈述原文有的内容 |
| `question` | 是 | 这张卡回答的问题，一句话 |
| `key_points` | 是 | 3–6 条，每条一个可核事实 |
| `formulas` | 否 | LaTeX 源码字符串数组（不带 `$`） |
| `theorems` | 否 | 见下；概念卡若含编号结果则必填 |
| `pitfalls` | 是 | ≥1 条，写“最容易错成什么” |
| `related` | 是 | 至少 1 条本集卡 id（lint 会核存在性） |
| `sources` | 是 | 见下，至少 1 条 |
| `rights` | 是 | 一律 `rewritten`（本集是译述+改写，不复制原文成段） |
| `status` | 是 | `reviewed`（经 sources 逐字核对 + 至少 1 条外核）或 `dev` |
| `verification` | 是 | 见下 |

## sources[]

```json
{
  "book": "Laumon, Séminaire Bourbaki 906 (2002), arXiv:math/0207078v1",
  "section": "§2",
  "pages": [7],
  "pdf_pages": [7],
  "quote": "法文原文逐字（≤300 字符，允许 … 省略）",
  "anchor": "08_source_code/SY02-46_…/源码/sections/s03-main.tex:L31-L37（Hecke 性质的译文）"
}
```

- `pages` 与 `pdf_pages` 都写 PDF 页序 1–19，两者相等，因此不写 `page_note`。
- `quote` 必须与 arXiv PDF 文本层逐字一致；公式下标被文本层压平时，以 TeX 源码为准并在 `anchor` 的括注里说明。
- `anchor` 必须能机械解析：`<仓库相对路径>:L起-L止`，括注写“说明”。

## theorems[]

```json
{
  "name": "定理 2.2（FGV 主定理）",
  "kind": "theorem",
  "statement": "中文陈述，量词、方向、适用范围必须与原文一致",
  "proof": {"status": "cited", "steps": [], "gap_note": ""},
  "source": "Laumon p.7–8；[F-G-V 2] 定理 1.1"
}
```

- `kind`：`theorem` / `proposition` / `corollary` / `lemma` / `definition` / `remark`，与底本层级一致，不升不降；底本未编号的写 `(0.2)` 并在 `name` 里注明“未编号”。
- `proof.status` 只用 `complete` / `sketch` / `cited` / `none`；`sketch` 时 `gap_note` 非空。
- Laumon 是综述，绝大多数证明是引用或概述，故多为 `cited`；只有原文给出完整论证的（定理 1.2 的代数证明）用 `complete`/`sketch`。

## verification

```json
{
  "status": "checked",
  "checked_on": "2026-11-27",
  "checks": [
    {"entry": "底本页 PDF", "url": "https://arxiv.org/pdf/math/0207078v1#page=7",
     "asserts": "p.7 逐字含 quote 所述定义", "verdict": "supports"},
    {"entry": "底本 TeX 源码", "url": "https://arxiv.org/e-print/math/0207078",
     "asserts": "源码第 1307–1326 行与 quote 同", "verdict": "supports"},
    {"entry": "F-G-V 2（E2）", "url": "https://arxiv.org/abs/math/0012255",
     "asserts": "摘要陈述同一主定理（不可约、各分支不可约、Hecke 特征层）", "verdict": "supports"}
  ]
}
```

- 每卡 ≥3 条 check，覆盖：`底本页 PDF`（E1 逐字引文）、`底本 TeX 源码`（E1 公式/措辞）、至少一条外部 E2。
- `verdict` ∈ `supports` / `partial` / `unverified` / `contradicts` / `not_applicable`；`partial` 必须在 `asserts` 里写清“只支持哪一半”。
- 外部 check 的 URL 必须是 E1/E2：arXiv、出版社 DOI、Numdam、zbMATH、nLab、Stacks。禁止博客/百科/知乎；不得只写“见原书”。

## 生成与校验

```bash
python datasets/sy0246/tools/make_cards.py          # 生成 cards/*.json 与 index.jsonl、verification.jsonl
python datasets/sy0246/tools/check_cards.py         # 本集专项检查（id/路径、anchor 行号越界、quote 长度、checks 数）
python tools/card_spec_check.py --set sy0246 --strict
```
