# 资料卡 JSON 规范（siebert v1）

Bernd Siebert 讲授、Jackson Van Dyke 记录的 *Mirror Symmetry*（2019 年秋课程讲义，公开讲义、未正式出版）中文译本《镜像对称：代数几何专题讲义》（103 页）的**裁切**材料规范。

讲义原 PDF 的印刷页为 **7–106**；卡中的「原书 p.N」一律指这组印刷页，不是中文译本的页序。换算以译稿的页码对照表为准。

一张卡一个 JSON 文件：UTF-8、缩进 2 空格、`ensure_ascii=False`，文件名 = id 的最后一段。

---

## 1. id 与目录

| 类型 | 目录 | id 形式 |
|---|---|---|
| 概念卡 | `cards/concepts/` | `siebert/concept/<slug>` |
| 推导卡 | `cards/derivations/` | `siebert/deriv/<slug>` |
| 勘误卡 | `cards/corrections/` | `siebert/correction/<slug>` |

`<slug>` 只含小写字母 `a–z`、数字 `0–9` 与连字符 `-`；不能以连字符开头或结尾，不能出现连续连字符。**slug 必须与文件名一致**（`lint_cards.py` 会核对）。

`type` 与目录一一对应：`concepts/` → `concept`，`derivations/` → `derivation`，`corrections/` → `correction`。

## 2. track

| track | 主题 | 覆盖范围 |
|---|---|---|
| `A` | 五次超曲面与数值镜像对称 | 概览、第 1 章 |
| `B` | 叠与模空间 | 第 2 章 |
| `C` | Gromov–Witten 理论与虚技术 | 第 3 章 |
| `D` | 环面几何 | 第 4 章 |
| `E` | 环面退化与镜像构造 | 第 5 章 |
| `F` | 同调镜像对称 | 第 6 章 |
| `O` | 术语、总览、方法论 | 跨章 |

一卡一个 track。跨章的内容按「主要证据落在哪一章」归轨，另一轨只放进 `related`，不重复落卡。

## 3. 三类卡共用的字段

| 字段 | 类型 | 要求 |
|---|---|---|
| `id` | string | 见 §1，全局唯一 |
| `type` | string | `concept` / `derivation` / `correction` |
| `track` | string | `A`–`F` 或 `O` |
| `title` | string | 中文标题，一卡一个主题 |
| `aliases` | string[] | 非空；英文名、常用记号、异名 |
| `summary` | string | ≤ 120 汉字（先去掉 `$...$` 公式，再去掉空白后计数） |
| `question` | string | 卡片正面的自测题，一句话，以「？」结尾 |
| `pitfalls` | string[] | 真正的易错点，不写「注意定义」这类废话 |
| `related` | string[] | 至少 2 条，必须能在本数据集内解析 |
| `sources` | object[] | 至少 1 条，见 §4 |
| `rights` | string | 一律 `rewritten`（自己的转述） |
| `status` | string | `draft` / `reviewed` / `published` |
| `provenance_note` | string | 证据链：原书页 + 核对用的 nLab / Stacks Project 条目 |

`summary` 是「一句话讲清这张卡」，不是摘要缩写；`question` 要能脱离卡片单独发问。

## 4. sources 的写法

```json
{
  "book": "Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)",
  "section": "第 1 章 §5 镜像五次超曲面",
  "pages": [15, 17],
  "anchor": "原书 p.15"
}
```

- `book` 必须逐字等于上面这串（`lint_cards.py` 的 `BOOK` 常量），否则 lint 报错。
- `section` 用「第 N 章 §M 小节名」；概览写「概览」；校订写「校订」。
- `pages` 是 `[起, 止]` 两个整数，且 `7 ≤ 起 ≤ 止 ≤ 106`。
- `anchor` 以「原书 p.」开头，后面跟页码；跨页可写 `原书 p.15–17`。
- 一张卡可有多条 `sources`；页码取印刷页，不取 PDF 页。

---

## 5. 概念卡

回答「这是什么、为什么需要、哪里会错」。

```json
{
  "id": "siebert/concept/mirror-quintic",
  "type": "concept",
  "track": "A",
  "title": "镜像五次超曲面",
  "aliases": ["mirror quintic", "镜像五次三维超曲面"],
  "summary": "五次超曲面按 (Z/5)³ 取商、再作射影消解后得到的光滑三次超曲面，与原来的五次超曲面构成镜像对。",
  "question": "镜像五次超曲面为什么必须经过 (Z/5)³ 商与射影消解？",
  "definition": {
    "text": "定义的完整陈述，可含行内公式 $h^{1,1}=1$ 与行间公式 $$h^{2,1}=101$$",
    "notation": "符号约定；没有就写空字符串"
  },
  "key_points": ["要点 1", "要点 2", "要点 3"],
  "formulas": ["$$c_3(z)=1$$"],
  "theorems": [
    {
      "name": "定理或命题的名字",
      "statement": "完整陈述",
      "proof": {
        "status": "complete",
        "steps": [
          {"no": 1, "text": "推导的一步", "why": "为什么这一步成立 / 为什么需要它"}
        ],
        "gap_note": ""
      },
      "source": "原书 p.15 §5"
    }
  ],
  "pitfalls": ["真正的易错点"],
  "related": ["siebert/deriv/picard-fuchs", "siebert/correction/notation-check"],
  "sources": [
    {
      "book": "Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)",
      "section": "第 1 章 §5 镜像五次超曲面",
      "pages": [15, 17],
      "anchor": "原书 p.15"
    }
  ],
  "rights": "rewritten",
  "status": "draft",
  "provenance_note": "原书 p.15–17 §5；术语按 nLab「mirror symmetry」条目核对。"
}
```

- `key_points` 至少 3 条（超过 6 条给 WARN）；`formulas` 至少 1 条。
- `theorems` 每项必填 `name` / `statement` / `proof` / `source`；`proof.status` ∈ `complete` / `sketch` / `none`，标 `complete` 必须有 `steps`。
- 证明没走完就老实标 `sketch`，在 `gap_note` 里写缺在哪一步。

## 6. 推导卡

回答「这条论证怎么一步步走通、每步凭什么」。

```json
{
  "id": "siebert/deriv/picard-fuchs",
  "type": "derivation",
  "track": "A",
  "title": "Picard–Fuchs 方程的推导",
  "aliases": ["Picard–Fuchs equation", "PF 方程"],
  "summary": "用 Griffiths 极点阶数约化，把周期积分的导数压回有限维 de Rham 上同调，从而得到二阶常微分方程。",
  "question": "周期积分满足的二阶方程是怎样从有限维上同调里推出来的？",
  "goal": "要得到的结论，一句话",
  "setup": ["前提 1", "前提 2"],
  "steps": [
    {
      "no": 1,
      "text": "这一步做什么",
      "why": "为什么必须这样 / 依据是什么",
      "locator": "原书 p.17 §7",
      "provenance": "A"
    }
  ],
  "result": "推导最终得到什么（可以带公式）",
  "gaps": ["原文只写「可以证明」、没有逐条验证的地方"],
  "pitfalls": ["易错点"],
  "related": ["siebert/concept/mirror-quintic", "siebert/correction/notation-check"],
  "sources": [
    {
      "book": "Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)",
      "section": "第 1 章 §7 Picard–Fuchs 方程",
      "pages": [17, 20],
      "anchor": "原书 p.17"
    }
  ],
  "rights": "rewritten",
  "status": "draft",
  "provenance_note": "原书 p.17–20 §7。"
}
```

`steps` 至少 3 步，每步必须有 `locator`（以「原书 p.」开头）与 `provenance`：

- `A` 讲义明写；
- `B` 由讲义推出、我们补的中间步；
- `C` 我们的判断。

`gaps` 至少 1 条：没有缺口就写清楚「本卡未覆盖的边界」，不要留空。

## 7. 勘误卡

回答「初版哪里错、为什么必须改、依据是什么」。

```json
{
  "id": "siebert/correction/notation-check",
  "type": "correction",
  "track": "O",
  "title": "「纤维」应为「纤维化」",
  "aliases": ["fibration 术语", "纤维化"],
  "summary": "初版把 fibration 译成「纤维」，与 fibre 混同；改后统一为「纤维化」。",
  "question": "初版这里为什么必须改？",
  "page": 15,
  "original": "初版的写法（只留足以辨认差异的片段）",
  "corrected": "改后的写法",
  "why": "为什么改：讲义原文、数学事实或术语表依据",
  "note": "补充说明，可空字符串",
  "pitfalls": ["只改这一处、不要推广到别处"],
  "related": ["siebert/concept/mirror-quintic", "siebert/deriv/picard-fuchs"],
  "sources": [
    {
      "book": "Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)",
      "section": "校订",
      "pages": [15, 15],
      "anchor": "原书 p.15"
    }
  ],
  "rights": "rewritten",
  "status": "draft",
  "provenance_note": "据译稿修订记录与讲义原 PDF p.15 逐条核对。"
}
```

- `page` 是单个整数，且 `7 ≤ page ≤ 106`。
- `original` / `corrected` 只留足以辨认差异的片段，不整段抄译文，更不抄讲义原文。
- `why` 必须给依据（讲义原句的转述、数学事实、术语表或 nLab / Stacks Project 条目），**不得写「更通顺」「更准确」这类空话**。
- 勘误卡覆盖两类改动：译本修订（初版译法 → 改后译法）与讲义本身的笔误 / 记号冲突（`original` 记原文写法，`corrected` 记按上下文应取的写法）。

---

## 8. 质检

```bash
python tools/lint_cards.py cards --strict     # 0 error 才算过；空 cards/ 也返回 0
python tools/build_index.py                   # 重建 index.jsonl
python tools/render_md.py                     # 重建 md/
```

`--strict` 只把 error 变成退出码 1，warning（如 `key_points` 超过 6 条）不拦。`--allow-missing` 跳过 `related` 的解析检查，只用于分批写卡的中途。
