# 块 A 校对 · 决策记录（trace-proof-chI-a）

对象：`源码/sections/s01-chI-1.tex`（§I.1–§I.4，p.7–p.22）。每条记：判断点 / 依据 / 结论与理由 / 事后确认。

## D1 段落判据怎么定（先错后对，真实弯路）
- 判断点：原文「一段」在版面上如何与「显示公式后的续排」区分？
- 依据：最初用「首行有缩进＝新段」的目测启发式，判 p.7「In the nonarchimedean case」为新段（**误判**）。改用 pymupdf 逐行取 `bbox.x0` 后发现：本排版新段首行缩进固定 x0=82.7pt，续行（含显示公式后的续排）x0=64.8pt。
- 结论：以 x0 数值为唯一判据，并用三个反例基准校准——p.12「Definition I.2.2.」、p.15「The semistable locus」、p.19「Implicit here」都是 x0=82.7（显示公式后另起的新段仍缩进）。
- 事后确认：p.7「In the nonarchimedean case」行 x0=64.8，与「…π of G(E).」同行续排 → 同段；译文 L25–L29 未分段，正确，不改。

## D2 三处「多分段」的认定
- 判断点：译文比原文多出的段界是处理自由，还是错误？
- 依据：逐页列段首清单（p.10 五个：117.5 / 162.6 / 306.0 / 456.0 / 539.6；p.14 六个；p.22 首行 y=117.5 x0=64.8）。译文在这三处把同段切成两段：L109「改变 $G$-主丛的平凡化…」、L236「更一般地…」、L553「这里 $\mathrm{BC}(\cO(1))$…」。
- 结论：BRIEF §4 要求逐段对照，故按原文合并（删 3 个空行；p.22 处同时删 `\noindent`）。
- 事后确认：重编译（16 页、0 error）后渲染三处，合并段落首行不再缩进、行文连贯。

## D3 页锚命令的选择（p.22）
- 判断点：合并后 p.22 的锚点还该用 `\srcpage{22}` 吗？
- 依据：`preamble.tex:51` 注释明说「页界落在句子中间时用 `\srcpageinl`」；`\srcpage` 走 `\marginnote`，在段中位置（紧随 display 之后）易不落版；其余 9 处段中页界全部用 `\srcpageinl`。
- 结论：p.22 改 `\srcpageinl{22}`，与全块体例一致；锚点总数不变（16）。
- 事后确认：`check_pagemarks.py` 报「16 锚点全部在 PDF 中可见」「p.7–p.22 锚点齐全」两个 `[ok]`。

## D4 「恰当」是不是错字
- 判断点：L73「它是基本的恰当它只有一条斜率」——异体/方言用法还是漏字？
- 依据：原文 p.9「it is basic precisely when it has only one slope λ」；同一文件 L278 同一句式正确作「当且仅当」。
- 结论：漏字，改「当且仅当」。
- 事后确认：编译 PDF 该句为「它是基本的当且仅当它只有一条斜率 λ」，语义与原文一致。

## D5 斜率记号 H 还是 D
- 判断点：p.9「as $H_\lambda$ for some slope λ」——OCR 里 H/D 易混。
- 依据：300 dpi 裁剪回图，字形明显是 $H_\lambda$。
- 结论：译文 L75 的 $H_\lambda$ 正确，不改。
- 事后确认：无 diff（本处零改动）。

## D6 p.12 两处 $(\bar{\mathbb F}_q)$ 上划线
- 判断点：译文 L149 用 $\ol{\FF}_q((t))=\breve E$、L151 用 $\FF_q((t))$（无上划线），是笔误还是原文两处本就不同？
- 依据：回图对照，原文确为「maps $\bar{\mathbb F}_q((t))=\breve E\to R$」与「continuous maps $\mathbb F_q((t))\to R$」两句，一处有一处无。
- 结论：译文分别对应，正确，不改。
- 事后确认：无 diff。

## D7 p.22「is a also」复核（译手请求复核项）
- 判断点：该处是 OCR 噪声、排版拆行假象，还是原文确实印错？
- 依据：300 dpi 裁剪 p.22 第 3–5 行，原文印作「Part (iv) / is a also consequence of Theorem I.3.4.」，行断点正在「is a」之后。
- 结论：原文确实如此（a also 语序笔误），**不是** OCR 假象；译注 L574 判断成立，译文按「也是……的推论」处理得当。正文不改，依据写入报告 §4；收尾时发现 `work/errata.tsv` 已有 E1 覆盖此处（见 D15）。
- 事后确认：报告 §4 第 4 条已附该依据。

## D8 Vogan 论文题名（译注事实错）
- 判断点：译注 L40 写 Vogan, *On the local Langlands conjecture*（[Vog93]），题名对不对？
- 依据：原书参考文献 p356：`[Vog93] D. Vogan, Jr., The local Langlands conjecture, Representation theory of groups and algebras, Contemp. Math., vol. 145, Amer. Math. Soc., Providence, RI, 1993, pp. 305–379.`（无「On」）。
- 结论：改题名为 *The local Langlands conjecture*；只改题名，不动译注其余文字（红线：不删译注）。
- 事后确认：tex 现有 `\emph{The local Langlands conjecture}`；报告 §2 第 5 条。

## D9 脚注编号实测（译手报 4/5/10/19，实测不同）
- 判断点：译注与作者脚注共用 `\footnote` 计数器（`preamble.tex:29–31`），作者原注 1–4 实际显示成几号？
- 依据：从编译 PDF 的脚注区逐条提取编号与首句：1/2/3＝译注（朗兰兹对偶群、L-包、本质上是双射）；4＝作者注 1（不消说…）；6＝作者注 2（把 $[\ast/G(E)]$ 换成…）；10＝作者注 3（这个结果似乎为专家所熟知…）；17＝作者注 4（事实上，我们只在 $E$ 为 $p$-进时…）。
- 结论：实为 **4、6、10、17**（译手报告 4/5/10/19 有误，5 与 19 是译注）。属体例问题非本块错字；报告 §4/§6 给出评估与建议（倾向「可接受＋凡例说明」，不动 preamble）。
- 事后确认：报告 §1 维度 5、§4 末段、§6 第 2 条均已按实测编号书写。

## D10 译注第 15 条出处（§III.2）可疑
- 判断点：L293 注称「幂幺群菱形…完整定义见 §III.2」，出处成立吗？
- 依据：全书 OCR 文本中 `unipotent group diamond` 仅出现在 p.15（本块使用处）；Chapter III 的 §III.2 是「The topological space $|\mathrm{Bun}_G|$」，其 §III.2.4 讲 Kottwitz 不变量的局部常性，p090/p103/p105 只出现 unipotent group scheme / "unipotent group" / unipotent radical。
- 结论：出处可疑，但可能的正确指向（§III.4 semistable locus 一带）无法确证；按红线不删不改译注，报报告 §4-5 交 Lead。
- 事后确认：报告 §4 第 5 条。

## D11 译注第 3 条引 p.36：成立
- 判断点：L23 注称原文 p.36 明确写到「对 GLn 与一般的 π，φπ 即通常所谓的半单 L-参数」。
- 依据：`01_pages/p036.txt:53–56` 原文「(ix) For G = GLn and supercuspidal π… Note that parts (viii) and (ix) together say that for GLn and general π, the L-parameter φπ is what is usually called the semisimple L-parameter.」
- 结论：引文准确，成立；不改。
- 事后确认：报告 §4 第 2 条。

## D12 p.21 (iv)/(v) 与 p.87 定理 III.0.2 编号互换
- 判断点：这算本块译错吗？
- 依据：本块译文与 p.21 原文逐条一致（(iv) 局部闭 + 上同调光滑 + $\langle 2\rho,\nu_b\rangle<2$；(v) 半稳定轨迹开 + 无交并）；通读笔记与 `疑点清单.tsv` 第 41 行均判「已解：原文自身不统一」。
- 结论：**不是本块错误**，不返工；仅报告 §6 提醒 Lead；`work/errata.tsv` 的 E4（open）即此条，见 D15。
- 事后确认：报告 §6 末段。

## D13 编译调用方式（真实弯路）
- 判断点：怎样在 MSYS bash 里跑 `build.bat`？
- 依据：`cmd //c build.bat check sections/s01-chI-1.tex pa` 只弹出交互式 cmd（banner + 提示符，无构建输出，**退出码 0**）——MSYS 的路径转换吃掉了参数，是假成功。改为 `MSYS2_ARG_CONV_EXCL='*' MSYS_NO_PATHCONV=1 cmd.exe /c 'build.bat check sections/s01-chI-1.tex pa'` 才真正构建。
- 结论：以后一律用后者，并以「产物 `_check_pa.pdf` 是否存在＋日志 0 error」判成功，不看退出码。
- 事后确认：得 `[OK] _check_pa.pdf`，16 页，`grep -c '^!'`＝0，Overfull/Underfull 均 0。

## D14 黑名单与越界检查
- 判断点：有无套话、来源黑名单、本机绝对路径、越权改文件？
- 依据：grep「显然/众所周知/不难看出/容易看出」＝0；「知乎/百度百科/CSDN/简书/公众号/博客」＝0；`C:\`、`/Users/`＝0；「的的」「了了」＝0。改动只落在本 section（5 处），preamble/main/build.bat/其他 section/glossary/01_pages 未碰。
- 结论：无问题，无需改动。
- 事后确认：报告 §1 维度 10、§5；`git` 不可用（非仓库），改用逐处 sed 复核改动点。

## D15 errata 台账核对（收尾发现）
- 判断点：报告原打算「建议把两处作者笔误登 errata」，但项目里是否已有勘误台账、已记了哪几条？
- 依据：`工程文件/work/errata.tsv` 已存在，表头为「序／位置／原写法／订正／依据1／依据2／置信度／影响卡片／状态」；已有 **E1**＝p.22「is a also consequence」→「is also a consequence」（high，**fixed**）、**E4**＝p.21 §I.4 的 (iv)/(v) 与 p.87 定理 III.0.2 对调（low，**open**），E2/E3 属其他块。
- 结论：不重复提案、不改台账（不属可写文件）。报告 §0/§4/§6 改口径为「E1 已登记、E4 已登记」，只建议**补登 E5**＝p.14「a map $S\to\Spa E$」漏 $\sharp$（译文照译，正文不改）。
- 事后确认：报告 §0、§3（p.14 行）、§4 第 4 条、§6 第 1 条四处均已改口。

## D16 「锚点印出来了」不等于「锚点位置对」（方法学）
- 判断点：`check_pagemarks.py` 给出两个 `[ok]`，是否足以判本块体例合格？
- 依据：块 B 的 trace 明说该脚本「只查锚点是否印出，不查位置」，他们据此抓出 p.25/p.30/p.35 三处锚点晚 5–26 行、p.29 落在词中间。故本块另写一次性脚本，把 16 个锚点后 60 字与 `01_pages/pNNN.txt` 的页首正文逐条并排比对。
- 结论：14 处与原文页首词逐字对齐（p.12 精确到「并｜不」之间、p.18 精确到 (viii)、p.21 精确到 (iii)）；p.7 差两个标题行（章标题＋节标题）、p.19 差一个定理标题行，属标题行错位，不影响定位，判为**可接受**并写入报告 §3，不改。
- 事后确认：报告 §1 维度 8、§5 各补一条；比对脚本与输出已删，只留结论（临时文件不列入交付）。
