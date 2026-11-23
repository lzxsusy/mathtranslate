# trace-curve-a —— §1.1–§1.4（p.3–p.10）决策流水

tag：curve-a　底本：Fargues, *Geometrization of the local Langlands correspondence: an overview*（2016-02-02）
逐条格式：**原文 → 我的处理 → 依据**。凡「图上核」= 见 `工程文件/work/pages/pNNN.png` 与 `工程文件/work/zoom/` 下放大图。

## A. 版式与宏

1. **`\section{曲线}` 后公式从 (1) 起**
   原文 → §1.1–1.4 的公式编号 (1)–(5)。处理 → `\section` 之后、`\subsection` 之前放 `\setcounter{equation}{0}`。
   依据 → 原始 PDF p.4 的 δ 公式即编号 (1)，且全块只有 5 个编号公式；若沿用 book 类 `\theequation`（节内连续）而前面 §1 已用过公式，编号会从 6 起。

2. **`tikzcd` 不能裸用**
   原文 → 三张交换图。处理 → 两图（p.4 V 图、p.7 菱形图）以 `\begin{center}…\end{center}` 包住、单元格内写 `$…$`；第三张（p.9 伴随函子）放在 `\[ … \]` 里，单元格用 `\text{}`。
   依据 → 本机 `tikzlibrarycd.code.tex:4390` 显示 `\tikzcd` 直接展开为 `\tikzpicture`，是行内图元而非数学显示。首轮裸用后图接在正文行末（实测 p.2 图与「此时有两个结构态射」挤在同一行），故必须自行居中。`\begin{center}` 放进 `\[…\]` 会报 `! Missing $ inserted`（已踩过一次）。

3. **`⟦π⟧` 的兜底**
   原文 → `R°⟦π⟧`、`F_q⟦T⟧`、`Z_p⟦T^{1/p^∞}⟧`。处理 → 文件头 `\providecommand{\llbracket}{[\![}` / `\rrbracket`，正文用 `\llbracket…\rrbracket`。
   依据 → preamble 未载 stmaryrd；SPEC 也明说无 `\llbracket`。选 `[\![` 而非 `\llbracket` 的替代字形，是为了不改 preamble。渲染后与原文双括号外观一致（见 `_check_a.pdf` p.3/p.5/p.8）。

4. **`⋄` 上标**
   原文 → `Spa(E)^⋄`、`X^⋄_{S,E}`、`𝒢^⋄`。处理 → `^\diamond`（amssymb）。
   依据 → preamble 无 `\diamond` 宏定义，但 amssymb 已载 `\diamond`；小号下渲染为小菱形，与原文扫描件一致（原文该符号本身在缩小时近似「°」）。

5. **页锚位置**
   - p.3：`\leavevmode\srcpage{3}设 $E$ 是…`（§1 首段行首）——原文 p.3 开头是 §1 标题与首段，锚贴首段最准；不放 `\section` 之后，因为那里是垂直模式，`\marginnote` 会挤出空段落。
     **与 SPEC 骨架的出入**：SPEC 写作「`\section{曲线}` → `\srcpage{3}` → `\subsection{adic 曲线}`」，实际把 `\srcpage{3}` 放在 §1.1 首段行首（即 `\subsection` 之后），只差一个标题的位置，换来标题间不留空行。若 Lead 要求严格照骨架，把该锚上移一行即可。
   - p.4 / p.10：`\srcpage{4}\begin{definition}`、`\srcpage{10}\begin{example}`——原文这两页正好从定理/例起头，锚只能放在环境之前。实测垂直模式下 `\marginnote` 多出一个空行（12pt，`_bench_a.tex` 对照：无锚时「定义 1.1」y=363pt，有锚 y=375pt）。已接受；若 Lead 要求零空行，改法见报告 §6。
   - p.5：`\item \srcpage{5}第二个…`——原文页界落在两条 bullet 之间，锚放第二条 bullet 行首。
   - 其余 p.6/7/8/9：段落首 `\leavevmode\srcpage{N}`。

6. **marginnote 出界（全书问题，未改 preamble）**
   实测 → oneside 主书里 8 个 `p.N` 全画在 x≈633pt（纸宽 595.28pt），看不见；twoside check 奇数页同此，偶数页落在左缘被裁掉一半（只余「p.5」「p.6」等）。
   依据 → `_check_a.log` 报 `\marginparwidth=116.0pt`，而 geometry `margin=2.6cm`≈73.7pt。preamble 第 40 行注释明说「任何不可见的情况都能事后核查」，故 `.pagemarks` 才是校验口径：本块 8 个锚齐全有序。**建议 Lead 统一在 preamble 加 `\setlength{\marginparwidth}{2cm}`。**

## B. 公式逐符号核对（图上核）

7. **公式 (1) 的指数为负**
   文本抽取得 `p− log|π(ymax)| log|ϖR(ymax)|`，符号层不可信。放大 p.4 后确认：
   `y ↦ p^{-\frac{\log|\pi(y^{\max})|}{\log|\varpi_R(y^{\max})|}}`（负指数、分母为 log|ϖ_R|）。→ 照此排。
   依据 → `工程文件/work/zoom/p004_a.png`。

8. **`D*_S` 的结构层公式**
   图上核（`p004_c.png`）：`D*_S = Spa(R°⟦π⟧, R^+ + πR°⟦π⟧) \ V(πϖ_R)`。注意第二项是 `R^+ + πR°⟦π⟧`（不是 `R^+⟦π⟧`）。→ 照排。

9. **`A` 的三行等式**
   图上核（p.5）：`A = W_{O_E}(R°) = W(R°)⊗_{W(F_q)}O_E = {Σ[x_n]π^n | x_n∈R°}`，右端括注 *(unique writing)*。→ 括注排成 `\text{（\emph{唯一}写法）}`，与原文右端对齐。

10. **Gauss 范数**
    图上核：`‖Σ_{n≫-∞}[x_n]π^n‖_ρ = sup_{n∈Z}‖x_n‖ρ^n`。注意左端是 `n≫-∞`（双向无穷和），不是 `n≥0`。→ 照排。

11. **公式 (4)(5) 的引号**
    原文用 `"D^{*,1/p^∞}_S/O_E^×"`（英文直引号表示「姑且这么说」）。→ 译作中文引号「」，并把引号写在数学外：`\text{“}…\text{”}`。理由：数学模式内的直引号在 xeCJK 下会与全角标点冲突。

12. **菱形交换图**
    放大 p.7 图（`p007_diag.png`）逐箭头核：上节点 `Y_{S,E_∞}`；`(-)^♭` 指左下到 `D^{*,1/p^∞}_S`；`-⊗̂E_∞` 由 `Y_{S,E}` 指右上；左下节点与 `Y_{S,E}` 各有一箭头汇于 `D^{*,1/p^∞}_S/O_E^×`，`Y_{S,E}` 那支标 `=`。→ tikz-cd 复刻（`[dl, "(-)^\flat"']`、`[ul, "-\hat{\otimes}E_\infty"]`、`[dl, "="']`）。
    已知差异：`=` 落在箭头右侧（原文左侧），`'` 换边后仍在右，未再纠缠。

## C. 术语与译法

13. **完满 / adic / 菱形 / untilt**：按 glossary。p.3 首现「完满空间」、p.3 首现「adic 空间」、p.7 首现「菱形」、p.7 定义 1.8 首现「untilt」各给 `\yizhu` 带来源（任务硬要求）。「untilt」全篇不译，作名词用（「一个 untilt」「$\sharp$ 是……的 untilt」）。

14. **pseudo-uniformizing element** → 「伪一致化元」（glossary 第 62 行）。不定冠词「a so-called pseudo-uniformizing element」译作「就是所谓的伪一致化元」。

15. **「It is “a curve”」** → 「它「是一条曲线」」。原文引号是强调「姑且称之为曲线」，故保留引号；同理「proper over S」→「在 S 上紧合」加引号。

16. **`y^{\max}`**：原文 max 为斜体上标（`y^{max}`）。→ 排 `y^{\max}`（正体）。纯排版取舍：正体更符合中文数学排版惯例，语义不变。

17. **`Õ_X`**：原文 `ν_* Õ_X = O_X`，`Õ` 为花体 O 加波浪。→ `\wt{\cO}_X`（preamble 有 `\wt`）。

18. **`Perf`**：原文显示体 `Perf_{F_q}`。→ `\mathrm{Perf}_{\FF_q}`。preamble 只有小写 `\perf`，不改 preamble，就地 `\mathrm`。

19. **「faithfull topology」** → 「忠实拓扑」。原文拼写多一个 l，属笔误，不另注（报告 §4 记一笔）。

20. **「Digging a little bit on finds」** → 「稍微深挖一下就会发现」。按语义（one finds）译，不保留拼写错误。

21. **口语照译**：`we try to convince the reader (and ourselves)` 一类句式本块集中于「作者选择少管严格的严谨性，多顾阐述」（注 1.7）、「人们忍不住「下降」」（§1.3.1）、「典型的问题：它上面的向量丛是什么？」（§1.2）。均按口语直译，未雅化。

## D. 疑误处理（照原样 + 说明）

22. **p.5 `[ϖ_F]=0`** → 照原样排 `[\varpi_F]=0`，加 `\yizhuw`。
    依据 → 同段商环写作 `A[1/ϖ_E, 1/[ϖ_R]]`，除子应为 `[ϖ_R]=0`；放大图 `p005_d.png` 确认原文确为 `F`。按任务「不许悄悄改」处理。

23. **p.5「all properties of section 1.1.2 apply to X_S」** → 照原样排「§1.1.2」，加 `\yizhuw`。
    依据 → 该句正在 §1.1.2 之内，所指应为 §1.1.1 的两条性质（强 Noether、「是一条曲线」）；放大图 `p005_b.png` 确认原文为 `1.1.2`。

24. **p.6「(the preceding case) of E is perfectoid」** → 按 `or` 译成「或者 E 完满的情形」，加 `\yizhuw` 说明原文作 of。
    依据 → 放大图 `p006_b.png`；原意是「离散赋值 **或** 完满」两种 E，否则命题 1.6 无从谈起。

25. **p.7「although Y_{F,E} is not perfectoid」** → 照原样排 `Y_{F,E}`，**未加注**，只在报告 §4 单列。
    依据 → 放大图 `p007_b.png` 确认原文为 `Y_{F,E}`；上下文（S 为一般完满空间、Y_{S,E} 才是主角）表明疑为 `Y_{S,E}`，但同句后半也出现 `Y_{F,E}⊗̂E_∞`，改动会连带改两处，交 Lead 定夺。

## E. 自查

26. 页锚数 8，`.pagemarks` = 3…10 各一次；无 `??`；`\srcpage` 不在脚注、不在任何环境内部（p.5 的锚在 `itemize` 的 `\item` 里，属正文行内，不是环境参数区）。
27. 定理号 aux 实测 1.1–1.23 连续无缺；公式号 (1)–(5)。
28. 编译：`cmd /c "build.bat check sections/s02-curve-a.tex a"` → `[OK] _check_a.pdf`，9 页，0 error，无 Overfull/Underfull。
29. 注意：`cmd //c` 在 MSYS bash 下会被当成交互式 cmd（只打印 banner），必须写 `cmd /c`；且 `sections\s02-…` 的反斜杠会被吃掉，用 `sections/s02-curve-a.tex`。
