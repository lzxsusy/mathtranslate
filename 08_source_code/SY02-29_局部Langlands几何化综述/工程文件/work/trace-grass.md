# trace-grass —— §3 翻译流水（tag: grass）

## 0. 环境与文件
- 工程根：`C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-29_局部Langlands几何化综述`
- 底本：`工程文件/work/src/p023.txt … p028.txt`（逐页文本）；页面图 `工程文件/work/pages/pNNN.png`
- 渲染：`PYTHONIOENCODING=utf-8 python 工程文件/tools/render_pages.py 23-28 --dpi 150`（p.28 已存在，skip）
- 编译：`cd 源码 && MSYS_NO_PATHCONV=1 cmd /c "build.bat check sections/s05-grassmannian.tex d"`（**必须正斜杠**，反斜杠被 MSYS 吃掉，TeX 报 `Undefined control sequence: <argument> "sectionss 05-…"`）
- 无 read/write/edit 工具，读文本用 `ops_inspect_local_file`（注意：它把反斜杠显示成双写），写文件用 `cat > … <<'TEX'`（引号防展开）。

## 1. 通读与结构确认
1. 读 TASK-translator.md、SPEC.md、glossary.tsv、preamble.tex、main.tex、build.bat。
2. 读 p023–p027 全文；p028 查明整页是 §4，§3 正文止于 p.27 末 → 6 个页锚中的 28 号无对应内容（见报告遗留 1）。
3. 逐页对 150 dpi 页面图核公式与排版，重点裁图核对：
   - p.24 顶部（裁 `0.07–0.38`）：确认注 3.3 为斜体、止于 “on Spec(R).”，其后 “One checks that…” 是**正体独立段落**，故译文把它放在 remark 环境之外。
   - p.23 竖排小图、p.25 命题 3.10 怪排的 hat-⊗、p.26 注 3.13 的 Gr_{B_dR} 下标、p.27 交换图。

## 2. 体例决策（含理由）
- **编号**：21 个环境全部用 `[section]` 共享计数器，连排即 3.1–3.21；未手写编号。
- **Hope 3.15**：preamble 第 78 行已有 `\newtheorem{hope}[theorem]{期望}`（Lead 后加），故直接用 `hope` 环境，不自建；正文语气保留「期望/应该」，不写成「猜想」。
- **Hecke 记号**：原文印斜体 *Hecke*，preamble 的 `\Hck` 印正体 “Hck”，故用 `\mathit{Hecke}^{\le\mu}`，未用 `\Hck`。
- **公式**：本块无编号公式，全部用 `\[ \]`；`\llbracket/\rrbracket` 就地 `\providecommand` 兜底（preamble 无 stmaryrd）。
- **节标题**：`\section{\texorpdfstring{$B_{\mathrm{dR}}$}{BdR}-仿射 Grassmann 簇与 Hecke 叠}`，避免 hyperref 书签里出现数学。
- **引文**：原文 [1][5][6][21][27][29][32] 以字面 [] 排（与 s02、s06 一致）；命题 3.5/定理 3.14 的引用放在 `\begin{proposition}[{[6]}]` 可选参数里，复现原文「Proposition 3.5 ([6]).」的头部样式。
- **译注**：`\yizhu` 3 条（A 级）、`\yizhuw` 3 条 + 另 2 条 A 级，共 8 条；每条 ≤120 字。
- **术语**：严格按 glossary.tsv；新词（torsor=扭子、perfection=完满化、minuscule=极小等）列在报告 §4 建议补录。

## 3. 页锚（源码位置）
`\srcpage{23}`（section 后）/ `{24}`（定义 3.1 后）/ `{25}`（3.3.1 前）/ `{26}`（注 3.13 前）/ `{27}`（注 3.18 前）/ `{28}`（文件末）。`_check_d.pagemarks` 输出 23–28 六行，顺序正确。

## 4. 编译与图像自检记录
| 轮次 | 结果 | 发现 / 处理 |
|---|---|---|
| 1 | 6 页 [OK] | 竖箭头 tikzcd 被排进段落中间（行内）；定义 3.1 后多出一段空白 |
| 2 | 6 页 [OK] | 给 tikzcd 加空行独立成段；删去段落内联 |
| 3 | 6 页 [OK] | `f:\mathcal{E}_1` 误写成 `f:\\mathcal`（渲染成 “mathcalE₁”），改正 |
| 4 | 6 页 [OK] | 两处 tikzcd 外包 `\[ \]` 居中，与原书一致；注 5 措辞改写 |
| 5 | 6 页 [OK] | 补 2 条译注（B_dR⁺、Witt 向量仿射 Grassmann 簇），脚注在定理环境内正常排出 |
| 6（终） | 6 页 [OK]，0 error，无 Overfull/Underfull，无 Missing character | 定稿 |

页面图复核：p.1 竖箭头图为独立居中图；p.5 Hecke 交换图 ←h 在左箭头上方、→h 在右箭头上方，与原文一致；p.6 猜想 3.21 的 `Ind_{Ĝ⋊Γ'}^{^LG}`、`IC_μ=Q̄_ℓ(⟨ρ,μ⟩)[⟨2ρ,μ⟩]` 上下标正确。

## 5. 试过但放弃的方案（教训）
- `\leavevmode\srcpage{N}` / 把锚移进定理环境 / 把锚贴到上一段末句：**都不稳定**，且会连带改变分页，使原本可见的锚消失（实测 p.25、p.26 会跟着丢）。结论：锚只保证语义位置与 pagemarks，不为「可见」调排版。
- `cmd //c build.bat`：MSYS 把 `//c` 当路径，直接进交互 shell；须 `MSYS_NO_PATHCONV=1 cmd /c`。
- 用 `sections\s05-…` 传参：反斜杠被吃，须正斜杠。

## 6. 未决 / 交 Lead
1. 本节末尾 `\srcpage{28}` 与 s06-statement.tex 首行重复 → 建议删本节这条（p.28 无 §3 内容）。
2. s06 的译注误称「全文无编号 3.21 的猜想」→ 实有猜想 3.21（本文件），建议删该译注。
3. 注 3.13 的 Gr_{B_dR}（下标）与推论 3.11 的 Gr^{B_dR}（上标）不一致 → 需全书统一。
4. `\Hck` 与 `\mathit{Hecke}` 二者择一，全书勿混用。
5. 引文编号须与 s99-bibliography 对应。
