# r-curve-b —— §1.5–§1.6（原文 p.10–p.16）

## 1. 交付

- 文件：`源码/sections/s03-curve-b.tex`（368 行）
- 页锚：p.10–p.16 共 **7** 个（`\srcpage{10}`…`\srcpage{14}`、`\srcpage{16}`，p.15 页界落在句中，用 `\srcpageinl{15}`）
  - `_check_b.pagemarks` = `10 11 12 13 14 15 16`（不缺、不重复、有序）
  - p.10 锚放 §1.5 标题之后（原文 p.10 末行即 `1.5. The schematical curve.`）；p.12、p.13、p.16 用 `\leavevmode\srcpage{N}` 贴在后续正文行首，避免垂直模式下 `\marginnote` 多出空段落
- 编译：`./build.bat check sections/s03-curve-b.tex b` → **`[OK] _check_b.pdf`，7 页，0 error**；日志无 Overfull/Underfull、无 undefined control sequence、无 undefined reference；只剩 hyperref 的 `Rerun to get /PageLabels entry` 与 `Label(s) may have changed`
  - **工具坑**：路径必须用正斜杠 `sections/s03-curve-b.tex`。build.bat 生成 `\input{"%~2"}`，反斜杠会被 TeX 当控制序列吃掉，报 `! Undefined control sequence. <argument> "sectionss 03-curve-b.tex"` → `No pages of output`。另：MSYS bash 下 `cmd //c "build.bat …"` 只会弹出交互式 cmd（只打印 banner 就退出），直接 `./build.bat check …` 即可。
- 定理编号（`_check_b.aux` 实测，与原文逐条一致）：定义 1.24、定义 1.25、命题 1.26、命题 1.27、推论 1.28、定理 1.29（[16]）、命题 1.30、命题 1.31、定义 1.32、命题 1.33 —— **1.24…1.33 连续，无断裂**
- 公式：p.14 的 (6) 用 `\begin{equation}\label{eq:1.6}` 实编；草稿守卫把 `equation` 预置为 5（s02 用掉 (1)–(5)），故排 **(6)**，且全书里接得上 s04 的下一个编号
- 交换图：p.15 的 `B⁺_dR(R♯) —θ→→ R♯，R ⤢ B⁺_dR，R ‖ R♯` 用 tikz-cd 复刻（θ 双箭头、`equal` 双线）
- 译注：`\yizhu` 4 条（带来源）+ `\yizhuw` 2 条（疑误说明），共 6 条

## 2. 编号对齐表

| 原文 | 译文（label） | 类型 | 页 |
|---|---|---|---|
| Definition 1.24 | `def:1.24` → 定义 1.24 | 定义 | p.11 |
| Definition 1.25 | `def:1.25` → 定义 1.25 | 定义 | p.12 |
| Proposition 1.26 | `prop:1.26` → 命题 1.26 | 命题 | p.13 |
| Proposition 1.27 | `prop:1.27` → 命题 1.27 | 命题 | p.14 |
| Corollary 1.28 | `cor:1.28` → 推论 1.28 | 推论 | p.14 |
| Theorem 1.29 ([16]) | `thm:1.29` → 定理 1.29 | 定理 | p.14 |
| Proposition 1.30 | `prop:1.30` → 命题 1.30 | 命题 | p.15 |
| Proposition 1.31 | `prop:1.31` → 命题 1.31 | 命题 | p.15 |
| Definition 1.32 | `def:1.32` → 定义 1.32 | 定义 | p.15 |
| Proposition 1.33 | `prop:1.33` → 命题 1.33 | 命题 | p.15 |
| 公式 (6) | `eq:1.6` → (6) | 公式 | p.14 |

节标题：`\subsection{概形曲线}`（全书 1.5）→ `\subsubsection*{1.5.1. 定义}` / `1.5.2. 一个等特征下的计算` / `1.5.3. 等特征下的类似计算` / `1.5.4. 概形曲线的内蕴定义与 GAGA` → `\subsection{untilt 作为概形曲线上的 Cartier 除子}`（全书 1.6）→ `1.6.1. 等特征情形` / `1.6.2. 不等特征情形` / `1.6.3. 沿 Cartier 除子的形式完备化`。原文 §2「The stack Bun_G」起不属本块，未写。

## 3. 译注

| # | 位置 | 内容 | 来源 |
|---|---|---|---|
| 1 | p.11 定义 1.24(1) | $P_R$ 以 $d$ 为分次；$\oo(Y)^{\varphi=\pi^d}$ 即 $\varphi(x)=\pi^d x$ 的元素，正是 $H^0$ 的显式描述 | A：原文 §1.5.1 p.11 |
| 2 | p.11 定义 1.24(2) | 「概形曲线」= schematical curve，与「adic 曲线」$X^{ad}$ 相对，两者由 $X^{ad}\to X^{sch}$ 联系 | A：原文 §1.5.1 p.11 |
| 3 | p.13 ind-概形 | ind-scheme 的译法与本工程 adic / pro-étale 等前缀词一致 | I：本工程术语惯例（术语表暂无） |
| 4 | p.15 上标 $\xi\varphi=\pi^{d-1}$ | 原文简写：先在 $\xi$ 处局部化，再取 $\varphi(x)=\pi^{d-1}x$ 的元素 | 译者按（无外部依据） |
| 5 | p.15 定义 1.32 | $\mathrm{B}^{+}_{dR}$ 即 Fontaine de Rham 周期环的正部分，此处实现为 $\mathbf{A}[1/\pi]$ 沿 $\xi$ 的形式完备化 | A：原文 §1.6.3 p.15 |
| 6 | p.15 「A usual」 | 原文作 “A usual”，当为 “As usual”（照例、如常）之误 | 译者按（无外部依据） |

## 4. 疑点

| 位置 | 原文 | 类型 | 处理 | 状态 |
|---|---|---|---|---|
| **§1.5.3 标题** | **“The analog computation in equal characteristic”** | **疑笔误（当为 unequal）** | **照译标题「等特征下的类似计算」，未改；见下** | **待 Lead 定夺** |
| p.13 §1.5.3 | 「with reduction $\mathscr{G}$ then $\mathscr{G}(R^\circ)$」 | 归约与群律用了同一花体字形（原文未用黑体 $\mathbb{G}$） | 照排两处 `\mathscr{G}` | 待 Lead 定夺 |
| p.14 定理 1.29 上方 | $T_\pi(\widetilde{\mathscr{G}}\otimes_{\oo_E}R^{\sharp,\circ})=\oo_E$ 的 $\oo_E$ | 原文该 $\oo_E$ 下方有一道短横（疑排版残留，无数学含义） | 按无下划线排 | 可接受 |
| p.14 推论 1.28 | 「$X^{sch}$ is **the the** categorical quotient」 | 原文冠词重复 | 中译无对应，只译一次 | 无碍 |
| p.15 命题 1.31 上方 | 「the convergent **Weirstrass** product」 | 原文拼写（Weierstrass） | 译名用正字「Weierstrass 乘积」 | 无碍 |
| **全书级** | `\srcpage` 的 marginnote | 版式：`\marginparwidth=116pt` ≫ geometry 外边距 2.6cm≈73.7pt，`p.N` 画到版心外、贴纸缘（实测 p.13 的注记在 x≈1130/1241px）；与 s02 报告 §4 同一问题 | **未改 preamble**（任务禁止）；`.pagemarks` 为校验口径，7 个锚齐全 | **建议 Lead 在 preamble 加 `\setlength{\marginparwidth}{2cm}`** |
| **p.10 归属** | 原文 p.10 末行是 §1.5 标题 | 与 s02 重复占位 | s02 已在例 1.19 前放 `\srcpage{10}`；本块按任务「p.10–p.16 共 7 锚」又在 §1.5 标题后放了一个。全书会重复 `label{srcpage:10}`（hyperref 警告）并在 `.pagemarks` 里出现两个 10 | **请 Lead 择一**：删本块的话删第 24 行 `\srcpage{10}`，本块余 6 锚（11–16） |

**关于 1.5.3 标题（任务指定必写）**：原文标题作 “The analog computation in **equal** characteristic”，但本节第一句就是 “Almost all the results of the preceding section extend to the case when $[E:\QQ_p]<+\infty$”，全节讲的是 Lubin–Tate 群律、$W_{\oo_E}(R^\circ)$ 一类**不等特征**对象；真正的等特征计算在 §1.5.2，不等特征的系统叙述在 §1.6.2（“The unequal characteristic case”）。三项旁证一致指向标题应为 **unequal characteristic**。按 TASK「疑误照原样译 + 报告单列」处理：标题译作「等特征下的类似计算」，正文照原文的不等特征内容译，未作任何改写。

**编号断裂**：无。定理 1.24–1.33 连续，公式 (6) 紧接 s02 的 (1)–(5)。

## 5. 新增术语建议

| 原文 | 建议译名 | 依据 |
|---|---|---|
| schematical curve | 概形曲线 | 任务指定；与「adic 曲线」成对 |
| adic curve | adic 曲线（adic 不译） | 与 glossary「adic 空间」一致 |
| primitive element of degree 1 | 次数 1 的本原元 | glossary；§1.4 已用 |
| pseudo-uniformising element | 伪一致化元 | glossary |
| convergent Weierstrass product | 收敛的 Weierstrass 乘积 | p.12、p.15 反复出现 |
| Lubin–Tate group law | Lubin–Tate 群律 | p.13 |
| Tate module | Tate 模 | p.12 |
| formal completion along a Cartier divisor | 沿 Cartier 除子的形式完备化 | glossary「形式完备化」 |

## 6. 遗留

- §2 起（The stack Bun_G）归 `s04-bung.tex`；本文件末尾以注释标明结束位置。
- **`⟦ ⟧` 兜底**：preamble 无 stmaryrd，本文件头用 `\providecommand{\llbracket}{[\![}` / `\rrbracket` 兜底（与 s02 同）。若 Lead 在 preamble 统一加 `\usepackage{stmaryrd}`，两处 `\providecommand` 自动失效，无需改动。
- **草稿守卫**：文件头 `\ifnum\value{section}=0` 块预置 `section=1, theorem=23, equation=5`，使单章自检排出 1.24–1.33 与 (6)；全书编译时 `section=1`，该块自动跳过。代价是单章草稿里两个 `\subsection` 排成「1.1 概形曲线」「1.2 untilt 作为…」（缺 §1 前文），全书里为 1.5 / 1.6 —— 并非编号错误。
- **p.15 为何用 `\srcpageinl`**：原文页界落在 “Let us form | the convergent Weierstrass product” 句中；用行内小号上标 `〔p.15〕` 才不会丢锚。
- 与 SPEC 骨架的出入：SPEC 示例把 `\srcpage{N}` 放在标题之后成行；本块对 p.12/13/16 改为 `\leavevmode\srcpage{N}` 紧贴后续正文行首（避免空段落，与 s02 的 p.3 写法一致），p.10/11/14 仍放在标题后成行（那里后面紧跟标题或环境，垂直模式下不产生空段落，已实测）。
- 本文件不设 `\setcounter{equation}{0}`：公式编号要接 s02 的 (1)–(5)，故让计数器自然延续。
