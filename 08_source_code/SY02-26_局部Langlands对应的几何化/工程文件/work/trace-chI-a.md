# 块 A · 决策记录（trace）

格式：判断点 / 依据 / 结论与理由 / 事后确认。★ = 真实走过的弯路（先做错，发现后改回）。

| # | 判断点 | 依据 | 结论与理由 | 事后确认 |
| --- | --- | --- | --- | --- |
| 1 ★ | 编译命令怎么写 | 第一次写 `cmd //c "build.bat check …"`，只打印 cmd 版权行、exit 0、什么也没编译 | 改 `cmd.exe /c "build.bat check sections/s01-chI-1.tex a"`。`//c` 被 MSYS 当成路径改写，等于没传参数 | 反复三次均正常输出 `[OK] _check_a.pdf` |
| 2 ★ | build.bat 的参数用正斜杠还是反斜杠 | 用 `sections\s01-chI-1.tex` 时编译报 `! Undefined control sequence. <argument> "sectionss 01-chI-1.tex"` | 必须用正斜杠。build.bat 把参数原样写进 `\input{"…"}`，反斜杠的 `\s` 被 TeX 当控制序列吃掉 | 改 `sections/s01-chI-1.tex` 后一次通过；这条也写进了给 Lead 的回报 |
| 3 ★ | `étale` 怎么排 | 初稿写 `\mathrm{\acute{e}t}`，日志出现 `Missing character: There is no ^^S in font [lmroman8-regular]` | 改为 `\text{ét}`（xeCJK 下正文字体有 é）。缺字违反质量门，不能留 | `grep -c "Missing character" _check_a.log` = 0 |
| 4 ★ | p.11→p.12 的跨页句 | 原文「Unfortunately, the map R→R((t)) does not admit any sections」跨页，我起初按页界拆成两段 | 合回同一段，跨页处只放行内锚点 `\srcpageinl{12}`。逐段对照要求段数与原一致，不能因页界造段 | 重读原文 p.11 末/p.12 首，确认是一个句子；段数核对通过 |
| 5 ★ | `\srcpage` 为什么不印 | p.7/10/12/14 的页边注在 PDF 里完全没有；日志无 Marginpar 警告 | 先改 `\leavevmode\srcpage{N}正文`（水平模式），p.12/14 仍丢；preamble 换成 marginnote 后仍丢 4 个（7/10/16/18）；加 `\leavevmode\mbox{}` 前置也无效 | 最终这 4 个改 `\srcpageinl`（上标〔p.N〕），`check_pagemarks.py` 两项 `[ok]`；版式不统一记入报告 §7 |
| 6 ★ | Rem I.2.13 的环境闭合 | 编译报 `! LaTeX Error: \begin{remark} on input line 362 ended by \end{document}.` | 写 p.17 时漏了 `\end{remark}`，补上即通过 | 重编译 12 页 `[OK]`；此后每次新增环境都数 begin/end（现 10/3/1/7 全配对） |
| 7 ★ | p.12 `Ė` 到底是什么 | OCR 给 `E`；按 `E-向量空间` 写过一次，读到同页 `maps F_q((t)) = E → R` 觉得不通 | 回 150dpi 原图：是 `\breve{E}`（短音符），且 `\breve E=\ol{\FF}_q((t))`，OCR 连 `\FF_q` 的上划线一起丢了 | 全篇 `\breve E` 检索 12 处，均与图一致；报告 §3 列为第 2 条转录错误 |
| 8 ★ | `G-Isoc` 与 `G-𝓘soc` 是同一个东西吗 | p.9 图上 `G-Isoc` 是正体（groupoid），p.10 起图上 `G-` 后是花体 `𝓘soc`（prestack），p.15 又回到正体，p.16 Rem I.2.10 又花体 | 二者是不同对象（groupoid vs 其上之叠），全书刻意用字形区分。译文分别用 `G\text{-}\Isoc` 与 `G\text{-}\mathcal{I}\mathrm{soc}` | 逐页对照四处出现，与原文一致；此判断写进报告 §3 末尾 |
| 9 | 章节标题是否写原文编号（I.1/I.2…） | SPEC 定死：编号不写进标题，靠 LaTeX 自动编号 | 标题只写中文译名（英文原题放行尾 `%` 注释）。理由：本书是 `book` 类、章号自动为 1，节号 1.x 正好等于 I.x | 实测 21 个对象的自动编号与原号**逐个相等**（1.2.1…1.4.1），故 §2 对齐表 21 行全部「一致」 |
| 10 | Def I.2.2 的 `\end{definition}` 放哪 | p.13 首行是斜体 `where the Frobenius φ acts on (R,R^+)`，字体与定义体一致 | 该行属定义体内的限定语，`\end{definition}` 移到它之后、且锚点 `\srcpage{13}` 置于该行前 | 编译后定义 1.2.2 的编号与斜体范围正确；p.13 首行仍为斜体 |
| 11 | `κ` 上划线位置的判读 | 150dpi 下 `π_1(G_E)_Γ` 的横线疑似压在 G 上 | 用 400dpi 局部裁切（`clip` 参数）放大，确认横线在 E 上 → 录 `\pi_1(G_{\ol E})_\Gamma`，与同页 `\Gal(\ol E|E)` 一致 | 放大图存 `_z1.png` 后即删；正文两处 `G_{\ol E}` 统一 |
| 12 | p.22 末句跨到 p.23 怎么收 | 原文 p.22 页末是「For」，句子在 p.23 继续，而 p.23 不属本块 | 依页界止于「对于」，不补写、不改写；交接点写进报告 §6 第 4 条 | 文件末行即「…给出。对于」；编译无「paragraph ended before」类错误 |
| 13 | 译注用 `\yizhu` 还是 `\yizhuw` | TASK 要求有依据的写来源、无依据才用 `\yizhuw` | 15 条全部有据（原文他处、§III.2、glossary、nLab 级常识），故全用 `\yizhu`，`\yizhuw` 0 条 | `grep -c '\yizhuw'` = 0；每条来源均标 A:/I: 等级 |
| 14 | 术语取舍：basic / semistable / proper | 术语裁定表（已冻结） | 分别作「基本的」「半稳定」「紧合」；`unipotent group diamond` 保留英文＋括注「幂幺群菱形」 | 全篇检索一致，无第二种译法 |
| 15 | 公式里的 `\GL`、`\Spd` 等未定义宏 | preamble 只定义了 `\Bun \Spa \Div \Hck \Gr \Isoc \Vect \Rep \QCoh \Spec \Aut …` | 不用自造宏，直接写 `\mathrm{GL}_n`、`\mathrm{Spd}`、`\mathrm{Perf}`、`\mathrm{BC}`、`\mathrm{Proj}`；`\GL_n` 出现后统一 sed 替换 | 编译 0 个 `Undefined control sequence`；不改 preamble（非我所有） |
