# 块 C · 译手决策记录（trace-chI-c）

四栏：判断点 / 依据 / 结论与理由 / 事后确认。记号约定：`A:` 表示有作者或工程依据，`J:` 表示译者判断。

## 一、结构与环境

| 判断点 | 依据 | 结论与理由 | 事后确认 |
| --- | --- | --- | --- |
| 本块是否重开 `\section{谱作用}` | 块 B 的 s02 已在 p.37 开 §I.10；SPEC「编号对象按原文编号、节号由整书自动排」 | 不重开。s03 开头只写一行注释 + `\srcpage{39}` + Remark I.10.3，避免整书出现两个 §10、并让 I.10.1–I.10.3 的计数器不被重置 | A/J: 已由块 B 的 s02 验证 §10 节头在其文件；本文件 `\section` 恰为 3 个（11/12/13） |
| Remark I.10.3 的环境 | SPEC 映射 Remark→`remark`；preamble `\newtheorem{remark}` 挂 `[theorem]` 计数器 | 用 `\begin{remark}`，编号由计数器自动给（整书为 1.10.3） | 编译输出「注 0.0.1」（单文件节号为 0，正常），编号链未断 |
| Problem I.11.1 用什么环境 | preamble 只定义 theorem/proposition/lemma/corollary/definition/example/construction/question/remark/conjecture/proof，无 `problem`；SPEC 映射表也无 Problem 条目 | 用 `question`（显示「问题 1.11.1」），编号与原文一致；环境名差异写入报告 §7 交 Lead 定夺，不擅自改 preamble | 编译通过且编号为 1.11.1（单文件为 0.1.1）；报告 §2 已标注「编号一致，环境名不同」 |
| I.13 呈现为「散文段 + 译者整理表」双轨 | 硬要求「做成可读的中文记号表，且与原文逐条对应」；同时 SPEC 要求逐段对照不改段序 | 5 段原文照译（不动原文叙述），其后加 `\subsection*{记号一览（译者整理）}` 的 `description` 表，19 条逐条对应并带页码。星号小节不进目录、不占编号，故不破坏逐段对照 | 目检 6 页：正文 5 段 + 表 19 条齐全；`\subsection*` 未出现在目录也不会被后续章节引用 |

## 二、术语与专名

| 判断点 | 依据 | 结论与理由 | 事后确认 |
| --- | --- | --- | --- |
| condensed 取「凝聚」还是「凝聚态」 | `术语裁定.md` 第 25 行 = 凝聚；`glossary.tsv` 第 148 行 = 凝聚态，二者冲突 | 裁定即冻结，取**凝聚**（凝聚数学、凝聚集、凝聚语言）。冲突不私自改表，写入报告 §5 第 4 条 | 全文 8 处「凝聚」，无「凝聚态」残留 |
| 人名是否首次括注原文 | BRIEF：人名按通行译名、首现括注原文；但 Fargues/Scholze 的首现发生在块 A 的引言 | 本块**一律用原文**，不再括注，避免与块 A 的首次括注重复、也避免读者以为这是首现 | 目检致谢长名单：Anschütz/Nekovář/Nizioł/Čésar 等变音符全部正常出字 |
| 文献标签 `[Far04]`、`[SW13]`、`[RV14, Conjecture 7.3]` | 硬要求「一律不译、不改」 | 全部照录，含方括号内的定理号与页码（如 `[Far12, Theorem 2 of the Préambule]` 照录） | PDF 提取核过 26 个标签，无一被 xeCJK 拆行或加空格 |
| `[CS]`、`[ČS19b]`、`[Lur09]` 的 Č/š | 原文 p.44 用 `[ČS19b]`；caron 属文献标签内容 | 保留 `Č`（不改成 C），与原文 bib 键一致 | 目检正常，未触发字体缺字 |
| etc.pp. 是否算笔误 | p.41 原文 "geometric Satake, etc.pp."；拉丁套语 *et cetera perge perge* | 判为**套语而非笔误**，正文译「等等」并加译注说明原写法，不静默规范化 | 报告 §4 第 3 条已记；§6 第 2 条保留低置信度说明 |
| anima 是否加译注 | 原文 I.13 自释 "for what is variously called spaces … ∞-groupoids, or homotopy types"；裁定「anima 不译」 | 不加译注（原文已自带定义，再加注是同一术语的二次注，违反「同一术语全书只注一次」的节约原则） | 报告 §4 末尾已说明理由，便于 Lead 复核 |
| 表外术语怎么处理 | 硬要求「表外术语保留英文写进报告 §5」 | perfectoid ball/sifted colimit/perverse-coherent/isocrystal 等一律**中文 + 括注英文 + 进报告 §5**，不私自写入 glossary.tsv | 报告 §5 共 11 行；正文首现均有括注（如「同晶（isocrystal）」） |

## 三、排版与符号

| 判断点 | 依据 | 结论与理由 | 事后确认 |
| --- | --- | --- | --- |
| 拉丁人名之间的连接号用 `--` 还是 Unicode en dash | 首版用 U+2013，xeCJK 把它当标点插入可拉伸 glue | 全部改 `--`（32 处）。理由是 en dash 在 `xeCJK` 下参与断行与对齐，justify 时会在「Nadler – Yun」之间撑出可见空隙 | 目检第 4 页：`Nadler--Yun [NY19]` 与 `Gaitsgory--Kazhdan--Rozenblyum--Varshavsky` 均连排无缝 |
| `D_{ét}` 的 é 怎么写 | XeTeX TU 编码下 `\mathrm{\acute{e}t}` 产出坏字（`Missing character ^^S`，PDF 提取为 `D￿et`） | 改 `D_{\text{ét}}`（3 处）：`\text` 走中文主字体链，é 由 ctex 字体直接提供 | 复编译 0 missing character，PDF 中 `D_ét` 字形正确 |
| 记号表用 `description` 的对齐参数 | 首版 `[leftmargin=5.5em,style=sameline]` 触发 `\enit@postlabel@i has an extra }` | 去掉 `style=sameline`，只用 `[leftmargin=6em]`；6em 恰好容下最宽标签 `A[X_1,…,X_n]` | 目检 19 条，最宽标签未压到说明文字 |
| 分类叠写 `*/G` 还是 `\ast/G` | 原文 p.44 明确「we write `*/G` instead of `BG`」，并解释是为避与 Borel 子群 `B` 混淆 | 译文写 `$\ast/G$`，并把原文那段「我们更偏好 `*/B` 而非 `BB`」的括号说明照译，保留作者的语气 | 目检 `\ast/G`、`\ast/B`、`$B(G)$` 三处不同记号未混 |
| 页标 `\srcpage` 放语义位置还是能显示的位置 | 试摆 4 轮发现位置一换显示就变（详见「弯路」3） | 一律放**语义正确处**（39 于 Remark 前、40 于跨页句「两种对偶描述」后、41/42/43 于各页首段前、44 于「Zhiyu Zhang 对第一版」处），宁可个别不显示也不让页标指错内容 | 目检 6 页：41、43 正常落边；39/40/42/44 未显示——问题上报报告 §7，不在本块硬凑 |

## 四、真实弯路

**弯路 1：build.bat 的反斜杠路径把 TeX 控制序列吃掉了。**
第一次按任务书原样调 `build.bat check sections\s03-chI-3.tex c`，报
`! Undefined control sequence. <argument> "sectionss 03-chI-3.tex"`。
成因有两层：MSYS bash 里 `cmd //c` 会退化成交互 shell，必须先 `MSYS2_ARG_CONV_EXCL='*' cmd.exe /c "…"`；而 build.bat 把参数原样塞进 `\input{"%~2"}`，`\s` 就此成了控制序列、`03` 被当作其参数吞掉。改用正斜杠 `sections/s03-chI-3.tex` 后一次通过。教训：凡是要进 `\input{}` 的路径，一律正斜杠。

**弯路 2：`\mathrm{\acute{e}t}` 的隐形坏字。**
编译只报三条 `Missing character: There is no ^^S in font [lmroman8-regular]`，不报 error；PDF 里肉眼几乎看不出，但 pymupdf 提取出来是 `D￿et`。顺着 `^^S` 定位到 `\acute` 在 `\mathrm` 内、XeTeX 的 TU 编码拿不到该组合字符。改成 `\text{ét}` 后消失。教训：`Missing character` 虽只是 warning，但等于静默丢字，必须当 error 处理；数学模式里的重音字符优先走 `\text`。

**弯路 3：`\srcpage` 的页标会静默消失（四次试摆）。**
为让 p.39/p.40/p.42/p.44 的页标显示出来，依次把它挪到定理环境内、段中、`\noindent` 之后、`\begin{remark}` 之前，共 4 轮；结果页标时有时无、且每次重编译丢的位置还不一样。又用 pymupdf 逐 span 扫 x<90 与 x>450 两条页边，确认不是双面排版奇偶页的问题。最终在 `源码/preamble.tex:38` 看到实现是 `\marginpar{\raggedleft\scriptsize\textcolor{yizhuGray}{p.#1}}`——`\marginpar` 在跨页段落与定理环境附近会被 LaTeX 静默丢弃（只给一条 `Marginpar on page 1 moved` 的 warning，甚至不给）。旁证：块 B 的 `_check_b.pdf` 丢了 p.25/p.28/p.32 三个、其余六个正常。结论是不在本块内硬凑（凑出来的位置都是错的），把六个页标放回语义位置并在报告 §7 建议 Lead 全局改用 `marginnote` 或加页对照表。

**弯路 4（较小）：嵌套在脚注里的译注会把标记弄丢。**
Hansen 的 hadal $t$-结构需要一条译注，但它出现在原脚注 7 里——把 `\yizhu` 直接嵌进 `\footnote{}`，编译后页脚多出一个悬空标记「3」、正文却没有对应注文（`\yizhu` 自己又生成一个脚注，嵌套脚注在 LaTeX 里不成立）。改为在 `\footnote{…}` 之后紧跟一条 `\yizhu`，正文出现「双射？²³」两个相邻标记。这个折中不漂亮但信息完整、来源可溯，遂接受并记录，未采用「把 hadal 注释塞进原脚注内部改写原文脚注」的做法（那会改动原文脚注的文本边界）。

**弯路 5（较小）：可选参数被标签里的 `]` 截断。**
`\item[$A[X_1,\dots,X_n]$]` 报 `! Missing $ inserted.`——`\item[...]` 的可选参数在第一个 `]` 处结束，标签里的 `]` 提前收尾。改用 `\item[{$A[X_1,\dots,X_n]$}]` 花括号保护后正常。教训：凡是写进 `\item[...]`、`\section[...]` 的标签，内含 `]` 一律加花括号。

**弯路 6（较小）：`style=sameline` 与 overfull。**
`\begin{description}[...,style=sameline]` 直接报 `! Argument of \enit@postlabel@i has an extra }.`（enumitem 的 sameline 与本版标签写法不兼容），删掉即好。另致谢前的人名串 `Gaitsgory–Kazhdan–Rozenblyum–Varshavsky [GKRV22]` 造成 `Overfull \hbox (15.91884pt too wide)`：在该段前后加 `\emergencystretch=2.5em`（段后复位 0pt）并在连字符后加 `\allowbreak`，最终 0 overfull。教训：长专名串优先给段落级 `\emergencystretch`，比逐词 `\allowbreak` 稳。

## 五、可复用结论

1. 本工程 `build.bat check` 的唯一可靠调用式：`cd 源码 && MSYS2_ARG_CONV_EXCL='*' cmd.exe /c "build.bat check sections/<file>.tex <tag>"`，路径正斜杠。
2. `Missing character` 一律当 error 追；`\mathrm{...}` 内不要放重音命令，改 `\text{...}`。
3. `\item[...]`、`\section[...]` 内出现 `]` 必须用 `{}` 包住整个标签。
4. `\srcpage` 目前会丢页标，属全局问题；块 C 的处理方式是「语义优先 + 上报」，后续块可沿用同一策略，待 Lead 统一修 `preamble.tex`。
5. 术语冲突（如 condensed）一律按 `术语裁定.md`，冲突本身只写报告、不改表。
