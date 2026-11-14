# BRIEF.md —— 项目总纲（所有译者必须先读）

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 为准：语料 / 轨迹 / 会话 CC BY 4.0，明确欢迎用于训练与蒸馏（译文与工程文档 CC BY-NC-SA 4.0）。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

## 0. 这是什么

底本：**Springer Lecture Notes in Mathematics 2386**
*Spectral Networks: Bridging higher-rank Teichmüller theory and BPS states*
作者：Clarence Kineider, Georgios Kydonakis, Eugen Rogozinnikov, Valdo Tatitscheff, Alexander Thomas
（arXiv:2412.03588v3 [math-ph]）

这是一本**数学-物理交叉的研究生教材**：前半本是高阶 Teichmüller 理论（Hitchin 表示、正性、Fock–Goncharov 坐标），中间引入**谱网络**（spectral networks）作为非阿贝尔化的几何工具，后半本接到 4d N=2 超对称规范理论、Seiberg–Witten 理论、S 类理论与 **BPS 态计数**，最后是推广（指数网络、三维网络、WKB cameral 网络、Virasoro 共形块的非阿贝尔化）。

**目标**：全书中文译注本（可编译 LaTeX 源码 + 成品 PDF），保留原文全部结构、编号、插图，加学术批注。

## 1. 页码与文件

| 项目 | 说明 |
|---|---|
| 印刷页码 | = PDF 页号 − 40 |
| 页面图像 | `work/pages/pNNN.png`（**PDF 页号**命名，200 dpi，公式唯一真值） |
| 文字层 | `work/split/pNNN.txt`（只能用来定位英文句子；数学符号不可信） |
| 裁图 | `work/figures/fig_X_Y.png`（清单 `work/figures.json`） |
| 公式清单 | `work/tags2.txt`（坐标校验过的编号公式） |
| 任务卡 | `work/blocks/<块名>.md`（页段、锚句、图、公式、章标题） |
| 交付 | `work/src/part/<块名>.tex`（一个块一个文件） |
| 规范 | `work/STYLE_GUIDE.md`（**硬约束**）、`work/glossary.tsv`（术语冻结表） |

## 2. 全书结构与章节译名（统一用表）

| Part | 章 | 英文标题 | 统一译名 |
|---|---|---|---|
| I 数学基础 | 1 | The Fundamental Group | 基本群 |
| | 2 | Covering spaces | 覆叠空间 |
| | 3 | Bundles and connections | 丛与联络 |
| | 4 | Hyperbolic geometry | 双曲几何 |
| | 5 | Cluster varieties | 簇代数簇 |
| II 高阶泰希米勒理论 | 6 | The Teichmüller space | 泰希米勒空间 |
| | 7 | Coordinates on Teichmüller space | 泰希米勒空间上的坐标 |
| | 8 | Differentials on a Riemann surface | 黎曼曲面上的微分 |
| | 9 | Higher-rank Teichmüller spaces | 高阶泰希米勒空间 |
| | 10 | Hitchin representations | Hitchin 表示 |
| | 11 | Maximal representations | 极大表示 |
| | 12 | Positivity | 正性 |
| III 几何中的谱网络 | 13 | Non-degenerate spectral networks | 非退化谱网络 |
| | 14 | General and Fenchel–Nielsen spectral networks | 一般谱网络与 Fenchel–Nielsen 谱网络 |
| | 15 | Non-abelianization and abelianization | 非阿贝尔化与阿贝尔化 |
| | 16 | WKB method and Stokes graphs | WKB 方法与 Stokes 图 |
| IV BPS 态的计数 | 17 | Four-dimensional supersymmetric quantum field theories | 四维超对称量子场论 |
| | 18 | Four-dimensional N = 2 gauge theories | 四维 N = 2 规范理论 |
| | 19 | Electric-magnetic duality | 电磁对偶 |
| | 20 | Seiberg–Witten theory | Seiberg–Witten 理论 |
| | 21 | Class S theories | S 类理论 |
| | 22 | BPS states in class S theories | S 类理论中的 BPS 态 |
| V 推广 | 23 | Exponential networks | 指数网络 |
| | 24 | Three-dimensional networks | 三维网络 |
| | 25 | WKB cameral networks | WKB cameral 网络 |
| | 26 | Non-abelianization for conformal Virasoro blocks | 共形 Virasoro 块的非阿贝尔化 |
| 附录 | A | Lie theory essentials | 李论基础 |

## 3. 各部分内容提要（帮你快速进入物理/数学语境）

- **Part I（Ch.1–5）数学基础**：基本群与覆叠空间、向量丛/联络/平坦联络与 Riemann–Hilbert 对应、双曲几何（双曲平面、纤毛曲面 ciliated surface、理想三角剖分、裤子分解）、簇代数簇（箭图、种子环面、变异 mutation）。
- **Part II（Ch.6–12）高阶泰希米勒理论**：Teichmüller 空间与和乐表示、Fenchel–Nielsen 坐标与剪切坐标、阿贝尔/二次微分及其轨道（trajectories）、谱曲线、Strebel 微分、特征簇 character variety、Hitchin 表示（正旗、Fock–Goncharov 坐标、snakes）、极大表示（Maslov 指标）、正性（全正性、Θ-正性）。
- **Part III（Ch.13–16）谱网络**：谱网络的定义（small / non-degenerate / WKB / Fenchel–Nielsen）、路径代数与路径提升、非阿贝尔化与阿贝尔化的互逆、用谱网络算 Fock–Goncharov 与 Fenchel–Nielsen 坐标；WKB 方法（形式 WKB、Borel 求和、Stokes 曲线、连接公式、Voros 符号、opers）。
- **Part IV（Ch.17–22）BPS 态计数**：4d 超对称 QFT（超庞加莱代数、超场、瞬子、反常、Seiberg 对偶）、4d N=2 理论、电磁对偶（磁单极、Witten 效应、Montonen–Olive 对偶、穿墙 wall-crossing）、Seiberg–Witten 理论（SW 曲线、可积系统、瞬子计数）、S 类理论（M 理论、膜构造、SW 曲线、A_{N-1} 型）、S 类理论中的 BPS 态（弦网、BPS 叶状结构、谱网络计数）。
- **Part V（Ch.23–26）推广**：指数网络（exponential networks）、三维网络（Chern–Simons）、WKB cameral 网络（cameral 覆盖）、Virasoro 共形块的非阿贝尔化。
- **附录 A**：复约化李代数、根数据、根系分类、实李群、Levi 分解与旗簇。
- **front_glossary 块**：内容简介（封底）、前言（含致谢）、符号表、Glossary 术语表。

## 4. 翻译原则（与 STYLE_GUIDE 一致，重点重申）

1. **数学为真**：公式一律看 200dpi 图像抄，文字层只用来定位英文；分式/上下标/根号/矩阵/积分号最容易错。
2. **编号唯一真值**：公式 `\tag`、定理环境 [编号]、图号，全部照原文，**不许自己数、不许重排**。
3. **不造假**：没有的图/表/文献不造；原文笔误照译，只在 `% [Tutor Note: ...]` 指出正确形式。
4. **术语按 `glossary.tsv`**；表外术语首次「中文（English）」，并在报告中列出新增术语。
5. **引用写纯文本**：「式 (3.4)」「见 [12]」，不用 `\ref`/`\eqref`/`\cite`。
6. **批注**：每 3–5 页 ≥1 条有信息量的 `% [Tutor Note: ...]`（易错点给核对方法 / 补省略论证 / 原文笔误给依据）。批注是注释，不进入排版。
7. **不自己编译**（Lead 统一编译）；不自己 `\newcommand`（缺宏报给 Lead）。
8. **不跳页**：任务卡的页段里每一页都要有对应正文。

## 5. 交付与回报

- 交付：`work/src/part/<块名>.tex`（UTF-8 无 BOM，LF）。
- 回报（消息给 Lead）用 STYLE_GUIDE §12 的六行格式：块名 / 覆盖范围 / 公式落实 / 图落实 / 定理环境 / 批注与存疑。
- 若任务卡页段与实际内容错位（页面起止与锚句不符），**立即报告 Lead**，不要自行改边界。

## 6. 编译环境（供了解，译者不用跑）

- TeX Live 2026：`<本地路径>`
- 编译前必须 `$env:TMP = work\tmp`；项目路径必须 ASCII。
- 引擎 xelatex ×2；中文 simsun/simhei，数学默认 CM。
