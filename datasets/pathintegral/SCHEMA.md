# 资料卡 JSON 规范（v1）

一份卡片一个 JSON 文件，UTF-8，缩进 2 空格。文件名 = id 的最后一段。概念卡放 `cards/concepts/`，例子卡放 `cards/examples/`。

## 概念卡

```json
{
  "id": "pi/concept/feynman-kernel",
  "type": "concept",
  "title": "费曼核与传播子",
  "aliases": ["Feynman kernel", "传播子", "路径积分核"],
  "track": "A",
  "summary": "不超过 120 汉字的摘要",
  "question": "卡片正面的自测题，一句话",
  "definition": {
    "text": "定义的完整陈述，可含 LaTeX 行内公式",
    "notation": "符号约定；没有就写空字符串"
  },
  "key_points": ["要点 1", "要点 2", "要点 3"],
  "formulas": ["$F_\\nabla=-\\frac{i}{\\hbar}\\omega$"],
  "theorems": [
    {
      "name": "定理/命题的名字",
      "statement": "完整陈述",
      "proof": {
        "status": "complete",
        "steps": [
          {"no": 1, "text": "推导", "why": "为什么这一步成立/为什么需要它"}
        ],
        "gap_note": ""
      },
      "source": "ch02a.tex:13-85（原书 p.80–82）"
    }
  ],
  "pitfalls": ["真正的易错点"],
  "related": ["pi/concept/path-integral-definition", "pi/example/free-particle-semiclassical"],
  "sources": [
    {
      "book": "量子力学与几何",
      "section": "§2.1.1 量子演化与费曼核",
      "pages": [80, 82],
      "pdf_pages": [81, 83],
      "anchor": "ch02a.tex:13-85"
    }
  ],
  "rights": "rewritten",
  "status": "draft"
}
```

字段规则：

| 字段 | 必填 | 规则 |
|---|---|---|
| `id` | 是 | `pi/concept/<slug>`，slug 只含小写字母、数字、连字符 |
| `type` | 是 | `concept` |
| `title` | 是 | 中文标题，可带英文原名 |
| `aliases` | 是 | 数组，至少 1 条（英文名/别名/缩写） |
| `track` | 是 | `A` 基础与时间切片 / `B` 高斯路径积分与谐振子 / `C` 渐近方法与半经典 / `D` 格林函数与 WKB / `E` 微扰与代数结构 / `O` 总览 |
| `summary` | 是 | ≤120 汉字（不含公式与空格） |
| `question` | 是 | 自测题，一句话，以问号结尾 |
| `definition.text` | 是 | 定义正文，非空 |
| `key_points` | 是 | ≥3 条，每条一句话 |
| `formulas` | 是 | ≥1 条，LaTeX 数学模式 |
| `theorems` | 是 | ≥1 条；每条含 `name/statement/proof/source` |
| `theorems[].proof.status` | 是 | `complete` 或 `sketch` |
| `complete` 的 steps | 是 | ≥2 步，每步 `text` 与 `why` 非空 |
| `sketch` 的 gap_note | 是 | 非空，写明缺哪一块 |
| `pitfalls` | 是 | ≥1 条 |
| `related` | 是 | ≥2 条，必须能解析到本库的 id |
| `sources` | 是 | ≥1 条；`pages` 为印刷页，`pdf_pages` = pages+1 |
| `rights` | 是 | 固定 `rewritten` |
| `status` | 是 | `draft`（统稿后改 `reviewed`） |

## 例子卡

```json
{
  "id": "pi/example/gamma-asymptotics",
  "type": "example",
  "title": "Gamma 函数的拉普拉斯渐近",
  "aliases": ["Gamma asymptotics"],
  "track": "C",
  "summary": "不超过 100 字的摘要",
  "question": "这张例子卡训练什么？",
  "concept_refs": ["pi/concept/laplace-method"],
  "setup": "题目设定：对象、维数、坐标系、要算什么",
  "computation": [
    {"no": 1, "text": "计算", "why": "为什么这样算"},
    {"no": 2, "text": "计算", "why": "为什么这样算"}
  ],
  "result": "最终结论，可用公式",
  "check": "独立复核办法：代回、特例、量纲、数值",
  "pitfalls": ["这一例特有的坑"],
  "related": ["pi/concept/gaussian-integral"],
  "sources": [
    {
      "book": "量子力学与几何",
      "section": "§2.5.1 拉普拉斯方法（例 2.5.1）",
      "pages": [97, 97],
      "pdf_pages": [98, 98],
      "anchor": "ch02a.tex:963-992"
    }
  ],
  "rights": "rewritten",
  "status": "draft"
}
```

字段规则：

| 字段 | 必填 | 规则 |
|---|---|---|
| `id` | 是 | `pi/example/<slug>` |
| `type` | 是 | `example` |
| `track` | 是 | `A`/`B`/`C`/`D`/`E` |
| `summary` | 是 | ≤100 汉字 |
| `question` | 是 | 一句话 |
| `concept_refs` | 是 | ≥1 条，解析到概念卡 |
| `setup` | 是 | 非空 |
| `computation` | 是 | ≥2 步，每步 `no/text/why` 非空 |
| `result` | 是 | 非空，最好有公式 |
| `check` | 是 | 非空，必须可执行 |
| `pitfalls` | 是 | ≥1 条 |
| `related` | 是 | ≥1 条 |
| `sources` | 是 | ≥1 条，页码规则同上 |

## 数学写法

- 行内公式 `$...$`，行间公式用 `$$...$$`（Markdown 渲染时用），JSON 字符串里反斜杠要双写。
- 矩阵可用 `\begin{pmatrix}...\end{pmatrix}`（MathJax/KaTeX 均支持）；除此之外不用 `\begin{...}` 环境，多行公式拆成多条 `formulas` 或写在 `statement` 里用 `\\` 分行。
- 只用 MathJax 的标准宏：`\mathbb{R}`、`\mathbb{C}`、`\operatorname{Span}`，不要用书内自定义的 `\R`、`\C`、`\Span`、`\pa`；后者在 Markdown 阅读器里会渲染成红字。
- 中文标点统一用全角；专名首次出现给英文原名，如「最速下降法（steepest descent）」。
- 引用书内编号写作「命题 5.1.7」「例 5.4.9」，不要只写裸编号。
