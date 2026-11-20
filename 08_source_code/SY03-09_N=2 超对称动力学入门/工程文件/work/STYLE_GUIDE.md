# STYLE_GUIDE —— 《N=2 超对称动力学入门》校对工程规范（v1.0）

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 与 LICENSE 为准：译文与语料是第三方底本的演绎作品，本库不代原作者授权、也不另设限制（检索、研究、教学、训练均可），权利人通知即撤；自产元数据、术语、工程文档与工作流为 CC BY 4.0。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`
（Lead 独占维护；队友只读不改。项目根：`<本地路径>`）

## 0. 底本与工程事实（已实测，勿再猜）

- **底本**：Yuji Tachikawa, *N=2 supersymmetric dynamics for pedestrians*，arXiv:1312.2684v2（2014-05-22）。
  本机 PDF：`<本地路径> supersymmetric dynamics for pedestrians 1312.2684v2.pdf`（**194 页**）。
- **arXiv 源码（v2，与底本一致）**：`<本地路径>`（452 KB，注释内写 "version 2"），
  参考文献 `dummies5.bbl`，插图 128 张 PDF。**已按节切分到 `work/ref/<块>-en.tex`；这是本项目校对的第一真值**
  （比 PDF 文字层可靠）。⚠️ `<本地路径>` 是 **v3** 源码，与底本 v2 有实质差异，**禁止使用**；
  凡 v3 与 v2 冲突，一律以 v2 为准。
- **待校对草稿**：本工程（XeLaTeX + xeCJK + Fandol/CMU 字体 + makeindex），目录结构：
  ```
  main.tex          标题页/目录/逐节 \input
  preamble.tex      版式、字体、hyperref/cleveref、\numberwithin
  macros.tex        数学宏（\cN \SU \SO \cU \cM ...）
  references.tex    参考文献（thebibliography，手写 .tex）
  young-kugo.sty    Young 图宏
  index.ist         索引样式（makeindex）
  index-terms.json  索引排序键
  texglyphlist.txt  xdvipdfmx 数学字形映射（编译时必须在本目录）
  sections/00-introduction.tex … 13-conclusions.tex, A-instantons.tex, B-theory-zoo.tex（16 个文件）
  figures/*.pdf     原文矢量插图
  build.ps1         一键编译（XeLaTeX + makeindex + XeLaTeX×2）
  ```
- **实测结构对照（原文 vs 草稿，自动生成见 `work/probe/structdiff.md`）**：
  `\section` 16/16、`\subsection` 58/57（草稿少 1）、`equation` 731/725（少 6）、`align` 24/24、
  `multline` 9/8（少 1）、`figure` 123/122（少 1）、`table` 3/3、`footnote` 18/18、`cite` 142/135（少 7 处引用）。
  原文 `\numberwithin{equation}{subsection}`、`\numberwithin{figure}{section}`、`\numberwithin{table}{section}`，
  草稿 preamble 与之一致（公式号形如 (4.3.2)，图表号形如「图 6.10」「表 2.1」）。
- **已知的缺失标签**（必须补）：`12-su-n-duality` 缺 `fig:f-term-relation`；`09-gaiotto` 缺 `++++`（原文本身的怪标签）。
- **原文分节英文对照**已切好放在 `work/ref/<块名>-en.tex`（例如 `work/ref/04-pure-su2-en.tex`），
  内容与 `sections/04-pure-su2.tex` 一一对应（`00` 同时覆盖原文 Introduction 与 Prerequisites/致谢两节）。

## 1. 校对目标（按优先级）

1. **无遗漏**：原文每一段、每个句子、每个公式、每条脚注、每个图注/表题、每处 `\cite` 都必须在译文中出现；
   不得有原文没有的内容（作者没说过的物理论断一个字都不加）。
2. **无错译**：物理含义、术语、逻辑关系（因果、条件、对偶方向）必须与原文一致。
3. **公式逐符号正确**：指标（上下标）、符号（正负号/i/2π 因子）、希腊字母、花体 vs 正体、
   矩阵分块、求和/求积范围、括号归属，全部与原文源码逐字对应。
4. **中文规范**：标点、术语统一、句子通顺；不得出现机翻腔（"的的"、被动堆叠、欧化长句）。
5. **LaTeX 健康**：不得引入编译错误；不得改 `\label` 键名（交叉引用依赖它）；不得改数学宏。

## 2. 允许修改的范围（硬性）

- **只能改自己负责的 `sections/*.tex` 文件**（见 BRIEF 分工）。
- **禁止**改：`main.tex`、`preamble.tex`、`macros.tex`、`references.tex`、`young-kugo.sty`、`index.ist`、
  `figures/`、以及其他人的 sections 文件。需要改这些 → 写进回执，由 Lead 统一处理。
- **禁止**：`\newcommand` 自造宏；改变 `\label{}` 键；把 `\begin{equation}` 改成别的环境（反之亦然），
  除非原文就是那个环境；删除 `\index{}`；把 `\cite` 换成纯文本。
- **单点修改**：一次改一处，改完在脑中对照上下文；**不要用正则整文件替换**（Lead 负责全局批量项）。

## 3. 数学与环境（原样保留，只改内容不改造型）

- 编号公式一律 `\begin{equation} … \label{…} \end{equation}`；`align`/`multline` 保持原有结构。
- 公式编号由 `\numberwithin{equation}{subsection}` 自动生成，**不要手写编号**。
- 交叉引用：`\eqref{...}`（式）、`\ref{...}`（节/图/表/脚注外的编号对象）保持原样，
  **不要改成 cleveref**（草稿未用 cleveref；preamble 虽加载但正文统一用 \ref/\eqref）。
- 单位与数学：`\text{...}` 里的中文可用；不要把中文塞进数学模式（`$中文$` 会缺字）。
- 中文标点：句末「。」、逗号「，」、顿号「、」、分号「；」、冒号「：」、引号「“”」、括号「（）」；
  **数学环境内部用英文标点**（点号 `.`、逗号 `,`）。
- 行内数学与中文之间的空格由 XeCJK 处理，草稿现有风格是「中文 $x$ 中文」（带空格），保持。

## 4. 术语（`work/glossary.tsv` 冻结，可补充但需在回执报告）

首次出现括注英文：例如「库仑支（Coulomb branch）」。人名/模型名/缩略语保留英文：
Seiberg、Witten、Gaiotto、Argyres、Douglas、Nekrasov、Nf、SU(N)、SO(N)、U(1)、CFT、BPS、AD（Argyres-Douglas）、
SW（Seiberg-Witten）、IR/UV。缩写用法参考 glossary。

## 5. 校对注（Tutor Note）

凡属「原文笔误 / 原文歧义 / 需要补充的省略论证 / 值得提醒的易错点」，写成 LaTeX 注释：
```latex
% [Tutor Note: p.42 式 (4.3.7) 中原文印作 +，由 … 可判定应为 −；正文照原文排版。]
```
密度不必强求；**但原文笔误必须给出判断依据**，且**正文照原文排**（不擅自改原文结论）。
这些注释会被脚本汇总进 `译注汇总.md`。

## 6. 校对方法（逐段对照，禁止"通读一遍凭感觉"）

1. 打开 `work/ref/<块>-en.tex`（原文 LaTeX）与你的 `sections/<块>.tex`；
2. **按顺序逐段对齐**：原文一段 → 译文对应段；确认无漏段/漏句；对每一句问"这句的信息在译文哪里？"
3. 公式：在原文找到同一 `\label`，逐字符比对（可借助 `work/probe/structdiff.md` 的低相似度清单）；
4. 图/表：`\includegraphics` 文件名、图注文字、表格每格内容；
5. 脚注：原文 18 条脚注，逐条对照；
6. `\cite`：原文该处的引用键是否都出现在译文同一位置（用脚本 `work/tools/cite_diff.py` 辅助）；
7. 中文：标点、术语、病句；
8. 每次改动后立即在 `work/review/<块>.md` 记一行（位置/类型/修改前后），最后汇总。

## 7. 自检清单（交稿前逐项）

- [ ] 本块的段落/句子/公式/脚注/图注/引用**无遗漏**（逐段核对过）
- [ ] 公式与原文逐符号一致（抽查 ≥15 条，重点：系数、上下标、正负号、i、2π、花体）
- [ ] 无新增内容；原文笔误照排 + Tutor Note
- [ ] `\label` 未改；无新增/删除环境；无自造宏
- [ ] 中文标点全部全角；数学环境内英文标点
- [ ] 术语与 `glossary.tsv` 一致；新术语已报告
- [ ] UTF-8 无 BOM、LF；无 `**`/Markdown 残留；无 U+FFFD

## 8. 回执格式（send_message 给 lead）

1) 负责块与文件；2) 改动统计（处数，按类型：遗漏补译/误译/公式/术语/标点/LaTeX）；
3) **必须让 Lead 知道的问题**（缺公式/缺图/缺脚注、preamble 需改、原文自身矛盾）；
4) 新术语（英→中）与 glossary 建议；
5) 自检结果逐项 pass/fail；6) 未解决问题清单。
