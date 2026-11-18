# 资料卡 JSON 规范（kshms v1）

底本：M. Kontsevich, Y. Soibelman《Homological mirror symmetry and torus fibrations》，
arXiv:math/0011041v2 [math.SG]（2001-06-04），66 页 letter 单栏，无摘要；
正文 9 节（§9 为附录），参考文献 34 条。

卡片依据**中文译注本**（`08_source_code/SY01-25_同调镜像对称与环面纤维化/`，57 页，
含 47 条译注、213 条术语、10 条勘误、7 条存疑）逐条抽取，不复述英文原文段落。

## 0. 与书籍数据集的两点不同

1. **编号照抄原文，不重编号**。原文明细：定义 1–23、定理 1–4、命题 1–15、引理 1–3、
   推论 1、猜想 1–5、注 1–22，每类各自连续、**不带节号**。「§6.3 中的定理」指 §6.3 一节里的定理，
   不是「定理 6.3」。卡片的 `kind_no` 直接写原文编号。
2. **注（Remark）单独成卡**。论文里 22 条 Remark 承载了相当一部分技术约定（如 注 19 的
   $\tilde{\mathcal{O}}'_Y$、注 21 的截断 theta 级数），不能并进相邻定理卡；一律进 `cards/remarks/`。

一卡一 JSON，UTF-8，缩进 2 空格，`ensure_ascii=False`，文件名 = id 最后一段。

- 概念卡 `cards/concepts/`，id `kshms/concept/<slug>`
- 注卡 `cards/remarks/`，id `kshms/remark/<slug>`
- 勘误卡 `cards/corrections/`，id `kshms/correction/<slug>`

`slug` 小写、连字符分隔、以类型前缀开头，便于扫读：`dfn-03-nonunital-a-inf-algebra`、
`thm-04-abelian-hms`、`prp-05-fukaya-oh`、`rmk-19-oy-tilde`、`corr-p01-h2-xv`。

## 1. 轨道（track）

| track | 名称 | 覆盖 | 卡片主要回答什么 |
| --- | --- | --- | --- |
| `O` | 纲领与阅读 | §1、§1.2 | 这篇文章要做什么、结论哪些已证哪些是猜想、怎么读 |
| `A` | CFT 与几何退化 | §2、§3 | CFT 模空间紧化的边界分层、A/B/T 分层、极大退化、Monge–Ampère 流形、整仿射结构 |
| `B` | $A_\infty$ 形式框架 | §4 | 非幺 $A_\infty$-代数/范畴、横截序列、$A_\infty$-预范畴、有向预范畴 |
| `C` | Fukaya 与退化 | §5 | Fukaya 范畴、$C((q))$ 上的 $A_\infty$-结构、Fukaya–Oh 范畴、权重与平面树 |
| `D` | Morse 机器 | §6 | Morse–Smale 复形、Morse/de Rham 两种 $A_\infty$-范畴、同调扰动、投影算子与同伦 |
| `E` | 刚性解析与凝聚层 | §7 | $Y^{an}$、Berkovich 谱、$\mathcal{C}(Y)$、$O'_Y$、命题 9–10 的解析化 |
| `F` | 同调镜像猜想 | §8 | 对象上的函子、谱与半群 $\varphi^t/\psi^t$、阿贝尔簇情形定理 4 |
| `G` | 复情形附录 | §9 | $\varepsilon$ 固定时如何重做、Dolbeault 扇区、Poincaré 丛、半群 $\varphi^t$ |

## 2. 概念卡必填字段

| 字段 | 类型 | 约束 |
| --- | --- | --- |
| `id` | string | `kshms/concept/<slug>` |
| `type` | string | `"concept"` |
| `track` | string | `O A B C D E F G` 之一 |
| `kind` | string | `定义` / `定理` / `命题` / `引理` / `推论` / `猜想` |
| `kind_no` | integer | 原文该类编号 |
| `title` | string | 中文标题，可含行内公式 |
| `aliases` | string[] | ≥2，原文英文名 + 通行别名/译名 |
| `summary` | string | ≤120 汉字（去公式与空白后计数），一句话说清「是什么/为什么重要」 |
| `question` | string | 一句话，以 `？` 结尾 |
| `statement` | string | 该条的**完整中文陈述**（照译本，可含 `$...$` / `$$...$$`） |
| `notation` | string | 记号约定；没有就空字符串 |
| `key_points` | string[] | ≥2，每条一个独立断言 |
| `formulas` | string[] | 关键公式（不带 `$`，渲染时补 `$$`） |
| `proof` | object | `{status: "complete"\|"sketch"\|"none", steps: [{no,text,why}], gap_note}` |
| `pitfalls` | string[] | ≥1，真正的易错点 |
| `related` | string[] | ≥1，解析到本库 `id` |
| `sources` | object[] | ≥1，见 §4 |
| `rights` | string | 固定 `"rewritten"` |
| `status` | string | `draft` / `reviewed` / `published` |
| `provenance_note` | string | 页码与译注依据，一句话 |

`proof.status`：原文给出完整证明写 `complete`（`steps` 至少 2 步）；只给思路、或引用他文写
`sketch`（`gap_note` 必须点名「缺口是什么、证明在哪」）；纯定义、猜想写 `none`（`steps` 为空数组）。

## 3. 注卡必填字段

`id`（`kshm/remark/...` 写作 `kshms/remark/<slug>`）、`type`、`track`、`kind_no`、`title`、`aliases`、
`summary`、`question`、`statement`（注的完整中文陈述）、`why`（这条注在全文里承担什么，1–3 句）、
`pitfalls`、`related`、`sources`、`rights`、`status`、`provenance_note`。

## 4. sources[] 字段

```json
{"book": "Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25）",
 "section": "§6.3",
 "pages": [40],
 "anchor": "源码/chunks/ch06.tex:120-137（定理 2）"}
```

`pages` 指**原文印刷页**（arXiv 版页码）；`anchor` 指译注本 LaTeX 源码的文件与行区间，
`tools/lint_cards.py` 会逐卡回查行区间是否越界。

## 5. 数学写作规则

1. 行内 `$...$`、行间 `$$...$$`；只用标准宏（`\mathbb`、`\mathcal`、`\operatorname`、`\mathrm`、
   `\frac`、`\otimes`、`\bigoplus`、`\sum`、`\int`），**不得出现译注本的自定义宏**
   （`\Ainf`、`\eps`、`\Cmer`、`\Ceps`、`\Yan`、`\TY`、`\Tstar`、`\dbar`、`\Hom`、`\C`、`\R`、`\Z`
   等一律展开为 `\mathcal{A}_\infty`、`\varepsilon`、`\mathbb{C}` 之类）。
2. 引用原文编号写「定义 3」「命题 9」「注 19」；页码写「p.40」（原文印刷页）。
3. 不做超出原文的推广：不加条件、不加等价、不举原文没有的例子；后续发展（Gross–Siebert 等）
   只能在 `pitfalls` 或 `provenance_note` 里点一句「后续工作不在本文范围」。
4. 中文全角标点；公式内英文标点。
5. 不写「显然」「易见」；每一步为什么成立写进 `why`。
6. 猜想卡必须写清「这是猜想，不是定理」，`proof.status` 一律 `none`。

## 6. 质检

```bash
python tools/lint_cards.py cards --strict   # 字段、编号、anchor、related 解析
python tools/build_index.py                 # 重建 index.jsonl
python tools/render_md.py                   # 重建 md/
```
