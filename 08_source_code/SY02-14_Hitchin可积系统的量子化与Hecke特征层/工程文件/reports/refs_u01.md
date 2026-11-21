# refs_u01（原书 p.381–p.386 参考文献）

## 已核对范围

- 页面图像 `工程文件/work/pages/p381.png … p386.png`（1445×1870）六页全部通读，逐条与文本层对照；对 `[Ak]`、`[D71]`、`[Se]`、`[J]`、`[T]`/`[Ve]` 另外做了 2–6 倍局部放大核对。
- 逐页条数：p381 16、p382 16、p383 13、p384 15、p385 16、p386 13，合计 **89 条**（脚本只生成 88 条，见下）。
- 跨页断点：p385→p386 断在 `[FF92]` 的 "…editors A. Tsuchiya, T. Eguchi, M. | Jimbo, Adv. Ser. in Math. Phys. …"，脚本已正确合并。

## 改动统计

- 条目：**88 → 89**。多出的一条是 `[Ve] Verdier`：p386 上 `[T]` 与 `[Ve]` 本是两条，脚本把 `[Ve]` 整条粘在 `[T]` 末尾（原文件第 88 行 `… vol. 1 (1968), 149–159. [Ve] J.L.Verdier. Catégories dérivées. In: SGA 4^{1}_{2}, Lecture Notes in Mathematics, vol. 569, 262–311. …`）。已拆成两行，`[T]` 尾句补回句点，`SGA 4½` 用 `$4\frac{1}{2}$` 排出叠分数。
- **45 条**有实质改动，**43 条**只是加了书名/刊名的 `\emph`（或未动）。`\emph{}` 共 **100 处**。
- 行末断字合并 4 处：`Pro-ceedings`、`struc-ture`、`Kashi-wara`、`multi-plicities`（`Korteweg-deVries`、`Gelfand-Dikii`、`Kac–Moody` 等真连字符/破折号一律未动）。
- 标点前多余空格：` ,` → `,` 共 **29 处**。
- 符号与连字符之间被空格断开（`𝔤 -modules`、`G - bundles`、`D -modules`、`C -categories`、`W -algebra`、`B -structures` 之类）共 15 处，涉及 `[BB81][BL][BLaSo][DSim][Fal93][F91][IM][Kas][Pa][Phys][Sa89][Sa91]`。
- Unicode 数学字符：`𝔤` → `$\mathfrak{g}$` 2 处（`[BB81]` 的 `$\mathfrak{g}$-modules`、`[BL]` 的 `$(\mathfrak{g},K)$-modules`）、`𝔭` → `$\mathfrak{p}$` 1 处（`[IM]` 的 `$\mathfrak{p}$-adic`）。`[MV]` 的 `BG`、`[Pa]` 的 `C-categories`、`[Kas]`/`[Sa89]`/`[Sa91]` 的 `D-modules` 等按原书排成数学斜体（`$BG$`、`$C$-categories`、`$D$-modules`）。
- 文本层丢失的重音补回 4 处：`[Del70] à points`、`[Se] fibrés à fibre vectorielle`、`[La88] cône`、`[Gi87] Kähler`（文本层原为 `a`、`a`、`coˆne`、`Ka¨hler`）。人名重音（`Gel'fand`、`Rozenfel'd`、`Mirković`、`École`、`Astérisque`）保持正常 Unicode 字母，未用 TeX 重音命令。
- 补空格 / 补句点 7 处（按任务书第 1、2 条）：`F. Akman.A` → `F. Akman. A`、`I.Mirković` → `I. Mirković`、`K.Vilonen` → `K. Vilonen`、`J.L.Verdier` → `J. L. Verdier`、`Amer.Math.Society` → `Amer. Math. Society`、`Trans.Amer.Math.Soc.` → `Trans. Amer. Math. Soc.`、`[KS]` 的 `vol 176` → `vol. 176`。
- 删掉粘在 `[Yet]` 末尾的非文献内容：`MASSACHUSETTS INSTITUTE OF TECHNOLOGY, CAMBRIDGE, MA 02139 / Current address: … / E-mail address: sasha@.mit.edu`（书末作者地址块）。

## 三处需要 lead 拍板的技术决定

1. **`style=nextline` 已删除**。ctex 与 enumitem 的 `nextline` 机制不兼容，本机实测（MiKTeX + XeLaTeX + ctex）报
   `! Argument of \enit@postlabel@i has an extra }.` / `! Paragraph ended before \enit@postlabel@i was complete.`，
   每一条 `\item` 都报；`article` + `enumitem` 无 ctex 时正常，`article` + ctex 必现。此外原书 p.381–386 的 `[键]` 本就与正文**同行**、只是左外悬挂缩进，`nextline` 反而与原书版式不符。现行为
   `\begin{description}[leftmargin=3.2em,itemsep=2pt]`（其余选项、环境、`\end{description}` 都在）。
2. **`\bdsection` 未定义**。全工程只有 `\bdsec`（`源码/main.tex:25`），`\bdsection` 除 `refs.tex:5` 外无任何定义；直接 `\input` 会报 Undefined control sequence。为让本文件「可直接编译」，在文件顶部加了带保护的定义
   `\@ifundefined{bdsection}{\NewDocumentCommand{\bdsection}{s o m}{\section*{#3}}}{}`；
   导言区日后若定义了 `\bdsection`，这段自动失效。结构行 `\bdsection*{参考文献}` 原样保留。
3. **`main.tex` 目前没接 `refs.tex`**：`源码/main.tex:60` 是 `\input{chapters/refs}`，而 `源码/chapters/refs.tex` 只是空壳（`\begin{thebibliography}{99}\end{thebibliography}`）。因此任务书要求的 `xelatex main.tex` 能过，但**并没有编到 `refs.tex`**。要真正用上，需把该行改成 `\input{refs}`（或把内容并入 `chapters/refs.tex`）。这两个文件我都没动。

## 渲染层的两个坑（已解决，只改写法不改内容）

- **en dash 被排成全角**：`ctex/xeCJK` 把 U+2013 判给宋体，PDF 里实测该字符的字体是 `SimSun`、宽 10.91pt，看起来是「262 – 311」这种左右带缝的短横。已把 79 处 `–` 全部改写成 LaTeX 的 `--`，现在由 `TeXGyreTermesX-Regular` 排、宽 5.45pt，与正文一致。
- **弯引号同理**：`’ “ ”` 也被排成全角（`Hitchin’ s` 这种）。已改成 ASCII：`’`→`'`，`“”`→`` ``…'' ``。改后 `Hitchin's`、`Rozenfel'd`、`Gel'fand`、`det`/`div`、`Topology '90` 全部正常。
- 文件内已无 U+2013/2014/2018/2019/201C/201D，只剩 é è ö à ä ô ć 这类正常字母。

## 原书本身的笔误与存疑（需人工确认）

| 页 | 键 | 原文 | 问题 | 我的处理 |
| --- | --- | --- | --- | --- |
| p.381 | [Ak] | `F. Akman.A characterization` | 缺空格（原书如此） | 已按指令补空格 |
| p.384 | [IM] | `Bruhat decompositiopns` | 多一个字母（原书如此） | 保留，建议订正为 `decompositions` |
| p.385 | [R] | `general Lie algbras` | 少字母（原书如此） | 保留，建议订正为 `algebras` |
| p.382 | [D71] | `La géometrie des groupes classiques` | 原书 `o` 上无重音（法语应为 `géométrie`） | 保留 |
| p.384 | [Kac97] | `Amer.Math.Society` | 缺空格 | 已补为 `Amer. Math. Society` |
| p.385 | [R] | `Trans.Amer.Math.Soc.` | 缺空格 | 已补为 `Trans. Amer. Math. Soc.` |
| p.385 | [KS] | `vol 176 (1987), 49–113` | `vol` 缺句点 | 已补为 `vol. 176` |
| p.384 | [Kap97] | `… spaces of local systems Preprint alg-geom/9710027.` | `systems` 后缺句点 | 保留原样，建议补句点 |
| p.381/382 | [BR]、[F84] | 条末 `… 103–138)` / `… 195–196)` | 整条无句末句点 | 保留（原文如此） |
| p.382/385/386 | [GD78]、[Lu83]、[Se] | `pp. 3-24`、`101-102`、`208-229`、`531-543` | 用短连字符而非 en dash | 保留（原文如此，未擅自统一） |
| p.386 | [Phys] | `L. O’Raifertaigh` | 通行拼写为 `O'Raifeartaigh` | 保留（人名不改） |
| p.386 | [T]/[Ve] | `[T]` 行末粘着 `[Ve]` 全条 | 脚本并条，非原书问题 | 已拆开 |

## 与原书版式的差异（有意为之）

- 原书刊名斜体极不一致：`Journal of Algebra`、`Annals of Math.`、`Illinois J. of Math.`、`Comptes Rendus`、`International Mathematics Research Notices`、`Commun. Math. Phys.`、`Journal of Amer. Math. Soc.`、`Russian Math. Surveys`、`Soviet Math. Doklady`、`Inventiones Math.`、`Annals of Physics`、`Publications Mathématiques IHES` 等均排**正体**；只有 `Ann. Sci. École Norm. Sup.`、`Duke Math. Jour.`、`Journal of Algebraic Geometry`、`Lecture Notes in Mathematics`、`Hodge Cycles…`、`Ergebnisse…`、`Astérisque` 等排斜体。按任务书第 3 条及其示例 `\emph{Journal of Algebra}`，已**统一**给所有书名/刊名/丛书名加 `\emph`；卷号、年份、页码未加斜体。
- `leftmargin=3.2em` 的悬挂缩进与条目间距 `itemsep=2pt` 保持脚本原设定。

## 自检结果

- `grep -c '\\item' refs.tex` = **89**（任务书写 88；差 1 即 `[Ve]`，理由见上，未增删任何真实条目）。
- `grep -n ' - \| , \| \. ' refs.tex` → **无输出**（exit 1）。
- 编码：UTF-8 **无 BOM**、CR 计数 0（全 LF）、无行尾空格、末行有换行；一条文献一行（89 行 `\item`，无跨行条目）。
- 结构保留：首行注释、`\bdsection*{参考文献}`、`\begin{description}[…]`、`\end{description}` 均在。
- 编译验证（三次）：
  1. `源码` 下 `xelatex -interaction=nonstopmode main.tex` → exit 0、**0 error**、41 页（但走的是 `chapters/refs` 空壳，见上）；
  2. 用 `main.tex` 的真实导言区单独 `\input{refs}`（测试文件 `C:\tmp\refscheck\integ\main_refs.tex`）→ exit 0、**0 error、0 Overfull**、5 页；
  3. 另用 `elegantbook` + `ctex` 的最小文档（不定义 `\bdsection`）验证文件自足 → exit 0、0 error。
- 目视检查：五次编译产物转 150 dpi PNG 逐页看过（`C:\tmp\refscheck\fin2-1.png`、`fin-2.png`、`p3v4-3.png`、`fin-4.png`、`fin2-5.png`）。fraktur `𝔤`/`𝔭`、`[J]` 的 `$\lim\limits_{\longleftarrow}{}^{(i)}$`、`[Ve]` 的 `SGA 4½`、en dash、引号、斜体书名均正常。
- 编译产物按任务要求**未删也未提交**，`源码/main.pdf`、`main.aux` 等仍在原处（`main.pdf` 由本次自检重新生成，41 页）。

## 未做 / 受限

- 只写了 `源码/refs.tex` 与 `工程文件/reports/refs_u01.md` 两个文件；`main.tex`、`chapters/refs.tex`、`elegantbook.cls` 一字未动。
- 未引入 `\cite`/`thebibliography` 机制（与原书一致，正文用 `[键]` 字面引用）。
- 未加任何中文译注或术语说明（参考文献不翻译标题）。
