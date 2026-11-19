# log_ch13 —— 第 13 章《Langlands 对应》校订记录

- 对象：`src/chapters/ch13.tex`（校前 802 行 / 62935 字节，校后 805 行 / 64090 字节）；英文 `en/ch13_en.txt`（1099 行，`<<< p.NNN >>>` 为 PDF 页码）；页面图 `pages/p-222.png` … `pages/p-241.png`。
- 范围：原 PDF pp.222–241（印刷 pp.221–240）。13.1 几何 Satake｜13.2 函数域上的非分歧 Langlands 对应｜13.3 分歧 Langlands 对应（13.3.1 自守侧、13.3.2 谱侧）｜13.4 $L$-函数｜13.5 整体 Langlands｜13.6 局部 Langlands 对应（13.6.1 一般形态、13.6.2 局部范畴、13.6.3 谱侧、13.6.4 完整/范畴化）。123 个编号公式、Remark 89–98、Example 90–93、定理 13、问题 8/9/10、既有注释 29 条。
- 方式：英文全文 + 中文全文各通读一遍逐段对齐；123 个公式逐个开页面图核对符号/上下标/箭头方向，关键处用 Python 裁切 3–5 倍放大复读；已知原文缺陷 4 项复核；改动只用 `edit` 精确替换。

## 一、结构与编号核对

- 公式编号：CN 共 123 个 `\tag{13.k}`，序列 13.1–13.123 连续、无重号、无缺号，与 EN 一一对应，**无编号失配**。
- 节结构：6 节 6 小节的标题与 EN 完全对应；Remark 89–98、Example 90–93、定理 13、问题 8/9/10 顺序齐全。
- 逐段核对：EN 每一段都能在 CN 找到对应句，**未发现整段/整句漏译，也未发现原文没有的增译**。
- 图 (13.100)：`p238_d1.png`、`p238_d2.png` 在 `src/figures/inline/`，由 `src/preamble.tex:72` 的 `\graphicspath` 解析，`src/main.log:1856-1859` 记录两图已载入；与 p.238 原图（三球 + $\sqcup_{S^1}$）一致，(13.101) 紧随其后。

## 二、已知原文缺陷复核（4 项，均已在旧注中处理，不重复报告）

| 位置 | 已知缺陷 | 复核结果 |
|---|---|---|
| p.222 正文 | $S^2\times S^2$ 应为 $S^2\times S^1$ | CN 按上下文取 $S^2\times S^1$，旧注 `ch13.tex:28` 已标明；与 (13.2) 左端一致 ✓ |
| (13.21) | $\prod_{x\in S}$ 应为 $\prod_{x\notin S}$ | CN `ch13.tex:163` 照译，旧注 `ch13.tex:165` 已标明；(13.22) 印作 $\prod_{x\notin S}G(\cO_x)\times\prod_{x\in S}K_x$，正确 ✓ |
| (13.90)(13.91) | 右端第二个 $\prod$ 缺指标 | 页面图 p.236 放大确认原书即无下标；CN `ch13.tex:583`（`\Big/\prod\times H`）、`ch13.tex:587`（`\Big/\prod`）照译，旧注 `ch13.tex:590` 已标明 ✓ |
| (13.107) | character→cocharacter lattice | 页面图 p.239 放大确认原文印 "character lattice"；CN `ch13.tex:714` 照译“特征格”，旧注 `ch13.tex:719` 已说明 $T(K)/T(\cO)$ 自然是余特征格、而 $\Lambda\text{-}\mathbf{mod}\simeq\QC(T^\vee)$ 需要特征格 ✓ |

## 三、P1/P2 改动（7 处）

| 位置（改后行号） | 类别 | 原文 | 原译 | 改为 | 理由 | 依据 |
|---|---|---|---|---|---|---|
| `ch13.tex:27` | P1 对象错位 | "but now it's just a vector space of representations" | 但现在它只是一个表示空间。 | 但现在它只是一个由表示构成的向量空间。 | 中文“表示空间”专指 $G$ 在其上作用的 $V$（representation space），而原文说的是“由表示构成的向量空间”（即 $K_0$ 层面的表示环），两者是不同对象。 | 页面图 p.222 该段末行 |
| `ch13.tex:159` | P1 指代错位 | "where $S$ is a finite subset of $C$, which consists of bundles equipped with some extra structure at the points in $S$" | 其中 $S$ 是 $C$ 的有限子集，它由在 $S$ 中各点处带有某些额外结构的丛构成。 | 其中 $S$ 是 $C$ 的有限子集；而 $\Bun_G(C,S)$ 由在 $S$ 中各点处带有某些额外结构的丛构成。 | 关系从句 which 的先行词是 $\Bun_G(C,S)$（(13.20) 的记号），不是子集 $S$；原译把“由丛构成”的主语错置为 $S$。 | 页面图 p.225 段首与 (13.20)–(13.22) |
| `ch13.tex:372` | P1 修饰对象 | "a version of (the reciprocal of) the characteristic polynomial of the Hecke eigenvalue" | Hecke 特征值（的倒数）特征多项式的一个版本 | Hecke 特征值的特征多项式（的倒数）的一个版本 | “倒数”修饰的是特征多项式整体（(13.47)(13.52)(13.53) 均为 $1/\det$），原译把它挂在“特征值”上，会被读成对算子取逆。 | 页面图 p.231 该句 + (13.47)(13.53) |
| `ch13.tex:703` | P2 记号 | $\cA_G(S^1)=\mathbf{Rep}_{\mathrm{cat}}(G(K))$（小写 cat） | `\Rep_{\mathrm{Cat}}(G(K))` | `\Rep_{\mathrm{cat}}(G(K))` | 原书下标为小写 cat；全仓库仅此一处写作大写，属记号漂移。 | 页面图 p.239 (13.106) 5 倍放大 |
| `ch13.tex:722` | P1 指标缺失 | "Consider unramified local systems: $\Loc^{\mathrm{unram}}_{T^\vee}$" | 考虑非分歧局部系统：$\Loc^{\mathrm{unram}}$ | 考虑非分歧局部系统：$\Loc^{\mathrm{unram}}_{T^\vee}$ | 原文与 (13.109)(13.110) 均带对偶环面下标；漏下标后与紧接着的“通过 Frobenius 分解”说不通。 | 页面图 p.239 该段与 (13.109) |
| `ch13.tex:74` | P2 术语跨章 | "spherical Hecke algebra" | 球面 Hecke 代数 | 球 Hecke 代数 | 同一英文术语全书两种译名：`src/chapters/ch10.tex:1755` 以 `\term{球 Hecke 范畴}{spherical Hecke category}` 立名、`src/chapters/ch12.tex:638/641/655` 均作“球 Hecke”，本章 2 处独用“球面”。 | `src/chapters/ch10.tex:1755`、`src/chapters/ch12.tex:638` |
| `ch13.tex:642` | P2 术语跨章 | 同上 | 球面 Hecke 代数 | 球 Hecke 代数 | 同上（同一节内统一）。 | 同上 |

说明：7 条“改为”串均已 `grep -F` 落地核验（命中数 1/1/1/1/1/2）。

## 四、新增注释（3 条，均为 `[来源：译者按（无外部依据）]`）

1. `ch13.tex:197`（rem91 段后，p.226）：源文写“product over $x\in S$ of $G(K)/G(\cO)$”，与同一句开头的“Away from $S$”、紧接着的“for $x\notin S$”以及 (13.27) 自相矛盾，应为 $\prod_{x\notin S}G(K_x)/G(\cO_x)$；按“照译 + 标明”处理。该处属源文（现场笔记）自身的笔误，无外部文献可引，故用译者按标签。
2. `ch13.tex:320`（(13.41) 旧注之后，p.229）：(13.39) 的 $\mathrm{Hecke}$ 与 (13.40)(13.41) 的 $\mathcal{H}\mathrm{ecke}$ 是同一整体 Hecke 代数的两种排版（p.229 放大确认：前者直立 H，后者花体 $\mathcal{H}$），不是两个环，以免读者误以为换了对象。
3. `ch13.tex:738`（(13.111) 之后，p.240）：该式左下角 $\Lambda\text{-}\mathbf{mod}\otimes\Rep(T)$ 的 $\Rep(T)$ 疑为 $\Rep(T^\vee)$ 之笔误——右端是对偶环面的商栈 $T^\vee/T^\vee$，且 (13.112) 把 $\Rep(T^\vee)$ 等同于 $\QC(\mathrm{pt}/T^\vee)$，故“稳定化子修正”张量进来的应是对偶环面的表示范畴。原文照印，译文照译并标明。

既有的 29 条注释一字未改、未删。

## 五、P3（只记录，不改）

1. `ch13.tex:211` (13.29) 译文用 `\twoheadrightarrow`，原书为 $\to$；语义无别。
2. `ch13.tex:657` 正文里夹了译者夹注“（原文此处为示意图…）”——这是译文自身的增补，不是原文文字；位置在 (13.100) 图前，不影响数学，未动。
3. `ch13.tex:792` “Kottwitz $G$-同晶（isocrystal）”：中文“同晶”不是通行译名（通常作“同晶体”/“晶体”）；`src/appendix_glossary.tex` 无此条，改则牵动全书，只记录。
4. 素理想记号：原书局部用斜体 $p$（如 (13.53) 的 $F_p$），译文全书统一用 $\mathfrak p$，与 `src/chapters/ch05.tex:92` 的用法一致；属全书记号归一，不改。
5. `ch13.tex:583` (13.90) 用 $K_p$、`ch13.tex:587` (13.91) 用 $K_{\mathfrak p}$：原书两式本身就一个用 $p$、一个用 $\mathfrak p$，译文逐式照应，未动。

## 六、GAP

- 本章 **0 条**。疑难处（(13.111) 的 $\Rep(T)$、rem91 的 $x\in S$、(13.90)(13.91) 缺指标、(13.107) 的 character lattice）都能用页面图确定“原文确实如此印”，属于原文笔误而非“原文含义不可确定”，按“照译 + 加注”处理，不标 GAP。
- 未出现需要查外部文献才能读懂的术语；`src/appendix_glossary.tex` 已覆盖本章主要术语（eigenfunction、isocrystal、cocharacter 无条目，但对应中文为通行译名，无需注释）。

## 七、存疑待裁定

1. **`ch13.tex:31` 旧注对 (13.1) 中 `*` 的解释**：旧注称 `*` 是“线性对偶”。但 p.222 原书排版为 $(\cA_G(S^2),*)$，而几何 Satake 是把 $(\cA_G(S^2),*)$ 与 $\Rep(G^\vee)$ 作**幺半**等价，“$*$”更像卷积乘法的记号（如 $(C,*)$ 记带张量结构的范畴）。因规程不许删改既有注释、又不便插入一条自相矛盾的注释，此处未动，请 lead 裁定是否改写旧注。
2. （已解决，供 lead 归档）`log_ch12.md` 提出的「球 Hecke」vs「球面 Hecke」跨章不一致：本章 2 处已统一为“球 Hecke 代数”，与 ch10/ch12 一致，全书该项可关闭。

## 八、收尾自检（规程 §7）

- `\begin` 153 / `\end` 153，相等。
- `$` 共 1170 个，偶数。
- `\label` 13 个（`ch:13`、`sec:13-1`…`sec:13-6`、`sec:13-3-1/2`、`sec:13-6-1`…`sec:13-6-4`），无重复。
- `\ref`/`\eqref`：本章内 0 处；全书其它文件指向本章 label 的引用也是 0 处 → 无悬空引用（不存在解析失败的可能）。
- `\tag` 123 个，13.1–13.123 连续无缺。
- `% [Tutor Note:` 32 条（29 既有 + 3 新增），全部以 `]]` 闭合；`% [GAP:` 0 条。
- 未改 `keytakeaways` / `sectionkey` 任何文字；未改既有注释文字；未编译（按分工由 lead 统一编译）。
- 改动文件仅 `src/chapters/ch13.tex`，新增文件仅 `logs/log_ch13.md`。
