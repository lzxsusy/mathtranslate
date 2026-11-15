# 黎曼曲面的模空间：Les Houches 讲义 —— 中文译注本

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 与 LICENSE 为准：译文与语料是第三方底本的演绎作品，保留权利，仅限非商业学术研读，权利人通知即撤；自产元数据、术语、工程文档与工作流为 CC BY 4.0。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

> **底本**：Alessandro Giacchetto, Danilo Lewański, *Les Houches lecture notes on moduli spaces of Riemann surfaces*, arXiv:2410.13273v2 [math.AG], 2026-02-27。
> **底本页数**：46 页（PDF p.1–46）；**PDF 页号 = 印刷页码，偏移 0**（封面即第 1 页）。
> **本译注本**：中文正文 + 全部 155 条编号公式 + 35 处编号定义/定理/命题/例/习题 + 原文 3 张表格 + 15 幅图的图注译文 + {{NOTES}} 条 Tutor Note（LaTeX 注释形式，另汇总为《译注汇总.md》）。

---

## 一、底本信息与页码映射

| 项目 | 值 |
|---|---|
| 原文标题 | Les Houches lecture notes on moduli spaces of Riemann surfaces |
| 作者 | Alessandro Giacchetto；Danilo Lewański |
| arXiv | 2410.13273v2 [math.AG]，2026 年 2 月 27 日 |
| 底本 PDF | 46 页，1 848 139 字节 |
| 页码映射 | **PDF 第 N 页 = 印刷第 N 页**（N = 1…46）。译文片段内以 `% [原文 p.N]` 标注 |
| 章节起始 | §1 p2｜§2 p4（2.1 p4, 2.2 p10, 2.3 p16）｜§3 p27（3.1 p27, 3.2 p31, 3.3 p35）｜§4 p38（4.1 p38, 4.2 p41）｜References p43 |
| 编号公式 | 155 条：§1: 1.1–1.2（2）｜§2: 2.1–2.79（79）｜§3: 3.1–3.60（60）｜§4: 4.1–4.14（14） |
| 编号环境 | 35 处（定义/定理/命题/例共用每节一套主计数器；习题单独一套计数器） |
| 插图 | 15 幅（Fig 1–15），**全部不复刻**，仅译图注并加"图从略"标记 |
| 表格 | 3 张（Table 1 p23、Table 2 p37、Table 3 p40–41），**照录重排** |

## 二、结构清单（本译注本）

```
main.tex                 主文件：封面 / 摘要 / 目录 / 章节骨架 / 参考文献
src/preamble.tex         导言区：页面、字体、数学宏、定理环境、页眉
src/sec1.tex             §1 引言（原文 p2–3）+ 致谢 / 资助信息
src/sec21.tex            §2.1 模空间的定义（p4–9）
src/sec22.tex            §2.2 分层结构与重言映射（p10–15）
src/sec23a.tex           §2.3 前半：相交理论（p16–20）
src/sec23b.tex           §2.3 后半：Witten 猜想（p21–26）
src/sec31.tex            §3.1 公理（p27–30）
src/sec32.tex            §3.2 Givental 作用（p31–34）
src/sec33.tex            §3.3 与拓扑递归的联系（p35–37）
src/sec4.tex             §4 进一步的方向（p38–42，含 4.2 小节标题）
src/refs.tex             参考文献（p43–46）
build_xelatex.bat        一键编译
compile.log              真实编译日志
译注汇总.md              全部 Tutor Note 索引（由 src/*.tex 自动抽取）
ERRATA.md                原文笔误登记表
```

## 三、编译方法

本译注本用 **XeLaTeX + ctex**（`ctexart`，`fontset=none` + 字体绝对路径），**必须用 XeLaTeX**，不能用 pdflatex（有中文与 fontspec）。

```bat
:: 一键编译（build_xelatex.bat 内容）
set TMP=%~dp0tmp
set TEMP=%TMP%
set XELATEX=G:\texlive\2026\bin\windows\xelatex.exe
"%XELATEX%" -interaction=nonstopmode -file-line-error main.tex
"%XELATEX%" -interaction=nonstopmode -file-line-error main.tex
```

注意事项：

1. **临时目录必须可写**。本机曾出现 `xdvipdfmx` 拿不到 `TMP` 直接崩溃（退出码 `-1073740777`、PDF 0 字节）；`build_xelatex.bat` 已把 `TMP`/`TEMP` 指到工程内 `tmp\`。
2. **字体**：`src/preamble.tex` 用
   `\setCJKmainfont[Path=C:/Windows/Fonts/,BoldFont=simhei.ttf,ItalicFont=simkai.ttf]{simsun.ttc}`，
   并显式声明 `zhkai`(simkai.ttf)、`zhhei`(simhei.ttf)、`zhfang`(simfang.ttf)。**不依赖 fontconfig**；若在非 Windows 机器编译，需改这四个字体。
3. 编译两遍以生成目录与书签。环境：TeX Live 2026（XeTeX 3.141592653-2.6-0.999998）。

## 四、译校体例

1. **正文照译，一字不改**：原文的笔误、排版瑕疵照原文译出，只在 `% [Tutor Note: ...]` 中指出并提供正确形式（并登记于 `ERRATA.md`）。
2. **公式编号唯一真值**：155 条编号公式与原文一一对应，`\begin{equation}...\tag{2.36}\end{equation}` 手工编号，缺一不可、不得重排。多行公式用 `align` 逐行 `\tag`；同一编号多式并列用 `\qquad` 分隔共用一 `\tag`。
3. **正文引用公式写纯文本**"式 (2.36)"，不用 `\eqref`（手工 `\tag` 无法自动交叉引用）。
4. **编号环境手工给号**：`\begin{definition}[2.1]`、`\begin{exercise}[2.3]` 等，印成"定义 2.1""习题 2.3"，编号严格按原文序列（定义/定理/命题/例共用每节一套计数器，习题独立计数器）。
5. **表**：原文 3 张表照录重排（表题中译并保留 Table 编号）。**图**：15 幅图不复刻（重画即伪造），在原位置以〔原文图 N 从略：图注中译〕标记，正文中"见图 N"照译。
6. **术语**：按 `glossary.tsv` 冻结（模空间、黎曼曲面、稳定图、重言类、上同调场论、拓扑递归……）。人名与文献名不音译（Witten、Givental、Kontsevich、Deligne、Mumford 等保留拉丁字母）；参考文献条目整条不译。
7. **Tutor Note**：只写四类——可验证的易错点（给出核对方法）、补出的省略论证、原文笔误（给正确形式 + 判断依据）、记号/术语说明。批注是 LaTeX 注释，**不进入排版**，按原文页序汇总于《译注汇总.md》。
8. 原文的 Acknowledgements 与 Funding information 是正文段落（非脚注），照原文结构译为两段带标题的正文。

## 五、原文笔误登记表

见 `ERRATA.md`（逐条给出：页码｜原文位置｜原文写法｜正确写法｜判断依据）。

## 六、统计

| 指标 | 数值 |
|---|---|
| 底本页数 | 46 |
| 本译注本页数 | **{{PAGES}}** |
| 编号公式 | **155**（校验：155/155 全部出现在成品 PDF 文本中） |
| 编号定义/定理/命题/例/习题 | **35**（序列与原文一致） |
| 表格 | 3（照录） |
| 插图 | 15（图注译出，图从略） |
| Tutor Note | **{{NOTES}}** 条 |
| 编译 | XeLaTeX ×2，0 error / 0 undefined / 0 missing character |

## 七、已知偏差与限制

1. **插图未复刻**：原文 15 幅图为矢量插图（TikZ 级），重画即伪造，故一律以"图从略 + 图注译文"代替；依赖图像的直观理解需回看原文。
2. **版式不逐页对齐**：中文排版的行宽/行距与原文不同，页数不一一对应，只有**页码标注**（`% [原文 p.N]`）对应。
3. **原文数学字体与符号形状**：原文用 `\mathcal`/`\mathrm` 的区分已按图像逐条核对，但个别手写体（如 $\mathscr$ 与 $\mathcal$ 的细微差别）在不影响语义处从简。
4. **表格数据**：Table 1/2/3 逐格对图抄录；Table 3 跨 p40–p41 两页，若原印刷有折行断字，已按数学含义复原为一行。
5. **批注是译者判断，不是原文**：所有 Tutor Note 均为译注者所加，与作者无关；其中"原文笔误"的判断依据写在批注内，读者可自行复核。
6. **原文有 15 处"编号公式"实际上是示意图示**（$(\Sigma,p_1,\dots,p_n)$ 型的曲面粘合图 / 配边图 / 稳定图 / 余切丛示意图）：分别是 (2.26)(2.27)(2.28)(2.29)(2.31)、(2.41)(2.54)、(3.9)–(3.12)、(3.15)、(3.26)(3.35)(3.39)。为**不丢失编号真值**，这些位置仍用 `equation` + `\tag{}` 排版，式内以〔原文此处为图示：…〕文字转述图示内容（不重画、不伪造）。这也是唯一"公式位置不做数学排字"的例外。
7. **§3.2 的三个子小节**（3.2.1 Rotation / 3.2.2 Translation / 3.2.3 Examples and Teleman）用 `\subsubsection` 排版，编号由自动计数器给出，恰好与原文 3.2.1/3.2.2/3.2.3 一致。
8. **脚注编号**：原文脚注与正文同为全文连续编号（1–4），译本改用 LaTeX 自动脚注编号，故编号可能与原文不一一对应（已在相关批注中说明原文是第几号脚注）。
9. **五个小节标题的位置**：§2.2、§2.3、§3.1、§3.2、§3.3 在原文中都排在页面中部（其前是上一小节的收尾），本译注本按原文位置就地排版，不凑到页顶。

## 八、版权声明

底本 arXiv:2410.13273v2 的著作权属于原作者 Alessandro Giacchetto 与 Danilo Lewański（arXiv 预印本，按其许可条款使用）。本文件是其**中文译注本**，仅供学习与研究使用，不用于商业目的；引用时请同时引用原文。译注部分（Tutor Note、术语表、说明文字）由本译注本作者提供。
