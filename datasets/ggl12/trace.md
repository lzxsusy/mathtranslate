# 决策记录（trace）

| # | 判断点 | 依据 | 结论与理由 | 事后确认 |
|---|---|---|---|---|
| 1 | 页码用 PDF 页序还是印刷页 | XREF 要求 + 抽查 p6/p101/p150 页脚 | 全文一律用 PDF 页序（pNNN 的 NNN）。页脚印的是 N−1，若用印刷页，verify_pages 与 sources.pages 会整体错一位。 | verify_pages 36 条全过；notes 骨架表的页码均按 PDF 页。 |
| 2 | **(2.28) 是不是笔误**（真弯路之一） | txt/12/p025.txt 只显示 "t2 = τ / τ"，我据 KW06 (3.50)(3.52) 复算，发现自洽需要 t²=τ̄/τ，遂怀疑 PDF 印成 τ/τ̄，准备按 §9.2 记 high 笔误 | 先不下结论，渲染 PDF p25 600dpi 裁图。结论：分子 τ 上有横杠，PDF 是对的，txt 抽取丢杠。**不是笔误，不记 errata**，改写进 notes「抽取陷阱」。若当时直接记 high，会冤枉作者，也会让卡片公式与原文相反。 | out/12_ggl12/external/p25_t2.png 存证；notes 4.1 第 2 条与 5 节均记明。 |
| 3 | 截图脚本输出路径报错（真弯路之二） | `FzErrorSystem: code=2: cannot open file 'external/p25_t2.png'` | 脚本 cwd 是仓库根（本库），不是 out/12_ggl12；external/ 只能放交付目录内，故改用 out/12_ggl12/external/p25_t2.png。 | 重跑成功生成 1946×848 PNG；同一脚本再生成 p30_psi.png。 |
| 4 | 打印 PDF 文本报 GBK 错（真弯路之三） | `UnicodeEncodeError: 'gbk' codec can't encode character '\u2212'` | Windows 控制台默认 GBK，PDF 里有 U+2212 减号。所有 PyMuPDF 脚本前加 PYTHONIOENCODING=utf-8，不改数据。 | 重跑正常输出；后续所有脚本沿用该环境变量。 |
| 5 | v2 comment 说 148 pp，实际 150 页，是否记 inconsistency | arXiv abs 页 comment "148 pp"；PDF 共 150 页，含 1 页 arXiv 封面，印刷页 1–149 | 不记 errata：148/149/150 的差是封面与计数口径，不是数学内容不自洽；记进 notes 外部来源表第 4 行备查。 | 逐页核对页脚 N−1 一致（p6→5、p101→100、p150→149）。 |
| 6 | E1（p20 "D3Xa" 应为 "D3Xc"）定级 | 同页 (2.8) 指标为 c、a 是参数；但只有本篇内部这一处，无第二独立出处 | 按 §9.2 记 low（仅内部不自洽、一处冲突），不记 high。卡片保留原文写法，provenance_note 标「存疑（见 errata E1）」。 | lint 接受（high 才强制依据2）；notes 勘误第 1 条写明。 |
| 7 | Khovanov 卡与旧卡撞名 | `term_index.py check` 报与 functoriality/…/khovanov-homology 同英文名 | 旧卡讲函子性，本卡只讲 (1.8)(1.9) 的双分次与 Euler 特征；不重复造卡，改题「Khovanov 同调的双分次结构」并加限定 alias，旧卡 id 记入 notes 3.1。 | 再跑 check：0 撞名。 |
| 8 | Nahm pole 卡与 ggl22/ggl13 撞名（真弯路之四，两轮） | 第一次 check 撞 ggl22 中文名；改名后又撞 ggl13 英文 alias "Nahm pole boundary condition" | 第一轮只改中文题名不够；第二轮把 alias 换成 "Nahm pole (principal embedding)"。教训：term_index 同时查 title 与 aliases，改名必须两处都动。 | 最终 check：18 张卡 0 撞名。 |
| 9 | 概念卡取 12 还是 13 张 | TASK 允许 12±2；§6（单值化缺陷）作者自己说 "there is plenty to understand"，且 §6.3–6.4 未细读 | 取 13 张：C1–C12 覆盖 §1–§5 主线，C13（Morse）补 §5.3.2，因为它解释 F 为何是 Z 分次；§6 不单列卡，只进 terms.tsv 与 notes 骨架，避免为未完成章节造卡。 | lint 报「概念 13 / 推导 5」，在 12±2 与 5±1 内。 |
| 10 | 定理 proof.status 怎么标 | 逐条回原文看证明程度：CS→Jones 引 [12]；Nahm 唯一性只说 "we require"；(4.10) 原文 "conjecturally"；ζ 的 (−1)^F 不变性原文 "not clear"；Morse 流方程原文 "straightforward exercise" | 分别标 gap/gap/gap/gap/sketch，并各写 gap_note。宁可显得弱，也不把引用当证明——否则卡片会替作者宣称未证之事。 | notes「不懂」6 条与各 gap_note 呼应；lint 对 sketch/gap 只要求 gap_note，已满足。 |
| 11 | (5.53) 的 1/4 是否与 (3.11) 冲突 | (3.11) P=(1/2h∨)(1/32π²)∫εTr_ad FF；h∨=2 时 1/2h∨=1/4；p1=(1/8π²)Tr F∧F | 一致，不记 errata。差别只是 1/4 是 SU(2) 的 h∨ 特例，一般 G 用 1/2h∨。 | notes 4.1 第 4 项与「不懂」第 3 条记明 p1 约定未独立核。 |
| 12 | 外部来源选哪几处 | BRIEF §9 要求 ≥3 独立来源，且公式须 ≥2 处独立出处 | 选 KW06（公式互证最强）、nLab（对偶链与迹解释）、Witten 1108.3103（作者自述仍称 candidate）、arXiv abs 页（v2 元数据）。G2 数值只是内部自检，不计独立来源。 | notes「外部来源」表 5 行（4 独立 + 1 自检），lint 通过。 |
