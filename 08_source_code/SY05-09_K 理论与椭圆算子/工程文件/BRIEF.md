# EN47 翻译工程 BRIEF（施工总纲 · Lead 维护，译者必读）

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 与 LICENSE 为准：译文与语料是第三方底本的演绎作品，本库不代原作者授权、也不另设限制（检索、研究、教学、训练均可），权利人通知即撤；自产元数据、术语、工程文档与工作流为 CC BY 4.0。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

> 本文件是本次工程的「工程说明书」。底本是一篇 50 页的英文讲义，体量小于常规专著，
> 故由 Lead 直接撰写施工总纲，不再另设外部说明书。
> 施工规范：`<本地路径>`（下称《纪律》）。
> 本 BRIEF 与《纪律》冲突时，以《纪律》的数学与术语规则为准，以本 BRIEF 的工程约定为准。

## 1. 任务与底本

把 Gregory D. Landweber, *K-Theory and Elliptic Operators*（arXiv:math/0504555v1
[math.AT], 27 Apr 2005）译成中文译注本：XeLaTeX + ctex，A4，保留原节号、节标题语义、
定理类环境的类型与顺序、脚注、参考文献编号，并加译者批注。

- 底本 PDF：`<本地路径>).pdf`（50 页，123,023 字符，文字层可用）
- 成品：`deliverable\EN47_Landweber_K理论与椭圆算子_中文译注本.pdf`
- **页映射：PDF 页 = 原书页**（PDF p1 = 扉页/arXiv 页，p2 = 目录，正文 §0 起于 p3，p50 = 参考文献）。
  书中第 N 页就是 PDF 第 N 页，不存在偏移。

### 底本元数据（写入 README）
- 作者：Gregory D. Landweber（University of Oregon）
- 题名：K-Theory and Elliptic Operators
- 来源：arXiv:math/0504555v1 [math.AT]，2005-04-27
- 篇幅：50 页；MSC 2000：Primary 55N15, 58J20；Secondary 19L47
- 性质：研究生入门讲义（由作者在 Princeton 本科讲座与 Oregon 研究生课程笔记整理），
  内容不原创，价值在统一记号、补全细节；附录 A/B 写得比常见文献细。

### 全书结构（原书页码）
| 节 | 标题 | 原书页 |
|---|---|---|
| §0 | The Index Problem（0.1 Introduction；0.2 Definitions and Examples） | 3–4 |
| §1 | K-Theory and Cohomology（1.1–1.7） | 5–13 |
| §2 | Statement of the Index Theorem（2.1–2.6） | 14–22 |
| §3 | Proof of the Index Theorem（3.1–3.4） | 23–31 |
| §4 | Equivariant K-Theory and Homogeneous Spaces（4.1–4.5） | 32–38 |
| A | A Proof of Bott Periodicity（A.1–A.5） | 39–45 |
| B | The Atiyah-Hirzebruch Spectral Sequence | 46–49 |
| — | References（[1]–[17]） | 50 |

**原文全部公式无编号、定理类环境无编号**（只有 `Definition.`、`Theorem (...).`、
`Proposition.`、`Claim.`、`Example.`、`Proof.`、`Corollary`、`Problem` 这样的标签，
没有「定理 1.2」式编号）。因此：
- 展示公式一律用 `\[ ... \]`，**禁止** `equation` / `\label` / `\tag`；
- 定理类环境一律用**不编号**的 `\newtheorem*` 版本（见 §6）；
- 交叉引用只用文字：「上面的定义」「第 2.2 节的构造」「式 (※) 不存在」。

## 2. 工程目录与写作用域

```
EN47_Landweber_K理论与椭圆算子_中文译注\
  BRIEF.md                  ← 本文件（Lead 独占）
  src\preamble.tex          ← 导言区（Lead 独占，译者只读）
  src\main.tex              ← 汇总文件（Lead 独占）
  src\chunks\cNN.tex        ← 你的块（唯一可写正文文件）
  src\tools\compile_chunk.py
  work\pages\pNNN.png       ← 150 dpi 整页图（只读）
  work\split\pNNN.txt       ← 文字层分页（只读，只当索引）
  work\zoom\                ← 300 dpi 裁片输出目录（可写临时文件）
  work\tmp_cNN\             ← 单块编译产物
  work\glossary.tsv         ← 冻结术语表（只读，不改正表）
  reports\cNN.md            ← 你的施工报告（可写）
  review\                   ← 校订记录（Lead/校订者写）
  deliverable\              ← 成品
```

**只写**：`src/chunks/cNN.tex`、`reports/cNN.md`、`work/zoom/` 与 `work/tmp_cNN/` 下的临时文件。
**绝不修改**：`src/preamble.tex`、`src/main.tex`、`work/glossary.tsv`、别人的 `chunks/*.tex`。
需要新宏、新术语、改体例 → 写进 `reports/cNN.md` 并在最后消息里告诉 Lead。
块文件**不要**写 `\documentclass`、`\begin{document}`、`\input{preamble}`。

## 3. 块划分表

| 块 | 内容 | 原书页（=PDF 页） | 起始小节 |
|---|---|---|---|
| c00 | §0 全节 + §1.1–§1.3 | 3–8 | `\section{指标问题}` |
| c01 | §1.4–§1.7 | 9–13 | `\subsection{Thom 同构}` |
| c02 | §2.1–§2.3 | 14–18 | `\section{指标定理的陈述}` |
| c03 | §2.4–§2.6 | 19–22 | `\subsection{奇维流形上的指标}` |
| c04 | §3.1–§3.3 | 23–27 | `\section{指标定理的证明}` |
| c05 | §3.4 | 28–31 | `\subsection{公理的验证}` |
| c06 | §4 全节 | 32–38 | `\section{等变 K 理论与齐性空间}` |
| c07 | 附录 A 全节 | 39–45 | `\section{Bott 周期性的一个证明}` |
| c08 | 附录 B + 参考文献 | 46–50 | `\section{Atiyah–Hirzebruch 谱序列}` |

- 块的起止以**节/小节标题**为界：块首第一行是 `\section{...}` 或 `\subsection{...}`。
- 附录用 `\section`（替代 `\appendix` 的字母编号）：标题写「附录 A Bott 周期性的一个证明」。
  二级小节写 `\subsection{预备}` 等，编号由 LaTeX 自动给 A.1/A.2…（`\thesubsection` 需与原文一致，
  preamble 已配好）。
- 每页起点在块内留一行注释：`% ===== 原书 p.9 =====`。

## 4. 工作流（每个块）

1. 读文字层 `work\split\pNNN.txt`（**只当索引**，数学符号一律不可信）。
2. 用 `read_image <本地路径>`
   看整页排版（150 dpi，1275×1650）。
3. 公式/上下标/花体/箭头细节看不清时裁 300 dpi 大图：
   `python work\tools\zoom.py N x0 y0 x1 y1`（坐标是页面比例 0–1，返回裁片路径，再用 `read_image` 打开）。
   **每一个展示公式、每一个定义/定理陈述、每个带上下标的符号都必须过一遍页图**。
4. 写 `src\chunks\cNN.tex`。
5. 编译自检：`python src\tools\compile_chunk.py cNN`（在任意目录执行均可；工程根为
   `<本地路径>`）；
   判据：errors 0 / overfull 0 / undefined 0 / missing char 0；再用 `read_image` 打开
   `work\tmp_cNN\wrap.pdf` 转出的页面目视（或直接读 PDF 文本核对）。
6. 写 `reports\cNN.md`（模板见 §8），给 Lead 发一条短消息：块号 + 公式/环境清单 + 疑点。

## 5. 文本层的坑（务必知道）

- **连字**：`ﬁ`(U+FB01)、`ﬀ`、`ﬂ`、`ﬃ`、`ﬄ` 出现在 Deﬁnition、diﬀerential、ﬂat 等词中；抄进正文前改回 fi/ff/fl。
- **上下标被拍平**：`H∗(X)`、`Kc(TX)`、`Hn(X; Z)` 这类都是上标/下标丢层次的残迹；
  `(−1)n` 实为 $(-1)^n$；`Λ∗(V )` 实为 $\Lambda^*(V)$。**一律回页图重读**。
- **行内公式错位**：`ξ̸ = 0` 实为 $\xi \neq 0$（≠ 被拆成 `̸ =`）；`∼=` 实为 $\cong$；
  `⊂`、`→`、`⊗`、`⊕`、`⌣`（上积）常出现为 `⌃`/`^`；`∂` 与 `d` 要区分。
- **图示**（交换图表）在文字层里是散落的字母与箭头，必须看页图重画。
- **脚注**：文字层把脚注排在页末，形如 `1The reader may…`；脚注必须并入正文 `\footnote{...}`，
  编号自动。
- 结论：**文字层只用来定位句子；凡要落进译文的公式与符号，一律以页图为准。**

## 6. LaTeX 规范

- 节标题：`\section{指标问题}`（原文「0 The Index Problem」），`\subsection{引言}`。
  **不写编号**，编号由 LaTeX 给。
- 展示公式：`\[ ... \]`。多行对齐用 `align*`（preamble 已允许）。
  公式内标点：句末标点放在公式后，不加在公式里。
- 定理类环境（全部不编号，preamble 已定义）：
  `definition`（定义）、`theorem`（定理）、`proposition`（命题）、`claim`（断言）、
  `example`（例）、`corollary`（推论）、`problem`（问题）、`proof`（证明环境）。
  带括号说明的照写：`\begin{theorem}[指标定理 A]`，渲染成「定理（指标定理 A）」。
  原文 Definition/Example 的正文用斜体，翻译后不用斜体（中文无斜体习惯），正文照排。
- 交换图表用 tikz-cd（preamble 已加载）。原文图表不编号，直接用 `\[ \begin{tikzcd}...\end{tikzcd} \]`
  或 `\begin{center}...\end{center}`。空单元写 `{}`；双线箭头用 `\arrow[r, Rightarrow]` 等。
- 花体：preamble 提供 `\cA...\cZ`、`\fA...\fD`、`\R \C \Z \Q \N \PP`、`\KK`。
  指标类用 `\IndexClass`（=\Im 的花体版本，preamble 定义，原名 ℑ）。
- 常用：`\Vect`（Vect）、`\K`（K）、`\Td`（td）、`\ch`（ch）、`\tind`（t-ind）、`\aind`（a-ind）、
  `\Ind`（Index）、`\Ker`、`\Coker`、`\rk`（rank）、`\pt`（pt）、`\dd`（d）、`\id`。
- 脚注：`\footnote{...}`，编号自动，与原文顺序一致（每页重新编号由 LaTeX 决定，可接受）。
- 参考文献：不翻译条目，`\begin{thebibliography}{99}` 里照抄英文，`\bibitem{[1]}` 用
  `\bibitem{1}` 形式（渲染为 [1]）。正文引用写 `[12]` 字面，不用 `\cite`。
- 译者批注：**命令形式** `\transnote{注文}`，紧跟被注段落之后独立成段。
  禁止 `\begin{transnote}...\end{transnote}`（会错排）。
- 中文标点全角；行内公式后接中文标点，标点在公式之后。
- **汉字与拉丁字母/数学公式之间不要手动加空格**：xeCJK 自动加间距；手加会出现双倍空隙。
- 段间空一行。

### 固定句式（全篇统一，减少风格漂移）
| 英文 | 译法 |
|---|---|
| Let X be … | 设 $X$ 是…… |
| We define … to be … | 把……定义为…… |
| Note that … | 注意…… |
| In particular, … | 特别地，…… |
| It follows that … | 由此得到…… |
| Thus / Hence | 于是 / 从而（同一段内交替，避免重复） |
| We obtain | 得到 |
| One checks that | 直接验证可知 |
| It is easy to see that | 容易看出 |
| if and only if | 当且仅当 |
| with respect to | 关于 |
| the map induced by f | 由 $f$ 诱导的映射 |
| by naturality | 由自然性 |
| as required | 如所要求 |
| a family of elliptic operators | 一族椭圆算子 |
| index of a family | 族的指标 |

## 7. 术语与批注

- 术语一律查 `work\glossary.tsv`（TSV：english / chinese / 备注）。表里有的照用，
  **不得自行改动**。表里没有的，首次出现写「中文（English）」，并在 `reports\cNN.md`
  的「新术语」节列出，由 Lead 汇总进表。
- 人名一律保留英文原名（Atiyah、Singer、Bott、Thom、Chern、Hirzebruch、Wiener、Hopf、
  Grothendieck、Fredholm、Dolbeault、de Rham、Poincaré、Euler、Todd）。
- 译者批注只写三类，每条必须有具体信息，全篇约 25–35 条：
  1. **易错预警**：读者极易混淆处（如 t-ind 与 a-ind 的区别；ℑ(X) 与 td(TX⊗C) 的关系；
     奇维流形上微分算子指标为零，所以必须扩到伪微分算子）。
  2. **含糊点拨**：原文省略的步骤/隐含约定（如「G-term」在等价关系里的作用；
     「proper map」为何保证延拓；横截性假设被省略之处）。
  3. **背景直觉**：为什么这样构造（如为什么用嵌入 R^m + 法丛复化造 t-ind；
     为什么象征给出 K(TX) 的类；为什么 Thom 同构是引擎）。
  **禁止**：复述原文、评价作者、写「值得注意的是」式空话、替作者补证明。

## 8. 中文文风（硬指标，交付前 grep）

- 以下句式出现次数必须为 0：
  「被……所」「进行……的」「对于……而言」「关于……的讨论」「使得……得以」
  「起到了……的作用」「有着……的意义」「众所周知」「不难发现」「值得注意的是」。
- 一句不超过 60–70 汉字；长句拆开。
- 不用「其」「该」「之」堆叠指代；不用「笔者」；少用「我们」（原文 we 可译为「我们」，
  但一段内不超过两次）。
- 数学句用「若…则…」「设…」「记…为…」「由…得…」「从而」。
- 被动语态少用；英文的被动长句改成中文主动或「可以…」。

## 9. 报告模板 `reports\cNN.md`

```markdown
# cNN 施工报告（原书 p.a–p.b）

## 完成情况
- 覆盖原书页：
- 小节：
- 展示公式：n 条（逐条列出所在页，便于复核）
- 定理类环境：定义 x / 定理 x / 命题 x / 断言 x / 例 x / 推论 x / 问题 x
- 图表：n 幅（tikz-cd 重画），位置
- 脚注：n 条
- 译者批注：n 条（一句话摘要 + 原书页）

## 疑点与请示（Lead 必读）
- 原文疑似笔误/含糊处（页 + 原文 + 我的处理）：
- 与块表不符处：
- 新术语（English → 中文）：

## 自检
- compile_chunk：errors / overfull / undefined / missing char
- 排版目视：通过/问题
```

## 10. 关键提醒

- **数学正确性高于一切**：宁可译得笨拙，不可译错符号、上下标、箭头方向、正负号。
- **不臆造**：原文省略、含糊、疑似错误 → 照原样译 + 批注，禁止「我觉得作者想说」。
- 读不懂的句子：先看 300 dpi 裁片，再查术语表与上下文；仍不懂就在报告里列出并给保守译法。
- 原文的 `t-ind`、`a-ind`、`ℑ(X)`、`K_c`、`S(TX)`、`H^*(X)` 等记号照抄，不改成中文。
- 每块完成后必须编译通过再交；**不要**把未编译的块留在 `chunks/` 里超过一个工作轮次。

## 11. 附：Lead 冻结的译名（与 glossary.tsv 同步）

指标问题 / 椭圆算子 / 象征（symbol）/ 主象征 / 椭圆复形 / 余核（cokernel）/ 核（kernel）/
指标（index）/ Fredholm 算子 / 解析指标（analytical index）/ 拓扑指标（topological index）/
象征映射 / 向量丛 / 复向量丛 / 实向量丛 / 线丛 / 切丛 / 法丛 / 平凡丛 / 子丛 / 商丛 /
拉回（pullback）/ 截面 / 零截面 / 局部平凡化 / 转移函数 / 粘合函数（clutching function）/
紧支撑 / 约化 K 理论 / 相对 K 理论 / Grothendieck 群 / 虚拟丛 / 同伦 / 同构类 /
直和 / 张量积 / 外幂 / 对偶丛 / 单位分解 / Hermite 度量 / 分类空间 /
Bott 周期性 / 悬挂（suspension）/ 环路空间 / 谱 / 广义上同调理论 /
Chern 类 / Chern 特征 / 示性类 / Euler 类 / Todd 类 / 基本类 / 上积（cup product）/
Thom 同构 / Thom 空间 / Gysin 映射 / 指标类（index class）/
等变 K 理论 / 齐性空间 / 诱导表示 / 表示环 / 特征（character）/
伪微分算子（pseudo-differential operator）/ 椭圆性 / 齐次复形 /
谱序列 / 纤维化 / 胞腔链复形 / 微分（differential of a spectral sequence）/
Wiener–Hopf 算子 / 切除（excision）/ 可缩 / 仿紧 / 单位分解 /
有向极限 / 幂等 / 投射模 / 挠 / 有限生成 / 半群 / 环 / 模
