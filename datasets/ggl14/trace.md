# 工作轨迹（trace）

四栏：判断点 / 依据 / 结论与理由 / 事后确认。带「弯路」标记的条目是实际走错后修正的。

| # | 判断点 | 依据 | 结论与理由 | 事后确认 |
| --- | --- | --- | --- | --- |
| 1 | 页码用 PDF 页还是印刷页 | 渲染 p002/p025/p026 见页脚 1/24/25；TASK.md 的页码约定 | 一律用 PDF 页序（PDF = 印刷 + 1）。理由：sources.pages、anchor、verify_pages 都以 txt/14/pNNN.txt 为准，混用会在回查时错位一页。 | verify_pages 42 条 quote 全部命中指定页，0 问题。 |
| 2 | 本会话怎么读文件 | 调 read 报 `unknown tool "read"`；ops_inspect_local_file 用相对路径解析到 Downloads 报 NOT_FOUND | 先用 working_directory 把 cwd 设到仓库根，再用 ops_inspect_local_file / ops_grep 传仓库根相对路径。理由：文件工具以 session cwd 为基准，不认「仓库根」这个概念。 | 此后所有读写正常；未再出现 NOT_FOUND。 |
| 3 | txt 抽取能不能直接当 quote | 初读发现 (1.5) 被压平成 `q = exp 2πi k + 2`、τ 对偶句乱序、`2^7` 变 `27` | 凡要进 sources.quote 的句子，先渲染 PDF 该页核对；压平行一律不用。理由：verify_pages 只做去标点匹配，压平行会假命中或假失败。 | (1.5) 在 p004 渲染为 `q = exp(2πi/(k+2))`，排版正确，只是 txt 丢失结构；该句因此不进 quote。 |
| 4 | **弯路①**：p13 的 τ 对偶句是不是笔误 | txt 作 `τ ∨replaced by τ = −1/ngτ ∨`，看上去主客颠倒 | 初判为笔误并准备进 errata。渲染 p013 后见原文是 `coupling parameter τ∨ replaced by τ = −1/(n_g τ∨)`：它与常见写法 τ∨=−1/(n_gτ) 互为逆写，且 n_g 对 G 与 G∨ 相同，**自洽，不是笔误**。撤回该条 errata，改记入 notes §4 的「记号陷阱」。理由：把等价改写当错误，会污染 errata 并误改卡片。 | errata.tsv 最终只有 E1/E2/E3 三条；notes §4 末段记下该陷阱与「不可用作 quote」。 |
| 5 | **弯路②**：p19 的 π₄ 表编号 | 早期阅读笔记把它记作 (2.16)，卡片正文与 errata 依据都照抄 | 写 errata 的「依据1」时想到要回查式号，grep 全篇 `2.16` 无命中，渲染 p019 见该表**无编号**。于是把卡片、errata、notes 里的 (2.16) 全部改成「π₄(G) 表」。理由：audit_locators 要求 locator 里的式号必须出现在所列页，编造编号会直接失败。 | 全包 grep `2.16` 无残留；audit_locators 通过。 |
| 6 | XREF 说 arXiv 元数据抓取失败，是否放弃外部校正 | XREF.md 的记录 + 任务书要求核 arxiv.org/abs 与 INSPIRE 1278911 | 改用 web_fetch 直接抓：abs 页摘要与 p1 逐句一致、26 pp、仅 v1；INSPIRE API 给 47 条参考文献与 26 页。理由：「抓取失败」是上一次的工具限制，不是文献本身的问题。 | notes 外部来源表第 1、2 行；figures caption 里的 3+2+2=7 与原文 p2 互证。 |
| 7 | E1（Sp(2n+1)）给什么置信度 | 同篇 p019 正文与 π₄ 表均作 Sp(2n)；π₄=Z₂ 只对偶数维辛群；库内 ggl12 对偶对表 G∨=SO(2n+1) ↔ G=Sp(2n)，全篇无 Sp(2n+1) | high：两处独立出处（本篇 p19、ggl12 卡）且与 p14 自身冲突。按 BRIEF §9.2 改卡 + 记账。 | errata E1 依据1/依据2 均已填；even-odd 卡加 corrections 并改写为 Sp(2n)。 |
| 8 | E2（脚注 4 缺括号）给什么置信度 | 同页 (1.5) 的 n_g=1、h∨=2 特例只能由分母读法还原；库内 ggl12 (3.13) q=exp(2πi/(n_g(k+h∨))) 同读法 | medium：同篇内部可判读，但「印刷缺括号」这个判断只有一处外部支持（ggl12），按纪律不升 high。 | dual-instanton-q 卡按订正后的式子写，并加 corrections 指向 E2。 |
| 9 | 卡片 related 能不能指向 ggl12 的卡 | lint 首轮报 `related 指向不存在的卡：ggl14/deriv/...` | 不能：related 必须是本包已存在 id；跨篇接口一律写进 notes §3 的表。理由：related 是包内图结构，跨包会破坏 lint 与后续索引。 | lint 通过；notes §3 列出 11 条接口（ggl12/ggl13/ggl10/gtgl15/kw06/ggl22/seidel）。 |
| 10 | 概念卡与推导卡的张数 | TASK 要求概念 8±2、推导 3±1，并给了「值得建卡」清单 | 概念 10：顶点模型、framing 因子、CS 与 Wilson 圈、Lefschetz 顶针、KW 方程、q 作瞬子数、H=H(V,Q)、五维提升、Nahm 极点、even/odd；推导 4：CS→KW、q 作瞬子数、5d→Khovanov、Nahm 极点由 KW 约化。理由：两讲各自的主链都要有对应卡，且推导卡覆盖三条「主链」。 | 卡 10 概念 + 4 推导，lint 无错。 |
| 11 | 中文定名怎么取 | 库内 datasets 既有 terms.tsv：Lefschetz thimble = Lefschetz 顶针（沿 seidel 包旧译，明确不用「指套」） | 沿用既有定名，不新造；Stokes 现象、扭化、BPS 不译等同样沿用。理由：术语表要跨篇可比，个人偏好让位于库内一致性。 | terms.tsv 27 条，term_index check 通过。 |
| 12 | quote 明明抄对了，verify_pages 却报搜不到 | p11 两条 quote 被 verify_pages 判为「原文里搜不到」 | 原文是 `actually a gauge-fixed version of the instanton equation`，我多写了句首 `it is`。去掉后通过。理由：quote 必须逐字连续，不能用省略号补主语。 | verify_pages 42 条 0 问题。 |
| 13 | locator/anchor 里要不要都写式号 | audit_locators 规则：取段内第一个 p.N 与该段所有 (x.y)，要求式号出现在这些页的 txt 里 | 只写该页确实印出的式号；p19（π₄ 表）、p21（约化方程）、p23（范畴）等无编号公式处只写节名与主题。理由：宁可少给定位，不可给错定位——错定位会让审计误报并掩盖真正的问题。 | audit_locators 通过；式号 1.1–1.26、2.1–2.15 与各页一一对上。 |
| 14 | 要不要把 volume conjecture 单独建卡 | 第一讲 p5–p10 花了不少篇幅在复临界点与顶针相消上，且与 ggl10 有接口 | 不单独建「volume conjecture」卡，而把顶针机制并入 lefschetz-thimble 卡，volume conjecture 只在要点与 notes 接口里提。理由：本篇对 volume conjecture 只作评述（作者明说未解决），建卡会把评述当结论。 | 顶针卡覆盖 (1.9)–(1.20)；notes §3 指向 ggl10 的三张卡。 |
| 15 | 交付前怎么自检 | TASK 第 8 条与「完成后回报」列出的四条命令 | 依次跑 lint（--strict）、verify_pages（--strict）、term_index check、audit_locators，全部 OK 后把 status 由 draft 改 dev。理由：四条命令分别管结构、引文回查、术语、定位审计，缺一不可。 | 见文末「收尾检查」一节的实际输出。 |
| 16 | **弯路③（收尾复核）**：term_index 报 4 处撞名，能否按「退出码 0」算通过 | check 退出码 0，但输出列了 4 处：CS 卡与 ggl12 同名同题，另 3 个裸 alias 分别撞 ggl12/ggl13/seidel | 不能算通过。按库内纪律「同概念不重复造卡、译名以旧卡为准」，逐条判断后给 4 张卡加限定词：CS 卡改题「Chern–Simons 配分函数与 Wilson 圈」；五维提升 alias 加 "with time direction"；顶针 alias 加 "in complex CS"；Nahm alias 加 "from KW equations"。id 不变，跨篇接口不动。理由：保留裸同题会让索引里出现同题双卡，也无法区分两篇的取景。 | term_index 重跑 0 撞名；lint/verify 复跑 0 问题；notes §3.1 补记处理结论。 |
