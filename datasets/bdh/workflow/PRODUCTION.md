# bdh 资料卡生产说明（给卡片作者）

本文件是 `datasets/bdh/` 的写作手册。写卡前先读 `../SCHEMA.md`（字段与约束的权威来源），
再读一张现成的好卡作范本：`../../gw06/cards/concepts/a-model-fukaya.json`。

## 1. 你要产出什么

每张卡一个 JSON 文件，放在：

- 概念卡：`datasets/bdh/cards/concepts/<slug>.json`
- 勘误卡：`datasets/bdh/cards/corrections/<slug>.json`

`<slug>` 只用小写字母、数字与连字符，全文唯一，与 `id` 最后一段一致。

**不要**手改 `index.jsonl`、`verification.jsonl`、`md/`、`MAP.md`、`taxonomy.md`（都是生成物）。

## 2. 锚点怎么取

`sources[].anchor` 形如：

```
08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch03.tex:214-229
```

- 必须指向仓内中译源码里**真实存在**的行号区间（`1 ≤ a ≤ b ≤ 文件行数`）。
- 用 `read` 工具读 `源码/chapters/chNN.tex` 确认行号；一个连续段落通常就是一行，
  所以 `a-b` 一般跨 1–15 行。
- 锚点区间要**包含**你在卡里断言的文字（定义、命题、公式、那句话）。
- `pages` 填原书**印刷页码**，`pdf_pages` 必须与 `pages` 完全相同（本书 PDF 页 = 印刷页）。
  页码从 `\SourcePage{N}` 标注与页眉确认；不确定就把区间写宽，不要编。

`page_note` 可以写「原书 p.61–62（`\SourcePage` 锚点）」这类口径说明。

## 3. 内容要求（概念卡）

- `summary`：一句话，去掉 `$...$` 后**汉字 ≤ 120**（校验会数）。说清「是什么 + 为什么重要」。
- `question`：以「？」结尾，是真问题（读者会问的那个），不是标题改写。
- `definition.text`：自足——先数学定义，再一句直觉。不写「上文」「如前所述」。
- `definition.notation`：记号约定，逐条列；可空但要尽量写。
- `key_points`：≥ 3 条，每条一个**可检验**的断言（最好带公式号或页号）。
- `formulas`：≥ 1 条，LaTeX **不带 `$`**。
- `pitfalls`：≥ 2 条，具体到「写错会得到什么错结论」。
- `annotations`：≥ 1 条，`type` 只能是 `易错预警` / `含糊点拨` / `背景直觉`，
  每条 `text` ≥ 40 汉字，且要给出**别人不会自己想到**的信息（不是复述定义）。
- `related`：≥ 2 个 id，必须能在本数据集内解析，不能指向自己。
  **为保证并行写作时也能解析，你的 `related` 至少要包含 2 个来自下面「公共枢纽 id」的条目**：
  - `bdh/concept/hitchin-integrable-system`
  - `bdh/concept/twisted-differential-operators`
  - `bdh/concept/hecke-eigensheaf`
  - `bdh/concept/oper`
  - `bdh/concept/langlands-dual`
  另外可以再指向你自己写的卡（同一批里可互相引用）。
- `status`：`reviewed`；`verification.status`：`source-only`；
  `verification.checked_on`：`2026-11-21`；
  `verification.checks`：逐条写你**真的做了**什么，例如
  「逐行对照 源码/chapters/ch03.tex:214-229」「公式 (45) 与原文 p.63 页面图像核对」「术语按 工程文件/work/术语表.md」。

## 4. 内容要求（勘误卡）

- `location`：节号 + `sXX.tex:行号`，例如 `§3.1 s03.tex:214`。
- `original` / `corrected`：只保留**差异片段**，不要整段复制译文；两者必须不同。
- `why`：必须给依据（原文英文、上下文、数学自洽、公式号、术语表），不得写「更通顺」。
- `note`：写核验边界。若属「原文笔误判定」（译文照录、只加译注），
  `note` 开头必须先写「译文未改，照原文保留」。
- 同样是 `sources` + `anchor`，锚点区间要**包含** `original` 那一段。

## 5. 术语

一律按 `工程文件/work/术语表.md`：stack 栈、symbol 象征、holonomic 完整、
critically twisted 临界扭、Hecke eigensheaf Hecke 特征层、oper 不译、torsor 不译（首现括注）。
数学符号写 LaTeX 命令（`\mathcal{D}`、`\mathfrak{g}`、`\operatorname{Bun}`），不要用 Unicode 数学字符。

## 6. 自检

写完后在 `datasets/bdh/` 目录跑：

```bash
"C:\Users\admin\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\python\python.exe" -X utf8 tools/make_cards.py --check
```

它只会读，不会改你的卡（生成物写入是另一条命令）。报错就改到你自己那几张卡通过；
若报的是**别人**的卡，忽略并在交付说明里提一句。

## 7. 纪律

- 只写 `cards/concepts/` 或 `cards/corrections/` 下属于你的文件；不动 `源码/`、不动别人的卡。
- 不写本机绝对路径；不写「本数据集」「本卡」这类自我指涉。
- 英文短引 ≤ 120 字符。
- 诚实：没核对 PDF 页面图就写「仅对照中译源码」。
