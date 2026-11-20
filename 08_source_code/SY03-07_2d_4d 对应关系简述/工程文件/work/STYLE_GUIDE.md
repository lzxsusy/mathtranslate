# STYLE_GUIDE —— 译本硬规范（tr-01 … tr-06 必读，逐条遵守）

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 与 LICENSE 为准：译文与语料是第三方底本的演绎作品，本库不代原作者授权、也不另设限制（检索、研究、教学、训练均可），权利人通知即撤；自产元数据、术语、工程文档与工作流为 CC BY 4.0。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

> 项目：Yuji Tachikawa, *A brief review of the 2d/4d correspondences*（arXiv:1608.02964v5，46 页）
> 中文译注本。底本体量：正文 pp.1–41，参考文献 pp.41–46（77 条）；
> **13 幅矢量图（图 1–13）/ 0 张表 / 137 条编号公式 / 无附录 / 无习题 / 无要点框**。
> 本规范由 Lead 冻结；译者**只读**，不要修改本文件、`preamble.tex`、`main.tex`、别人的 chunk。

---

## ① 页码体系

- 底本 PDF 页号 = 印刷页码（偏移 0）。全文一律写「原文 p.N」。
- 每个原文页开始处插一行注释：`% [原文 p.N]`
- 每个 chunk 文件开头写一行：`% ===== 原文 pp.X–Y =====`（本块页段）
- 本译本自身的页眉页码由 LaTeX 自动生成，不用管。

## ② 片段规则（chunk）

- 文件：`work/src/chunks/trNNa.tex`、`trNNb.tex`、`trNNc.tex`，UTF-8 **无 BOM**、**LF** 换行。
- 按 a→b→c 顺序被 `main.tex` 拼装；**已在 main.tex 里按块顺序固定注入**，不要新增文件、不要改 main.tex。
- 建议每 2–4 页写一片，**边译边写**，不要等全读完再一次性写一个大文件。
- chunk 里**不许**出现：`\documentclass`、`\usepackage`、`\begin{document}`、`\end{document}`、`\newcommand`、`\renewcommand`、`\input`、`\include`。
- **不许**写 markdown 记号（`**粗体**`、`#` 标题、`- ` 列表）；一律用 LaTeX 命令。
- 标题层级只用 `\section` / `\subsection` / `\subsubsection`，**且只在 BRIEF 指定的位置**写。
  编号由 LaTeX 自动生成，**不要手写「2.1」这样的编号**。
- 文件末尾不要 `\end{document}`；一个字都没写就别建文件。

## ③ 公式编号（R4：唯一真值 = `work/tags.txt`）

- 全部 **137 条**编号公式必须与原文一一对应：**不缺、不重、不跳、不重排、不自造**。
- 编号公式一律：
  ```latex
  \begin{equation}
    ... \tag{2.13}
  \end{equation}
  ```
- 多行公式用 `align`/`gather`，**每行一个 `\tag`**；一条编号跨多行时 `\tag` 放最后一行。
- 无编号公式用 `\[ ... \]` 或 `equation*`，**绝不自造编号**。
- 引用公式一律写纯文本「式 (2.13)」，**不要用 `\ref`/`\eqref`**（tag 是手写的，自动引用会指错）。
- 公式太宽导致 Overfull 时：
  `\begin{equation}\resizebox{0.985\textwidth}{!}{$\displaystyle ...$}\tag{X.Y}\end{equation}`
- 你的块的 tag 区间写在 BRIEF 里；**首尾必须与邻居接上**。交稿前用
  `work/tags_bypage.txt` 逐页核对一遍（那是实测出来的真值表）。

## ④ 可用宏（只能用 preamble 里定义过的；需要新宏 → 报告 Lead，不要自己 `\newcommand`）

- 集合：`\R \C \Z \N \Q \E`
- 花体：`\cA`…`\cZ`（`\cN` = N=2 里的花体 N、`\cO`、`\cZ` 等）
- frak：`\fg \fh \ft \fu \fsu \fso \fsp`
- 群：`\SU \SO \Sp \USp \U \GL`（正体，直接用，不要写 `\mathrm{SU}`）
- 微分/指数/虚数：`\dd \ee \ii`
- 算子：`\Tr \tr \diag \sgn \ord \vol \rk \rank \Pf \Res \id`（`\det` 用 LaTeX 自带的）
- 理论名：`\Toda \Liouville`
- 常数：`\half`
- 缩写：`\ie \eg \cf`
- 带上划线简写：`\bQ \bq \bN \bepsilon \btheta \bphi \bpsi \blambda`
- 版式宏：`\para{...}`（原文粗体行内小标题）、`\figtitle{N}{...}`、`\tabtitle{N}{...}`、
  `keybox`/`keyboxplain`（本底本用不到）、`exercise`（本底本无习题）、`\refitem`（参考文献专用）
- 其它直接用 amsmath/mathtools 的（`\frac \tfrac \dfrac \sum \int \prod \sqrt \overline
  \widehat \tilde \langle \rangle \mathbb` 等），TikZ 也可用。

## ⑤ 批注格式（Tutor Note）

- 一律写成 LaTeX 注释，**不进入排版**：
  ```latex
  % [Tutor Note: p.13, 式 (2.50) 下面这一步：作者把 ... 直接写成 ...；中间用到的是 ...
  %  容易错的地方是 ...]
  ```
- **密度：每 2–3 页 ≥ 1 条，每节 ≥ 3 条。**本块公式密集处请加到更多。
- 批注必须是**可验证**的内容，只允许四类：
  1. 易错点的精确提醒（哪个符号/哪个上下标/哪个因子 2 容易漏）；
  2. 作者跳过的推导步骤**补出来**（写清「由 X 代入 Y 得」的具体代数）；
  3. 原文笔误的指认 + 正确形式（**必须先 500 dpi 裁图复核**，见 ⑨）；
  4. 与其它章节/文献的对照（「这与 §5.1 的 (5.3) 是同一件事」）。
- **禁止**：空泛的「这里很重要」「注意理解」；编造原文没有的物理内容；写不成对的 `$`
  （批注里可以有 `$...$`，但必须成对，否则自检脚本误报）。

## ⑥ 图 / 表 / 要点框 / 定理

- **图**：13 幅图全是原文矢量图，由 Lead 用 500 dpi 裁成 `work/figures/figN.png`。
  写法（**不要用 `\caption` 自动编号**）：
  ```latex
  \begin{center}
    \includegraphics[width=0.42\textwidth]{fig5.png}
    \figtitle{5}{原文图注的中文翻译}
  \end{center}
  ```
  图注 = 原文 `Figure N:` 之后那句话的**忠实中译**，不许增删内容。
- **表**：**底本 0 张表**。如果你"觉得"某处该有表 —— 没有，不要造表（R1）。
- **要点框**：原文没有灰色要点框。**不要用 keybox**。
- **定理环境**：原文没有编号定理；`theorem*` 等只是备用，不要滥用。
- **脚注**：原文有少量脚注，用 `\footnote{...}` 就地排；跨块时核对编号连续性。

## ⑦ 禁止事项（违反 = 返工）

1. 不改别人的 chunk 文件；不改 `preamble.tex` / `main.tex` / 本文件。
2. 不自造公式编号、不改公式编号顺序。
3. 不把整段英文原文留在正文（图注里的英文原句也必须译；专有名词除外）。
4. 不删原文内容、不「顺手简化」原文的推导。
5. 不用 `\ref` `\eqref` `\cite`；文献引用写 `[12]`、`[45–54]`（en-dash 写 `--`）。
6. 不用 markdown 记号；不写 `\newcommand`；不写 `\documentclass`。
7. 不猜看不清的公式：看不清就裁图放大；仍看不清 → 写进回执，让 Lead 复核。

## ⑧ 边界规定（跨块接缝，最容易重复/遗漏）

- 原则：**跨页/跨块的句子，由「开始者」写完**。
- 每个块的**起点与终点锚点句**写在 BRIEF 里，**逐字对齐**：
  - 你的块从锚点句**开始**（含该句），不要重写上一块已经写过的半句；
  - 你的块到锚点句**之前**结束，不要越界抢下一块的标题或首句。
- 边界裁决以 `work/TIMELINE.md` 为准（Lead 已写死）。
- 章节标题归属：`\section`/`\subsection` 由 BRIEF 指定的归属者写；**别人不要重复写**。

## ⑨ 文字层可靠度（血泪教训）

- ✅ 正文单词、段落边界、脚注、章节标题 —— 文字层可信，用来定位与理解。
- ❌ **数学符号一律不可信**：`\frac{m}{2}` 可能抽成 `2m`；上下标错位；
  `\mathcal{N}` 抽成 `N`；`\omega` 抽成 `f`；`\alpha` 抽成 `a`；
  `n_\ell-1` 抽成 `n_{\ell-1}`；`\bar` 横线直接丢失；`\int` 抽成孤立符号。
  **每个公式必须逐页看 `work/pages/pNNN.png`（200 dpi）逐符号抄写。**
- 看不清细节时裁图放大（500–1000 dpi）：
  ```powershell
  $py = "<本地路径>"
  & $py "<本地路径>" <页> <x0> <y0> <x1> <y1> <out.png> [dpi]
  ```
  坐标是 PDF 点坐标，整页 **612 × 792**（本底本是 US Letter，不是 A4）。
- ⚠️ **任何「原文笔误」的指控，必须先用 500+ dpi 裁图复核原文**，否则不许写进批注。

## ⑩ 交稿前自检清单（逐项过，回执里逐项写 pass/fail）

```
[ ] chunk 文件都在 work/src/chunks/ 下，命名 trNNa/b/c.tex，UTF-8 无 BOM、LF
[ ] 没有 \documentclass/\usepackage/\begin{document}/\newcommand/\input/\ref/\eqref/\cite
[ ] 没有 markdown 记号；去注释后 $ 数量为偶数
[ ] \tag 集合 == BRIEF 给我的 tag 区间（不缺、不重、不跳、不自造）
[ ] 花括号平衡；\begin/\end 配对
[ ] 每 2–3 页 ≥1 条 Tutor Note，每节 ≥3 条
[ ] 图按 \figtitle 写、编号与原文一致（图注已译）
[ ] 章节标题只写我归属的那些，没越界
[ ] 首尾与 BRIEF 的锚点句对齐（没重复邻居的半句、没抢邻居的标题）
[ ] 每个公式都对着 200 dpi 页图逐符号核过（不是抄文字层）
```

## ⑪ 回报格式（send_message 给 lead，固定 5 项）

1. **文件与页段**：写了哪几个文件、覆盖原文 pp.X–Y；
2. **tag 区间**：实际写出的 tag 列表范围，有无跳号/存疑；
3. **原文可疑或笔误**：页 + 式号 + 判据（已裁图复核的写「已复核」）；
4. **新增术语**：英文 → 中文（Lead 汇总进 glossary 再全书归一）；
5. **自检结果**：⑩ 的清单逐项 pass/fail。

## ⑫ 术语（`work/glossary.tsv` 为冻结表，制表符分隔）

- 首次出现写「中文（English）」，之后只用中文；人名/模型名/缩写（SU(2)、CFT、OPE、TN、DOZZ）保留英文。
- 拿不准就**照 glossary.tsv**；glossary 里没有的，按最通行译法译并在回执第 4 项报告。
- 同一英文**全书只能有一个中译**；发现邻居用了别的译法 → 报告 Lead，不要自己改别人的文件。
