# PATCH_LOG —— Lead 落改记录（全部 exact-match，命中数核对后写入）

> 原则：不用正则批量改正文；每条替换要求命中数符合预期，否则跳过并报告（见 `tools/patch_*.py` 输出）。
> 本文件记录 2026-11-04 全部落改，供交付前审计。

## A. 工程/版式（Lead 自有文件）

| # | 文件 | 改动 | 原因 |
|---|---|---|---|
| A1 | `src/preamble.tex` | 图宏重构：`\figimg{文件}`（无图注自闭合）与 `\figfigure[宽]{文件}{图号}{图注}`（图片+图注同一 minipage，绝不分页拆开）；`\figtitle` 仅保留为旧写法兼容（实际已不用） | 初版 `\figimg`/`\figtitle` 分两句会被分页拆开（图 4.1 图注曾跑到下一页） |
| A2 | `src/preamble.tex` | 加 `\graphicspath{{figures/}}`；加 `\ii,\ee,\dd,\Log`；TikZ 形状库 `shapes.geometric/shapes.misc/shapes.arrows` 等 | 译者用到 `\ii,\Log`、`\node[ellipse]`、`p4_fig*.png` 相对路径 |
| A3 | `src/preamble.tex` | 页眉 `\chaptermark` 用「第\thechapter 章」+ 标题，去掉 \MakeUppercase；`\emergencystretch=3em` | 页眉曾显示英文 "Chapter"、标题被强制大写；Overfull 19→3 |
| A4 | `src/preamble.tex` | `\refitem` 宏（参考文献条目，悬挂缩进） | gen_refs 输出格式 |
| A5 | `src/main.tex` | 第 6 章 papersource 后加资助说明小字块（NSF CAREER DMS-1944952 + Sloan；Simons #635846 + NSF DMS-2204109） | 原文 p1 作者资助脚注，译者块未含（tr-07 校对 M1） |
| A6 | `work/figures/p4_fig01–11.png` | 重裁：紧按「drawings ∪ 图内文字标注」bbox，400 dpi | 初版按整行宽裁、白边占 50% 导致显示过小（tr-05 校对 O2） |
| A7 | `work/figures/p3_p13/p14/p17/p39.png` | 第 3 章 4 张无编号插图（tr-02/tr-03 裁，Lead 复核） | 底本普查漏项，已补入 BRIEF/README |
| A8 | 全部 chunk | `\figtitle{N}{...}` 合并进 `\figfigure`（11 处，精确两行替换）；无图注图保持 `\figimg` | 见 A1 |

## B. 译文落改（交叉校对报告 → Lead 执行）

| # | 来源 | 目标 | 改动 | 处数 |
|---|---|---|---|---|
| B1 | tr-05 → tr-04 | tr04c/tr04f | `\mathbb{M}_\R,\N_\R` → `M_\R,N_\R`（原文斜体 M、N；且 \N 与自然数撞车） | 7 |
| B2 | tr-05 → tr-04 | tr04a/tr04b | `\rtimes` → `\times`（页图印作 ×）+ Tutor Note 说明半直积含义 | 2 |
| B3 | tr-05 → tr-04 | tr04d | 「奇点轨迹」→「奇异轨迹」（glossary singular locus） | 1 |
| B4 | tr-01 → tr-06 | tr06b/tr06c | 跨引用节号改本书编号：第 4 节→第 4.4 节（3 处）、第 10 节→第 4.10 节（1 处） | 4 |
| B5 | tr-01 → tr-06 | tr06d | 定理 6.5.1 条件(2) Ω 去 check；两处英文定理名→「定理/命题」；9 处跨引用改本书编号（定理 6.4.2、式 (6.5.1)/(6.5.2)/(6.5.3)/(6.6.1)、第 6.6.1 节、定理 6.5.1/6.5.2） | 12 |
| B6 | tr-07 → tr-01 | tr01f/tr01d/tr01b/tr01c | 第 6 章 p12 虚数单位 `\mathbf{i}`→`i`；删多译「恰当」；第 2 章 p10→p11 跨界句按「开始者写完」移入 tr01b | 3 |
| B7 | tr-08 → tr-07 | tr07a | 「第 2、3、4、5、6 章」→「第 5.2–5.6 节」 | 1 |
| B8 | tr-03 → tr-02 | tr02f | 「环面 strata」「零维 strata」→「环面分层」「零维分层」 | 2 |
| B9 | tr-04 → c01 | c01c | 「全纯 Hitchin 系统」→「亚纯 Hitchin 系统」；`hyperK\"ahler`→「超 Kähler」；「完全的 hyperKähler 度量」→「完备的超 Kähler 度量」 | 10 |
| B10 | tr-04 → c01 | c01b/c01c | 「log Gromov–Witten」→「对数 Gromov–Witten」；「分片光滑」→「分段光滑」；`$(X_{t_i},g_i)$`→`$(\mathcal{X}_{t_i},g_i)$`；删冗余「出人意料的、意想之外」；c01c 头注释 pp.10–14→pp.10–15 | 5 |
| B11 | Lead 全书归一 | 全部 chunk | 「twistor 空间」→「扭量空间」（4）；「消失轮」→「消没轮」（2）；`hermitian`→`Hermitian`（1）；「分片」→「分段」（tr02e/tr07d/tr08a/b/c 共 9） | 16 |

## C. 术语与文档

| # | 文件 | 改动 |
|---|---|---|
| C1 | `work/glossary.tsv` | 由 100 条扩充到 225 条（合并 tr-01/02/03/04/05/07/08 回报的新术语 + 统一「扭量空间/消没轮/校准子流形」等） |
| C2 | `work/STYLE_GUIDE.md` | §1.3 增补：原文按节编号对象用「章.节.原编号」，按全章连续编号对象（Question/Remark）用「章.原编号」 |
| C3 | `work/BRIEF.md` | 增补「正文延伸进参考文献起始页」表；第 3 章 4 张无编号图 + 1 张无编号表；第 4 章无 p65 正文、无致谢 |
| C4 | `work/TIMELINE.md` | 边界裁定（开始者写完）与跨译者边界通知记录 |
| C5 | `work/README.md` | 交付说明：底本信息、结构、编译、体例、原文笔误登记表、统计、已知限制、版权 |

## D. 校验脚本（`work/tools/`）

`check.py`（Gate 1：tag 集合/括号/环境/$/禁用命令/编码/markdown）、`verify_pdf.py`（Gate 3：tag 回读/图/字体/异常文本/目录）、`coverage.py`（页覆盖）、`gen_refs.py`（参考文献转录）、`gen_notes.py`（译注汇总）、`pack.py`（打包）、`patch_*.py`（落改）、`extract_figs.py`（图裁切）、`crop.py`（公式裁图，按论文 key）。
