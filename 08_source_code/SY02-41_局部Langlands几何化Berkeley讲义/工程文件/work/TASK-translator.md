# 译手契约 · SY02-41《局部 Langlands 对应的几何化：Berkeley 讲义》

> 你是本工程的译手。**只做分给你的那几讲**，只写分给你的那几个 `.tex` 文件。
> 本次翻译的是 Peter Scholze 讲授、Tony Feng 记录的讲义（148 页，27 讲）。
> 数学正确性优先于文采；不确定的地方**照原文直译 + 记入疑点清单**，绝不臆造。

## 一、输入

1. 原文纯文本：`C:\Users\admin\Downloads\fs_scholze_work\lectures\LNN.txt`（NN 为讲次）。
   页界以 `%%% ===== 原文 pN =====` 标记；**印刷页码 = PDF 页码**（偏移 0）。
2. 页面图像：`C:\Users\admin\Downloads\fs_scholze_work\imgs\pNNN.png`（150 dpi）。
   文本层是线性化的，上下标会拆行、`ﬁ` 是连字、`⊕` 可能变 `M`、`⊔` 变 `a`、`\breve E` 变 `˘E`。
   **凡是公式、上下标、括号嵌套不确定，必须打开对应页图核对**。这是硬要求：公式只信页面图像。
3. 术语表：`C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-41_局部Langlands几何化Berkeley讲义\工程文件\work\glossary.tsv`
   （207 条，第一部分是英文/中文/依据/出处四列）。**开译前整表读一遍**。
4. 记号表：同目录 `work/symbols.tsv`。

## 二、输出

- 只为分给你的每一讲写一个文件：
  `C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-41_局部Langlands几何化Berkeley讲义\源码\sections\sNN-*.tex`
  （文件名分别人已固定，覆写占位内容即可）。**不要改 `main.tex`、`preamble.tex`，不要碰别人的 section 文件。**
- 另写一份报告：`工程文件/reports/chNN-*.md`（见第六节）。

## 三、LaTeX 格式契约（照抄，不要自由发挥）

1. 文件**第一行**就是节标题，形如：
   ```latex
   \section[Fargues--Fontaine 曲线 I]{Fargues--Fontaine 曲线 I（11 月 2 日）}
   ```
   方括号里是目录/页眉用短名（不带日期），花括号里是正文标题（带日期）。
   短名与正文标题以本说明分配给你的为准（见第五节表），不要自己改。
2. **页锚**：每遇到 `%%% ===== 原文 pN =====`，就在该页第一段正文之前写 `\srcpage{N}`。
   例：`%%% ===== 原文 p7 =====` → `\srcpage{7}`。
3. **编号一律交给 LaTeX，禁止手写编号**：
   - 原文 `1.1. Setup.` → `\subsection{Setup}`（自动排成「1.1 Setup」）。
     原文 `1.8.1.` 这种三级标题 → `\subsubsection{...}`。
   - 原文 `Definition 1.1.` → `\begin{definition}...\end{definition}`；
     同理 `\begin{example}`、`\begin{theorem}`、`\begin{proposition}`、`\begin{lemma}`、
     `\begin{corollary}`、`\begin{remark}`、`\begin{warning}`、`\begin{question}`、
     `\begin{conjecture}`、`\begin{notation}`。
   - **所有编号条目共用一个计数器**（自动排成「讲次.序号」）。这意味着：
     原文出现的**每一个**编号条目都必须落成一个环境，**一个都不能漏、顺序不能变**，
     否则该讲后面所有编号全错。译完请数一遍：本节最后一个编号是否等于原文最后一个编号。
   - 本讲义不用 `chapter`，讲次就是 `\section`。
4. 数学：行内 `$...$`，行间 `\[...\]` 或 `align*`/`gather*`（不要用 `eqnarray`）。
   **行间公式一律不编号**：不用 `equation` 环境，不写 `\label`，**禁用 `\eqref`、`\ref`、`\cite`**。
   原文用公式编号回指（"the functor (4.3.1)"、"by (3.2.1)"）时，改写成描述性说法
   （「上述函子」「前式」「即前一个短正合列」）。
   交换图用 `tikz-cd`（preamble 已载入 `tikz`、`tikz-cd`）。简单箭头图也用 tikz-cd。
5. 只有 preamble 里定义过的宏才能用。已知可用：`\cA`–`\cZ`（花体）、`\Bun \Bun_G`、`\Spa`、`\Hck`、
   `\Perf`、`\Div`、`\Gr`、`\Isoc`、`\Vect`、`\Rep`、`\LocSys`、`\QCoh`、`\Dmod`、`\Sht`、`\BT`、
   `\Qp \Zp \Fp \Fq \Fl \Ql \Zl`、`\BdR \Bcris \Bst \BHT \Ainf`、`\breveE`、`\Lam`、
   `\et`（é t 连写，用于 étale 外的场合；**étale/pro-étale 请直接写 `étale`、`pro-étale` 原词**）、
   `\Tr \Aut \End \Ext \Hom \Tor \Gr \Pic \Lie \Sym \Ind \Res \Gal \Weil \Frob \Art \Proj \Spf \Isom \id \im \coker \rk \HN \Spec`、
   `\wt{} \ol{} \ul{}`、`\Fil \trdeg`。
   不在这个表里、preamble 也没有的宏**不许用**；需要新记号就写纯 LaTeX（`\mathrm{...}`、`\operatorname{...}`）。
6. 脚注：原文脚注 → `\footnote{...}`；**译注** → `\yizhu{正文}{来源}`，
   来源写等级 + 出处，例如 `\yizhu{...}{A（原文 §1.2 p.8）}`、`\yizhu{...}{I（本库 SY02-26 术语表）}`、
   `\yizhu{...}{B（nLab "condensed mathematics"）}`。**译注只在三种情况写**：
   术语背景、原文省略、原文笔误；每条 1–4 句，每讲不超过 6 条。不要写读后感。
7. 引文/文献：原文 `[FS]`、`[KL15]` 之类保持原样。参考文献表由 lead 统一做，不用你写 `thebibliography`。
8. 不要写 `\usepackage`、不要写 `\documentclass`、不要写 `\begin{document}`。

## 四、译文风格

- 书面现代汉语，句子长度 ≤ 60–70 汉字；长英文句拆成两三句。
- 逻辑连接词按词义分译：Thus→因此、Hence→从而、Therefore→所以、In particular→特别地、
  Conversely→反之、Indeed→事实上、Namely→即、However→然而、Note that→注意、
  Recall that→回忆、Similarly→类似地、More precisely→更确切地说。
- 首现术语写「中文（English）」，同一术语后续只用中文；**人名、定理名、软件名、记号不译**。
- 中文与拉丁字母/数字之间加一个半角空格（如「étale 上同调」「Fargues–Fontaine 曲线」「$p$ 进」）。
- 标点用全角（，。；：？！「」），公式内仍用半角。
- 原文的破折号 `—` 用 `——`；`i.e.`→即、`e.g.`→例如、`cf.`→参看、`resp.`→分别。
- 原文 `1.1` 这类小节号不要手写；交叉引用原文用「Theorem 2.14」就直接写「定理 2.14」（正文里的定值引用照抄数字）。
- 不确定的句子宁可直译加括号注英文原词，也不要改写数学内容。

## 五、本次分给你的讲次

| 讲次 | 原文文件 | 输出文件 | 短名 | 正标题 |
|---|---|---|---|---|
| 见任务消息 | LNN.txt | sNN-*.tex | 见任务消息 | 见任务消息 |

（每条任务的短名/正标题在任务消息里给出，与 `main.tex` 中的一致。）

## 六、自检（交稿前逐条过）

1. `\srcpage{N}` 个数 = 原文该讲的页数；页锚顺序递增。
2. `\begin{x}` 与 `\end{x}` 一一配对；`$` 成对；`\[`/`\]` 成对。
3. 没有 `\usepackage`、没有 `\section*`（除非原文确有无编号小节）、没有手写编号。
4. 本节最后一个编号条目与原文最后一个编号一致（数一遍）。
5. 术语与 `glossary.tsv` 一致；`grep` 旧译/禁用译名 = 0。
6. 报告写 `工程文件/reports/chNN-*.md`，四个小节：
   - `## 一、范围与页数`（原文 pX–pY，共 n 页，`\srcpage` n 个）
   - `## 二、术语新增/异议`（表格：英文 / 你用的中文 / 依据 / 页码）
   - `## 三、疑点`（原文可能笔误、跳步、看不懂的句子；写清页码与你的处理）
   - `## 四、遗留`（没做完、需 lead 定夺的）

## 七、禁止

- 不臆造定理、不补证明、不「顺手改好」原文的错误（只记疑点）。
- 不看/不引黑名单站点；不联网。
- 不在 `work/`、`reports/` 之外写文件；不留 `.aux`、`.log`。
- 不写「本讲作者认为」这类评论；译文里不出现「译者以为」以外的主观话（译注一律走 `\yizhu`）。
