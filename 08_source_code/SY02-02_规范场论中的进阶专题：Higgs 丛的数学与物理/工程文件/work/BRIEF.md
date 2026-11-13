# BRIEF —— 分工、边界与编号契约（v1.0，Lead 独占）

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；本项目语料默认不用于训练，要用须先整库审计并经 Lead 书面批准。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

底本：Laura P. Schaposnik, *Advanced topics in gauge theory: mathematics and physics of Higgs bundles*,
arXiv:1907.09800v1，**53 页**，PDF 页 = 印刷页（偏移 0）。
项目根：`<本地路径>`；工作区 `work\`；输出 `work\src\chunks\`。

## 一、分工表（Lead + 7 译者 + 1 工程）

| 块 | 文件 | 原文页 | 内容 | 编号区间 | 图/表/标题归属 |
|---|---|---|---|---|---|
| Lead | `c01.tex` | pp.1–5 | §1 引言、§2 开头、§2.1 | 2.1–2.12 | `\section{引言}`、`\section{模空间…}`、`\subsection{Higgs 丛…}`（2.1） |
| tr-01 | `tr01{a,b,c}.tex` | pp.6–12 | §2.2、§2.3、§2.4（Wild） | 2.13–2.25 | **图 2.24（fig1.png）**、`\subsection{实 Higgs 丛}`(2.2)、`\subsection{抛物 Higgs 丛}`(2.3)、`\subsection{野 Higgs 丛}`(2.4) |
| tr-02 | `tr02{a,b,c}.tex` | pp.13–20 | §2.5 问题集 I、§3 开头、§3.1、§3.2 前半 | 问题 1–5；3.1–3.7 | `\subsection{问题集 I}`(2.5)、`\section{…Hitchin 纤维化…}`(§3)、`\subsection{…Teichmüller 分支}`(3.1)、`\subsection{…正则纤维}`(3.2) |
| tr-03 | `tr03{a,b,c}.tex` | pp.21–25 | §3.2 后半、§3.3、§3.4 问题集 II | 3.8–3.10；问题 6–10 | `\subsection{…奇异轨迹}`(3.3)、`\subsection{问题集 II}`(3.4) |
| tr-04 | `tr04{a,b,c}.tex` | pp.26–31 | §4 开头、§4.1、§4.2 前半 | 4.1–4.9 | **表 4.7、表 4.8**、`\section{…膜…}`(§4)、`\subsection{有限群作用…}`(4.1)、`\subsection{反全纯对合…}`(4.2) |
| tr-05 | `tr05{a,b,c}.tex` | pp.32–38 | §4.2 后半、§4.3 问题集 III | 4.10–4.18；问题 11–15 | `\subsection{问题集 III}`(4.3) |
| tr-06 | `tr06{a,b,c}.tex` | pp.39–44（+p45 顶部半句） | §5 开头、§5.1、§5.2 | 5.1–5.12 | **图 5.10（fig2.png）**、`\section{…对应关系}`(§5)、`\subsection{群同构…}`(5.1)、`\subsection{多边形与超多边形}`(5.2) |
| tr-07 | `tr07{a,b,c}.tex` | pp.45（§5.3 起）–49 | §5.3、§5.4 问题集 IV、致谢 | 5.13；问题 16–20 | `\subsection{Langlands 对偶}`(5.3)、`\subsection{问题集 IV}`(5.4)、`\para{致谢}` |
| tr-qa | `c-refs.tex` 等 | pp.49–53 | 参考文献（不译，英文原貌） | — | 图表裁剪、参考转录、Gate 脚本 |

> 每个译者写 2–3 个文件：**按页拆**（a/b/c 依 a→b→c 顺序拼装），不要一个文件写 7 页。
> 文件名严格为 `trNNa.tex`、`trNNb.tex`、`trNNc.tex`（三位 NN：01…07）。

**三级编号行内小标题（`X.Y.Z.`）共 7 条，一律用 `\para` 手工写编号**（不用 `\subsubsection`，防止漏一条导致全书编号错位）：
`2.4.1`（p11，tr-01）、`3.2.1`（p19，tr-02）、`4.2.1`（p30，tr-04）、`4.2.2`（p33，tr-05）、
`4.2.3`（p34，tr-05）、`4.2.4`（p35，tr-05）、`5.1.1`（p39，tr-06）。
另：**p6 顶部两段 §2.1 续文（无编号条目）归 tr-01**（见 TIMELINE #1）。

## 二、编号契约（**首尾必须接上邻居**）
原文每节内**定理/命题/定义/例/注/猜想/公式/图/表共用一个计数器**。你的块必须严格输出自己区间内的全部编号：

| 块 | 必须输出（逐条，编号照抄原文） |
|---|---|
| Lead | 定义 2.1、例 2.2、定义 2.3、注 2.4、例 2.5、定理 2.6、式 (2.7)、式 (2.8)、定义 2.9、例 2.10、例 2.11、式 (2.12) |
| tr-01 | 定义 2.13、例 2.14、定义 2.15、例 2.16、式 (2.17)、式 (2.18)、定义 2.19、注 2.20、式 (2.21)、注 2.22、式 (2.23)、**图 2.24**、猜想 2.25 |
| tr-02 | **问题 1–5**、注 3.1、式 (3.2)、式 (3.3)、定理 3.4、式 (3.5)、例 3.6、定理 3.7 |
| tr-03 | 式 (3.8)、式 (3.9)、定理 3.10、**问题 6–10** |
| tr-04 | 例 4.1、定理 4.2、定理 4.3、命题 4.4、式 (4.5)、式 (4.6)、**表 4.7**、**表 4.8**、例 4.9 |
| tr-05 | 式 (4.10)、式 (4.11)、定理 4.12、式 (4.13)、猜想 4.14、定理 4.15、定理 4.16、定理 4.17、定理 4.18、**问题 11–15** |
| tr-06 | 式 (5.1)、式 (5.2)、命题 5.3、式 (5.4)、定理 5.5、注 5.6、定义 5.7、例 5.8、注 5.9、**图 5.10**、定理 5.11、注 5.12 |
| tr-07 | 猜想 5.13、**问题 16–20**、致谢 |

> 参考清单：`work\statements.tsv`（46 条，kind/编号/页码）、`work\tags.txt`（20 条公式）、
> `work\problems.tsv`（20 道习题）、`work\tags_bypage.txt`（页→编号，最方便）。

## 三、边界接缝（裁决，已写入 TIMELINE.md，**双向都已知**）
1. **Lead → tr-01**：p5 末句 "(v, w), and Φ a Higgs field … which satisfies (2.12)." 完整结束；
   tr-01 从 p6 的 `\subsection{实 Higgs 丛}` 开始。**干净边界，不重叠。**
2. **tr-01 → tr-02**：p12 末为脚注 "…monodromy data."；tr-02 从 p13 `\subsection{问题集 I}` 开始。**干净。**
3. **tr-02 → tr-03**：p20 末为行间公式 `… →π0(∧) →. . . .`；tr-03 从 p21 首段 "Hence, there is a short exact sequence …" 开始。**干净。**
4. **tr-03 → tr-04**：p25 末句 "… Hitchin maps defined in [72] and [10]."；tr-04 从 p26 `\section` 开始。**干净。**
5. **tr-04 → tr-05（跨页句！）**：p31 末句 "…finite dimensional abelian varieties given by Jacobians or Prym varieties of quotient"
   在 p32 续 "spectral curves, as shown in [89,91]." → **tr-04 负责把这句话写完**（可读 p32 首行），
   **tr-05 从 p32 第 2 句 "Having mentioned the spectral data for these objects in previous chapters…" 开始，不得重复该句。**
6. **tr-05 → tr-06**：p38 末为 Problem 15 的提问；tr-06 从 p39 `\section` 开始。**干净。**
7. **tr-06 → tr-07（跨页句！）**：p44 末 "… The central node corresponds to the contribution from the 7-brane"
   在 p45 续 "wrapped over the gauge theory curve, and the satellite nodes to the flavour branes of the system." →
   **tr-06 负责把这句话写完**；**tr-07 从 p45 的 `\subsection{Langlands 对偶}`（5.3）开始，不得重复该句。**
8. **tr-07 → 参考文献**：致谢到 p49 结束（"... NSF grants DMS-1509693 and CAREER DMS 1749013."）；
   `c-refs.tex` 由 tr-qa 生成，tr-07 不要写参考资料部分。

## 四、每块开工必读（按顺序全文读完）
1. `work\STYLE_GUIDE.md`（硬规范）
2. 本文件 `work\BRIEF.md`
3. `work\glossary.tsv`（术语冻结表）
4. `work\TIMELINE.md`（边界裁决）

## 五、工作方法
- 先读 `work\split\pNNN.txt` 把握论证结构与段落（文字层只用于定位）；
- 再逐页 `read_image` 看 `work\pages\pNNN.png`（200dpi），公式/符号逐符号抄写；
- 看不清就裁图放大：`& $py "work\tools\crop.py" <页> <x0> <y0> <x1> <y1> <out.png> [dpi]`（PDF 点坐标，整页 612×792）；
- **不要编译**（Lead 统一编译）；不改 preamble/main/STYLE_GUIDE/BRIEF/TIMELINE/别人的 chunks；
- 每写 2–3 页就落盘一个 chunk 文件，不要憋到最后；
- 完成前过 STYLE_GUIDE §10 自检清单 → send_message 给 lead 按 §11 回执。

## 六、时间与质量
质量优先：宁慢勿错。某页图像确实无法辨认 → 写进回执，**不要猜**、不要编造。
