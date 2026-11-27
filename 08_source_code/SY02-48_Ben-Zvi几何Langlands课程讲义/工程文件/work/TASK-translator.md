# 译手契约 · SY02-48《几何 Langlands：Ben-Zvi 课程讲义》

> 你是本工程的译手。**只做分给你的那几讲**，只写分给你的那几个 `.tex` 文件。
> 底本：David Ben-Zvi 讲授、Arun Debray 记录的 UT Austin M390C（Geometric Langlands，
> 2021 春季）live-TeX 讲义，89 页 31 讲。
> 数学正确性优先于文采；不确定就**照原文直译 + 记入疑点**，绝不臆造。

## 一、输入

1. 原文纯文本：`lectures/LNN.txt`（NN 为两位讲次，如 `L07.txt`）。
   页界以 `%%%%% ===== 原文 pN =====` 标记；**印刷页码 = PDF 页码，偏移 0**。
2. 页面图像（仅在文本层公式被拍扁时用）：`工程文件/work/pages/pNNN.png`（150 dpi）。
   文本层是线性化的：分式被拆成三行、上下标拆行、`⊗` 可能变 `O`、`⊕` 变 `M`、
   `ﬁ` 是连字、`˘` 是 `\breve`。**行间公式拿不准就打开对应页图核对**（用 `read_image`）。
3. 术语表：`工程文件/work/glossary.tsv`（四列：英文 / 中文 / 依据 / 出处）。**开译前整表读一遍**。
   表里有的**必须照用**；表外先查 `01_corpus_zh/数语规范/TERMS.tsv` 与同目录 SY02-41/SY02-26 的
   glossary；都没有就**保留英文**并在报告 §2 登记，**不许自己造新译名**。
4. 条目总表：`工程文件/work/条目总表.tsv`（原文每个编号条目的页码与首句，供你核对条目不漏）。

## 二、输出

- 每讲一个文件：`源码/sections/sNN-*.tex`（文件名已固定，**覆写占位内容**；表见第五节）。
- 每讲一份报告：`工程文件/reports/chNN.md`（格式见第六节）。文件名就是 `ch01.md` … `ch31.md`。
- 不在别处写文件；**不要碰 `main.tex`、`preamble.tex`、别人的 section 与报告**。

## 三、LaTeX 格式契约（照抄，不要自由发挥）

1. 文件**第一行**就是节标题，占位文件里已经写好，例如：
   ```latex
   \section[概览与模形式的一种视角]{概览与模形式的一种视角（1 月 19 日）}
   ```
   **标题照占位文件里的原样保留**（含日期），只往下写正文。
2. **页锚**：每遇到 `%%%%% ===== 原文 pN =====`，就在该页第一段正文前写 `\srcpage{N}`。
   例：`%%%%% ===== 原文 p7 =====` → `\srcpage{7}`。页锚顺序递增，一页一个，不多不少。
3. **编号一律交给 LaTeX，禁止手写编号**：
   - 原文 `1.1. Setup.` → `\subsection{Setup}`；`1.8.1.` → `\subsubsection{...}`。
   - 原文 `Definition 3.2.` → `\begin{definition}...\end{definition}`；同理
     `example`、`theorem`、`proposition`、`lemma`、`corollary`、`remark`、`warning`、
     `question`、`conjecture`、`notation`、`fact`、`exercise`、`construction`、`hope`。
   - **所有编号条目共用一个计数器**，自动排成「讲次.序号」。所以：原文**每一个**编号条目
     都要落成一个环境，**一个都不能漏、顺序不能变**，否则该讲后面所有编号全错。
     原文条目里的 "1.2" 之类**不要写进正文**，环境会自动排。
   - 本讲义不用 `chapter`，讲次就是 `\section`。
4. 数学：行内 `$...$`；行间用 `\[...\]` 或 `align*`/`gather*`（不用 `eqnarray`）。
   **行间公式一律不编号**：不用 `equation`，不写 `\label`，**禁用 `\eqref`、`\ref`、`\cite`**。
   原文用公式号回指（"by (9.8)"、"the map (3.4.1)"）时改写成「前式」「上述映射」
   「即前面那个限制乘积」这类描述性说法。
   交换图用 `tikz-cd`（preamble 已载入）。原文的 `_` 下标里的多字符请加花括号。
5. 可用宏（preamble 已定义）：`\cA`–`\cZ`（花体）、`\Bun`、`\BunG`、`\Spa`、`\Hck`、`\Perf`、`\Div`、
   `\Gr`、`\Isoc`、`\Vect`、`\Rep`、`\LocSys`、`\QCoh`、`\IndCoh`、`\Dmod`、`\Sht`、`\BT`、
   `\Qp \Zp \Fp \Fq \Fl \Ql \Zl`、`\BdR \Bcris \Bst \BHT \Ainf`、`\breveE`、`\Lam`、`\et`、
   `\Tr \Aut \End \Ext \Hom \Tor \Pic \Lie \Sym \Ind \Res \Gal \Weil \Frob \Art \Proj \Spf \Isom \id \im \coker \rk \HN \Spec \rank \Perv \dashto`、
   `\wt{} \ol{} \ul{}`、`\Fil \trdeg`、`\Q \Z \C \R \F \A \G \P`（单字母域符号）。
   不在表里、preamble 也没有的宏**不许用**；需要新记号就写 `\mathrm{...}`、`\operatorname{...}`。
6. 脚注：原文脚注 → `\footnote{...}`；**译注** → `\yizhu{正文}{来源}`，
   来源写等级 + 出处，如 `\yizhu{...}{A（原文 p.42）}`、`\yizhu{...}{I（本库 SY02-41 术语表）}`、
   `\yizhu{...}{B（nLab "topological field theory"）}`。**译注只写三类**：术语背景、
   原文省略、原文笔误；每条 1–3 句，**每讲 ≤ 6 条**。不写读后感。
7. 引文 `[Mac80]`、`[Lur09]` 之类原样保留（参考文献表由 lead 统一排，不用你写）。
8. 不写 `\usepackage`、`\documentclass`、`\begin{document}`、`\section*`。

## 四、译文风格

- 书面现代汉语，一句 ≤ 60–70 汉字；长英文句拆成两三句。
- 逻辑词按词义分译：Thus→因此、Hence→从而、Therefore→所以、In particular→特别地、
  Conversely→反之、Indeed→事实上、Namely→即、However→然而、Note that→注意、
  Recall that→回忆、Similarly→类似地、More precisely→更确切地说、On the other hand→另一方面。
- 首现术语写「中文（English）」，后续只用中文；**人名、定理名、软件名、记号不译**
  （Ben-Zvi、Debray、Langlands、Hecke、Satake、Tannakian、Fourier、Maxwell、Wilson、't Hooft、Witten 等）。
- 中文与拉丁字母/数字之间加一个半角空格（「Hecke 代数」「$p$ 进」「2021 年」）。
- 标点全角（，。；：？！「」），公式内仍半角。破折号 `—` 用 `——`。
- `i.e.`→即、`e.g.`→例如、`cf.`→参看、`resp.`→分别、`iff`→当且仅当。
- 原文正文里写「Theorem 6.2」就写「定理 6.2」（数字照抄，不许改）。
- 原文是**课堂口语**，有 "Maybe we are Odysseus…"、"TODO: I need to fix these restricted products"
  "be careful/sorry!" 这类话：**照译**，保留口语味；`(TODO: …)` 原样译成「（TODO：……）」，
  **不要删、不要替作者改**。原文铅笔注记、`(be careful!)` 一律保留。

## 五、本次分给你的讲次

见任务消息里的表（讲次 / 原文文件 / 输出文件 / 标题）。文件名与标题以 `源码/main.tex` 为准。

## 六、自检（交稿前逐条过，必须跑到 OK）

```bash
python 工程文件/tools/check_sections.py NN MM
```
（在工程根目录跑；NN/MM 是你的讲次。它会核页锚序列、编号条目数、环境配对、禁用命令。）
**必须 0 问题**才能交稿。然后写报告 `工程文件/reports/chNN.md`：

```
## 一、范围与页数
原文 pX–pY，共 n 页，`\srcpage` n 个；编号条目 m 条（原文 m 条）。

## 二、术语新增/异议
| 英文 | 中文 | 依据 | 页码 |

## 三、疑点
原文可能笔误、跳步、看不懂的句子；写清页码与你的处理。

## 四、遗留
没做完、需 lead 定夺的（没有就写「无」）。
```

## 七、禁止

- 不臆造定理、不补证明、不「顺手改好」原文错误（只记疑点）。
- 不联网、不引黑名单站点。
- 不留 `.aux`、`.log`；不写 `work/`、`reports/`、自己 section 之外的文件。
- 译文里不出现「译者以为」这类主观话（译注一律走 `\yizhu`）。
