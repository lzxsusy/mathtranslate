# 资料卡 JSON 规范（raskin_lcft v1）

Sam Raskin 讲授、Oron Propp 整理的 *Lectures on Cohomological Class Field Theory*（MIT 18.786，2016 年春课程讲义，公开讲义、未正式出版）中文译本《上同调类域论讲义》（91 页）的**裁切**材料规范。

讲义原 PDF 的印刷页为 **1–115**；卡中的「原书 p.N」一律指这组印刷页，不是中文译本的页序（译本的物理页 = 印刷页 + 4，首页另有三页前言目录）。

一张卡一个 JSON 文件：UTF-8、缩进 2 空格、`ensure_ascii=False`，文件名 = id 的最后一段。

---

## 1. id 与目录

| 类型 | 目录 | id 形式 |
|---|---|---|
| 概念卡 | `cards/concepts/` | `raskin_lcft/concept/<slug>` |
| 推导卡 | `cards/derivations/` | `raskin_lcft/deriv/<slug>` |
| 勘误卡 | `cards/corrections/` | `raskin_lcft/correction/<slug>` |

`<slug>` 只含小写字母 `a–z`、数字 `0–9` 与连字符 `-`；不能以连字符开头或结尾，不能出现连续连字符。**slug 必须与文件名一致**（`lint_cards.py` 会核对）。

`type` 与目录一一对应：`concepts/` → `concept`，`derivations/` → `derivation`，`corrections/` → `correction`。

## 2. track

| track | 主题 | 覆盖范围 |
|---|---|---|
| `A` | 局部类域论与希尔伯特符号 | 第 1–5 讲 |
| `B` | 同调代数工具 | 第 6–12 讲 |
| `C` | 无界复形的 Tate 上同调与消没定理 | 第 13–17 讲 |
| `D` | 范数群、Kummer 理论与存在定理 | 第 18 讲 |
| `E` | 布劳尔群、两个不等式与 gcft 主定理 | 第 19–23 讲 |

一卡一个 track。跨讲的内容按「主要证据落在哪一讲」归轨，其余只放进 `related`，不重复落卡。

## 3. 三类卡共用的字段

| 字段 | 类型 | 要求 |
|---|---|---|
| `id` | string | 见 §1，全局唯一 |
| `type` | string | `concept` / `derivation` / `correction` |
| `track` | string | `A`–`E` |
| `title` | string | 中文标题，一卡一个主题 |
| `aliases` | string[] | 非空；英文名、常用记号、异名 |
| `summary` | string | ≤ 120 汉字（先去掉 `$...$` 公式，再去掉空白后计数） |
| `question` | string | 卡片正面的自测题，一句话，以「？」结尾 |
| `pitfalls` | string[] | 真正的易错点，不写「注意定义」这类废话 |
| `related` | string[] | 至少 2 条，必须能在本数据集内解析 |
| `sources` | object[] | 至少 1 条，见 §4 |
| `rights` | string | 一律 `rewritten`（自己的转述） |
| `status` | string | `draft` / `reviewed` / `published` |
| `provenance_note` | string | 证据链：原书页 + 核对用的标准文献（如 Milne *CFT*、Neukirch–Schmidt–Wingberg、Weibel） |

`summary` 是「一句话讲清这张卡」，不是摘要缩写；`question` 要能脱离卡片单独发问。

## 4. sources 的写法

```json
{
  "book": "Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)",
  "section": "第 2 讲 希尔伯特符号",
  "pages": [6, 9],
  "anchor": "原书 p.6"
}
```

- `book` 必须逐字等于上面这串（`lint_cards.py` 的 `BOOK` 常量），否则 lint 报错。
- `section` 用「第 N 讲 讲名」（讲名见 [MAP.md](MAP.md)）；校订写「校订」。
- `pages` 是 `[起, 止]` 两个整数，且 `1 ≤ 起 ≤ 止 ≤ 115`。
- `anchor` 以「原书 p.」开头，后面跟页码；跨页可写 `原书 p.15–17`。
- 一张卡可有多条 `sources`；页码取印刷页，不取 PDF 页。

---

## 5. 概念卡

回答「这是什么、为什么需要、哪里会错」。

```json
{
  "id": "raskin_lcft/concept/hilbert-symbol",
  "type": "concept",
  "track": "A",
  "title": "希尔伯特符号",
  "aliases": ["Hilbert symbol", "二次希尔伯特符号", "(a,b)_K"],
  "summary": "K^×/(K^×)^2 上的双乘配对：b 是 K(√a)/K 的范数时取 1，否则取 −1；n=2 的 lcft 全部内容都装在这个符号里。",
  "question": "为什么「b 是 K(√a)/K 的范数」这件事能用一个 ±1 的双乘性符号来记录？",
  "definition": {
    "text": "对 $a,b\\in K^\\times$，$(a,b)_K=1$ 当且仅当 $b$ 属于 $K(\\sqrt a)/K$ 的范数群，否则为 $-1$。",
    "notation": "$(\\ ,\\ )_K$；$b\\in N_{K(\\sqrt a)/K}K(\\sqrt a)^\\times\\iff(a,b)_K=1$"
  },
  "key_points": ["要点 1", "要点 2", "要点 3"],
  "formulas": ["$(a,b)_K=1\\iff b\\in N_{K(\\sqrt a)/K}K(\\sqrt a)^\\times$"],
  "theorems": [
    {
      "name": "命题 2.3（良定义与双乘性）",
      "statement": "完整陈述",
      "proof": {
        "status": "sketch",
        "steps": [
          {"no": 1, "text": "推导的一步", "why": "为什么这一步成立 / 为什么需要它"}
        ],
        "gap_note": "缺在哪一步"
      },
      "source": "原书 p.6"
    }
  ],
  "pitfalls": ["真正的易错点"],
  "related": ["raskin_lcft/concept/lcft-main-theorem", "raskin_lcft/concept/norm-group"],
  "sources": [
    {
      "book": "Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)",
      "section": "第 2 讲 希尔伯特符号",
      "pages": [6, 9],
      "anchor": "原书 p.6"
    }
  ],
  "rights": "rewritten",
  "status": "reviewed",
  "provenance_note": "原书 p.6–9；定义与双乘性按译文命题 2.3、定理 2.12 转写，并与 Milne CFT 的 Hilbert 符号条核对。"
}
```

- `key_points` 至少 3 条（超过 6 条给 WARN）；`formulas` 至少 1 条。
- `theorems` 每项必填 `name` / `statement` / `proof` / `source`；`proof.status` ∈ `complete` / `sketch` / `none`，标 `complete` 必须有 `steps`。
- 证明没走完就老实标 `sketch`，在 `gap_note` 里写缺在哪一步。

## 6. 推导卡

回答「这条论证怎么一步步走通、每步凭什么」。

```json
{
  "id": "raskin_lcft/deriv/herbrand-quotient-multiplicativity",
  "type": "derivation",
  "track": "B",
  "title": "Herbrand 商的乘性：从有限长复形到 χ(L^×)=n",
  "aliases": ["Herbrand quotient multiplicativity", "χ 乘性"],
  "summary": "先证有限长复形的 Euler 特征乘性（引理 6.4），再经截断与长正合列把它搬到 χ(L^×)，最后落在 lcft 的 χ(L^×)=n。",
  "question": "引理 6.4 的指标计算凭什么能一路推到 χ(L^×)=[L:K]？",
  "goal": "对循环扩张 $L/K$ 证明 $\\chi(L^\\times)=[L:K]$。",
  "setup": ["前提 1", "前提 2"],
  "steps": [
    {
      "no": 1,
      "text": "这一步做什么",
      "why": "为什么必须这样 / 依据是什么",
      "locator": "原书 p.25 引理 6.4",
      "provenance": "A"
    }
  ],
  "result": "$\\chi(L^\\times)=[L:K]=n$。",
  "gaps": ["原文只写「显然」、没有逐条验证的地方"],
  "pitfalls": ["易错点"],
  "related": ["raskin_lcft/concept/herbrand-quotient", "raskin_lcft/correction/exactness-index"],
  "sources": [
    {
      "book": "Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)",
      "section": "第 6 讲 正合列与 Tate 上同调",
      "pages": [25, 25],
      "anchor": "原书 p.25"
    }
  ],
  "rights": "rewritten",
  "status": "reviewed",
  "provenance_note": "原书 p.25、30、31、38；引理 6.4 的指标链底本自相矛盾，按勘误卡 exactness-index 改写后的归纳法转写。"
}
```

`steps` 至少 3 步，每步必须有 `locator`（以「原书 p.」开头）与 `provenance`：

- `A` 讲义明写；
- `B` 由讲义推出、我们补的中间步；
- `C` 我们的判断。

`gaps` 至少 1 条：没有缺口就写清楚「本卡未覆盖的边界」，不要留空。

## 7. 勘误卡

回答「底本哪里错、为什么必须改、译文怎么处理」。

```json
{
  "id": "raskin_lcft/correction/bimultiplicativity",
  "type": "correction",
  "track": "A",
  "title": "双乘性解释句把 $b$ 印成了两处 $by^2$",
  "aliases": ["bimultiplicativity typo", "双乘性句子"],
  "summary": "底本说 $(a,bc)=1$ 当且仅当 $(a,b)=1$ 且 $(a,c)=1$，却把两个方程都印成 ax²+by²，第二个应为 ax²+bcy²。",
  "question": "这处排印错误为什么会让双乘性的解释变成循环论证？",
  "page": 6,
  "original": "either we can solve both $ax^2+by^2=1$ and $ax^2+cy^2=1$ separately",
  "corrected": "$ax^2+bcy^2=1$ 与 $ax^2+by^2=1$、$ax^2+cy^2=1$ 分别可解",
  "why": "双乘性要说的是 $(a,bc)=1\\iff(a,b)=1$ 且 $(a,c)=1$；两处都印成 $by^2$ 时第一个方程与前提重复，命题退化为同义反复，而 $ax^2+bcy^2=1$ 正是 $b$ 与 $c$ 两种范数条件的合取。",
  "note": "译文按数学含义改为 $ax^2+bcy^2=1$，并在源文件留 `% [原文疑误：…]` 注释。",
  "pitfalls": ["只改这一处，不要把全书的 $by^2$ 都替换掉"],
  "related": ["raskin_lcft/concept/hilbert-symbol", "raskin_lcft/correction/ker-n-direction"],
  "sources": [
    {
      "book": "Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)",
      "section": "校订",
      "pages": [6, 6],
      "anchor": "原书 p.6"
    }
  ],
  "rights": "rewritten",
  "status": "reviewed",
  "provenance_note": "据原 PDF p.6 页面图与排版保真抽取文本逐字核对；另见工程目录 `工程文件/ERRATA.md` 第 1 条。"
}
```

- `page` 是单个整数，且 `1 ≤ page ≤ 115`。
- `original` / `corrected` 只留足以辨认差异的片段，不整段抄译文，更不抄讲义原文。
- `why` 必须给依据（数学事实、上下文的定义、术语表或标准文献），**不得写「更通顺」「更准确」这类空话**。
- 勘误卡覆盖两类改动：译本修订（初版译法 → 改后译法）与底本本身的笔误 / 记号冲突（`original` 记原文写法，`corrected` 记按上下文应取的写法）。本数据集 10 张勘误卡全部属于后者，均经与原 PDF 逐页核对。

---

## 8. 质检

```bash
python tools/lint_cards.py cards --strict     # 0 error 才算过；空 cards/ 也返回 0
python tools/build_index.py                   # 重建 index.jsonl
python tools/render_md.py                     # 重建 md/
```

`--strict` 只把 error 变成退出码 1，warning（如 `key_points` 超过 6 条）不拦。`--allow-missing` 跳过 `related` 的解析检查，只用于分批写卡的中途。
