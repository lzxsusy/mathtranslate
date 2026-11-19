# log_ch14 —— 第 14 章《导出代数几何》校订记录

- 对象：`src/chapters/ch14.tex`（改前 363 行，改后 388 行）；英文原文 `en/ch14_en.txt`（434 行，`<<< p.NNN >>>` 为 PDF 页码）；页面图 `pages/p-242.png` … `pages/p-250.png`。
- 范围：原 PDF pp.242–250（9 页），3 节 5 小节（14.1.1–14.1.4、14.2.1），43 个编号公式，1 张表（Table 14.1），2 个图片式记号（`\diagram{p243_d1.png}`、`\includegraphics{p244_d1.png}`，文件均在 `src/figures/inline/`）。
- 方式：9 页页面图逐页开图，EN 与 CN 逐段对齐通读；43 个 `\tag{}` 逐符号核对。**结论：全章未发现漏译、增译或符号错置**（详见 §一）。

## 一、结构与编号核对（无失配）

- 公式：(14.1)–(14.43) 共 43 个，序列完整、无缺号、无重号，与 EN 的 43 个逐一对应；(14.29)(14.43) 内的分式、`\PP_n`、`T^{*}[1]`、`\wedge^{\bullet}\Omega_M[n]` 与印本一致。
- 节结构：14.1 拓扑场论与 $\mathbb{E}_n$-代数（14.1.1 局部算子上的 $\mathbb{E}_n$-代数结构、14.1.2 $\mathbb{E}_n$-代数的来源、14.1.3 可加性、14.1.4 范畴表现）／14.2 Hochschild 上同调（14.2.1 Gerstenhaber 代数）／14.3 量子化，与 EN 完全对应。
- 定理/例/注编号：定理 14、定理 15、Remark 99／100／101、例 94–104 与印本逐一一致（含原书 Rem 99 在例 94 之前的跳号）。
- 表 14.1：4×4 表，单元格（$\mathbb{E}_1$-algebra／$\mathbb{E}_1$-category／$\mathbb{E}_1$ 2-category／$\mathbb{E}_2$-algebra／$\mathbb{E}_2$-category (BTC)／$\mathbb{E}_3$-algebra）与印本逐格一致；表题中的「BTC = braided tensor category」译出。
- 关键公式复核：(14.10) 的图形参数（`p244_d1.png` 即原书那个「方框套圆」的图）；(14.16) 的嵌套下标；(14.20) $\mathrm{HH}^*(A)=\End_{A\text{-}\mathbf{mod}\text{-}A}(A)$；(14.26) $P_n=H_*(\mathbb{E}_n)$；(14.30) HKR 同构；(14.35) $\mathrm{Comm}\to\mathbb{E}_n\to\mathrm{Lie}[1-n]$；(14.36) 三角形图；(14.39) $\cB_X(S^1)=\mathrm{HH}^*(R)\simeq\wedge^{\bullet}T_X$；(14.40) $\cM_{\cB_X}=\Spec\cB_X(S^1)=T^{*}[1]X$；(14.43) $\wedge^{\bullet}T_M=\mathrm{HH}^{*}$、$\wedge^{\bullet}\Omega_M[n]=\mathrm{HH}_{*}$。
- 区分 $\mathrm{HH}_*$ 与 $\mathrm{HH}^{*}$ 处（p.249「dim = Tr(id)」一段）原文即已区分上下星，译文照此，未混。引用形式 `[PTVV13, CPT$^+$17]` 与原书页边批注一致（bibliography 里对应 `[PTVV13]`、`[CPT+17]`）。

## 二、实质改动（1 处，P2）

**P2 — 定理 15 标题中的人名拼写（现 CN 270 行）。**

- 原书 p.246 印作「Hochschild-Konstant-Rosenburg」。已知点里记录的是 Rosenburg→Rosenberg（译文已改），但同一行里的 **Konstant** 也是错拼（正确为 Bertram **Kostant**），且与本译本第 15 章「Hochschild--Kostant--Rosenberg」不一致。
- 改为：`\begin{srcthm}{15（Hochschild–Kostant–Rosenberg（HKR））}`。
- 随后加注说明（现 276–281 行），注中给出处 `[来源：Hochschild--Kostant--Rosenberg《Differential forms on regular affine algebras》，Trans. Amer. Math. Soc. 102 (1962)]`。

## 三、新增注释（5 条）

1. **首段末（现 19–23 行）**：p.241 原文「$Z(S^{2})^{\otimes 2}\to Z(S^{1})$」疑为笔误——$\Sigma$ 是 $S^{1}\sqcup S^{1}\to S^{1}$ 的配边，$\Hom$ 里应是 $Z(S^{1})^{\otimes 2}$，紧接的 (14.1)(14.2) 也写作 $Z(S^{1})^{\otimes 2}$。译文照印本保留 $S^{2}$（按规程不改与印本不同的数学），仅加注。`[译者按（无外部依据）：由同段 (14.1) 的内部一致性判定]`
2. **(14.3) 之后（现 36–41 行）**：(14.1)–(14.3) 是同一件事的三种说法；$Z$ 在配边模空间上局部常值 ⇒ 局部常值链复形，故 (14.2) 写成 $\Hom(\cdots)\otimes C^{*}(M)$，再用张量–$\Hom$ 伴随搬到另一侧即 (14.3)。并指出原书 (14.2) 用上标 $C^{*}$、(14.3) 用下标 $C_{*}$，指同一链复形，译文照原文未统一。`[译者按（无外部依据）：由 (14.1)--(14.4) 的内部一致性判定]`
3 **「算子代数」（operad）处（现 79–83 行）**：本章「算子代数」是 operad（May 的小 $n$ 圆盘 operad）的译名，与泛函分析里的 operator algebra 无关；第 11、15 章同语境直接写英文 operad，本仓库资料卡作「操作子」，三种写法尚未统一。`[来源：本仓库资料卡 functoriality/concept/operad]`
4. **Deligne 猜想处（现 206–209 行）**：Deligne 猜想（$\mathrm{HH}^{*}(A)$ 上的 $\mathbb{E}_2$ 结构）已是定理（McClure–Smith 证明）；书里说它是 Dunn–Lurie 可加性的「平凡推论」是指在 $\mathbb{E}_n$ 框架就位后这一步形式化。`[来源：McClure--Smith《A solution of Deligne's Hochschild cohomology conjecture》，Contemp. Math. 293 (2002)]`
5. **定理 15 之后（现 276–281 行）**：见 §二。

## 四、P3（只记录，不改正文）

1. **导读块与正文自相矛盾（只记不改）**：`keytakeaways`（CN 4 行）说「取上同调后 $\mathbb{E}_n$ 退化为 $\PP_n$-代数：$n=1$ 是普通结合代数」，而正文 Example 98 明说「$\mathbb{P}_1$-代数就是普通 Poisson 代数」，Example 99/正文又说 $\PP_3$ 是括号次数 $-2$ 的 Poisson 代数——按正文，$n=1$ 应是普通 Poisson 代数（括号次数 0），不是结合代数。导读块不许改，提请 lead 定夺。
2. **「切触结构」= tangential structure**（CN 347 行）：中文「切触」是 contact（切触几何）的标准译名，tangential structure 宜作「切向结构／切丛结构」。但全书一致如此：`ch10.tex:1106`（`\term{切触结构}{tangential structure}`）、`ch15.tex:242`（「警告 2」）、`ch14.tex:4`（keytakeaways）。属全书术语决定，不宜在本章单改。
3. `[,]_{SN}`（CN 263 行附近）：原书 (14.29) 前后只写 $\{\,\}=[\,]$，译本给括号加了 SN 下标；紧接的句子已点名 Schouten–Nijenhuis，语义无误，只是多一个原文没有的下标。
4. (14.2) 用 $C^{*}(M)$、(14.3) 用 $C_{*}(M)$：原书不统一（已加注说明，未改）。
5. (14.16) 原书用嵌套下标 $1_{1_{._{.}}}$，译本线性化为 $1_{1\cdots1}$（既有注已说明，共 5 个 1）。
6. $\PP_n$ 与 $P_n$：原书 p.246 印 $P_n$（如 $P_n=H_*(\mathbb{E}_n)$、a $P_n$-algebra）、p.247 起印黑板的 $\mathbb{P}_n$，混用；译本统一为 `\PP_n`。
7. 表 14.1 用 `tabular` 重排（原书是排版表，`table14-1.png` 仅存图，译本正文件内有注说明）。
8. (14.36) 原图（p.247）实际是「Comm 与 Assoc 并列、二者之间**没有**箭头」＋「Assoc→Lie 的 $[\,]$」＋「Lie 弯回 Assoc 的 $U$」；译本线性化为 $\mathrm{Comm}\xleftarrow{\ }\mathrm{Assoc}\xrightarrow{[\,]}\mathrm{Lie}$ 并单列 $U:\mathrm{Lie}\to\mathrm{Assoc}$，既有注已交代，语义比原图更清楚。

## 五、存疑待裁定

1. keytakeaways 的「$n=1$ 是普通结合代数」与正文 Example 98 矛盾（见 §四.1）——导读块禁改，需 lead 决定是否统一。
2. operad 的译名（「算子代数」／英文 `operad`／「操作子」）跨章不统一，且「算子代数」与全书大量出现的「局部算子代数」撞车；本章只加注未改词，建议全书统一（资料卡作「操作子」）。
3. 「切触结构」是否全书改为「切向结构」（见 §四.2），涉及 ch10/ch14/ch15，非本章可定。
4. 已知点复核：Thm 15「Hochschild-Konstant-Rosenburg」——「Rosenburg→Rosenberg」早已改对；本次补改同一行的「Konstant→Kostant」（原书两处都拼错）。

## 六、自检（规程 §7）

- `\begin{` / `\end{`：65 / 65；非注释区 `$` 计数 590（偶数）。
- `\label` 10 个，无重复；本章无 `\ref`（对表 14.1 的指向用文字「表 14.1」）；`\label{tab:14-1}` 与 `ch:14`/`sec:*` 均唯一。
- 本次改动 6 处，均可用 `grep` 定位：`Kostant–Rosenberg（HKR）`（270 行）、`上一段末尾的 $Z(S^{2})`（19 行）、`(14.1)--(14.3) 是同一件事`（36 行）、`上文“算子代数”是 operad`（79 行）、`Deligne 猜想（`（206 行）、`定理名的三位作者`（276 行）。
- 未改动：`keytakeaways`、`sectionkey`、既有 9 条 `[Tutor Note]` 正文、图文件、preamble、其它章；未编译（约定由 lead 统一编译）。
