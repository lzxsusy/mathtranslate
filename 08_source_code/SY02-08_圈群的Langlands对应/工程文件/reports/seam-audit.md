# 接缝连续性审计报告（seam-audit）

- 审计对象：按 main.tex 输入顺序的全部章节片段（ch01-1 → ch01-2 → ch02 → ch03-1 → ch03-2 → ch04 → ch05-1 → ch05-2 → ch06 → ch07 → ch08 → ch09-1 → ch09-2 → ch10-1 → ch10-2 → ch10-3 → ch10-4 → appendix → glossary → bibliography）。
- 审计时间：2026-10-28 16:15–16:24（**快照**，结论以 16:24 状态为准）。审计期间工作区持续并发写入：`ch06.tex` 于 16:18:14 才出现（此前缺失）、`ch09-2.tex` 于 16:17:24 更新；**16:21:52 发生一次全库批量写入**（几乎全部 tex 被同时 touch），**16:22:59–16:23:30 又有 ch01-2/ch06/ch09-2/ch10-1/ch10-3/glossary 等再次更新**。我在每次写入之后都重取了各缝的关键首尾段；seam 12 的现状在 16:24 复核（其"重复半句"在审计期间被并发修复，但仍余"跨段断句"）。**正式定稿后建议对 08、09、12、13 四缝再跑一次本法**。
- 方法（对每个接缝）：
  1. 取上一文件末尾 3–4 段（去注释、按空行切段）与下一文件开头 3–4 段；
  2. 取原书 PDF 上一单元末页 pX 与下一单元首页 pX+1 的图像（下 40%＋上 40% 拼图）核对版式与断页；
  3. 取 `text/pX.txt` 末 6 行与 `text/pX+1.txt` 首 6 行，逐句比对译文首尾是否与原文页边界一一对应（判断漏段/重复）；
  4. 全书级检查：用"栈"扫描（剔除注释行）所有 `\begin`/`\end` 环境配对；在临时目录整书编译 main.tex（不改 tex）。
- **只写报告，未修改任何 tex**；所有中间产物（拼图、编译输出）均在系统临时目录。

## 总体结论

- 原书 17 个接缝中：**16 个通过**（其中 4 个已知接缝——01、04、07、16——经 Lead/U15/U17 处理正确；08、09 因 `ch06.tex` 在审计期间补齐而由"缺文件"转为通过）；**1 个残余排版问题**：**接缝 12（ch09-1 → ch09-2，p283/p284）跨段断句**——审计期间（16:22:59）的并发修复已删去原先"重复半句"，但句子仍被**段落边界**切开（ch09-1 以"…中"结束一段、ch09-2 以"的点集…"另起一段），建议合并段落或改写句界（见问题 1，P2）。
- **未发现段落级漏译**：除接缝 12 的"跨段断句"外，其余各缝译文首尾均与源页边界行一一对应，未见漏段、重复段或错位；seam 12 的源文句子本身已完整译出，只是被切在两段之间。
- 新增的 2 个编辑性接缝（appendix → glossary → bibliography，`glossary.tex` 为 Lead 新增、原书无对应页）连接正常；仅需 Lead 确认术语表的编号/位置（见问题 3）。
- 环境检查：全书所有 LaTeX 环境成对（含**跨文件**的 `proof`，见接缝 07）；结束时扫描栈为空。
- 整书编译（临时输出目录，不改 tex）：审计中两次执行——16:20 版 **EXIT=0，0 error，320 页**；16:24 最新版 **EXIT=0，0 error，0 LaTeX Warning，327 页**。首遍曾出现的 4 条 `Reference undefined` 与 1 条 "Label(s) may have changed" 在最新版已消失（疑因 16:22:59 的并发修改中相关 `\ref` 已改为纯文本或标签已建立；如需确认可看 main.log）。**注意**：`ch05-1.tex` 单独 `check.ps1` 必然失败（proof 跨文件未闭合，设计如此），不代表合并稿有问题。

## 逐缝结论表

| # | 接缝 | 原文页（PDF） | 结论 | 说明 |
|---|---|---|---|---|
| 01 | ch01-1 → ch01-2 | p22→p23 | ✅ 通过（Lead 已处理） | ch01-1 末已含 p23 首两句收尾（"…also exists for such curves. The local counterpart…this book."→"…这样的曲线也存在整体 Langlands 对应的一个版本。这一对应的局部对应物，正是本书的主题。"）；ch01-2 直接起 §1.2，无重复、无缺口 |
| 02 | ch01-2 → ch02 | p44→p45 | ✅ 通过 | p44 末段（"…construct the local geometric Langlands correspondence for loop groups."）与 ch01-2 末段对齐；ch02 以 `\begingroup`+`\chapter{顶点代数}` 起，首段与 p45 首段对齐 |
| 03 | ch02 → ch03-1 | p74→p75 | ✅ 通过 | p74 末 OPE 段（"…depends only on the singular terms."）与 ch02 末段对齐；ch03-1 以 `\chapter{构造中心元}` 起；ch02 的 `\begingroup/\endgroup` 成对 |
| 04 | ch03-1 → ch03-2 | p94→p95 | ✅ 通过（已知接缝） | §3.3.4 续文：ch03-1 末"…生成元 $J^a_n$（$n<0$），"与 ch03-2 首"它们就是 $V_{\kappa_c}(\fg)$ 中 $\bar J^a_n|0\rangle$ 的符号…"严格连续；ch03-2 未重复 §3.3.4 前文 |
| 05 | ch03-2 → ch04 | p114→p115 | ✅ 通过 | p114 末（"…where ${}^LG$ is the Langlands dual group to $G$."）与 ch03-2 末段对齐；ch04 章首与 p115 首段对齐 |
| 06 | ch04 → ch05-1 | p139→p140 | ✅ 通过 | p139 末（"…and so $Z(\hat{\mathfrak g})=\C$."）与 ch04 末句"…从而 $Z_\kappa(\hat{\mathfrak{g}})=\mathbb{C}$。`\end{proof}`"对齐；ch05-1 章首与 p140 首段对齐 |
| 07 | ch05-1 → ch05-2 | p153→p154 | ✅ 通过（已知接缝，跨文件 proof） | 句子连续："…由于这些商空间的元素"+"分别由 $\cA^{\fg}$ 与 $\operatorname{Vect}L\cU$ 中元素的有限线性组合表示…"；`proof` 环境在 ch05-1 开启、在 ch05-2 第 16 行 `\end{proof}` 关闭，合并后正常。**遗留**：ch05-2 开头 L7–13 的"合并接缝·请 Lead 处理"注释已过期（见问题 2） |
| 08 | ch05-2 → ch06 | p176→p177 | ✅ 通过（审计期间补齐） | p176 末段"总结本章结果：…下一章我们将在顶点代数语言中解释这个同态。"与 ch05-2 末段对齐；ch06 以 `\begingroup`+`\chapter{Wakimoto 模}` 起，首段与 p177 首段对齐。ch06 于 16:18 出现 |
| 09 | ch06 → ch07 | p208→p209 | ✅ 通过（审计期间补齐） | p208 末句"…Hence $W_{\lambda/t}$ is irreducible. This completes the proof."与 ch06 末"…$W_{\lambda/t}$ 不可约。证毕。`\end{proof}`+"`\endgroup`"对齐；ch07 章首与 p209 首段对齐 |
| 10 | ch07 → ch08 | p231→p232 | ✅ 通过 | p231 末"…generalizes Proposition 7.3.6 to arbitrary dominant integral weights."与 ch07 末段"…该命题把命题 7.3.6 推广到任意整优权。"对齐；ch08 章首与 p232 首段对齐 |
| 11 | ch08 → ch09-1 | p260→p261 | ✅ 通过 | p260 末段（"…intersection of the kernels of the W-algebra screening operators."）与 ch08 末段对齐；ch09-1 章首与 p261 首段对齐 |
| **12** | **ch09-1 → ch09-2** | **p283→p284** | **⚠️ 待修：跨段断句** | 句子内容完整、无重复（重复半句已于审计期间 16:22:59 的并发修复中删除），但 ch09-1 以"…纤维 $\mu^{-1}(\chi)$ 中"结段、ch09-2 以"的点集与 Springer 纤维…"另起一段，合并后段落边界插在句子中间。见"问题 1"（P2） |
| 13 | ch09-2 → ch10-1 | p314→p315 | ✅ 通过（ch09-2 于 16:17 更新后） | p314 末句"…this proves Theorem 9.6.1."与 ch09-2 末段"…这证明了定理 9.6.1。"对齐（16:17 之前的版本曾缺此收尾段，现已补齐）；ch10-1 章首与 p315 首段对齐 |
| 14 | ch10-1 → ch10-2 | p325→p326 | ✅ 通过 | p325 末段与脚注 2 与 ch10-1 末对齐；ch10-2 起 §10.3，正文与 p326 首段对齐（keypoints 为编辑性插入，位于标题之后、正文之前） |
| 15 | ch10-2 → ch10-3 | p347（同页） | ✅ 通过（U15 已补） | ch10-2 末 = Conjecture 10.3.13 含 (10.3-29) 与 p347 上半页一致；ch10-3 从 §10.4 起，无重复、无缺口 |
| 16 | ch10-3 → ch10-4 | p374→p375 | ✅ 通过（U17 已接） | "…即 Miura 变换在正则 oper 处的纤维，"+ p375 首"获得了有用的解释：它正是范畴…的射影化。"严格连续 |
| 17 | ch10-4 → appendix | p388→p389 | ✅ 通过 | p388 末段"…the mysteries of the geometric Langlands correspondence."与 ch10-4 末段对齐；appendix 以 `\chapter{李代数与泛包络代数}` 起（题名问题见问题 3） |
| 18 | appendix → glossary（**新增**） | 原书无对应页（p395 末→p396 标题页之间） | ✅/N.A. | `glossary.tex` 为 Lead 编辑性章节（`\chapter{术语表}`，位于 `\appendix` 下会自动编号"附录 B"），非原书内容；与前后无内容重叠 |
| 19 | glossary → bibliography（**新增**） | p396 | ✅ 通过 | `bibliography.tex` 以 `\chapter*{参考文献}` 起，与 p396 "Bibliography" 对齐；glossary 为插入章节，不影响原书连续性 |

## 问题详情（按优先级）

### 问题 1（P2，建议修）：接缝 12 — ch09-1 → ch09-2，p283/p284 跨段断句

- **源文边界**（p283 末 → p284 首）：
  - p283: `… This implies that the set of points in the fiber μ⁻¹(χ) of the`
  - p284: `Miura transformation μ over χ ∈ Op^{nilp,λ}_G is in bijection with the set of points of the Springer fiber Sp_{Res_λ(χ)} (see (9.3-10)).`
- **当前译文（16:24 状态）**：
  - `ch09-1.tex` 末段结尾：`…与 Miura 变换 $\mu$（见 (9.3-3)）在 $\Op^{\mathrm{nilp},\check\lambda}_G$ 上的限制一致。这意味着，纤维 $\mu^{-1}(\chi)$ 中`（句子在此结束**一段**，末尾无标点）
  - `ch09-2.tex` 开头是**另一段**：`的点集与 Springer 纤维 $\operatorname{Sp}_{\operatorname{Res}_{\check\lambda}(\chi)}$ 的点集一一对应（见 (9.3-10)）。`
- **问题**：句子内容已完整、也无重复（审计期间 16:22:59 的并发修复删掉了旧版"由此推出，Miura 变换…"这一重复半句），但两句分属两段：合并后会读成"……纤维 $\mu^{-1}(\chi)$ 中"〔段落结束、下一段缩进〕"的点集与……"——句子被段落边界切开，排版上会出现一个孤立的"中"收段。
- **修复方案（二选一）**：
  - **方案 A（推荐，改动最小）**：在 `ch09-1.tex` 末尾把该句补全并断句——把"这意味着，纤维 $\mu^{-1}(\chi)$ 中"改为"这意味着，纤维 $\mu^{-1}(\chi)$ 的点集与 Springer 纤维 $\operatorname{Sp}_{\operatorname{Res}_{\check\lambda}(\chi)}$ 的点集一一对应（见 (9.3-10)）。"，同时删除 `ch09-2.tex` 开头那一段"的点集与 Springer 纤维…（见 (9.3-10)）。"。
  - **方案 B**：不合并内容，只合并段落——把 `ch09-2.tex` 开头这一段并入前一段（即在合成稿中去掉两文件之间的空行），使整句成为一段；但跨文件段落合并需要在 main.tex 合成后手工处理，不推荐。
- 说明：此处**无内容缺口**，也无重复，仅需调整句界/段落边界；属排版层问题（P2）。

### 问题 2（P3，清理项）：接缝 07 的过期注释与 ch05-1 单文件编译

- `ch05-2.tex` 第 7–13 行有一条"[合并接缝 · 请 Lead 处理]"注释，指示 (a) 删除 ch05-1 末尾 `\end{proof}`、(b) 删除 `\begin{proof}[证明（续）]`、(c) 保留本证明末尾 `\end{proof}`。经查：**(a)(b) 已实际完成**（ch05-1 已无尾部 `\end{proof}`；ch05-2 已无 `\begin{proof}[证明（续）]`），当前合并状态正确。**建议删除或改写这条过期注释**，以免后续误删。
- `ch05-1.tex` 单独跑 `check.ps1` 会因 proof 未闭合而报错；这是"跨文件 proof"的设计后果，合并稿编译正常（本次整书编译 EXIT=0）。不建议为让单文件可编译而在 ch05-1 末尾补 `\end{proof}`（会破坏合并）。

### 问题 3（P4，编辑性，非内容缺口）：appendix 题名与 glossary 位置

- `appendix.tex` 用 `\chapter{李代数与泛包络代数}`；原书 p389 只印 "Appendix"（无题名），随后直接 A.1。当前写法在正文产生"附录 A 李代数与泛包络代数"，属**编辑性增题**；若严格照原书，可改为 `\chapter{附录}`（或保留但视为译者所拟）。
- `glossary.tex` 用 `\chapter{术语表}` 且位于 `\appendix` 之后，会被编号为"附录 B"并进入目录。若术语表不应算作附录，建议移到 `\backmatter` 之后并改用 `\chapter*{术语表}`。
- `reports/U09.md` 仍缺失（`ch06.tex` 已交付但无对应报告）；建议补一份，便于终审核对 ch06 的覆盖范围与自检结论。

## 复核方法与可重复性

- 本报告结论基于"上文件末 3–4 段 × 下文件首 3–4 段 × pX/pX+1 图像下/上半 × pX/pX+1 文字层首末 6 行"四重对照；环境检查用全书"栈"扫描（跳过 `%` 注释行）；整书编译用 `xelatex -output-directory <temp> main.tex`。
- 审计为 **16:24 快照**。定稿前若仍有批量写入（本审计期间 16:21:52、16:22:59–16:23:30 均有），建议对 08、09、12、13 四缝重跑；另对被 16:21–16:23 批量 touch 的文件（ch01-2、ch06、ch09-2、ch10-1、ch10-3、glossary）相关接缝（01/02、08/09、12/13、14/15、16、18/19）再做一次首尾抽查。
- 未做的事：未逐字重译校对（由各单元自检与 structure/formula/terms-audit 负责）；未检查单元内部页码覆盖（同上）。
