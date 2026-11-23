# r-curve-a —— §1.1–§1.4（原文 p.3–p.10）

## 1. 交付

- 文件：`源码/sections/s02-curve-a.tex`（450 行）
- 页锚：p.3–p.10 共 **8** 个（`\srcpage{3}`…`\srcpage{10}`，各一次，均按原文页首落位；p.3 用 `\leavevmode\srcpage{3}` 起首段，p.4 与 p.10 落在 `definition`/`example` 之前）
- 编译：`build.bat check sections/s02-curve-a.tex a` → **0 error**；`_check_a.pagemarks` = 3 4 5 6 7 8 9 10（不缺、不重、有序）；无 Overfull/Underfull 告警
  - **工具坑**：路径必须用正斜杠 `sections/s02-curve-a.tex`。build.bat 用 `echo \input{"%~2"}` 生成壳文件，反斜杠 `sections\s02-…` 会被 TeX 当成控制序列，报 `! Undefined control sequence. <argument> "sectionss 02-curve-a.tex"`；这是 build.bat 的问题，与本文件无关。（另：MSYS bash 下要写 `cmd /c`，写 `cmd //c` 只会弹出交互式 cmd。）
- 交叉引用：`\eqref{eq:1.1–1.5}` 与 `[27]`、`[26]`、`[10]`、`[15]`、`[11]`、`[24]` 全部解析（第二遍无 undefined reference）
- 定理/公式编号（aux 实测）：Definition 1.1、1.2、1.3、1.4、1.5、1.8、1.12、1.15、1.17；Proposition 1.6、1.10、1.18、1.22、1.23；Remark 1.7、1.9、1.14、1.20；Corollary 1.11、1.13、1.21；Lemma 1.16；Example 1.19 —— 与原文 **1.1…1.23 逐条一致**；公式 (1)(2)(3)(4)(5) 复原
- 交换图：p.4 双结构态射图、p.7 菱形图、p.9 伴随函子图，均用 tikz-cd

## 2. 编号对齐表

| 原文 | 译文（label） | 类型 |
|---|---|---|
| (1) p.4 半径函数 δ | `\eqref{eq:1.1}` → (1) | 公式 |
| (2) p.6 乘积公式 | `\eqref{eq:1.2}` → (2) | 公式 |
| (3) p.6 X_{S,E} 商 | `\eqref{eq:1.3}` → (3) | 公式 |
| (4) p.7 加引号的“D/O_E^×” | `\eqref{eq:1.4}` → (4) | 公式 |
| (5) p.7 环面的“公式” | `\eqref{eq:1.5}` → (5) | 公式 |
| Definition 1.1 | `def:1.1` → 定义 1.1 | 定义 |
| Definition 1.2 | `def:1.2` → 定义 1.2 | 定义 |
| Definition 1.3 | `def:1.3` → 定义 1.3 | 定义 |
| Definition 1.4 | `def:1.4` → 定义 1.4 | 定义 |
| Definition 1.5 | `def:1.5` → 定义 1.5 | 定义 |
| Proposition 1.6 | `prop:1.6` → 命题 1.6 | 命题 |
| Remark 1.7 | `rem:1.7` → 注 1.7 | 注 |
| Definition 1.8 | `def:1.8` → 定义 1.8 | 定义 |
| Remark 1.9 | `rem:1.9` → 注 1.9 | 注 |
| Proposition 1.10 | `prop:1.10` → 命题 1.10 | 命题 |
| Corollary 1.11 | `cor:1.11` → 推论 1.11 | 推论 |
| Definition 1.12 | `def:1.12` → 定义 1.12 (Scholze [27]) | 定义 |
| Corollary 1.13 | `cor:1.13` → 推论 1.13 | 推论 |
| Remark 1.14 | `rem:1.14` → 注 1.14 | 注 |
| Definition 1.15 | `def:1.15` → 定义 1.15 | 定义 |
| Lemma 1.16 | `lem:1.16` → 引理 1.16 | 引理 |
| Definition 1.17 | `def:1.17` → 定义 1.17 | 定义 |
| Proposition 1.18 | `prop:1.18` → 命题 1.18 | 命题 |
| Example 1.19 | `ex:1.19` → 例 1.19 | 例 |
| Remark 1.20 | `rem:1.20` → 注 1.20 | 注 |
| Corollary 1.21 | `cor:1.21` → 推论 1.21 | 推论 |
| Proposition 1.22 | `prop:1.22` → 命题 1.22 | 命题 |
| Proposition 1.23 | `prop:1.23` → 命题 1.23 | 命题 |

节标题：`\section{曲线}`（1.）→ `\subsection{adic 曲线}`（1.1）→ `\subsubsection*{1.1.1. 等特征情形}` / `1.1.2. 不等特征情形` → `\subsection{等特征与不等特征的联系}`（1.2）→ `\subsection{菱形乘积公式}`（1.3）→ `1.3.1. 菱形` / `1.3.2. 乘积公式` → `\subsection{untilt 作为曲线上的 Cartier 除子}`（1.4）→ `1.4.1. 等特征情形` / `1.4.2. 不等特征情形` / `1.4.3. 若干 Hilbert 菱形`。原文 §1.5「The schematical curve」标题不属本块，未写。

## 3. 译注

共 11 条：`\yizhu` 8 条（带来源）、`\yizhuw` 3 条（疑误说明，无外部依据）。

| # | 位置 | 术语/内容 | 来源 |
|---|---|---|---|
| 1 | p.3 首次出现「完满空间」 | 完满空间不固定基完满域（[24] vs [11]/[27]） | A：原文 §1.1 p.3；I：glossary |
| 2 | p.3 首次出现「adic 空间」 | Huber 框架：经典点+几何点 | A：Huber 1996；I：glossary |
| 3 | p.4 公式 (1) 后 | δ(y) 的几何含义、δ(φ(y))=δ(y)^{1/q} | A：原文 §1.1.1 p.4 |
| 4 | p.7 首次出现「菱形」 | 菱形 = pro-étale 拓扑下的代数空间 | A：原文 §1.3.1、Def 1.12；I：glossary |
| 5 | p.7 定义 1.8(1) | untilt 与倾斜互逆（不译） | A：Def 1.8；I：glossary |
| 6 | p.9 「前完满空间」 | pre-perfectoid 指的是基变换后完满 | A：原文 §1.3.2 p.9 |
| 7 | p.9 「Weierstrass 分解」 | 次数 1 本原元 = 单位×(π−a) = 次数 1 Cartier 除子 | A：原文 §1.4.1 p.9 |
| 8 | p.10 「Hilbert 菱形」 | 对应曲线的 d 次对称积 | A：原文 §1.4.3 p.10 |
| 9 | p.5 `[ϖ_F]=0` | 疑为 `[ϖ_R]` 之误（照原样） | 译者按（无外部依据） |
| 10 | p.5 「§1.1.2 的所有性质」 | 疑为 §1.1.1 之误（照原样） | 译者按（无外部依据） |
| 11 | p.6 「of E is perfectoid」 | of 当为 or（按 or 译） | 译者按（无外部依据） |

## 4. 疑点

| 位置 | 原文 | 类型 | 处理 | 状态 |
|---|---|---|---|---|
| p.5 亚纯除子 | 「沿除子 π=0 与 [ϖ_F]=0」 | 疑笔误（上下文商环为 A[1/ϖ_E,1/[ϖ_R]]） | 照原样 + `\yizhuw` | 待 Lead 定夺 |
| p.5 末段 | 「all properties of section 1.1.2 apply to X_S」 | 疑笔误（本节即 1.1.2，应为 1.1.1） | 照原样 + `\yizhuw` | 待 Lead 定夺 |
| p.6 首段 | 「(the preceding case) **of** E is perfectoid」 | 疑笔误（of→or） | 按 or 译 + `\yizhuw` | 待 Lead 定夺 |
| p.7 §1.3.1 首句 | 「although **Y_{F,E}** is not perfectoid」 | 疑笔误（应为 Y_{S,E}；同句下文的 Y_{F,E}⊗̂E_∞ 也如此） | 照原样，未加注 | 待 Lead 定夺 |
| p.7 菱形图 | 「=」标在 Y_{S,E}→D/O_E^× 箭头一侧 | 排版差异（原文在箭头左侧） | 标在箭头右侧 | 可接受 |
| p.9 注 1.14 | 「Digging a little bit **on** finds」 | 原文拼写（one finds） | 译作「就会发现」 | 无碍 |
| p.10 §1.4.3 | 「[27] 的 **faithfull** topology」 | 原文拼写（faithful） | 译作「忠实拓扑」 | 无碍 |
| p.8 | 「Do we **loose** some properties」 | 原文拼写（lose） | 译作「丢掉」 | 无碍 |
| **全书级** | `\srcpage` 的 marginnote | 版式缺陷：`\marginparwidth=116pt` > 版心外边距 2.6cm≈73.7pt，oneside 下 p.N 全部落到纸张右缘之外（实测绘制于 x≈633pt，纸宽 595pt）；twoside check 时偶数页在左缘被裁一半 | **未改 preamble**（任务禁止）；`.pagemarks` 正常，8 个锚齐全 | **建议 Lead 在 preamble 加一行 `\setlength{\marginparwidth}{2cm}`（或给 geometry 传 `marginparwidth`）** |

## 5. 新增术语建议

| 原文 | 建议译名 | 依据 |
|---|---|---|
| pre-perfectoid space | 前完满空间 | 原文 §1.3.2 自定义；与「完满」保持词族一致 |
| primitive element of degree d | 次数 d 本原元 | §1.4 全节；degree 1→次数 1 |
| strongly noetherian | 强 Noether | 原文 §1.1.1「Huber's sense」；与 SY02-26 译法一致 |
| faithful topology | 忠实拓扑 | §1.4.3 引 [27] |
| ramified Witt vectors | 分歧 Witt 向量 | §1.1.2 定义 1.3 |

## 6. 遗留

- §1.5 起不在本块范围。
- `\srcpage{5}` 落在 `itemize` 的第二条 `\item` 内（原文页界正好在两条 bullet 之间）。若「锚不入环境」要按机械口径严格执行，请 Lead 示下：可拆成两个 `itemize`，但两条 bullet 之间会多出垂直间距。
- **`⟦ ⟧` 兜底**：preamble 无 stmaryrd，本文件头用 `\providecommand{\llbracket}{[\![}` / `\rrbracket` 兜底。若 Lead 决定在 preamble 统一加 `\usepackage{stmaryrd}`（或 `\newcommand\llbracket{\lBrack…}`），删掉本文件头两行即可；`\providecommand` 在别处已定义时不会冲突。
- **p.3 归属**：p.3 上半页（「本文结构如下」列表 + Thanks）属 s01，本文件从 `\section{曲线}` 起。若 s01 也在 p.3 放锚，全书会出现两个 `\srcpage{3}`，请 Lead 统一归属。
- 与 SPEC 骨架的出入：骨架为「`\section{曲线}` → `\srcpage{3}` → `\subsection{adic 曲线}`」，实际把 `\srcpage{3}` 放在 §1.1 首段行首（`\subsection` 之后），避免标题之间出现空段落。需要严格照骨架时上移一行即可。
- 本文件在 `\section{曲线}` 之后置 `\setcounter{equation}{0}`，以确保公式从 (1) 起；文件结束时 equation 计数为 5，后续块若需另起编号请自行处理。
- 页锚中 p.4、p.10 因落在定理环境之前而处于垂直模式，`\marginnote` 会多出一个空段落（实测 12pt）；如 Lead 认为不可接受，可统一改为「锚点贴上一段句末」的写法。
