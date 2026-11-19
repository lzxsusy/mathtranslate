# Functoriality 资料卡 Schema

本数据集收录 Abouzaid–Bottman《Functoriality in categorical symplectic geometry》
（arXiv:2210.11159v1，68 页）的**自述重写**资料卡。一张卡一个 JSON 文件，
UTF-8、缩进 2 空格、`ensure_ascii=False`，文件名 = id 最后一段。

- `book`：`Abouzaid & Bottman, Functoriality in categorical symplectic geometry (arXiv:2210.11159v1)`
- 原文页：arXiv PDF 页码 1–68（与印刷页一致），卡片一律用「原书 p.N」标注。

## 卡的类型与目录

| type | 目录 | 一张卡 = 什么 |
|---|---|---|
| `concept` | `cards/concepts/` | 一个概念的**自足说明**：定义、要点、公式、相关定理 |
| `deriv` | `cards/derivations/` | 一个论证单元的**推理链**：目标、设置、步骤、缺口 |
| `correction` | `cards/corrections/` | 原文一处**笔误**：原文写法、应作什么、为什么 |

id 形如 `functoriality/concept/<slug>`、`functoriality/deriv/<slug>`、
`functoriality/correction/<slug>`；slug 只含小写字母、数字与连字符。

## 轨道（track）

| track | 内容 |
|---|---|
| `A` | 第 1–2 章：辛流形、Floer 上同调、Fukaya A∞-范畴、操作子原理、反常 |
| `B` | 第 3 章：凝聚层对应、MWW 函子、拼接 Floer、Φ#、双模、伴随、约化、延拓映射 |
| `C` | 第 4 章：巫曲线与巫球模空间、相对 2-操作子、辛 (A∞,2)-范畴 Symp |
| `D` | 第 5 章：Dehn 扭转、Khovanov 同调、Floer 场论、HMS、G-流形、形式群、Barr–Beck |
| `O` | 术语与总览 |

## 通用字段（三类卡都有）

| 字段 | 类型 | 约束 |
|---|---|---|
| `id` | str | 与路径、文件名一致；全局唯一 |
| `type` | str | `concept` / `deriv` / `correction`，须与目录一致 |
| `track` | str | `A`–`D` / `O` |
| `title` | str | 中文术语（首次可带括号英文） |
| `aliases` | list[str] | 非空；英文原名、异名（如 `["symplectic manifold"]`） |
| `summary` | str | ≤120 汉字（去掉 `$...$` 与空白后计），一句话说清这张卡在讲什么 |
| `question` | str | 以 `？` 或 `?` 结尾，是这张卡回答的问题 |
| `pitfalls` | list[str] | ≥1（lint 只查存在，写作要求 ≥2）；常见误解或易错点，须具体（不写「容易混淆」这类空话） |
| `related` | list[str] | ≥2 条，全库存在的卡 id |
| `sources` | list[obj] | ≥1 条，见下 |
| `rights` | str | 固定 `"rewritten"` |
| `status` | str | `draft` / `reviewed` / `published` |
| `provenance_note` | str | 记来源页与去向，如「原书 p.29–31 §3.6；公式取自中译本 chapter3.tex」 |

`sources` 每一项：

```json
{"book": "Abouzaid & Bottman, Functoriality in categorical symplectic geometry (arXiv:2210.11159v1)",
 "section": "§3.6",
 "pages": [29, 31],
 "anchor": "原书 p.29–31 §3.6"}
```

- `pages` 为两个递增整数，落在所引节的页区间内（见 `tools/audit_pages.py` 的内置映射）。
- `anchor` 以 `原书 p.` 开头，页码须在 `pages` 内。

## 交换图（`diagrams`，概念卡与推导卡可选）

本论文的骨架大量靠交换图表达（函子、双模、伴随、操作子复合）。**凡是原文用交换图
讲清的一步，卡里必须把图也画出来**：只写文字的「复合满足结合律」读者无法复核。
图用 tikz-cd 自足书写（不用 `\input`、不引用外部文件），核对时编译通过才算数。

| 字段 | 类型 | 约束 |
|---|---|---|
| `diagrams` | list[obj] | 可选，≤4 张；每项见下 |

每张图：

```json
{"title": "Φ_L 与复合相容（同伦意义）",
 "tikz": "\\begin{tikzcd}[column sep=large]…\\end{tikzcd}",
 "note": "可选：图中符号读法与原文位置的对应"}
```

- `title` ≤40 字，说明这张图在证什么；`tikz` 必须含 `\begin{tikzcd}` 或 `\begin{tikzpicture}` 且环境闭合，不得含 `%`、`$$`、`equation` 环境。
- 只用 `amsmath` / `amssymb` / `tikz-cd` 的命令，外加 `tools/check_diagrams.py` preamble 预定义的记号宏（`\Fuk \HF \SH \SC \HH \QC \QH \MC \Ainf \wt \ol \pt \op \bC \bR \bZ \bP \CP`）。其它算子名一律写字面（`\operatorname{CF}`、`\operatorname{Ch}`、`\operatorname{Mod}`），**不要自造宏**：check_diagrams 不认得的宏会直接编译失败。`\hom` 由 amsmath 提供，可直接用；`\Hom` 请写 `\operatorname{Hom}`。
- 图必须与中译本的图或英文原文的 `tikzcd` 一致（可简化排版，不得改数学内容）；内容对不上就不画，写进 `gaps`。
- `python tools/check_diagrams.py cards --png` 编译全部图并渲染 `md/diagrams/*.png`。

## 概念卡（concept）专有

| 字段 | 类型 | 约束 |
|---|---|---|
| `definition` | obj | `{text, notation}`：text 是完整定义（可含 `$$...$$`），notation 写记号约定 |
| `key_points` | list[str] | ≥3 条；每条一句，讲这条定义「为什么这样定」或「用在哪」 |
| `formulas` | list[str] | ≥1 条 LaTeX 公式；**必须逐字取自中译本对应章的 .tex 源码**（`tools/check_formulas.py` 会做子串核对） |
| `theorems` | list[obj] | 相关定理，见下；可为空列表 |

`theorems` 每一项：

```json
{"name": "MWW 复合定理",
 "statement": "……（中文陈述，可含公式）",
 "proof": {"status": "sketch", "steps": [{"no": 1, "text": "……", "why": "……"}], "gap_note": "原文未给证明，仅引 [WW15]"},
 "source": "原书 p.21 §3.3"}
```

- `proof.status`：`complete`（原文给了完整证明）/ `sketch`（原文给思路或我们补的骨架）/
  `none`（原文只陈述）。`none` 时 `steps` 为空列表，`gap_note` 必须说明缺口在哪。
- `complete` 仅在原文确实给出完整证明时使用；本论文是综述，多数应标 `sketch` 或 `none`。

## 推导卡（deriv）专有

| 字段 | 类型 | 约束 |
|---|---|---|
| `goal` | str | 要证/要构造什么，一句话 |
| `setup` | list[str] | ≥1 条：假设、记号、前提卡 |
| `steps` | list[obj] | ≥3 步，见下 |
| `result` | str | 结论（含公式） |
| `gaps` | list[str] | ≥1 条：原文省略的步骤、我们补的中间步、未解决处 |

`steps` 每一步：

```json
{"no": 1, "text": "……", "why": "为什么这一步成立/为什么要这样做",
 "locator": "原书 p.29", "provenance": "A"}
```

- `locator` 以「原书 p.」开头。
- `provenance`：`A` 原文明写；`B` 由原文补出的中间步；`C` 我们的判断（须在 `why` 里说明依据）。

## 勘误卡（correction）专有

| 字段 | 类型 | 约束 |
|---|---|---|
| `page` | int | 原文页码 1–68 |
| `original` | str | 原文写法（≤60 字，只留可辨认差异的片段） |
| `corrected` | str | 应作什么（≤60 字） |
| `why` | str | 依据：上下文/数学事实/文献；不得写「更通顺」 |
| `note` | str | 中译本如何处理（保留原文＋译注） |

## 校验

```sh
python tools/lint_cards.py cards --strict      # 字段与结构
python tools/audit_pages.py cards              # 页锚与节区间
python tools/check_formulas.py cards --corpus <中译本 chapter*.tex>   # 公式子串回查
python tools/check_diagrams.py cards --png                          # 交换图编译 + 渲染 PNG
python tools/build_index.py                    # 生成 index.jsonl
python tools/render_md.py                      # 生成 md/
```

## 权利

全部卡 `rights: "rewritten"`：中文表述、推理链、易错点与页锚均为自述重写，
不复制原文段落，不复制原图；单个术语原文引用不超过必要长度。
可随数据集以 CC BY 4.0 发布。
