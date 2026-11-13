# 工程/QA 报告（task-23）

角色：tr-qa（工程与 QA）。底本：arXiv:1312.2684**v2**（PDF 194 页；源码 `1312.2684v2_src/dummies5.tex` + `dummies5.bbl`）。
报告时间：2026-11-05 09:50 左右（**项目在并行编辑中**，以下数字为当时快照；最终以 Lead 全量编译后的 Gate 为准）。

---

## 0. 结论摘要

1. **BRIEF §2 的 7 条「已知缺口」全部是计数假象**：那些 731/123/58/142 是**含注释掉内容**（`%…` 与 `\if0…\fi`）的原始计数。
   把 v2 原文与草稿都按「剥 `%` 注释 + 删 `\if0` 块」重算后，16 个块逐块完全一致（见 §1），**不需要补任何公式/图/label/小节/引用**。
   最强的独立证据：原 PDF 与草稿 PDF 的公式编号去重总数 **793 vs 793**，且逐节分布完全相同（§1.3）。
2. 附录 A/B：结构、公式、图表、脚注、引用全部与原文一致；仅做中文标点修正 5 处、误译 1 处（单键→单链），
   并按 STYLE_GUIDE §5 补 2 条 Tutor Note（原文笔误）。B 块「少 2 条方程」实为 `\if0` 块内容，原文 PDF 不排版。
3. 参考文献 `references.tex` 与 v2 `dummies5.bbl`：**123 vs 123 条、键序完全一致、逐条内容归一化后 100% 相同**，无需改动；
   `\cite` 键集合与原文完全一致（135 条命令 / 180 个键 / 123 唯一）。
4. 索引：201 处 `\index` ⇄ 201 条 `.idx` 条目；180 唯一键与 `index-terms.json` 完全对应；makeindex
   **201 entries accepted, 0 rejected, 0 warnings**；`.ind` 180 项、201 个页码引用，页码范围 7–149，无重复。
5. 5 个 Gate 工具全部就绪并实测（§5）：`check.py`、`verify_pdf.py`、`cite_diff.py`、`gen_notes.py`、`pack.py`；
   另有 `work/tmp/build_qa.ps1`（独立镜像 `n2qa`，不碰 Lead 的 `n2build` 与项目根 `main.pdf`）。
6. 待 Lead 处理：`check.py` 目前仅剩 **半角标点残留**（中文句号 `.` 未全角化；A/B 已清零，其余 10 个 sections 文件
   共约 108 处，`final_punct.py --apply` 可批量处理）；`glossary.tsv` 的「驯服穿孔」与正文 19 处「驯性穿孔」不一致；
   `10-argyres-douglas.tex:269` 也有「单键李群」（应「单链」）。见 §6。

---

## 1. 结构对照（全 16 块，剥注释 + 删 `\if0` 后）

### 1.1 方法
- 原文：`work/ref/<块>-en.tex`（v2 切分）→ 去掉 `%` 行内/行尾注释，删除 `\if0 … \fi` 块；
- 草稿：`sections/<块>.tex` → 去掉 `%` 注释；
- 统计 `\section/\subsection/equation/align/multline/figure/table/\footnote/\cite/\label`，并比较 `\cite` 键集合、`\label` 集合。

### 1.2 总计（原文 true vs 草稿 true）

| 对象 | 原文 | 草稿 |
|---|---|---|
| `\section` | 16 | 16 |
| `\subsection` | 57 | 57 |
| `equation` 环境 | 725 | 725 |
| `align` 环境 | 24 | 24 |
| `multline` | 8 | 8 |
| `figure` | 122 | 122 |
| `table` | 3 | 3 |
| `\footnote` | 18 | 18 |
| `\cite` 命令 | 135 | 135 |
| `\cite` 键（次/唯一） | 180 / 123 | 180 / 123（集合差 0） |
| `\label` 集合 | 389 | 389（缺失 0 / 多余 0） |

逐块明细（eq/al/ml/fig/tab/fn）也全部相等，例如：
`09-gaiotto 74/2/0/18/0/2`、`12-su-n-duality 73/1/32/0/1`、`A-instantons 35/3/1/2/0/0`、`B-theory-zoo 16/0/0/0/1/1`。

### 1.3 PDF 层独立复核（原 PDF vs QA 编译的草稿 PDF）

| 指标 | 原 PDF（194 页） | 草稿 PDF（162 页） |
|---|---|---|
| 公式编号去重总数 `(x.y.z)`+`(A.n.m)` | **793** | **793** |
| 逐节分布 | 1:58, 2:65, 3:54, 4:74, 5:37, 6:40, 7:47, 8:41, 9:82, 10:48, 11:109, 12:79, A:43, B:16 | **完全相同** |
| 图（唯一图号） | 122 | 122 |
| 表 | 3 | 3 |
| 参考文献条目 | 123（[1]–[123]） | 123 |

### 1.4 BRIEF §2 七项裁定

| # | BRIEF 说法 | 实际 | 结论 |
|---|---|---|---|
| 1 | 12-su-n-duality 缺 `fig:f-term-relation` 图 | v2 源码第 5834–5839 行整段 `%` 注释；v2 PDF 也无此图 | **不是缺口，不要补** |
| 2 | 09-gaiotto 缺 `\label{++++}` | v2 源码 grep 0 命中（该 label 不存在） | **不要补** |
| 3 | 12-su-n-duality equation 76→73、figure 33→32 | 剥注释后原文就是 73 / 32，草稿 73 / 32 | **无缺口** |
| 4 | B-theory-zoo equation 18→16 | 18 含 `\if0`（v2 6414–6430 行）里的 2 个 equation + 1 个 multline；`\if0` 恒假 | **无缺口（16 正确）** |
| 5 | 09-gaiotto equation 75→74 | 剥注释后原文 74，草稿 74 | **无缺口** |
| 6 | `\cite` 142→135 少 7 处 | 142 含注释里的 7 处 `\cite`；剥注释后原文 135 = 草稿 135，键集合完全一致 | **无缺口** |
| 7 | `\subsection` 58→57 少 1 | v2 第 495 行 `%\subsection{The Witten effect…}` 本被注释；剥注释后 57 = 57 | **无缺口** |

> 建议：`work/probe/structdiff.md` 与 `work/tools/audit.py` 的计数基准改为「剥注释 + 删 `\if0`」，
> 否则会持续误报；`audit.py` 目前只删整行注释，行内 `%` 与 `\if0` 仍会计入。

---

## 2. 附录 A/B 校对

### 2.1 结构/公式
- **A-instantons**（原 pp.173–180）：39 个数学环境（35 equation + 3 align + 1 multline）与原文**按 label 和顺序一一对应**；
  2 图（`fig:omega`、`fig:armleg`）、0 脚注，label 集合一致。
- **B-theory-zoo**（pp.180–194）：16 个 equation、1 table（`tab:ADEeq`）、1 脚注，与原文 typeset 内容一致；
  原文 `\if0` 的 “Second class of examples” 段（2 equation + 1 multline）按原 PDF 正确省略。

### 2.2 公式逐条比对
去掉空白/花括号等纯格式差异后逐条比较：A/B 全部公式**无实质差异**（差异仅为 `\frac1` vs `\frac{1}`、`\quad` vs `\qquad`、
句末句点、以及 B 中一处单行公式改写为 `aligned` 的等价形式）。原文笔误照排（见 §2.4）。

### 2.3 段落/内容
逐段对照 `work/ref/A-instantons-en.tex`、`B-theory-zoo-en.tex` 通读全文：
- A：24 个正文段落 = 原文 24 个（2 个独立 figure 段落在译文中并入上下文，内容不丢）；
- B：30 个正文段落 = 原文前 30 段（原文另有 `\if0` 段与 `\bibliographystyle` 等非正文块，正确省略）；
- 未发现漏段、漏句或增译；术语与上下文一致。

### 2.4 本次对 A/B 的改动（均在授权范围内）
1. `A-instantons.tex` 图 A.1 图注「示意图.」→「示意图。」
2. `A-instantons.tex` 图 A.2 图注「数目.」→「数目。」
3. `B-theory-zoo.tex` 脚注「本节.」→「本节。」
4. `B-theory-zoo.tex` 首段「分散在不同位置.」→「分散在不同位置。」
5. `B-theory-zoo.tex` 表 B.1 表题「三变量方程表示.」→「三变量方程表示。」
6. `B-theory-zoo.tex` 表 B.1 表题「单键李群」→「**单链**李群」（simply-laced 误译；`10-argyres-douglas.tex:269` 有同样问题，属 tr-06 文件，未越权修改）
7. 新增 Tutor Note（原文笔误，正文照排）：
   - A 式 (A.2.13)（p.178）：原文第二个分量印作 $\epsilon_{i\beta\epsilon_2}z_2$，按对称性应为 $e^{i\beta\epsilon_2}z_2$；
   - A p.178：「These data are sufficient to compute $Z_2$」——本段是 $k=1$（单瞬子），按上下文应为 $Z_1$。
   两处均已写 `% [Tutor Note: …]`，`gen_notes.py` 已收录。

> 注：A/B 中另有原文本身的不平衡括号等笔误，因不影响语义且译文已自然处理，未额外加注。

---

## 3. 参考文献核对（references.tex vs v2 dummies5.bbl）

- 条目数：**123 vs 123**；`\bibitem` 键序列**完全一致**（0 缺失、0 多余、0 错序）。
- 内容：逐条按 `\bibitem` 对齐，归一化（去空白/花括号、忽略 URL）后**全部相同**（最小相似度 1.000）；
  作者、标题、期刊/卷/页、arXiv 号、DOI 链接均一致。
- 编号：`thebibliography{100}` 按序生成 [1]–[123]；原 PDF 与草稿 PDF 文本均为 123 个连续编号，无缺号。
- `\cite`：`cite_diff.py` 按 16 块比较，命令数 135/135，键集合差 0；全文 180 个键、123 唯一；
  无未定义 cite，无未被引用的 bibitem。**结论：references.tex 无需改动**。

---

## 4. 索引核对

| 检查 | 结果 |
|---|---|
| 正文 `\index{}` | 201 处（16 个文件） |
| `main.idx` | 201 条 entry，180 个唯一键；与正文一一对应 |
| `index-terms.json` | 180 键；180 个正文键全部登记；json 无未用键 |
| 格式 | 全部为 `Key@中文|hyperpage`（201/201） |
| makeindex（`index.ist`） | **201 entries accepted, 0 rejected, 0 warnings**；1736 comparisons |
| `main.ind` | 180 个 `\item`、201 个页码引用，302 行；页码范围 7–149（均 < 全书 162 页） |
| 重复 | 无 (entry,page) 重复；`\index` 中嵌 `$…{=}…$` 等花括号已用平衡括号解析，无截断 |

> 提示：个别 `\index` 参数内含数学花括号（如 `NFourTheory@$\cN{=}4$ 理论`），简单正则 `\{([^}]*)\}` 会截断；
> 本报告工具（`check.py`/探针）已改为平衡括号解析。

---

## 5. 工具与运行结果（work/tools/）

### 5.1 `check.py`（Gate 1 静态检查，返回码非 0 = FAIL）
检查：UTF-8/BOM/U+FFFD/CRLF、花括号、`\begin/\end` 配对、`$` 奇偶、markdown 残留、中文语境半角标点、
`\label` 重复、`\ref/\eqref` 未定义目标、`\cite` 未定义/未引用、`\index` 未登记、逐文件统计。
当前快照：**FAIL（ERROR 108，WARN 0）**——ERROR 全部是**中文句号仍是半角 `.`**（A/B 已清零）：
`12-su-n-duality 31、09-gaiotto 18、04-pure-su2 13、06-six-dimensions 13、08-two-three-flavors 12、
11-other-groups 8、10-argyres-douglas 7、01-electromagnetic 3、07-higgs 2、00-introduction 1`（数字随并行编辑变动）。
其它项全部通过：label 389 无重复、372 处 ref 无未定义、cite 180/123 无未定义、bibitem 123 无未引用、index 201/180 全登记。
> 期望 Lead 用 `final_punct.py --apply` 统一收尾后再跑一遍。

### 5.2 `verify_pdf.py`（Gate 3 成品回读）
对 `work/tmp/qa_main.pdf`（162 页）运行：**PASS**。
- 目录 level1/2/3 = 19/57/69（= 期望）
- 公式编号 793/793，逐节 OK；图 122/122（逐节 OK）、表 3、脚注 18（PDF 规则线 15 页）
- 参考文献 123 条无缺号；字体 419 个全部嵌入（仅 `Mathematica3` 无子集前缀，属插图自带 Type1，WARN）
- 无 `??`/未解析引用；抽页渲染：`verify_p002`（目录）、`verify_p140`（附录 A 首页）、`verify_p146`（附录 B 首页）、
  `verify_p018`（最密公式页）、`verify_p152`（参考文献首页）、`verify_p160`（索引页）。
- 期望值常量来自原 PDF 实测（页内注释有出处）。

### 5.3 `cite_diff.py`（按块 cite 键差异）
原文按「剥注释 + 删 `\if0`」、译文按「剥注释」比较；支持 `\cite[..]{a,b}`。
当前：**PASS**（16 块命令数 135/135，键集合差 0）。

### 5.4 `gen_notes.py`
收集 `sections/*.tex` 的 `% [Tutor Note: …]`（跨行合并、按文件排序），输出 `deliverable/译注汇总.md`，支持可选输出路径。
当前快照：**14 条**（`03-renormalization 1、07-higgs 2、08-two-three-flavors 2、09-gaiotto 1、
10-argyres-douglas 3、11-other-groups 2、A-instantons 2`，其余 0；随并行编辑增加）。

### 5.5 `pack.py`
打包 `deliverable/`：PDF（`N=2超对称动力学入门_中文译注本.pdf`）、`src/`（main/preamble/macros/references/
young-kugo.sty/index.ist/index-terms.json/texglyphlist.txt/sections/figures/build.ps1）、`compile.log`、
`译注汇总.md`、`README.md`，并复制 `读书笔记/`（若存在）。支持可选输出目录（自测用）。
已测到 `work/tmp/pack_test`：PASS（PDF 4,773,420 B；src 14 个文件 + 129 个 figures；compile.log、译注汇总、README 均就位）。

### 5.6 `work/tmp/build_qa.ps1`（QA 独立编译）
镜像到 `…\default-workspace\n2qa`（**不碰 Lead 的 n2build、不写项目根 main.pdf**），
执行 xelatex → makeindex → xelatex×2，产物只写 `work/tmp/qa_main.pdf`、`qa_main.log`、`qa_main.idx`、`qa_main.ind`、`qa_makeindex.log`。
最近一次（A/B 修改后）：162 页，`file:line=0 fatal=0 undefined=0 missingchar=0 overfull=0`；makeindex 0 warnings。

---

## 6. 需 Lead 决策 / 后续事项

1. **半角句号收尾**：`check.py` 目前唯一 ERROR 是中文语境半角 `.`（约 108 处，全部在其他 sections 文件）；
   `final_punct.py --apply` 可统一转「。」（A/B 已手工清零）。
2. **术语不一致**：`glossary.tsv` 写「tame puncture = 驯服穿孔」，正文全部用「**驯性**穿孔」（19 处）；
   按 STYLE_GUIDE §4 glossary 冻结，请 Lead 决定更新 glossary 还是改正文（建议 glossary 改为「驯性穿孔」）。
3. **`单键李群` → `单链李群`**：`10-argyres-douglas.tex:269` 有同样误译（tr-06 文件；我不越权修改）。
   建议 Lead 通知 tr-06 或统一修。
4. **BRIEF §2 / structdiff / audit.py 的计数基准**需改为「剥注释 + 删 `\if0`」，否则会继续误报缺口（本报告 §1.4）。
5. **参考工具**：`audit.py` 的 `strip_comments` 只删整行注释、不处理行内 `%` 与 `\if0`，且 `labels()` 用 `[^}]+` 正则，
   对含花括号的 `\index` 也会截断——建议由 Lead 决定是否删除/替换为 `check.py + cite_diff.py`。
6. A/B 的 2 条 Tutor Note 属新增内容，`gen_notes.py` 已收录；若 Lead 认为原文笔误无需加注，可删（不影响编译）。

---

## 7. 交付物清单

- `work/tools/check.py`、`verify_pdf.py`、`cite_diff.py`、`gen_notes.py`、`pack.py`、`final_gate.py`、`README.md`
- `work/tmp/build_qa.ps1`（QA 独立编译脚本，支持 `-Src` 指定任意源码树）
- 校对修改：`sections/A-instantons.tex`、`sections/B-theory-zoo.tex`（§2.4）
- `deliverable/译注汇总.md`（gen_notes 生成，最终 32 条）
- `deliverable/核对清单.md`（最终版，含一键 Gate + 独立重建对照）
- 本报告 `work/review/qa.md`

---

## 8. 最终 Gate 结果（2026-11-05 10:22，全稿校对完成后）

Lead 完成全局收尾（final_punct apply、驯性→驯服穿孔、θ/β 术语、glossary 回写）并重编译后，
`work/tools/final_gate.py` 一键核对 **全绿**：

| 步骤 | 结果 | 关键输出 |
|---|---|---|
| Gate 1 `check.py` | ✅ PASS | ERROR 0 / WARN 0 |
| Gate 3 `verify_pdf.py` | ✅ PASS | 162 页；公式 793 逐节 OK；图 122、表 3、脚注 18、文献 123、字体全嵌入、无 `??` |
| `cite_diff.py` | ✅ PASS | 缺失 0 / 多余 0（135/135） |
| `gen_notes.py` | ✅ PASS | 32 条 → `deliverable/译注汇总.md` |
| `pack.py` | ✅ PASS | pack OK |

`check.py` 末轮收尾的两处修正（均为工具准确性，非正文改动）：
1. `strip_math()` 的环境正则缺少分组（`\begin\{(?:…)`），导致含 `\text{…}` 的公式未被整体屏蔽而误报；
   已修正。剩余 2 处「中文半角句点」经核实位于 equation 的 `\text{…}` 内，按「数学环境内用英文标点」
   口径属正确写法，不再报错。
2. 增加白名单：`\label{***}` / `\eqref{***}`（原文标签）不误报 markdown `**`；`Teichm\"uller` 的 `"` 为
   LaTeX 变音符（工具不做英文引号检查）。

**独立重建对照**：只用交付包 `deliverable/src/` 在独立镜像 `n2qa` 重编译（不覆盖项目根 `main.pdf`），
`file:line=0 / fatal=0 / undefined=0 / missingchar=0 / overfull=0`，makeindex 0 warnings；
与项目根 `main.pdf` 对比：页数 162=162、公式编号 793=793 且逐节相同、图 122=122（逐节相同）、表 3=3、
脚注规则线 15=15（源 18 条）、参考文献 123=123、目录 19/57/69、字体 419 个全嵌入，
**逐页文本 162/162 页完全一致**。详见 `deliverable/核对清单.md` §五 与 `work/tmp/qa_deliv_compare.log`。

> §6 的 1–3 项已由 Lead 处理完毕（final_punct 已 apply；「驯性穿孔」已统一为 glossary 的「驯服穿孔」；
> 10-AD 的「单键李群」由 tr-06 修正）。
