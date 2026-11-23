# 风格指南 · SY01-07《几何内窥与镜像对称》中译注本

> 本工程服从 `04_playbook/01_数学文献翻译纪律.md` **v2.1** 与 `01_corpus_zh/数语规范/`（README + STYLE_NL + STYLE_FORMAL）。
> 本文件只写这部书的具体约定；与《纪律》冲突时以《纪律》为准。

## 0. 身份与目标

原文：Edward Frenkel & Edward Witten, *Geometric Endoscopy and Mirror Symmetry*, arXiv:0710.5939v3，2008，130 页。

读者：懂代数几何、表示论与 Langlands 纲领基本语言，但不一定做过几何 Langlands/镜对称计算的研究生与研究者。
目标文本：**读起来像一篇中文数学论文**，不是逐词硬译；数学正确性 > 术语一致 > 可读性。原文是研究论文，不是教材：保留作者的论证节奏、限定词与保留意见，不把猜想写成定理。

## 1. 文体

- 书面语；原文 *we* 译「我们」，*one* 视语境译「人们」或「我们」。
- 保留原文段落切分；长句可断，但 Thus / Hence / In particular / However / Of course / Namely 等逻辑连接词必须显式译出：因此／于是／特别地／然而／当然／即。
- 原文的谨慎语气（we expect / we predict / it is natural to conjecture / this suggests）必须保留；不得改成「证明了」「显然」。
- 中文标点全角（，。；：「」）；不用网络语、感叹号；英文缩写与中文之间按数语规范处理。
- 原文的斜体强调、引号、破折号保留其功能；不额外加「值得注意的是」之类填充语。

## 2. 术语

- 一律以 `工程文件/GLOSSARY.md`（及 `work/glossary.tsv`）为准；并行审校期间不得跨块改术语，发现新问题写进回报，由 Lead 统一裁定。
- 表外术语按学界通行译法；首次出现给「中文（English）」，并登记到 `work/glossary.tsv`。
- 人名、定理名、软件名不译：Frenkel、Witten、Langlands、Hitchin、Hecke、Ngô、Kottwitz、Labesse、Shelstad、Springer、Steinberg、Prym、Seiberg、Witten、SYZ、Bun_G 等。
- 保留英文的术语：gerbe、oper、improper Hecke functor、L-packet、B-field、spin structure、theta characteristic（按 GLOSSARY 已有条目执行）。
- 复合词中心词后置：geometric Langlands correspondence → 几何 Langlands 对应；Hitchin fibration → Hitchin 纤维化；Hecke eigensheaf → Hecke 本征层。
- 缩写首次出现给全称：SYZ（Strominger–Yau–Zaslow）、TQFT（如出现）、S-duality（S-对偶）。

## 3. 数学排版

- 公式、编号、环境一律照原文；公式编号 (x.y) 不得重排、不得合并。
- 只允许使用 `源码/preamble.tex` 已定义的宏与 amsmath/amssymb/mathtools/bm/tikz 标准命令；**不得新增 `\newcommand`**。
- `\label`/`\ref`/`\cite` key 保留原名；文献标签 `[KW]`、`[N1]` 与原文一致。
- 公式中的英文单词（`\mathrm{Bun}`、`\operatorname{Spec}`、`\mathrm{Higgs}` 等）不译。
- 插图：原书 p.18 唯一插图，`figures/fig-p18-hitchin-fibers.png`，图注中文并标「原书 p.18」；不得补画原文没有的图。
- 脚注保留为脚注；编号由 LaTeX 重排，属正常现象。

## 4. 页锚点与分片

- 每页正文前一行：`% ==== 原文 PDF 第 N 页（印刷页 N）====`，N 用阿拉伯数字；不得跳页、重号。
- 分片按 `s01-intro.tex` … `s11-appendix.tex` + `references.tex`；`main.tex` 用 `\frag{...}` 顺序引入。
- 每节开头保留 `keytakeaway` 环境（本节重点：物理图像/数学工具/主要结论），它是译注，不是原文。
- 页边界段落跨页时，中文可挂在上一页锚点下；审校按块核对，不按单页字数判断漏译。

## 5. 批注

四类，写在 LaTeX 注释里，不进入排版：

| 类型 | 用途 | 格式 |
|---|---|---|
| Tutor Note | 推导补足、易错预警、物理图像 | `% [Tutor Note: …]` |
| 原文疑误 | 已判定为原书笔误，译文照录 | `% [原文疑误: 原书 p.N …；判断依据 …]` |
| 存疑 | 无法从原文确证、但疑有问题 | `% [存疑: …]` |
| 背景补充 | 对中文读者构成门槛的术语/背景 | `% [背景补充: …]` |

每条解释性批注必须有来源标记（v2.1 §2.5.6），放在批注末尾：
- 只依据原书上下文：`[依据：原书 p.N 第 X 段；…]`
- 依赖外部来源：`[来源：nLab/Stacks/ProofWiki/教材/原始论文 …（A/B/I 级）]`
- 无外部依据的推断：`[译者按（上下文推断，无外部依据）：…]`

禁止：黑名单来源（知乎、百度百科、CSDN、简书、公众号、B站、个人博客、AI 摘要）；编造页码/定理号/链接/访问日期；把 nLab 句子直译照抄。

## 6. 数学内容

- 一切数学陈述照原文；发现原文错误时译文照译，紧随其后加「原文疑误」批注，**不直接把原文改成正确式子**。
- 译者对原书笔误的修正（若正文已按正确数学写）保留，并在批注标明「原文疑误/译者补正」；审校时不得改回原文。
- 不补原文没有的定理、条件、证明；需要背景时写进批注，不塞进正文。

## 7. 编译与交付

- 命令：`xelatex main.tex` 连续两遍；不得留 `.aux`、`.log`、`.synctex.gz` 入库。
- 自检：0 error、0 overfull、0 undefined、0 missing character；页数与 BRIEF 对得上。
- 成品：`工程文件/deliverable/Frenkel-Witten_几何内窥与镜像对称_中文译注本.pdf`。
- 单文件版 `Frenkel-Witten_几何内窥与镜像对称_0710.5939.tex` 是发布副本，改动后必须与分片版同步重建。
