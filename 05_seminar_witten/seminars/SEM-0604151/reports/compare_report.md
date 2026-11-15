# 附录 A 对照报告（compare_report.md）

工作目录：`C:\Users\admin\Desktop\witten-exegesis\papers\WIT-0604151-EMDGL`
完成时间：2026-11-15

## 1. 交付物

| 文件 | 状态 | 规模 |
|---|---|---|
| `manuscript/sections/50_appendix_compare.tex` | 完成 | 251 行、约 20.3 K 字符、5 张表、6 段 `origquote`、6 条自检问题 |
| `reports/compare_report.md` | 本文件 | — |
| `build/check_compare/check.tex` | 自编译用，照抄 `build/check_layer0/check.tex` 只换 input 文件 | 5 行 |

未改动 `main.tex`、`preamble.tex` 及其他 section（只读）。自编译产物 `build/check_compare/check.{pdf,aux,log}` 留在原目录。

## 2. 四份文本的版本事实（已核实）

| 文本 | 核实结果 |
|---|---|
| KW06 底本 | arXiv:hep-th/0604151，2006-04；*CNTP* 1 (2007)；231 页、12 节、146 条参考文献；自陈两个 gap（只做非分歧；不阐明 2d CFT 的用处）在印刷 p.5 |
| Witten 2008 | **0802.0999 = *Mirror Symmetry, Hitchin's Equations, and Langlands Duality***，2008-02-07，math.RT，15 页、6 节；无六维内容、无 M5、无 't Hooft 算子；末尾明说以 K–W 的 4d 理论为输入（p.14） |
| Witten 2009 | **0905.2720 = *Geometric Langlands From Six Dimensions***，2009，hep-th，30 页、5 节；2008-06 Montreal Raoul Bott 纪念会讲稿；六维 (0,2)、M5 膜、't Hooft 算子的缺陷解释、复曲面版 GL 全在此篇 |
| Frenkel | arXiv:hep-th/0512172，Date: December 2005；基于 2003-03 Les Houches「Number Theory and Physics」与 2004-03 IAS DARPA workshop 讲稿；128 页、9 节 |
| Setter | Caltech 博士论文，2013 年（Defended 2012-08-24），169 页；标题为 *Topological Quantum Field Theory and the Geometric Langlands **Correspondence***（任务提示写作 Program，按标题页与摘要采用 Correspondence）；导师 A. Kapustin |
| 中译本 | 均只用于核对（0802 中译 41 页、Setter 中译 118 页、Frenkel 中译 86 页）；附录中**未**引用中译文，故无译本页码问题 |

**重要更正**：任务把「Geometric Langlands From Six Dimensions」记作 0802.0999，实际两篇是不同论文。附录在节首用 `warn` 框明写这一区别，并分别使用 `\anchor{0802.0999 p.N}` 与 `\anchor{0905.2720 p.N}` 两套锚点，避免把六维内容记错在 0802.0999 名下。

## 3. 三节结构与对照表行数

- §A.1 与 Witten 2008/2009 对照：表 A.2「S1–S8 与 M1–M5 在两篇 Witten 中的命运」，**10 行**（S1–S8 八行 + 新增六维 + 新增 M5/复曲面）。另对 2009 的五条未补齐缺口逐条给出锚点（simply-laced 限制、无定理、6d 理论未构造、level-r 对应未做、2006 第二 gap 只部分回应）。
- §A.2 与 Frenkel 2003 对照：表 A.3「两条路线的入口对照」，**10 行**（对象 A/B 侧、工具、对偶含义、分歧处理、D-模来源、群的语言、2d CFT 角色、已证范围、曲线与边界）；另给三条可互译条目（T-对偶 \pB；c.c. 膜 D-模 ↔ Hitchin 量子化 \pB；分歧 ↔ 2-流形算子 \pC）与一处不可互译（opers，\pC）。
- §A.3 与 Setter 2013 对照：表 A.4「Setter 2013 与 K–W 2006 的分工」，**10 行**（4d 扭化、C 上紧化、膜范畴、线算子、面算子、't Hooft=Hecke、c.c. 膜→D-模、n-范畴层级、Vafa–Witten、定理化）。
- §A.4 小结：表 A.5「三份文献的位置与替代边界」，**4 行**。
- 表 A.1「本附录对照的四份文本」：**5 行**。

## 4. provenance 统计

| 标记 | 含义 | 条数 |
|---|---|---|
| `\pA` | 原文/对照文献明写 | **46** |
| `\pB` | 原文暗示、我们重建 | **10** |
| `\pC` | 我们的判断 | **33** |

锚点合计 136 处：`src` 45、`0905.2720` 36、`Frenkel` 24、`Setter` 20、`0802.0999` 11。表 A.2–A.5 的约定是「每格除标 \pB、\pC 者外均为 \pA」，已在正文阅读约定中声明。

## 5. 自编译记录

工作目录 `build/check_compare/`，命令（两遍）：

```
& "C:\Users\admin\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe" -interaction=nonstopmode -halt-on-error check.tex
```

日志结果（`build/check_compare/check.log`）：

- error（`^!` 行）：**0**
- Overfull \hbox：**0**
- Underfull \hbox：23（全部来自表格 `p{}` 列的自然欠满，以及 preamble 里 fancyhdr 的 `E` option 警告；不构成版面问题）
- undefined reference：**0**（`\S\ref{sec:compare-setter}` 两遍后解析为 §1.3，主文档中将是 §A.3）
- 页数：**10 页**（`Output written on check.pdf (10 pages).`），在要求的 6–10 页内
- 视觉复核：`latex_look` 渲染第 1、3、6、8、9 页，确认表 A.1–A.5 不出界、`warn`/`kcard`/`origquote` 正常显示

排版上没有 `\usepackage`、`\newcommand`、外部图片，未用 `tabularx`（表格一律 `p{...}` + `\footnotesize`）。

## 6. 三节的核心结论（正文已展开）

1. **§A.1**：2009 把 2006 的 S2–S8 压缩成 p.3–4 一句话与 p.6 一句 't Hooft=Hecke，保留两端（S1、S7），中间六步折叠进「$d-2$ 维给范畴」的公理。六维不是补证明而是换起点（4d 对偶变成 6d (0,2) 的推论）；「绕开 4d 扭化」只是修辞，逻辑上仍以 2006 的扭化等价为前提。新增 M5 膜、Taub-NUT BPS=⊗ level-1 WZW、复曲面版 GL；未补齐：证明、非 simply-laced、6d 理论本身、level-r 对应、2006 第二 gap。
2. **§A.2**：Frenkel 与 K–W 是「构造 Hecke 特征层」与「解释它为何存在」两条入口；同一对象（Hecke 特征层 ↔ 特征膜）、不同工具（临界 level 共形块/opers ↔ 扭化规范论/膜）；分歧是分水岭（Frenkel 主场，K–W 自陈只做非分歧）。
3. **§A.3**：Setter 不是把 K–W 严格化，而是沿其方向往 3d/2d 推进；严格化对象是**缺陷的范畴结构**（§4.1 范畴=多对象代数、§4.4 面算子 2-范畴），不是 GL 对应；依赖顺序是整篇 [1] 为输入（38 处引用均不带节号），第 2 章复述、第 5 章再紧化，不重证任何一步；与 Witten 2009 的方向相反（一个往上抬、一个往下压）。

## 7. 两条最不可靠的判断（连同理由）

1. **「2009 在逻辑上并未绕开 4d 扭化，只是修辞上把 4d 降为 6d 的推论」**（\pC，见 §A.1「『绕开 4d 扭化』的真相」）。
   理由：这是对一篇 30 页讲稿整体论证结构的判断，依据只有 (a) p.3–4 用「第三种扭化的等价」陈述 GL 的措辞，(b) 全文不出现 S2–S8 的技术细节（Hitchin 仅见参考文献、B-model 0 次）。作者本人若被追问，完全可能主张六维框架才是「真正的」第一性原理，2006 的扭化只是它的低能近似；本附录无法证伪这一读法。
2. **「c.c. 膜给出的 D-模 = Frenkel 书中 Hitchin 量子化给出的 D-模」**（\pB，见 §A.2 互译条目 (2)）。
   理由：两处构造各自都有明写（KW §11.1 c.c. 膜 → D-模；Frenkel §9.5 $D'_{-h^\vee}\cong\mathrm{Fun}\,\mathrm{Op}_{\Ldual\mathfrak{g}}(X)$），但**没有任何一篇把这两个对象等同起来**；等同靠我们补上「$\MC$ 上的 D-模」与「$\mathrm{Bun}_G$ 上 Hecke 特征层」之间的那一步。这一步在文献中通常由 Beilinson–Drinfeld 的表述衔接，但本附录没有逐句核对，故只标 \pB。

（第三条候选：Setter「严格化对象是缺陷范畴而非 GL」也是 \pC，依据是 `Hecke` 仅 5 次、无 Hecke 函子定义、无 Atiyah 公理引用与章节分布；这条把握较大，故未列入前二。）

## 8. 存疑与无法核实的点

1. **统计口径**：Setter「38 处引用 [1]」「22 个 Proposition」是 `pdftotext` 文本 grep 计数，可能包含文献表与重复引用；正文已避免据此作精细断言，只用作「以整篇为输入」「定理化不涉及 GL」的辅证。
2. **0905.2720 的年份**：arXiv 编号 2009，正文自述为 2008-06 讲稿；表 A.1 记「2009 年」并注讲稿时间，未把两者混同。
3. **0802.0999 的节标题**：原文 6 节标题（A-Model and B-Model 等）未在附录中逐字引用，只给页码与内容概述，避免与中译本节名不一致。
4. **中译本页码**：本附录未引用任何中译文，因此不存在译本页码核对问题；若后续要加中译引文，需按各译本版权页重编页码。
5. **2006 底本锚点**：全部用印刷页（`\anchor{src p.N}` = `source/text/p{N+1:03d}.txt`），未逐条回查 PDF 页；抽样核对过的锚点（p.3、p.5、p.6、p.16、p.38、p.71、p.74、p.78、p.103、p.116、p.123、p.148、p.184、p.186、p.196、p.201）与目录一致。

## 9. 过程记录（供复核）

写入过程中曾用 PowerShell 文本替换调整表 A.4 列宽，因 PowerShell 5.1 的 `Get-Content -Raw` 默认按系统 ANSI 编码读取 UTF-8 文件，再写回时造成全文乱码（445 字符不可逆丢失）。已用 write 工具**整篇重写**为最终版，并以下列校验确认无损：字符数 20 319、CJK 5 212、`?` 0、PUA 字符 0、花括号平衡、`\pA/\pB/\pC` 计数与损坏前一致（46/10/33）、编译 0 error。后续对 `.tex` 的修改**只用** `write`/`edit` 工具，不再用 PowerShell 改写文本。
