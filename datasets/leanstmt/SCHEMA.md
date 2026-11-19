# leanstmt 卡 schema（v0.2）

一卡一 JSON，UTF-8、缩进 2 空格、`ensure_ascii=false`；字段顺序不强制，但下列字段必须有。

| 字段 | 类型 | 约束 |
| --- | --- | --- |
| `id` | string | `leanstmt/witten2015-<key>` 或 `leanstmt/witten2008-<key>`，`<key>` 小写字母数字，全包唯一 |
| `type` | string | 固定 `"statement"` |
| `title` | string | 中文短标题，≤ 40 字 |
| `track` | string | `W15`（Witten 2015）/ `W08`（Witten 2008）；后续论文加新标签 |
| `source.paper` | string | 原题名 |
| `source.arxiv` | string | `arXiv:<id>v<版>`，版次必须写明 |
| `source.section` | string | 原文节号，如 `2.6.6`、`5` |
| `source.pages` | [int,int] | **印刷页**区间闭区间。Witten 2015：印刷页 = PDF 页 − 1；Witten 2008：印刷页 = PDF 页 |
| `source.anchor` | string | 更细的锚（式号/定理名/段落），不许写「见正文」 |
| `natural_language.zh` | string | 译文的陈述句（一至两句，量词与假设写全） |
| `natural_language.en` | string | 英文原文的紧缩版（≤ 200 字符，只作对照） |
| `lean.file` | string | 相对本包根的 Lean 文件路径 |
| `lean.name` | string | 全限定声明名（`Namespace.name`），必须能在 `lean.file` 里 grep 到 |
| `lean.statement` | string | Lean 语句源码（可含换行），必须与文件中声明一致 |
| `lean.imports` | [string] | 该文件实际 import 的模块名（`Mathlib.X.Y`） |
| `dependencies[]` | [{name,module,kind}] | 用到的 mathlib/自有引理；`kind ∈ {mathlib,local}`；gap 卡可为空 |
| `hypotheses` | [string] | Lean 语句里显式/隐式假设的中文说明（空数组表示无） |
| `scope` | string | `discrete-core` / `algebraic-core` / `arithmetic-core` / `gap` |
| `backtranslation.zh` | string | 只读 Lean 语句写出的回译（不看中文陈述） |
| `backtranslation.method` | string | 固定 `"blind-backtranslation"` |
| `backtranslation.reviewer` | string | 回译者标识（`subagent`/人名）；写卡人不得同时是回译者 |
| `verification.status` | string | `certified`（0 error、`sorry_count=0`）或 `gap`（有 `sorry`） |
| `verification.toolchain` | string | `lean-toolchain` 内容 |
| `verification.mathlib_rev` | string | `lake-manifest.json` 里 mathlib 的 `rev`（40 位） |
| `verification.checked_at` | string | `YYYY-MM-DD` |
| `verification.checker` | string | 检查方式（如 `lake env lean（逐文件）`） |
| `verification.sorry_count` | int | 该声明所在文件里**本声明**引入的 `sorry` 数 |
| `gaps[]` | [{reason,blocked_by}] | `scope="gap"` 时至少 1 条；否则空数组 |
| `notes` | string | 写卡人备注：这一步形式化了什么、没形式化什么 |
| `rights` | string | 固定 `"rewritten"` |
| `status` | string | `draft` / `dev`（禁 `prod`/`train`） |

## 硬性纪律

1. **不虚标**：`verification.status` 只能由 `tools/check_lean.py --run` 的实测结果决定。
2. **不掺沙**：`lean.statement` 与源文件必须逐字一致（lint 会做归一化比对）。
3. **不越界**：只转写原文已有的陈述；不替作者补新命题、不改假设强弱；改写假设必须在
   `hypotheses` 与 `notes` 里写明「与原文的差异」。
4. **不留假名**：`dependencies` 里出现的一切名字，必须能用 `#check` 或 `lake env lean` 复现；
   查不到就删，不许写「大概在 mathlib 里」。
5. **缺口照登**：做不到的陈述不删，写 `gap` 卡并把缺什么写清楚；缺口卡数量按论文统计。
