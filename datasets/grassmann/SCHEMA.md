# 格拉斯曼资料卡 · JSON 规范（v1）

一张卡一个 JSON 文件，UTF-8，2 空格缩进，无 BOM，文件末尾留一个换行。
`filename` = `id` 最后一段。概念卡放 `cards/concepts/`，例子卡放 `cards/examples/`。
全部必须通过 `python tools\validate_cards.py --strict`（0 error）。

> 本库脱胎于 `..\_cards_shtuka`（同一套字段与流程），差别只有三处：
> `id` 前缀 `grassmann/`、`track` 是章节轨道 A/1–9、`sources.anchor` 指向 `chapters/chNN.tex:行号`。

## 概念卡

```json
{
  "id": "grassmann/concept/alpha-stable-coherent-system",
  "type": "concept",
  "title": "α-稳定凝聚系",
  "aliases": ["alpha-stable coherent system", "α-稳定 (E,V)", "stability of coherent systems"],
  "track": "7",
  "summary": "光滑射影曲线上的凝聚系 (E,V) 按 α-斜率判稳：μ_α=deg E+α dim V 除以秩；α 越大越难稳定，阈值处发生翻转。",
  "question": "α 变大时，(E,V) 为什么更容易不稳定？阈值 α 由什么决定？",
  "definition": {
    "text": "设 $C$ 是光滑射影曲线。$C$ 上一个型为 $(n,d,k)$ 的**凝聚系**是一对 $(E,V)$，其中 $E$ 是 $C$ 上秩 $n$、次数 $d$ 的向量丛，$V\\subseteq H^0(E)$ 是 $k$ 维线性子空间。**凝聚子系**是一对 $(F,W)$，$F\\subseteq E$ 是子丛且 $W\\subseteq V\\cap H^0(F)$。对实数 $\\alpha$ 定义 $\\alpha$-斜率 $$\\mu_\\alpha(E,V)=\\frac{d}{n}+\\alpha\\frac{k}{n}=\\frac{\\deg E+\\alpha\\dim V}{\\operatorname{rk}E}.$$ 若对每个真凝聚子系 $(F,W)$ 都有 $\\mu_\\alpha(F,W)<\\mu_\\alpha(E,V)$，则称 $(E,V)$ 是 $\\alpha$-稳定的；把 $<$ 换成 $\\le$ 得 $\\alpha$-半稳定。",
    "notation": "$n=\\operatorname{rk}E$，$d=\\deg E$，$k=\\dim V$；$\\alpha\\in\\mathbb{R}$；「真」指 $0<\\operatorname{rk}F<\\operatorname{rk}E$。"
  },
  "key_points": [
    "$\\alpha=0$ 时退化为向量丛的斜率稳定性（只看 $d/n$），$V$ 不再进入判据。",
    "$\\alpha\\to+\\infty$ 时稳定性由 $k/n$ 主导：系的维数相对秩越小越好。",
    "$(F,0)$ 也是凝聚子系。$\\alpha\\le 0$ 且 $k\\ge 1$ 时，$(E,0)$ 的斜率 $d/n$ 不小于 $(E,V)$，故不可能稳定——这正是本章要求 $\\alpha>0$ 的原因。",
    "对固定 $(n,d,k)$，$\\alpha$ 被分成有限个区间，模空间 $G(\\alpha;n,d,k)$ 只在区间内不变。"
  ],
  "formulas": [
    "\\mu_\\alpha(E,V)=\\frac{\\deg E+\\alpha\\dim V}{\\operatorname{rk}E}",
    "\\mu_\\alpha(E',V')<\\mu_\\alpha(E,V)\\quad\\text{对所有真子系}"
  ],
  "theorems": [
    {
      "name": "α-稳定凝聚系的模空间（存在性框架）",
      "statement": "对固定 $(n,d,k)$ 与使稳定性非空的 $\\alpha$，$\\alpha$-稳定凝聚系的模空间是拟射影簇；当 $\\alpha$ 足够大时它同构于某个 Quot 概形的开子集。",
      "proof": {
        "status": "reference",
        "steps": [],
        "gap_note": ""
      },
      "source": "中译 p.116–118（§1 定义、§2 存在性问题）；原始构造见 Le Potier / King–Newstead"
    }
  ],
  "pitfalls": [
    "把 $\\mu_\\alpha$ 写成 $\\tfrac{d}{n}+\\alpha k$——第二项忘了除秩，比较不同秩的子系时结论会翻。",
    "只查「极大的」凝聚子系 $(F,V\\cap H^0(F))$，忘了 $(F,0)$ 也算：$\\alpha\\le 0$ 的情形就是被它判掉的。"
  ],
  "related": [
    "grassmann/concept/slope-stability",
    "grassmann/concept/coherent-system"
  ],
  "sources": [
    {
      "book": "Grassmannians, Moduli Spaces and Vector Bundles (Clay 14)",
      "section": "ch7 §1 定义",
      "pages_zh": "116",
      "pages_en": "130",
      "anchor": "chapters/ch07.tex:14"
    }
  ],
  "rights": "rewritten",
  "status": "draft"
}
```

> 上面是**格式示例**（内容真实、可直接用；`related` 指向的两张卡 Phase 3 会建）。照抄结构，别照抄标题。

## 例子卡

在概念卡全部字段之外，多三个字段（并且 `type` 为 `example`）：

```json
{
  "id": "grassmann/example/alpha-stable-genus-2-k-1",
  "type": "example",
  "concept_refs": ["grassmann/concept/alpha-stable-coherent-system", "grassmann/concept/slope-stability"],
  "setup": "取 $C$ 为亏格 2 的光滑射影曲线，$n=2$，$d=3$，$k=1$：即 $(E,V)$ 为秩 2、次数 3 的向量丛配上 1 维子空间 $V\\subset H^0(E)$。",
  "computation": "由 $\\mu_\\alpha=\\frac{3+\\alpha}{2}$，对秩 1 的真子系 $L\\subset E$，$\\mu_\\alpha(L)=\\deg L$。……（此处写完整的代入与判稳过程，最后给出稳定的 $\\alpha$ 区间）。",
  "…": "其余字段同概念卡"
}
```

## 字段硬规则（validate 会查）

| 字段 | 要求 |
|---|---|
| `id` | `grassmann/concept/[a-z0-9-]+` 或 `grassmann/example/…`；与文件名一致 |
| `track` | `A`（跨章基础）或 `1`–`9`（对应章） |
| `summary` | 汉字数 20–120（不含公式与英文） |
| `question` | 以 `？` 或 `?` 结尾 |
| `definition.text` | 非空；带公式；与**中译本正文**一致 |
| `key_points` | ≥3 条，每条一句完整的话 |
| `formulas` | ≥1 条，LaTeX，`$` 成对；JSON 里反斜杠写双 |
| `theorems` | ≥1 条；`proof.status` ∈ `complete`（steps ≥2，每步有 `text` 与 `why`）/ `sketch`（必须 `gap_note`）/ `reference`（只给出处） |
| `pitfalls` | ≥1 条，必须是**具体的坑**（写错的下场），不是「注意细节」 |
| `related` | ≥2 条，且必须是真实存在的卡 id（跨章优先） |
| `sources` | ≥1 条，含 `book/section/pages_zh/pages_en/anchor`；`anchor` 必须是 `chapters/chNN.tex:行号` 且行号真指向内容 |
| `rights` | 固定 `rewritten` |
| `status` | `draft`（卡手交）→ Lead 抽查后 `reviewed` |

## 别做的事

- 不写本机路径、不写 `C:\`、不写私有仓库地址。
- 不从 PDF 文字层复制公式（会被拆碎）；公式从 `.tex` 抄。
- 不复述译文原句当 `definition`：要改写成自己的话，必要时给一个原文没有的等价说法。
- 不在卡片里下「原文这里错了」的结论——那是 errata 的事；卡片只写正确的数学，坑里点一句「中译 p.N 有误，见 errata」。
